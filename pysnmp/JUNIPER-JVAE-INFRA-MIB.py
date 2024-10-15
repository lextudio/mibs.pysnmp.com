# SNMP MIB module (JUNIPER-JVAE-INFRA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-JVAE-INFRA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:23 2024
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

(InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6")

(jnxJVAEMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxJVAEMibRoot")

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

jnxJVAEInfraMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 1)
)
jnxJVAEInfraMIB.setRevisions(
        ("2012-08-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxJVAEInfraNotifications_ObjectIdentity = ObjectIdentity
jnxJVAEInfraNotifications = _JnxJVAEInfraNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 0)
)
_JnxJVAEInfraObjects_ObjectIdentity = ObjectIdentity
jnxJVAEInfraObjects = _JnxJVAEInfraObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1)
)
_JnxJVAEInfraTables_ObjectIdentity = ObjectIdentity
jnxJVAEInfraTables = _JnxJVAEInfraTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1)
)
_JnxJVAECNTable_Object = MibTable
jnxJVAECNTable = _JnxJVAECNTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxJVAECNTable.setStatus("current")
_JnxJVAECNEntry_Object = MibTableRow
jnxJVAECNEntry = _JnxJVAECNEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 1, 1)
)
jnxJVAECNEntry.setIndexNames(
    (0, "JUNIPER-JVAE-INFRA-MIB", "jnxJVAECNId"),
)
if mibBuilder.loadTexts:
    jnxJVAECNEntry.setStatus("current")


class _JnxJVAECNId_Type(DisplayString):
    """Custom type jnxJVAECNId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JnxJVAECNId_Type.__name__ = "DisplayString"
_JnxJVAECNId_Object = MibTableColumn
jnxJVAECNId = _JnxJVAECNId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 1, 1, 1),
    _JnxJVAECNId_Type()
)
jnxJVAECNId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJVAECNId.setStatus("current")


class _JnxJVAECNName_Type(DisplayString):
    """Custom type jnxJVAECNName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 60),
    )


_JnxJVAECNName_Type.__name__ = "DisplayString"
_JnxJVAECNName_Object = MibTableColumn
jnxJVAECNName = _JnxJVAECNName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 1, 1, 2),
    _JnxJVAECNName_Type()
)
jnxJVAECNName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNName.setStatus("current")


class _JnxJVAECCName_Type(DisplayString):
    """Custom type jnxJVAECCName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 60),
    )


_JnxJVAECCName_Type.__name__ = "DisplayString"
_JnxJVAECCName_Object = MibTableColumn
jnxJVAECCName = _JnxJVAECCName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 1, 1, 3),
    _JnxJVAECCName_Type()
)
jnxJVAECCName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECCName.setStatus("current")


class _JnxJVAECNState_Type(Integer32):
    """Custom type jnxJVAECNState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("offline", 0),
          ("online", 1))
    )


_JnxJVAECNState_Type.__name__ = "Integer32"
_JnxJVAECNState_Object = MibTableColumn
jnxJVAECNState = _JnxJVAECNState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 1, 1, 4),
    _JnxJVAECNState_Type()
)
jnxJVAECNState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNState.setStatus("current")


class _JnxJVAECNLastStateChange_Type(DisplayString):
    """Custom type jnxJVAECNLastStateChange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(26, 30),
    )


_JnxJVAECNLastStateChange_Type.__name__ = "DisplayString"
_JnxJVAECNLastStateChange_Object = MibTableColumn
jnxJVAECNLastStateChange = _JnxJVAECNLastStateChange_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 1, 1, 5),
    _JnxJVAECNLastStateChange_Type()
)
jnxJVAECNLastStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNLastStateChange.setStatus("current")
_JnxJVAECNRouterIPv4_Type = InetAddressIPv4
_JnxJVAECNRouterIPv4_Object = MibTableColumn
jnxJVAECNRouterIPv4 = _JnxJVAECNRouterIPv4_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 1, 1, 6),
    _JnxJVAECNRouterIPv4_Type()
)
jnxJVAECNRouterIPv4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNRouterIPv4.setStatus("current")
_JnxJVAECNRouterIPv6_Type = InetAddressIPv6
_JnxJVAECNRouterIPv6_Object = MibTableColumn
jnxJVAECNRouterIPv6 = _JnxJVAECNRouterIPv6_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 1, 1, 7),
    _JnxJVAECNRouterIPv6_Type()
)
jnxJVAECNRouterIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNRouterIPv6.setStatus("current")
_JnxJVAECNMgmtIPv4_Type = InetAddressIPv4
_JnxJVAECNMgmtIPv4_Object = MibTableColumn
jnxJVAECNMgmtIPv4 = _JnxJVAECNMgmtIPv4_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 1, 1, 8),
    _JnxJVAECNMgmtIPv4_Type()
)
jnxJVAECNMgmtIPv4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNMgmtIPv4.setStatus("current")
_JnxJVAECNMgmtIPv6_Type = InetAddressIPv6
_JnxJVAECNMgmtIPv6_Object = MibTableColumn
jnxJVAECNMgmtIPv6 = _JnxJVAECNMgmtIPv6_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 1, 1, 9),
    _JnxJVAECNMgmtIPv6_Type()
)
jnxJVAECNMgmtIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNMgmtIPv6.setStatus("current")


class _JnxJVAECNSWVersion_Type(DisplayString):
    """Custom type jnxJVAECNSWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_JnxJVAECNSWVersion_Type.__name__ = "DisplayString"
_JnxJVAECNSWVersion_Object = MibTableColumn
jnxJVAECNSWVersion = _JnxJVAECNSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 1, 1, 10),
    _JnxJVAECNSWVersion_Type()
)
jnxJVAECNSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNSWVersion.setStatus("current")
_JnxJVAEVMTable_Object = MibTable
jnxJVAEVMTable = _JnxJVAEVMTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    jnxJVAEVMTable.setStatus("current")
_JnxJVAEVMEntry_Object = MibTableRow
jnxJVAEVMEntry = _JnxJVAEVMEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 2, 1)
)
jnxJVAEVMEntry.setIndexNames(
    (0, "JUNIPER-JVAE-INFRA-MIB", "jnxJVAEVMId"),
)
if mibBuilder.loadTexts:
    jnxJVAEVMEntry.setStatus("current")


class _JnxJVAEVMId_Type(OctetString):
    """Custom type jnxJVAEVMId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_JnxJVAEVMId_Type.__name__ = "OctetString"
_JnxJVAEVMId_Object = MibTableColumn
jnxJVAEVMId = _JnxJVAEVMId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 2, 1, 1),
    _JnxJVAEVMId_Type()
)
jnxJVAEVMId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJVAEVMId.setStatus("current")


class _JnxJVAEVMName_Type(DisplayString):
    """Custom type jnxJVAEVMName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 60),
    )


_JnxJVAEVMName_Type.__name__ = "DisplayString"
_JnxJVAEVMName_Object = MibTableColumn
jnxJVAEVMName = _JnxJVAEVMName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 2, 1, 2),
    _JnxJVAEVMName_Type()
)
jnxJVAEVMName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAEVMName.setStatus("current")


class _JnxJVAEVMCCName_Type(DisplayString):
    """Custom type jnxJVAEVMCCName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 60),
    )


_JnxJVAEVMCCName_Type.__name__ = "DisplayString"
_JnxJVAEVMCCName_Object = MibTableColumn
jnxJVAEVMCCName = _JnxJVAEVMCCName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 2, 1, 3),
    _JnxJVAEVMCCName_Type()
)
jnxJVAEVMCCName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAEVMCCName.setStatus("current")


class _JnxJVAEVMCNName_Type(DisplayString):
    """Custom type jnxJVAEVMCNName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 60),
    )


_JnxJVAEVMCNName_Type.__name__ = "DisplayString"
_JnxJVAEVMCNName_Object = MibTableColumn
jnxJVAEVMCNName = _JnxJVAEVMCNName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 2, 1, 4),
    _JnxJVAEVMCNName_Type()
)
jnxJVAEVMCNName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAEVMCNName.setStatus("current")


class _JnxJVAEVMCNId_Type(DisplayString):
    """Custom type jnxJVAEVMCNId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JnxJVAEVMCNId_Type.__name__ = "DisplayString"
_JnxJVAEVMCNId_Object = MibTableColumn
jnxJVAEVMCNId = _JnxJVAEVMCNId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 2, 1, 5),
    _JnxJVAEVMCNId_Type()
)
jnxJVAEVMCNId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAEVMCNId.setStatus("current")


class _JnxJVAEVMUuid_Type(OctetString):
    """Custom type jnxJVAEVMUuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 60),
    )


_JnxJVAEVMUuid_Type.__name__ = "OctetString"
_JnxJVAEVMUuid_Object = MibTableColumn
jnxJVAEVMUuid = _JnxJVAEVMUuid_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 2, 1, 6),
    _JnxJVAEVMUuid_Type()
)
jnxJVAEVMUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAEVMUuid.setStatus("current")


class _JnxJVAEVMPkg_Type(DisplayString):
    """Custom type jnxJVAEVMPkg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_JnxJVAEVMPkg_Type.__name__ = "DisplayString"
_JnxJVAEVMPkg_Object = MibTableColumn
jnxJVAEVMPkg = _JnxJVAEVMPkg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 2, 1, 7),
    _JnxJVAEVMPkg_Type()
)
jnxJVAEVMPkg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAEVMPkg.setStatus("current")


class _JnxJVAEVMStatus_Type(Integer32):
    """Custom type jnxJVAEVMStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("offline", 0),
          ("online", 1))
    )


_JnxJVAEVMStatus_Type.__name__ = "Integer32"
_JnxJVAEVMStatus_Object = MibTableColumn
jnxJVAEVMStatus = _JnxJVAEVMStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 2, 1, 8),
    _JnxJVAEVMStatus_Type()
)
jnxJVAEVMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAEVMStatus.setStatus("current")

# Managed Objects groups


# Notification objects

jnxJVAECNStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 0, 1)
)
jnxJVAECNStateChange.setObjects(
      *(("JUNIPER-JVAE-INFRA-MIB", "jnxJVAECNId"),
        ("JUNIPER-JVAE-INFRA-MIB", "jnxJVAECNName"),
        ("JUNIPER-JVAE-INFRA-MIB", "jnxJVAECCName"),
        ("JUNIPER-JVAE-INFRA-MIB", "jnxJVAECNState"),
        ("JUNIPER-JVAE-INFRA-MIB", "jnxJVAECNLastStateChange"))
)
if mibBuilder.loadTexts:
    jnxJVAECNStateChange.setStatus(
        "current"
    )

jnxJVAEVMStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 0, 2)
)
jnxJVAEVMStateChange.setObjects(
      *(("JUNIPER-JVAE-INFRA-MIB", "jnxJVAEVMId"),
        ("JUNIPER-JVAE-INFRA-MIB", "jnxJVAEVMName"),
        ("JUNIPER-JVAE-INFRA-MIB", "jnxJVAEVMCNId"),
        ("JUNIPER-JVAE-INFRA-MIB", "jnxJVAEVMUuid"),
        ("JUNIPER-JVAE-INFRA-MIB", "jnxJVAEVMStatus"))
)
if mibBuilder.loadTexts:
    jnxJVAEVMStateChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-JVAE-INFRA-MIB",
    **{"jnxJVAEInfraMIB": jnxJVAEInfraMIB,
       "jnxJVAEInfraNotifications": jnxJVAEInfraNotifications,
       "jnxJVAECNStateChange": jnxJVAECNStateChange,
       "jnxJVAEVMStateChange": jnxJVAEVMStateChange,
       "jnxJVAEInfraObjects": jnxJVAEInfraObjects,
       "jnxJVAEInfraTables": jnxJVAEInfraTables,
       "jnxJVAECNTable": jnxJVAECNTable,
       "jnxJVAECNEntry": jnxJVAECNEntry,
       "jnxJVAECNId": jnxJVAECNId,
       "jnxJVAECNName": jnxJVAECNName,
       "jnxJVAECCName": jnxJVAECCName,
       "jnxJVAECNState": jnxJVAECNState,
       "jnxJVAECNLastStateChange": jnxJVAECNLastStateChange,
       "jnxJVAECNRouterIPv4": jnxJVAECNRouterIPv4,
       "jnxJVAECNRouterIPv6": jnxJVAECNRouterIPv6,
       "jnxJVAECNMgmtIPv4": jnxJVAECNMgmtIPv4,
       "jnxJVAECNMgmtIPv6": jnxJVAECNMgmtIPv6,
       "jnxJVAECNSWVersion": jnxJVAECNSWVersion,
       "jnxJVAEVMTable": jnxJVAEVMTable,
       "jnxJVAEVMEntry": jnxJVAEVMEntry,
       "jnxJVAEVMId": jnxJVAEVMId,
       "jnxJVAEVMName": jnxJVAEVMName,
       "jnxJVAEVMCCName": jnxJVAEVMCCName,
       "jnxJVAEVMCNName": jnxJVAEVMCNName,
       "jnxJVAEVMCNId": jnxJVAEVMCNId,
       "jnxJVAEVMUuid": jnxJVAEVMUuid,
       "jnxJVAEVMPkg": jnxJVAEVMPkg,
       "jnxJVAEVMStatus": jnxJVAEVMStatus}
)
