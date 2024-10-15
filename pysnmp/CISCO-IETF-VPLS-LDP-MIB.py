# SNMP MIB module (CISCO-IETF-VPLS-LDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IETF-VPLS-LDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:06 2024
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

(cvplsConfigIndex,
 cvplsPwBindIndex) = mibBuilder.importSymbols(
    "CISCO-IETF-VPLS-GENERIC-MIB",
    "cvplsConfigIndex",
    "cvplsPwBindIndex")

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(VPNId,) = mibBuilder.importSymbols(
    "VPN-TC-STD-MIB",
    "VPNId")


# MODULE-IDENTITY

cvplsLdpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 141)
)
cvplsLdpMIB.setRevisions(
        ("2007-11-22 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CvplsLdpObjects_ObjectIdentity = ObjectIdentity
cvplsLdpObjects = _CvplsLdpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 141, 1)
)
_CvplsLdpConfigTable_Object = MibTable
cvplsLdpConfigTable = _CvplsLdpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 141, 1, 1)
)
if mibBuilder.loadTexts:
    cvplsLdpConfigTable.setStatus("current")
_CvplsLdpConfigEntry_Object = MibTableRow
cvplsLdpConfigEntry = _CvplsLdpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 141, 1, 1, 1)
)
cvplsLdpConfigEntry.setIndexNames(
    (0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex"),
)
if mibBuilder.loadTexts:
    cvplsLdpConfigEntry.setStatus("current")


class _CvplsLdpConfigMacAddrWithdraw_Type(TruthValue):
    """Custom type cvplsLdpConfigMacAddrWithdraw based on TruthValue"""


_CvplsLdpConfigMacAddrWithdraw_Object = MibTableColumn
cvplsLdpConfigMacAddrWithdraw = _CvplsLdpConfigMacAddrWithdraw_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 141, 1, 1, 1, 1),
    _CvplsLdpConfigMacAddrWithdraw_Type()
)
cvplsLdpConfigMacAddrWithdraw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvplsLdpConfigMacAddrWithdraw.setStatus("current")
_CvplsLdpPwBindTable_Object = MibTable
cvplsLdpPwBindTable = _CvplsLdpPwBindTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 141, 1, 2)
)
if mibBuilder.loadTexts:
    cvplsLdpPwBindTable.setStatus("current")
_CvplsLdpPwBindEntry_Object = MibTableRow
cvplsLdpPwBindEntry = _CvplsLdpPwBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 141, 1, 2, 1)
)
cvplsLdpPwBindEntry.setIndexNames(
    (0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex"),
    (0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsPwBindIndex"),
)
if mibBuilder.loadTexts:
    cvplsLdpPwBindEntry.setStatus("current")


class _CvplsLdpPwBindMacAddressLimit_Type(Unsigned32):
    """Custom type cvplsLdpPwBindMacAddressLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CvplsLdpPwBindMacAddressLimit_Type.__name__ = "Unsigned32"
_CvplsLdpPwBindMacAddressLimit_Object = MibTableColumn
cvplsLdpPwBindMacAddressLimit = _CvplsLdpPwBindMacAddressLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 141, 1, 2, 1, 1),
    _CvplsLdpPwBindMacAddressLimit_Type()
)
cvplsLdpPwBindMacAddressLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvplsLdpPwBindMacAddressLimit.setStatus("current")
_CvplsLdpConformance_ObjectIdentity = ObjectIdentity
cvplsLdpConformance = _CvplsLdpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 141, 2)
)
_CvplsLdpCompliances_ObjectIdentity = ObjectIdentity
cvplsLdpCompliances = _CvplsLdpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 141, 2, 1)
)
_CvplsLdpGroups_ObjectIdentity = ObjectIdentity
cvplsLdpGroups = _CvplsLdpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 141, 2, 2)
)

# Managed Objects groups

cvplsLdpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 141, 2, 2, 1)
)
cvplsLdpGroup.setObjects(
      *(("CISCO-IETF-VPLS-LDP-MIB", "cvplsLdpConfigMacAddrWithdraw"),
        ("CISCO-IETF-VPLS-LDP-MIB", "cvplsLdpPwBindMacAddressLimit"))
)
if mibBuilder.loadTexts:
    cvplsLdpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cvplsLdpModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 141, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cvplsLdpModuleFullCompliance.setStatus(
        "current"
    )

cvplsLdpModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 141, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cvplsLdpModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IETF-VPLS-LDP-MIB",
    **{"cvplsLdpMIB": cvplsLdpMIB,
       "cvplsLdpObjects": cvplsLdpObjects,
       "cvplsLdpConfigTable": cvplsLdpConfigTable,
       "cvplsLdpConfigEntry": cvplsLdpConfigEntry,
       "cvplsLdpConfigMacAddrWithdraw": cvplsLdpConfigMacAddrWithdraw,
       "cvplsLdpPwBindTable": cvplsLdpPwBindTable,
       "cvplsLdpPwBindEntry": cvplsLdpPwBindEntry,
       "cvplsLdpPwBindMacAddressLimit": cvplsLdpPwBindMacAddressLimit,
       "cvplsLdpConformance": cvplsLdpConformance,
       "cvplsLdpCompliances": cvplsLdpCompliances,
       "cvplsLdpModuleFullCompliance": cvplsLdpModuleFullCompliance,
       "cvplsLdpModuleReadOnlyCompliance": cvplsLdpModuleReadOnlyCompliance,
       "cvplsLdpGroups": cvplsLdpGroups,
       "cvplsLdpGroup": cvplsLdpGroup}
)
