# SNMP MIB module (A3COM-HUAWEI-DOT11-CFGEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-DOT11-CFGEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:38 2024
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

(h3cDot11,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-DOT11-REF-MIB",
    "h3cDot11")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cDot11CFGEXT = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 6)
)
h3cDot11CFGEXT.setRevisions(
        ("2010-06-02 14:00",
         "2007-04-25 20:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cDot11LoadBalance_ObjectIdentity = ObjectIdentity
h3cDot11LoadBalance = _H3cDot11LoadBalance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 6, 1)
)
_H3cDot11LBGlobalGroup_ObjectIdentity = ObjectIdentity
h3cDot11LBGlobalGroup = _H3cDot11LBGlobalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 6, 1, 1)
)
_H3cDot11LoadBalanceTrafficEnable_Type = TruthValue
_H3cDot11LoadBalanceTrafficEnable_Object = MibScalar
h3cDot11LoadBalanceTrafficEnable = _H3cDot11LoadBalanceTrafficEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 6, 1, 1, 1),
    _H3cDot11LoadBalanceTrafficEnable_Type()
)
h3cDot11LoadBalanceTrafficEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11LoadBalanceTrafficEnable.setStatus("current")
_H3cDot11LoadBalanceTrafficThres_Type = Integer32
_H3cDot11LoadBalanceTrafficThres_Object = MibScalar
h3cDot11LoadBalanceTrafficThres = _H3cDot11LoadBalanceTrafficThres_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 6, 1, 1, 2),
    _H3cDot11LoadBalanceTrafficThres_Type()
)
h3cDot11LoadBalanceTrafficThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11LoadBalanceTrafficThres.setStatus("current")
_H3cDot11LoadBalanceSessionEnable_Type = TruthValue
_H3cDot11LoadBalanceSessionEnable_Object = MibScalar
h3cDot11LoadBalanceSessionEnable = _H3cDot11LoadBalanceSessionEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 6, 1, 1, 3),
    _H3cDot11LoadBalanceSessionEnable_Type()
)
h3cDot11LoadBalanceSessionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11LoadBalanceSessionEnable.setStatus("current")
_H3cDot11LoadBalanceSessionThres_Type = Integer32
_H3cDot11LoadBalanceSessionThres_Object = MibScalar
h3cDot11LoadBalanceSessionThres = _H3cDot11LoadBalanceSessionThres_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 6, 1, 1, 4),
    _H3cDot11LoadBalanceSessionThres_Type()
)
h3cDot11LoadBalanceSessionThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11LoadBalanceSessionThres.setStatus("current")


class _H3cDot11LoadBalanceTrafficGap_Type(Integer32):
    """Custom type h3cDot11LoadBalanceTrafficGap based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 40),
    )


_H3cDot11LoadBalanceTrafficGap_Type.__name__ = "Integer32"
_H3cDot11LoadBalanceTrafficGap_Object = MibScalar
h3cDot11LoadBalanceTrafficGap = _H3cDot11LoadBalanceTrafficGap_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 6, 1, 1, 5),
    _H3cDot11LoadBalanceTrafficGap_Type()
)
h3cDot11LoadBalanceTrafficGap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11LoadBalanceTrafficGap.setStatus("current")


class _H3cDot11LoadBalanceSessionGap_Type(Integer32):
    """Custom type h3cDot11LoadBalanceSessionGap based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_H3cDot11LoadBalanceSessionGap_Type.__name__ = "Integer32"
_H3cDot11LoadBalanceSessionGap_Object = MibScalar
h3cDot11LoadBalanceSessionGap = _H3cDot11LoadBalanceSessionGap_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 6, 1, 1, 6),
    _H3cDot11LoadBalanceSessionGap_Type()
)
h3cDot11LoadBalanceSessionGap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11LoadBalanceSessionGap.setStatus("current")
_H3cDot11LBTrafficThresKbps_Type = Integer32
_H3cDot11LBTrafficThresKbps_Object = MibScalar
h3cDot11LBTrafficThresKbps = _H3cDot11LBTrafficThresKbps_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 6, 1, 1, 7),
    _H3cDot11LBTrafficThresKbps_Type()
)
h3cDot11LBTrafficThresKbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11LBTrafficThresKbps.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11LBTrafficThresKbps.setUnits("kbps")
_H3cDot11LBTrafficGapKbps_Type = Integer32
_H3cDot11LBTrafficGapKbps_Object = MibScalar
h3cDot11LBTrafficGapKbps = _H3cDot11LBTrafficGapKbps_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 6, 1, 1, 8),
    _H3cDot11LBTrafficGapKbps_Type()
)
h3cDot11LBTrafficGapKbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11LBTrafficGapKbps.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11LBTrafficGapKbps.setUnits("kbps")
_H3cDot11LBRadioGroupTable_Object = MibTable
h3cDot11LBRadioGroupTable = _H3cDot11LBRadioGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 6, 1, 2)
)
if mibBuilder.loadTexts:
    h3cDot11LBRadioGroupTable.setStatus("current")
_H3cDot11LBRadioGroupEntry_Object = MibTableRow
h3cDot11LBRadioGroupEntry = _H3cDot11LBRadioGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 6, 1, 2, 1)
)
h3cDot11LBRadioGroupEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-CFGEXT-MIB", "h3cDot11LBRadioGroupId"),
)
if mibBuilder.loadTexts:
    h3cDot11LBRadioGroupEntry.setStatus("current")
_H3cDot11LBRadioGroupId_Type = Unsigned32
_H3cDot11LBRadioGroupId_Object = MibTableColumn
h3cDot11LBRadioGroupId = _H3cDot11LBRadioGroupId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 6, 1, 2, 1, 1),
    _H3cDot11LBRadioGroupId_Type()
)
h3cDot11LBRadioGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11LBRadioGroupId.setStatus("current")
_H3cDot11LBRadioGroupDesc_Type = OctetString
_H3cDot11LBRadioGroupDesc_Object = MibTableColumn
h3cDot11LBRadioGroupDesc = _H3cDot11LBRadioGroupDesc_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 6, 1, 2, 1, 2),
    _H3cDot11LBRadioGroupDesc_Type()
)
h3cDot11LBRadioGroupDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11LBRadioGroupDesc.setStatus("current")
_H3cDot11LBRadioGroupRowStatus_Type = RowStatus
_H3cDot11LBRadioGroupRowStatus_Object = MibTableColumn
h3cDot11LBRadioGroupRowStatus = _H3cDot11LBRadioGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 6, 1, 2, 1, 3),
    _H3cDot11LBRadioGroupRowStatus_Type()
)
h3cDot11LBRadioGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11LBRadioGroupRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-DOT11-CFGEXT-MIB",
    **{"h3cDot11CFGEXT": h3cDot11CFGEXT,
       "h3cDot11LoadBalance": h3cDot11LoadBalance,
       "h3cDot11LBGlobalGroup": h3cDot11LBGlobalGroup,
       "h3cDot11LoadBalanceTrafficEnable": h3cDot11LoadBalanceTrafficEnable,
       "h3cDot11LoadBalanceTrafficThres": h3cDot11LoadBalanceTrafficThres,
       "h3cDot11LoadBalanceSessionEnable": h3cDot11LoadBalanceSessionEnable,
       "h3cDot11LoadBalanceSessionThres": h3cDot11LoadBalanceSessionThres,
       "h3cDot11LoadBalanceTrafficGap": h3cDot11LoadBalanceTrafficGap,
       "h3cDot11LoadBalanceSessionGap": h3cDot11LoadBalanceSessionGap,
       "h3cDot11LBTrafficThresKbps": h3cDot11LBTrafficThresKbps,
       "h3cDot11LBTrafficGapKbps": h3cDot11LBTrafficGapKbps,
       "h3cDot11LBRadioGroupTable": h3cDot11LBRadioGroupTable,
       "h3cDot11LBRadioGroupEntry": h3cDot11LBRadioGroupEntry,
       "h3cDot11LBRadioGroupId": h3cDot11LBRadioGroupId,
       "h3cDot11LBRadioGroupDesc": h3cDot11LBRadioGroupDesc,
       "h3cDot11LBRadioGroupRowStatus": h3cDot11LBRadioGroupRowStatus}
)
