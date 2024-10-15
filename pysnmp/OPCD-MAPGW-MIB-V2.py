# SNMP MIB module (OPCD-MAPGW-MIB-V2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OPCD-MAPGW-MIB-V2
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:15 2024
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

_Ocmapgw_ObjectIdentity = ObjectIdentity
ocmapgw = _Ocmapgw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30374, 8)
)
_Ocmapgw_traps_ObjectIdentity = ObjectIdentity
ocmapgw_traps = _Ocmapgw_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30374, 8, 1)
)
_Definitions_ObjectIdentity = ObjectIdentity
definitions = _Definitions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30374, 8, 1, 0)
)
_Vars_ObjectIdentity = ObjectIdentity
vars = _Vars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30374, 8, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 30374, 8, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 30374, 8, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 30374, 8, 1, 1, 3),
    _Mcr_Text_Type()
)
mcr_Text.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mcr_Text.setStatus("current")

# Managed Objects groups


# Notification objects

ocmapgw_sccp_cogestion = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 8, 1, 0, 2)
)
ocmapgw_sccp_cogestion.setObjects(
      *(("OPCD-MAPGW-MIB-V2", "mcr_Host"),
        ("OPCD-MAPGW-MIB-V2", "mcr_Severity"),
        ("OPCD-MAPGW-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocmapgw_sccp_cogestion.setStatus(
        "current"
    )

ocmapgw_sccp_cogestion_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 8, 1, 0, 3)
)
ocmapgw_sccp_cogestion_Canceled.setObjects(
      *(("OPCD-MAPGW-MIB-V2", "mcr_Host"),
        ("OPCD-MAPGW-MIB-V2", "mcr_Severity"),
        ("OPCD-MAPGW-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocmapgw_sccp_cogestion_Canceled.setStatus(
        "current"
    )

ocmapgw_ssn_oss = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 8, 1, 0, 4)
)
ocmapgw_ssn_oss.setObjects(
      *(("OPCD-MAPGW-MIB-V2", "mcr_Host"),
        ("OPCD-MAPGW-MIB-V2", "mcr_Severity"),
        ("OPCD-MAPGW-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocmapgw_ssn_oss.setStatus(
        "current"
    )

ocmapgw_ssn_oss_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 8, 1, 0, 5)
)
ocmapgw_ssn_oss_Canceled.setObjects(
      *(("OPCD-MAPGW-MIB-V2", "mcr_Host"),
        ("OPCD-MAPGW-MIB-V2", "mcr_Severity"),
        ("OPCD-MAPGW-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocmapgw_ssn_oss_Canceled.setStatus(
        "current"
    )

ocmapgw_pc_inaccessible = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 8, 1, 0, 6)
)
ocmapgw_pc_inaccessible.setObjects(
      *(("OPCD-MAPGW-MIB-V2", "mcr_Host"),
        ("OPCD-MAPGW-MIB-V2", "mcr_Severity"),
        ("OPCD-MAPGW-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocmapgw_pc_inaccessible.setStatus(
        "current"
    )

ocmapgw_pc_inaccessible_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 8, 1, 0, 7)
)
ocmapgw_pc_inaccessible_Canceled.setObjects(
      *(("OPCD-MAPGW-MIB-V2", "mcr_Host"),
        ("OPCD-MAPGW-MIB-V2", "mcr_Severity"),
        ("OPCD-MAPGW-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocmapgw_pc_inaccessible_Canceled.setStatus(
        "current"
    )

ocmapgw_cong_level1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 8, 1, 0, 8)
)
ocmapgw_cong_level1.setObjects(
      *(("OPCD-MAPGW-MIB-V2", "mcr_Host"),
        ("OPCD-MAPGW-MIB-V2", "mcr_Severity"),
        ("OPCD-MAPGW-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocmapgw_cong_level1.setStatus(
        "current"
    )

ocmapgw_cong_level1_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 8, 1, 0, 9)
)
ocmapgw_cong_level1_Canceled.setObjects(
      *(("OPCD-MAPGW-MIB-V2", "mcr_Host"),
        ("OPCD-MAPGW-MIB-V2", "mcr_Severity"),
        ("OPCD-MAPGW-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocmapgw_cong_level1_Canceled.setStatus(
        "current"
    )

ocmapgw_cong_level2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 8, 1, 0, 10)
)
ocmapgw_cong_level2.setObjects(
      *(("OPCD-MAPGW-MIB-V2", "mcr_Host"),
        ("OPCD-MAPGW-MIB-V2", "mcr_Severity"),
        ("OPCD-MAPGW-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocmapgw_cong_level2.setStatus(
        "current"
    )

ocmapgw_cong_level2_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 8, 1, 0, 11)
)
ocmapgw_cong_level2_Canceled.setObjects(
      *(("OPCD-MAPGW-MIB-V2", "mcr_Host"),
        ("OPCD-MAPGW-MIB-V2", "mcr_Severity"),
        ("OPCD-MAPGW-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocmapgw_cong_level2_Canceled.setStatus(
        "current"
    )

ocmapgw_cong_level3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 8, 1, 0, 12)
)
ocmapgw_cong_level3.setObjects(
      *(("OPCD-MAPGW-MIB-V2", "mcr_Host"),
        ("OPCD-MAPGW-MIB-V2", "mcr_Severity"),
        ("OPCD-MAPGW-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocmapgw_cong_level3.setStatus(
        "current"
    )

ocmapgw_cong_level3_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 8, 1, 0, 13)
)
ocmapgw_cong_level3_Canceled.setObjects(
      *(("OPCD-MAPGW-MIB-V2", "mcr_Host"),
        ("OPCD-MAPGW-MIB-V2", "mcr_Severity"),
        ("OPCD-MAPGW-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocmapgw_cong_level3_Canceled.setStatus(
        "current"
    )

ocmapgw_crashed = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 8, 1, 0, 14)
)
ocmapgw_crashed.setObjects(
      *(("OPCD-MAPGW-MIB-V2", "mcr_Host"),
        ("OPCD-MAPGW-MIB-V2", "mcr_Severity"),
        ("OPCD-MAPGW-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocmapgw_crashed.setStatus(
        "current"
    )

ocmapgw_crashed_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 8, 1, 0, 15)
)
ocmapgw_crashed_Canceled.setObjects(
      *(("OPCD-MAPGW-MIB-V2", "mcr_Host"),
        ("OPCD-MAPGW-MIB-V2", "mcr_Severity"),
        ("OPCD-MAPGW-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocmapgw_crashed_Canceled.setStatus(
        "current"
    )

ocmapgw_notraffic = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 8, 1, 0, 16)
)
ocmapgw_notraffic.setObjects(
      *(("OPCD-MAPGW-MIB-V2", "mcr_Host"),
        ("OPCD-MAPGW-MIB-V2", "mcr_Severity"),
        ("OPCD-MAPGW-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocmapgw_notraffic.setStatus(
        "current"
    )

ocmapgw_notraffic_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 8, 1, 0, 17)
)
ocmapgw_notraffic_Canceled.setObjects(
      *(("OPCD-MAPGW-MIB-V2", "mcr_Host"),
        ("OPCD-MAPGW-MIB-V2", "mcr_Severity"),
        ("OPCD-MAPGW-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocmapgw_notraffic_Canceled.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPCD-MAPGW-MIB-V2",
    **{"ocmapgw": ocmapgw,
       "ocmapgw-traps": ocmapgw_traps,
       "definitions": definitions,
       "ocmapgw-sccp-cogestion": ocmapgw_sccp_cogestion,
       "ocmapgw-sccp-cogestion-Canceled": ocmapgw_sccp_cogestion_Canceled,
       "ocmapgw-ssn-oss": ocmapgw_ssn_oss,
       "ocmapgw-ssn-oss-Canceled": ocmapgw_ssn_oss_Canceled,
       "ocmapgw-pc-inaccessible": ocmapgw_pc_inaccessible,
       "ocmapgw-pc-inaccessible-Canceled": ocmapgw_pc_inaccessible_Canceled,
       "ocmapgw-cong-level1": ocmapgw_cong_level1,
       "ocmapgw-cong-level1-Canceled": ocmapgw_cong_level1_Canceled,
       "ocmapgw-cong-level2": ocmapgw_cong_level2,
       "ocmapgw-cong-level2-Canceled": ocmapgw_cong_level2_Canceled,
       "ocmapgw-cong-level3": ocmapgw_cong_level3,
       "ocmapgw-cong-level3-Canceled": ocmapgw_cong_level3_Canceled,
       "ocmapgw-crashed": ocmapgw_crashed,
       "ocmapgw-crashed-Canceled": ocmapgw_crashed_Canceled,
       "ocmapgw-notraffic": ocmapgw_notraffic,
       "ocmapgw-notraffic-Canceled": ocmapgw_notraffic_Canceled,
       "vars": vars,
       "mcr-Host": mcr_Host,
       "mcr-Severity": mcr_Severity,
       "mcr-Text": mcr_Text}
)
