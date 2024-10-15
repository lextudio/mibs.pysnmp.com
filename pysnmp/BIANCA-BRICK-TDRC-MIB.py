# SNMP MIB module (BIANCA-BRICK-TDRC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-TDRC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:48 2024
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

_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Biboip_ObjectIdentity = ObjectIdentity
biboip = _Biboip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 5)
)
_IpTdrcTable_Object = MibTable
ipTdrcTable = _IpTdrcTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 43)
)
if mibBuilder.loadTexts:
    ipTdrcTable.setStatus("mandatory")
_IpTdrcEntry_Object = MibTableRow
ipTdrcEntry = _IpTdrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 43, 1)
)
ipTdrcEntry.setIndexNames(
    (0, "BIANCA-BRICK-TDRC-MIB", "ipTdrcIfIndex"),
)
if mibBuilder.loadTexts:
    ipTdrcEntry.setStatus("mandatory")


class _IpTdrcIfIndex_Type(Integer32):
    """Custom type ipTdrcIfIndex based on Integer32"""
    defaultValue = 0


_IpTdrcIfIndex_Object = MibTableColumn
ipTdrcIfIndex = _IpTdrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 43, 1, 1),
    _IpTdrcIfIndex_Type()
)
ipTdrcIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTdrcIfIndex.setStatus("mandatory")


class _IpTdrcMode_Type(Integer32):
    """Custom type ipTdrcMode based on Integer32"""
    defaultValue = 3

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
        *(("ack-prioritisation", 2),
          ("delete", 5),
          ("disabled", 1),
          ("dynamic", 4),
          ("static", 3))
    )


_IpTdrcMode_Type.__name__ = "Integer32"
_IpTdrcMode_Object = MibTableColumn
ipTdrcMode = _IpTdrcMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 43, 1, 2),
    _IpTdrcMode_Type()
)
ipTdrcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTdrcMode.setStatus("mandatory")


class _IpTdrcMaxRate_Type(Integer32):
    """Custom type ipTdrcMaxRate based on Integer32"""
    defaultValue = 1024000


_IpTdrcMaxRate_Object = MibTableColumn
ipTdrcMaxRate = _IpTdrcMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 43, 1, 3),
    _IpTdrcMaxRate_Type()
)
ipTdrcMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTdrcMaxRate.setStatus("mandatory")


class _IpTdrcWindowScaling_Type(Integer32):
    """Custom type ipTdrcWindowScaling based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_IpTdrcWindowScaling_Type.__name__ = "Integer32"
_IpTdrcWindowScaling_Object = MibTableColumn
ipTdrcWindowScaling = _IpTdrcWindowScaling_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 43, 1, 4),
    _IpTdrcWindowScaling_Type()
)
ipTdrcWindowScaling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTdrcWindowScaling.setStatus("mandatory")


class _IpTdrcMss_Type(Integer32):
    """Custom type ipTdrcMss based on Integer32"""
    defaultValue = 1452

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4056),
    )


_IpTdrcMss_Type.__name__ = "Integer32"
_IpTdrcMss_Object = MibTableColumn
ipTdrcMss = _IpTdrcMss_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 43, 1, 5),
    _IpTdrcMss_Type()
)
ipTdrcMss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTdrcMss.setStatus("mandatory")


class _IpTdrcServices_Type(Integer32):
    """Custom type ipTdrcServices based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("listed-only", 1))
    )


_IpTdrcServices_Type.__name__ = "Integer32"
_IpTdrcServices_Object = MibTableColumn
ipTdrcServices = _IpTdrcServices_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 43, 1, 6),
    _IpTdrcServices_Type()
)
ipTdrcServices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTdrcServices.setStatus("mandatory")
_IpTdrcServiceTable_Object = MibTable
ipTdrcServiceTable = _IpTdrcServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 44)
)
if mibBuilder.loadTexts:
    ipTdrcServiceTable.setStatus("mandatory")
_IpTdrcServiceEntry_Object = MibTableRow
ipTdrcServiceEntry = _IpTdrcServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 44, 1)
)
ipTdrcServiceEntry.setIndexNames(
    (0, "BIANCA-BRICK-TDRC-MIB", "ipTdrcServiceIfIndex"),
)
if mibBuilder.loadTexts:
    ipTdrcServiceEntry.setStatus("mandatory")


class _IpTdrcServiceIfIndex_Type(Integer32):
    """Custom type ipTdrcServiceIfIndex based on Integer32"""
    defaultValue = 0


_IpTdrcServiceIfIndex_Object = MibTableColumn
ipTdrcServiceIfIndex = _IpTdrcServiceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 44, 1, 1),
    _IpTdrcServiceIfIndex_Type()
)
ipTdrcServiceIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTdrcServiceIfIndex.setStatus("mandatory")


class _IpTdrcServicePort_Type(Integer32):
    """Custom type ipTdrcServicePort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpTdrcServicePort_Type.__name__ = "Integer32"
_IpTdrcServicePort_Object = MibTableColumn
ipTdrcServicePort = _IpTdrcServicePort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 44, 1, 2),
    _IpTdrcServicePort_Type()
)
ipTdrcServicePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTdrcServicePort.setStatus("mandatory")


class _IpTdrcServiceStatus_Type(Integer32):
    """Custom type ipTdrcServiceStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("delete", 5),
          ("disabled", 2),
          ("enabled", 1))
    )


_IpTdrcServiceStatus_Type.__name__ = "Integer32"
_IpTdrcServiceStatus_Object = MibTableColumn
ipTdrcServiceStatus = _IpTdrcServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 44, 1, 3),
    _IpTdrcServiceStatus_Type()
)
ipTdrcServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTdrcServiceStatus.setStatus("mandatory")
_IpTdrcServiceAlias_Type = DisplayString
_IpTdrcServiceAlias_Object = MibTableColumn
ipTdrcServiceAlias = _IpTdrcServiceAlias_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 44, 1, 4),
    _IpTdrcServiceAlias_Type()
)
ipTdrcServiceAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTdrcServiceAlias.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-TDRC-MIB",
    **{"bintec": bintec,
       "bibo": bibo,
       "biboip": biboip,
       "ipTdrcTable": ipTdrcTable,
       "ipTdrcEntry": ipTdrcEntry,
       "ipTdrcIfIndex": ipTdrcIfIndex,
       "ipTdrcMode": ipTdrcMode,
       "ipTdrcMaxRate": ipTdrcMaxRate,
       "ipTdrcWindowScaling": ipTdrcWindowScaling,
       "ipTdrcMss": ipTdrcMss,
       "ipTdrcServices": ipTdrcServices,
       "ipTdrcServiceTable": ipTdrcServiceTable,
       "ipTdrcServiceEntry": ipTdrcServiceEntry,
       "ipTdrcServiceIfIndex": ipTdrcServiceIfIndex,
       "ipTdrcServicePort": ipTdrcServicePort,
       "ipTdrcServiceStatus": ipTdrcServiceStatus,
       "ipTdrcServiceAlias": ipTdrcServiceAlias}
)
