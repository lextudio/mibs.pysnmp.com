# SNMP MIB module (HH3C-DOT11-CFGEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-DOT11-CFGEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:51 2024
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

(hh3cDot11,) = mibBuilder.importSymbols(
    "HH3C-DOT11-REF-MIB",
    "hh3cDot11")

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

hh3cDot11CFGEXT = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 6)
)
hh3cDot11CFGEXT.setRevisions(
        ("2010-06-02 14:00",
         "2007-04-25 20:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cDot11LoadBalance_ObjectIdentity = ObjectIdentity
hh3cDot11LoadBalance = _Hh3cDot11LoadBalance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 6, 1)
)
_Hh3cDot11LBGlobalGroup_ObjectIdentity = ObjectIdentity
hh3cDot11LBGlobalGroup = _Hh3cDot11LBGlobalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 6, 1, 1)
)
_Hh3cDot11LoadBalanceTrafficEnable_Type = TruthValue
_Hh3cDot11LoadBalanceTrafficEnable_Object = MibScalar
hh3cDot11LoadBalanceTrafficEnable = _Hh3cDot11LoadBalanceTrafficEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 6, 1, 1, 1),
    _Hh3cDot11LoadBalanceTrafficEnable_Type()
)
hh3cDot11LoadBalanceTrafficEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11LoadBalanceTrafficEnable.setStatus("current")
_Hh3cDot11LoadBalanceTrafficThres_Type = Integer32
_Hh3cDot11LoadBalanceTrafficThres_Object = MibScalar
hh3cDot11LoadBalanceTrafficThres = _Hh3cDot11LoadBalanceTrafficThres_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 6, 1, 1, 2),
    _Hh3cDot11LoadBalanceTrafficThres_Type()
)
hh3cDot11LoadBalanceTrafficThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11LoadBalanceTrafficThres.setStatus("current")
_Hh3cDot11LoadBalanceSessionEnable_Type = TruthValue
_Hh3cDot11LoadBalanceSessionEnable_Object = MibScalar
hh3cDot11LoadBalanceSessionEnable = _Hh3cDot11LoadBalanceSessionEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 6, 1, 1, 3),
    _Hh3cDot11LoadBalanceSessionEnable_Type()
)
hh3cDot11LoadBalanceSessionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11LoadBalanceSessionEnable.setStatus("current")
_Hh3cDot11LoadBalanceSessionThres_Type = Integer32
_Hh3cDot11LoadBalanceSessionThres_Object = MibScalar
hh3cDot11LoadBalanceSessionThres = _Hh3cDot11LoadBalanceSessionThres_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 6, 1, 1, 4),
    _Hh3cDot11LoadBalanceSessionThres_Type()
)
hh3cDot11LoadBalanceSessionThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11LoadBalanceSessionThres.setStatus("current")


class _Hh3cDot11LoadBalanceTrafficGap_Type(Integer32):
    """Custom type hh3cDot11LoadBalanceTrafficGap based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 40),
    )


_Hh3cDot11LoadBalanceTrafficGap_Type.__name__ = "Integer32"
_Hh3cDot11LoadBalanceTrafficGap_Object = MibScalar
hh3cDot11LoadBalanceTrafficGap = _Hh3cDot11LoadBalanceTrafficGap_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 6, 1, 1, 5),
    _Hh3cDot11LoadBalanceTrafficGap_Type()
)
hh3cDot11LoadBalanceTrafficGap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11LoadBalanceTrafficGap.setStatus("current")


class _Hh3cDot11LoadBalanceSessionGap_Type(Integer32):
    """Custom type hh3cDot11LoadBalanceSessionGap based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Hh3cDot11LoadBalanceSessionGap_Type.__name__ = "Integer32"
_Hh3cDot11LoadBalanceSessionGap_Object = MibScalar
hh3cDot11LoadBalanceSessionGap = _Hh3cDot11LoadBalanceSessionGap_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 6, 1, 1, 6),
    _Hh3cDot11LoadBalanceSessionGap_Type()
)
hh3cDot11LoadBalanceSessionGap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11LoadBalanceSessionGap.setStatus("current")
_Hh3cDot11LBTrafficThresKbps_Type = Integer32
_Hh3cDot11LBTrafficThresKbps_Object = MibScalar
hh3cDot11LBTrafficThresKbps = _Hh3cDot11LBTrafficThresKbps_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 6, 1, 1, 7),
    _Hh3cDot11LBTrafficThresKbps_Type()
)
hh3cDot11LBTrafficThresKbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11LBTrafficThresKbps.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11LBTrafficThresKbps.setUnits("kbps")
_Hh3cDot11LBTrafficGapKbps_Type = Integer32
_Hh3cDot11LBTrafficGapKbps_Object = MibScalar
hh3cDot11LBTrafficGapKbps = _Hh3cDot11LBTrafficGapKbps_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 6, 1, 1, 8),
    _Hh3cDot11LBTrafficGapKbps_Type()
)
hh3cDot11LBTrafficGapKbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11LBTrafficGapKbps.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11LBTrafficGapKbps.setUnits("kbps")
_Hh3cDot11LBRadioGroupTable_Object = MibTable
hh3cDot11LBRadioGroupTable = _Hh3cDot11LBRadioGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 6, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cDot11LBRadioGroupTable.setStatus("current")
_Hh3cDot11LBRadioGroupEntry_Object = MibTableRow
hh3cDot11LBRadioGroupEntry = _Hh3cDot11LBRadioGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 6, 1, 2, 1)
)
hh3cDot11LBRadioGroupEntry.setIndexNames(
    (0, "HH3C-DOT11-CFGEXT-MIB", "hh3cDot11LBRadioGroupId"),
)
if mibBuilder.loadTexts:
    hh3cDot11LBRadioGroupEntry.setStatus("current")
_Hh3cDot11LBRadioGroupId_Type = Unsigned32
_Hh3cDot11LBRadioGroupId_Object = MibTableColumn
hh3cDot11LBRadioGroupId = _Hh3cDot11LBRadioGroupId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 6, 1, 2, 1, 1),
    _Hh3cDot11LBRadioGroupId_Type()
)
hh3cDot11LBRadioGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11LBRadioGroupId.setStatus("current")
_Hh3cDot11LBRadioGroupDesc_Type = OctetString
_Hh3cDot11LBRadioGroupDesc_Object = MibTableColumn
hh3cDot11LBRadioGroupDesc = _Hh3cDot11LBRadioGroupDesc_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 6, 1, 2, 1, 2),
    _Hh3cDot11LBRadioGroupDesc_Type()
)
hh3cDot11LBRadioGroupDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11LBRadioGroupDesc.setStatus("current")
_Hh3cDot11LBRadioGroupRowStatus_Type = RowStatus
_Hh3cDot11LBRadioGroupRowStatus_Object = MibTableColumn
hh3cDot11LBRadioGroupRowStatus = _Hh3cDot11LBRadioGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 6, 1, 2, 1, 3),
    _Hh3cDot11LBRadioGroupRowStatus_Type()
)
hh3cDot11LBRadioGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11LBRadioGroupRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DOT11-CFGEXT-MIB",
    **{"hh3cDot11CFGEXT": hh3cDot11CFGEXT,
       "hh3cDot11LoadBalance": hh3cDot11LoadBalance,
       "hh3cDot11LBGlobalGroup": hh3cDot11LBGlobalGroup,
       "hh3cDot11LoadBalanceTrafficEnable": hh3cDot11LoadBalanceTrafficEnable,
       "hh3cDot11LoadBalanceTrafficThres": hh3cDot11LoadBalanceTrafficThres,
       "hh3cDot11LoadBalanceSessionEnable": hh3cDot11LoadBalanceSessionEnable,
       "hh3cDot11LoadBalanceSessionThres": hh3cDot11LoadBalanceSessionThres,
       "hh3cDot11LoadBalanceTrafficGap": hh3cDot11LoadBalanceTrafficGap,
       "hh3cDot11LoadBalanceSessionGap": hh3cDot11LoadBalanceSessionGap,
       "hh3cDot11LBTrafficThresKbps": hh3cDot11LBTrafficThresKbps,
       "hh3cDot11LBTrafficGapKbps": hh3cDot11LBTrafficGapKbps,
       "hh3cDot11LBRadioGroupTable": hh3cDot11LBRadioGroupTable,
       "hh3cDot11LBRadioGroupEntry": hh3cDot11LBRadioGroupEntry,
       "hh3cDot11LBRadioGroupId": hh3cDot11LBRadioGroupId,
       "hh3cDot11LBRadioGroupDesc": hh3cDot11LBRadioGroupDesc,
       "hh3cDot11LBRadioGroupRowStatus": hh3cDot11LBRadioGroupRowStatus}
)
