# SNMP MIB module (AtiStackInfo-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AtiStackInfo-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:09 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

alliedTelesyn = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207)
)


# Types definitions



class MACAddress(OctetString):
    """Custom type MACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibObject_ObjectIdentity = ObjectIdentity
mibObject = _MibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8)
)
_AtiStackInfoMib_ObjectIdentity = ObjectIdentity
atiStackInfoMib = _AtiStackInfoMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 16)
)
_AtiswitchEnhancedStacking_ObjectIdentity = ObjectIdentity
atiswitchEnhancedStacking = _AtiswitchEnhancedStacking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 16, 1)
)


class _AtiswitchEnhStackMode_Type(Integer32):
    """Custom type atiswitchEnhStackMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2),
          ("unavailable", 3))
    )


_AtiswitchEnhStackMode_Type.__name__ = "Integer32"
_AtiswitchEnhStackMode_Object = MibScalar
atiswitchEnhStackMode = _AtiswitchEnhStackMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 16, 1, 1),
    _AtiswitchEnhStackMode_Type()
)
atiswitchEnhStackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiswitchEnhStackMode.setStatus("current")


class _AtiswitchEnhStackDiscover_Type(Integer32):
    """Custom type atiswitchEnhStackDiscover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discover", 1),
          ("do-not-discover", 2))
    )


_AtiswitchEnhStackDiscover_Type.__name__ = "Integer32"
_AtiswitchEnhStackDiscover_Object = MibScalar
atiswitchEnhStackDiscover = _AtiswitchEnhStackDiscover_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 16, 1, 2),
    _AtiswitchEnhStackDiscover_Type()
)
atiswitchEnhStackDiscover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiswitchEnhStackDiscover.setStatus("current")
_AtiswitchEnhStackRemoteNumber_Type = Integer32
_AtiswitchEnhStackRemoteNumber_Object = MibScalar
atiswitchEnhStackRemoteNumber = _AtiswitchEnhStackRemoteNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 16, 1, 3),
    _AtiswitchEnhStackRemoteNumber_Type()
)
atiswitchEnhStackRemoteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEnhStackRemoteNumber.setStatus("current")
_AtiswitchEnhStackTable_Object = MibTable
atiswitchEnhStackTable = _AtiswitchEnhStackTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 16, 1, 4)
)
if mibBuilder.loadTexts:
    atiswitchEnhStackTable.setStatus("current")
_AtiswitchEnhStackEntry_Object = MibTableRow
atiswitchEnhStackEntry = _AtiswitchEnhStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 16, 1, 4, 1)
)
atiswitchEnhStackEntry.setIndexNames(
    (0, "AtiStackInfo-MIB", "atiswitchEnhStackSwId"),
)
if mibBuilder.loadTexts:
    atiswitchEnhStackEntry.setStatus("current")


class _AtiswitchEnhStackSwId_Type(Integer32):
    """Custom type atiswitchEnhStackSwId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtiswitchEnhStackSwId_Type.__name__ = "Integer32"
_AtiswitchEnhStackSwId_Object = MibTableColumn
atiswitchEnhStackSwId = _AtiswitchEnhStackSwId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 16, 1, 4, 1, 1),
    _AtiswitchEnhStackSwId_Type()
)
atiswitchEnhStackSwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEnhStackSwId.setStatus("current")
_AtiswitchEnhStackSwMacAddr_Type = MACAddress
_AtiswitchEnhStackSwMacAddr_Object = MibTableColumn
atiswitchEnhStackSwMacAddr = _AtiswitchEnhStackSwMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 16, 1, 4, 1, 2),
    _AtiswitchEnhStackSwMacAddr_Type()
)
atiswitchEnhStackSwMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEnhStackSwMacAddr.setStatus("current")


class _AtiswitchEnhStackSwName_Type(DisplayString):
    """Custom type atiswitchEnhStackSwName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AtiswitchEnhStackSwName_Type.__name__ = "DisplayString"
_AtiswitchEnhStackSwName_Object = MibTableColumn
atiswitchEnhStackSwName = _AtiswitchEnhStackSwName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 16, 1, 4, 1, 3),
    _AtiswitchEnhStackSwName_Type()
)
atiswitchEnhStackSwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEnhStackSwName.setStatus("current")


class _AtiswitchEnhStackSwMode_Type(DisplayString):
    """Custom type atiswitchEnhStackSwMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AtiswitchEnhStackSwMode_Type.__name__ = "DisplayString"
_AtiswitchEnhStackSwMode_Object = MibTableColumn
atiswitchEnhStackSwMode = _AtiswitchEnhStackSwMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 16, 1, 4, 1, 4),
    _AtiswitchEnhStackSwMode_Type()
)
atiswitchEnhStackSwMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEnhStackSwMode.setStatus("current")


class _AtiswitchEnhStackSwSoftwareVersion_Type(DisplayString):
    """Custom type atiswitchEnhStackSwSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AtiswitchEnhStackSwSoftwareVersion_Type.__name__ = "DisplayString"
_AtiswitchEnhStackSwSoftwareVersion_Object = MibTableColumn
atiswitchEnhStackSwSoftwareVersion = _AtiswitchEnhStackSwSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 16, 1, 4, 1, 5),
    _AtiswitchEnhStackSwSoftwareVersion_Type()
)
atiswitchEnhStackSwSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEnhStackSwSoftwareVersion.setStatus("current")


class _AtiswitchEnhStackSwModel_Type(DisplayString):
    """Custom type atiswitchEnhStackSwModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AtiswitchEnhStackSwModel_Type.__name__ = "DisplayString"
_AtiswitchEnhStackSwModel_Object = MibTableColumn
atiswitchEnhStackSwModel = _AtiswitchEnhStackSwModel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 16, 1, 4, 1, 6),
    _AtiswitchEnhStackSwModel_Type()
)
atiswitchEnhStackSwModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiswitchEnhStackSwModel.setStatus("current")
_AtiswitchEnhStackConnect_Type = TruthValue
_AtiswitchEnhStackConnect_Object = MibTableColumn
atiswitchEnhStackConnect = _AtiswitchEnhStackConnect_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 16, 1, 4, 1, 7),
    _AtiswitchEnhStackConnect_Type()
)
atiswitchEnhStackConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiswitchEnhStackConnect.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AtiStackInfo-MIB",
    **{"MACAddress": MACAddress,
       "alliedTelesyn": alliedTelesyn,
       "mibObject": mibObject,
       "atiStackInfoMib": atiStackInfoMib,
       "atiswitchEnhancedStacking": atiswitchEnhancedStacking,
       "atiswitchEnhStackMode": atiswitchEnhStackMode,
       "atiswitchEnhStackDiscover": atiswitchEnhStackDiscover,
       "atiswitchEnhStackRemoteNumber": atiswitchEnhStackRemoteNumber,
       "atiswitchEnhStackTable": atiswitchEnhStackTable,
       "atiswitchEnhStackEntry": atiswitchEnhStackEntry,
       "atiswitchEnhStackSwId": atiswitchEnhStackSwId,
       "atiswitchEnhStackSwMacAddr": atiswitchEnhStackSwMacAddr,
       "atiswitchEnhStackSwName": atiswitchEnhStackSwName,
       "atiswitchEnhStackSwMode": atiswitchEnhStackSwMode,
       "atiswitchEnhStackSwSoftwareVersion": atiswitchEnhStackSwSoftwareVersion,
       "atiswitchEnhStackSwModel": atiswitchEnhStackSwModel,
       "atiswitchEnhStackConnect": atiswitchEnhStackConnect}
)
