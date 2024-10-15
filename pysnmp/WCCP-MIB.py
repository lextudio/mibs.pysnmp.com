# SNMP MIB module (WCCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WCCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:41 2024
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

(blueCoatMgmt,) = mibBuilder.importSymbols(
    "BLUECOAT-MIB",
    "blueCoatMgmt")

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

(DisplayString,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

deviceWccpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class WccpServiceType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("standard", 1),
          ("unknown", 3))
    )



class WccpVersion(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 3),
          ("version1", 1),
          ("version2", 2))
    )



# MIB Managed Objects in the order of their OIDs

_DeviceWccpEnabled_Type = TruthValue
_DeviceWccpEnabled_Object = MibScalar
deviceWccpEnabled = _DeviceWccpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 5, 1),
    _DeviceWccpEnabled_Type()
)
deviceWccpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceWccpEnabled.setStatus("current")
_DeviceWccpMIBObjects_ObjectIdentity = ObjectIdentity
deviceWccpMIBObjects = _DeviceWccpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 5, 2)
)
_DeviceWccpValues_ObjectIdentity = ObjectIdentity
deviceWccpValues = _DeviceWccpValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1)
)
_DeviceWccpValueTable_Object = MibTable
deviceWccpValueTable = _DeviceWccpValueTable_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    deviceWccpValueTable.setStatus("current")
_DeviceWccpValueEntry_Object = MibTableRow
deviceWccpValueEntry = _DeviceWccpValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1)
)
deviceWccpValueEntry.setIndexNames(
    (0, "WCCP-MIB", "deviceWccpIndex"),
)
if mibBuilder.loadTexts:
    deviceWccpValueEntry.setStatus("current")


class _DeviceWccpIndex_Type(Integer32):
    """Custom type deviceWccpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DeviceWccpIndex_Type.__name__ = "Integer32"
_DeviceWccpIndex_Object = MibTableColumn
deviceWccpIndex = _DeviceWccpIndex_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 1),
    _DeviceWccpIndex_Type()
)
deviceWccpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    deviceWccpIndex.setStatus("current")
_DeviceWccpServiceID_Type = Integer32
_DeviceWccpServiceID_Object = MibTableColumn
deviceWccpServiceID = _DeviceWccpServiceID_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 2),
    _DeviceWccpServiceID_Type()
)
deviceWccpServiceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceWccpServiceID.setStatus("current")
_DeviceWccpServiceType_Type = WccpServiceType
_DeviceWccpServiceType_Object = MibTableColumn
deviceWccpServiceType = _DeviceWccpServiceType_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 3),
    _DeviceWccpServiceType_Type()
)
deviceWccpServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceWccpServiceType.setStatus("current")
_DeviceWccpServiceVersion_Type = WccpVersion
_DeviceWccpServiceVersion_Object = MibTableColumn
deviceWccpServiceVersion = _DeviceWccpServiceVersion_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 4),
    _DeviceWccpServiceVersion_Type()
)
deviceWccpServiceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceWccpServiceVersion.setStatus("current")
_DeviceWccpPacketsRedir_Type = Counter64
_DeviceWccpPacketsRedir_Object = MibTableColumn
deviceWccpPacketsRedir = _DeviceWccpPacketsRedir_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 5),
    _DeviceWccpPacketsRedir_Type()
)
deviceWccpPacketsRedir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceWccpPacketsRedir.setStatus("current")
_DeviceWccpPacketsLowRedir_Type = Counter32
_DeviceWccpPacketsLowRedir_Object = MibTableColumn
deviceWccpPacketsLowRedir = _DeviceWccpPacketsLowRedir_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 6),
    _DeviceWccpPacketsLowRedir_Type()
)
deviceWccpPacketsLowRedir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceWccpPacketsLowRedir.setStatus("current")
_DeviceWccpBytesRedir_Type = Counter64
_DeviceWccpBytesRedir_Object = MibTableColumn
deviceWccpBytesRedir = _DeviceWccpBytesRedir_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 7),
    _DeviceWccpBytesRedir_Type()
)
deviceWccpBytesRedir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceWccpBytesRedir.setStatus("current")
_DeviceWccpBytesLowRedir_Type = Counter32
_DeviceWccpBytesLowRedir_Object = MibTableColumn
deviceWccpBytesLowRedir = _DeviceWccpBytesLowRedir_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 8),
    _DeviceWccpBytesLowRedir_Type()
)
deviceWccpBytesLowRedir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceWccpBytesLowRedir.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WCCP-MIB",
    **{"WccpServiceType": WccpServiceType,
       "WccpVersion": WccpVersion,
       "deviceWccpMIB": deviceWccpMIB,
       "deviceWccpEnabled": deviceWccpEnabled,
       "deviceWccpMIBObjects": deviceWccpMIBObjects,
       "deviceWccpValues": deviceWccpValues,
       "deviceWccpValueTable": deviceWccpValueTable,
       "deviceWccpValueEntry": deviceWccpValueEntry,
       "deviceWccpIndex": deviceWccpIndex,
       "deviceWccpServiceID": deviceWccpServiceID,
       "deviceWccpServiceType": deviceWccpServiceType,
       "deviceWccpServiceVersion": deviceWccpServiceVersion,
       "deviceWccpPacketsRedir": deviceWccpPacketsRedir,
       "deviceWccpPacketsLowRedir": deviceWccpPacketsLowRedir,
       "deviceWccpBytesRedir": deviceWccpBytesRedir,
       "deviceWccpBytesLowRedir": deviceWccpBytesLowRedir}
)
