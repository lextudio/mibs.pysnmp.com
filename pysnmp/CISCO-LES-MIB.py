# SNMP MIB module (CISCO-LES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:59 2024
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

(CiscoVciInteger,
 CiscoVpiInteger) = mibBuilder.importSymbols(
    "CISCO-BUS-MIB",
    "CiscoVciInteger",
    "CiscoVpiInteger")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(AtmLaneAddress,) = mibBuilder.importSymbols(
    "LAN-EMULATION-CLIENT-MIB",
    "AtmLaneAddress")

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
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(DisplayString,
 MacAddress,
 RowStatus,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC-v1",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TimeStamp")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLesMIB_ObjectIdentity = ObjectIdentity
ciscoLesMIB = _CiscoLesMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 39)
)
_CiscoLesMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLesMIBObjects = _CiscoLesMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1)
)
_Les_ObjectIdentity = ObjectIdentity
les = _Les_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1)
)
_LesTable_Object = MibTable
lesTable = _LesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lesTable.setStatus("mandatory")
_LesEntry_Object = MibTableRow
lesEntry = _LesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 1, 1)
)
lesEntry.setIndexNames(
    (0, "CISCO-LES-MIB", "lesElanName"),
    (0, "CISCO-LES-MIB", "lesIndex"),
)
if mibBuilder.loadTexts:
    lesEntry.setStatus("mandatory")


class _LesElanName_Type(DisplayString):
    """Custom type lesElanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LesElanName_Type.__name__ = "DisplayString"
_LesElanName_Object = MibTableColumn
lesElanName = _LesElanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 1, 1, 1),
    _LesElanName_Type()
)
lesElanName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lesElanName.setStatus("mandatory")


class _LesIndex_Type(Integer32):
    """Custom type lesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LesIndex_Type.__name__ = "Integer32"
_LesIndex_Object = MibTableColumn
lesIndex = _LesIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 1, 1, 2),
    _LesIndex_Type()
)
lesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lesIndex.setStatus("mandatory")
_LesAtmAddrSpec_Type = AtmLaneAddress
_LesAtmAddrSpec_Object = MibTableColumn
lesAtmAddrSpec = _LesAtmAddrSpec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 1, 1, 3),
    _LesAtmAddrSpec_Type()
)
lesAtmAddrSpec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesAtmAddrSpec.setStatus("mandatory")


class _LesAtmAddrMask_Type(OctetString):
    """Custom type lesAtmAddrMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LesAtmAddrMask_Type.__name__ = "OctetString"
_LesAtmAddrMask_Object = MibTableColumn
lesAtmAddrMask = _LesAtmAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 1, 1, 4),
    _LesAtmAddrMask_Type()
)
lesAtmAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesAtmAddrMask.setStatus("mandatory")
_LesAtmAddrActual_Type = AtmLaneAddress
_LesAtmAddrActual_Object = MibTableColumn
lesAtmAddrActual = _LesAtmAddrActual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 1, 1, 5),
    _LesAtmAddrActual_Type()
)
lesAtmAddrActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesAtmAddrActual.setStatus("mandatory")
_LesIfIndex_Type = Integer32
_LesIfIndex_Object = MibTableColumn
lesIfIndex = _LesIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 1, 1, 6),
    _LesIfIndex_Type()
)
lesIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesIfIndex.setStatus("mandatory")
_LesSubIfNum_Type = Integer32
_LesSubIfNum_Object = MibTableColumn
lesSubIfNum = _LesSubIfNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 1, 1, 7),
    _LesSubIfNum_Type()
)
lesSubIfNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesSubIfNum.setStatus("mandatory")
_LesColocBusAtmAddrSpec_Type = AtmLaneAddress
_LesColocBusAtmAddrSpec_Object = MibTableColumn
lesColocBusAtmAddrSpec = _LesColocBusAtmAddrSpec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 1, 1, 8),
    _LesColocBusAtmAddrSpec_Type()
)
lesColocBusAtmAddrSpec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesColocBusAtmAddrSpec.setStatus("mandatory")


class _LesColocBusAtmAddrMask_Type(OctetString):
    """Custom type lesColocBusAtmAddrMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LesColocBusAtmAddrMask_Type.__name__ = "OctetString"
_LesColocBusAtmAddrMask_Object = MibTableColumn
lesColocBusAtmAddrMask = _LesColocBusAtmAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 1, 1, 9),
    _LesColocBusAtmAddrMask_Type()
)
lesColocBusAtmAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesColocBusAtmAddrMask.setStatus("mandatory")
_LesColocBusAtmAddrActl_Type = AtmLaneAddress
_LesColocBusAtmAddrActl_Object = MibTableColumn
lesColocBusAtmAddrActl = _LesColocBusAtmAddrActl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 1, 1, 10),
    _LesColocBusAtmAddrActl_Type()
)
lesColocBusAtmAddrActl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesColocBusAtmAddrActl.setStatus("mandatory")
_LesUpTime_Type = TimeStamp
_LesUpTime_Object = MibTableColumn
lesUpTime = _LesUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 1, 1, 11),
    _LesUpTime_Type()
)
lesUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesUpTime.setStatus("mandatory")


class _LesLanType_Type(Integer32):
    """Custom type lesLanType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dot3", 1),
          ("dot5", 2))
    )


_LesLanType_Type.__name__ = "Integer32"
_LesLanType_Object = MibTableColumn
lesLanType = _LesLanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 1, 1, 12),
    _LesLanType_Type()
)
lesLanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesLanType.setStatus("mandatory")


class _LesMaxFrm_Type(Integer32):
    """Custom type lesMaxFrm based on Integer32"""
    defaultValue = 1516

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1516,
              4544,
              9234,
              18190)
        )
    )
    namedValues = NamedValues(
        *(("dot3", 1516),
          ("rfc1626", 9234),
          ("tr16Mb", 18190),
          ("tr4Mb", 4544))
    )


_LesMaxFrm_Type.__name__ = "Integer32"
_LesMaxFrm_Object = MibTableColumn
lesMaxFrm = _LesMaxFrm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 1, 1, 13),
    _LesMaxFrm_Type()
)
lesMaxFrm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesMaxFrm.setStatus("mandatory")


class _LesJoinTimeout_Type(Integer32):
    """Custom type lesJoinTimeout based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_LesJoinTimeout_Type.__name__ = "Integer32"
_LesJoinTimeout_Object = MibTableColumn
lesJoinTimeout = _LesJoinTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 1, 1, 14),
    _LesJoinTimeout_Type()
)
lesJoinTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesJoinTimeout.setStatus("mandatory")
_LesLecsAtmAddr_Type = AtmLaneAddress
_LesLecsAtmAddr_Object = MibTableColumn
lesLecsAtmAddr = _LesLecsAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 1, 1, 15),
    _LesLecsAtmAddr_Type()
)
lesLecsAtmAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesLecsAtmAddr.setStatus("mandatory")
_LesControlDistVpi_Type = CiscoVpiInteger
_LesControlDistVpi_Object = MibTableColumn
lesControlDistVpi = _LesControlDistVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 1, 1, 16),
    _LesControlDistVpi_Type()
)
lesControlDistVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesControlDistVpi.setStatus("mandatory")
_LesControlDistVci_Type = CiscoVciInteger
_LesControlDistVci_Object = MibTableColumn
lesControlDistVci = _LesControlDistVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 1, 1, 17),
    _LesControlDistVci_Type()
)
lesControlDistVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesControlDistVci.setStatus("mandatory")


class _LesOperStatus_Type(Integer32):
    """Custom type lesOperStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_LesOperStatus_Type.__name__ = "Integer32"
_LesOperStatus_Object = MibTableColumn
lesOperStatus = _LesOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 1, 1, 18),
    _LesOperStatus_Type()
)
lesOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesOperStatus.setStatus("mandatory")


class _LesAdminStatus_Type(Integer32):
    """Custom type lesAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_LesAdminStatus_Type.__name__ = "Integer32"
_LesAdminStatus_Object = MibTableColumn
lesAdminStatus = _LesAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 1, 1, 19),
    _LesAdminStatus_Type()
)
lesAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesAdminStatus.setStatus("mandatory")
_LesStatus_Type = RowStatus
_LesStatus_Object = MibTableColumn
lesStatus = _LesStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 1, 1, 20),
    _LesStatus_Type()
)
lesStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesStatus.setStatus("mandatory")


class _LesSegmentID_Type(Integer32):
    """Custom type lesSegmentID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_LesSegmentID_Type.__name__ = "Integer32"
_LesSegmentID_Object = MibTableColumn
lesSegmentID = _LesSegmentID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 1, 1, 21),
    _LesSegmentID_Type()
)
lesSegmentID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesSegmentID.setStatus("mandatory")
_LesStatsTable_Object = MibTable
lesStatsTable = _LesStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 2)
)
if mibBuilder.loadTexts:
    lesStatsTable.setStatus("mandatory")
_LesStatsEntry_Object = MibTableRow
lesStatsEntry = _LesStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 2, 1)
)
lesStatsEntry.setIndexNames(
    (0, "CISCO-LES-MIB", "lesElanName"),
    (0, "CISCO-LES-MIB", "lesIndex"),
)
if mibBuilder.loadTexts:
    lesStatsEntry.setStatus("mandatory")
_LesInErrors_Type = Counter32
_LesInErrors_Object = MibTableColumn
lesInErrors = _LesInErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 2, 1, 1),
    _LesInErrors_Type()
)
lesInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesInErrors.setStatus("mandatory")
_LesInErrorLastLec_Type = AtmLaneAddress
_LesInErrorLastLec_Object = MibTableColumn
lesInErrorLastLec = _LesInErrorLastLec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 2, 1, 2),
    _LesInErrorLastLec_Type()
)
lesInErrorLastLec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesInErrorLastLec.setStatus("mandatory")
_LesInFlushReplies_Type = Counter32
_LesInFlushReplies_Object = MibTableColumn
lesInFlushReplies = _LesInFlushReplies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 2, 1, 3),
    _LesInFlushReplies_Type()
)
lesInFlushReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesInFlushReplies.setStatus("mandatory")
_LesInJoinReqs_Type = Counter32
_LesInJoinReqs_Object = MibTableColumn
lesInJoinReqs = _LesInJoinReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 2, 1, 4),
    _LesInJoinReqs_Type()
)
lesInJoinReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesInJoinReqs.setStatus("mandatory")
_LesOutJoinFails_Type = Counter32
_LesOutJoinFails_Object = MibTableColumn
lesOutJoinFails = _LesOutJoinFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 2, 1, 5),
    _LesOutJoinFails_Type()
)
lesOutJoinFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesOutJoinFails.setStatus("mandatory")
_LesJoinLastFailCause_Type = Integer32
_LesJoinLastFailCause_Object = MibTableColumn
lesJoinLastFailCause = _LesJoinLastFailCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 2, 1, 6),
    _LesJoinLastFailCause_Type()
)
lesJoinLastFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesJoinLastFailCause.setStatus("mandatory")
_LesJoinLastFailLec_Type = AtmLaneAddress
_LesJoinLastFailLec_Object = MibTableColumn
lesJoinLastFailLec = _LesJoinLastFailLec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 2, 1, 7),
    _LesJoinLastFailLec_Type()
)
lesJoinLastFailLec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesJoinLastFailLec.setStatus("mandatory")
_LesOutConfigReqs_Type = Counter32
_LesOutConfigReqs_Object = MibTableColumn
lesOutConfigReqs = _LesOutConfigReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 2, 1, 8),
    _LesOutConfigReqs_Type()
)
lesOutConfigReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesOutConfigReqs.setStatus("mandatory")
_LesInConfigResps_Type = Counter32
_LesInConfigResps_Object = MibTableColumn
lesInConfigResps = _LesInConfigResps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 2, 1, 9),
    _LesInConfigResps_Type()
)
lesInConfigResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesInConfigResps.setStatus("mandatory")
_LesInConfigFails_Type = Counter32
_LesInConfigFails_Object = MibTableColumn
lesInConfigFails = _LesInConfigFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 2, 1, 10),
    _LesInConfigFails_Type()
)
lesInConfigFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesInConfigFails.setStatus("mandatory")
_LesInRegisReqs_Type = Counter32
_LesInRegisReqs_Object = MibTableColumn
lesInRegisReqs = _LesInRegisReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 2, 1, 11),
    _LesInRegisReqs_Type()
)
lesInRegisReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesInRegisReqs.setStatus("mandatory")
_LesOutRegisFails_Type = Counter32
_LesOutRegisFails_Object = MibTableColumn
lesOutRegisFails = _LesOutRegisFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 2, 1, 12),
    _LesOutRegisFails_Type()
)
lesOutRegisFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesOutRegisFails.setStatus("mandatory")
_LesRegisLastFailCause_Type = Integer32
_LesRegisLastFailCause_Object = MibTableColumn
lesRegisLastFailCause = _LesRegisLastFailCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 2, 1, 13),
    _LesRegisLastFailCause_Type()
)
lesRegisLastFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesRegisLastFailCause.setStatus("mandatory")
_LesRegisLastFailLec_Type = AtmLaneAddress
_LesRegisLastFailLec_Object = MibTableColumn
lesRegisLastFailLec = _LesRegisLastFailLec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 2, 1, 14),
    _LesRegisLastFailLec_Type()
)
lesRegisLastFailLec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesRegisLastFailLec.setStatus("mandatory")
_LesInUnregReqs_Type = Counter32
_LesInUnregReqs_Object = MibTableColumn
lesInUnregReqs = _LesInUnregReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 2, 1, 15),
    _LesInUnregReqs_Type()
)
lesInUnregReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesInUnregReqs.setStatus("mandatory")
_LesInLearpUcasts_Type = Counter32
_LesInLearpUcasts_Object = MibTableColumn
lesInLearpUcasts = _LesInLearpUcasts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 2, 1, 16),
    _LesInLearpUcasts_Type()
)
lesInLearpUcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesInLearpUcasts.setStatus("mandatory")
_LesInLearpBroadcasts_Type = Counter32
_LesInLearpBroadcasts_Object = MibTableColumn
lesInLearpBroadcasts = _LesInLearpBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 2, 1, 17),
    _LesInLearpBroadcasts_Type()
)
lesInLearpBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesInLearpBroadcasts.setStatus("mandatory")
_LesOutLearpFwd_Type = Counter32
_LesOutLearpFwd_Object = MibTableColumn
lesOutLearpFwd = _LesOutLearpFwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 2, 1, 18),
    _LesOutLearpFwd_Type()
)
lesOutLearpFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesOutLearpFwd.setStatus("mandatory")
_LesInLearpResps_Type = Counter32
_LesInLearpResps_Object = MibTableColumn
lesInLearpResps = _LesInLearpResps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 2, 1, 19),
    _LesInLearpResps_Type()
)
lesInLearpResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesInLearpResps.setStatus("mandatory")
_LesInNarpReqs_Type = Counter32
_LesInNarpReqs_Object = MibTableColumn
lesInNarpReqs = _LesInNarpReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 2, 1, 20),
    _LesInNarpReqs_Type()
)
lesInNarpReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesInNarpReqs.setStatus("mandatory")
_LesInTopolReqs_Type = Counter32
_LesInTopolReqs_Object = MibTableColumn
lesInTopolReqs = _LesInTopolReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 1, 2, 1, 21),
    _LesInTopolReqs_Type()
)
lesInTopolReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesInTopolReqs.setStatus("mandatory")
_LeClient_ObjectIdentity = ObjectIdentity
leClient = _LeClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 2)
)
_LesClientTable_Object = MibTable
lesClientTable = _LesClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lesClientTable.setStatus("mandatory")
_LesClientEntry_Object = MibTableRow
lesClientEntry = _LesClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 2, 1, 1)
)
lesClientEntry.setIndexNames(
    (0, "CISCO-LES-MIB", "lesElanName"),
    (0, "CISCO-LES-MIB", "lesIndex"),
    (0, "CISCO-LES-MIB", "lesClientLecid"),
)
if mibBuilder.loadTexts:
    lesClientEntry.setStatus("mandatory")


class _LesClientLecid_Type(Integer32):
    """Custom type lesClientLecid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65279),
    )


_LesClientLecid_Type.__name__ = "Integer32"
_LesClientLecid_Object = MibTableColumn
lesClientLecid = _LesClientLecid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 2, 1, 1, 1),
    _LesClientLecid_Type()
)
lesClientLecid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lesClientLecid.setStatus("mandatory")
_LesClientAtmAddr_Type = AtmLaneAddress
_LesClientAtmAddr_Object = MibTableColumn
lesClientAtmAddr = _LesClientAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 2, 1, 1, 2),
    _LesClientAtmAddr_Type()
)
lesClientAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesClientAtmAddr.setStatus("mandatory")


class _LesClientState_Type(Integer32):
    """Custom type lesClientState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("addLec", 4),
          ("busConnect", 5),
          ("connected", 1),
          ("joinRecv", 2),
          ("operational", 6),
          ("terminating", 7),
          ("verify", 3))
    )


_LesClientState_Type.__name__ = "Integer32"
_LesClientState_Object = MibTableColumn
lesClientState = _LesClientState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 2, 1, 1, 3),
    _LesClientState_Type()
)
lesClientState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesClientState.setStatus("mandatory")
_LesClientIfIndex_Type = Integer32
_LesClientIfIndex_Object = MibTableColumn
lesClientIfIndex = _LesClientIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 2, 1, 1, 4),
    _LesClientIfIndex_Type()
)
lesClientIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesClientIfIndex.setStatus("mandatory")
_LesClientControlVpi_Type = CiscoVpiInteger
_LesClientControlVpi_Object = MibTableColumn
lesClientControlVpi = _LesClientControlVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 2, 1, 1, 5),
    _LesClientControlVpi_Type()
)
lesClientControlVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesClientControlVpi.setStatus("mandatory")
_LesClientControlVci_Type = CiscoVciInteger
_LesClientControlVci_Object = MibTableColumn
lesClientControlVci = _LesClientControlVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 2, 1, 1, 6),
    _LesClientControlVci_Type()
)
lesClientControlVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesClientControlVci.setStatus("mandatory")
_LesClientStatus_Type = RowStatus
_LesClientStatus_Object = MibTableColumn
lesClientStatus = _LesClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 2, 1, 1, 7),
    _LesClientStatus_Type()
)
lesClientStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesClientStatus.setStatus("mandatory")
_Register_ObjectIdentity = ObjectIdentity
register = _Register_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 3)
)
_LesMacRegTable_Object = MibTable
lesMacRegTable = _LesMacRegTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 3, 1)
)
if mibBuilder.loadTexts:
    lesMacRegTable.setStatus("mandatory")
_LesMacRegEntry_Object = MibTableRow
lesMacRegEntry = _LesMacRegEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 3, 1, 1)
)
lesMacRegEntry.setIndexNames(
    (0, "CISCO-LES-MIB", "lesElanName"),
    (0, "CISCO-LES-MIB", "lesIndex"),
    (0, "CISCO-LES-MIB", "lesMacRegMacAddress"),
)
if mibBuilder.loadTexts:
    lesMacRegEntry.setStatus("mandatory")
_LesMacRegMacAddress_Type = MacAddress
_LesMacRegMacAddress_Object = MibTableColumn
lesMacRegMacAddress = _LesMacRegMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 3, 1, 1, 1),
    _LesMacRegMacAddress_Type()
)
lesMacRegMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lesMacRegMacAddress.setStatus("mandatory")
_LesMacRegAtmAddr_Type = AtmLaneAddress
_LesMacRegAtmAddr_Object = MibTableColumn
lesMacRegAtmAddr = _LesMacRegAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 3, 1, 1, 3),
    _LesMacRegAtmAddr_Type()
)
lesMacRegAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesMacRegAtmAddr.setStatus("mandatory")


class _LesMacRegLecid_Type(Integer32):
    """Custom type lesMacRegLecid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65279),
    )


_LesMacRegLecid_Type.__name__ = "Integer32"
_LesMacRegLecid_Object = MibTableColumn
lesMacRegLecid = _LesMacRegLecid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 3, 1, 1, 4),
    _LesMacRegLecid_Type()
)
lesMacRegLecid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesMacRegLecid.setStatus("mandatory")
_LesRDRegTable_Object = MibTable
lesRDRegTable = _LesRDRegTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 3, 2)
)
if mibBuilder.loadTexts:
    lesRDRegTable.setStatus("mandatory")
_LesRDRegEntry_Object = MibTableRow
lesRDRegEntry = _LesRDRegEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 3, 2, 1)
)
lesRDRegEntry.setIndexNames(
    (0, "CISCO-LES-MIB", "lesElanName"),
    (0, "CISCO-LES-MIB", "lesIndex"),
    (0, "CISCO-LES-MIB", "lesRDRegSegmentId"),
    (0, "CISCO-LES-MIB", "lesRDRegBridgeNum"),
)
if mibBuilder.loadTexts:
    lesRDRegEntry.setStatus("mandatory")


class _LesRDRegSegmentId_Type(Integer32):
    """Custom type lesRDRegSegmentId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_LesRDRegSegmentId_Type.__name__ = "Integer32"
_LesRDRegSegmentId_Object = MibTableColumn
lesRDRegSegmentId = _LesRDRegSegmentId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 3, 2, 1, 1),
    _LesRDRegSegmentId_Type()
)
lesRDRegSegmentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lesRDRegSegmentId.setStatus("mandatory")


class _LesRDRegBridgeNum_Type(Integer32):
    """Custom type lesRDRegBridgeNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_LesRDRegBridgeNum_Type.__name__ = "Integer32"
_LesRDRegBridgeNum_Object = MibTableColumn
lesRDRegBridgeNum = _LesRDRegBridgeNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 3, 2, 1, 2),
    _LesRDRegBridgeNum_Type()
)
lesRDRegBridgeNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lesRDRegBridgeNum.setStatus("mandatory")
_LesRDRegAtmAddr_Type = AtmLaneAddress
_LesRDRegAtmAddr_Object = MibTableColumn
lesRDRegAtmAddr = _LesRDRegAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 3, 2, 1, 3),
    _LesRDRegAtmAddr_Type()
)
lesRDRegAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesRDRegAtmAddr.setStatus("mandatory")


class _LesRDRegLecid_Type(Integer32):
    """Custom type lesRDRegLecid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65279),
    )


_LesRDRegLecid_Type.__name__ = "Integer32"
_LesRDRegLecid_Object = MibTableColumn
lesRDRegLecid = _LesRDRegLecid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 1, 3, 2, 1, 4),
    _LesRDRegLecid_Type()
)
lesRDRegLecid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesRDRegLecid.setStatus("mandatory")
_CiscoLesMIBConformance_ObjectIdentity = ObjectIdentity
ciscoLesMIBConformance = _CiscoLesMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 2)
)
_CiscoLesMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLesMIBGroups = _CiscoLesMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 2, 1)
)
_CiscoLesGroup_ObjectIdentity = ObjectIdentity
ciscoLesGroup = _CiscoLesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 2, 1, 1)
)
_CiscoLesStatsGroup_ObjectIdentity = ObjectIdentity
ciscoLesStatsGroup = _CiscoLesStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 2, 1, 2)
)
_CiscoLesColocatedGroup_ObjectIdentity = ObjectIdentity
ciscoLesColocatedGroup = _CiscoLesColocatedGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 2, 1, 3)
)
_CiscoLesLecsGroup_ObjectIdentity = ObjectIdentity
ciscoLesLecsGroup = _CiscoLesLecsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 2, 1, 4)
)
_CiscoLesCntrlDistGroup_ObjectIdentity = ObjectIdentity
ciscoLesCntrlDistGroup = _CiscoLesCntrlDistGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 2, 1, 5)
)
_CiscoLesSubIfGroup_ObjectIdentity = ObjectIdentity
ciscoLesSubIfGroup = _CiscoLesSubIfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 2, 1, 6)
)
_CiscoLesClientGroup_ObjectIdentity = ObjectIdentity
ciscoLesClientGroup = _CiscoLesClientGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 2, 1, 7)
)
_CiscoLesTokenRingGroup_ObjectIdentity = ObjectIdentity
ciscoLesTokenRingGroup = _CiscoLesTokenRingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 2, 1, 8)
)
_CiscoLesMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLesMIBCompliances = _CiscoLesMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 2, 2)
)
_CiscoLesMIBCompliance_ObjectIdentity = ObjectIdentity
ciscoLesMIBCompliance = _CiscoLesMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 39, 2, 2, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LES-MIB",
    **{"ciscoLesMIB": ciscoLesMIB,
       "ciscoLesMIBObjects": ciscoLesMIBObjects,
       "les": les,
       "lesTable": lesTable,
       "lesEntry": lesEntry,
       "lesElanName": lesElanName,
       "lesIndex": lesIndex,
       "lesAtmAddrSpec": lesAtmAddrSpec,
       "lesAtmAddrMask": lesAtmAddrMask,
       "lesAtmAddrActual": lesAtmAddrActual,
       "lesIfIndex": lesIfIndex,
       "lesSubIfNum": lesSubIfNum,
       "lesColocBusAtmAddrSpec": lesColocBusAtmAddrSpec,
       "lesColocBusAtmAddrMask": lesColocBusAtmAddrMask,
       "lesColocBusAtmAddrActl": lesColocBusAtmAddrActl,
       "lesUpTime": lesUpTime,
       "lesLanType": lesLanType,
       "lesMaxFrm": lesMaxFrm,
       "lesJoinTimeout": lesJoinTimeout,
       "lesLecsAtmAddr": lesLecsAtmAddr,
       "lesControlDistVpi": lesControlDistVpi,
       "lesControlDistVci": lesControlDistVci,
       "lesOperStatus": lesOperStatus,
       "lesAdminStatus": lesAdminStatus,
       "lesStatus": lesStatus,
       "lesSegmentID": lesSegmentID,
       "lesStatsTable": lesStatsTable,
       "lesStatsEntry": lesStatsEntry,
       "lesInErrors": lesInErrors,
       "lesInErrorLastLec": lesInErrorLastLec,
       "lesInFlushReplies": lesInFlushReplies,
       "lesInJoinReqs": lesInJoinReqs,
       "lesOutJoinFails": lesOutJoinFails,
       "lesJoinLastFailCause": lesJoinLastFailCause,
       "lesJoinLastFailLec": lesJoinLastFailLec,
       "lesOutConfigReqs": lesOutConfigReqs,
       "lesInConfigResps": lesInConfigResps,
       "lesInConfigFails": lesInConfigFails,
       "lesInRegisReqs": lesInRegisReqs,
       "lesOutRegisFails": lesOutRegisFails,
       "lesRegisLastFailCause": lesRegisLastFailCause,
       "lesRegisLastFailLec": lesRegisLastFailLec,
       "lesInUnregReqs": lesInUnregReqs,
       "lesInLearpUcasts": lesInLearpUcasts,
       "lesInLearpBroadcasts": lesInLearpBroadcasts,
       "lesOutLearpFwd": lesOutLearpFwd,
       "lesInLearpResps": lesInLearpResps,
       "lesInNarpReqs": lesInNarpReqs,
       "lesInTopolReqs": lesInTopolReqs,
       "leClient": leClient,
       "lesClientTable": lesClientTable,
       "lesClientEntry": lesClientEntry,
       "lesClientLecid": lesClientLecid,
       "lesClientAtmAddr": lesClientAtmAddr,
       "lesClientState": lesClientState,
       "lesClientIfIndex": lesClientIfIndex,
       "lesClientControlVpi": lesClientControlVpi,
       "lesClientControlVci": lesClientControlVci,
       "lesClientStatus": lesClientStatus,
       "register": register,
       "lesMacRegTable": lesMacRegTable,
       "lesMacRegEntry": lesMacRegEntry,
       "lesMacRegMacAddress": lesMacRegMacAddress,
       "lesMacRegAtmAddr": lesMacRegAtmAddr,
       "lesMacRegLecid": lesMacRegLecid,
       "lesRDRegTable": lesRDRegTable,
       "lesRDRegEntry": lesRDRegEntry,
       "lesRDRegSegmentId": lesRDRegSegmentId,
       "lesRDRegBridgeNum": lesRDRegBridgeNum,
       "lesRDRegAtmAddr": lesRDRegAtmAddr,
       "lesRDRegLecid": lesRDRegLecid,
       "ciscoLesMIBConformance": ciscoLesMIBConformance,
       "ciscoLesMIBGroups": ciscoLesMIBGroups,
       "ciscoLesGroup": ciscoLesGroup,
       "ciscoLesStatsGroup": ciscoLesStatsGroup,
       "ciscoLesColocatedGroup": ciscoLesColocatedGroup,
       "ciscoLesLecsGroup": ciscoLesLecsGroup,
       "ciscoLesCntrlDistGroup": ciscoLesCntrlDistGroup,
       "ciscoLesSubIfGroup": ciscoLesSubIfGroup,
       "ciscoLesClientGroup": ciscoLesClientGroup,
       "ciscoLesTokenRingGroup": ciscoLesTokenRingGroup,
       "ciscoLesMIBCompliances": ciscoLesMIBCompliances,
       "ciscoLesMIBCompliance": ciscoLesMIBCompliance}
)
