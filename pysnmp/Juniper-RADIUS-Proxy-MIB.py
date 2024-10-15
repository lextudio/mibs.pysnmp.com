# SNMP MIB module (Juniper-RADIUS-Proxy-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-RADIUS-Proxy-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:13 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

juniRadiusProxyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 73)
)
juniRadiusProxyMIB.setRevisions(
        ("2004-01-23 19:32",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniRadiusProxyObjects_ObjectIdentity = ObjectIdentity
juniRadiusProxyObjects = _JuniRadiusProxyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 1)
)
_JuniRadiusGeneralProxy_ObjectIdentity = ObjectIdentity
juniRadiusGeneralProxy = _JuniRadiusGeneralProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 1, 1)
)


class _JuniRadiusProxyUdpChecksum_Type(TruthValue):
    """Custom type juniRadiusProxyUdpChecksum based on TruthValue"""


_JuniRadiusProxyUdpChecksum_Object = MibScalar
juniRadiusProxyUdpChecksum = _JuniRadiusProxyUdpChecksum_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 1, 1, 1),
    _JuniRadiusProxyUdpChecksum_Type()
)
juniRadiusProxyUdpChecksum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusProxyUdpChecksum.setStatus("current")
_JuniRadiusAuthProxyCfg_ObjectIdentity = ObjectIdentity
juniRadiusAuthProxyCfg = _JuniRadiusAuthProxyCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 1, 2)
)


class _JuniRadiusAuthProxyCfgPortNumber_Type(Integer32):
    """Custom type juniRadiusAuthProxyCfgPortNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniRadiusAuthProxyCfgPortNumber_Type.__name__ = "Integer32"
_JuniRadiusAuthProxyCfgPortNumber_Object = MibScalar
juniRadiusAuthProxyCfgPortNumber = _JuniRadiusAuthProxyCfgPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 1, 2, 1),
    _JuniRadiusAuthProxyCfgPortNumber_Type()
)
juniRadiusAuthProxyCfgPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusAuthProxyCfgPortNumber.setStatus("current")
_JuniRadiusAuthProxyCfgClientTable_Object = MibTable
juniRadiusAuthProxyCfgClientTable = _JuniRadiusAuthProxyCfgClientTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 1, 2, 2)
)
if mibBuilder.loadTexts:
    juniRadiusAuthProxyCfgClientTable.setStatus("current")
_JuniRadiusAuthProxyCfgClientEntry_Object = MibTableRow
juniRadiusAuthProxyCfgClientEntry = _JuniRadiusAuthProxyCfgClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 1, 2, 2, 1)
)
juniRadiusAuthProxyCfgClientEntry.setIndexNames(
    (0, "Juniper-RADIUS-Proxy-MIB", "juniRadiusAuthProxyCfgClientAddress"),
    (0, "Juniper-RADIUS-Proxy-MIB", "juniRadiusAuthProxyCfgClientMask"),
)
if mibBuilder.loadTexts:
    juniRadiusAuthProxyCfgClientEntry.setStatus("current")
_JuniRadiusAuthProxyCfgClientAddress_Type = IpAddress
_JuniRadiusAuthProxyCfgClientAddress_Object = MibTableColumn
juniRadiusAuthProxyCfgClientAddress = _JuniRadiusAuthProxyCfgClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 1, 2, 2, 1, 1),
    _JuniRadiusAuthProxyCfgClientAddress_Type()
)
juniRadiusAuthProxyCfgClientAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniRadiusAuthProxyCfgClientAddress.setStatus("current")
_JuniRadiusAuthProxyCfgClientMask_Type = IpAddress
_JuniRadiusAuthProxyCfgClientMask_Object = MibTableColumn
juniRadiusAuthProxyCfgClientMask = _JuniRadiusAuthProxyCfgClientMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 1, 2, 2, 1, 2),
    _JuniRadiusAuthProxyCfgClientMask_Type()
)
juniRadiusAuthProxyCfgClientMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniRadiusAuthProxyCfgClientMask.setStatus("current")
_JuniRadiusAuthProxyCfgRowStatus_Type = RowStatus
_JuniRadiusAuthProxyCfgRowStatus_Object = MibTableColumn
juniRadiusAuthProxyCfgRowStatus = _JuniRadiusAuthProxyCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 1, 2, 2, 1, 3),
    _JuniRadiusAuthProxyCfgRowStatus_Type()
)
juniRadiusAuthProxyCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRadiusAuthProxyCfgRowStatus.setStatus("current")


class _JuniRadiusAuthProxyCfgClientKey_Type(DisplayString):
    """Custom type juniRadiusAuthProxyCfgClientKey based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniRadiusAuthProxyCfgClientKey_Type.__name__ = "DisplayString"
_JuniRadiusAuthProxyCfgClientKey_Object = MibTableColumn
juniRadiusAuthProxyCfgClientKey = _JuniRadiusAuthProxyCfgClientKey_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 1, 2, 2, 1, 4),
    _JuniRadiusAuthProxyCfgClientKey_Type()
)
juniRadiusAuthProxyCfgClientKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRadiusAuthProxyCfgClientKey.setStatus("current")
_JuniRadiusAcctProxyCfg_ObjectIdentity = ObjectIdentity
juniRadiusAcctProxyCfg = _JuniRadiusAcctProxyCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 1, 3)
)


class _JuniRadiusAcctProxyCfgPortNumber_Type(Integer32):
    """Custom type juniRadiusAcctProxyCfgPortNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniRadiusAcctProxyCfgPortNumber_Type.__name__ = "Integer32"
_JuniRadiusAcctProxyCfgPortNumber_Object = MibScalar
juniRadiusAcctProxyCfgPortNumber = _JuniRadiusAcctProxyCfgPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 1, 3, 1),
    _JuniRadiusAcctProxyCfgPortNumber_Type()
)
juniRadiusAcctProxyCfgPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusAcctProxyCfgPortNumber.setStatus("current")
_JuniRadiusAcctProxyCfgClientTable_Object = MibTable
juniRadiusAcctProxyCfgClientTable = _JuniRadiusAcctProxyCfgClientTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 1, 3, 2)
)
if mibBuilder.loadTexts:
    juniRadiusAcctProxyCfgClientTable.setStatus("current")
_JuniRadiusAcctProxyCfgClientEntry_Object = MibTableRow
juniRadiusAcctProxyCfgClientEntry = _JuniRadiusAcctProxyCfgClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 1, 3, 2, 1)
)
juniRadiusAcctProxyCfgClientEntry.setIndexNames(
    (0, "Juniper-RADIUS-Proxy-MIB", "juniRadiusAcctProxyCfgClientAddress"),
    (0, "Juniper-RADIUS-Proxy-MIB", "juniRadiusAcctProxyCfgClientMask"),
)
if mibBuilder.loadTexts:
    juniRadiusAcctProxyCfgClientEntry.setStatus("current")
_JuniRadiusAcctProxyCfgClientAddress_Type = IpAddress
_JuniRadiusAcctProxyCfgClientAddress_Object = MibTableColumn
juniRadiusAcctProxyCfgClientAddress = _JuniRadiusAcctProxyCfgClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 1, 3, 2, 1, 1),
    _JuniRadiusAcctProxyCfgClientAddress_Type()
)
juniRadiusAcctProxyCfgClientAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniRadiusAcctProxyCfgClientAddress.setStatus("current")
_JuniRadiusAcctProxyCfgClientMask_Type = IpAddress
_JuniRadiusAcctProxyCfgClientMask_Object = MibTableColumn
juniRadiusAcctProxyCfgClientMask = _JuniRadiusAcctProxyCfgClientMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 1, 3, 2, 1, 2),
    _JuniRadiusAcctProxyCfgClientMask_Type()
)
juniRadiusAcctProxyCfgClientMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniRadiusAcctProxyCfgClientMask.setStatus("current")
_JuniRadiusAcctProxyCfgRowStatus_Type = RowStatus
_JuniRadiusAcctProxyCfgRowStatus_Object = MibTableColumn
juniRadiusAcctProxyCfgRowStatus = _JuniRadiusAcctProxyCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 1, 3, 2, 1, 3),
    _JuniRadiusAcctProxyCfgRowStatus_Type()
)
juniRadiusAcctProxyCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRadiusAcctProxyCfgRowStatus.setStatus("current")


class _JuniRadiusAcctProxyCfgClientKey_Type(DisplayString):
    """Custom type juniRadiusAcctProxyCfgClientKey based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniRadiusAcctProxyCfgClientKey_Type.__name__ = "DisplayString"
_JuniRadiusAcctProxyCfgClientKey_Object = MibTableColumn
juniRadiusAcctProxyCfgClientKey = _JuniRadiusAcctProxyCfgClientKey_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 1, 3, 2, 1, 4),
    _JuniRadiusAcctProxyCfgClientKey_Type()
)
juniRadiusAcctProxyCfgClientKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRadiusAcctProxyCfgClientKey.setStatus("current")
_JuniRadiusProxyMIBConformance_ObjectIdentity = ObjectIdentity
juniRadiusProxyMIBConformance = _JuniRadiusProxyMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 2)
)
_JuniRadiusProxyMIBCompliances_ObjectIdentity = ObjectIdentity
juniRadiusProxyMIBCompliances = _JuniRadiusProxyMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 2, 1)
)
_JuniRadiusProxyMIBGroups_ObjectIdentity = ObjectIdentity
juniRadiusProxyMIBGroups = _JuniRadiusProxyMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 2, 2)
)

# Managed Objects groups

juniRadiusBasicProxyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 2, 2, 1)
)
juniRadiusBasicProxyGroup.setObjects(
    ("Juniper-RADIUS-Proxy-MIB", "juniRadiusProxyUdpChecksum")
)
if mibBuilder.loadTexts:
    juniRadiusBasicProxyGroup.setStatus("current")

juniRadiusAuthProxyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 2, 2, 2)
)
juniRadiusAuthProxyGroup.setObjects(
      *(("Juniper-RADIUS-Proxy-MIB", "juniRadiusAuthProxyCfgPortNumber"),
        ("Juniper-RADIUS-Proxy-MIB", "juniRadiusAuthProxyCfgRowStatus"),
        ("Juniper-RADIUS-Proxy-MIB", "juniRadiusAuthProxyCfgClientKey"))
)
if mibBuilder.loadTexts:
    juniRadiusAuthProxyGroup.setStatus("current")

juniRadiusAcctProxyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 2, 2, 3)
)
juniRadiusAcctProxyGroup.setObjects(
      *(("Juniper-RADIUS-Proxy-MIB", "juniRadiusAcctProxyCfgPortNumber"),
        ("Juniper-RADIUS-Proxy-MIB", "juniRadiusAcctProxyCfgRowStatus"),
        ("Juniper-RADIUS-Proxy-MIB", "juniRadiusAcctProxyCfgClientKey"))
)
if mibBuilder.loadTexts:
    juniRadiusAcctProxyGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniRadiusProxyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 73, 2, 1, 1)
)
if mibBuilder.loadTexts:
    juniRadiusProxyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-RADIUS-Proxy-MIB",
    **{"juniRadiusProxyMIB": juniRadiusProxyMIB,
       "juniRadiusProxyObjects": juniRadiusProxyObjects,
       "juniRadiusGeneralProxy": juniRadiusGeneralProxy,
       "juniRadiusProxyUdpChecksum": juniRadiusProxyUdpChecksum,
       "juniRadiusAuthProxyCfg": juniRadiusAuthProxyCfg,
       "juniRadiusAuthProxyCfgPortNumber": juniRadiusAuthProxyCfgPortNumber,
       "juniRadiusAuthProxyCfgClientTable": juniRadiusAuthProxyCfgClientTable,
       "juniRadiusAuthProxyCfgClientEntry": juniRadiusAuthProxyCfgClientEntry,
       "juniRadiusAuthProxyCfgClientAddress": juniRadiusAuthProxyCfgClientAddress,
       "juniRadiusAuthProxyCfgClientMask": juniRadiusAuthProxyCfgClientMask,
       "juniRadiusAuthProxyCfgRowStatus": juniRadiusAuthProxyCfgRowStatus,
       "juniRadiusAuthProxyCfgClientKey": juniRadiusAuthProxyCfgClientKey,
       "juniRadiusAcctProxyCfg": juniRadiusAcctProxyCfg,
       "juniRadiusAcctProxyCfgPortNumber": juniRadiusAcctProxyCfgPortNumber,
       "juniRadiusAcctProxyCfgClientTable": juniRadiusAcctProxyCfgClientTable,
       "juniRadiusAcctProxyCfgClientEntry": juniRadiusAcctProxyCfgClientEntry,
       "juniRadiusAcctProxyCfgClientAddress": juniRadiusAcctProxyCfgClientAddress,
       "juniRadiusAcctProxyCfgClientMask": juniRadiusAcctProxyCfgClientMask,
       "juniRadiusAcctProxyCfgRowStatus": juniRadiusAcctProxyCfgRowStatus,
       "juniRadiusAcctProxyCfgClientKey": juniRadiusAcctProxyCfgClientKey,
       "juniRadiusProxyMIBConformance": juniRadiusProxyMIBConformance,
       "juniRadiusProxyMIBCompliances": juniRadiusProxyMIBCompliances,
       "juniRadiusProxyCompliance": juniRadiusProxyCompliance,
       "juniRadiusProxyMIBGroups": juniRadiusProxyMIBGroups,
       "juniRadiusBasicProxyGroup": juniRadiusBasicProxyGroup,
       "juniRadiusAuthProxyGroup": juniRadiusAuthProxyGroup,
       "juniRadiusAcctProxyGroup": juniRadiusAcctProxyGroup}
)
