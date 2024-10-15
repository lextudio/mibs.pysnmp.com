# SNMP MIB module (Wellfleet-IKE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-IKE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:25 2024
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
 Opaque,
 TimeTicks,
 Unsigned32,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(wfIKEGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfIKEGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfIkeDescriptorTable_Object = MibTable
wfIkeDescriptorTable = _WfIkeDescriptorTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 1)
)
if mibBuilder.loadTexts:
    wfIkeDescriptorTable.setStatus("mandatory")
_WfIkeDescriptorEntry_Object = MibTableRow
wfIkeDescriptorEntry = _WfIkeDescriptorEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 1, 1)
)
wfIkeDescriptorEntry.setIndexNames(
    (0, "Wellfleet-IKE-MIB", "wfIkeDescriptorLocalIpAddr"),
    (0, "Wellfleet-IKE-MIB", "wfIkeDescriptorPeerIpAddr"),
    (0, "Wellfleet-IKE-MIB", "wfIkeDescriptorIndex"),
)
if mibBuilder.loadTexts:
    wfIkeDescriptorEntry.setStatus("mandatory")


class _WfIkeDescriptorCreate_Type(Integer32):
    """Custom type wfIkeDescriptorCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfIkeDescriptorCreate_Type.__name__ = "Integer32"
_WfIkeDescriptorCreate_Object = MibTableColumn
wfIkeDescriptorCreate = _WfIkeDescriptorCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 1, 1, 1),
    _WfIkeDescriptorCreate_Type()
)
wfIkeDescriptorCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIkeDescriptorCreate.setStatus("mandatory")


class _WfIkeDescriptorStatus_Type(Integer32):
    """Custom type wfIkeDescriptorStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("notpresent", 3),
          ("up", 1))
    )


_WfIkeDescriptorStatus_Type.__name__ = "Integer32"
_WfIkeDescriptorStatus_Object = MibTableColumn
wfIkeDescriptorStatus = _WfIkeDescriptorStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 1, 1, 2),
    _WfIkeDescriptorStatus_Type()
)
wfIkeDescriptorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIkeDescriptorStatus.setStatus("mandatory")
_WfIkeDescriptorLocalIpAddr_Type = IpAddress
_WfIkeDescriptorLocalIpAddr_Object = MibTableColumn
wfIkeDescriptorLocalIpAddr = _WfIkeDescriptorLocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 1, 1, 3),
    _WfIkeDescriptorLocalIpAddr_Type()
)
wfIkeDescriptorLocalIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIkeDescriptorLocalIpAddr.setStatus("mandatory")
_WfIkeDescriptorPeerIpAddr_Type = IpAddress
_WfIkeDescriptorPeerIpAddr_Object = MibTableColumn
wfIkeDescriptorPeerIpAddr = _WfIkeDescriptorPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 1, 1, 4),
    _WfIkeDescriptorPeerIpAddr_Type()
)
wfIkeDescriptorPeerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIkeDescriptorPeerIpAddr.setStatus("mandatory")
_WfIkeDescriptorIndex_Type = Integer32
_WfIkeDescriptorIndex_Object = MibTableColumn
wfIkeDescriptorIndex = _WfIkeDescriptorIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 1, 1, 5),
    _WfIkeDescriptorIndex_Type()
)
wfIkeDescriptorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIkeDescriptorIndex.setStatus("mandatory")


class _WfIkeDescriptorExchange_Type(Integer32):
    """Custom type wfIkeDescriptorExchange based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aggressive", 2),
          ("main", 1))
    )


_WfIkeDescriptorExchange_Type.__name__ = "Integer32"
_WfIkeDescriptorExchange_Object = MibTableColumn
wfIkeDescriptorExchange = _WfIkeDescriptorExchange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 1, 1, 6),
    _WfIkeDescriptorExchange_Type()
)
wfIkeDescriptorExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIkeDescriptorExchange.setStatus("mandatory")
_WfIkeDescriptorProposals_Type = Opaque
_WfIkeDescriptorProposals_Object = MibTableColumn
wfIkeDescriptorProposals = _WfIkeDescriptorProposals_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 1, 1, 7),
    _WfIkeDescriptorProposals_Type()
)
wfIkeDescriptorProposals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIkeDescriptorProposals.setStatus("mandatory")
_WfIkeDescriptorName_Type = DisplayString
_WfIkeDescriptorName_Object = MibTableColumn
wfIkeDescriptorName = _WfIkeDescriptorName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 1, 1, 8),
    _WfIkeDescriptorName_Type()
)
wfIkeDescriptorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIkeDescriptorName.setStatus("mandatory")
_WfIkeDescriptorPreSharedSecret_Type = OctetString
_WfIkeDescriptorPreSharedSecret_Object = MibTableColumn
wfIkeDescriptorPreSharedSecret = _WfIkeDescriptorPreSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 1, 1, 9),
    _WfIkeDescriptorPreSharedSecret_Type()
)
wfIkeDescriptorPreSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIkeDescriptorPreSharedSecret.setStatus("mandatory")


class _WfIkeDescriptorExpiryMinutes_Type(Integer32):
    """Custom type wfIkeDescriptorExpiryMinutes based on Integer32"""
    defaultValue = 480


_WfIkeDescriptorExpiryMinutes_Object = MibTableColumn
wfIkeDescriptorExpiryMinutes = _WfIkeDescriptorExpiryMinutes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 1, 1, 10),
    _WfIkeDescriptorExpiryMinutes_Type()
)
wfIkeDescriptorExpiryMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIkeDescriptorExpiryMinutes.setStatus("mandatory")


class _WfIkeDescriptorExpiryKBytes_Type(Integer32):
    """Custom type wfIkeDescriptorExpiryKBytes based on Integer32"""
    defaultValue = 1024


_WfIkeDescriptorExpiryKBytes_Object = MibTableColumn
wfIkeDescriptorExpiryKBytes = _WfIkeDescriptorExpiryKBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 1, 1, 11),
    _WfIkeDescriptorExpiryKBytes_Type()
)
wfIkeDescriptorExpiryKBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIkeDescriptorExpiryKBytes.setStatus("mandatory")


class _WfIkeDescriptorExpiryPref_Type(Integer32):
    """Custom type wfIkeDescriptorExpiryPref based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("kbytes", 2),
          ("minutes", 1))
    )


_WfIkeDescriptorExpiryPref_Type.__name__ = "Integer32"
_WfIkeDescriptorExpiryPref_Object = MibTableColumn
wfIkeDescriptorExpiryPref = _WfIkeDescriptorExpiryPref_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 1, 1, 12),
    _WfIkeDescriptorExpiryPref_Type()
)
wfIkeDescriptorExpiryPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIkeDescriptorExpiryPref.setStatus("mandatory")


class _WfIkeDescriptorIdType_Type(Integer32):
    """Custom type wfIkeDescriptorIdType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("host", 3),
          ("range", 1),
          ("subnet", 2))
    )


_WfIkeDescriptorIdType_Type.__name__ = "Integer32"
_WfIkeDescriptorIdType_Object = MibTableColumn
wfIkeDescriptorIdType = _WfIkeDescriptorIdType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 1, 1, 13),
    _WfIkeDescriptorIdType_Type()
)
wfIkeDescriptorIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIkeDescriptorIdType.setStatus("mandatory")
_WfIkeTransformTable_Object = MibTable
wfIkeTransformTable = _WfIkeTransformTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 2)
)
if mibBuilder.loadTexts:
    wfIkeTransformTable.setStatus("mandatory")
_WfIkeTransformEntry_Object = MibTableRow
wfIkeTransformEntry = _WfIkeTransformEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 2, 1)
)
wfIkeTransformEntry.setIndexNames(
    (0, "Wellfleet-IKE-MIB", "wfIkeTransformNumber"),
)
if mibBuilder.loadTexts:
    wfIkeTransformEntry.setStatus("mandatory")


class _WfIkeTransformCreate_Type(Integer32):
    """Custom type wfIkeTransformCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfIkeTransformCreate_Type.__name__ = "Integer32"
_WfIkeTransformCreate_Object = MibTableColumn
wfIkeTransformCreate = _WfIkeTransformCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 2, 1, 1),
    _WfIkeTransformCreate_Type()
)
wfIkeTransformCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIkeTransformCreate.setStatus("mandatory")


class _WfIkeTransformStatus_Type(Integer32):
    """Custom type wfIkeTransformStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("notpresent", 3),
          ("up", 1))
    )


_WfIkeTransformStatus_Type.__name__ = "Integer32"
_WfIkeTransformStatus_Object = MibTableColumn
wfIkeTransformStatus = _WfIkeTransformStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 2, 1, 2),
    _WfIkeTransformStatus_Type()
)
wfIkeTransformStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIkeTransformStatus.setStatus("mandatory")
_WfIkeTransformNumber_Type = Integer32
_WfIkeTransformNumber_Object = MibTableColumn
wfIkeTransformNumber = _WfIkeTransformNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 2, 1, 3),
    _WfIkeTransformNumber_Type()
)
wfIkeTransformNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIkeTransformNumber.setStatus("mandatory")


class _WfIkeTransformCipherAlg_Type(Integer32):
    """Custom type wfIkeTransformCipherAlg based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5)
        )
    )
    namedValues = NamedValues(
        *(("des", 1),
          ("desede", 5))
    )


_WfIkeTransformCipherAlg_Type.__name__ = "Integer32"
_WfIkeTransformCipherAlg_Object = MibTableColumn
wfIkeTransformCipherAlg = _WfIkeTransformCipherAlg_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 2, 1, 4),
    _WfIkeTransformCipherAlg_Type()
)
wfIkeTransformCipherAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIkeTransformCipherAlg.setStatus("mandatory")


class _WfIkeTransformDesKeyStrength_Type(Integer32):
    """Custom type wfIkeTransformDesKeyStrength based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fiftysixbit", 2),
          ("fortybit", 1))
    )


_WfIkeTransformDesKeyStrength_Type.__name__ = "Integer32"
_WfIkeTransformDesKeyStrength_Object = MibTableColumn
wfIkeTransformDesKeyStrength = _WfIkeTransformDesKeyStrength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 2, 1, 5),
    _WfIkeTransformDesKeyStrength_Type()
)
wfIkeTransformDesKeyStrength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIkeTransformDesKeyStrength.setStatus("mandatory")


class _WfIkeTransformIntegrityAlg_Type(Integer32):
    """Custom type wfIkeTransformIntegrityAlg based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("sha1", 2))
    )


_WfIkeTransformIntegrityAlg_Type.__name__ = "Integer32"
_WfIkeTransformIntegrityAlg_Object = MibTableColumn
wfIkeTransformIntegrityAlg = _WfIkeTransformIntegrityAlg_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 2, 1, 6),
    _WfIkeTransformIntegrityAlg_Type()
)
wfIkeTransformIntegrityAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIkeTransformIntegrityAlg.setStatus("mandatory")
_WfIkeSlotTable_Object = MibTable
wfIkeSlotTable = _WfIkeSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 3)
)
if mibBuilder.loadTexts:
    wfIkeSlotTable.setStatus("mandatory")
_WfIkeSlotEntry_Object = MibTableRow
wfIkeSlotEntry = _WfIkeSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 3, 1)
)
wfIkeSlotEntry.setIndexNames(
    (0, "Wellfleet-IKE-MIB", "wfIkeSlotNum"),
)
if mibBuilder.loadTexts:
    wfIkeSlotEntry.setStatus("mandatory")


class _WfIkeSlotCreate_Type(Integer32):
    """Custom type wfIkeSlotCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfIkeSlotCreate_Type.__name__ = "Integer32"
_WfIkeSlotCreate_Object = MibTableColumn
wfIkeSlotCreate = _WfIkeSlotCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 3, 1, 1),
    _WfIkeSlotCreate_Type()
)
wfIkeSlotCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIkeSlotCreate.setStatus("mandatory")
_WfIkeSlotNum_Type = Integer32
_WfIkeSlotNum_Object = MibTableColumn
wfIkeSlotNum = _WfIkeSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 3, 1, 2),
    _WfIkeSlotNum_Type()
)
wfIkeSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIkeSlotNum.setStatus("mandatory")


class _WfIkeSlotLogLevel_Type(Integer32):
    """Custom type wfIkeSlotLogLevel based on Integer32"""
    defaultValue = 0


_WfIkeSlotLogLevel_Object = MibTableColumn
wfIkeSlotLogLevel = _WfIkeSlotLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 3, 1, 3),
    _WfIkeSlotLogLevel_Type()
)
wfIkeSlotLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIkeSlotLogLevel.setStatus("mandatory")
_WfIkeSaTable_Object = MibTable
wfIkeSaTable = _WfIkeSaTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 4)
)
if mibBuilder.loadTexts:
    wfIkeSaTable.setStatus("mandatory")
_WfIkeSaEntry_Object = MibTableRow
wfIkeSaEntry = _WfIkeSaEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 4, 1)
)
wfIkeSaEntry.setIndexNames(
    (0, "Wellfleet-IKE-MIB", "wfIkeSaSrc"),
    (0, "Wellfleet-IKE-MIB", "wfIkeSaDest"),
    (0, "Wellfleet-IKE-MIB", "wfIkeSaIndex"),
)
if mibBuilder.loadTexts:
    wfIkeSaEntry.setStatus("mandatory")


class _WfIkeSaCreate_Type(Integer32):
    """Custom type wfIkeSaCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfIkeSaCreate_Type.__name__ = "Integer32"
_WfIkeSaCreate_Object = MibTableColumn
wfIkeSaCreate = _WfIkeSaCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 4, 1, 1),
    _WfIkeSaCreate_Type()
)
wfIkeSaCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIkeSaCreate.setStatus("mandatory")
_WfIkeSaSrc_Type = IpAddress
_WfIkeSaSrc_Object = MibTableColumn
wfIkeSaSrc = _WfIkeSaSrc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 4, 1, 2),
    _WfIkeSaSrc_Type()
)
wfIkeSaSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIkeSaSrc.setStatus("mandatory")
_WfIkeSaDest_Type = IpAddress
_WfIkeSaDest_Object = MibTableColumn
wfIkeSaDest = _WfIkeSaDest_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 4, 1, 3),
    _WfIkeSaDest_Type()
)
wfIkeSaDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIkeSaDest.setStatus("mandatory")
_WfIkeSaIndex_Type = Integer32
_WfIkeSaIndex_Object = MibTableColumn
wfIkeSaIndex = _WfIkeSaIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 4, 1, 4),
    _WfIkeSaIndex_Type()
)
wfIkeSaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIkeSaIndex.setStatus("mandatory")


class _WfIkeSaCipherAlg_Type(Integer32):
    """Custom type wfIkeSaCipherAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("des", 2),
          ("des3", 3))
    )


_WfIkeSaCipherAlg_Type.__name__ = "Integer32"
_WfIkeSaCipherAlg_Object = MibTableColumn
wfIkeSaCipherAlg = _WfIkeSaCipherAlg_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 4, 1, 5),
    _WfIkeSaCipherAlg_Type()
)
wfIkeSaCipherAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIkeSaCipherAlg.setStatus("mandatory")


class _WfIkeSaIntegrityAlg_Type(Integer32):
    """Custom type wfIkeSaIntegrityAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 2),
          ("sha1", 3))
    )


_WfIkeSaIntegrityAlg_Type.__name__ = "Integer32"
_WfIkeSaIntegrityAlg_Object = MibTableColumn
wfIkeSaIntegrityAlg = _WfIkeSaIntegrityAlg_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 4, 1, 6),
    _WfIkeSaIntegrityAlg_Type()
)
wfIkeSaIntegrityAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIkeSaIntegrityAlg.setStatus("mandatory")


class _WfIkeSaExpiryUnits_Type(Integer32):
    """Custom type wfIkeSaExpiryUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("kilobytes", 2),
          ("minutes", 1))
    )


_WfIkeSaExpiryUnits_Type.__name__ = "Integer32"
_WfIkeSaExpiryUnits_Object = MibTableColumn
wfIkeSaExpiryUnits = _WfIkeSaExpiryUnits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 4, 1, 7),
    _WfIkeSaExpiryUnits_Type()
)
wfIkeSaExpiryUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIkeSaExpiryUnits.setStatus("mandatory")
_WfIkeSaExpiryValue_Type = Integer32
_WfIkeSaExpiryValue_Object = MibTableColumn
wfIkeSaExpiryValue = _WfIkeSaExpiryValue_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 4, 1, 8),
    _WfIkeSaExpiryValue_Type()
)
wfIkeSaExpiryValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIkeSaExpiryValue.setStatus("mandatory")
_WfIkeSaBadDecrypt_Type = Counter32
_WfIkeSaBadDecrypt_Object = MibTableColumn
wfIkeSaBadDecrypt = _WfIkeSaBadDecrypt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 4, 1, 9),
    _WfIkeSaBadDecrypt_Type()
)
wfIkeSaBadDecrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIkeSaBadDecrypt.setStatus("mandatory")
_WfIkeSaBadPad_Type = Counter32
_WfIkeSaBadPad_Object = MibTableColumn
wfIkeSaBadPad = _WfIkeSaBadPad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 4, 1, 10),
    _WfIkeSaBadPad_Type()
)
wfIkeSaBadPad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIkeSaBadPad.setStatus("mandatory")
_WfIkeSaTxPkts_Type = Counter32
_WfIkeSaTxPkts_Object = MibTableColumn
wfIkeSaTxPkts = _WfIkeSaTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 4, 1, 11),
    _WfIkeSaTxPkts_Type()
)
wfIkeSaTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIkeSaTxPkts.setStatus("mandatory")
_WfIkeSaRxPkts_Type = Counter32
_WfIkeSaRxPkts_Object = MibTableColumn
wfIkeSaRxPkts = _WfIkeSaRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 4, 1, 12),
    _WfIkeSaRxPkts_Type()
)
wfIkeSaRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIkeSaRxPkts.setStatus("mandatory")
_WfIkeSaTxOctets_Type = Counter32
_WfIkeSaTxOctets_Object = MibTableColumn
wfIkeSaTxOctets = _WfIkeSaTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 4, 1, 13),
    _WfIkeSaTxOctets_Type()
)
wfIkeSaTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIkeSaTxOctets.setStatus("mandatory")
_WfIkeSaRxOctets_Type = Counter32
_WfIkeSaRxOctets_Object = MibTableColumn
wfIkeSaRxOctets = _WfIkeSaRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27, 4, 1, 14),
    _WfIkeSaRxOctets_Type()
)
wfIkeSaRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIkeSaRxOctets.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-IKE-MIB",
    **{"wfIkeDescriptorTable": wfIkeDescriptorTable,
       "wfIkeDescriptorEntry": wfIkeDescriptorEntry,
       "wfIkeDescriptorCreate": wfIkeDescriptorCreate,
       "wfIkeDescriptorStatus": wfIkeDescriptorStatus,
       "wfIkeDescriptorLocalIpAddr": wfIkeDescriptorLocalIpAddr,
       "wfIkeDescriptorPeerIpAddr": wfIkeDescriptorPeerIpAddr,
       "wfIkeDescriptorIndex": wfIkeDescriptorIndex,
       "wfIkeDescriptorExchange": wfIkeDescriptorExchange,
       "wfIkeDescriptorProposals": wfIkeDescriptorProposals,
       "wfIkeDescriptorName": wfIkeDescriptorName,
       "wfIkeDescriptorPreSharedSecret": wfIkeDescriptorPreSharedSecret,
       "wfIkeDescriptorExpiryMinutes": wfIkeDescriptorExpiryMinutes,
       "wfIkeDescriptorExpiryKBytes": wfIkeDescriptorExpiryKBytes,
       "wfIkeDescriptorExpiryPref": wfIkeDescriptorExpiryPref,
       "wfIkeDescriptorIdType": wfIkeDescriptorIdType,
       "wfIkeTransformTable": wfIkeTransformTable,
       "wfIkeTransformEntry": wfIkeTransformEntry,
       "wfIkeTransformCreate": wfIkeTransformCreate,
       "wfIkeTransformStatus": wfIkeTransformStatus,
       "wfIkeTransformNumber": wfIkeTransformNumber,
       "wfIkeTransformCipherAlg": wfIkeTransformCipherAlg,
       "wfIkeTransformDesKeyStrength": wfIkeTransformDesKeyStrength,
       "wfIkeTransformIntegrityAlg": wfIkeTransformIntegrityAlg,
       "wfIkeSlotTable": wfIkeSlotTable,
       "wfIkeSlotEntry": wfIkeSlotEntry,
       "wfIkeSlotCreate": wfIkeSlotCreate,
       "wfIkeSlotNum": wfIkeSlotNum,
       "wfIkeSlotLogLevel": wfIkeSlotLogLevel,
       "wfIkeSaTable": wfIkeSaTable,
       "wfIkeSaEntry": wfIkeSaEntry,
       "wfIkeSaCreate": wfIkeSaCreate,
       "wfIkeSaSrc": wfIkeSaSrc,
       "wfIkeSaDest": wfIkeSaDest,
       "wfIkeSaIndex": wfIkeSaIndex,
       "wfIkeSaCipherAlg": wfIkeSaCipherAlg,
       "wfIkeSaIntegrityAlg": wfIkeSaIntegrityAlg,
       "wfIkeSaExpiryUnits": wfIkeSaExpiryUnits,
       "wfIkeSaExpiryValue": wfIkeSaExpiryValue,
       "wfIkeSaBadDecrypt": wfIkeSaBadDecrypt,
       "wfIkeSaBadPad": wfIkeSaBadPad,
       "wfIkeSaTxPkts": wfIkeSaTxPkts,
       "wfIkeSaRxPkts": wfIkeSaRxPkts,
       "wfIkeSaTxOctets": wfIkeSaTxOctets,
       "wfIkeSaRxOctets": wfIkeSaRxOctets}
)
