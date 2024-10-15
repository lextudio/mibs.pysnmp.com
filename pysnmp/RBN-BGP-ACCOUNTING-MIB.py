# SNMP MIB module (RBN-BGP-ACCOUNTING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-BGP-ACCOUNTING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:44:57 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

rbnBgpPolAcctMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 20)
)
rbnBgpPolAcctMIB.setRevisions(
        ("2005-09-20 00:00",
         "2002-03-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnBgpPolAcctMIBObjects_ObjectIdentity = ObjectIdentity
rbnBgpPolAcctMIBObjects = _RbnBgpPolAcctMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 20, 1)
)
_RbnBpaTable_Object = MibTable
rbnBpaTable = _RbnBpaTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 20, 1, 1)
)
if mibBuilder.loadTexts:
    rbnBpaTable.setStatus("current")
_RbnBpaEntry_Object = MibTableRow
rbnBpaEntry = _RbnBpaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 20, 1, 1, 1)
)
rbnBpaEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RBN-BGP-ACCOUNTING-MIB", "rbnBpaBucketIndex"),
)
if mibBuilder.loadTexts:
    rbnBpaEntry.setStatus("current")


class _RbnBpaBucketIndex_Type(Integer32):
    """Custom type rbnBpaBucketIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RbnBpaBucketIndex_Type.__name__ = "Integer32"
_RbnBpaBucketIndex_Object = MibTableColumn
rbnBpaBucketIndex = _RbnBpaBucketIndex_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 20, 1, 1, 1, 1),
    _RbnBpaBucketIndex_Type()
)
rbnBpaBucketIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnBpaBucketIndex.setStatus("current")
_RbnBpaInPacketCount_Type = Counter64
_RbnBpaInPacketCount_Object = MibTableColumn
rbnBpaInPacketCount = _RbnBpaInPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 20, 1, 1, 1, 2),
    _RbnBpaInPacketCount_Type()
)
rbnBpaInPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnBpaInPacketCount.setStatus("current")
_RbnBpaInOctetCount_Type = Counter64
_RbnBpaInOctetCount_Object = MibTableColumn
rbnBpaInOctetCount = _RbnBpaInOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 20, 1, 1, 1, 3),
    _RbnBpaInOctetCount_Type()
)
rbnBpaInOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnBpaInOctetCount.setStatus("current")


class _RbnBpaCircuitDescr_Type(SnmpAdminString):
    """Custom type rbnBpaCircuitDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 192),
    )


_RbnBpaCircuitDescr_Type.__name__ = "SnmpAdminString"
_RbnBpaCircuitDescr_Object = MibTableColumn
rbnBpaCircuitDescr = _RbnBpaCircuitDescr_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 20, 1, 1, 1, 4),
    _RbnBpaCircuitDescr_Type()
)
rbnBpaCircuitDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnBpaCircuitDescr.setStatus("current")


class _RbnBpaInterfaceName_Type(SnmpAdminString):
    """Custom type rbnBpaInterfaceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_RbnBpaInterfaceName_Type.__name__ = "SnmpAdminString"
_RbnBpaInterfaceName_Object = MibTableColumn
rbnBpaInterfaceName = _RbnBpaInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 20, 1, 1, 1, 5),
    _RbnBpaInterfaceName_Type()
)
rbnBpaInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnBpaInterfaceName.setStatus("current")


class _RbnBpaContextName_Type(SnmpAdminString):
    """Custom type rbnBpaContextName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RbnBpaContextName_Type.__name__ = "SnmpAdminString"
_RbnBpaContextName_Object = MibTableColumn
rbnBpaContextName = _RbnBpaContextName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 20, 1, 1, 1, 6),
    _RbnBpaContextName_Type()
)
rbnBpaContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnBpaContextName.setStatus("current")
_RbnBgpPolAcctMIBConformance_ObjectIdentity = ObjectIdentity
rbnBgpPolAcctMIBConformance = _RbnBgpPolAcctMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 20, 3)
)
_RbnBgpPolAcctMIBCompliances_ObjectIdentity = ObjectIdentity
rbnBgpPolAcctMIBCompliances = _RbnBgpPolAcctMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 20, 3, 1)
)
_RbnBgpPolAcctMIBGroups_ObjectIdentity = ObjectIdentity
rbnBgpPolAcctMIBGroups = _RbnBgpPolAcctMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 20, 3, 2)
)

# Managed Objects groups

rbnBpaTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 20, 3, 2, 1)
)
rbnBpaTableGroup.setObjects(
      *(("RBN-BGP-ACCOUNTING-MIB", "rbnBpaBucketIndex"),
        ("RBN-BGP-ACCOUNTING-MIB", "rbnBpaInPacketCount"),
        ("RBN-BGP-ACCOUNTING-MIB", "rbnBpaInOctetCount"))
)
if mibBuilder.loadTexts:
    rbnBpaTableGroup.setStatus("deprecated")

rbnBpaTableGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 20, 3, 2, 2)
)
rbnBpaTableGroup1.setObjects(
      *(("RBN-BGP-ACCOUNTING-MIB", "rbnBpaBucketIndex"),
        ("RBN-BGP-ACCOUNTING-MIB", "rbnBpaInPacketCount"),
        ("RBN-BGP-ACCOUNTING-MIB", "rbnBpaInOctetCount"),
        ("RBN-BGP-ACCOUNTING-MIB", "rbnBpaCircuitDescr"),
        ("RBN-BGP-ACCOUNTING-MIB", "rbnBpaInterfaceName"),
        ("RBN-BGP-ACCOUNTING-MIB", "rbnBpaContextName"))
)
if mibBuilder.loadTexts:
    rbnBpaTableGroup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rbnBgpPolAcctMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 20, 3, 1, 1)
)
if mibBuilder.loadTexts:
    rbnBgpPolAcctMIBCompliance.setStatus(
        "deprecated"
    )

rbnBgpPolAcctMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 20, 3, 1, 2)
)
if mibBuilder.loadTexts:
    rbnBgpPolAcctMIBCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-BGP-ACCOUNTING-MIB",
    **{"rbnBgpPolAcctMIB": rbnBgpPolAcctMIB,
       "rbnBgpPolAcctMIBObjects": rbnBgpPolAcctMIBObjects,
       "rbnBpaTable": rbnBpaTable,
       "rbnBpaEntry": rbnBpaEntry,
       "rbnBpaBucketIndex": rbnBpaBucketIndex,
       "rbnBpaInPacketCount": rbnBpaInPacketCount,
       "rbnBpaInOctetCount": rbnBpaInOctetCount,
       "rbnBpaCircuitDescr": rbnBpaCircuitDescr,
       "rbnBpaInterfaceName": rbnBpaInterfaceName,
       "rbnBpaContextName": rbnBpaContextName,
       "rbnBgpPolAcctMIBConformance": rbnBgpPolAcctMIBConformance,
       "rbnBgpPolAcctMIBCompliances": rbnBgpPolAcctMIBCompliances,
       "rbnBgpPolAcctMIBCompliance": rbnBgpPolAcctMIBCompliance,
       "rbnBgpPolAcctMIBCompliance1": rbnBgpPolAcctMIBCompliance1,
       "rbnBgpPolAcctMIBGroups": rbnBgpPolAcctMIBGroups,
       "rbnBpaTableGroup": rbnBpaTableGroup,
       "rbnBpaTableGroup1": rbnBpaTableGroup1}
)
