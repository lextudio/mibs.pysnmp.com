# SNMP MIB module (DPI-LANA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DPI-LANA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:18 2024
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

_Dpi_ObjectIdentity = ObjectIdentity
dpi = _Dpi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 901)
)
_DpiProducts_ObjectIdentity = ObjectIdentity
dpiProducts = _DpiProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 901, 1)
)
_DpiLANA_ObjectIdentity = ObjectIdentity
dpiLANA = _DpiLANA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 901, 1, 2)
)
_LanaInterface_ObjectIdentity = ObjectIdentity
lanaInterface = _LanaInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 901, 1, 2, 2)
)


class _LanaRs232PortSpeed_Type(Integer32):
    """Custom type lanaRs232PortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("b1200", 0),
          ("b19200", 4),
          ("b2400", 1),
          ("b38400", 5),
          ("b4800", 2),
          ("b9600", 3))
    )


_LanaRs232PortSpeed_Type.__name__ = "Integer32"
_LanaRs232PortSpeed_Object = MibScalar
lanaRs232PortSpeed = _LanaRs232PortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 901, 1, 2, 2, 1),
    _LanaRs232PortSpeed_Type()
)
lanaRs232PortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanaRs232PortSpeed.setStatus("mandatory")


class _LanaRs232AsyncPortBits_Type(Integer32):
    """Custom type lanaRs232AsyncPortBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("eight", 8),
          ("five", 5),
          ("seven", 7),
          ("six", 6))
    )


_LanaRs232AsyncPortBits_Type.__name__ = "Integer32"
_LanaRs232AsyncPortBits_Object = MibScalar
lanaRs232AsyncPortBits = _LanaRs232AsyncPortBits_Object(
    (1, 3, 6, 1, 4, 1, 901, 1, 2, 2, 2),
    _LanaRs232AsyncPortBits_Type()
)
lanaRs232AsyncPortBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanaRs232AsyncPortBits.setStatus("mandatory")


class _LanaRs232AsyncPortStopBits_Type(Integer32):
    """Custom type lanaRs232AsyncPortStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("one-and-half", 3),
          ("two", 2))
    )


_LanaRs232AsyncPortStopBits_Type.__name__ = "Integer32"
_LanaRs232AsyncPortStopBits_Object = MibScalar
lanaRs232AsyncPortStopBits = _LanaRs232AsyncPortStopBits_Object(
    (1, 3, 6, 1, 4, 1, 901, 1, 2, 2, 3),
    _LanaRs232AsyncPortStopBits_Type()
)
lanaRs232AsyncPortStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanaRs232AsyncPortStopBits.setStatus("mandatory")


class _LanaRs232AsyncPortParity_Type(Integer32):
    """Custom type lanaRs232AsyncPortParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even", 3),
          ("none", 1),
          ("odd", 2))
    )


_LanaRs232AsyncPortParity_Type.__name__ = "Integer32"
_LanaRs232AsyncPortParity_Object = MibScalar
lanaRs232AsyncPortParity = _LanaRs232AsyncPortParity_Object(
    (1, 3, 6, 1, 4, 1, 901, 1, 2, 2, 4),
    _LanaRs232AsyncPortParity_Type()
)
lanaRs232AsyncPortParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanaRs232AsyncPortParity.setStatus("mandatory")
_LanaSubnetMask_Type = IpAddress
_LanaSubnetMask_Object = MibScalar
lanaSubnetMask = _LanaSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 901, 1, 2, 2, 5),
    _LanaSubnetMask_Type()
)
lanaSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanaSubnetMask.setStatus("mandatory")
_LanaDefGatewayIpAddr_Type = IpAddress
_LanaDefGatewayIpAddr_Object = MibScalar
lanaDefGatewayIpAddr = _LanaDefGatewayIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 901, 1, 2, 2, 6),
    _LanaDefGatewayIpAddr_Type()
)
lanaDefGatewayIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanaDefGatewayIpAddr.setStatus("mandatory")


class _LanaForwBroadcast_Type(Integer32):
    """Custom type lanaForwBroadcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_LanaForwBroadcast_Type.__name__ = "Integer32"
_LanaForwBroadcast_Object = MibScalar
lanaForwBroadcast = _LanaForwBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 901, 1, 2, 2, 7),
    _LanaForwBroadcast_Type()
)
lanaForwBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanaForwBroadcast.setStatus("mandatory")
_LanaMgmt_ObjectIdentity = ObjectIdentity
lanaMgmt = _LanaMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 901, 1, 2, 3)
)


class _LanaReset_Type(Integer32):
    """Custom type lanaReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("one", 1)
    )


_LanaReset_Type.__name__ = "Integer32"
_LanaReset_Object = MibScalar
lanaReset = _LanaReset_Object(
    (1, 3, 6, 1, 4, 1, 901, 1, 2, 3, 1),
    _LanaReset_Type()
)
lanaReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanaReset.setStatus("mandatory")


class _LanaFactoryDefault_Type(Integer32):
    """Custom type lanaFactoryDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("one", 1)
    )


_LanaFactoryDefault_Type.__name__ = "Integer32"
_LanaFactoryDefault_Object = MibScalar
lanaFactoryDefault = _LanaFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 901, 1, 2, 3, 2),
    _LanaFactoryDefault_Type()
)
lanaFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanaFactoryDefault.setStatus("mandatory")


class _LanaUpdateUnit_Type(Integer32):
    """Custom type lanaUpdateUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("one", 1)
    )


_LanaUpdateUnit_Type.__name__ = "Integer32"
_LanaUpdateUnit_Object = MibScalar
lanaUpdateUnit = _LanaUpdateUnit_Object(
    (1, 3, 6, 1, 4, 1, 901, 1, 2, 3, 3),
    _LanaUpdateUnit_Type()
)
lanaUpdateUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanaUpdateUnit.setStatus("mandatory")
_LanaSWMajorVer_Type = Integer32
_LanaSWMajorVer_Object = MibScalar
lanaSWMajorVer = _LanaSWMajorVer_Object(
    (1, 3, 6, 1, 4, 1, 901, 1, 2, 3, 4),
    _LanaSWMajorVer_Type()
)
lanaSWMajorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanaSWMajorVer.setStatus("mandatory")
_LanaSWMinorVer_Type = Integer32
_LanaSWMinorVer_Object = MibScalar
lanaSWMinorVer = _LanaSWMinorVer_Object(
    (1, 3, 6, 1, 4, 1, 901, 1, 2, 3, 5),
    _LanaSWMinorVer_Type()
)
lanaSWMinorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanaSWMinorVer.setStatus("mandatory")
_LanaSWRevision_Type = Integer32
_LanaSWRevision_Object = MibScalar
lanaSWRevision = _LanaSWRevision_Object(
    (1, 3, 6, 1, 4, 1, 901, 1, 2, 3, 6),
    _LanaSWRevision_Type()
)
lanaSWRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanaSWRevision.setStatus("mandatory")
_LanaNest_ObjectIdentity = ObjectIdentity
lanaNest = _LanaNest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 901, 1, 2, 4)
)
_LanaIPAddrTableTotal_Type = Integer32
_LanaIPAddrTableTotal_Object = MibScalar
lanaIPAddrTableTotal = _LanaIPAddrTableTotal_Object(
    (1, 3, 6, 1, 4, 1, 901, 1, 2, 4, 1),
    _LanaIPAddrTableTotal_Type()
)
lanaIPAddrTableTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanaIPAddrTableTotal.setStatus("mandatory")
_LanaIPAddrTable_Object = MibTable
lanaIPAddrTable = _LanaIPAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 901, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    lanaIPAddrTable.setStatus("mandatory")
_LanaIPAddrEntry_Object = MibTableRow
lanaIPAddrEntry = _LanaIPAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 901, 1, 2, 4, 2, 1)
)
lanaIPAddrEntry.setIndexNames(
    (0, "DPI-LANA-MIB", "lanaIPAddrIndex"),
)
if mibBuilder.loadTexts:
    lanaIPAddrEntry.setStatus("mandatory")


class _LanaIPAddrIndex_Type(Integer32):
    """Custom type lanaIPAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_LanaIPAddrIndex_Type.__name__ = "Integer32"
_LanaIPAddrIndex_Object = MibTableColumn
lanaIPAddrIndex = _LanaIPAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 901, 1, 2, 4, 2, 1, 1),
    _LanaIPAddrIndex_Type()
)
lanaIPAddrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanaIPAddrIndex.setStatus("mandatory")
_LanaIPAddr_Type = IpAddress
_LanaIPAddr_Object = MibTableColumn
lanaIPAddr = _LanaIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 901, 1, 2, 4, 2, 1, 2),
    _LanaIPAddr_Type()
)
lanaIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanaIPAddr.setStatus("mandatory")
_LanaIPAddrTableClear_Type = Integer32
_LanaIPAddrTableClear_Object = MibScalar
lanaIPAddrTableClear = _LanaIPAddrTableClear_Object(
    (1, 3, 6, 1, 4, 1, 901, 1, 2, 4, 3),
    _LanaIPAddrTableClear_Type()
)
lanaIPAddrTableClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanaIPAddrTableClear.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DPI-LANA-MIB",
    **{"dpi": dpi,
       "dpiProducts": dpiProducts,
       "dpiLANA": dpiLANA,
       "lanaInterface": lanaInterface,
       "lanaRs232PortSpeed": lanaRs232PortSpeed,
       "lanaRs232AsyncPortBits": lanaRs232AsyncPortBits,
       "lanaRs232AsyncPortStopBits": lanaRs232AsyncPortStopBits,
       "lanaRs232AsyncPortParity": lanaRs232AsyncPortParity,
       "lanaSubnetMask": lanaSubnetMask,
       "lanaDefGatewayIpAddr": lanaDefGatewayIpAddr,
       "lanaForwBroadcast": lanaForwBroadcast,
       "lanaMgmt": lanaMgmt,
       "lanaReset": lanaReset,
       "lanaFactoryDefault": lanaFactoryDefault,
       "lanaUpdateUnit": lanaUpdateUnit,
       "lanaSWMajorVer": lanaSWMajorVer,
       "lanaSWMinorVer": lanaSWMinorVer,
       "lanaSWRevision": lanaSWRevision,
       "lanaNest": lanaNest,
       "lanaIPAddrTableTotal": lanaIPAddrTableTotal,
       "lanaIPAddrTable": lanaIPAddrTable,
       "lanaIPAddrEntry": lanaIPAddrEntry,
       "lanaIPAddrIndex": lanaIPAddrIndex,
       "lanaIPAddr": lanaIPAddr,
       "lanaIPAddrTableClear": lanaIPAddrTableClear}
)
