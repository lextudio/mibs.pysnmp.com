# SNMP MIB module (ZXR10-PEAKRATE1MIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZXR10-PEAKRATE1MIN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:02 2024
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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zte_ObjectIdentity = ObjectIdentity
zte = _Zte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
_Zxr10_ObjectIdentity = ObjectIdentity
zxr10 = _Zxr10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3)
)
_Zxr10switch_ObjectIdentity = ObjectIdentity
zxr10switch = _Zxr10switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102)
)
_Zxr10Peakrate1Min_ObjectIdentity = ObjectIdentity
zxr10Peakrate1Min = _Zxr10Peakrate1Min_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 31)
)
_PortPeakrateTable_Object = MibTable
portPeakrateTable = _PortPeakrateTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 31, 1)
)
if mibBuilder.loadTexts:
    portPeakrateTable.setStatus("current")
_PortPeakrateEntry_Object = MibTableRow
portPeakrateEntry = _PortPeakrateEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 31, 1, 1)
)
portPeakrateEntry.setIndexNames(
    (0, "ZXR10-PEAKRATE1MIN-MIB", "portIfOutIndex"),
)
if mibBuilder.loadTexts:
    portPeakrateEntry.setStatus("current")


class _PortIfOutIndex_Type(Integer32):
    """Custom type portIfOutIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortIfOutIndex_Type.__name__ = "Integer32"
_PortIfOutIndex_Object = MibTableColumn
portIfOutIndex = _PortIfOutIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 31, 1, 1, 1),
    _PortIfOutIndex_Type()
)
portIfOutIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIfOutIndex.setStatus("current")


class _PortPeakrateEnable_Type(Integer32):
    """Custom type portPeakrateEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PortPeakrateEnable_Type.__name__ = "Integer32"
_PortPeakrateEnable_Object = MibTableColumn
portPeakrateEnable = _PortPeakrateEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 31, 1, 1, 2),
    _PortPeakrateEnable_Type()
)
portPeakrateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPeakrateEnable.setStatus("current")
_PortInUnicastPktsPeak_Type = Counter64
_PortInUnicastPktsPeak_Object = MibTableColumn
portInUnicastPktsPeak = _PortInUnicastPktsPeak_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 31, 1, 1, 3),
    _PortInUnicastPktsPeak_Type()
)
portInUnicastPktsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInUnicastPktsPeak.setStatus("current")
if mibBuilder.loadTexts:
    portInUnicastPktsPeak.setUnits("ppm")
_PortInUnicastTime_Type = OctetString
_PortInUnicastTime_Object = MibTableColumn
portInUnicastTime = _PortInUnicastTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 31, 1, 1, 4),
    _PortInUnicastTime_Type()
)
portInUnicastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInUnicastTime.setStatus("current")
_PortInMulticastPktsPeak_Type = Counter64
_PortInMulticastPktsPeak_Object = MibTableColumn
portInMulticastPktsPeak = _PortInMulticastPktsPeak_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 31, 1, 1, 5),
    _PortInMulticastPktsPeak_Type()
)
portInMulticastPktsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInMulticastPktsPeak.setStatus("current")
if mibBuilder.loadTexts:
    portInMulticastPktsPeak.setUnits("ppm")
_PortInMulticastTime_Type = OctetString
_PortInMulticastTime_Object = MibTableColumn
portInMulticastTime = _PortInMulticastTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 31, 1, 1, 6),
    _PortInMulticastTime_Type()
)
portInMulticastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInMulticastTime.setStatus("current")
_PortInBroadcastPktsPeak_Type = Counter64
_PortInBroadcastPktsPeak_Object = MibTableColumn
portInBroadcastPktsPeak = _PortInBroadcastPktsPeak_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 31, 1, 1, 7),
    _PortInBroadcastPktsPeak_Type()
)
portInBroadcastPktsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInBroadcastPktsPeak.setStatus("current")
if mibBuilder.loadTexts:
    portInBroadcastPktsPeak.setUnits("ppm")
_PortInBroadcastTime_Type = OctetString
_PortInBroadcastTime_Object = MibTableColumn
portInBroadcastTime = _PortInBroadcastTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 31, 1, 1, 8),
    _PortInBroadcastTime_Type()
)
portInBroadcastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInBroadcastTime.setStatus("current")
_PortInTotalErrPktsPeak_Type = Counter64
_PortInTotalErrPktsPeak_Object = MibTableColumn
portInTotalErrPktsPeak = _PortInTotalErrPktsPeak_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 31, 1, 1, 9),
    _PortInTotalErrPktsPeak_Type()
)
portInTotalErrPktsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInTotalErrPktsPeak.setStatus("current")
if mibBuilder.loadTexts:
    portInTotalErrPktsPeak.setUnits("ppm")
_PortInTotalErrTime_Type = OctetString
_PortInTotalErrTime_Object = MibTableColumn
portInTotalErrTime = _PortInTotalErrTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 31, 1, 1, 10),
    _PortInTotalErrTime_Type()
)
portInTotalErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInTotalErrTime.setStatus("current")
_PortOutUnicastPktsPeak_Type = Counter64
_PortOutUnicastPktsPeak_Object = MibTableColumn
portOutUnicastPktsPeak = _PortOutUnicastPktsPeak_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 31, 1, 1, 11),
    _PortOutUnicastPktsPeak_Type()
)
portOutUnicastPktsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOutUnicastPktsPeak.setStatus("current")
if mibBuilder.loadTexts:
    portOutUnicastPktsPeak.setUnits("ppm")
_PortOutUnicastTime_Type = OctetString
_PortOutUnicastTime_Object = MibTableColumn
portOutUnicastTime = _PortOutUnicastTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 31, 1, 1, 12),
    _PortOutUnicastTime_Type()
)
portOutUnicastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOutUnicastTime.setStatus("current")
_PortOutMulticastPktsPeak_Type = Counter64
_PortOutMulticastPktsPeak_Object = MibTableColumn
portOutMulticastPktsPeak = _PortOutMulticastPktsPeak_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 31, 1, 1, 13),
    _PortOutMulticastPktsPeak_Type()
)
portOutMulticastPktsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOutMulticastPktsPeak.setStatus("current")
if mibBuilder.loadTexts:
    portOutMulticastPktsPeak.setUnits("ppm")
_PortOutMulticastTime_Type = OctetString
_PortOutMulticastTime_Object = MibTableColumn
portOutMulticastTime = _PortOutMulticastTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 31, 1, 1, 14),
    _PortOutMulticastTime_Type()
)
portOutMulticastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOutMulticastTime.setStatus("current")
_PortOutBroadcastPktsPeak_Type = Counter64
_PortOutBroadcastPktsPeak_Object = MibTableColumn
portOutBroadcastPktsPeak = _PortOutBroadcastPktsPeak_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 31, 1, 1, 15),
    _PortOutBroadcastPktsPeak_Type()
)
portOutBroadcastPktsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOutBroadcastPktsPeak.setStatus("current")
if mibBuilder.loadTexts:
    portOutBroadcastPktsPeak.setUnits("ppm")
_PortOutBroadcastTime_Type = OctetString
_PortOutBroadcastTime_Object = MibTableColumn
portOutBroadcastTime = _PortOutBroadcastTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 31, 1, 1, 16),
    _PortOutBroadcastTime_Type()
)
portOutBroadcastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOutBroadcastTime.setStatus("current")
_PortOutTotalErrPktsPeak_Type = Counter64
_PortOutTotalErrPktsPeak_Object = MibTableColumn
portOutTotalErrPktsPeak = _PortOutTotalErrPktsPeak_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 31, 1, 1, 17),
    _PortOutTotalErrPktsPeak_Type()
)
portOutTotalErrPktsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOutTotalErrPktsPeak.setStatus("current")
if mibBuilder.loadTexts:
    portOutTotalErrPktsPeak.setUnits("ppm")
_PortOutTotalErrTime_Type = OctetString
_PortOutTotalErrTime_Object = MibTableColumn
portOutTotalErrTime = _PortOutTotalErrTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 31, 1, 1, 18),
    _PortOutTotalErrTime_Type()
)
portOutTotalErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOutTotalErrTime.setStatus("current")


class _PortClearPeakPkts_Type(Integer32):
    """Custom type portClearPeakPkts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("clear", 0)
    )


_PortClearPeakPkts_Type.__name__ = "Integer32"
_PortClearPeakPkts_Object = MibTableColumn
portClearPeakPkts = _PortClearPeakPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 31, 1, 1, 19),
    _PortClearPeakPkts_Type()
)
portClearPeakPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portClearPeakPkts.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXR10-PEAKRATE1MIN-MIB",
    **{"DisplayString": DisplayString,
       "zte": zte,
       "zxr10": zxr10,
       "zxr10switch": zxr10switch,
       "zxr10Peakrate1Min": zxr10Peakrate1Min,
       "portPeakrateTable": portPeakrateTable,
       "portPeakrateEntry": portPeakrateEntry,
       "portIfOutIndex": portIfOutIndex,
       "portPeakrateEnable": portPeakrateEnable,
       "portInUnicastPktsPeak": portInUnicastPktsPeak,
       "portInUnicastTime": portInUnicastTime,
       "portInMulticastPktsPeak": portInMulticastPktsPeak,
       "portInMulticastTime": portInMulticastTime,
       "portInBroadcastPktsPeak": portInBroadcastPktsPeak,
       "portInBroadcastTime": portInBroadcastTime,
       "portInTotalErrPktsPeak": portInTotalErrPktsPeak,
       "portInTotalErrTime": portInTotalErrTime,
       "portOutUnicastPktsPeak": portOutUnicastPktsPeak,
       "portOutUnicastTime": portOutUnicastTime,
       "portOutMulticastPktsPeak": portOutMulticastPktsPeak,
       "portOutMulticastTime": portOutMulticastTime,
       "portOutBroadcastPktsPeak": portOutBroadcastPktsPeak,
       "portOutBroadcastTime": portOutBroadcastTime,
       "portOutTotalErrPktsPeak": portOutTotalErrPktsPeak,
       "portOutTotalErrTime": portOutTotalErrTime,
       "portClearPeakPkts": portClearPeakPkts}
)
