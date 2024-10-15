# SNMP MIB module (PDN-DSL-ATM-BOND-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-DSL-ATM-BOND-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:35 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(pdn_interfaces,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-interfaces")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TruthValue")


# MODULE-IDENTITY

pdnDslAtmBondMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33)
)
pdnDslAtmBondMIB.setRevisions(
        ("2005-08-03 00:00",
         "2005-08-01 00:00",
         "2005-07-26 00:00",
         "2005-06-07 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PdnDslAtmBondGroupIndexTC(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class PdnDslAtmBondGroupIdentityTC(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class PdnDslAtmBondGroupBearerNumberTC(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )



class PdnDslAtmBondLinkStatusAsmTC(Integer32, TextualConvention):
    status = "current"
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
        *(("acceptableToCarryBondedTraffic", 3),
          ("notProvisioned", 1),
          ("selectedToCarryBondedTraffic", 4),
          ("shouldNotBeUsed", 2))
    )



class PdnDslAtmBondAsmRxStatusTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notReceivedASM", 2),
          ("receivedASM", 1))
    )



class PdnDslAtmBondGroupDataRateTC(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )



class PdnDslAtmBondGroupDiffDelayTolTC(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class PdnDslAtmBondGroupStatusTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("operational", 1),
          ("unavailable", 2))
    )



class PdnDslAtmBondGroupFailReasonTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("atucDiffDelayExceeded", 5),
          ("atucMinDataRateNotMet", 3),
          ("aturDiffDelayExceeded", 6),
          ("aturMinDataRateNotMet", 4),
          ("notApplicable", 1),
          ("unknown", 2))
    )



# MIB Managed Objects in the order of their OIDs

_PdnDslAtmBondNotifications_ObjectIdentity = ObjectIdentity
pdnDslAtmBondNotifications = _PdnDslAtmBondNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 0)
)
_PdnDslAtmBondObjects_ObjectIdentity = ObjectIdentity
pdnDslAtmBondObjects = _PdnDslAtmBondObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1)
)
_PdnDslAtmBondNextGroupIndex_Type = TestAndIncr
_PdnDslAtmBondNextGroupIndex_Object = MibScalar
pdnDslAtmBondNextGroupIndex = _PdnDslAtmBondNextGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 1),
    _PdnDslAtmBondNextGroupIndex_Type()
)
pdnDslAtmBondNextGroupIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnDslAtmBondNextGroupIndex.setStatus("current")


class _PdnDslAtmBondNbrOfGroups_Type(Unsigned32):
    """Custom type pdnDslAtmBondNbrOfGroups based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdnDslAtmBondNbrOfGroups_Type.__name__ = "Unsigned32"
_PdnDslAtmBondNbrOfGroups_Object = MibScalar
pdnDslAtmBondNbrOfGroups = _PdnDslAtmBondNbrOfGroups_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 2),
    _PdnDslAtmBondNbrOfGroups_Type()
)
pdnDslAtmBondNbrOfGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDslAtmBondNbrOfGroups.setStatus("current")
_PdnDslAtmBondGroupTable_Object = MibTable
pdnDslAtmBondGroupTable = _PdnDslAtmBondGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 3)
)
if mibBuilder.loadTexts:
    pdnDslAtmBondGroupTable.setStatus("current")
_PdnDslAtmBondGroupEntry_Object = MibTableRow
pdnDslAtmBondGroupEntry = _PdnDslAtmBondGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 3, 1)
)
pdnDslAtmBondGroupEntry.setIndexNames(
    (0, "PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupIndex"),
)
if mibBuilder.loadTexts:
    pdnDslAtmBondGroupEntry.setStatus("current")
_PdnDslAtmBondGroupIndex_Type = PdnDslAtmBondGroupIndexTC
_PdnDslAtmBondGroupIndex_Object = MibTableColumn
pdnDslAtmBondGroupIndex = _PdnDslAtmBondGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 3, 1, 1),
    _PdnDslAtmBondGroupIndex_Type()
)
pdnDslAtmBondGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnDslAtmBondGroupIndex.setStatus("current")
_PdnDslAtmBondGroupRowStatus_Type = RowStatus
_PdnDslAtmBondGroupRowStatus_Object = MibTableColumn
pdnDslAtmBondGroupRowStatus = _PdnDslAtmBondGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 3, 1, 2),
    _PdnDslAtmBondGroupRowStatus_Type()
)
pdnDslAtmBondGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnDslAtmBondGroupRowStatus.setStatus("current")


class _PdnDslAtmBondGroupNbrRefs_Type(Unsigned32):
    """Custom type pdnDslAtmBondGroupNbrRefs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdnDslAtmBondGroupNbrRefs_Type.__name__ = "Unsigned32"
_PdnDslAtmBondGroupNbrRefs_Object = MibTableColumn
pdnDslAtmBondGroupNbrRefs = _PdnDslAtmBondGroupNbrRefs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 3, 1, 3),
    _PdnDslAtmBondGroupNbrRefs_Type()
)
pdnDslAtmBondGroupNbrRefs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDslAtmBondGroupNbrRefs.setStatus("current")
_PdnDslAtmBondGroupIfIndex_Type = InterfaceIndex
_PdnDslAtmBondGroupIfIndex_Object = MibTableColumn
pdnDslAtmBondGroupIfIndex = _PdnDslAtmBondGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 3, 1, 4),
    _PdnDslAtmBondGroupIfIndex_Type()
)
pdnDslAtmBondGroupIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDslAtmBondGroupIfIndex.setStatus("current")
_PdnDslAtmBondGroupID_Type = PdnDslAtmBondGroupIdentityTC
_PdnDslAtmBondGroupID_Object = MibTableColumn
pdnDslAtmBondGroupID = _PdnDslAtmBondGroupID_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 3, 1, 5),
    _PdnDslAtmBondGroupID_Type()
)
pdnDslAtmBondGroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnDslAtmBondGroupID.setStatus("current")


class _PdnDslAtmBondGroupAlarmConfProfileName_Type(SnmpAdminString):
    """Custom type pdnDslAtmBondGroupAlarmConfProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 32),
    )


_PdnDslAtmBondGroupAlarmConfProfileName_Type.__name__ = "SnmpAdminString"
_PdnDslAtmBondGroupAlarmConfProfileName_Object = MibTableColumn
pdnDslAtmBondGroupAlarmConfProfileName = _PdnDslAtmBondGroupAlarmConfProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 3, 1, 6),
    _PdnDslAtmBondGroupAlarmConfProfileName_Type()
)
pdnDslAtmBondGroupAlarmConfProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnDslAtmBondGroupAlarmConfProfileName.setStatus("current")
_PdnDslAtmBondGroupAtucMaxNetDataRate_Type = PdnDslAtmBondGroupDataRateTC
_PdnDslAtmBondGroupAtucMaxNetDataRate_Object = MibTableColumn
pdnDslAtmBondGroupAtucMaxNetDataRate = _PdnDslAtmBondGroupAtucMaxNetDataRate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 3, 1, 7),
    _PdnDslAtmBondGroupAtucMaxNetDataRate_Type()
)
pdnDslAtmBondGroupAtucMaxNetDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnDslAtmBondGroupAtucMaxNetDataRate.setStatus("current")
if mibBuilder.loadTexts:
    pdnDslAtmBondGroupAtucMaxNetDataRate.setUnits("bps")
_PdnDslAtmBondGroupAturMaxNetDataRate_Type = PdnDslAtmBondGroupDataRateTC
_PdnDslAtmBondGroupAturMaxNetDataRate_Object = MibTableColumn
pdnDslAtmBondGroupAturMaxNetDataRate = _PdnDslAtmBondGroupAturMaxNetDataRate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 3, 1, 8),
    _PdnDslAtmBondGroupAturMaxNetDataRate_Type()
)
pdnDslAtmBondGroupAturMaxNetDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnDslAtmBondGroupAturMaxNetDataRate.setStatus("current")
if mibBuilder.loadTexts:
    pdnDslAtmBondGroupAturMaxNetDataRate.setUnits("bps")
_PdnDslAtmBondGroupAtucMinNetDataRate_Type = PdnDslAtmBondGroupDataRateTC
_PdnDslAtmBondGroupAtucMinNetDataRate_Object = MibTableColumn
pdnDslAtmBondGroupAtucMinNetDataRate = _PdnDslAtmBondGroupAtucMinNetDataRate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 3, 1, 9),
    _PdnDslAtmBondGroupAtucMinNetDataRate_Type()
)
pdnDslAtmBondGroupAtucMinNetDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnDslAtmBondGroupAtucMinNetDataRate.setStatus("current")
if mibBuilder.loadTexts:
    pdnDslAtmBondGroupAtucMinNetDataRate.setUnits("bps")
_PdnDslAtmBondGroupAturMinNetDataRate_Type = PdnDslAtmBondGroupDataRateTC
_PdnDslAtmBondGroupAturMinNetDataRate_Object = MibTableColumn
pdnDslAtmBondGroupAturMinNetDataRate = _PdnDslAtmBondGroupAturMinNetDataRate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 3, 1, 10),
    _PdnDslAtmBondGroupAturMinNetDataRate_Type()
)
pdnDslAtmBondGroupAturMinNetDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnDslAtmBondGroupAturMinNetDataRate.setStatus("current")
if mibBuilder.loadTexts:
    pdnDslAtmBondGroupAturMinNetDataRate.setUnits("bps")
_PdnDslAtmBondGroupAtucDiffDelay_Type = PdnDslAtmBondGroupDiffDelayTolTC
_PdnDslAtmBondGroupAtucDiffDelay_Object = MibTableColumn
pdnDslAtmBondGroupAtucDiffDelay = _PdnDslAtmBondGroupAtucDiffDelay_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 3, 1, 11),
    _PdnDslAtmBondGroupAtucDiffDelay_Type()
)
pdnDslAtmBondGroupAtucDiffDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnDslAtmBondGroupAtucDiffDelay.setStatus("current")
if mibBuilder.loadTexts:
    pdnDslAtmBondGroupAtucDiffDelay.setUnits("milliseconds")
_PdnDslAtmBondGroupAturDiffDelay_Type = PdnDslAtmBondGroupDiffDelayTolTC
_PdnDslAtmBondGroupAturDiffDelay_Object = MibTableColumn
pdnDslAtmBondGroupAturDiffDelay = _PdnDslAtmBondGroupAturDiffDelay_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 3, 1, 12),
    _PdnDslAtmBondGroupAturDiffDelay_Type()
)
pdnDslAtmBondGroupAturDiffDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnDslAtmBondGroupAturDiffDelay.setStatus("current")
if mibBuilder.loadTexts:
    pdnDslAtmBondGroupAturDiffDelay.setUnits("milliseconds")
_PdnDslAtmBondGroupStatusNotifyEnabled_Type = TruthValue
_PdnDslAtmBondGroupStatusNotifyEnabled_Object = MibTableColumn
pdnDslAtmBondGroupStatusNotifyEnabled = _PdnDslAtmBondGroupStatusNotifyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 3, 1, 13),
    _PdnDslAtmBondGroupStatusNotifyEnabled_Type()
)
pdnDslAtmBondGroupStatusNotifyEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnDslAtmBondGroupStatusNotifyEnabled.setStatus("current")
_PdnDslAtmBondMappingTable_Object = MibTable
pdnDslAtmBondMappingTable = _PdnDslAtmBondMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 4)
)
if mibBuilder.loadTexts:
    pdnDslAtmBondMappingTable.setStatus("current")
_PdnDslAtmBondMappingEntry_Object = MibTableRow
pdnDslAtmBondMappingEntry = _PdnDslAtmBondMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 4, 1)
)
pdnDslAtmBondMappingEntry.setIndexNames(
    (0, "PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondDslIfIndex"),
    (0, "PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondBearerNbr"),
)
if mibBuilder.loadTexts:
    pdnDslAtmBondMappingEntry.setStatus("current")
_PdnDslAtmBondDslIfIndex_Type = InterfaceIndex
_PdnDslAtmBondDslIfIndex_Object = MibTableColumn
pdnDslAtmBondDslIfIndex = _PdnDslAtmBondDslIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 4, 1, 1),
    _PdnDslAtmBondDslIfIndex_Type()
)
pdnDslAtmBondDslIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnDslAtmBondDslIfIndex.setStatus("current")
_PdnDslAtmBondBearerNbr_Type = PdnDslAtmBondGroupBearerNumberTC
_PdnDslAtmBondBearerNbr_Object = MibTableColumn
pdnDslAtmBondBearerNbr = _PdnDslAtmBondBearerNbr_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 4, 1, 2),
    _PdnDslAtmBondBearerNbr_Type()
)
pdnDslAtmBondBearerNbr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnDslAtmBondBearerNbr.setStatus("current")
_PdnDslAtmBondMappingRowStatus_Type = RowStatus
_PdnDslAtmBondMappingRowStatus_Object = MibTableColumn
pdnDslAtmBondMappingRowStatus = _PdnDslAtmBondMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 4, 1, 3),
    _PdnDslAtmBondMappingRowStatus_Type()
)
pdnDslAtmBondMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnDslAtmBondMappingRowStatus.setStatus("current")
_PdnDslAtmBondMappingGroupIndex_Type = PdnDslAtmBondGroupIndexTC
_PdnDslAtmBondMappingGroupIndex_Object = MibTableColumn
pdnDslAtmBondMappingGroupIndex = _PdnDslAtmBondMappingGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 4, 1, 4),
    _PdnDslAtmBondMappingGroupIndex_Type()
)
pdnDslAtmBondMappingGroupIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnDslAtmBondMappingGroupIndex.setStatus("current")
_PdnDslAtmBondGroupIndexMappingTable_Object = MibTable
pdnDslAtmBondGroupIndexMappingTable = _PdnDslAtmBondGroupIndexMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 5)
)
if mibBuilder.loadTexts:
    pdnDslAtmBondGroupIndexMappingTable.setStatus("current")
_PdnDslAtmBondGroupIndexMappingEntry_Object = MibTableRow
pdnDslAtmBondGroupIndexMappingEntry = _PdnDslAtmBondGroupIndexMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 5, 1)
)
pdnDslAtmBondGroupIndexMappingEntry.setIndexNames(
    (0, "PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupIfIndex"),
)
if mibBuilder.loadTexts:
    pdnDslAtmBondGroupIndexMappingEntry.setStatus("current")
_PdnDslAtmBondGroupIndexMappingIndex_Type = PdnDslAtmBondGroupIndexTC
_PdnDslAtmBondGroupIndexMappingIndex_Object = MibTableColumn
pdnDslAtmBondGroupIndexMappingIndex = _PdnDslAtmBondGroupIndexMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 5, 1, 1),
    _PdnDslAtmBondGroupIndexMappingIndex_Type()
)
pdnDslAtmBondGroupIndexMappingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDslAtmBondGroupIndexMappingIndex.setStatus("current")
_PdnDslAtmBondGroupInvMappingTable_Object = MibTable
pdnDslAtmBondGroupInvMappingTable = _PdnDslAtmBondGroupInvMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 6)
)
if mibBuilder.loadTexts:
    pdnDslAtmBondGroupInvMappingTable.setStatus("current")
_PdnDslAtmBondGroupInvMappingEntry_Object = MibTableRow
pdnDslAtmBondGroupInvMappingEntry = _PdnDslAtmBondGroupInvMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 6, 1)
)
pdnDslAtmBondGroupInvMappingEntry.setIndexNames(
    (0, "PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupIndex"),
    (0, "PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondDslIfIndex"),
)
if mibBuilder.loadTexts:
    pdnDslAtmBondGroupInvMappingEntry.setStatus("current")
_PdnDslAtmBondInvMappingBearerNbr_Type = PdnDslAtmBondGroupBearerNumberTC
_PdnDslAtmBondInvMappingBearerNbr_Object = MibTableColumn
pdnDslAtmBondInvMappingBearerNbr = _PdnDslAtmBondInvMappingBearerNbr_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 6, 1, 1),
    _PdnDslAtmBondInvMappingBearerNbr_Type()
)
pdnDslAtmBondInvMappingBearerNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDslAtmBondInvMappingBearerNbr.setStatus("current")
_PdnDslAtmBondPerfTable_Object = MibTable
pdnDslAtmBondPerfTable = _PdnDslAtmBondPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 7)
)
if mibBuilder.loadTexts:
    pdnDslAtmBondPerfTable.setStatus("current")
_PdnDslAtmBondPerfEntry_Object = MibTableRow
pdnDslAtmBondPerfEntry = _PdnDslAtmBondPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 7, 1)
)
pdnDslAtmBondPerfEntry.setIndexNames(
    (0, "PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupIndex"),
)
if mibBuilder.loadTexts:
    pdnDslAtmBondPerfEntry.setStatus("current")
_PdnDslAtmBondPerfCurrAtucNetDataRate_Type = PdnDslAtmBondGroupDataRateTC
_PdnDslAtmBondPerfCurrAtucNetDataRate_Object = MibTableColumn
pdnDslAtmBondPerfCurrAtucNetDataRate = _PdnDslAtmBondPerfCurrAtucNetDataRate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 7, 1, 1),
    _PdnDslAtmBondPerfCurrAtucNetDataRate_Type()
)
pdnDslAtmBondPerfCurrAtucNetDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDslAtmBondPerfCurrAtucNetDataRate.setStatus("current")
if mibBuilder.loadTexts:
    pdnDslAtmBondPerfCurrAtucNetDataRate.setUnits("bps")
_PdnDslAtmBondPerfCurrAturNetDataRate_Type = PdnDslAtmBondGroupDataRateTC
_PdnDslAtmBondPerfCurrAturNetDataRate_Object = MibTableColumn
pdnDslAtmBondPerfCurrAturNetDataRate = _PdnDslAtmBondPerfCurrAturNetDataRate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 7, 1, 2),
    _PdnDslAtmBondPerfCurrAturNetDataRate_Type()
)
pdnDslAtmBondPerfCurrAturNetDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDslAtmBondPerfCurrAturNetDataRate.setStatus("current")
if mibBuilder.loadTexts:
    pdnDslAtmBondPerfCurrAturNetDataRate.setUnits("bps")
_PdnDslAtmBondPerfPrevAtucNetDataRate_Type = PdnDslAtmBondGroupDataRateTC
_PdnDslAtmBondPerfPrevAtucNetDataRate_Object = MibTableColumn
pdnDslAtmBondPerfPrevAtucNetDataRate = _PdnDslAtmBondPerfPrevAtucNetDataRate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 7, 1, 3),
    _PdnDslAtmBondPerfPrevAtucNetDataRate_Type()
)
pdnDslAtmBondPerfPrevAtucNetDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDslAtmBondPerfPrevAtucNetDataRate.setStatus("current")
if mibBuilder.loadTexts:
    pdnDslAtmBondPerfPrevAtucNetDataRate.setUnits("bps")
_PdnDslAtmBondPerfPrevAturNetDataRate_Type = PdnDslAtmBondGroupDataRateTC
_PdnDslAtmBondPerfPrevAturNetDataRate_Object = MibTableColumn
pdnDslAtmBondPerfPrevAturNetDataRate = _PdnDslAtmBondPerfPrevAturNetDataRate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 7, 1, 4),
    _PdnDslAtmBondPerfPrevAturNetDataRate_Type()
)
pdnDslAtmBondPerfPrevAturNetDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDslAtmBondPerfPrevAturNetDataRate.setStatus("current")
if mibBuilder.loadTexts:
    pdnDslAtmBondPerfPrevAturNetDataRate.setUnits("bps")
_PdnDslAtmBondPerfGroupStatus_Type = PdnDslAtmBondGroupStatusTC
_PdnDslAtmBondPerfGroupStatus_Object = MibTableColumn
pdnDslAtmBondPerfGroupStatus = _PdnDslAtmBondPerfGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 7, 1, 5),
    _PdnDslAtmBondPerfGroupStatus_Type()
)
pdnDslAtmBondPerfGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDslAtmBondPerfGroupStatus.setStatus("current")
_PdnDslAtmBondPerfFailReason_Type = PdnDslAtmBondGroupFailReasonTC
_PdnDslAtmBondPerfFailReason_Object = MibTableColumn
pdnDslAtmBondPerfFailReason = _PdnDslAtmBondPerfFailReason_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 7, 1, 6),
    _PdnDslAtmBondPerfFailReason_Type()
)
pdnDslAtmBondPerfFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDslAtmBondPerfFailReason.setStatus("current")
_PdnDslAtmBondPerfFailCount_Type = Counter32
_PdnDslAtmBondPerfFailCount_Object = MibTableColumn
pdnDslAtmBondPerfFailCount = _PdnDslAtmBondPerfFailCount_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 7, 1, 7),
    _PdnDslAtmBondPerfFailCount_Type()
)
pdnDslAtmBondPerfFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDslAtmBondPerfFailCount.setStatus("current")
_PdnDslAtmBondPerfRunTime_Type = Counter32
_PdnDslAtmBondPerfRunTime_Object = MibTableColumn
pdnDslAtmBondPerfRunTime = _PdnDslAtmBondPerfRunTime_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 7, 1, 8),
    _PdnDslAtmBondPerfRunTime_Type()
)
pdnDslAtmBondPerfRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDslAtmBondPerfRunTime.setStatus("current")
if mibBuilder.loadTexts:
    pdnDslAtmBondPerfRunTime.setUnits("seconds")
_PdnDslAtmBondPerfUAS_Type = Counter32
_PdnDslAtmBondPerfUAS_Object = MibTableColumn
pdnDslAtmBondPerfUAS = _PdnDslAtmBondPerfUAS_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 7, 1, 9),
    _PdnDslAtmBondPerfUAS_Type()
)
pdnDslAtmBondPerfUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDslAtmBondPerfUAS.setStatus("current")
if mibBuilder.loadTexts:
    pdnDslAtmBondPerfUAS.setUnits("seconds")
_PdnDslAtmBondPerfAtucRxCellLoss_Type = Counter32
_PdnDslAtmBondPerfAtucRxCellLoss_Object = MibTableColumn
pdnDslAtmBondPerfAtucRxCellLoss = _PdnDslAtmBondPerfAtucRxCellLoss_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 7, 1, 10),
    _PdnDslAtmBondPerfAtucRxCellLoss_Type()
)
pdnDslAtmBondPerfAtucRxCellLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDslAtmBondPerfAtucRxCellLoss.setStatus("current")
_PdnDslAtmBondPerfAturRxCellLoss_Type = Counter32
_PdnDslAtmBondPerfAturRxCellLoss_Object = MibTableColumn
pdnDslAtmBondPerfAturRxCellLoss = _PdnDslAtmBondPerfAturRxCellLoss_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 7, 1, 11),
    _PdnDslAtmBondPerfAturRxCellLoss_Type()
)
pdnDslAtmBondPerfAturRxCellLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDslAtmBondPerfAturRxCellLoss.setStatus("current")
_PdnDslAtmBond15MinIntervalTable_Object = MibTable
pdnDslAtmBond15MinIntervalTable = _PdnDslAtmBond15MinIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 8)
)
if mibBuilder.loadTexts:
    pdnDslAtmBond15MinIntervalTable.setStatus("current")
_PdnDslAtmBond15MinIntervalEntry_Object = MibTableRow
pdnDslAtmBond15MinIntervalEntry = _PdnDslAtmBond15MinIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 8, 1)
)
pdnDslAtmBond15MinIntervalEntry.setIndexNames(
    (0, "PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupIndex"),
    (0, "PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBond15MinIntervalNumber"),
)
if mibBuilder.loadTexts:
    pdnDslAtmBond15MinIntervalEntry.setStatus("current")


class _PdnDslAtmBond15MinIntervalNumber_Type(Unsigned32):
    """Custom type pdnDslAtmBond15MinIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_PdnDslAtmBond15MinIntervalNumber_Type.__name__ = "Unsigned32"
_PdnDslAtmBond15MinIntervalNumber_Object = MibTableColumn
pdnDslAtmBond15MinIntervalNumber = _PdnDslAtmBond15MinIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 8, 1, 1),
    _PdnDslAtmBond15MinIntervalNumber_Type()
)
pdnDslAtmBond15MinIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnDslAtmBond15MinIntervalNumber.setStatus("current")
_PdnDslAtmBond15MinIntervalStartDateAndTime_Type = DateAndTime
_PdnDslAtmBond15MinIntervalStartDateAndTime_Object = MibTableColumn
pdnDslAtmBond15MinIntervalStartDateAndTime = _PdnDslAtmBond15MinIntervalStartDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 8, 1, 2),
    _PdnDslAtmBond15MinIntervalStartDateAndTime_Type()
)
pdnDslAtmBond15MinIntervalStartDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDslAtmBond15MinIntervalStartDateAndTime.setStatus("current")
_PdnDslAtmBond15MinIntervalFailCount_Type = Counter32
_PdnDslAtmBond15MinIntervalFailCount_Object = MibTableColumn
pdnDslAtmBond15MinIntervalFailCount = _PdnDslAtmBond15MinIntervalFailCount_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 8, 1, 3),
    _PdnDslAtmBond15MinIntervalFailCount_Type()
)
pdnDslAtmBond15MinIntervalFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDslAtmBond15MinIntervalFailCount.setStatus("current")
_PdnDslAtmBond15MinIntervalRunTime_Type = Counter32
_PdnDslAtmBond15MinIntervalRunTime_Object = MibTableColumn
pdnDslAtmBond15MinIntervalRunTime = _PdnDslAtmBond15MinIntervalRunTime_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 8, 1, 4),
    _PdnDslAtmBond15MinIntervalRunTime_Type()
)
pdnDslAtmBond15MinIntervalRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDslAtmBond15MinIntervalRunTime.setStatus("current")
_PdnDslAtmBond15MinIntervalUAS_Type = Counter32
_PdnDslAtmBond15MinIntervalUAS_Object = MibTableColumn
pdnDslAtmBond15MinIntervalUAS = _PdnDslAtmBond15MinIntervalUAS_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 8, 1, 5),
    _PdnDslAtmBond15MinIntervalUAS_Type()
)
pdnDslAtmBond15MinIntervalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDslAtmBond15MinIntervalUAS.setStatus("current")
_PdnDslAtmBond15MinIntervalAtucRxCellLoss_Type = Counter32
_PdnDslAtmBond15MinIntervalAtucRxCellLoss_Object = MibTableColumn
pdnDslAtmBond15MinIntervalAtucRxCellLoss = _PdnDslAtmBond15MinIntervalAtucRxCellLoss_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 8, 1, 6),
    _PdnDslAtmBond15MinIntervalAtucRxCellLoss_Type()
)
pdnDslAtmBond15MinIntervalAtucRxCellLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDslAtmBond15MinIntervalAtucRxCellLoss.setStatus("current")
_PdnDslAtmBond15MinIntervalAturRxCellLoss_Type = Counter32
_PdnDslAtmBond15MinIntervalAturRxCellLoss_Object = MibTableColumn
pdnDslAtmBond15MinIntervalAturRxCellLoss = _PdnDslAtmBond15MinIntervalAturRxCellLoss_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 8, 1, 7),
    _PdnDslAtmBond15MinIntervalAturRxCellLoss_Type()
)
pdnDslAtmBond15MinIntervalAturRxCellLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDslAtmBond15MinIntervalAturRxCellLoss.setStatus("current")
_PdnDslAtmBond1DayIntervalTable_Object = MibTable
pdnDslAtmBond1DayIntervalTable = _PdnDslAtmBond1DayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 9)
)
if mibBuilder.loadTexts:
    pdnDslAtmBond1DayIntervalTable.setStatus("current")
_PdnDslAtmBond1DayIntervalEntry_Object = MibTableRow
pdnDslAtmBond1DayIntervalEntry = _PdnDslAtmBond1DayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 9, 1)
)
pdnDslAtmBond1DayIntervalEntry.setIndexNames(
    (0, "PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupIndex"),
    (0, "PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBond1DayIntervalNumber"),
)
if mibBuilder.loadTexts:
    pdnDslAtmBond1DayIntervalEntry.setStatus("current")


class _PdnDslAtmBond1DayIntervalNumber_Type(Unsigned32):
    """Custom type pdnDslAtmBond1DayIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_PdnDslAtmBond1DayIntervalNumber_Type.__name__ = "Unsigned32"
_PdnDslAtmBond1DayIntervalNumber_Object = MibTableColumn
pdnDslAtmBond1DayIntervalNumber = _PdnDslAtmBond1DayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 9, 1, 1),
    _PdnDslAtmBond1DayIntervalNumber_Type()
)
pdnDslAtmBond1DayIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnDslAtmBond1DayIntervalNumber.setStatus("current")
_PdnDslAtmBond1DayIntervalStartDateAndTime_Type = DateAndTime
_PdnDslAtmBond1DayIntervalStartDateAndTime_Object = MibTableColumn
pdnDslAtmBond1DayIntervalStartDateAndTime = _PdnDslAtmBond1DayIntervalStartDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 9, 1, 2),
    _PdnDslAtmBond1DayIntervalStartDateAndTime_Type()
)
pdnDslAtmBond1DayIntervalStartDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDslAtmBond1DayIntervalStartDateAndTime.setStatus("current")
_PdnDslAtmBond1DayIntervalFailCount_Type = Counter32
_PdnDslAtmBond1DayIntervalFailCount_Object = MibTableColumn
pdnDslAtmBond1DayIntervalFailCount = _PdnDslAtmBond1DayIntervalFailCount_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 9, 1, 3),
    _PdnDslAtmBond1DayIntervalFailCount_Type()
)
pdnDslAtmBond1DayIntervalFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDslAtmBond1DayIntervalFailCount.setStatus("current")
_PdnDslAtmBond1DayIntervalRunTime_Type = Counter32
_PdnDslAtmBond1DayIntervalRunTime_Object = MibTableColumn
pdnDslAtmBond1DayIntervalRunTime = _PdnDslAtmBond1DayIntervalRunTime_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 9, 1, 4),
    _PdnDslAtmBond1DayIntervalRunTime_Type()
)
pdnDslAtmBond1DayIntervalRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDslAtmBond1DayIntervalRunTime.setStatus("current")
_PdnDslAtmBond1DayIntervalUAS_Type = Counter32
_PdnDslAtmBond1DayIntervalUAS_Object = MibTableColumn
pdnDslAtmBond1DayIntervalUAS = _PdnDslAtmBond1DayIntervalUAS_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 9, 1, 5),
    _PdnDslAtmBond1DayIntervalUAS_Type()
)
pdnDslAtmBond1DayIntervalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDslAtmBond1DayIntervalUAS.setStatus("current")
_PdnDslAtmBond1DayIntervalAtucRxCellLoss_Type = Counter32
_PdnDslAtmBond1DayIntervalAtucRxCellLoss_Object = MibTableColumn
pdnDslAtmBond1DayIntervalAtucRxCellLoss = _PdnDslAtmBond1DayIntervalAtucRxCellLoss_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 9, 1, 6),
    _PdnDslAtmBond1DayIntervalAtucRxCellLoss_Type()
)
pdnDslAtmBond1DayIntervalAtucRxCellLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDslAtmBond1DayIntervalAtucRxCellLoss.setStatus("current")
_PdnDslAtmBond1DayIntervalAturRxCellLoss_Type = Counter32
_PdnDslAtmBond1DayIntervalAturRxCellLoss_Object = MibTableColumn
pdnDslAtmBond1DayIntervalAturRxCellLoss = _PdnDslAtmBond1DayIntervalAturRxCellLoss_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 9, 1, 7),
    _PdnDslAtmBond1DayIntervalAturRxCellLoss_Type()
)
pdnDslAtmBond1DayIntervalAturRxCellLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDslAtmBond1DayIntervalAturRxCellLoss.setStatus("current")
_PdnDslAtmBondLinkTable_Object = MibTable
pdnDslAtmBondLinkTable = _PdnDslAtmBondLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 10)
)
if mibBuilder.loadTexts:
    pdnDslAtmBondLinkTable.setStatus("current")
_PdnDslAtmBondLinkEntry_Object = MibTableRow
pdnDslAtmBondLinkEntry = _PdnDslAtmBondLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 10, 1)
)
pdnDslAtmBondLinkEntry.setIndexNames(
    (0, "PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupIndex"),
    (0, "PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondDslIfIndex"),
)
if mibBuilder.loadTexts:
    pdnDslAtmBondLinkEntry.setStatus("current")
_PdnDslAtmBondLinkAtucRxLinkStatus_Type = PdnDslAtmBondLinkStatusAsmTC
_PdnDslAtmBondLinkAtucRxLinkStatus_Object = MibTableColumn
pdnDslAtmBondLinkAtucRxLinkStatus = _PdnDslAtmBondLinkAtucRxLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 10, 1, 1),
    _PdnDslAtmBondLinkAtucRxLinkStatus_Type()
)
pdnDslAtmBondLinkAtucRxLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDslAtmBondLinkAtucRxLinkStatus.setStatus("current")
_PdnDslAtmBondLinkAturRxLinkStatus_Type = PdnDslAtmBondLinkStatusAsmTC
_PdnDslAtmBondLinkAturRxLinkStatus_Object = MibTableColumn
pdnDslAtmBondLinkAturRxLinkStatus = _PdnDslAtmBondLinkAturRxLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 10, 1, 2),
    _PdnDslAtmBondLinkAturRxLinkStatus_Type()
)
pdnDslAtmBondLinkAturRxLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDslAtmBondLinkAturRxLinkStatus.setStatus("current")
_PdnDslAtmBondLinkAtucTxLinkStatus_Type = PdnDslAtmBondLinkStatusAsmTC
_PdnDslAtmBondLinkAtucTxLinkStatus_Object = MibTableColumn
pdnDslAtmBondLinkAtucTxLinkStatus = _PdnDslAtmBondLinkAtucTxLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 10, 1, 3),
    _PdnDslAtmBondLinkAtucTxLinkStatus_Type()
)
pdnDslAtmBondLinkAtucTxLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDslAtmBondLinkAtucTxLinkStatus.setStatus("current")
_PdnDslAtmBondLinkAturTxLinkStatus_Type = PdnDslAtmBondLinkStatusAsmTC
_PdnDslAtmBondLinkAturTxLinkStatus_Object = MibTableColumn
pdnDslAtmBondLinkAturTxLinkStatus = _PdnDslAtmBondLinkAturTxLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 10, 1, 4),
    _PdnDslAtmBondLinkAturTxLinkStatus_Type()
)
pdnDslAtmBondLinkAturTxLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDslAtmBondLinkAturTxLinkStatus.setStatus("current")
_PdnDslAtmBondLinkAtucAsmRxStatus_Type = PdnDslAtmBondAsmRxStatusTC
_PdnDslAtmBondLinkAtucAsmRxStatus_Object = MibTableColumn
pdnDslAtmBondLinkAtucAsmRxStatus = _PdnDslAtmBondLinkAtucAsmRxStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 10, 1, 5),
    _PdnDslAtmBondLinkAtucAsmRxStatus_Type()
)
pdnDslAtmBondLinkAtucAsmRxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDslAtmBondLinkAtucAsmRxStatus.setStatus("current")
_PdnDslAtmBondLinkAturAsmRxStatus_Type = PdnDslAtmBondAsmRxStatusTC
_PdnDslAtmBondLinkAturAsmRxStatus_Object = MibTableColumn
pdnDslAtmBondLinkAturAsmRxStatus = _PdnDslAtmBondLinkAturAsmRxStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 10, 1, 6),
    _PdnDslAtmBondLinkAturAsmRxStatus_Type()
)
pdnDslAtmBondLinkAturAsmRxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDslAtmBondLinkAturAsmRxStatus.setStatus("current")
_PdnDslAtmBondAlarmConfProfileTable_Object = MibTable
pdnDslAtmBondAlarmConfProfileTable = _PdnDslAtmBondAlarmConfProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 11)
)
if mibBuilder.loadTexts:
    pdnDslAtmBondAlarmConfProfileTable.setStatus("current")
_PdnDslAtmBondAlarmConfProfileEntry_Object = MibTableRow
pdnDslAtmBondAlarmConfProfileEntry = _PdnDslAtmBondAlarmConfProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 11, 1)
)
pdnDslAtmBondAlarmConfProfileEntry.setIndexNames(
    (1, "PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondAlarmConfProfileName"),
)
if mibBuilder.loadTexts:
    pdnDslAtmBondAlarmConfProfileEntry.setStatus("current")


class _PdnDslAtmBondAlarmConfProfileName_Type(SnmpAdminString):
    """Custom type pdnDslAtmBondAlarmConfProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PdnDslAtmBondAlarmConfProfileName_Type.__name__ = "SnmpAdminString"
_PdnDslAtmBondAlarmConfProfileName_Object = MibTableColumn
pdnDslAtmBondAlarmConfProfileName = _PdnDslAtmBondAlarmConfProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 11, 1, 1),
    _PdnDslAtmBondAlarmConfProfileName_Type()
)
pdnDslAtmBondAlarmConfProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnDslAtmBondAlarmConfProfileName.setStatus("current")
_PdnDslAtmBondAlarmConfRowStatus_Type = RowStatus
_PdnDslAtmBondAlarmConfRowStatus_Object = MibTableColumn
pdnDslAtmBondAlarmConfRowStatus = _PdnDslAtmBondAlarmConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 11, 1, 2),
    _PdnDslAtmBondAlarmConfRowStatus_Type()
)
pdnDslAtmBondAlarmConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnDslAtmBondAlarmConfRowStatus.setStatus("current")


class _PdnDslAtmBondAlarmConfNbrRefs_Type(Unsigned32):
    """Custom type pdnDslAtmBondAlarmConfNbrRefs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdnDslAtmBondAlarmConfNbrRefs_Type.__name__ = "Unsigned32"
_PdnDslAtmBondAlarmConfNbrRefs_Object = MibTableColumn
pdnDslAtmBondAlarmConfNbrRefs = _PdnDslAtmBondAlarmConfNbrRefs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 11, 1, 3),
    _PdnDslAtmBondAlarmConfNbrRefs_Type()
)
pdnDslAtmBondAlarmConfNbrRefs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDslAtmBondAlarmConfNbrRefs.setStatus("current")


class _PdnDslAtmBondAlarmConfAtucThreshRateUp_Type(Integer32):
    """Custom type pdnDslAtmBondAlarmConfAtucThreshRateUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdnDslAtmBondAlarmConfAtucThreshRateUp_Type.__name__ = "Integer32"
_PdnDslAtmBondAlarmConfAtucThreshRateUp_Object = MibTableColumn
pdnDslAtmBondAlarmConfAtucThreshRateUp = _PdnDslAtmBondAlarmConfAtucThreshRateUp_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 11, 1, 4),
    _PdnDslAtmBondAlarmConfAtucThreshRateUp_Type()
)
pdnDslAtmBondAlarmConfAtucThreshRateUp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnDslAtmBondAlarmConfAtucThreshRateUp.setStatus("current")
if mibBuilder.loadTexts:
    pdnDslAtmBondAlarmConfAtucThreshRateUp.setUnits("bps")


class _PdnDslAtmBondAlarmConfAturThreshRateUp_Type(Integer32):
    """Custom type pdnDslAtmBondAlarmConfAturThreshRateUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdnDslAtmBondAlarmConfAturThreshRateUp_Type.__name__ = "Integer32"
_PdnDslAtmBondAlarmConfAturThreshRateUp_Object = MibTableColumn
pdnDslAtmBondAlarmConfAturThreshRateUp = _PdnDslAtmBondAlarmConfAturThreshRateUp_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 11, 1, 5),
    _PdnDslAtmBondAlarmConfAturThreshRateUp_Type()
)
pdnDslAtmBondAlarmConfAturThreshRateUp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnDslAtmBondAlarmConfAturThreshRateUp.setStatus("current")
if mibBuilder.loadTexts:
    pdnDslAtmBondAlarmConfAturThreshRateUp.setUnits("bps")


class _PdnDslAtmBondAlarmConfAtucThreshRateDown_Type(Integer32):
    """Custom type pdnDslAtmBondAlarmConfAtucThreshRateDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdnDslAtmBondAlarmConfAtucThreshRateDown_Type.__name__ = "Integer32"
_PdnDslAtmBondAlarmConfAtucThreshRateDown_Object = MibTableColumn
pdnDslAtmBondAlarmConfAtucThreshRateDown = _PdnDslAtmBondAlarmConfAtucThreshRateDown_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 11, 1, 6),
    _PdnDslAtmBondAlarmConfAtucThreshRateDown_Type()
)
pdnDslAtmBondAlarmConfAtucThreshRateDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnDslAtmBondAlarmConfAtucThreshRateDown.setStatus("current")
if mibBuilder.loadTexts:
    pdnDslAtmBondAlarmConfAtucThreshRateDown.setUnits("bps")


class _PdnDslAtmBondAlarmConfAturThreshRateDown_Type(Integer32):
    """Custom type pdnDslAtmBondAlarmConfAturThreshRateDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdnDslAtmBondAlarmConfAturThreshRateDown_Type.__name__ = "Integer32"
_PdnDslAtmBondAlarmConfAturThreshRateDown_Object = MibTableColumn
pdnDslAtmBondAlarmConfAturThreshRateDown = _PdnDslAtmBondAlarmConfAturThreshRateDown_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 11, 1, 7),
    _PdnDslAtmBondAlarmConfAturThreshRateDown_Type()
)
pdnDslAtmBondAlarmConfAturThreshRateDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnDslAtmBondAlarmConfAturThreshRateDown.setStatus("current")
if mibBuilder.loadTexts:
    pdnDslAtmBondAlarmConfAturThreshRateDown.setUnits("bps")
_PdnDslAtmBondAFNs_ObjectIdentity = ObjectIdentity
pdnDslAtmBondAFNs = _PdnDslAtmBondAFNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 2)
)
_PdnDslAtmBondConformance_ObjectIdentity = ObjectIdentity
pdnDslAtmBondConformance = _PdnDslAtmBondConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3)
)
_PdnDslAtmBondCompliances_ObjectIdentity = ObjectIdentity
pdnDslAtmBondCompliances = _PdnDslAtmBondCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 1)
)
_PdnDslAtmBondGroups_ObjectIdentity = ObjectIdentity
pdnDslAtmBondGroups = _PdnDslAtmBondGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2)
)
_PdnDslAtmBondObjGroups_ObjectIdentity = ObjectIdentity
pdnDslAtmBondObjGroups = _PdnDslAtmBondObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1)
)
_PdnDslAtmBondAfnGroups_ObjectIdentity = ObjectIdentity
pdnDslAtmBondAfnGroups = _PdnDslAtmBondAfnGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 2)
)
_PdnDslAtmBondNtfyGroups_ObjectIdentity = ObjectIdentity
pdnDslAtmBondNtfyGroups = _PdnDslAtmBondNtfyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 3)
)

# Managed Objects groups

pdnDslAtmBondGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 1)
)
pdnDslAtmBondGroup.setObjects(
      *(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondNextGroupIndex"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondNbrOfGroups"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupRowStatus"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupNbrRefs"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupIfIndex"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupID"))
)
if mibBuilder.loadTexts:
    pdnDslAtmBondGroup.setStatus("current")

pdnDslAtmBondMaxRateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 2)
)
pdnDslAtmBondMaxRateGroup.setObjects(
      *(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupAtucMaxNetDataRate"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupAturMaxNetDataRate"))
)
if mibBuilder.loadTexts:
    pdnDslAtmBondMaxRateGroup.setStatus("current")

pdnDslAtmBondMinRateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 3)
)
pdnDslAtmBondMinRateGroup.setObjects(
      *(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupAtucMinNetDataRate"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupAturMinNetDataRate"))
)
if mibBuilder.loadTexts:
    pdnDslAtmBondMinRateGroup.setStatus("current")

pdnDslAtmBondDiffDelayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 4)
)
pdnDslAtmBondDiffDelayGroup.setObjects(
      *(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupAtucDiffDelay"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupAturDiffDelay"))
)
if mibBuilder.loadTexts:
    pdnDslAtmBondDiffDelayGroup.setStatus("current")

pdnDslAtmBondGroupStatusNotifyEnabledGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 5)
)
pdnDslAtmBondGroupStatusNotifyEnabledGroup.setObjects(
    ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupStatusNotifyEnabled")
)
if mibBuilder.loadTexts:
    pdnDslAtmBondGroupStatusNotifyEnabledGroup.setStatus("current")

pdnDslAtmBondMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 6)
)
pdnDslAtmBondMappingGroup.setObjects(
      *(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondMappingRowStatus"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondMappingGroupIndex"))
)
if mibBuilder.loadTexts:
    pdnDslAtmBondMappingGroup.setStatus("current")

pdnDslAtmBondIndexMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 7)
)
pdnDslAtmBondIndexMappingGroup.setObjects(
    ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupIndexMappingIndex")
)
if mibBuilder.loadTexts:
    pdnDslAtmBondIndexMappingGroup.setStatus("current")

pdnDslAtmBondInvMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 8)
)
pdnDslAtmBondInvMappingGroup.setObjects(
    ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondInvMappingBearerNbr")
)
if mibBuilder.loadTexts:
    pdnDslAtmBondInvMappingGroup.setStatus("current")

pdnDslAtmBondPerfAggDataRateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 9)
)
pdnDslAtmBondPerfAggDataRateGroup.setObjects(
      *(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondPerfCurrAtucNetDataRate"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondPerfCurrAturNetDataRate"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondPerfPrevAtucNetDataRate"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondPerfPrevAturNetDataRate"))
)
if mibBuilder.loadTexts:
    pdnDslAtmBondPerfAggDataRateGroup.setStatus("current")

pdnDslAtmBondPerfBondGroupStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 10)
)
pdnDslAtmBondPerfBondGroupStatusGroup.setObjects(
    ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondPerfGroupStatus")
)
if mibBuilder.loadTexts:
    pdnDslAtmBondPerfBondGroupStatusGroup.setStatus("current")

pdnDslAtmBondDateAndTimeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 11)
)
pdnDslAtmBondDateAndTimeGroup.setObjects(
      *(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBond15MinIntervalStartDateAndTime"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBond1DayIntervalStartDateAndTime"))
)
if mibBuilder.loadTexts:
    pdnDslAtmBondDateAndTimeGroup.setStatus("current")

pdnDslAtmBondRunTimeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 12)
)
pdnDslAtmBondRunTimeGroup.setObjects(
      *(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondPerfRunTime"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBond15MinIntervalRunTime"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBond1DayIntervalRunTime"))
)
if mibBuilder.loadTexts:
    pdnDslAtmBondRunTimeGroup.setStatus("current")

pdnDslAtmBondRxCellLossGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 13)
)
pdnDslAtmBondRxCellLossGroup.setObjects(
      *(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondPerfAtucRxCellLoss"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondPerfAturRxCellLoss"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBond15MinIntervalAtucRxCellLoss"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBond15MinIntervalAturRxCellLoss"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBond1DayIntervalAtucRxCellLoss"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBond1DayIntervalAturRxCellLoss"))
)
if mibBuilder.loadTexts:
    pdnDslAtmBondRxCellLossGroup.setStatus("current")

pdnDslAtmBondPerfFailReasonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 14)
)
pdnDslAtmBondPerfFailReasonGroup.setObjects(
    ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondPerfFailReason")
)
if mibBuilder.loadTexts:
    pdnDslAtmBondPerfFailReasonGroup.setStatus("current")

pdnDslAtmBondFailCountGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 15)
)
pdnDslAtmBondFailCountGroup.setObjects(
      *(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondPerfFailCount"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBond15MinIntervalFailCount"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBond1DayIntervalFailCount"))
)
if mibBuilder.loadTexts:
    pdnDslAtmBondFailCountGroup.setStatus("current")

pdnDslAtmBondUASGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 16)
)
pdnDslAtmBondUASGroup.setObjects(
      *(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondPerfUAS"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBond15MinIntervalUAS"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBond1DayIntervalUAS"))
)
if mibBuilder.loadTexts:
    pdnDslAtmBondUASGroup.setStatus("current")

pdnDslAtmBondTrafficCapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 17)
)
pdnDslAtmBondTrafficCapGroup.setObjects(
      *(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondLinkAtucRxLinkStatus"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondLinkAturRxLinkStatus"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondLinkAtucTxLinkStatus"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondLinkAturTxLinkStatus"))
)
if mibBuilder.loadTexts:
    pdnDslAtmBondTrafficCapGroup.setStatus("current")

pdnDslATmBondAsmRxStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 18)
)
pdnDslATmBondAsmRxStatusGroup.setObjects(
      *(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondLinkAtucAsmRxStatus"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondLinkAturAsmRxStatus"))
)
if mibBuilder.loadTexts:
    pdnDslATmBondAsmRxStatusGroup.setStatus("current")

pdnDslAtmBondAlarmConfProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 19)
)
pdnDslAtmBondAlarmConfProfileGroup.setObjects(
      *(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupAlarmConfProfileName"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondAlarmConfRowStatus"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondAlarmConfNbrRefs"))
)
if mibBuilder.loadTexts:
    pdnDslAtmBondAlarmConfProfileGroup.setStatus("current")

pdnDslAtmBondAlarmConfAtucThreshRateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 20)
)
pdnDslAtmBondAlarmConfAtucThreshRateGroup.setObjects(
      *(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondAlarmConfAtucThreshRateUp"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondAlarmConfAtucThreshRateDown"))
)
if mibBuilder.loadTexts:
    pdnDslAtmBondAlarmConfAtucThreshRateGroup.setStatus("current")

pdnDslAtmBondAlarmConfAturThreshRateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 21)
)
pdnDslAtmBondAlarmConfAturThreshRateGroup.setObjects(
      *(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondAlarmConfAturThreshRateUp"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondAlarmConfAturThreshRateDown"))
)
if mibBuilder.loadTexts:
    pdnDslAtmBondAlarmConfAturThreshRateGroup.setStatus("current")


# Notification objects

pdnDslAtmBondAtucRateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 0, 1)
)
pdnDslAtmBondAtucRateChange.setObjects(
      *(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupIfIndex"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondPerfCurrAtucNetDataRate"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondPerfPrevAtucNetDataRate"))
)
if mibBuilder.loadTexts:
    pdnDslAtmBondAtucRateChange.setStatus(
        "current"
    )

pdnDslAtmBondAturRateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 0, 2)
)
pdnDslAtmBondAturRateChange.setObjects(
      *(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupIfIndex"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondPerfCurrAturNetDataRate"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondPerfPrevAturNetDataRate"))
)
if mibBuilder.loadTexts:
    pdnDslAtmBondAturRateChange.setStatus(
        "current"
    )

pdnDslAtmBondGroupStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 0, 3)
)
pdnDslAtmBondGroupStatusChange.setObjects(
      *(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupIfIndex"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondPerfGroupStatus"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondPerfFailReason"))
)
if mibBuilder.loadTexts:
    pdnDslAtmBondGroupStatusChange.setStatus(
        "current"
    )


# Notifications groups

pdnDslAtmBondNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 3, 1)
)
pdnDslAtmBondNotificationsGroup.setObjects(
      *(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondAtucRateChange"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondAturRateChange"),
        ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupStatusChange"))
)
if mibBuilder.loadTexts:
    pdnDslAtmBondNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

pdnDslAtmBondMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 1, 1)
)
if mibBuilder.loadTexts:
    pdnDslAtmBondMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-DSL-ATM-BOND-MIB",
    **{"PdnDslAtmBondGroupIndexTC": PdnDslAtmBondGroupIndexTC,
       "PdnDslAtmBondGroupIdentityTC": PdnDslAtmBondGroupIdentityTC,
       "PdnDslAtmBondGroupBearerNumberTC": PdnDslAtmBondGroupBearerNumberTC,
       "PdnDslAtmBondLinkStatusAsmTC": PdnDslAtmBondLinkStatusAsmTC,
       "PdnDslAtmBondAsmRxStatusTC": PdnDslAtmBondAsmRxStatusTC,
       "PdnDslAtmBondGroupDataRateTC": PdnDslAtmBondGroupDataRateTC,
       "PdnDslAtmBondGroupDiffDelayTolTC": PdnDslAtmBondGroupDiffDelayTolTC,
       "PdnDslAtmBondGroupStatusTC": PdnDslAtmBondGroupStatusTC,
       "PdnDslAtmBondGroupFailReasonTC": PdnDslAtmBondGroupFailReasonTC,
       "pdnDslAtmBondMIB": pdnDslAtmBondMIB,
       "pdnDslAtmBondNotifications": pdnDslAtmBondNotifications,
       "pdnDslAtmBondAtucRateChange": pdnDslAtmBondAtucRateChange,
       "pdnDslAtmBondAturRateChange": pdnDslAtmBondAturRateChange,
       "pdnDslAtmBondGroupStatusChange": pdnDslAtmBondGroupStatusChange,
       "pdnDslAtmBondObjects": pdnDslAtmBondObjects,
       "pdnDslAtmBondNextGroupIndex": pdnDslAtmBondNextGroupIndex,
       "pdnDslAtmBondNbrOfGroups": pdnDslAtmBondNbrOfGroups,
       "pdnDslAtmBondGroupTable": pdnDslAtmBondGroupTable,
       "pdnDslAtmBondGroupEntry": pdnDslAtmBondGroupEntry,
       "pdnDslAtmBondGroupIndex": pdnDslAtmBondGroupIndex,
       "pdnDslAtmBondGroupRowStatus": pdnDslAtmBondGroupRowStatus,
       "pdnDslAtmBondGroupNbrRefs": pdnDslAtmBondGroupNbrRefs,
       "pdnDslAtmBondGroupIfIndex": pdnDslAtmBondGroupIfIndex,
       "pdnDslAtmBondGroupID": pdnDslAtmBondGroupID,
       "pdnDslAtmBondGroupAlarmConfProfileName": pdnDslAtmBondGroupAlarmConfProfileName,
       "pdnDslAtmBondGroupAtucMaxNetDataRate": pdnDslAtmBondGroupAtucMaxNetDataRate,
       "pdnDslAtmBondGroupAturMaxNetDataRate": pdnDslAtmBondGroupAturMaxNetDataRate,
       "pdnDslAtmBondGroupAtucMinNetDataRate": pdnDslAtmBondGroupAtucMinNetDataRate,
       "pdnDslAtmBondGroupAturMinNetDataRate": pdnDslAtmBondGroupAturMinNetDataRate,
       "pdnDslAtmBondGroupAtucDiffDelay": pdnDslAtmBondGroupAtucDiffDelay,
       "pdnDslAtmBondGroupAturDiffDelay": pdnDslAtmBondGroupAturDiffDelay,
       "pdnDslAtmBondGroupStatusNotifyEnabled": pdnDslAtmBondGroupStatusNotifyEnabled,
       "pdnDslAtmBondMappingTable": pdnDslAtmBondMappingTable,
       "pdnDslAtmBondMappingEntry": pdnDslAtmBondMappingEntry,
       "pdnDslAtmBondDslIfIndex": pdnDslAtmBondDslIfIndex,
       "pdnDslAtmBondBearerNbr": pdnDslAtmBondBearerNbr,
       "pdnDslAtmBondMappingRowStatus": pdnDslAtmBondMappingRowStatus,
       "pdnDslAtmBondMappingGroupIndex": pdnDslAtmBondMappingGroupIndex,
       "pdnDslAtmBondGroupIndexMappingTable": pdnDslAtmBondGroupIndexMappingTable,
       "pdnDslAtmBondGroupIndexMappingEntry": pdnDslAtmBondGroupIndexMappingEntry,
       "pdnDslAtmBondGroupIndexMappingIndex": pdnDslAtmBondGroupIndexMappingIndex,
       "pdnDslAtmBondGroupInvMappingTable": pdnDslAtmBondGroupInvMappingTable,
       "pdnDslAtmBondGroupInvMappingEntry": pdnDslAtmBondGroupInvMappingEntry,
       "pdnDslAtmBondInvMappingBearerNbr": pdnDslAtmBondInvMappingBearerNbr,
       "pdnDslAtmBondPerfTable": pdnDslAtmBondPerfTable,
       "pdnDslAtmBondPerfEntry": pdnDslAtmBondPerfEntry,
       "pdnDslAtmBondPerfCurrAtucNetDataRate": pdnDslAtmBondPerfCurrAtucNetDataRate,
       "pdnDslAtmBondPerfCurrAturNetDataRate": pdnDslAtmBondPerfCurrAturNetDataRate,
       "pdnDslAtmBondPerfPrevAtucNetDataRate": pdnDslAtmBondPerfPrevAtucNetDataRate,
       "pdnDslAtmBondPerfPrevAturNetDataRate": pdnDslAtmBondPerfPrevAturNetDataRate,
       "pdnDslAtmBondPerfGroupStatus": pdnDslAtmBondPerfGroupStatus,
       "pdnDslAtmBondPerfFailReason": pdnDslAtmBondPerfFailReason,
       "pdnDslAtmBondPerfFailCount": pdnDslAtmBondPerfFailCount,
       "pdnDslAtmBondPerfRunTime": pdnDslAtmBondPerfRunTime,
       "pdnDslAtmBondPerfUAS": pdnDslAtmBondPerfUAS,
       "pdnDslAtmBondPerfAtucRxCellLoss": pdnDslAtmBondPerfAtucRxCellLoss,
       "pdnDslAtmBondPerfAturRxCellLoss": pdnDslAtmBondPerfAturRxCellLoss,
       "pdnDslAtmBond15MinIntervalTable": pdnDslAtmBond15MinIntervalTable,
       "pdnDslAtmBond15MinIntervalEntry": pdnDslAtmBond15MinIntervalEntry,
       "pdnDslAtmBond15MinIntervalNumber": pdnDslAtmBond15MinIntervalNumber,
       "pdnDslAtmBond15MinIntervalStartDateAndTime": pdnDslAtmBond15MinIntervalStartDateAndTime,
       "pdnDslAtmBond15MinIntervalFailCount": pdnDslAtmBond15MinIntervalFailCount,
       "pdnDslAtmBond15MinIntervalRunTime": pdnDslAtmBond15MinIntervalRunTime,
       "pdnDslAtmBond15MinIntervalUAS": pdnDslAtmBond15MinIntervalUAS,
       "pdnDslAtmBond15MinIntervalAtucRxCellLoss": pdnDslAtmBond15MinIntervalAtucRxCellLoss,
       "pdnDslAtmBond15MinIntervalAturRxCellLoss": pdnDslAtmBond15MinIntervalAturRxCellLoss,
       "pdnDslAtmBond1DayIntervalTable": pdnDslAtmBond1DayIntervalTable,
       "pdnDslAtmBond1DayIntervalEntry": pdnDslAtmBond1DayIntervalEntry,
       "pdnDslAtmBond1DayIntervalNumber": pdnDslAtmBond1DayIntervalNumber,
       "pdnDslAtmBond1DayIntervalStartDateAndTime": pdnDslAtmBond1DayIntervalStartDateAndTime,
       "pdnDslAtmBond1DayIntervalFailCount": pdnDslAtmBond1DayIntervalFailCount,
       "pdnDslAtmBond1DayIntervalRunTime": pdnDslAtmBond1DayIntervalRunTime,
       "pdnDslAtmBond1DayIntervalUAS": pdnDslAtmBond1DayIntervalUAS,
       "pdnDslAtmBond1DayIntervalAtucRxCellLoss": pdnDslAtmBond1DayIntervalAtucRxCellLoss,
       "pdnDslAtmBond1DayIntervalAturRxCellLoss": pdnDslAtmBond1DayIntervalAturRxCellLoss,
       "pdnDslAtmBondLinkTable": pdnDslAtmBondLinkTable,
       "pdnDslAtmBondLinkEntry": pdnDslAtmBondLinkEntry,
       "pdnDslAtmBondLinkAtucRxLinkStatus": pdnDslAtmBondLinkAtucRxLinkStatus,
       "pdnDslAtmBondLinkAturRxLinkStatus": pdnDslAtmBondLinkAturRxLinkStatus,
       "pdnDslAtmBondLinkAtucTxLinkStatus": pdnDslAtmBondLinkAtucTxLinkStatus,
       "pdnDslAtmBondLinkAturTxLinkStatus": pdnDslAtmBondLinkAturTxLinkStatus,
       "pdnDslAtmBondLinkAtucAsmRxStatus": pdnDslAtmBondLinkAtucAsmRxStatus,
       "pdnDslAtmBondLinkAturAsmRxStatus": pdnDslAtmBondLinkAturAsmRxStatus,
       "pdnDslAtmBondAlarmConfProfileTable": pdnDslAtmBondAlarmConfProfileTable,
       "pdnDslAtmBondAlarmConfProfileEntry": pdnDslAtmBondAlarmConfProfileEntry,
       "pdnDslAtmBondAlarmConfProfileName": pdnDslAtmBondAlarmConfProfileName,
       "pdnDslAtmBondAlarmConfRowStatus": pdnDslAtmBondAlarmConfRowStatus,
       "pdnDslAtmBondAlarmConfNbrRefs": pdnDslAtmBondAlarmConfNbrRefs,
       "pdnDslAtmBondAlarmConfAtucThreshRateUp": pdnDslAtmBondAlarmConfAtucThreshRateUp,
       "pdnDslAtmBondAlarmConfAturThreshRateUp": pdnDslAtmBondAlarmConfAturThreshRateUp,
       "pdnDslAtmBondAlarmConfAtucThreshRateDown": pdnDslAtmBondAlarmConfAtucThreshRateDown,
       "pdnDslAtmBondAlarmConfAturThreshRateDown": pdnDslAtmBondAlarmConfAturThreshRateDown,
       "pdnDslAtmBondAFNs": pdnDslAtmBondAFNs,
       "pdnDslAtmBondConformance": pdnDslAtmBondConformance,
       "pdnDslAtmBondCompliances": pdnDslAtmBondCompliances,
       "pdnDslAtmBondMIBCompliance": pdnDslAtmBondMIBCompliance,
       "pdnDslAtmBondGroups": pdnDslAtmBondGroups,
       "pdnDslAtmBondObjGroups": pdnDslAtmBondObjGroups,
       "pdnDslAtmBondGroup": pdnDslAtmBondGroup,
       "pdnDslAtmBondMaxRateGroup": pdnDslAtmBondMaxRateGroup,
       "pdnDslAtmBondMinRateGroup": pdnDslAtmBondMinRateGroup,
       "pdnDslAtmBondDiffDelayGroup": pdnDslAtmBondDiffDelayGroup,
       "pdnDslAtmBondGroupStatusNotifyEnabledGroup": pdnDslAtmBondGroupStatusNotifyEnabledGroup,
       "pdnDslAtmBondMappingGroup": pdnDslAtmBondMappingGroup,
       "pdnDslAtmBondIndexMappingGroup": pdnDslAtmBondIndexMappingGroup,
       "pdnDslAtmBondInvMappingGroup": pdnDslAtmBondInvMappingGroup,
       "pdnDslAtmBondPerfAggDataRateGroup": pdnDslAtmBondPerfAggDataRateGroup,
       "pdnDslAtmBondPerfBondGroupStatusGroup": pdnDslAtmBondPerfBondGroupStatusGroup,
       "pdnDslAtmBondDateAndTimeGroup": pdnDslAtmBondDateAndTimeGroup,
       "pdnDslAtmBondRunTimeGroup": pdnDslAtmBondRunTimeGroup,
       "pdnDslAtmBondRxCellLossGroup": pdnDslAtmBondRxCellLossGroup,
       "pdnDslAtmBondPerfFailReasonGroup": pdnDslAtmBondPerfFailReasonGroup,
       "pdnDslAtmBondFailCountGroup": pdnDslAtmBondFailCountGroup,
       "pdnDslAtmBondUASGroup": pdnDslAtmBondUASGroup,
       "pdnDslAtmBondTrafficCapGroup": pdnDslAtmBondTrafficCapGroup,
       "pdnDslATmBondAsmRxStatusGroup": pdnDslATmBondAsmRxStatusGroup,
       "pdnDslAtmBondAlarmConfProfileGroup": pdnDslAtmBondAlarmConfProfileGroup,
       "pdnDslAtmBondAlarmConfAtucThreshRateGroup": pdnDslAtmBondAlarmConfAtucThreshRateGroup,
       "pdnDslAtmBondAlarmConfAturThreshRateGroup": pdnDslAtmBondAlarmConfAturThreshRateGroup,
       "pdnDslAtmBondAfnGroups": pdnDslAtmBondAfnGroups,
       "pdnDslAtmBondNtfyGroups": pdnDslAtmBondNtfyGroups,
       "pdnDslAtmBondNotificationsGroup": pdnDslAtmBondNotificationsGroup}
)
