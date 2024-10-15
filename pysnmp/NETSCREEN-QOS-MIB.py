# SNMP MIB module (NETSCREEN-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:50 2024
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

(netscreenQos,) = mibBuilder.importSymbols(
    "NETSCREEN-SMI",
    "netscreenQos")

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


# MODULE-IDENTITY

netscreenQosMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 5, 0)
)
netscreenQosMibModule.setRevisions(
        ("2004-05-03 00:00",
         "2004-03-03 00:00",
         "2001-09-28 00:00",
         "2001-05-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _NsQosUsrShapingMode_Type(Integer32):
    """Custom type nsQosUsrShapingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("auto", 4),
          ("off", 0),
          ("off-on", 3),
          ("on", 1),
          ("on-off", 2))
    )


_NsQosUsrShapingMode_Type.__name__ = "Integer32"
_NsQosUsrShapingMode_Object = MibScalar
nsQosUsrShapingMode = _NsQosUsrShapingMode_Object(
    (1, 3, 6, 1, 4, 1, 3224, 5, 1),
    _NsQosUsrShapingMode_Type()
)
nsQosUsrShapingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsQosUsrShapingMode.setStatus("current")


class _NsQosSysShapingMode_Type(Integer32):
    """Custom type nsQosSysShapingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("auto", 4),
          ("off", 0),
          ("off-on", 3),
          ("on", 1),
          ("on-off", 2))
    )


_NsQosSysShapingMode_Type.__name__ = "Integer32"
_NsQosSysShapingMode_Object = MibScalar
nsQosSysShapingMode = _NsQosSysShapingMode_Object(
    (1, 3, 6, 1, 4, 1, 3224, 5, 2),
    _NsQosSysShapingMode_Type()
)
nsQosSysShapingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsQosSysShapingMode.setStatus("current")
_NsQosPly_ObjectIdentity = ObjectIdentity
nsQosPly = _NsQosPly_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 5, 3)
)
_NsQosPlyTable_Object = MibTable
nsQosPlyTable = _NsQosPlyTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 5, 3, 1)
)
if mibBuilder.loadTexts:
    nsQosPlyTable.setStatus("current")
_NsQosPlyEntry_Object = MibTableRow
nsQosPlyEntry = _NsQosPlyEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 5, 3, 1, 1)
)
nsQosPlyEntry.setIndexNames(
    (0, "NETSCREEN-QOS-MIB", "nsQosPlyId"),
)
if mibBuilder.loadTexts:
    nsQosPlyEntry.setStatus("current")


class _NsQosPlyId_Type(Integer32):
    """Custom type nsQosPlyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsQosPlyId_Type.__name__ = "Integer32"
_NsQosPlyId_Object = MibTableColumn
nsQosPlyId = _NsQosPlyId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 5, 3, 1, 1, 1),
    _NsQosPlyId_Type()
)
nsQosPlyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsQosPlyId.setStatus("current")
_NsQosPlyVsys_Type = Integer32
_NsQosPlyVsys_Object = MibTableColumn
nsQosPlyVsys = _NsQosPlyVsys_Object(
    (1, 3, 6, 1, 4, 1, 3224, 5, 3, 1, 1, 2),
    _NsQosPlyVsys_Type()
)
nsQosPlyVsys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsQosPlyVsys.setStatus("current")


class _NsQosPlyQosEnable_Type(Integer32):
    """Custom type nsQosPlyQosEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NsQosPlyQosEnable_Type.__name__ = "Integer32"
_NsQosPlyQosEnable_Object = MibTableColumn
nsQosPlyQosEnable = _NsQosPlyQosEnable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 5, 3, 1, 1, 3),
    _NsQosPlyQosEnable_Type()
)
nsQosPlyQosEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsQosPlyQosEnable.setStatus("current")
_NsQosPlyGanBW_Type = Integer32
_NsQosPlyGanBW_Object = MibTableColumn
nsQosPlyGanBW = _NsQosPlyGanBW_Object(
    (1, 3, 6, 1, 4, 1, 3224, 5, 3, 1, 1, 4),
    _NsQosPlyGanBW_Type()
)
nsQosPlyGanBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsQosPlyGanBW.setStatus("current")
_NsQosPlyMaxBW_Type = Integer32
_NsQosPlyMaxBW_Object = MibTableColumn
nsQosPlyMaxBW = _NsQosPlyMaxBW_Object(
    (1, 3, 6, 1, 4, 1, 3224, 5, 3, 1, 1, 5),
    _NsQosPlyMaxBW_Type()
)
nsQosPlyMaxBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsQosPlyMaxBW.setStatus("current")
_NsQosPlyTraffPriority_Type = Integer32
_NsQosPlyTraffPriority_Object = MibTableColumn
nsQosPlyTraffPriority = _NsQosPlyTraffPriority_Object(
    (1, 3, 6, 1, 4, 1, 3224, 5, 3, 1, 1, 6),
    _NsQosPlyTraffPriority_Type()
)
nsQosPlyTraffPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsQosPlyTraffPriority.setStatus("current")


class _NsQosPlyDSEnable_Type(Integer32):
    """Custom type nsQosPlyDSEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NsQosPlyDSEnable_Type.__name__ = "Integer32"
_NsQosPlyDSEnable_Object = MibTableColumn
nsQosPlyDSEnable = _NsQosPlyDSEnable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 5, 3, 1, 1, 7),
    _NsQosPlyDSEnable_Type()
)
nsQosPlyDSEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsQosPlyDSEnable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-QOS-MIB",
    **{"netscreenQosMibModule": netscreenQosMibModule,
       "nsQosUsrShapingMode": nsQosUsrShapingMode,
       "nsQosSysShapingMode": nsQosSysShapingMode,
       "nsQosPly": nsQosPly,
       "nsQosPlyTable": nsQosPlyTable,
       "nsQosPlyEntry": nsQosPlyEntry,
       "nsQosPlyId": nsQosPlyId,
       "nsQosPlyVsys": nsQosPlyVsys,
       "nsQosPlyQosEnable": nsQosPlyQosEnable,
       "nsQosPlyGanBW": nsQosPlyGanBW,
       "nsQosPlyMaxBW": nsQosPlyMaxBW,
       "nsQosPlyTraffPriority": nsQosPlyTraffPriority,
       "nsQosPlyDSEnable": nsQosPlyDSEnable}
)
