# SNMP MIB module (OPCD-CCXML-MIB-V2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OPCD-CCXML-MIB-V2
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:13 2024
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

_Occcxml_ObjectIdentity = ObjectIdentity
occcxml = _Occcxml_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30374, 12)
)
_Occcxml_traps_ObjectIdentity = ObjectIdentity
occcxml_traps = _Occcxml_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30374, 12, 1)
)
_Definitions_ObjectIdentity = ObjectIdentity
definitions = _Definitions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30374, 12, 1, 0)
)
_Vars_ObjectIdentity = ObjectIdentity
vars = _Vars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30374, 12, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 30374, 12, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 30374, 12, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 30374, 12, 1, 1, 3),
    _Mcr_Text_Type()
)
mcr_Text.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mcr_Text.setStatus("current")

# Managed Objects groups


# Notification objects

occcxml_Crash = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 12, 1, 0, 2)
)
occcxml_Crash.setObjects(
      *(("OPCD-CCXML-MIB-V2", "mcr_Host"),
        ("OPCD-CCXML-MIB-V2", "mcr_Severity"),
        ("OPCD-CCXML-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occcxml_Crash.setStatus(
        "current"
    )

occcxml_Crash_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 12, 1, 0, 3)
)
occcxml_Crash_Canceled.setObjects(
      *(("OPCD-CCXML-MIB-V2", "mcr_Host"),
        ("OPCD-CCXML-MIB-V2", "mcr_Severity"),
        ("OPCD-CCXML-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occcxml_Crash_Canceled.setStatus(
        "current"
    )

occcxml_ipc_ISUPGW_ConnProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 12, 1, 0, 4)
)
occcxml_ipc_ISUPGW_ConnProblem.setObjects(
      *(("OPCD-CCXML-MIB-V2", "mcr_Host"),
        ("OPCD-CCXML-MIB-V2", "mcr_Severity"),
        ("OPCD-CCXML-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occcxml_ipc_ISUPGW_ConnProblem.setStatus(
        "current"
    )

occcxml_ipc_ISUPGW_ConnProblem_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 12, 1, 0, 5)
)
occcxml_ipc_ISUPGW_ConnProblem_Canceled.setObjects(
      *(("OPCD-CCXML-MIB-V2", "mcr_Host"),
        ("OPCD-CCXML-MIB-V2", "mcr_Severity"),
        ("OPCD-CCXML-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occcxml_ipc_ISUPGW_ConnProblem_Canceled.setStatus(
        "current"
    )

occcxml_ipc_MEDIAGW_ConnProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 12, 1, 0, 6)
)
occcxml_ipc_MEDIAGW_ConnProblem.setObjects(
      *(("OPCD-CCXML-MIB-V2", "mcr_Host"),
        ("OPCD-CCXML-MIB-V2", "mcr_Severity"),
        ("OPCD-CCXML-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occcxml_ipc_MEDIAGW_ConnProblem.setStatus(
        "current"
    )

occcxml_ipc_MEDIAGW_ConnProblem_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 12, 1, 0, 7)
)
occcxml_ipc_MEDIAGW_ConnProblem_Canceled.setObjects(
      *(("OPCD-CCXML-MIB-V2", "mcr_Host"),
        ("OPCD-CCXML-MIB-V2", "mcr_Severity"),
        ("OPCD-CCXML-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occcxml_ipc_MEDIAGW_ConnProblem_Canceled.setStatus(
        "current"
    )

occcxml_ipc_VXML_ConnProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 12, 1, 0, 8)
)
occcxml_ipc_VXML_ConnProblem.setObjects(
      *(("OPCD-CCXML-MIB-V2", "mcr_Host"),
        ("OPCD-CCXML-MIB-V2", "mcr_Severity"),
        ("OPCD-CCXML-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occcxml_ipc_VXML_ConnProblem.setStatus(
        "current"
    )

occcxml_ipc_VXML_ConnProblem_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 12, 1, 0, 9)
)
occcxml_ipc_VXML_ConnProblem_Canceled.setObjects(
      *(("OPCD-CCXML-MIB-V2", "mcr_Host"),
        ("OPCD-CCXML-MIB-V2", "mcr_Severity"),
        ("OPCD-CCXML-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occcxml_ipc_VXML_ConnProblem_Canceled.setStatus(
        "current"
    )

occcxml_ipc_USSDBR_ConnProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 12, 1, 0, 10)
)
occcxml_ipc_USSDBR_ConnProblem.setObjects(
      *(("OPCD-CCXML-MIB-V2", "mcr_Host"),
        ("OPCD-CCXML-MIB-V2", "mcr_Severity"),
        ("OPCD-CCXML-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occcxml_ipc_USSDBR_ConnProblem.setStatus(
        "current"
    )

occcxml_ipc_USSDBR_ConnProblem_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 12, 1, 0, 11)
)
occcxml_ipc_USSDBR_ConnProblem_Canceled.setObjects(
      *(("OPCD-CCXML-MIB-V2", "mcr_Host"),
        ("OPCD-CCXML-MIB-V2", "mcr_Severity"),
        ("OPCD-CCXML-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occcxml_ipc_USSDBR_ConnProblem_Canceled.setStatus(
        "current"
    )

occcxml_Loading_plugin_Failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 12, 1, 0, 12)
)
occcxml_Loading_plugin_Failed.setObjects(
      *(("OPCD-CCXML-MIB-V2", "mcr_Host"),
        ("OPCD-CCXML-MIB-V2", "mcr_Severity"),
        ("OPCD-CCXML-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occcxml_Loading_plugin_Failed.setStatus(
        "current"
    )

occcxml_Loading_plugin_Failed_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 12, 1, 0, 13)
)
occcxml_Loading_plugin_Failed_Canceled.setObjects(
      *(("OPCD-CCXML-MIB-V2", "mcr_Host"),
        ("OPCD-CCXML-MIB-V2", "mcr_Severity"),
        ("OPCD-CCXML-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occcxml_Loading_plugin_Failed_Canceled.setStatus(
        "current"
    )

occcxml_CDRSubsys_Problem = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 12, 1, 0, 14)
)
occcxml_CDRSubsys_Problem.setObjects(
      *(("OPCD-CCXML-MIB-V2", "mcr_Host"),
        ("OPCD-CCXML-MIB-V2", "mcr_Severity"),
        ("OPCD-CCXML-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occcxml_CDRSubsys_Problem.setStatus(
        "current"
    )

occcxml_CDRSubsys_Problem_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 12, 1, 0, 15)
)
occcxml_CDRSubsys_Problem_Canceled.setObjects(
      *(("OPCD-CCXML-MIB-V2", "mcr_Host"),
        ("OPCD-CCXML-MIB-V2", "mcr_Severity"),
        ("OPCD-CCXML-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    occcxml_CDRSubsys_Problem_Canceled.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPCD-CCXML-MIB-V2",
    **{"occcxml": occcxml,
       "occcxml-traps": occcxml_traps,
       "definitions": definitions,
       "occcxml-Crash": occcxml_Crash,
       "occcxml-Crash-Canceled": occcxml_Crash_Canceled,
       "occcxml-ipc-ISUPGW-ConnProblem": occcxml_ipc_ISUPGW_ConnProblem,
       "occcxml-ipc-ISUPGW-ConnProblem-Canceled": occcxml_ipc_ISUPGW_ConnProblem_Canceled,
       "occcxml-ipc-MEDIAGW-ConnProblem": occcxml_ipc_MEDIAGW_ConnProblem,
       "occcxml-ipc-MEDIAGW-ConnProblem-Canceled": occcxml_ipc_MEDIAGW_ConnProblem_Canceled,
       "occcxml-ipc-VXML-ConnProblem": occcxml_ipc_VXML_ConnProblem,
       "occcxml-ipc-VXML-ConnProblem-Canceled": occcxml_ipc_VXML_ConnProblem_Canceled,
       "occcxml-ipc-USSDBR-ConnProblem": occcxml_ipc_USSDBR_ConnProblem,
       "occcxml-ipc-USSDBR-ConnProblem-Canceled": occcxml_ipc_USSDBR_ConnProblem_Canceled,
       "occcxml-Loading-plugin-Failed": occcxml_Loading_plugin_Failed,
       "occcxml-Loading-plugin-Failed-Canceled": occcxml_Loading_plugin_Failed_Canceled,
       "occcxml-CDRSubsys-Problem": occcxml_CDRSubsys_Problem,
       "occcxml-CDRSubsys-Problem-Canceled": occcxml_CDRSubsys_Problem_Canceled,
       "vars": vars,
       "mcr-Host": mcr_Host,
       "mcr-Severity": mcr_Severity,
       "mcr-Text": mcr_Text}
)
