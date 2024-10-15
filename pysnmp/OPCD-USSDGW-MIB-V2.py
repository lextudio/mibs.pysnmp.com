# SNMP MIB module (OPCD-USSDGW-MIB-V2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OPCD-USSDGW-MIB-V2
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:17 2024
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

_Ocussdgw_ObjectIdentity = ObjectIdentity
ocussdgw = _Ocussdgw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30374, 2)
)
_Ocussdgw_traps_ObjectIdentity = ObjectIdentity
ocussdgw_traps = _Ocussdgw_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30374, 2, 1)
)
_Definitions_ObjectIdentity = ObjectIdentity
definitions = _Definitions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30374, 2, 1, 0)
)
_Vars_ObjectIdentity = ObjectIdentity
vars = _Vars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30374, 2, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 30374, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 30374, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 30374, 2, 1, 1, 3),
    _Mcr_Text_Type()
)
mcr_Text.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mcr_Text.setStatus("current")

# Managed Objects groups


# Notification objects

ocussdgw_Crash = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 2, 1, 0, 2)
)
ocussdgw_Crash.setObjects(
      *(("OPCD-USSDGW-MIB-V2", "mcr_Host"),
        ("OPCD-USSDGW-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDGW-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdgw_Crash.setStatus(
        "current"
    )

ocussdgw_Crash_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 2, 1, 0, 3)
)
ocussdgw_Crash_Canceled.setObjects(
      *(("OPCD-USSDGW-MIB-V2", "mcr_Host"),
        ("OPCD-USSDGW-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDGW-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdgw_Crash_Canceled.setStatus(
        "current"
    )

ocussdgw_Stp1_Inaccessible = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 2, 1, 0, 4)
)
ocussdgw_Stp1_Inaccessible.setObjects(
      *(("OPCD-USSDGW-MIB-V2", "mcr_Host"),
        ("OPCD-USSDGW-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDGW-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdgw_Stp1_Inaccessible.setStatus(
        "current"
    )

ocussdgw_Stp1_Inaccessible_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 2, 1, 0, 5)
)
ocussdgw_Stp1_Inaccessible_Canceled.setObjects(
      *(("OPCD-USSDGW-MIB-V2", "mcr_Host"),
        ("OPCD-USSDGW-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDGW-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdgw_Stp1_Inaccessible_Canceled.setStatus(
        "current"
    )

ocussdgw_Stp2_Inaccessible = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 2, 1, 0, 6)
)
ocussdgw_Stp2_Inaccessible.setObjects(
      *(("OPCD-USSDGW-MIB-V2", "mcr_Host"),
        ("OPCD-USSDGW-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDGW-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdgw_Stp2_Inaccessible.setStatus(
        "current"
    )

ocussdgw_Stp2_Inaccessible_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 2, 1, 0, 7)
)
ocussdgw_Stp2_Inaccessible_Canceled.setObjects(
      *(("OPCD-USSDGW-MIB-V2", "mcr_Host"),
        ("OPCD-USSDGW-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDGW-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdgw_Stp2_Inaccessible_Canceled.setStatus(
        "current"
    )

ocussdgw_Stp1_Congestion = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 2, 1, 0, 8)
)
ocussdgw_Stp1_Congestion.setObjects(
      *(("OPCD-USSDGW-MIB-V2", "mcr_Host"),
        ("OPCD-USSDGW-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDGW-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdgw_Stp1_Congestion.setStatus(
        "current"
    )

ocussdgw_Stp1_Congestion_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 2, 1, 0, 9)
)
ocussdgw_Stp1_Congestion_Canceled.setObjects(
      *(("OPCD-USSDGW-MIB-V2", "mcr_Host"),
        ("OPCD-USSDGW-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDGW-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdgw_Stp1_Congestion_Canceled.setStatus(
        "current"
    )

ocussdgw_Stp2_Congestion = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 2, 1, 0, 10)
)
ocussdgw_Stp2_Congestion.setObjects(
      *(("OPCD-USSDGW-MIB-V2", "mcr_Host"),
        ("OPCD-USSDGW-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDGW-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdgw_Stp2_Congestion.setStatus(
        "current"
    )

ocussdgw_Stp2_Congestion_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 2, 1, 0, 11)
)
ocussdgw_Stp2_Congestion_Canceled.setObjects(
      *(("OPCD-USSDGW-MIB-V2", "mcr_Host"),
        ("OPCD-USSDGW-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDGW-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdgw_Stp2_Congestion_Canceled.setStatus(
        "current"
    )

ocussdgw_CongestionUssd = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 2, 1, 0, 12)
)
ocussdgw_CongestionUssd.setObjects(
      *(("OPCD-USSDGW-MIB-V2", "mcr_Host"),
        ("OPCD-USSDGW-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDGW-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdgw_CongestionUssd.setStatus(
        "current"
    )

ocussdgw_CongestionUssd_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 2, 1, 0, 13)
)
ocussdgw_CongestionUssd_Canceled.setObjects(
      *(("OPCD-USSDGW-MIB-V2", "mcr_Host"),
        ("OPCD-USSDGW-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDGW-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdgw_CongestionUssd_Canceled.setStatus(
        "current"
    )

ocussdgw_SmppConnDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 2, 1, 0, 14)
)
ocussdgw_SmppConnDown.setObjects(
      *(("OPCD-USSDGW-MIB-V2", "mcr_Host"),
        ("OPCD-USSDGW-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDGW-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdgw_SmppConnDown.setStatus(
        "current"
    )

ocussdgw_SmppConnDown_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 2, 1, 0, 15)
)
ocussdgw_SmppConnDown_Canceled.setObjects(
      *(("OPCD-USSDGW-MIB-V2", "mcr_Host"),
        ("OPCD-USSDGW-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDGW-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdgw_SmppConnDown_Canceled.setStatus(
        "current"
    )

ocussdgw_NoSS7trafic = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 2, 1, 0, 16)
)
ocussdgw_NoSS7trafic.setObjects(
      *(("OPCD-USSDGW-MIB-V2", "mcr_Host"),
        ("OPCD-USSDGW-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDGW-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdgw_NoSS7trafic.setStatus(
        "current"
    )

ocussdgw_NoSS7trafic_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 2, 1, 0, 17)
)
ocussdgw_NoSS7trafic_Canceled.setObjects(
      *(("OPCD-USSDGW-MIB-V2", "mcr_Host"),
        ("OPCD-USSDGW-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDGW-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdgw_NoSS7trafic_Canceled.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPCD-USSDGW-MIB-V2",
    **{"ocussdgw": ocussdgw,
       "ocussdgw-traps": ocussdgw_traps,
       "definitions": definitions,
       "ocussdgw-Crash": ocussdgw_Crash,
       "ocussdgw-Crash-Canceled": ocussdgw_Crash_Canceled,
       "ocussdgw-Stp1-Inaccessible": ocussdgw_Stp1_Inaccessible,
       "ocussdgw-Stp1-Inaccessible-Canceled": ocussdgw_Stp1_Inaccessible_Canceled,
       "ocussdgw-Stp2-Inaccessible": ocussdgw_Stp2_Inaccessible,
       "ocussdgw-Stp2-Inaccessible-Canceled": ocussdgw_Stp2_Inaccessible_Canceled,
       "ocussdgw-Stp1-Congestion": ocussdgw_Stp1_Congestion,
       "ocussdgw-Stp1-Congestion-Canceled": ocussdgw_Stp1_Congestion_Canceled,
       "ocussdgw-Stp2-Congestion": ocussdgw_Stp2_Congestion,
       "ocussdgw-Stp2-Congestion-Canceled": ocussdgw_Stp2_Congestion_Canceled,
       "ocussdgw-CongestionUssd": ocussdgw_CongestionUssd,
       "ocussdgw-CongestionUssd-Canceled": ocussdgw_CongestionUssd_Canceled,
       "ocussdgw-SmppConnDown": ocussdgw_SmppConnDown,
       "ocussdgw-SmppConnDown-Canceled": ocussdgw_SmppConnDown_Canceled,
       "ocussdgw-NoSS7trafic": ocussdgw_NoSS7trafic,
       "ocussdgw-NoSS7trafic-Canceled": ocussdgw_NoSS7trafic_Canceled,
       "vars": vars,
       "mcr-Host": mcr_Host,
       "mcr-Severity": mcr_Severity,
       "mcr-Text": mcr_Text}
)
