# SNMP MIB module (HPN-ICF-DOT11-CFGEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-DOT11-CFGEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:50 2024
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

(hpnicfDot11,) = mibBuilder.importSymbols(
    "HPN-ICF-DOT11-REF-MIB",
    "hpnicfDot11")

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

hpnicfDot11CFGEXT = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 6)
)
hpnicfDot11CFGEXT.setRevisions(
        ("2010-06-02 14:00",
         "2007-04-25 20:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfDot11LoadBalance_ObjectIdentity = ObjectIdentity
hpnicfDot11LoadBalance = _HpnicfDot11LoadBalance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 6, 1)
)
_HpnicfDot11LBGlobalGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11LBGlobalGroup = _HpnicfDot11LBGlobalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 6, 1, 1)
)
_HpnicfDot11LoadBalanceTrafficEnable_Type = TruthValue
_HpnicfDot11LoadBalanceTrafficEnable_Object = MibScalar
hpnicfDot11LoadBalanceTrafficEnable = _HpnicfDot11LoadBalanceTrafficEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 6, 1, 1, 1),
    _HpnicfDot11LoadBalanceTrafficEnable_Type()
)
hpnicfDot11LoadBalanceTrafficEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11LoadBalanceTrafficEnable.setStatus("current")
_HpnicfDot11LoadBalanceTrafficThres_Type = Integer32
_HpnicfDot11LoadBalanceTrafficThres_Object = MibScalar
hpnicfDot11LoadBalanceTrafficThres = _HpnicfDot11LoadBalanceTrafficThres_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 6, 1, 1, 2),
    _HpnicfDot11LoadBalanceTrafficThres_Type()
)
hpnicfDot11LoadBalanceTrafficThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11LoadBalanceTrafficThres.setStatus("current")
_HpnicfDot11LoadBalanceSessionEnable_Type = TruthValue
_HpnicfDot11LoadBalanceSessionEnable_Object = MibScalar
hpnicfDot11LoadBalanceSessionEnable = _HpnicfDot11LoadBalanceSessionEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 6, 1, 1, 3),
    _HpnicfDot11LoadBalanceSessionEnable_Type()
)
hpnicfDot11LoadBalanceSessionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11LoadBalanceSessionEnable.setStatus("current")
_HpnicfDot11LoadBalanceSessionThres_Type = Integer32
_HpnicfDot11LoadBalanceSessionThres_Object = MibScalar
hpnicfDot11LoadBalanceSessionThres = _HpnicfDot11LoadBalanceSessionThres_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 6, 1, 1, 4),
    _HpnicfDot11LoadBalanceSessionThres_Type()
)
hpnicfDot11LoadBalanceSessionThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11LoadBalanceSessionThres.setStatus("current")


class _HpnicfDot11LoadBalanceTrafficGap_Type(Integer32):
    """Custom type hpnicfDot11LoadBalanceTrafficGap based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 40),
    )


_HpnicfDot11LoadBalanceTrafficGap_Type.__name__ = "Integer32"
_HpnicfDot11LoadBalanceTrafficGap_Object = MibScalar
hpnicfDot11LoadBalanceTrafficGap = _HpnicfDot11LoadBalanceTrafficGap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 6, 1, 1, 5),
    _HpnicfDot11LoadBalanceTrafficGap_Type()
)
hpnicfDot11LoadBalanceTrafficGap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11LoadBalanceTrafficGap.setStatus("current")


class _HpnicfDot11LoadBalanceSessionGap_Type(Integer32):
    """Custom type hpnicfDot11LoadBalanceSessionGap based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HpnicfDot11LoadBalanceSessionGap_Type.__name__ = "Integer32"
_HpnicfDot11LoadBalanceSessionGap_Object = MibScalar
hpnicfDot11LoadBalanceSessionGap = _HpnicfDot11LoadBalanceSessionGap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 6, 1, 1, 6),
    _HpnicfDot11LoadBalanceSessionGap_Type()
)
hpnicfDot11LoadBalanceSessionGap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11LoadBalanceSessionGap.setStatus("current")
_HpnicfDot11LBTrafficThresKbps_Type = Integer32
_HpnicfDot11LBTrafficThresKbps_Object = MibScalar
hpnicfDot11LBTrafficThresKbps = _HpnicfDot11LBTrafficThresKbps_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 6, 1, 1, 7),
    _HpnicfDot11LBTrafficThresKbps_Type()
)
hpnicfDot11LBTrafficThresKbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11LBTrafficThresKbps.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11LBTrafficThresKbps.setUnits("kbps")
_HpnicfDot11LBTrafficGapKbps_Type = Integer32
_HpnicfDot11LBTrafficGapKbps_Object = MibScalar
hpnicfDot11LBTrafficGapKbps = _HpnicfDot11LBTrafficGapKbps_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 6, 1, 1, 8),
    _HpnicfDot11LBTrafficGapKbps_Type()
)
hpnicfDot11LBTrafficGapKbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11LBTrafficGapKbps.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11LBTrafficGapKbps.setUnits("kbps")
_HpnicfDot11LBRadioGroupTable_Object = MibTable
hpnicfDot11LBRadioGroupTable = _HpnicfDot11LBRadioGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 6, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfDot11LBRadioGroupTable.setStatus("current")
_HpnicfDot11LBRadioGroupEntry_Object = MibTableRow
hpnicfDot11LBRadioGroupEntry = _HpnicfDot11LBRadioGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 6, 1, 2, 1)
)
hpnicfDot11LBRadioGroupEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-CFGEXT-MIB", "hpnicfDot11LBRadioGroupId"),
)
if mibBuilder.loadTexts:
    hpnicfDot11LBRadioGroupEntry.setStatus("current")
_HpnicfDot11LBRadioGroupId_Type = Unsigned32
_HpnicfDot11LBRadioGroupId_Object = MibTableColumn
hpnicfDot11LBRadioGroupId = _HpnicfDot11LBRadioGroupId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 6, 1, 2, 1, 1),
    _HpnicfDot11LBRadioGroupId_Type()
)
hpnicfDot11LBRadioGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11LBRadioGroupId.setStatus("current")
_HpnicfDot11LBRadioGroupDesc_Type = OctetString
_HpnicfDot11LBRadioGroupDesc_Object = MibTableColumn
hpnicfDot11LBRadioGroupDesc = _HpnicfDot11LBRadioGroupDesc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 6, 1, 2, 1, 2),
    _HpnicfDot11LBRadioGroupDesc_Type()
)
hpnicfDot11LBRadioGroupDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11LBRadioGroupDesc.setStatus("current")
_HpnicfDot11LBRadioGroupRowStatus_Type = RowStatus
_HpnicfDot11LBRadioGroupRowStatus_Object = MibTableColumn
hpnicfDot11LBRadioGroupRowStatus = _HpnicfDot11LBRadioGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 6, 1, 2, 1, 3),
    _HpnicfDot11LBRadioGroupRowStatus_Type()
)
hpnicfDot11LBRadioGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11LBRadioGroupRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-DOT11-CFGEXT-MIB",
    **{"hpnicfDot11CFGEXT": hpnicfDot11CFGEXT,
       "hpnicfDot11LoadBalance": hpnicfDot11LoadBalance,
       "hpnicfDot11LBGlobalGroup": hpnicfDot11LBGlobalGroup,
       "hpnicfDot11LoadBalanceTrafficEnable": hpnicfDot11LoadBalanceTrafficEnable,
       "hpnicfDot11LoadBalanceTrafficThres": hpnicfDot11LoadBalanceTrafficThres,
       "hpnicfDot11LoadBalanceSessionEnable": hpnicfDot11LoadBalanceSessionEnable,
       "hpnicfDot11LoadBalanceSessionThres": hpnicfDot11LoadBalanceSessionThres,
       "hpnicfDot11LoadBalanceTrafficGap": hpnicfDot11LoadBalanceTrafficGap,
       "hpnicfDot11LoadBalanceSessionGap": hpnicfDot11LoadBalanceSessionGap,
       "hpnicfDot11LBTrafficThresKbps": hpnicfDot11LBTrafficThresKbps,
       "hpnicfDot11LBTrafficGapKbps": hpnicfDot11LBTrafficGapKbps,
       "hpnicfDot11LBRadioGroupTable": hpnicfDot11LBRadioGroupTable,
       "hpnicfDot11LBRadioGroupEntry": hpnicfDot11LBRadioGroupEntry,
       "hpnicfDot11LBRadioGroupId": hpnicfDot11LBRadioGroupId,
       "hpnicfDot11LBRadioGroupDesc": hpnicfDot11LBRadioGroupDesc,
       "hpnicfDot11LBRadioGroupRowStatus": hpnicfDot11LBRadioGroupRowStatus}
)
