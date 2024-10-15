# SNMP MIB module (ENTERASYS-VRRP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-VRRP-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:44 2024
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(VrId,
 vrrpOperationsInetAddrType) = mibBuilder.importSymbols(
    "VRRP-MIB",
    "VrId",
    "vrrpOperationsInetAddrType")


# MODULE-IDENTITY

etsysVrrpExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64)
)
etsysVrrpExtMIB.setRevisions(
        ("2009-08-10 19:43",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysVrrpExtOperations_ObjectIdentity = ObjectIdentity
etsysVrrpExtOperations = _EtsysVrrpExtOperations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 1)
)
_EtsysVrrpExtOperTable_Object = MibTable
etsysVrrpExtOperTable = _EtsysVrrpExtOperTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 1, 1)
)
if mibBuilder.loadTexts:
    etsysVrrpExtOperTable.setStatus("current")
_EtsysVrrpExtOperEntry_Object = MibTableRow
etsysVrrpExtOperEntry = _EtsysVrrpExtOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 1, 1, 1)
)
etsysVrrpExtOperEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtOperVrId"),
)
if mibBuilder.loadTexts:
    etsysVrrpExtOperEntry.setStatus("current")
_EtsysVrrpExtOperVrId_Type = VrId
_EtsysVrrpExtOperVrId_Object = MibTableColumn
etsysVrrpExtOperVrId = _EtsysVrrpExtOperVrId_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 1, 1, 1, 1),
    _EtsysVrrpExtOperVrId_Type()
)
etsysVrrpExtOperVrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysVrrpExtOperVrId.setStatus("current")


class _EtsysVrrpExtOperState_Type(Integer32):
    """Custom type etsysVrrpExtOperState based on Integer32"""
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
        *(("backup", 2),
          ("ifDown", 4),
          ("initialize", 1),
          ("master", 3),
          ("preemptDelay", 5))
    )


_EtsysVrrpExtOperState_Type.__name__ = "Integer32"
_EtsysVrrpExtOperState_Object = MibTableColumn
etsysVrrpExtOperState = _EtsysVrrpExtOperState_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 1, 1, 1, 2),
    _EtsysVrrpExtOperState_Type()
)
etsysVrrpExtOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysVrrpExtOperState.setStatus("current")


class _EtsysVrrpExtOperAcceptMode_Type(Integer32):
    """Custom type etsysVrrpExtOperAcceptMode based on Integer32"""
    defaultValue = 2

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


_EtsysVrrpExtOperAcceptMode_Type.__name__ = "Integer32"
_EtsysVrrpExtOperAcceptMode_Object = MibTableColumn
etsysVrrpExtOperAcceptMode = _EtsysVrrpExtOperAcceptMode_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 1, 1, 1, 3),
    _EtsysVrrpExtOperAcceptMode_Type()
)
etsysVrrpExtOperAcceptMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysVrrpExtOperAcceptMode.setStatus("current")


class _EtsysVrrpExtOperPreemptModeDelay_Type(Integer32):
    """Custom type etsysVrrpExtOperPreemptModeDelay based on Integer32"""
    defaultValue = 0


_EtsysVrrpExtOperPreemptModeDelay_Object = MibTableColumn
etsysVrrpExtOperPreemptModeDelay = _EtsysVrrpExtOperPreemptModeDelay_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 1, 1, 1, 4),
    _EtsysVrrpExtOperPreemptModeDelay_Type()
)
etsysVrrpExtOperPreemptModeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysVrrpExtOperPreemptModeDelay.setStatus("current")
_EtsysVrrpExtOperCriticalIpAddrCount_Type = Integer32
_EtsysVrrpExtOperCriticalIpAddrCount_Object = MibTableColumn
etsysVrrpExtOperCriticalIpAddrCount = _EtsysVrrpExtOperCriticalIpAddrCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 1, 1, 1, 5),
    _EtsysVrrpExtOperCriticalIpAddrCount_Type()
)
etsysVrrpExtOperCriticalIpAddrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysVrrpExtOperCriticalIpAddrCount.setStatus("current")
_EtsysVrrpExtCriticalIpAddrTable_Object = MibTable
etsysVrrpExtCriticalIpAddrTable = _EtsysVrrpExtCriticalIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 1, 2)
)
if mibBuilder.loadTexts:
    etsysVrrpExtCriticalIpAddrTable.setStatus("current")
_EtsysVrrpExtCriticalIpAddrEntry_Object = MibTableRow
etsysVrrpExtCriticalIpAddrEntry = _EtsysVrrpExtCriticalIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 1, 2, 1)
)
etsysVrrpExtCriticalIpAddrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtOperVrId"),
    (0, "VRRP-MIB", "vrrpOperationsInetAddrType"),
    (0, "ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtCriticalIpAddr"),
)
if mibBuilder.loadTexts:
    etsysVrrpExtCriticalIpAddrEntry.setStatus("current")


class _EtsysVrrpExtCriticalIpAddr_Type(InetAddress):
    """Custom type etsysVrrpExtCriticalIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_EtsysVrrpExtCriticalIpAddr_Type.__name__ = "InetAddress"
_EtsysVrrpExtCriticalIpAddr_Object = MibTableColumn
etsysVrrpExtCriticalIpAddr = _EtsysVrrpExtCriticalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 1, 2, 1, 1),
    _EtsysVrrpExtCriticalIpAddr_Type()
)
etsysVrrpExtCriticalIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysVrrpExtCriticalIpAddr.setStatus("current")


class _EtsysVrrpExtCriticalIpAddrPriority_Type(Integer32):
    """Custom type etsysVrrpExtCriticalIpAddrPriority based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_EtsysVrrpExtCriticalIpAddrPriority_Type.__name__ = "Integer32"
_EtsysVrrpExtCriticalIpAddrPriority_Object = MibTableColumn
etsysVrrpExtCriticalIpAddrPriority = _EtsysVrrpExtCriticalIpAddrPriority_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 1, 2, 1, 2),
    _EtsysVrrpExtCriticalIpAddrPriority_Type()
)
etsysVrrpExtCriticalIpAddrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysVrrpExtCriticalIpAddrPriority.setStatus("current")


class _EtsysVrrpExtCriticalIpAddrState_Type(Integer32):
    """Custom type etsysVrrpExtCriticalIpAddrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_EtsysVrrpExtCriticalIpAddrState_Type.__name__ = "Integer32"
_EtsysVrrpExtCriticalIpAddrState_Object = MibTableColumn
etsysVrrpExtCriticalIpAddrState = _EtsysVrrpExtCriticalIpAddrState_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 1, 2, 1, 3),
    _EtsysVrrpExtCriticalIpAddrState_Type()
)
etsysVrrpExtCriticalIpAddrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysVrrpExtCriticalIpAddrState.setStatus("current")
_EtsysVrrpExtCriticalIpAddrRowStatus_Type = RowStatus
_EtsysVrrpExtCriticalIpAddrRowStatus_Object = MibTableColumn
etsysVrrpExtCriticalIpAddrRowStatus = _EtsysVrrpExtCriticalIpAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 1, 2, 1, 4),
    _EtsysVrrpExtCriticalIpAddrRowStatus_Type()
)
etsysVrrpExtCriticalIpAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysVrrpExtCriticalIpAddrRowStatus.setStatus("current")
_EtsysVrrpExtConformance_ObjectIdentity = ObjectIdentity
etsysVrrpExtConformance = _EtsysVrrpExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 2)
)
_EtsysVrrpExtMIBCompliances_ObjectIdentity = ObjectIdentity
etsysVrrpExtMIBCompliances = _EtsysVrrpExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 2, 1)
)
_EtsysVrrpExtMIBGroups_ObjectIdentity = ObjectIdentity
etsysVrrpExtMIBGroups = _EtsysVrrpExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 2, 2)
)

# Managed Objects groups

etsysVrrpExtMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 2, 2, 1)
)
etsysVrrpExtMIBGroup.setObjects(
      *(("ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtOperState"),
        ("ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtOperAcceptMode"),
        ("ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtOperPreemptModeDelay"),
        ("ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtOperCriticalIpAddrCount"),
        ("ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtCriticalIpAddrPriority"),
        ("ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtCriticalIpAddrState"),
        ("ENTERASYS-VRRP-EXT-MIB", "etsysVrrpExtCriticalIpAddrRowStatus"))
)
if mibBuilder.loadTexts:
    etsysVrrpExtMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysVrrpExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 64, 2, 1, 1)
)
if mibBuilder.loadTexts:
    etsysVrrpExtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-VRRP-EXT-MIB",
    **{"etsysVrrpExtMIB": etsysVrrpExtMIB,
       "etsysVrrpExtOperations": etsysVrrpExtOperations,
       "etsysVrrpExtOperTable": etsysVrrpExtOperTable,
       "etsysVrrpExtOperEntry": etsysVrrpExtOperEntry,
       "etsysVrrpExtOperVrId": etsysVrrpExtOperVrId,
       "etsysVrrpExtOperState": etsysVrrpExtOperState,
       "etsysVrrpExtOperAcceptMode": etsysVrrpExtOperAcceptMode,
       "etsysVrrpExtOperPreemptModeDelay": etsysVrrpExtOperPreemptModeDelay,
       "etsysVrrpExtOperCriticalIpAddrCount": etsysVrrpExtOperCriticalIpAddrCount,
       "etsysVrrpExtCriticalIpAddrTable": etsysVrrpExtCriticalIpAddrTable,
       "etsysVrrpExtCriticalIpAddrEntry": etsysVrrpExtCriticalIpAddrEntry,
       "etsysVrrpExtCriticalIpAddr": etsysVrrpExtCriticalIpAddr,
       "etsysVrrpExtCriticalIpAddrPriority": etsysVrrpExtCriticalIpAddrPriority,
       "etsysVrrpExtCriticalIpAddrState": etsysVrrpExtCriticalIpAddrState,
       "etsysVrrpExtCriticalIpAddrRowStatus": etsysVrrpExtCriticalIpAddrRowStatus,
       "etsysVrrpExtConformance": etsysVrrpExtConformance,
       "etsysVrrpExtMIBCompliances": etsysVrrpExtMIBCompliances,
       "etsysVrrpExtMIBCompliance": etsysVrrpExtMIBCompliance,
       "etsysVrrpExtMIBGroups": etsysVrrpExtMIBGroups,
       "etsysVrrpExtMIBGroup": etsysVrrpExtMIBGroup}
)
