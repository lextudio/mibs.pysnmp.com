# SNMP MIB module (DECHUB900-COMMON-MIB-V3-0) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DECHUB900-COMMON-MIB-V3-0
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:39 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dec_ObjectIdentity = ObjectIdentity
dec = _Dec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36)
)
_Ema_ObjectIdentity = ObjectIdentity
ema = _Ema_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2)
)
_DecMIBextension_ObjectIdentity = ObjectIdentity
decMIBextension = _DecMIBextension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18)
)
_DecHub900_ObjectIdentity = ObjectIdentity
decHub900 = _DecHub900_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11)
)
_PubCommon_ObjectIdentity = ObjectIdentity
pubCommon = _PubCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2)
)
_PcomSlot_ObjectIdentity = ObjectIdentity
pcomSlot = _PcomSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 1)
)


class _PcomOperStatus_Type(Integer32):
    """Custom type pcomOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 6),
          ("enabled", 1),
          ("failure", 3),
          ("initializing", 2),
          ("loading", 5),
          ("lowPowerMode", 9),
          ("needProgramLoad", 7),
          ("nonFatalFailure", 4),
          ("testing", 8))
    )


_PcomOperStatus_Type.__name__ = "Integer32"
_PcomOperStatus_Object = MibScalar
pcomOperStatus = _PcomOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 1, 1),
    _PcomOperStatus_Type()
)
pcomOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomOperStatus.setStatus("mandatory")


class _PcomAdminStatus_Type(Integer32):
    """Custom type pcomAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("reset", 3),
          ("restoreToDefaults", 4))
    )


_PcomAdminStatus_Type.__name__ = "Integer32"
_PcomAdminStatus_Object = MibScalar
pcomAdminStatus = _PcomAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 1, 2),
    _PcomAdminStatus_Type()
)
pcomAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcomAdminStatus.setStatus("mandatory")


class _PcomDiagFailure_Type(Integer32):
    """Custom type pcomDiagFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PcomDiagFailure_Type.__name__ = "Integer32"
_PcomDiagFailure_Object = MibScalar
pcomDiagFailure = _PcomDiagFailure_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 1, 3),
    _PcomDiagFailure_Type()
)
pcomDiagFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomDiagFailure.setStatus("mandatory")


class _PcomSerialNumber_Type(DisplayString):
    """Custom type pcomSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PcomSerialNumber_Type.__name__ = "DisplayString"
_PcomSerialNumber_Object = MibScalar
pcomSerialNumber = _PcomSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 1, 4),
    _PcomSerialNumber_Type()
)
pcomSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcomSerialNumber.setStatus("mandatory")


class _PcomSlotNumber_Type(Integer32):
    """Custom type pcomSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_PcomSlotNumber_Type.__name__ = "Integer32"
_PcomSlotNumber_Object = MibScalar
pcomSlotNumber = _PcomSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 1, 5),
    _PcomSlotNumber_Type()
)
pcomSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomSlotNumber.setStatus("mandatory")


class _PcomEsn_Type(Integer32):
    """Custom type pcomEsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_PcomEsn_Type.__name__ = "Integer32"
_PcomEsn_Object = MibScalar
pcomEsn = _PcomEsn_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 1, 6),
    _PcomEsn_Type()
)
pcomEsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomEsn.setStatus("mandatory")
_PcomHub_ObjectIdentity = ObjectIdentity
pcomHub = _PcomHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 2)
)


class _PcomHubId_Type(OctetString):
    """Custom type pcomHubId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_PcomHubId_Type.__name__ = "OctetString"
_PcomHubId_Object = MibScalar
pcomHubId = _PcomHubId_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 2, 1),
    _PcomHubId_Type()
)
pcomHubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomHubId.setStatus("deprecated")
_PcomHubIpAddress_Type = IpAddress
_PcomHubIpAddress_Object = MibScalar
pcomHubIpAddress = _PcomHubIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 2, 2),
    _PcomHubIpAddress_Type()
)
pcomHubIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomHubIpAddress.setStatus("mandatory")


class _PcomHubCommunity_Type(OctetString):
    """Custom type pcomHubCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PcomHubCommunity_Type.__name__ = "OctetString"
_PcomHubCommunity_Object = MibScalar
pcomHubCommunity = _PcomHubCommunity_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 2, 3),
    _PcomHubCommunity_Type()
)
pcomHubCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomHubCommunity.setStatus("mandatory")
_PcomLed_ObjectIdentity = ObjectIdentity
pcomLed = _PcomLed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 3)
)
_PcomLedTable_Object = MibTable
pcomLedTable = _PcomLedTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 3, 1)
)
if mibBuilder.loadTexts:
    pcomLedTable.setStatus("mandatory")
_PcomLedEntry_Object = MibTableRow
pcomLedEntry = _PcomLedEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 3, 1, 1)
)
pcomLedEntry.setIndexNames(
    (0, "DECHUB900-COMMON-MIB-V3-0", "pcomLedIndex"),
)
if mibBuilder.loadTexts:
    pcomLedEntry.setStatus("mandatory")


class _PcomLedIndex_Type(Integer32):
    """Custom type pcomLedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_PcomLedIndex_Type.__name__ = "Integer32"
_PcomLedIndex_Object = MibTableColumn
pcomLedIndex = _PcomLedIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 3, 1, 1, 1),
    _PcomLedIndex_Type()
)
pcomLedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomLedIndex.setStatus("mandatory")


class _PcomLedDescr_Type(DisplayString):
    """Custom type pcomLedDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_PcomLedDescr_Type.__name__ = "DisplayString"
_PcomLedDescr_Object = MibTableColumn
pcomLedDescr = _PcomLedDescr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 3, 1, 1, 2),
    _PcomLedDescr_Type()
)
pcomLedDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomLedDescr.setStatus("mandatory")


class _PcomLedProgram_Type(OctetString):
    """Custom type pcomLedProgram based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_PcomLedProgram_Type.__name__ = "OctetString"
_PcomLedProgram_Object = MibTableColumn
pcomLedProgram = _PcomLedProgram_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 3, 1, 1, 3),
    _PcomLedProgram_Type()
)
pcomLedProgram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomLedProgram.setStatus("mandatory")
_PcomLedInterestingChanges_Type = Counter32
_PcomLedInterestingChanges_Object = MibScalar
pcomLedInterestingChanges = _PcomLedInterestingChanges_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 3, 2),
    _PcomLedInterestingChanges_Type()
)
pcomLedInterestingChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomLedInterestingChanges.setStatus("mandatory")
_PcomLoad_ObjectIdentity = ObjectIdentity
pcomLoad = _PcomLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 4)
)


class _PcomLoadAdminStatus_Type(Integer32):
    """Custom type pcomLoadAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 4),
          ("other", 1),
          ("start-read", 2),
          ("start-write", 3))
    )


_PcomLoadAdminStatus_Type.__name__ = "Integer32"
_PcomLoadAdminStatus_Object = MibScalar
pcomLoadAdminStatus = _PcomLoadAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 4, 1),
    _PcomLoadAdminStatus_Type()
)
pcomLoadAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcomLoadAdminStatus.setStatus("mandatory")


class _PcomLoadOperStatus_Type(Integer32):
    """Custom type pcomLoadOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 3),
          ("none", 1),
          ("success", 2))
    )


_PcomLoadOperStatus_Type.__name__ = "Integer32"
_PcomLoadOperStatus_Object = MibScalar
pcomLoadOperStatus = _PcomLoadOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 4, 2),
    _PcomLoadOperStatus_Type()
)
pcomLoadOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomLoadOperStatus.setStatus("mandatory")


class _PcomLoadFilename_Type(DisplayString):
    """Custom type pcomLoadFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PcomLoadFilename_Type.__name__ = "DisplayString"
_PcomLoadFilename_Object = MibScalar
pcomLoadFilename = _PcomLoadFilename_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 4, 3),
    _PcomLoadFilename_Type()
)
pcomLoadFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcomLoadFilename.setStatus("mandatory")
_PcomLoadIpHostAddr_Type = IpAddress
_PcomLoadIpHostAddr_Object = MibScalar
pcomLoadIpHostAddr = _PcomLoadIpHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 4, 4),
    _PcomLoadIpHostAddr_Type()
)
pcomLoadIpHostAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcomLoadIpHostAddr.setStatus("mandatory")


class _PcomLoadDevSpecific_Type(Integer32):
    """Custom type pcomLoadDevSpecific based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PcomLoadDevSpecific_Type.__name__ = "Integer32"
_PcomLoadDevSpecific_Object = MibScalar
pcomLoadDevSpecific = _PcomLoadDevSpecific_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 4, 5),
    _PcomLoadDevSpecific_Type()
)
pcomLoadDevSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomLoadDevSpecific.setStatus("mandatory")


class _PcomLoadTftpDirection_Type(Integer32):
    """Custom type pcomLoadTftpDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pcomLoadTftpDirectionAckWrite", 1),
          ("pcomLoadTftpDirectionStartRead", 2))
    )


_PcomLoadTftpDirection_Type.__name__ = "Integer32"
_PcomLoadTftpDirection_Object = MibScalar
pcomLoadTftpDirection = _PcomLoadTftpDirection_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 4, 6),
    _PcomLoadTftpDirection_Type()
)
pcomLoadTftpDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomLoadTftpDirection.setStatus("mandatory")
_PcomSnmpAuth_ObjectIdentity = ObjectIdentity
pcomSnmpAuth = _PcomSnmpAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 5)
)
_PcomSnmpAuthTrap_ObjectIdentity = ObjectIdentity
pcomSnmpAuthTrap = _PcomSnmpAuthTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 5, 1)
)


class _PcomSnmpAuthTrapCommunity_Type(OctetString):
    """Custom type pcomSnmpAuthTrapCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 31),
    )


_PcomSnmpAuthTrapCommunity_Type.__name__ = "OctetString"
_PcomSnmpAuthTrapCommunity_Object = MibScalar
pcomSnmpAuthTrapCommunity = _PcomSnmpAuthTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 5, 1, 1),
    _PcomSnmpAuthTrapCommunity_Type()
)
pcomSnmpAuthTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcomSnmpAuthTrapCommunity.setStatus("mandatory")
_PcomSnmpAuthTrapUserTable_Object = MibTable
pcomSnmpAuthTrapUserTable = _PcomSnmpAuthTrapUserTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 5, 1, 2)
)
if mibBuilder.loadTexts:
    pcomSnmpAuthTrapUserTable.setStatus("mandatory")
_PcomSnmpAuthTrapUserEntry_Object = MibTableRow
pcomSnmpAuthTrapUserEntry = _PcomSnmpAuthTrapUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 5, 1, 2, 1)
)
pcomSnmpAuthTrapUserEntry.setIndexNames(
    (0, "DECHUB900-COMMON-MIB-V3-0", "pcomSnmpAuthTrapUserAddr"),
)
if mibBuilder.loadTexts:
    pcomSnmpAuthTrapUserEntry.setStatus("mandatory")
_PcomSnmpAuthTrapUserAddr_Type = IpAddress
_PcomSnmpAuthTrapUserAddr_Object = MibTableColumn
pcomSnmpAuthTrapUserAddr = _PcomSnmpAuthTrapUserAddr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 5, 1, 2, 1, 1),
    _PcomSnmpAuthTrapUserAddr_Type()
)
pcomSnmpAuthTrapUserAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcomSnmpAuthTrapUserAddr.setStatus("mandatory")


class _PcomSnmpAuthTrapUserStatus_Type(Integer32):
    """Custom type pcomSnmpAuthTrapUserStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_PcomSnmpAuthTrapUserStatus_Type.__name__ = "Integer32"
_PcomSnmpAuthTrapUserStatus_Object = MibTableColumn
pcomSnmpAuthTrapUserStatus = _PcomSnmpAuthTrapUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 5, 1, 2, 1, 2),
    _PcomSnmpAuthTrapUserStatus_Type()
)
pcomSnmpAuthTrapUserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcomSnmpAuthTrapUserStatus.setStatus("mandatory")
_PcomSnmpAuthReadOnly_ObjectIdentity = ObjectIdentity
pcomSnmpAuthReadOnly = _PcomSnmpAuthReadOnly_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 5, 2)
)


class _PcomSnmpAuthReadOnlyCommunity_Type(OctetString):
    """Custom type pcomSnmpAuthReadOnlyCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 31),
    )


_PcomSnmpAuthReadOnlyCommunity_Type.__name__ = "OctetString"
_PcomSnmpAuthReadOnlyCommunity_Object = MibScalar
pcomSnmpAuthReadOnlyCommunity = _PcomSnmpAuthReadOnlyCommunity_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 5, 2, 1),
    _PcomSnmpAuthReadOnlyCommunity_Type()
)
pcomSnmpAuthReadOnlyCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcomSnmpAuthReadOnlyCommunity.setStatus("mandatory")
_PcomSnmpAuthReadOnlyUserTable_Object = MibTable
pcomSnmpAuthReadOnlyUserTable = _PcomSnmpAuthReadOnlyUserTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 5, 2, 2)
)
if mibBuilder.loadTexts:
    pcomSnmpAuthReadOnlyUserTable.setStatus("mandatory")
_PcomSnmpAuthReadOnlyUserEntry_Object = MibTableRow
pcomSnmpAuthReadOnlyUserEntry = _PcomSnmpAuthReadOnlyUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 5, 2, 2, 1)
)
pcomSnmpAuthReadOnlyUserEntry.setIndexNames(
    (0, "DECHUB900-COMMON-MIB-V3-0", "pcomSnmpAuthReadOnlyUserAddr"),
)
if mibBuilder.loadTexts:
    pcomSnmpAuthReadOnlyUserEntry.setStatus("mandatory")
_PcomSnmpAuthReadOnlyUserAddr_Type = IpAddress
_PcomSnmpAuthReadOnlyUserAddr_Object = MibTableColumn
pcomSnmpAuthReadOnlyUserAddr = _PcomSnmpAuthReadOnlyUserAddr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 5, 2, 2, 1, 1),
    _PcomSnmpAuthReadOnlyUserAddr_Type()
)
pcomSnmpAuthReadOnlyUserAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcomSnmpAuthReadOnlyUserAddr.setStatus("mandatory")


class _PcomSnmpAuthReadOnlyUserMask_Type(OctetString):
    """Custom type pcomSnmpAuthReadOnlyUserMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_PcomSnmpAuthReadOnlyUserMask_Type.__name__ = "OctetString"
_PcomSnmpAuthReadOnlyUserMask_Object = MibTableColumn
pcomSnmpAuthReadOnlyUserMask = _PcomSnmpAuthReadOnlyUserMask_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 5, 2, 2, 1, 2),
    _PcomSnmpAuthReadOnlyUserMask_Type()
)
pcomSnmpAuthReadOnlyUserMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcomSnmpAuthReadOnlyUserMask.setStatus("mandatory")


class _PcomSnmpAuthReadOnlyUserStatus_Type(Integer32):
    """Custom type pcomSnmpAuthReadOnlyUserStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_PcomSnmpAuthReadOnlyUserStatus_Type.__name__ = "Integer32"
_PcomSnmpAuthReadOnlyUserStatus_Object = MibTableColumn
pcomSnmpAuthReadOnlyUserStatus = _PcomSnmpAuthReadOnlyUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 5, 2, 2, 1, 3),
    _PcomSnmpAuthReadOnlyUserStatus_Type()
)
pcomSnmpAuthReadOnlyUserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcomSnmpAuthReadOnlyUserStatus.setStatus("mandatory")
_PcomSnmpAuthReadWrite_ObjectIdentity = ObjectIdentity
pcomSnmpAuthReadWrite = _PcomSnmpAuthReadWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 5, 3)
)


class _PcomSnmpAuthReadWriteCommunity_Type(OctetString):
    """Custom type pcomSnmpAuthReadWriteCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 31),
    )


_PcomSnmpAuthReadWriteCommunity_Type.__name__ = "OctetString"
_PcomSnmpAuthReadWriteCommunity_Object = MibScalar
pcomSnmpAuthReadWriteCommunity = _PcomSnmpAuthReadWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 5, 3, 1),
    _PcomSnmpAuthReadWriteCommunity_Type()
)
pcomSnmpAuthReadWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcomSnmpAuthReadWriteCommunity.setStatus("mandatory")
_PcomSnmpAuthReadWriteUserTable_Object = MibTable
pcomSnmpAuthReadWriteUserTable = _PcomSnmpAuthReadWriteUserTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 5, 3, 2)
)
if mibBuilder.loadTexts:
    pcomSnmpAuthReadWriteUserTable.setStatus("mandatory")
_PcomSnmpAuthReadWriteUserEntry_Object = MibTableRow
pcomSnmpAuthReadWriteUserEntry = _PcomSnmpAuthReadWriteUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 5, 3, 2, 1)
)
pcomSnmpAuthReadWriteUserEntry.setIndexNames(
    (0, "DECHUB900-COMMON-MIB-V3-0", "pcomSnmpAuthReadWriteUserAddr"),
)
if mibBuilder.loadTexts:
    pcomSnmpAuthReadWriteUserEntry.setStatus("mandatory")
_PcomSnmpAuthReadWriteUserAddr_Type = IpAddress
_PcomSnmpAuthReadWriteUserAddr_Object = MibTableColumn
pcomSnmpAuthReadWriteUserAddr = _PcomSnmpAuthReadWriteUserAddr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 5, 3, 2, 1, 1),
    _PcomSnmpAuthReadWriteUserAddr_Type()
)
pcomSnmpAuthReadWriteUserAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcomSnmpAuthReadWriteUserAddr.setStatus("mandatory")


class _PcomSnmpAuthReadWriteUserMask_Type(OctetString):
    """Custom type pcomSnmpAuthReadWriteUserMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_PcomSnmpAuthReadWriteUserMask_Type.__name__ = "OctetString"
_PcomSnmpAuthReadWriteUserMask_Object = MibTableColumn
pcomSnmpAuthReadWriteUserMask = _PcomSnmpAuthReadWriteUserMask_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 5, 3, 2, 1, 2),
    _PcomSnmpAuthReadWriteUserMask_Type()
)
pcomSnmpAuthReadWriteUserMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcomSnmpAuthReadWriteUserMask.setStatus("mandatory")


class _PcomSnmpAuthReadWriteUserStatus_Type(Integer32):
    """Custom type pcomSnmpAuthReadWriteUserStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_PcomSnmpAuthReadWriteUserStatus_Type.__name__ = "Integer32"
_PcomSnmpAuthReadWriteUserStatus_Object = MibTableColumn
pcomSnmpAuthReadWriteUserStatus = _PcomSnmpAuthReadWriteUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 5, 3, 2, 1, 3),
    _PcomSnmpAuthReadWriteUserStatus_Type()
)
pcomSnmpAuthReadWriteUserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcomSnmpAuthReadWriteUserStatus.setStatus("mandatory")
_PcomSnmpAuthUnauth_ObjectIdentity = ObjectIdentity
pcomSnmpAuthUnauth = _PcomSnmpAuthUnauth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 5, 4)
)
_PcomSnmpAuthUnauthTable_Object = MibTable
pcomSnmpAuthUnauthTable = _PcomSnmpAuthUnauthTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 5, 4, 1)
)
if mibBuilder.loadTexts:
    pcomSnmpAuthUnauthTable.setStatus("mandatory")
_PcomSnmpAuthUnauthEntry_Object = MibTableRow
pcomSnmpAuthUnauthEntry = _PcomSnmpAuthUnauthEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 5, 4, 1, 1)
)
pcomSnmpAuthUnauthEntry.setIndexNames(
    (0, "DECHUB900-COMMON-MIB-V3-0", "pcomSnmpAuthUnauthIndex"),
)
if mibBuilder.loadTexts:
    pcomSnmpAuthUnauthEntry.setStatus("mandatory")


class _PcomSnmpAuthUnauthIndex_Type(Integer32):
    """Custom type pcomSnmpAuthUnauthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PcomSnmpAuthUnauthIndex_Type.__name__ = "Integer32"
_PcomSnmpAuthUnauthIndex_Object = MibTableColumn
pcomSnmpAuthUnauthIndex = _PcomSnmpAuthUnauthIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 5, 4, 1, 1, 1),
    _PcomSnmpAuthUnauthIndex_Type()
)
pcomSnmpAuthUnauthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomSnmpAuthUnauthIndex.setStatus("mandatory")
_PcomSnmpAuthUnauthTimeStamp_Type = TimeTicks
_PcomSnmpAuthUnauthTimeStamp_Object = MibTableColumn
pcomSnmpAuthUnauthTimeStamp = _PcomSnmpAuthUnauthTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 5, 4, 1, 1, 2),
    _PcomSnmpAuthUnauthTimeStamp_Type()
)
pcomSnmpAuthUnauthTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomSnmpAuthUnauthTimeStamp.setStatus("mandatory")
_PcomSnmpAuthUnauthIpAddress_Type = IpAddress
_PcomSnmpAuthUnauthIpAddress_Object = MibTableColumn
pcomSnmpAuthUnauthIpAddress = _PcomSnmpAuthUnauthIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 5, 4, 1, 1, 3),
    _PcomSnmpAuthUnauthIpAddress_Type()
)
pcomSnmpAuthUnauthIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomSnmpAuthUnauthIpAddress.setStatus("mandatory")


class _PcomSnmpAuthUnauthUdpPort_Type(Integer32):
    """Custom type pcomSnmpAuthUnauthUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PcomSnmpAuthUnauthUdpPort_Type.__name__ = "Integer32"
_PcomSnmpAuthUnauthUdpPort_Object = MibTableColumn
pcomSnmpAuthUnauthUdpPort = _PcomSnmpAuthUnauthUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 5, 4, 1, 1, 4),
    _PcomSnmpAuthUnauthUdpPort_Type()
)
pcomSnmpAuthUnauthUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomSnmpAuthUnauthUdpPort.setStatus("mandatory")


class _PcomSnmpAuthUnauthCommunity_Type(OctetString):
    """Custom type pcomSnmpAuthUnauthCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PcomSnmpAuthUnauthCommunity_Type.__name__ = "OctetString"
_PcomSnmpAuthUnauthCommunity_Object = MibTableColumn
pcomSnmpAuthUnauthCommunity = _PcomSnmpAuthUnauthCommunity_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 5, 4, 1, 1, 5),
    _PcomSnmpAuthUnauthCommunity_Type()
)
pcomSnmpAuthUnauthCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomSnmpAuthUnauthCommunity.setStatus("mandatory")


class _PcomSnmpAuthUnauthOperation_Type(Integer32):
    """Custom type pcomSnmpAuthUnauthOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("getNextRequest", 3),
          ("getRequest", 2),
          ("getResponse", 4),
          ("other", 1),
          ("setRequest", 5))
    )


_PcomSnmpAuthUnauthOperation_Type.__name__ = "Integer32"
_PcomSnmpAuthUnauthOperation_Object = MibTableColumn
pcomSnmpAuthUnauthOperation = _PcomSnmpAuthUnauthOperation_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 5, 4, 1, 1, 6),
    _PcomSnmpAuthUnauthOperation_Type()
)
pcomSnmpAuthUnauthOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomSnmpAuthUnauthOperation.setStatus("mandatory")


class _PcomSnmpAuthUnauthReason_Type(Integer32):
    """Custom type pcomSnmpAuthUnauthReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("badComName", 1),
          ("badComUse", 2))
    )


_PcomSnmpAuthUnauthReason_Type.__name__ = "Integer32"
_PcomSnmpAuthUnauthReason_Object = MibTableColumn
pcomSnmpAuthUnauthReason = _PcomSnmpAuthUnauthReason_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 5, 4, 1, 1, 7),
    _PcomSnmpAuthUnauthReason_Type()
)
pcomSnmpAuthUnauthReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomSnmpAuthUnauthReason.setStatus("mandatory")
_PcomErrLog_ObjectIdentity = ObjectIdentity
pcomErrLog = _PcomErrLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 6)
)


class _PcomErrLogNumEntries_Type(Integer32):
    """Custom type pcomErrLogNumEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PcomErrLogNumEntries_Type.__name__ = "Integer32"
_PcomErrLogNumEntries_Object = MibScalar
pcomErrLogNumEntries = _PcomErrLogNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 6, 1),
    _PcomErrLogNumEntries_Type()
)
pcomErrLogNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomErrLogNumEntries.setStatus("mandatory")
_PcomErrLogTable_Object = MibTable
pcomErrLogTable = _PcomErrLogTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 6, 2)
)
if mibBuilder.loadTexts:
    pcomErrLogTable.setStatus("mandatory")
_PcomErrLogEntry_Object = MibTableRow
pcomErrLogEntry = _PcomErrLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 6, 2, 1)
)
pcomErrLogEntry.setIndexNames(
    (0, "DECHUB900-COMMON-MIB-V3-0", "pcomErrLogIndex"),
)
if mibBuilder.loadTexts:
    pcomErrLogEntry.setStatus("mandatory")


class _PcomErrLogIndex_Type(Integer32):
    """Custom type pcomErrLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PcomErrLogIndex_Type.__name__ = "Integer32"
_PcomErrLogIndex_Object = MibTableColumn
pcomErrLogIndex = _PcomErrLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 6, 2, 1, 1),
    _PcomErrLogIndex_Type()
)
pcomErrLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomErrLogIndex.setStatus("mandatory")
_PcomErrLogTimeStamp_Type = TimeTicks
_PcomErrLogTimeStamp_Object = MibTableColumn
pcomErrLogTimeStamp = _PcomErrLogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 6, 2, 1, 2),
    _PcomErrLogTimeStamp_Type()
)
pcomErrLogTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomErrLogTimeStamp.setStatus("mandatory")


class _PcomErrLogResetNumber_Type(Integer32):
    """Custom type pcomErrLogResetNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_PcomErrLogResetNumber_Type.__name__ = "Integer32"
_PcomErrLogResetNumber_Object = MibTableColumn
pcomErrLogResetNumber = _PcomErrLogResetNumber_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 6, 2, 1, 3),
    _PcomErrLogResetNumber_Type()
)
pcomErrLogResetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomErrLogResetNumber.setStatus("mandatory")


class _PcomErrLogInfo_Type(DisplayString):
    """Custom type pcomErrLogInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PcomErrLogInfo_Type.__name__ = "DisplayString"
_PcomErrLogInfo_Object = MibTableColumn
pcomErrLogInfo = _PcomErrLogInfo_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 6, 2, 1, 4),
    _PcomErrLogInfo_Type()
)
pcomErrLogInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomErrLogInfo.setStatus("mandatory")


class _PcomErrLogFwVersion_Type(DisplayString):
    """Custom type pcomErrLogFwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PcomErrLogFwVersion_Type.__name__ = "DisplayString"
_PcomErrLogFwVersion_Object = MibTableColumn
pcomErrLogFwVersion = _PcomErrLogFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 6, 2, 1, 5),
    _PcomErrLogFwVersion_Type()
)
pcomErrLogFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomErrLogFwVersion.setStatus("mandatory")
_PcomEsys_ObjectIdentity = ObjectIdentity
pcomEsys = _PcomEsys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 7)
)
_PcomEsysPowerups_Type = Counter32
_PcomEsysPowerups_Object = MibScalar
pcomEsysPowerups = _PcomEsysPowerups_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 7, 1),
    _PcomEsysPowerups_Type()
)
pcomEsysPowerups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomEsysPowerups.setStatus("mandatory")
_PcomEsysMgmtResets_Type = Counter32
_PcomEsysMgmtResets_Object = MibScalar
pcomEsysMgmtResets = _PcomEsysMgmtResets_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 7, 2),
    _PcomEsysMgmtResets_Type()
)
pcomEsysMgmtResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomEsysMgmtResets.setStatus("mandatory")
_PcomEsysUnsolicitedResets_Type = Counter32
_PcomEsysUnsolicitedResets_Object = MibScalar
pcomEsysUnsolicitedResets = _PcomEsysUnsolicitedResets_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 7, 3),
    _PcomEsysUnsolicitedResets_Type()
)
pcomEsysUnsolicitedResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomEsysUnsolicitedResets.setStatus("mandatory")


class _PcomEsysNVRAMfailedFlag_Type(Integer32):
    """Custom type pcomEsysNVRAMfailedFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_PcomEsysNVRAMfailedFlag_Type.__name__ = "Integer32"
_PcomEsysNVRAMfailedFlag_Object = MibScalar
pcomEsysNVRAMfailedFlag = _PcomEsysNVRAMfailedFlag_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 7, 4),
    _PcomEsysNVRAMfailedFlag_Type()
)
pcomEsysNVRAMfailedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomEsysNVRAMfailedFlag.setStatus("mandatory")


class _PcomEsysNVRAMsize_Type(Integer32):
    """Custom type pcomEsysNVRAMsize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PcomEsysNVRAMsize_Type.__name__ = "Integer32"
_PcomEsysNVRAMsize_Object = MibScalar
pcomEsysNVRAMsize = _PcomEsysNVRAMsize_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 7, 5),
    _PcomEsysNVRAMsize_Type()
)
pcomEsysNVRAMsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomEsysNVRAMsize.setStatus("mandatory")


class _PcomEsysNVRAMavailableOctets_Type(Integer32):
    """Custom type pcomEsysNVRAMavailableOctets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PcomEsysNVRAMavailableOctets_Type.__name__ = "Integer32"
_PcomEsysNVRAMavailableOctets_Object = MibScalar
pcomEsysNVRAMavailableOctets = _PcomEsysNVRAMavailableOctets_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 7, 6),
    _PcomEsysNVRAMavailableOctets_Type()
)
pcomEsysNVRAMavailableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomEsysNVRAMavailableOctets.setStatus("mandatory")


class _PcomEsysHubVersion_Type(DisplayString):
    """Custom type pcomEsysHubVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PcomEsysHubVersion_Type.__name__ = "DisplayString"
_PcomEsysHubVersion_Object = MibScalar
pcomEsysHubVersion = _PcomEsysHubVersion_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 7, 7),
    _PcomEsysHubVersion_Type()
)
pcomEsysHubVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomEsysHubVersion.setStatus("mandatory")
_PcomEif_ObjectIdentity = ObjectIdentity
pcomEif = _PcomEif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 8)
)
_PcomEifTable_Object = MibTable
pcomEifTable = _PcomEifTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 8, 1)
)
if mibBuilder.loadTexts:
    pcomEifTable.setStatus("mandatory")
_PcomEifEntry_Object = MibTableRow
pcomEifEntry = _PcomEifEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 8, 1, 1)
)
pcomEifEntry.setIndexNames(
    (0, "DECHUB900-COMMON-MIB-V3-0", "pcomEifIndex"),
)
if mibBuilder.loadTexts:
    pcomEifEntry.setStatus("mandatory")


class _PcomEifIndex_Type(Integer32):
    """Custom type pcomEifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PcomEifIndex_Type.__name__ = "Integer32"
_PcomEifIndex_Object = MibTableColumn
pcomEifIndex = _PcomEifIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 8, 1, 1, 1),
    _PcomEifIndex_Type()
)
pcomEifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomEifIndex.setStatus("mandatory")
_PcomEifInBroadcastPkts_Type = Counter32
_PcomEifInBroadcastPkts_Object = MibTableColumn
pcomEifInBroadcastPkts = _PcomEifInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 8, 1, 1, 2),
    _PcomEifInBroadcastPkts_Type()
)
pcomEifInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomEifInBroadcastPkts.setStatus("mandatory")
_PcomLigo_ObjectIdentity = ObjectIdentity
pcomLigo = _PcomLigo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 9)
)


class _PcomLigoNumEntries_Type(Integer32):
    """Custom type pcomLigoNumEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PcomLigoNumEntries_Type.__name__ = "Integer32"
_PcomLigoNumEntries_Object = MibScalar
pcomLigoNumEntries = _PcomLigoNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 9, 1),
    _PcomLigoNumEntries_Type()
)
pcomLigoNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomLigoNumEntries.setStatus("mandatory")
_PcomLigoTable_Object = MibTable
pcomLigoTable = _PcomLigoTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 9, 2)
)
if mibBuilder.loadTexts:
    pcomLigoTable.setStatus("mandatory")
_PcomLigoEntry_Object = MibTableRow
pcomLigoEntry = _PcomLigoEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 9, 2, 1)
)
pcomLigoEntry.setIndexNames(
    (0, "DECHUB900-COMMON-MIB-V3-0", "pcomLigoIndex"),
)
if mibBuilder.loadTexts:
    pcomLigoEntry.setStatus("mandatory")


class _PcomLigoIndex_Type(Integer32):
    """Custom type pcomLigoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PcomLigoIndex_Type.__name__ = "Integer32"
_PcomLigoIndex_Object = MibTableColumn
pcomLigoIndex = _PcomLigoIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 9, 2, 1, 1),
    _PcomLigoIndex_Type()
)
pcomLigoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomLigoIndex.setStatus("mandatory")


class _PcomLigoType_Type(Integer32):
    """Custom type pcomLigoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 3),
          ("fddi", 2),
          ("other", 1))
    )


_PcomLigoType_Type.__name__ = "Integer32"
_PcomLigoType_Object = MibTableColumn
pcomLigoType = _PcomLigoType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 9, 2, 1, 2),
    _PcomLigoType_Type()
)
pcomLigoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomLigoType.setStatus("mandatory")


class _PcomLigoSubtypeSelect_Type(Integer32):
    """Custom type pcomLigoSubtypeSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PcomLigoSubtypeSelect_Type.__name__ = "Integer32"
_PcomLigoSubtypeSelect_Object = MibTableColumn
pcomLigoSubtypeSelect = _PcomLigoSubtypeSelect_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 9, 2, 1, 3),
    _PcomLigoSubtypeSelect_Type()
)
pcomLigoSubtypeSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcomLigoSubtypeSelect.setStatus("mandatory")


class _PcomLigoSubtypeNumEntries_Type(Integer32):
    """Custom type pcomLigoSubtypeNumEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PcomLigoSubtypeNumEntries_Type.__name__ = "Integer32"
_PcomLigoSubtypeNumEntries_Object = MibScalar
pcomLigoSubtypeNumEntries = _PcomLigoSubtypeNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 9, 3),
    _PcomLigoSubtypeNumEntries_Type()
)
pcomLigoSubtypeNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomLigoSubtypeNumEntries.setStatus("mandatory")
_PcomLigoSubtypeTable_Object = MibTable
pcomLigoSubtypeTable = _PcomLigoSubtypeTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 9, 4)
)
if mibBuilder.loadTexts:
    pcomLigoSubtypeTable.setStatus("mandatory")
_PcomLigoSubtypeEntry_Object = MibTableRow
pcomLigoSubtypeEntry = _PcomLigoSubtypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 9, 4, 1)
)
pcomLigoSubtypeEntry.setIndexNames(
    (0, "DECHUB900-COMMON-MIB-V3-0", "pcomLigoSubtypeIndex"),
)
if mibBuilder.loadTexts:
    pcomLigoSubtypeEntry.setStatus("mandatory")


class _PcomLigoSubtypeIndex_Type(Integer32):
    """Custom type pcomLigoSubtypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PcomLigoSubtypeIndex_Type.__name__ = "Integer32"
_PcomLigoSubtypeIndex_Object = MibTableColumn
pcomLigoSubtypeIndex = _PcomLigoSubtypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 9, 4, 1, 1),
    _PcomLigoSubtypeIndex_Type()
)
pcomLigoSubtypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomLigoSubtypeIndex.setStatus("mandatory")


class _PcomLigoSubtypeLigoIndex_Type(Integer32):
    """Custom type pcomLigoSubtypeLigoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PcomLigoSubtypeLigoIndex_Type.__name__ = "Integer32"
_PcomLigoSubtypeLigoIndex_Object = MibTableColumn
pcomLigoSubtypeLigoIndex = _PcomLigoSubtypeLigoIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 9, 4, 1, 2),
    _PcomLigoSubtypeLigoIndex_Type()
)
pcomLigoSubtypeLigoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomLigoSubtypeLigoIndex.setStatus("mandatory")


class _PcomLigoSubtypeLabelIndexMask_Type(Integer32):
    """Custom type pcomLigoSubtypeLabelIndexMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PcomLigoSubtypeLabelIndexMask_Type.__name__ = "Integer32"
_PcomLigoSubtypeLabelIndexMask_Object = MibTableColumn
pcomLigoSubtypeLabelIndexMask = _PcomLigoSubtypeLabelIndexMask_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 9, 4, 1, 3),
    _PcomLigoSubtypeLabelIndexMask_Type()
)
pcomLigoSubtypeLabelIndexMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomLigoSubtypeLabelIndexMask.setStatus("mandatory")


class _PcomLigoSubtypeFlavor_Type(Integer32):
    """Custom type pcomLigoSubtypeFlavor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-back", 13),
          ("ethernet-front", 12),
          ("fddiNonroot", 3),
          ("fddiNonroot-M", 14),
          ("fddiNonroot-S", 15),
          ("fddiNonroot-SM", 16),
          ("fddiRoot-Primary", 1),
          ("fddiRoot-Secondary", 2),
          ("fddiStump-Primary", 10),
          ("fddiStump-Secondary", 11),
          ("fddiTrunk-A-Primary", 4),
          ("fddiTrunk-A-Secondary", 5),
          ("fddiTrunk-AB-Primary", 8),
          ("fddiTrunk-AB-Secondary", 9),
          ("fddiTrunk-B-Primary", 6),
          ("fddiTrunk-B-Secondary", 7))
    )


_PcomLigoSubtypeFlavor_Type.__name__ = "Integer32"
_PcomLigoSubtypeFlavor_Object = MibTableColumn
pcomLigoSubtypeFlavor = _PcomLigoSubtypeFlavor_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 9, 4, 1, 4),
    _PcomLigoSubtypeFlavor_Type()
)
pcomLigoSubtypeFlavor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomLigoSubtypeFlavor.setStatus("mandatory")


class _PcomLigoLabelNumEntries_Type(Integer32):
    """Custom type pcomLigoLabelNumEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PcomLigoLabelNumEntries_Type.__name__ = "Integer32"
_PcomLigoLabelNumEntries_Object = MibScalar
pcomLigoLabelNumEntries = _PcomLigoLabelNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 9, 5),
    _PcomLigoLabelNumEntries_Type()
)
pcomLigoLabelNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomLigoLabelNumEntries.setStatus("mandatory")
_PcomLigoLabelTable_Object = MibTable
pcomLigoLabelTable = _PcomLigoLabelTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 9, 6)
)
if mibBuilder.loadTexts:
    pcomLigoLabelTable.setStatus("mandatory")
_PcomLigoLabelEntry_Object = MibTableRow
pcomLigoLabelEntry = _PcomLigoLabelEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 9, 6, 1)
)
pcomLigoLabelEntry.setIndexNames(
    (0, "DECHUB900-COMMON-MIB-V3-0", "pcomLigoLabelIndex"),
)
if mibBuilder.loadTexts:
    pcomLigoLabelEntry.setStatus("mandatory")


class _PcomLigoLabelIndex_Type(Integer32):
    """Custom type pcomLigoLabelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PcomLigoLabelIndex_Type.__name__ = "Integer32"
_PcomLigoLabelIndex_Object = MibTableColumn
pcomLigoLabelIndex = _PcomLigoLabelIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 9, 6, 1, 1),
    _PcomLigoLabelIndex_Type()
)
pcomLigoLabelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomLigoLabelIndex.setStatus("mandatory")


class _PcomLigoLabelString_Type(DisplayString):
    """Custom type pcomLigoLabelString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PcomLigoLabelString_Type.__name__ = "DisplayString"
_PcomLigoLabelString_Object = MibTableColumn
pcomLigoLabelString = _PcomLigoLabelString_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 9, 6, 1, 2),
    _PcomLigoLabelString_Type()
)
pcomLigoLabelString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomLigoLabelString.setStatus("mandatory")
_PcomCon_ObjectIdentity = ObjectIdentity
pcomCon = _PcomCon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 10)
)
_PcomConTotalConfigChanges_Type = Counter32
_PcomConTotalConfigChanges_Object = MibScalar
pcomConTotalConfigChanges = _PcomConTotalConfigChanges_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 10, 1),
    _PcomConTotalConfigChanges_Type()
)
pcomConTotalConfigChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomConTotalConfigChanges.setStatus("mandatory")


class _PcomConNumEntries_Type(Integer32):
    """Custom type pcomConNumEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PcomConNumEntries_Type.__name__ = "Integer32"
_PcomConNumEntries_Object = MibScalar
pcomConNumEntries = _PcomConNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 10, 2),
    _PcomConNumEntries_Type()
)
pcomConNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomConNumEntries.setStatus("mandatory")
_PcomConTable_Object = MibTable
pcomConTable = _PcomConTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 10, 3)
)
if mibBuilder.loadTexts:
    pcomConTable.setStatus("mandatory")
_PcomConEntry_Object = MibTableRow
pcomConEntry = _PcomConEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 10, 3, 1)
)
pcomConEntry.setIndexNames(
    (0, "DECHUB900-COMMON-MIB-V3-0", "pcomConIndex"),
)
if mibBuilder.loadTexts:
    pcomConEntry.setStatus("mandatory")


class _PcomConIndex_Type(Integer32):
    """Custom type pcomConIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PcomConIndex_Type.__name__ = "Integer32"
_PcomConIndex_Object = MibTableColumn
pcomConIndex = _PcomConIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 10, 3, 1, 1),
    _PcomConIndex_Type()
)
pcomConIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomConIndex.setStatus("mandatory")


class _PcomConTech_Type(Integer32):
    """Custom type pcomConTech based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ethernet", 1)
    )


_PcomConTech_Type.__name__ = "Integer32"
_PcomConTech_Object = MibTableColumn
pcomConTech = _PcomConTech_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 10, 3, 1, 2),
    _PcomConTech_Type()
)
pcomConTech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomConTech.setStatus("mandatory")


class _PcomConClass_Type(Integer32):
    """Custom type pcomConClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("bezcon", 1),
          ("extcon", 2),
          ("interthinwire", 3),
          ("mac", 4))
    )


_PcomConClass_Type.__name__ = "Integer32"
_PcomConClass_Object = MibTableColumn
pcomConClass = _PcomConClass_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 10, 3, 1, 3),
    _PcomConClass_Type()
)
pcomConClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomConClass.setStatus("mandatory")


class _PcomConGroupId_Type(Integer32):
    """Custom type pcomConGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PcomConGroupId_Type.__name__ = "Integer32"
_PcomConGroupId_Object = MibTableColumn
pcomConGroupId = _PcomConGroupId_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 10, 3, 1, 4),
    _PcomConGroupId_Type()
)
pcomConGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcomConGroupId.setStatus("mandatory")


class _PcomConGroupSet_Type(OctetString):
    """Custom type pcomConGroupSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_PcomConGroupSet_Type.__name__ = "OctetString"
_PcomConGroupSet_Object = MibTableColumn
pcomConGroupSet = _PcomConGroupSet_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 10, 3, 1, 5),
    _PcomConGroupSet_Type()
)
pcomConGroupSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomConGroupSet.setStatus("mandatory")


class _PcomConLabel_Type(DisplayString):
    """Custom type pcomConLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PcomConLabel_Type.__name__ = "DisplayString"
_PcomConLabel_Object = MibTableColumn
pcomConLabel = _PcomConLabel_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 10, 3, 1, 6),
    _PcomConLabel_Type()
)
pcomConLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomConLabel.setStatus("mandatory")


class _PcomConSubtypeSelect_Type(Integer32):
    """Custom type pcomConSubtypeSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PcomConSubtypeSelect_Type.__name__ = "Integer32"
_PcomConSubtypeSelect_Object = MibTableColumn
pcomConSubtypeSelect = _PcomConSubtypeSelect_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 10, 3, 1, 7),
    _PcomConSubtypeSelect_Type()
)
pcomConSubtypeSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcomConSubtypeSelect.setStatus("mandatory")


class _PcomConSubtypeNumEntries_Type(Integer32):
    """Custom type pcomConSubtypeNumEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PcomConSubtypeNumEntries_Type.__name__ = "Integer32"
_PcomConSubtypeNumEntries_Object = MibScalar
pcomConSubtypeNumEntries = _PcomConSubtypeNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 10, 4),
    _PcomConSubtypeNumEntries_Type()
)
pcomConSubtypeNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomConSubtypeNumEntries.setStatus("mandatory")
_PcomConSubtypeTable_Object = MibTable
pcomConSubtypeTable = _PcomConSubtypeTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 10, 5)
)
if mibBuilder.loadTexts:
    pcomConSubtypeTable.setStatus("mandatory")
_PcomConSubtypeEntry_Object = MibTableRow
pcomConSubtypeEntry = _PcomConSubtypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 10, 5, 1)
)
pcomConSubtypeEntry.setIndexNames(
    (0, "DECHUB900-COMMON-MIB-V3-0", "pcomConSubtypeIndex"),
)
if mibBuilder.loadTexts:
    pcomConSubtypeEntry.setStatus("mandatory")


class _PcomConSubtypeIndex_Type(Integer32):
    """Custom type pcomConSubtypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PcomConSubtypeIndex_Type.__name__ = "Integer32"
_PcomConSubtypeIndex_Object = MibTableColumn
pcomConSubtypeIndex = _PcomConSubtypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 10, 5, 1, 1),
    _PcomConSubtypeIndex_Type()
)
pcomConSubtypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomConSubtypeIndex.setStatus("mandatory")


class _PcomConSubtypeConSet_Type(OctetString):
    """Custom type pcomConSubtypeConSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_PcomConSubtypeConSet_Type.__name__ = "OctetString"
_PcomConSubtypeConSet_Object = MibTableColumn
pcomConSubtypeConSet = _PcomConSubtypeConSet_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 10, 5, 1, 2),
    _PcomConSubtypeConSet_Type()
)
pcomConSubtypeConSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomConSubtypeConSet.setStatus("mandatory")


class _PcomConSubtypeFlavor_Type(Integer32):
    """Custom type pcomConSubtypeFlavor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aui", 3),
          ("default", 1),
          ("thinwire", 2))
    )


_PcomConSubtypeFlavor_Type.__name__ = "Integer32"
_PcomConSubtypeFlavor_Object = MibTableColumn
pcomConSubtypeFlavor = _PcomConSubtypeFlavor_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 10, 5, 1, 3),
    _PcomConSubtypeFlavor_Type()
)
pcomConSubtypeFlavor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomConSubtypeFlavor.setStatus("mandatory")


class _PcomConIntLanNumEntries_Type(Integer32):
    """Custom type pcomConIntLanNumEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PcomConIntLanNumEntries_Type.__name__ = "Integer32"
_PcomConIntLanNumEntries_Object = MibScalar
pcomConIntLanNumEntries = _PcomConIntLanNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 10, 6),
    _PcomConIntLanNumEntries_Type()
)
pcomConIntLanNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomConIntLanNumEntries.setStatus("mandatory")
_PcomConIntLanTable_Object = MibTable
pcomConIntLanTable = _PcomConIntLanTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 10, 7)
)
if mibBuilder.loadTexts:
    pcomConIntLanTable.setStatus("mandatory")
_PcomConIntLanEntry_Object = MibTableRow
pcomConIntLanEntry = _PcomConIntLanEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 10, 7, 1)
)
pcomConIntLanEntry.setIndexNames(
    (0, "DECHUB900-COMMON-MIB-V3-0", "pcomConIntLanIndex"),
)
if mibBuilder.loadTexts:
    pcomConIntLanEntry.setStatus("mandatory")


class _PcomConIntLanIndex_Type(Integer32):
    """Custom type pcomConIntLanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PcomConIntLanIndex_Type.__name__ = "Integer32"
_PcomConIntLanIndex_Object = MibTableColumn
pcomConIntLanIndex = _PcomConIntLanIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 10, 7, 1, 1),
    _PcomConIntLanIndex_Type()
)
pcomConIntLanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomConIntLanIndex.setStatus("mandatory")


class _PcomConIntLanGroupIdMask_Type(OctetString):
    """Custom type pcomConIntLanGroupIdMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_PcomConIntLanGroupIdMask_Type.__name__ = "OctetString"
_PcomConIntLanGroupIdMask_Object = MibTableColumn
pcomConIntLanGroupIdMask = _PcomConIntLanGroupIdMask_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 10, 7, 1, 2),
    _PcomConIntLanGroupIdMask_Type()
)
pcomConIntLanGroupIdMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomConIntLanGroupIdMask.setStatus("mandatory")


class _PcomConIntLanName_Type(DisplayString):
    """Custom type pcomConIntLanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PcomConIntLanName_Type.__name__ = "DisplayString"
_PcomConIntLanName_Object = MibTableColumn
pcomConIntLanName = _PcomConIntLanName_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 10, 7, 1, 3),
    _PcomConIntLanName_Type()
)
pcomConIntLanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcomConIntLanName.setStatus("mandatory")


class _PcomConAssignNumEntries_Type(Integer32):
    """Custom type pcomConAssignNumEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PcomConAssignNumEntries_Type.__name__ = "Integer32"
_PcomConAssignNumEntries_Object = MibScalar
pcomConAssignNumEntries = _PcomConAssignNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 10, 8),
    _PcomConAssignNumEntries_Type()
)
pcomConAssignNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcomConAssignNumEntries.setStatus("mandatory")
_PcomConAssignTable_Object = MibTable
pcomConAssignTable = _PcomConAssignTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 10, 9)
)
if mibBuilder.loadTexts:
    pcomConAssignTable.setStatus("mandatory")
_PcomConAssignEntry_Object = MibTableRow
pcomConAssignEntry = _PcomConAssignEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 10, 9, 1)
)
pcomConAssignEntry.setIndexNames(
    (0, "DECHUB900-COMMON-MIB-V3-0", "pcomConAssignIndex"),
)
if mibBuilder.loadTexts:
    pcomConAssignEntry.setStatus("mandatory")


class _PcomConAssignIndex_Type(Integer32):
    """Custom type pcomConAssignIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PcomConAssignIndex_Type.__name__ = "Integer32"
_PcomConAssignIndex_Object = MibTableColumn
pcomConAssignIndex = _PcomConAssignIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 10, 9, 1, 1),
    _PcomConAssignIndex_Type()
)
pcomConAssignIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcomConAssignIndex.setStatus("mandatory")


class _PcomConAssignConGroup_Type(Integer32):
    """Custom type pcomConAssignConGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PcomConAssignConGroup_Type.__name__ = "Integer32"
_PcomConAssignConGroup_Object = MibTableColumn
pcomConAssignConGroup = _PcomConAssignConGroup_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 10, 9, 1, 2),
    _PcomConAssignConGroup_Type()
)
pcomConAssignConGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcomConAssignConGroup.setStatus("mandatory")


class _PcomConAssignIntLan_Type(Integer32):
    """Custom type pcomConAssignIntLan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PcomConAssignIntLan_Type.__name__ = "Integer32"
_PcomConAssignIntLan_Object = MibTableColumn
pcomConAssignIntLan = _PcomConAssignIntLan_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 10, 9, 1, 3),
    _PcomConAssignIntLan_Type()
)
pcomConAssignIntLan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcomConAssignIntLan.setStatus("mandatory")


class _PcomConAssignEntryStatus_Type(Integer32):
    """Custom type pcomConAssignEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )


_PcomConAssignEntryStatus_Type.__name__ = "Integer32"
_PcomConAssignEntryStatus_Object = MibTableColumn
pcomConAssignEntryStatus = _PcomConAssignEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 10, 9, 1, 4),
    _PcomConAssignEntryStatus_Type()
)
pcomConAssignEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcomConAssignEntryStatus.setStatus("mandatory")
_Pcom90mgt_ObjectIdentity = ObjectIdentity
pcom90mgt = _Pcom90mgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 11)
)


class _Pcom90mgtBackplaneHubMaster_Type(Integer32):
    """Custom type pcom90mgtBackplaneHubMaster based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Pcom90mgtBackplaneHubMaster_Type.__name__ = "Integer32"
_Pcom90mgtBackplaneHubMaster_Object = MibScalar
pcom90mgtBackplaneHubMaster = _Pcom90mgtBackplaneHubMaster_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 11, 1),
    _Pcom90mgtBackplaneHubMaster_Type()
)
pcom90mgtBackplaneHubMaster.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcom90mgtBackplaneHubMaster.setStatus("mandatory")


class _Pcom90mgtBackplaneHubMasterState_Type(Integer32):
    """Custom type pcom90mgtBackplaneHubMasterState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_Pcom90mgtBackplaneHubMasterState_Type.__name__ = "Integer32"
_Pcom90mgtBackplaneHubMasterState_Object = MibScalar
pcom90mgtBackplaneHubMasterState = _Pcom90mgtBackplaneHubMasterState_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 11, 2),
    _Pcom90mgtBackplaneHubMasterState_Type()
)
pcom90mgtBackplaneHubMasterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcom90mgtBackplaneHubMasterState.setStatus("mandatory")


class _Pcom90mgtBackplaneConfig_Type(Integer32):
    """Custom type pcom90mgtBackplaneConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("decStack90", 5),
          ("notConfigured", 1),
          ("pair-DEChub90", 4),
          ("single-DEChub90", 3),
          ("standAlone", 2))
    )


_Pcom90mgtBackplaneConfig_Type.__name__ = "Integer32"
_Pcom90mgtBackplaneConfig_Object = MibScalar
pcom90mgtBackplaneConfig = _Pcom90mgtBackplaneConfig_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 2, 11, 3),
    _Pcom90mgtBackplaneConfig_Type()
)
pcom90mgtBackplaneConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcom90mgtBackplaneConfig.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DECHUB900-COMMON-MIB-V3-0",
    **{"dec": dec,
       "ema": ema,
       "decMIBextension": decMIBextension,
       "decHub900": decHub900,
       "pubCommon": pubCommon,
       "pcomSlot": pcomSlot,
       "pcomOperStatus": pcomOperStatus,
       "pcomAdminStatus": pcomAdminStatus,
       "pcomDiagFailure": pcomDiagFailure,
       "pcomSerialNumber": pcomSerialNumber,
       "pcomSlotNumber": pcomSlotNumber,
       "pcomEsn": pcomEsn,
       "pcomHub": pcomHub,
       "pcomHubId": pcomHubId,
       "pcomHubIpAddress": pcomHubIpAddress,
       "pcomHubCommunity": pcomHubCommunity,
       "pcomLed": pcomLed,
       "pcomLedTable": pcomLedTable,
       "pcomLedEntry": pcomLedEntry,
       "pcomLedIndex": pcomLedIndex,
       "pcomLedDescr": pcomLedDescr,
       "pcomLedProgram": pcomLedProgram,
       "pcomLedInterestingChanges": pcomLedInterestingChanges,
       "pcomLoad": pcomLoad,
       "pcomLoadAdminStatus": pcomLoadAdminStatus,
       "pcomLoadOperStatus": pcomLoadOperStatus,
       "pcomLoadFilename": pcomLoadFilename,
       "pcomLoadIpHostAddr": pcomLoadIpHostAddr,
       "pcomLoadDevSpecific": pcomLoadDevSpecific,
       "pcomLoadTftpDirection": pcomLoadTftpDirection,
       "pcomSnmpAuth": pcomSnmpAuth,
       "pcomSnmpAuthTrap": pcomSnmpAuthTrap,
       "pcomSnmpAuthTrapCommunity": pcomSnmpAuthTrapCommunity,
       "pcomSnmpAuthTrapUserTable": pcomSnmpAuthTrapUserTable,
       "pcomSnmpAuthTrapUserEntry": pcomSnmpAuthTrapUserEntry,
       "pcomSnmpAuthTrapUserAddr": pcomSnmpAuthTrapUserAddr,
       "pcomSnmpAuthTrapUserStatus": pcomSnmpAuthTrapUserStatus,
       "pcomSnmpAuthReadOnly": pcomSnmpAuthReadOnly,
       "pcomSnmpAuthReadOnlyCommunity": pcomSnmpAuthReadOnlyCommunity,
       "pcomSnmpAuthReadOnlyUserTable": pcomSnmpAuthReadOnlyUserTable,
       "pcomSnmpAuthReadOnlyUserEntry": pcomSnmpAuthReadOnlyUserEntry,
       "pcomSnmpAuthReadOnlyUserAddr": pcomSnmpAuthReadOnlyUserAddr,
       "pcomSnmpAuthReadOnlyUserMask": pcomSnmpAuthReadOnlyUserMask,
       "pcomSnmpAuthReadOnlyUserStatus": pcomSnmpAuthReadOnlyUserStatus,
       "pcomSnmpAuthReadWrite": pcomSnmpAuthReadWrite,
       "pcomSnmpAuthReadWriteCommunity": pcomSnmpAuthReadWriteCommunity,
       "pcomSnmpAuthReadWriteUserTable": pcomSnmpAuthReadWriteUserTable,
       "pcomSnmpAuthReadWriteUserEntry": pcomSnmpAuthReadWriteUserEntry,
       "pcomSnmpAuthReadWriteUserAddr": pcomSnmpAuthReadWriteUserAddr,
       "pcomSnmpAuthReadWriteUserMask": pcomSnmpAuthReadWriteUserMask,
       "pcomSnmpAuthReadWriteUserStatus": pcomSnmpAuthReadWriteUserStatus,
       "pcomSnmpAuthUnauth": pcomSnmpAuthUnauth,
       "pcomSnmpAuthUnauthTable": pcomSnmpAuthUnauthTable,
       "pcomSnmpAuthUnauthEntry": pcomSnmpAuthUnauthEntry,
       "pcomSnmpAuthUnauthIndex": pcomSnmpAuthUnauthIndex,
       "pcomSnmpAuthUnauthTimeStamp": pcomSnmpAuthUnauthTimeStamp,
       "pcomSnmpAuthUnauthIpAddress": pcomSnmpAuthUnauthIpAddress,
       "pcomSnmpAuthUnauthUdpPort": pcomSnmpAuthUnauthUdpPort,
       "pcomSnmpAuthUnauthCommunity": pcomSnmpAuthUnauthCommunity,
       "pcomSnmpAuthUnauthOperation": pcomSnmpAuthUnauthOperation,
       "pcomSnmpAuthUnauthReason": pcomSnmpAuthUnauthReason,
       "pcomErrLog": pcomErrLog,
       "pcomErrLogNumEntries": pcomErrLogNumEntries,
       "pcomErrLogTable": pcomErrLogTable,
       "pcomErrLogEntry": pcomErrLogEntry,
       "pcomErrLogIndex": pcomErrLogIndex,
       "pcomErrLogTimeStamp": pcomErrLogTimeStamp,
       "pcomErrLogResetNumber": pcomErrLogResetNumber,
       "pcomErrLogInfo": pcomErrLogInfo,
       "pcomErrLogFwVersion": pcomErrLogFwVersion,
       "pcomEsys": pcomEsys,
       "pcomEsysPowerups": pcomEsysPowerups,
       "pcomEsysMgmtResets": pcomEsysMgmtResets,
       "pcomEsysUnsolicitedResets": pcomEsysUnsolicitedResets,
       "pcomEsysNVRAMfailedFlag": pcomEsysNVRAMfailedFlag,
       "pcomEsysNVRAMsize": pcomEsysNVRAMsize,
       "pcomEsysNVRAMavailableOctets": pcomEsysNVRAMavailableOctets,
       "pcomEsysHubVersion": pcomEsysHubVersion,
       "pcomEif": pcomEif,
       "pcomEifTable": pcomEifTable,
       "pcomEifEntry": pcomEifEntry,
       "pcomEifIndex": pcomEifIndex,
       "pcomEifInBroadcastPkts": pcomEifInBroadcastPkts,
       "pcomLigo": pcomLigo,
       "pcomLigoNumEntries": pcomLigoNumEntries,
       "pcomLigoTable": pcomLigoTable,
       "pcomLigoEntry": pcomLigoEntry,
       "pcomLigoIndex": pcomLigoIndex,
       "pcomLigoType": pcomLigoType,
       "pcomLigoSubtypeSelect": pcomLigoSubtypeSelect,
       "pcomLigoSubtypeNumEntries": pcomLigoSubtypeNumEntries,
       "pcomLigoSubtypeTable": pcomLigoSubtypeTable,
       "pcomLigoSubtypeEntry": pcomLigoSubtypeEntry,
       "pcomLigoSubtypeIndex": pcomLigoSubtypeIndex,
       "pcomLigoSubtypeLigoIndex": pcomLigoSubtypeLigoIndex,
       "pcomLigoSubtypeLabelIndexMask": pcomLigoSubtypeLabelIndexMask,
       "pcomLigoSubtypeFlavor": pcomLigoSubtypeFlavor,
       "pcomLigoLabelNumEntries": pcomLigoLabelNumEntries,
       "pcomLigoLabelTable": pcomLigoLabelTable,
       "pcomLigoLabelEntry": pcomLigoLabelEntry,
       "pcomLigoLabelIndex": pcomLigoLabelIndex,
       "pcomLigoLabelString": pcomLigoLabelString,
       "pcomCon": pcomCon,
       "pcomConTotalConfigChanges": pcomConTotalConfigChanges,
       "pcomConNumEntries": pcomConNumEntries,
       "pcomConTable": pcomConTable,
       "pcomConEntry": pcomConEntry,
       "pcomConIndex": pcomConIndex,
       "pcomConTech": pcomConTech,
       "pcomConClass": pcomConClass,
       "pcomConGroupId": pcomConGroupId,
       "pcomConGroupSet": pcomConGroupSet,
       "pcomConLabel": pcomConLabel,
       "pcomConSubtypeSelect": pcomConSubtypeSelect,
       "pcomConSubtypeNumEntries": pcomConSubtypeNumEntries,
       "pcomConSubtypeTable": pcomConSubtypeTable,
       "pcomConSubtypeEntry": pcomConSubtypeEntry,
       "pcomConSubtypeIndex": pcomConSubtypeIndex,
       "pcomConSubtypeConSet": pcomConSubtypeConSet,
       "pcomConSubtypeFlavor": pcomConSubtypeFlavor,
       "pcomConIntLanNumEntries": pcomConIntLanNumEntries,
       "pcomConIntLanTable": pcomConIntLanTable,
       "pcomConIntLanEntry": pcomConIntLanEntry,
       "pcomConIntLanIndex": pcomConIntLanIndex,
       "pcomConIntLanGroupIdMask": pcomConIntLanGroupIdMask,
       "pcomConIntLanName": pcomConIntLanName,
       "pcomConAssignNumEntries": pcomConAssignNumEntries,
       "pcomConAssignTable": pcomConAssignTable,
       "pcomConAssignEntry": pcomConAssignEntry,
       "pcomConAssignIndex": pcomConAssignIndex,
       "pcomConAssignConGroup": pcomConAssignConGroup,
       "pcomConAssignIntLan": pcomConAssignIntLan,
       "pcomConAssignEntryStatus": pcomConAssignEntryStatus,
       "pcom90mgt": pcom90mgt,
       "pcom90mgtBackplaneHubMaster": pcom90mgtBackplaneHubMaster,
       "pcom90mgtBackplaneHubMasterState": pcom90mgtBackplaneHubMasterState,
       "pcom90mgtBackplaneConfig": pcom90mgtBackplaneConfig}
)
