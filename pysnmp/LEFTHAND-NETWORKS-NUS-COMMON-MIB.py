# SNMP MIB module (LEFTHAND-NETWORKS-NUS-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LEFTHAND-NETWORKS-NUS-COMMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:41 2024
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

(lhnModules,
 lhnNusCommonMIB) = mibBuilder.importSymbols(
    "LEFTHAND-NETWORKS-GLOBAL-REG",
    "lhnModules",
    "lhnNusCommonMIB")

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

leftHandNetworksNusCommonModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 1, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LhnNusCommonConfs_ObjectIdentity = ObjectIdentity
lhnNusCommonConfs = _LhnNusCommonConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 1)
)
_LhnNusCommonGroups_ObjectIdentity = ObjectIdentity
lhnNusCommonGroups = _LhnNusCommonGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 1, 1)
)
_LhnNusCommonCompl_ObjectIdentity = ObjectIdentity
lhnNusCommonCompl = _LhnNusCommonCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 1, 2)
)
_LhnNusCommonObjs_ObjectIdentity = ObjectIdentity
lhnNusCommonObjs = _LhnNusCommonObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2)
)
_LhnNusCommonInfo_ObjectIdentity = ObjectIdentity
lhnNusCommonInfo = _LhnNusCommonInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1)
)
_LhnNusCommonNetwork_ObjectIdentity = ObjectIdentity
lhnNusCommonNetwork = _LhnNusCommonNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2)
)
_LhnNusCommonDNS_ObjectIdentity = ObjectIdentity
lhnNusCommonDNS = _LhnNusCommonDNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3)
)
_LhnNusCommonStorage_ObjectIdentity = ObjectIdentity
lhnNusCommonStorage = _LhnNusCommonStorage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4)
)
_LhnNusCommonNTP_ObjectIdentity = ObjectIdentity
lhnNusCommonNTP = _LhnNusCommonNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 5)
)
_LhnNusCommonNIS_ObjectIdentity = ObjectIdentity
lhnNusCommonNIS = _LhnNusCommonNIS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 6)
)
_LhnNusCommonAEBS_ObjectIdentity = ObjectIdentity
lhnNusCommonAEBS = _LhnNusCommonAEBS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 7)
)
_LhnNusCommonShares_ObjectIdentity = ObjectIdentity
lhnNusCommonShares = _LhnNusCommonShares_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 8)
)
_LhnNusCommonNTDomain_ObjectIdentity = ObjectIdentity
lhnNusCommonNTDomain = _LhnNusCommonNTDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 9)
)
_LhnNusCommonSysOptions_ObjectIdentity = ObjectIdentity
lhnNusCommonSysOptions = _LhnNusCommonSysOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 10)
)
_LhnNusCommonSecurity_ObjectIdentity = ObjectIdentity
lhnNusCommonSecurity = _LhnNusCommonSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11)
)
_LhnNusCommonClustering_ObjectIdentity = ObjectIdentity
lhnNusCommonClustering = _LhnNusCommonClustering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12)
)
_LhnNusCommonNotification_ObjectIdentity = ObjectIdentity
lhnNusCommonNotification = _LhnNusCommonNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 13)
)
_LhnNusCommonStatus_ObjectIdentity = ObjectIdentity
lhnNusCommonStatus = _LhnNusCommonStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 99)
)
_LhnNusCommonEvents_ObjectIdentity = ObjectIdentity
lhnNusCommonEvents = _LhnNusCommonEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 3)
)

# Managed Objects groups

lhnNusCommonBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 1, 1, 1)
)
lhnNusCommonBasicGroup.setObjects(
      *(("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonInfo"),
        ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonNetwork"),
        ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonDNS"),
        ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonStorage"),
        ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonNTP"),
        ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonNIS"),
        ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonAEBS"),
        ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonShares"),
        ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonNTDomain"),
        ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonSysOptions"),
        ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonSecurity"),
        ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonClustering"),
        ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonNotification"),
        ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonStatus"))
)
if mibBuilder.loadTexts:
    lhnNusCommonBasicGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lhnNusCommonComplianceV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lhnNusCommonComplianceV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LEFTHAND-NETWORKS-NUS-COMMON-MIB",
    **{"leftHandNetworksNusCommonModule": leftHandNetworksNusCommonModule,
       "lhnNusCommonConfs": lhnNusCommonConfs,
       "lhnNusCommonGroups": lhnNusCommonGroups,
       "lhnNusCommonBasicGroup": lhnNusCommonBasicGroup,
       "lhnNusCommonCompl": lhnNusCommonCompl,
       "lhnNusCommonComplianceV1": lhnNusCommonComplianceV1,
       "lhnNusCommonObjs": lhnNusCommonObjs,
       "lhnNusCommonInfo": lhnNusCommonInfo,
       "lhnNusCommonNetwork": lhnNusCommonNetwork,
       "lhnNusCommonDNS": lhnNusCommonDNS,
       "lhnNusCommonStorage": lhnNusCommonStorage,
       "lhnNusCommonNTP": lhnNusCommonNTP,
       "lhnNusCommonNIS": lhnNusCommonNIS,
       "lhnNusCommonAEBS": lhnNusCommonAEBS,
       "lhnNusCommonShares": lhnNusCommonShares,
       "lhnNusCommonNTDomain": lhnNusCommonNTDomain,
       "lhnNusCommonSysOptions": lhnNusCommonSysOptions,
       "lhnNusCommonSecurity": lhnNusCommonSecurity,
       "lhnNusCommonClustering": lhnNusCommonClustering,
       "lhnNusCommonNotification": lhnNusCommonNotification,
       "lhnNusCommonStatus": lhnNusCommonStatus,
       "lhnNusCommonEvents": lhnNusCommonEvents}
)
