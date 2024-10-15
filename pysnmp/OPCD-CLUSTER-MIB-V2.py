# SNMP MIB module (OPCD-CLUSTER-MIB-V2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OPCD-CLUSTER-MIB-V2
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:14 2024
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

(opencode_systems,) = mibBuilder.importSymbols(
    "OPCD-SUPPORT-MIB-V2",
    "opencode-systems")

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

_Occluster_ObjectIdentity = ObjectIdentity
occluster = _Occluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30374, 40)
)
_Occluster_traps_ObjectIdentity = ObjectIdentity
occluster_traps = _Occluster_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30374, 40, 1)
)
_Definitions_ObjectIdentity = ObjectIdentity
definitions = _Definitions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30374, 40, 1, 0)
)
_Vars_ObjectIdentity = ObjectIdentity
vars = _Vars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30374, 40, 1, 1)
)


class _Mcr_Host_Type(DisplayString):
    """Custom type mcr_Host based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Mcr_Host_Type.__name__ = "DisplayString"
_Mcr_Host_Object = MibScalar
mcr_Host = _Mcr_Host_Object(
    (1, 3, 6, 1, 4, 1, 30374, 40, 1, 1, 1),
    _Mcr_Host_Type()
)
mcr_Host.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mcr_Host.setStatus("current")


class _Mcr_Severity_Type(Integer32):
    """Custom type mcr_Severity based on Integer32"""
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("normal", 4),
          ("warning", 5))
    )


_Mcr_Severity_Type.__name__ = "Integer32"
_Mcr_Severity_Object = MibScalar
mcr_Severity = _Mcr_Severity_Object(
    (1, 3, 6, 1, 4, 1, 30374, 40, 1, 1, 2),
    _Mcr_Severity_Type()
)
mcr_Severity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mcr_Severity.setStatus("mandatory")


class _Mcr_Text_Type(DisplayString):
    """Custom type mcr_Text based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Mcr_Text_Type.__name__ = "DisplayString"
_Mcr_Text_Object = MibScalar
mcr_Text = _Mcr_Text_Object(
    (1, 3, 6, 1, 4, 1, 30374, 40, 1, 1, 3),
    _Mcr_Text_Type()
)
mcr_Text.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mcr_Text.setStatus("current")

# Managed Objects groups


# Notification objects

occluster_became_supervisor = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 40, 1, 0, 2)
)
occluster_became_supervisor.setObjects(
      *(("OPCD-CLUSTER-MIB-V2", "mcr_Host"),
        ("OPCD-CLUSTER-MIB-V2", "mcr_Severity"),
        ("OPCD-CLUSTER-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occluster_became_supervisor.setStatus(
        "current"
    )

occluster_became_supervisor_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 40, 1, 0, 3)
)
occluster_became_supervisor_Canceled.setObjects(
      *(("OPCD-CLUSTER-MIB-V2", "mcr_Host"),
        ("OPCD-CLUSTER-MIB-V2", "mcr_Severity"),
        ("OPCD-CLUSTER-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occluster_became_supervisor_Canceled.setStatus(
        "current"
    )

occluster_node_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 40, 1, 0, 4)
)
occluster_node_down.setObjects(
      *(("OPCD-CLUSTER-MIB-V2", "mcr_Host"),
        ("OPCD-CLUSTER-MIB-V2", "mcr_Severity"),
        ("OPCD-CLUSTER-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occluster_node_down.setStatus(
        "current"
    )

occluster_node_down_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 40, 1, 0, 5)
)
occluster_node_down_Canceled.setObjects(
      *(("OPCD-CLUSTER-MIB-V2", "mcr_Host"),
        ("OPCD-CLUSTER-MIB-V2", "mcr_Severity"),
        ("OPCD-CLUSTER-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occluster_node_down_Canceled.setStatus(
        "current"
    )

occluster_resourceagent_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 40, 1, 0, 6)
)
occluster_resourceagent_down.setObjects(
      *(("OPCD-CLUSTER-MIB-V2", "mcr_Host"),
        ("OPCD-CLUSTER-MIB-V2", "mcr_Severity"),
        ("OPCD-CLUSTER-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occluster_resourceagent_down.setStatus(
        "current"
    )

occluster_resourceagent_down_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 40, 1, 0, 7)
)
occluster_resourceagent_down_Canceled.setObjects(
      *(("OPCD-CLUSTER-MIB-V2", "mcr_Host"),
        ("OPCD-CLUSTER-MIB-V2", "mcr_Severity"),
        ("OPCD-CLUSTER-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occluster_resourceagent_down_Canceled.setStatus(
        "current"
    )

occluster_resource_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 40, 1, 0, 8)
)
occluster_resource_down.setObjects(
      *(("OPCD-CLUSTER-MIB-V2", "mcr_Host"),
        ("OPCD-CLUSTER-MIB-V2", "mcr_Severity"),
        ("OPCD-CLUSTER-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occluster_resource_down.setStatus(
        "current"
    )

occluster_resource_down_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 40, 1, 0, 9)
)
occluster_resource_down_Canceled.setObjects(
      *(("OPCD-CLUSTER-MIB-V2", "mcr_Host"),
        ("OPCD-CLUSTER-MIB-V2", "mcr_Severity"),
        ("OPCD-CLUSTER-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occluster_resource_down_Canceled.setStatus(
        "current"
    )

occluster_service_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 40, 1, 0, 10)
)
occluster_service_down.setObjects(
      *(("OPCD-CLUSTER-MIB-V2", "mcr_Host"),
        ("OPCD-CLUSTER-MIB-V2", "mcr_Severity"),
        ("OPCD-CLUSTER-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occluster_service_down.setStatus(
        "current"
    )

occluster_service_down_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 40, 1, 0, 11)
)
occluster_service_down_Canceled.setObjects(
      *(("OPCD-CLUSTER-MIB-V2", "mcr_Host"),
        ("OPCD-CLUSTER-MIB-V2", "mcr_Severity"),
        ("OPCD-CLUSTER-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occluster_service_down_Canceled.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPCD-CLUSTER-MIB-V2",
    **{"occluster": occluster,
       "occluster-traps": occluster_traps,
       "definitions": definitions,
       "occluster-became-supervisor": occluster_became_supervisor,
       "occluster-became-supervisor-Canceled": occluster_became_supervisor_Canceled,
       "occluster-node-down": occluster_node_down,
       "occluster-node-down-Canceled": occluster_node_down_Canceled,
       "occluster-resourceagent-down": occluster_resourceagent_down,
       "occluster-resourceagent-down-Canceled": occluster_resourceagent_down_Canceled,
       "occluster-resource-down": occluster_resource_down,
       "occluster-resource-down-Canceled": occluster_resource_down_Canceled,
       "occluster-service-down": occluster_service_down,
       "occluster-service-down-Canceled": occluster_service_down_Canceled,
       "vars": vars,
       "mcr-Host": mcr_Host,
       "mcr-Severity": mcr_Severity,
       "mcr-Text": mcr_Text}
)
