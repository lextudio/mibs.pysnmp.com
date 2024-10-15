# SNMP MIB module (DPS-MIB-NGD-V10) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DPS-MIB-NGD-V10
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:22 2024
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

(dpsRTU,) = mibBuilder.importSymbols(
    "DPS-MIB-V38",
    "dpsRTU")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

dpsRTUp8001Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8001)
)
dpsRTUp8001Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8001Set.setStatus(
        ""
    )

dpsRTUp8002Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8002)
)
dpsRTUp8002Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8002Set.setStatus(
        ""
    )

dpsRTUp8003Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8003)
)
dpsRTUp8003Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8003Set.setStatus(
        ""
    )

dpsRTUp8004Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8004)
)
dpsRTUp8004Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8004Set.setStatus(
        ""
    )

dpsRTUp8005Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8005)
)
dpsRTUp8005Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8005Set.setStatus(
        ""
    )

dpsRTUp8006Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8006)
)
dpsRTUp8006Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8006Set.setStatus(
        ""
    )

dpsRTUp8007Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8007)
)
dpsRTUp8007Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8007Set.setStatus(
        ""
    )

dpsRTUp8008Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8008)
)
dpsRTUp8008Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8008Set.setStatus(
        ""
    )

dpsRTUp8009Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8009)
)
dpsRTUp8009Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8009Set.setStatus(
        ""
    )

dpsRTUp8010Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8010)
)
dpsRTUp8010Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8010Set.setStatus(
        ""
    )

dpsRTUp8011Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8011)
)
dpsRTUp8011Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8011Set.setStatus(
        ""
    )

dpsRTUp8012Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8012)
)
dpsRTUp8012Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8012Set.setStatus(
        ""
    )

dpsRTUp8013Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8013)
)
dpsRTUp8013Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8013Set.setStatus(
        ""
    )

dpsRTUp8014Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8014)
)
dpsRTUp8014Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8014Set.setStatus(
        ""
    )

dpsRTUp8015Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8015)
)
dpsRTUp8015Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8015Set.setStatus(
        ""
    )

dpsRTUp8016Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8016)
)
dpsRTUp8016Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8016Set.setStatus(
        ""
    )

dpsRTUp8017Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8017)
)
dpsRTUp8017Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8017Set.setStatus(
        ""
    )

dpsRTUp8018Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8018)
)
dpsRTUp8018Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8018Set.setStatus(
        ""
    )

dpsRTUp8019Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8019)
)
dpsRTUp8019Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8019Set.setStatus(
        ""
    )

dpsRTUp8020Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8020)
)
dpsRTUp8020Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8020Set.setStatus(
        ""
    )

dpsRTUp8021Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8021)
)
dpsRTUp8021Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8021Set.setStatus(
        ""
    )

dpsRTUp8022Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8022)
)
dpsRTUp8022Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8022Set.setStatus(
        ""
    )

dpsRTUp8023Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8023)
)
dpsRTUp8023Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8023Set.setStatus(
        ""
    )

dpsRTUp8024Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8024)
)
dpsRTUp8024Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8024Set.setStatus(
        ""
    )

dpsRTUp8025Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8025)
)
dpsRTUp8025Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8025Set.setStatus(
        ""
    )

dpsRTUp8026Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8026)
)
dpsRTUp8026Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8026Set.setStatus(
        ""
    )

dpsRTUp8027Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8027)
)
dpsRTUp8027Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8027Set.setStatus(
        ""
    )

dpsRTUp8028Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8028)
)
dpsRTUp8028Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8028Set.setStatus(
        ""
    )

dpsRTUp8029Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8029)
)
dpsRTUp8029Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8029Set.setStatus(
        ""
    )

dpsRTUp8030Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8030)
)
dpsRTUp8030Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8030Set.setStatus(
        ""
    )

dpsRTUp8031Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8031)
)
dpsRTUp8031Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8031Set.setStatus(
        ""
    )

dpsRTUp8032Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8032)
)
dpsRTUp8032Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8032Set.setStatus(
        ""
    )

dpsRTUp8033Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8033)
)
dpsRTUp8033Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8033Set.setStatus(
        ""
    )

dpsRTUp8034Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8034)
)
dpsRTUp8034Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8034Set.setStatus(
        ""
    )

dpsRTUp8035Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8035)
)
dpsRTUp8035Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8035Set.setStatus(
        ""
    )

dpsRTUp8036Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8036)
)
dpsRTUp8036Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8036Set.setStatus(
        ""
    )

dpsRTUp8037Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8037)
)
dpsRTUp8037Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8037Set.setStatus(
        ""
    )

dpsRTUp8038Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8038)
)
dpsRTUp8038Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8038Set.setStatus(
        ""
    )

dpsRTUp8039Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8039)
)
dpsRTUp8039Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8039Set.setStatus(
        ""
    )

dpsRTUp8040Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8040)
)
dpsRTUp8040Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8040Set.setStatus(
        ""
    )

dpsRTUp8041Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8041)
)
dpsRTUp8041Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8041Set.setStatus(
        ""
    )

dpsRTUp8042Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8042)
)
dpsRTUp8042Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8042Set.setStatus(
        ""
    )

dpsRTUp8043Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8043)
)
dpsRTUp8043Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8043Set.setStatus(
        ""
    )

dpsRTUp8044Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8044)
)
dpsRTUp8044Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8044Set.setStatus(
        ""
    )

dpsRTUp8045Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8045)
)
dpsRTUp8045Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8045Set.setStatus(
        ""
    )

dpsRTUp8046Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8046)
)
dpsRTUp8046Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8046Set.setStatus(
        ""
    )

dpsRTUp8047Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8047)
)
dpsRTUp8047Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8047Set.setStatus(
        ""
    )

dpsRTUp8048Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8048)
)
dpsRTUp8048Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8048Set.setStatus(
        ""
    )

dpsRTUp8049Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8049)
)
dpsRTUp8049Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8049Set.setStatus(
        ""
    )

dpsRTUp8050Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8050)
)
dpsRTUp8050Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8050Set.setStatus(
        ""
    )

dpsRTUp8051Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8051)
)
dpsRTUp8051Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8051Set.setStatus(
        ""
    )

dpsRTUp8052Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8052)
)
dpsRTUp8052Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8052Set.setStatus(
        ""
    )

dpsRTUp8053Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8053)
)
dpsRTUp8053Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8053Set.setStatus(
        ""
    )

dpsRTUp8054Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8054)
)
dpsRTUp8054Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8054Set.setStatus(
        ""
    )

dpsRTUp8055Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8055)
)
dpsRTUp8055Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8055Set.setStatus(
        ""
    )

dpsRTUp8056Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8056)
)
dpsRTUp8056Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8056Set.setStatus(
        ""
    )

dpsRTUp8057Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8057)
)
dpsRTUp8057Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8057Set.setStatus(
        ""
    )

dpsRTUp8058Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8058)
)
dpsRTUp8058Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8058Set.setStatus(
        ""
    )

dpsRTUp8059Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8059)
)
dpsRTUp8059Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8059Set.setStatus(
        ""
    )

dpsRTUp8060Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8060)
)
dpsRTUp8060Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8060Set.setStatus(
        ""
    )

dpsRTUp8061Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8061)
)
dpsRTUp8061Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8061Set.setStatus(
        ""
    )

dpsRTUp8062Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8062)
)
dpsRTUp8062Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8062Set.setStatus(
        ""
    )

dpsRTUp8063Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8063)
)
dpsRTUp8063Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8063Set.setStatus(
        ""
    )

dpsRTUp8064Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8064)
)
dpsRTUp8064Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8064Set.setStatus(
        ""
    )

dpsRTUp8065Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8065)
)
dpsRTUp8065Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8065Set.setStatus(
        ""
    )

dpsRTUp8066Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8066)
)
dpsRTUp8066Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8066Set.setStatus(
        ""
    )

dpsRTUp8067Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8067)
)
dpsRTUp8067Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8067Set.setStatus(
        ""
    )

dpsRTUp8068Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8068)
)
dpsRTUp8068Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8068Set.setStatus(
        ""
    )

dpsRTUp8069Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8069)
)
dpsRTUp8069Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8069Set.setStatus(
        ""
    )

dpsRTUp8070Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8070)
)
dpsRTUp8070Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8070Set.setStatus(
        ""
    )

dpsRTUp8071Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8071)
)
dpsRTUp8071Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8071Set.setStatus(
        ""
    )

dpsRTUp8072Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8072)
)
dpsRTUp8072Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8072Set.setStatus(
        ""
    )

dpsRTUp8073Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8073)
)
dpsRTUp8073Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8073Set.setStatus(
        ""
    )

dpsRTUp8074Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8074)
)
dpsRTUp8074Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8074Set.setStatus(
        ""
    )

dpsRTUp8075Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8075)
)
dpsRTUp8075Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8075Set.setStatus(
        ""
    )

dpsRTUp8076Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8076)
)
dpsRTUp8076Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8076Set.setStatus(
        ""
    )

dpsRTUp8077Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8077)
)
dpsRTUp8077Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8077Set.setStatus(
        ""
    )

dpsRTUp8078Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8078)
)
dpsRTUp8078Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8078Set.setStatus(
        ""
    )

dpsRTUp8079Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8079)
)
dpsRTUp8079Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8079Set.setStatus(
        ""
    )

dpsRTUp8080Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8080)
)
dpsRTUp8080Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8080Set.setStatus(
        ""
    )

dpsRTUp8081Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8081)
)
dpsRTUp8081Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8081Set.setStatus(
        ""
    )

dpsRTUp8082Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8082)
)
dpsRTUp8082Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8082Set.setStatus(
        ""
    )

dpsRTUp8083Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8083)
)
dpsRTUp8083Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8083Set.setStatus(
        ""
    )

dpsRTUp8084Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8084)
)
dpsRTUp8084Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8084Set.setStatus(
        ""
    )

dpsRTUp8085Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8085)
)
dpsRTUp8085Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8085Set.setStatus(
        ""
    )

dpsRTUp8086Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8086)
)
dpsRTUp8086Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8086Set.setStatus(
        ""
    )

dpsRTUp8087Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8087)
)
dpsRTUp8087Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8087Set.setStatus(
        ""
    )

dpsRTUp8088Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8088)
)
dpsRTUp8088Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8088Set.setStatus(
        ""
    )

dpsRTUp8089Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8089)
)
dpsRTUp8089Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8089Set.setStatus(
        ""
    )

dpsRTUp8090Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8090)
)
dpsRTUp8090Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8090Set.setStatus(
        ""
    )

dpsRTUp8091Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8091)
)
dpsRTUp8091Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8091Set.setStatus(
        ""
    )

dpsRTUp8092Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8092)
)
dpsRTUp8092Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8092Set.setStatus(
        ""
    )

dpsRTUp8093Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8093)
)
dpsRTUp8093Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8093Set.setStatus(
        ""
    )

dpsRTUp8094Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8094)
)
dpsRTUp8094Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8094Set.setStatus(
        ""
    )

dpsRTUp8095Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8095)
)
dpsRTUp8095Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8095Set.setStatus(
        ""
    )

dpsRTUp8096Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8096)
)
dpsRTUp8096Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8096Set.setStatus(
        ""
    )

dpsRTUp8097Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8097)
)
dpsRTUp8097Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8097Set.setStatus(
        ""
    )

dpsRTUp8098Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8098)
)
dpsRTUp8098Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8098Set.setStatus(
        ""
    )

dpsRTUp8099Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8099)
)
dpsRTUp8099Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8099Set.setStatus(
        ""
    )

dpsRTUp8100Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8100)
)
dpsRTUp8100Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8100Set.setStatus(
        ""
    )

dpsRTUp8101Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8101)
)
dpsRTUp8101Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8101Set.setStatus(
        ""
    )

dpsRTUp8102Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8102)
)
dpsRTUp8102Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8102Set.setStatus(
        ""
    )

dpsRTUp8103Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8103)
)
dpsRTUp8103Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8103Set.setStatus(
        ""
    )

dpsRTUp8104Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8104)
)
dpsRTUp8104Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8104Set.setStatus(
        ""
    )

dpsRTUp8105Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8105)
)
dpsRTUp8105Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8105Set.setStatus(
        ""
    )

dpsRTUp8106Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8106)
)
dpsRTUp8106Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8106Set.setStatus(
        ""
    )

dpsRTUp8107Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8107)
)
dpsRTUp8107Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8107Set.setStatus(
        ""
    )

dpsRTUp8108Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8108)
)
dpsRTUp8108Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8108Set.setStatus(
        ""
    )

dpsRTUp8109Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8109)
)
dpsRTUp8109Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8109Set.setStatus(
        ""
    )

dpsRTUp8110Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8110)
)
dpsRTUp8110Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8110Set.setStatus(
        ""
    )

dpsRTUp8111Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8111)
)
dpsRTUp8111Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8111Set.setStatus(
        ""
    )

dpsRTUp8112Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8112)
)
dpsRTUp8112Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8112Set.setStatus(
        ""
    )

dpsRTUp8113Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8113)
)
dpsRTUp8113Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8113Set.setStatus(
        ""
    )

dpsRTUp8114Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8114)
)
dpsRTUp8114Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8114Set.setStatus(
        ""
    )

dpsRTUp8115Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8115)
)
dpsRTUp8115Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8115Set.setStatus(
        ""
    )

dpsRTUp8116Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8116)
)
dpsRTUp8116Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8116Set.setStatus(
        ""
    )

dpsRTUp8117Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8117)
)
dpsRTUp8117Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8117Set.setStatus(
        ""
    )

dpsRTUp8118Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8118)
)
dpsRTUp8118Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8118Set.setStatus(
        ""
    )

dpsRTUp8119Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8119)
)
dpsRTUp8119Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8119Set.setStatus(
        ""
    )

dpsRTUp8120Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8120)
)
dpsRTUp8120Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8120Set.setStatus(
        ""
    )

dpsRTUp8121Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8121)
)
dpsRTUp8121Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8121Set.setStatus(
        ""
    )

dpsRTUp8122Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8122)
)
dpsRTUp8122Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8122Set.setStatus(
        ""
    )

dpsRTUp8123Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8123)
)
dpsRTUp8123Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8123Set.setStatus(
        ""
    )

dpsRTUp8124Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8124)
)
dpsRTUp8124Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8124Set.setStatus(
        ""
    )

dpsRTUp8125Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8125)
)
dpsRTUp8125Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8125Set.setStatus(
        ""
    )

dpsRTUp8126Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8126)
)
dpsRTUp8126Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8126Set.setStatus(
        ""
    )

dpsRTUp8127Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8127)
)
dpsRTUp8127Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8127Set.setStatus(
        ""
    )

dpsRTUp8128Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8128)
)
dpsRTUp8128Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8128Set.setStatus(
        ""
    )

dpsRTUp8129Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8129)
)
dpsRTUp8129Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8129Set.setStatus(
        ""
    )

dpsRTUp8130Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8130)
)
dpsRTUp8130Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8130Set.setStatus(
        ""
    )

dpsRTUp8131Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8131)
)
dpsRTUp8131Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8131Set.setStatus(
        ""
    )

dpsRTUp8132Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8132)
)
dpsRTUp8132Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8132Set.setStatus(
        ""
    )

dpsRTUp8133Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8133)
)
dpsRTUp8133Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8133Set.setStatus(
        ""
    )

dpsRTUp8134Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8134)
)
dpsRTUp8134Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8134Set.setStatus(
        ""
    )

dpsRTUp8135Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8135)
)
dpsRTUp8135Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8135Set.setStatus(
        ""
    )

dpsRTUp8136Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8136)
)
dpsRTUp8136Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8136Set.setStatus(
        ""
    )

dpsRTUp8137Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8137)
)
dpsRTUp8137Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8137Set.setStatus(
        ""
    )

dpsRTUp8138Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8138)
)
dpsRTUp8138Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8138Set.setStatus(
        ""
    )

dpsRTUp8139Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8139)
)
dpsRTUp8139Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8139Set.setStatus(
        ""
    )

dpsRTUp8140Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8140)
)
dpsRTUp8140Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8140Set.setStatus(
        ""
    )

dpsRTUp8141Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8141)
)
dpsRTUp8141Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8141Set.setStatus(
        ""
    )

dpsRTUp8142Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8142)
)
dpsRTUp8142Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8142Set.setStatus(
        ""
    )

dpsRTUp8143Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8143)
)
dpsRTUp8143Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8143Set.setStatus(
        ""
    )

dpsRTUp8144Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8144)
)
dpsRTUp8144Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8144Set.setStatus(
        ""
    )

dpsRTUp8145Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8145)
)
dpsRTUp8145Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8145Set.setStatus(
        ""
    )

dpsRTUp8146Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8146)
)
dpsRTUp8146Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8146Set.setStatus(
        ""
    )

dpsRTUp8147Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8147)
)
dpsRTUp8147Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8147Set.setStatus(
        ""
    )

dpsRTUp8148Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8148)
)
dpsRTUp8148Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8148Set.setStatus(
        ""
    )

dpsRTUp8149Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8149)
)
dpsRTUp8149Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8149Set.setStatus(
        ""
    )

dpsRTUp8150Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8150)
)
dpsRTUp8150Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8150Set.setStatus(
        ""
    )

dpsRTUp8151Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8151)
)
dpsRTUp8151Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8151Set.setStatus(
        ""
    )

dpsRTUp8152Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8152)
)
dpsRTUp8152Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8152Set.setStatus(
        ""
    )

dpsRTUp8153Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8153)
)
dpsRTUp8153Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8153Set.setStatus(
        ""
    )

dpsRTUp8154Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8154)
)
dpsRTUp8154Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8154Set.setStatus(
        ""
    )

dpsRTUp8155Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8155)
)
dpsRTUp8155Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8155Set.setStatus(
        ""
    )

dpsRTUp8156Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8156)
)
dpsRTUp8156Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8156Set.setStatus(
        ""
    )

dpsRTUp8157Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8157)
)
dpsRTUp8157Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8157Set.setStatus(
        ""
    )

dpsRTUp8158Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8158)
)
dpsRTUp8158Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8158Set.setStatus(
        ""
    )

dpsRTUp8159Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8159)
)
dpsRTUp8159Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8159Set.setStatus(
        ""
    )

dpsRTUp8160Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8160)
)
dpsRTUp8160Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8160Set.setStatus(
        ""
    )

dpsRTUp8161Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8161)
)
dpsRTUp8161Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8161Set.setStatus(
        ""
    )

dpsRTUp8162Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8162)
)
dpsRTUp8162Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8162Set.setStatus(
        ""
    )

dpsRTUp8163Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8163)
)
dpsRTUp8163Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8163Set.setStatus(
        ""
    )

dpsRTUp8164Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8164)
)
dpsRTUp8164Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8164Set.setStatus(
        ""
    )

dpsRTUp8165Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8165)
)
dpsRTUp8165Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8165Set.setStatus(
        ""
    )

dpsRTUp8166Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8166)
)
dpsRTUp8166Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8166Set.setStatus(
        ""
    )

dpsRTUp8167Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8167)
)
dpsRTUp8167Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8167Set.setStatus(
        ""
    )

dpsRTUp8168Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8168)
)
dpsRTUp8168Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8168Set.setStatus(
        ""
    )

dpsRTUp8169Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8169)
)
dpsRTUp8169Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8169Set.setStatus(
        ""
    )

dpsRTUp8170Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8170)
)
dpsRTUp8170Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8170Set.setStatus(
        ""
    )

dpsRTUp8171Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8171)
)
dpsRTUp8171Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8171Set.setStatus(
        ""
    )

dpsRTUp8172Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8172)
)
dpsRTUp8172Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8172Set.setStatus(
        ""
    )

dpsRTUp8173Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8173)
)
dpsRTUp8173Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8173Set.setStatus(
        ""
    )

dpsRTUp8174Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8174)
)
dpsRTUp8174Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8174Set.setStatus(
        ""
    )

dpsRTUp8175Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8175)
)
dpsRTUp8175Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8175Set.setStatus(
        ""
    )

dpsRTUp8176Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8176)
)
dpsRTUp8176Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8176Set.setStatus(
        ""
    )

dpsRTUp8193Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8193)
)
dpsRTUp8193Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8193Set.setStatus(
        ""
    )

dpsRTUp8194Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8194)
)
dpsRTUp8194Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8194Set.setStatus(
        ""
    )

dpsRTUp8195Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8195)
)
dpsRTUp8195Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8195Set.setStatus(
        ""
    )

dpsRTUp8196Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8196)
)
dpsRTUp8196Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8196Set.setStatus(
        ""
    )

dpsRTUp8197Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8197)
)
dpsRTUp8197Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8197Set.setStatus(
        ""
    )

dpsRTUp8198Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8198)
)
dpsRTUp8198Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8198Set.setStatus(
        ""
    )

dpsRTUp8199Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8199)
)
dpsRTUp8199Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8199Set.setStatus(
        ""
    )

dpsRTUp8200Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8200)
)
dpsRTUp8200Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8200Set.setStatus(
        ""
    )

dpsRTUp8201Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8201)
)
dpsRTUp8201Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8201Set.setStatus(
        ""
    )

dpsRTUp8202Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8202)
)
dpsRTUp8202Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8202Set.setStatus(
        ""
    )

dpsRTUp8203Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8203)
)
dpsRTUp8203Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8203Set.setStatus(
        ""
    )

dpsRTUp8204Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8204)
)
dpsRTUp8204Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8204Set.setStatus(
        ""
    )

dpsRTUp8205Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8205)
)
dpsRTUp8205Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8205Set.setStatus(
        ""
    )

dpsRTUp8206Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8206)
)
dpsRTUp8206Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8206Set.setStatus(
        ""
    )

dpsRTUp8207Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8207)
)
dpsRTUp8207Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8207Set.setStatus(
        ""
    )

dpsRTUp8208Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8208)
)
dpsRTUp8208Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8208Set.setStatus(
        ""
    )

dpsRTUp8209Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8209)
)
dpsRTUp8209Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8209Set.setStatus(
        ""
    )

dpsRTUp8210Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8210)
)
dpsRTUp8210Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8210Set.setStatus(
        ""
    )

dpsRTUp8211Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8211)
)
dpsRTUp8211Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8211Set.setStatus(
        ""
    )

dpsRTUp8212Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8212)
)
dpsRTUp8212Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8212Set.setStatus(
        ""
    )

dpsRTUp8213Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8213)
)
dpsRTUp8213Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8213Set.setStatus(
        ""
    )

dpsRTUp8214Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8214)
)
dpsRTUp8214Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8214Set.setStatus(
        ""
    )

dpsRTUp8215Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8215)
)
dpsRTUp8215Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8215Set.setStatus(
        ""
    )

dpsRTUp8216Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8216)
)
dpsRTUp8216Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8216Set.setStatus(
        ""
    )

dpsRTUp8217Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8217)
)
dpsRTUp8217Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8217Set.setStatus(
        ""
    )

dpsRTUp8218Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8218)
)
dpsRTUp8218Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8218Set.setStatus(
        ""
    )

dpsRTUp8219Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8219)
)
dpsRTUp8219Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8219Set.setStatus(
        ""
    )

dpsRTUp8220Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8220)
)
dpsRTUp8220Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8220Set.setStatus(
        ""
    )

dpsRTUp8221Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8221)
)
dpsRTUp8221Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8221Set.setStatus(
        ""
    )

dpsRTUp8222Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8222)
)
dpsRTUp8222Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8222Set.setStatus(
        ""
    )

dpsRTUp8223Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8223)
)
dpsRTUp8223Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8223Set.setStatus(
        ""
    )

dpsRTUp8224Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8224)
)
dpsRTUp8224Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8224Set.setStatus(
        ""
    )

dpsRTUp8225Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8225)
)
dpsRTUp8225Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8225Set.setStatus(
        ""
    )

dpsRTUp8226Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8226)
)
dpsRTUp8226Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8226Set.setStatus(
        ""
    )

dpsRTUp8227Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8227)
)
dpsRTUp8227Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8227Set.setStatus(
        ""
    )

dpsRTUp8228Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8228)
)
dpsRTUp8228Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8228Set.setStatus(
        ""
    )

dpsRTUp8229Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8229)
)
dpsRTUp8229Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8229Set.setStatus(
        ""
    )

dpsRTUp8230Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8230)
)
dpsRTUp8230Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8230Set.setStatus(
        ""
    )

dpsRTUp8231Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8231)
)
dpsRTUp8231Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8231Set.setStatus(
        ""
    )

dpsRTUp8232Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8232)
)
dpsRTUp8232Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8232Set.setStatus(
        ""
    )

dpsRTUp8233Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8233)
)
dpsRTUp8233Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8233Set.setStatus(
        ""
    )

dpsRTUp8234Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8234)
)
dpsRTUp8234Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8234Set.setStatus(
        ""
    )

dpsRTUp8235Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8235)
)
dpsRTUp8235Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8235Set.setStatus(
        ""
    )

dpsRTUp8236Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8236)
)
dpsRTUp8236Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8236Set.setStatus(
        ""
    )

dpsRTUp8237Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8237)
)
dpsRTUp8237Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8237Set.setStatus(
        ""
    )

dpsRTUp8238Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8238)
)
dpsRTUp8238Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8238Set.setStatus(
        ""
    )

dpsRTUp8239Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8239)
)
dpsRTUp8239Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8239Set.setStatus(
        ""
    )

dpsRTUp8240Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8240)
)
dpsRTUp8240Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8240Set.setStatus(
        ""
    )

dpsRTUp8241Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8241)
)
dpsRTUp8241Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8241Set.setStatus(
        ""
    )

dpsRTUp8242Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8242)
)
dpsRTUp8242Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8242Set.setStatus(
        ""
    )

dpsRTUp8243Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8243)
)
dpsRTUp8243Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8243Set.setStatus(
        ""
    )

dpsRTUp8244Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8244)
)
dpsRTUp8244Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8244Set.setStatus(
        ""
    )

dpsRTUp8245Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8245)
)
dpsRTUp8245Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8245Set.setStatus(
        ""
    )

dpsRTUp8246Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8246)
)
dpsRTUp8246Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8246Set.setStatus(
        ""
    )

dpsRTUp8247Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8247)
)
dpsRTUp8247Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8247Set.setStatus(
        ""
    )

dpsRTUp8248Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8248)
)
dpsRTUp8248Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8248Set.setStatus(
        ""
    )

dpsRTUp8249Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8249)
)
dpsRTUp8249Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8249Set.setStatus(
        ""
    )

dpsRTUp8250Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8250)
)
dpsRTUp8250Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8250Set.setStatus(
        ""
    )

dpsRTUp8251Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8251)
)
dpsRTUp8251Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8251Set.setStatus(
        ""
    )

dpsRTUp8252Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8252)
)
dpsRTUp8252Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8252Set.setStatus(
        ""
    )

dpsRTUp8253Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8253)
)
dpsRTUp8253Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8253Set.setStatus(
        ""
    )

dpsRTUp8254Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8254)
)
dpsRTUp8254Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8254Set.setStatus(
        ""
    )

dpsRTUp8255Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8255)
)
dpsRTUp8255Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8255Set.setStatus(
        ""
    )

dpsRTUp8256Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8256)
)
dpsRTUp8256Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8256Set.setStatus(
        ""
    )

dpsRTUp8257Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8257)
)
dpsRTUp8257Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8257Set.setStatus(
        ""
    )

dpsRTUp8258Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8258)
)
dpsRTUp8258Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8258Set.setStatus(
        ""
    )

dpsRTUp8259Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8259)
)
dpsRTUp8259Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8259Set.setStatus(
        ""
    )

dpsRTUp8260Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8260)
)
dpsRTUp8260Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8260Set.setStatus(
        ""
    )

dpsRTUp8321Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8321)
)
dpsRTUp8321Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8321Set.setStatus(
        ""
    )

dpsRTUp8322Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8322)
)
dpsRTUp8322Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8322Set.setStatus(
        ""
    )

dpsRTUp8323Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8323)
)
dpsRTUp8323Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8323Set.setStatus(
        ""
    )

dpsRTUp8324Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8324)
)
dpsRTUp8324Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8324Set.setStatus(
        ""
    )

dpsRTUp8385Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8385)
)
dpsRTUp8385Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8385Set.setStatus(
        ""
    )

dpsRTUp8386Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8386)
)
dpsRTUp8386Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8386Set.setStatus(
        ""
    )

dpsRTUp8387Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8387)
)
dpsRTUp8387Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8387Set.setStatus(
        ""
    )

dpsRTUp8388Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8388)
)
dpsRTUp8388Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8388Set.setStatus(
        ""
    )

dpsRTUp8449Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8449)
)
dpsRTUp8449Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8449Set.setStatus(
        ""
    )

dpsRTUp8450Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8450)
)
dpsRTUp8450Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8450Set.setStatus(
        ""
    )

dpsRTUp8451Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8451)
)
dpsRTUp8451Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8451Set.setStatus(
        ""
    )

dpsRTUp8452Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8452)
)
dpsRTUp8452Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8452Set.setStatus(
        ""
    )

dpsRTUp8513Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8513)
)
dpsRTUp8513Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8513Set.setStatus(
        ""
    )

dpsRTUp8514Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8514)
)
dpsRTUp8514Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8514Set.setStatus(
        ""
    )

dpsRTUp8515Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8515)
)
dpsRTUp8515Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8515Set.setStatus(
        ""
    )

dpsRTUp8516Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8516)
)
dpsRTUp8516Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8516Set.setStatus(
        ""
    )

dpsRTUp8577Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8577)
)
dpsRTUp8577Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8577Set.setStatus(
        ""
    )

dpsRTUp8578Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8578)
)
dpsRTUp8578Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8578Set.setStatus(
        ""
    )

dpsRTUp8579Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8579)
)
dpsRTUp8579Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8579Set.setStatus(
        ""
    )

dpsRTUp8580Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8580)
)
dpsRTUp8580Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8580Set.setStatus(
        ""
    )

dpsRTUp8641Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8641)
)
dpsRTUp8641Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8641Set.setStatus(
        ""
    )

dpsRTUp8642Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8642)
)
dpsRTUp8642Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8642Set.setStatus(
        ""
    )

dpsRTUp8643Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8643)
)
dpsRTUp8643Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8643Set.setStatus(
        ""
    )

dpsRTUp8644Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8644)
)
dpsRTUp8644Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8644Set.setStatus(
        ""
    )

dpsRTUp8645Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8645)
)
dpsRTUp8645Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8645Set.setStatus(
        ""
    )

dpsRTUp8646Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8646)
)
dpsRTUp8646Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8646Set.setStatus(
        ""
    )

dpsRTUp8647Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8647)
)
dpsRTUp8647Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8647Set.setStatus(
        ""
    )

dpsRTUp8648Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8648)
)
dpsRTUp8648Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8648Set.setStatus(
        ""
    )

dpsRTUp8657Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8657)
)
dpsRTUp8657Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8657Set.setStatus(
        ""
    )

dpsRTUp8658Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8658)
)
dpsRTUp8658Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8658Set.setStatus(
        ""
    )

dpsRTUp8659Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8659)
)
dpsRTUp8659Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8659Set.setStatus(
        ""
    )

dpsRTUp8673Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8673)
)
dpsRTUp8673Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8673Set.setStatus(
        ""
    )

dpsRTUp8676Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8676)
)
dpsRTUp8676Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8676Set.setStatus(
        ""
    )

dpsRTUp8677Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8677)
)
dpsRTUp8677Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8677Set.setStatus(
        ""
    )

dpsRTUp8678Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8678)
)
dpsRTUp8678Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8678Set.setStatus(
        ""
    )

dpsRTUp8681Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8681)
)
dpsRTUp8681Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8681Set.setStatus(
        ""
    )

dpsRTUp8682Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8682)
)
dpsRTUp8682Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8682Set.setStatus(
        ""
    )

dpsRTUp8683Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8683)
)
dpsRTUp8683Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8683Set.setStatus(
        ""
    )

dpsRTUp8684Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8684)
)
dpsRTUp8684Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8684Set.setStatus(
        ""
    )

dpsRTUp8685Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8685)
)
dpsRTUp8685Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8685Set.setStatus(
        ""
    )

dpsRTUp8686Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8686)
)
dpsRTUp8686Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8686Set.setStatus(
        ""
    )

dpsRTUp8687Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8687)
)
dpsRTUp8687Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8687Set.setStatus(
        ""
    )

dpsRTUp8688Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8688)
)
dpsRTUp8688Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8688Set.setStatus(
        ""
    )

dpsRTUp8689Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8689)
)
dpsRTUp8689Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8689Set.setStatus(
        ""
    )

dpsRTUp8690Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8690)
)
dpsRTUp8690Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8690Set.setStatus(
        ""
    )

dpsRTUp8691Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8691)
)
dpsRTUp8691Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8691Set.setStatus(
        ""
    )

dpsRTUp8692Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8692)
)
dpsRTUp8692Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8692Set.setStatus(
        ""
    )

dpsRTUp8693Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8693)
)
dpsRTUp8693Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8693Set.setStatus(
        ""
    )

dpsRTUp8694Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8694)
)
dpsRTUp8694Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8694Set.setStatus(
        ""
    )

dpsRTUp8695Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8695)
)
dpsRTUp8695Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8695Set.setStatus(
        ""
    )

dpsRTUp8696Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8696)
)
dpsRTUp8696Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8696Set.setStatus(
        ""
    )

dpsRTUp8697Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8697)
)
dpsRTUp8697Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8697Set.setStatus(
        ""
    )

dpsRTUp8698Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8698)
)
dpsRTUp8698Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8698Set.setStatus(
        ""
    )

dpsRTUp8699Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8699)
)
dpsRTUp8699Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8699Set.setStatus(
        ""
    )

dpsRTUp8700Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8700)
)
dpsRTUp8700Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8700Set.setStatus(
        ""
    )

dpsRTUp8701Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8701)
)
dpsRTUp8701Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8701Set.setStatus(
        ""
    )

dpsRTUp8702Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8702)
)
dpsRTUp8702Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8702Set.setStatus(
        ""
    )

dpsRTUp8703Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8703)
)
dpsRTUp8703Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8703Set.setStatus(
        ""
    )

dpsRTUp8704Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 8704)
)
dpsRTUp8704Set.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp8704Set.setStatus(
        ""
    )

dpsRTUp9001Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9001)
)
dpsRTUp9001Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9001Clr.setStatus(
        ""
    )

dpsRTUp9002Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9002)
)
dpsRTUp9002Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9002Clr.setStatus(
        ""
    )

dpsRTUp9003Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9003)
)
dpsRTUp9003Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9003Clr.setStatus(
        ""
    )

dpsRTUp9004Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9004)
)
dpsRTUp9004Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9004Clr.setStatus(
        ""
    )

dpsRTUp9005Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9005)
)
dpsRTUp9005Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9005Clr.setStatus(
        ""
    )

dpsRTUp9006Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9006)
)
dpsRTUp9006Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9006Clr.setStatus(
        ""
    )

dpsRTUp9007Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9007)
)
dpsRTUp9007Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9007Clr.setStatus(
        ""
    )

dpsRTUp9008Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9008)
)
dpsRTUp9008Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9008Clr.setStatus(
        ""
    )

dpsRTUp9009Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9009)
)
dpsRTUp9009Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9009Clr.setStatus(
        ""
    )

dpsRTUp9010Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9010)
)
dpsRTUp9010Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9010Clr.setStatus(
        ""
    )

dpsRTUp9011Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9011)
)
dpsRTUp9011Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9011Clr.setStatus(
        ""
    )

dpsRTUp9012Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9012)
)
dpsRTUp9012Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9012Clr.setStatus(
        ""
    )

dpsRTUp9013Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9013)
)
dpsRTUp9013Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9013Clr.setStatus(
        ""
    )

dpsRTUp9014Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9014)
)
dpsRTUp9014Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9014Clr.setStatus(
        ""
    )

dpsRTUp9015Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9015)
)
dpsRTUp9015Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9015Clr.setStatus(
        ""
    )

dpsRTUp9016Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9016)
)
dpsRTUp9016Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9016Clr.setStatus(
        ""
    )

dpsRTUp9017Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9017)
)
dpsRTUp9017Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9017Clr.setStatus(
        ""
    )

dpsRTUp9018Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9018)
)
dpsRTUp9018Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9018Clr.setStatus(
        ""
    )

dpsRTUp9019Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9019)
)
dpsRTUp9019Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9019Clr.setStatus(
        ""
    )

dpsRTUp9020Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9020)
)
dpsRTUp9020Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9020Clr.setStatus(
        ""
    )

dpsRTUp9021Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9021)
)
dpsRTUp9021Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9021Clr.setStatus(
        ""
    )

dpsRTUp9022Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9022)
)
dpsRTUp9022Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9022Clr.setStatus(
        ""
    )

dpsRTUp9023Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9023)
)
dpsRTUp9023Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9023Clr.setStatus(
        ""
    )

dpsRTUp9024Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9024)
)
dpsRTUp9024Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9024Clr.setStatus(
        ""
    )

dpsRTUp9025Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9025)
)
dpsRTUp9025Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9025Clr.setStatus(
        ""
    )

dpsRTUp9026Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9026)
)
dpsRTUp9026Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9026Clr.setStatus(
        ""
    )

dpsRTUp9027Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9027)
)
dpsRTUp9027Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9027Clr.setStatus(
        ""
    )

dpsRTUp9028Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9028)
)
dpsRTUp9028Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9028Clr.setStatus(
        ""
    )

dpsRTUp9029Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9029)
)
dpsRTUp9029Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9029Clr.setStatus(
        ""
    )

dpsRTUp9030Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9030)
)
dpsRTUp9030Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9030Clr.setStatus(
        ""
    )

dpsRTUp9031Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9031)
)
dpsRTUp9031Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9031Clr.setStatus(
        ""
    )

dpsRTUp9032Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9032)
)
dpsRTUp9032Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9032Clr.setStatus(
        ""
    )

dpsRTUp9033Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9033)
)
dpsRTUp9033Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9033Clr.setStatus(
        ""
    )

dpsRTUp9034Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9034)
)
dpsRTUp9034Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9034Clr.setStatus(
        ""
    )

dpsRTUp9035Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9035)
)
dpsRTUp9035Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9035Clr.setStatus(
        ""
    )

dpsRTUp9036Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9036)
)
dpsRTUp9036Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9036Clr.setStatus(
        ""
    )

dpsRTUp9037Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9037)
)
dpsRTUp9037Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9037Clr.setStatus(
        ""
    )

dpsRTUp9038Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9038)
)
dpsRTUp9038Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9038Clr.setStatus(
        ""
    )

dpsRTUp9039Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9039)
)
dpsRTUp9039Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9039Clr.setStatus(
        ""
    )

dpsRTUp9040Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9040)
)
dpsRTUp9040Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9040Clr.setStatus(
        ""
    )

dpsRTUp9041Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9041)
)
dpsRTUp9041Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9041Clr.setStatus(
        ""
    )

dpsRTUp9042Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9042)
)
dpsRTUp9042Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9042Clr.setStatus(
        ""
    )

dpsRTUp9043Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9043)
)
dpsRTUp9043Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9043Clr.setStatus(
        ""
    )

dpsRTUp9044Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9044)
)
dpsRTUp9044Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9044Clr.setStatus(
        ""
    )

dpsRTUp9045Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9045)
)
dpsRTUp9045Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9045Clr.setStatus(
        ""
    )

dpsRTUp9046Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9046)
)
dpsRTUp9046Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9046Clr.setStatus(
        ""
    )

dpsRTUp9047Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9047)
)
dpsRTUp9047Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9047Clr.setStatus(
        ""
    )

dpsRTUp9048Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9048)
)
dpsRTUp9048Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9048Clr.setStatus(
        ""
    )

dpsRTUp9049Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9049)
)
dpsRTUp9049Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9049Clr.setStatus(
        ""
    )

dpsRTUp9050Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9050)
)
dpsRTUp9050Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9050Clr.setStatus(
        ""
    )

dpsRTUp9051Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9051)
)
dpsRTUp9051Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9051Clr.setStatus(
        ""
    )

dpsRTUp9052Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9052)
)
dpsRTUp9052Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9052Clr.setStatus(
        ""
    )

dpsRTUp9053Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9053)
)
dpsRTUp9053Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9053Clr.setStatus(
        ""
    )

dpsRTUp9054Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9054)
)
dpsRTUp9054Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9054Clr.setStatus(
        ""
    )

dpsRTUp9055Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9055)
)
dpsRTUp9055Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9055Clr.setStatus(
        ""
    )

dpsRTUp9056Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9056)
)
dpsRTUp9056Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9056Clr.setStatus(
        ""
    )

dpsRTUp9057Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9057)
)
dpsRTUp9057Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9057Clr.setStatus(
        ""
    )

dpsRTUp9058Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9058)
)
dpsRTUp9058Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9058Clr.setStatus(
        ""
    )

dpsRTUp9059Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9059)
)
dpsRTUp9059Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9059Clr.setStatus(
        ""
    )

dpsRTUp9060Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9060)
)
dpsRTUp9060Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9060Clr.setStatus(
        ""
    )

dpsRTUp9061Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9061)
)
dpsRTUp9061Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9061Clr.setStatus(
        ""
    )

dpsRTUp9062Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9062)
)
dpsRTUp9062Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9062Clr.setStatus(
        ""
    )

dpsRTUp9063Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9063)
)
dpsRTUp9063Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9063Clr.setStatus(
        ""
    )

dpsRTUp9064Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9064)
)
dpsRTUp9064Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9064Clr.setStatus(
        ""
    )

dpsRTUp9065Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9065)
)
dpsRTUp9065Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9065Clr.setStatus(
        ""
    )

dpsRTUp9066Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9066)
)
dpsRTUp9066Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9066Clr.setStatus(
        ""
    )

dpsRTUp9067Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9067)
)
dpsRTUp9067Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9067Clr.setStatus(
        ""
    )

dpsRTUp9068Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9068)
)
dpsRTUp9068Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9068Clr.setStatus(
        ""
    )

dpsRTUp9069Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9069)
)
dpsRTUp9069Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9069Clr.setStatus(
        ""
    )

dpsRTUp9070Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9070)
)
dpsRTUp9070Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9070Clr.setStatus(
        ""
    )

dpsRTUp9071Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9071)
)
dpsRTUp9071Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9071Clr.setStatus(
        ""
    )

dpsRTUp9072Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9072)
)
dpsRTUp9072Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9072Clr.setStatus(
        ""
    )

dpsRTUp9073Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9073)
)
dpsRTUp9073Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9073Clr.setStatus(
        ""
    )

dpsRTUp9074Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9074)
)
dpsRTUp9074Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9074Clr.setStatus(
        ""
    )

dpsRTUp9075Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9075)
)
dpsRTUp9075Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9075Clr.setStatus(
        ""
    )

dpsRTUp9076Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9076)
)
dpsRTUp9076Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9076Clr.setStatus(
        ""
    )

dpsRTUp9077Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9077)
)
dpsRTUp9077Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9077Clr.setStatus(
        ""
    )

dpsRTUp9078Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9078)
)
dpsRTUp9078Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9078Clr.setStatus(
        ""
    )

dpsRTUp9079Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9079)
)
dpsRTUp9079Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9079Clr.setStatus(
        ""
    )

dpsRTUp9080Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9080)
)
dpsRTUp9080Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9080Clr.setStatus(
        ""
    )

dpsRTUp9081Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9081)
)
dpsRTUp9081Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9081Clr.setStatus(
        ""
    )

dpsRTUp9082Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9082)
)
dpsRTUp9082Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9082Clr.setStatus(
        ""
    )

dpsRTUp9083Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9083)
)
dpsRTUp9083Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9083Clr.setStatus(
        ""
    )

dpsRTUp9084Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9084)
)
dpsRTUp9084Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9084Clr.setStatus(
        ""
    )

dpsRTUp9085Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9085)
)
dpsRTUp9085Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9085Clr.setStatus(
        ""
    )

dpsRTUp9086Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9086)
)
dpsRTUp9086Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9086Clr.setStatus(
        ""
    )

dpsRTUp9087Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9087)
)
dpsRTUp9087Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9087Clr.setStatus(
        ""
    )

dpsRTUp9088Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9088)
)
dpsRTUp9088Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9088Clr.setStatus(
        ""
    )

dpsRTUp9089Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9089)
)
dpsRTUp9089Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9089Clr.setStatus(
        ""
    )

dpsRTUp9090Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9090)
)
dpsRTUp9090Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9090Clr.setStatus(
        ""
    )

dpsRTUp9091Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9091)
)
dpsRTUp9091Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9091Clr.setStatus(
        ""
    )

dpsRTUp9092Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9092)
)
dpsRTUp9092Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9092Clr.setStatus(
        ""
    )

dpsRTUp9093Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9093)
)
dpsRTUp9093Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9093Clr.setStatus(
        ""
    )

dpsRTUp9094Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9094)
)
dpsRTUp9094Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9094Clr.setStatus(
        ""
    )

dpsRTUp9095Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9095)
)
dpsRTUp9095Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9095Clr.setStatus(
        ""
    )

dpsRTUp9096Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9096)
)
dpsRTUp9096Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9096Clr.setStatus(
        ""
    )

dpsRTUp9097Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9097)
)
dpsRTUp9097Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9097Clr.setStatus(
        ""
    )

dpsRTUp9098Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9098)
)
dpsRTUp9098Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9098Clr.setStatus(
        ""
    )

dpsRTUp9099Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9099)
)
dpsRTUp9099Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9099Clr.setStatus(
        ""
    )

dpsRTUp9100Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9100)
)
dpsRTUp9100Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9100Clr.setStatus(
        ""
    )

dpsRTUp9101Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9101)
)
dpsRTUp9101Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9101Clr.setStatus(
        ""
    )

dpsRTUp9102Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9102)
)
dpsRTUp9102Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9102Clr.setStatus(
        ""
    )

dpsRTUp9103Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9103)
)
dpsRTUp9103Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9103Clr.setStatus(
        ""
    )

dpsRTUp9104Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9104)
)
dpsRTUp9104Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9104Clr.setStatus(
        ""
    )

dpsRTUp9105Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9105)
)
dpsRTUp9105Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9105Clr.setStatus(
        ""
    )

dpsRTUp9106Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9106)
)
dpsRTUp9106Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9106Clr.setStatus(
        ""
    )

dpsRTUp9107Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9107)
)
dpsRTUp9107Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9107Clr.setStatus(
        ""
    )

dpsRTUp9108Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9108)
)
dpsRTUp9108Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9108Clr.setStatus(
        ""
    )

dpsRTUp9109Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9109)
)
dpsRTUp9109Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9109Clr.setStatus(
        ""
    )

dpsRTUp9110Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9110)
)
dpsRTUp9110Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9110Clr.setStatus(
        ""
    )

dpsRTUp9111Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9111)
)
dpsRTUp9111Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9111Clr.setStatus(
        ""
    )

dpsRTUp9112Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9112)
)
dpsRTUp9112Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9112Clr.setStatus(
        ""
    )

dpsRTUp9113Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9113)
)
dpsRTUp9113Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9113Clr.setStatus(
        ""
    )

dpsRTUp9114Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9114)
)
dpsRTUp9114Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9114Clr.setStatus(
        ""
    )

dpsRTUp9115Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9115)
)
dpsRTUp9115Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9115Clr.setStatus(
        ""
    )

dpsRTUp9116Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9116)
)
dpsRTUp9116Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9116Clr.setStatus(
        ""
    )

dpsRTUp9117Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9117)
)
dpsRTUp9117Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9117Clr.setStatus(
        ""
    )

dpsRTUp9118Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9118)
)
dpsRTUp9118Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9118Clr.setStatus(
        ""
    )

dpsRTUp9119Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9119)
)
dpsRTUp9119Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9119Clr.setStatus(
        ""
    )

dpsRTUp9120Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9120)
)
dpsRTUp9120Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9120Clr.setStatus(
        ""
    )

dpsRTUp9121Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9121)
)
dpsRTUp9121Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9121Clr.setStatus(
        ""
    )

dpsRTUp9122Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9122)
)
dpsRTUp9122Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9122Clr.setStatus(
        ""
    )

dpsRTUp9123Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9123)
)
dpsRTUp9123Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9123Clr.setStatus(
        ""
    )

dpsRTUp9124Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9124)
)
dpsRTUp9124Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9124Clr.setStatus(
        ""
    )

dpsRTUp9125Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9125)
)
dpsRTUp9125Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9125Clr.setStatus(
        ""
    )

dpsRTUp9126Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9126)
)
dpsRTUp9126Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9126Clr.setStatus(
        ""
    )

dpsRTUp9127Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9127)
)
dpsRTUp9127Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9127Clr.setStatus(
        ""
    )

dpsRTUp9128Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9128)
)
dpsRTUp9128Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9128Clr.setStatus(
        ""
    )

dpsRTUp9129Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9129)
)
dpsRTUp9129Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9129Clr.setStatus(
        ""
    )

dpsRTUp9130Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9130)
)
dpsRTUp9130Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9130Clr.setStatus(
        ""
    )

dpsRTUp9131Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9131)
)
dpsRTUp9131Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9131Clr.setStatus(
        ""
    )

dpsRTUp9132Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9132)
)
dpsRTUp9132Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9132Clr.setStatus(
        ""
    )

dpsRTUp9133Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9133)
)
dpsRTUp9133Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9133Clr.setStatus(
        ""
    )

dpsRTUp9134Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9134)
)
dpsRTUp9134Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9134Clr.setStatus(
        ""
    )

dpsRTUp9135Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9135)
)
dpsRTUp9135Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9135Clr.setStatus(
        ""
    )

dpsRTUp9136Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9136)
)
dpsRTUp9136Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9136Clr.setStatus(
        ""
    )

dpsRTUp9137Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9137)
)
dpsRTUp9137Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9137Clr.setStatus(
        ""
    )

dpsRTUp9138Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9138)
)
dpsRTUp9138Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9138Clr.setStatus(
        ""
    )

dpsRTUp9139Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9139)
)
dpsRTUp9139Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9139Clr.setStatus(
        ""
    )

dpsRTUp9140Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9140)
)
dpsRTUp9140Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9140Clr.setStatus(
        ""
    )

dpsRTUp9141Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9141)
)
dpsRTUp9141Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9141Clr.setStatus(
        ""
    )

dpsRTUp9142Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9142)
)
dpsRTUp9142Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9142Clr.setStatus(
        ""
    )

dpsRTUp9143Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9143)
)
dpsRTUp9143Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9143Clr.setStatus(
        ""
    )

dpsRTUp9144Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9144)
)
dpsRTUp9144Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9144Clr.setStatus(
        ""
    )

dpsRTUp9145Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9145)
)
dpsRTUp9145Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9145Clr.setStatus(
        ""
    )

dpsRTUp9146Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9146)
)
dpsRTUp9146Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9146Clr.setStatus(
        ""
    )

dpsRTUp9147Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9147)
)
dpsRTUp9147Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9147Clr.setStatus(
        ""
    )

dpsRTUp9148Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9148)
)
dpsRTUp9148Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9148Clr.setStatus(
        ""
    )

dpsRTUp9149Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9149)
)
dpsRTUp9149Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9149Clr.setStatus(
        ""
    )

dpsRTUp9150Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9150)
)
dpsRTUp9150Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9150Clr.setStatus(
        ""
    )

dpsRTUp9151Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9151)
)
dpsRTUp9151Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9151Clr.setStatus(
        ""
    )

dpsRTUp9152Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9152)
)
dpsRTUp9152Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9152Clr.setStatus(
        ""
    )

dpsRTUp9153Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9153)
)
dpsRTUp9153Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9153Clr.setStatus(
        ""
    )

dpsRTUp9154Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9154)
)
dpsRTUp9154Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9154Clr.setStatus(
        ""
    )

dpsRTUp9155Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9155)
)
dpsRTUp9155Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9155Clr.setStatus(
        ""
    )

dpsRTUp9156Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9156)
)
dpsRTUp9156Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9156Clr.setStatus(
        ""
    )

dpsRTUp9157Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9157)
)
dpsRTUp9157Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9157Clr.setStatus(
        ""
    )

dpsRTUp9158Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9158)
)
dpsRTUp9158Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9158Clr.setStatus(
        ""
    )

dpsRTUp9159Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9159)
)
dpsRTUp9159Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9159Clr.setStatus(
        ""
    )

dpsRTUp9160Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9160)
)
dpsRTUp9160Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9160Clr.setStatus(
        ""
    )

dpsRTUp9161Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9161)
)
dpsRTUp9161Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9161Clr.setStatus(
        ""
    )

dpsRTUp9162Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9162)
)
dpsRTUp9162Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9162Clr.setStatus(
        ""
    )

dpsRTUp9163Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9163)
)
dpsRTUp9163Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9163Clr.setStatus(
        ""
    )

dpsRTUp9164Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9164)
)
dpsRTUp9164Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9164Clr.setStatus(
        ""
    )

dpsRTUp9165Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9165)
)
dpsRTUp9165Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9165Clr.setStatus(
        ""
    )

dpsRTUp9166Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9166)
)
dpsRTUp9166Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9166Clr.setStatus(
        ""
    )

dpsRTUp9167Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9167)
)
dpsRTUp9167Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9167Clr.setStatus(
        ""
    )

dpsRTUp9168Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9168)
)
dpsRTUp9168Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9168Clr.setStatus(
        ""
    )

dpsRTUp9169Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9169)
)
dpsRTUp9169Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9169Clr.setStatus(
        ""
    )

dpsRTUp9170Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9170)
)
dpsRTUp9170Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9170Clr.setStatus(
        ""
    )

dpsRTUp9171Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9171)
)
dpsRTUp9171Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9171Clr.setStatus(
        ""
    )

dpsRTUp9172Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9172)
)
dpsRTUp9172Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9172Clr.setStatus(
        ""
    )

dpsRTUp9173Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9173)
)
dpsRTUp9173Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9173Clr.setStatus(
        ""
    )

dpsRTUp9174Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9174)
)
dpsRTUp9174Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9174Clr.setStatus(
        ""
    )

dpsRTUp9175Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9175)
)
dpsRTUp9175Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9175Clr.setStatus(
        ""
    )

dpsRTUp9176Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9176)
)
dpsRTUp9176Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9176Clr.setStatus(
        ""
    )

dpsRTUp9193Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9193)
)
dpsRTUp9193Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9193Clr.setStatus(
        ""
    )

dpsRTUp9194Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9194)
)
dpsRTUp9194Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9194Clr.setStatus(
        ""
    )

dpsRTUp9195Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9195)
)
dpsRTUp9195Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9195Clr.setStatus(
        ""
    )

dpsRTUp9196Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9196)
)
dpsRTUp9196Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9196Clr.setStatus(
        ""
    )

dpsRTUp9197Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9197)
)
dpsRTUp9197Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9197Clr.setStatus(
        ""
    )

dpsRTUp9198Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9198)
)
dpsRTUp9198Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9198Clr.setStatus(
        ""
    )

dpsRTUp9199Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9199)
)
dpsRTUp9199Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9199Clr.setStatus(
        ""
    )

dpsRTUp9200Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9200)
)
dpsRTUp9200Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9200Clr.setStatus(
        ""
    )

dpsRTUp9201Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9201)
)
dpsRTUp9201Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9201Clr.setStatus(
        ""
    )

dpsRTUp9202Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9202)
)
dpsRTUp9202Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9202Clr.setStatus(
        ""
    )

dpsRTUp9203Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9203)
)
dpsRTUp9203Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9203Clr.setStatus(
        ""
    )

dpsRTUp9204Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9204)
)
dpsRTUp9204Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9204Clr.setStatus(
        ""
    )

dpsRTUp9205Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9205)
)
dpsRTUp9205Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9205Clr.setStatus(
        ""
    )

dpsRTUp9206Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9206)
)
dpsRTUp9206Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9206Clr.setStatus(
        ""
    )

dpsRTUp9207Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9207)
)
dpsRTUp9207Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9207Clr.setStatus(
        ""
    )

dpsRTUp9208Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9208)
)
dpsRTUp9208Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9208Clr.setStatus(
        ""
    )

dpsRTUp9209Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9209)
)
dpsRTUp9209Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9209Clr.setStatus(
        ""
    )

dpsRTUp9210Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9210)
)
dpsRTUp9210Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9210Clr.setStatus(
        ""
    )

dpsRTUp9211Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9211)
)
dpsRTUp9211Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9211Clr.setStatus(
        ""
    )

dpsRTUp9212Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9212)
)
dpsRTUp9212Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9212Clr.setStatus(
        ""
    )

dpsRTUp9213Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9213)
)
dpsRTUp9213Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9213Clr.setStatus(
        ""
    )

dpsRTUp9214Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9214)
)
dpsRTUp9214Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9214Clr.setStatus(
        ""
    )

dpsRTUp9215Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9215)
)
dpsRTUp9215Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9215Clr.setStatus(
        ""
    )

dpsRTUp9216Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9216)
)
dpsRTUp9216Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9216Clr.setStatus(
        ""
    )

dpsRTUp9217Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9217)
)
dpsRTUp9217Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9217Clr.setStatus(
        ""
    )

dpsRTUp9218Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9218)
)
dpsRTUp9218Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9218Clr.setStatus(
        ""
    )

dpsRTUp9219Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9219)
)
dpsRTUp9219Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9219Clr.setStatus(
        ""
    )

dpsRTUp9220Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9220)
)
dpsRTUp9220Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9220Clr.setStatus(
        ""
    )

dpsRTUp9221Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9221)
)
dpsRTUp9221Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9221Clr.setStatus(
        ""
    )

dpsRTUp9222Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9222)
)
dpsRTUp9222Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9222Clr.setStatus(
        ""
    )

dpsRTUp9223Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9223)
)
dpsRTUp9223Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9223Clr.setStatus(
        ""
    )

dpsRTUp9224Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9224)
)
dpsRTUp9224Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9224Clr.setStatus(
        ""
    )

dpsRTUp9225Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9225)
)
dpsRTUp9225Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9225Clr.setStatus(
        ""
    )

dpsRTUp9226Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9226)
)
dpsRTUp9226Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9226Clr.setStatus(
        ""
    )

dpsRTUp9227Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9227)
)
dpsRTUp9227Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9227Clr.setStatus(
        ""
    )

dpsRTUp9228Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9228)
)
dpsRTUp9228Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9228Clr.setStatus(
        ""
    )

dpsRTUp9229Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9229)
)
dpsRTUp9229Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9229Clr.setStatus(
        ""
    )

dpsRTUp9230Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9230)
)
dpsRTUp9230Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9230Clr.setStatus(
        ""
    )

dpsRTUp9231Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9231)
)
dpsRTUp9231Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9231Clr.setStatus(
        ""
    )

dpsRTUp9232Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9232)
)
dpsRTUp9232Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9232Clr.setStatus(
        ""
    )

dpsRTUp9233Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9233)
)
dpsRTUp9233Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9233Clr.setStatus(
        ""
    )

dpsRTUp9234Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9234)
)
dpsRTUp9234Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9234Clr.setStatus(
        ""
    )

dpsRTUp9235Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9235)
)
dpsRTUp9235Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9235Clr.setStatus(
        ""
    )

dpsRTUp9236Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9236)
)
dpsRTUp9236Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9236Clr.setStatus(
        ""
    )

dpsRTUp9237Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9237)
)
dpsRTUp9237Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9237Clr.setStatus(
        ""
    )

dpsRTUp9238Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9238)
)
dpsRTUp9238Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9238Clr.setStatus(
        ""
    )

dpsRTUp9239Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9239)
)
dpsRTUp9239Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9239Clr.setStatus(
        ""
    )

dpsRTUp9240Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9240)
)
dpsRTUp9240Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9240Clr.setStatus(
        ""
    )

dpsRTUp9241Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9241)
)
dpsRTUp9241Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9241Clr.setStatus(
        ""
    )

dpsRTUp9242Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9242)
)
dpsRTUp9242Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9242Clr.setStatus(
        ""
    )

dpsRTUp9243Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9243)
)
dpsRTUp9243Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9243Clr.setStatus(
        ""
    )

dpsRTUp9244Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9244)
)
dpsRTUp9244Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9244Clr.setStatus(
        ""
    )

dpsRTUp9245Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9245)
)
dpsRTUp9245Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9245Clr.setStatus(
        ""
    )

dpsRTUp9246Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9246)
)
dpsRTUp9246Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9246Clr.setStatus(
        ""
    )

dpsRTUp9247Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9247)
)
dpsRTUp9247Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9247Clr.setStatus(
        ""
    )

dpsRTUp9248Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9248)
)
dpsRTUp9248Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9248Clr.setStatus(
        ""
    )

dpsRTUp9249Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9249)
)
dpsRTUp9249Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9249Clr.setStatus(
        ""
    )

dpsRTUp9250Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9250)
)
dpsRTUp9250Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9250Clr.setStatus(
        ""
    )

dpsRTUp9251Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9251)
)
dpsRTUp9251Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9251Clr.setStatus(
        ""
    )

dpsRTUp9252Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9252)
)
dpsRTUp9252Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9252Clr.setStatus(
        ""
    )

dpsRTUp9253Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9253)
)
dpsRTUp9253Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9253Clr.setStatus(
        ""
    )

dpsRTUp9254Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9254)
)
dpsRTUp9254Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9254Clr.setStatus(
        ""
    )

dpsRTUp9255Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9255)
)
dpsRTUp9255Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9255Clr.setStatus(
        ""
    )

dpsRTUp9256Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9256)
)
dpsRTUp9256Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9256Clr.setStatus(
        ""
    )

dpsRTUp9257Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9257)
)
dpsRTUp9257Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9257Clr.setStatus(
        ""
    )

dpsRTUp9258Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9258)
)
dpsRTUp9258Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9258Clr.setStatus(
        ""
    )

dpsRTUp9259Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9259)
)
dpsRTUp9259Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9259Clr.setStatus(
        ""
    )

dpsRTUp9260Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9260)
)
dpsRTUp9260Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9260Clr.setStatus(
        ""
    )

dpsRTUp9321Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9321)
)
dpsRTUp9321Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9321Clr.setStatus(
        ""
    )

dpsRTUp9322Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9322)
)
dpsRTUp9322Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9322Clr.setStatus(
        ""
    )

dpsRTUp9323Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9323)
)
dpsRTUp9323Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9323Clr.setStatus(
        ""
    )

dpsRTUp9324Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9324)
)
dpsRTUp9324Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9324Clr.setStatus(
        ""
    )

dpsRTUp9385Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9385)
)
dpsRTUp9385Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9385Clr.setStatus(
        ""
    )

dpsRTUp9386Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9386)
)
dpsRTUp9386Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9386Clr.setStatus(
        ""
    )

dpsRTUp9387Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9387)
)
dpsRTUp9387Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9387Clr.setStatus(
        ""
    )

dpsRTUp9388Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9388)
)
dpsRTUp9388Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9388Clr.setStatus(
        ""
    )

dpsRTUp9449Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9449)
)
dpsRTUp9449Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9449Clr.setStatus(
        ""
    )

dpsRTUp9450Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9450)
)
dpsRTUp9450Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9450Clr.setStatus(
        ""
    )

dpsRTUp9451Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9451)
)
dpsRTUp9451Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9451Clr.setStatus(
        ""
    )

dpsRTUp9452Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9452)
)
dpsRTUp9452Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9452Clr.setStatus(
        ""
    )

dpsRTUp9513Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9513)
)
dpsRTUp9513Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9513Clr.setStatus(
        ""
    )

dpsRTUp9514Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9514)
)
dpsRTUp9514Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9514Clr.setStatus(
        ""
    )

dpsRTUp9515Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9515)
)
dpsRTUp9515Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9515Clr.setStatus(
        ""
    )

dpsRTUp9516Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9516)
)
dpsRTUp9516Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9516Clr.setStatus(
        ""
    )

dpsRTUp9577Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9577)
)
dpsRTUp9577Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9577Clr.setStatus(
        ""
    )

dpsRTUp9578Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9578)
)
dpsRTUp9578Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9578Clr.setStatus(
        ""
    )

dpsRTUp9579Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9579)
)
dpsRTUp9579Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9579Clr.setStatus(
        ""
    )

dpsRTUp9580Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9580)
)
dpsRTUp9580Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9580Clr.setStatus(
        ""
    )

dpsRTUp9641Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9641)
)
dpsRTUp9641Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9641Clr.setStatus(
        ""
    )

dpsRTUp9642Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9642)
)
dpsRTUp9642Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9642Clr.setStatus(
        ""
    )

dpsRTUp9643Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9643)
)
dpsRTUp9643Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9643Clr.setStatus(
        ""
    )

dpsRTUp9644Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9644)
)
dpsRTUp9644Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9644Clr.setStatus(
        ""
    )

dpsRTUp9645Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9645)
)
dpsRTUp9645Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9645Clr.setStatus(
        ""
    )

dpsRTUp9646Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9646)
)
dpsRTUp9646Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9646Clr.setStatus(
        ""
    )

dpsRTUp9647Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9647)
)
dpsRTUp9647Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9647Clr.setStatus(
        ""
    )

dpsRTUp9648Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9648)
)
dpsRTUp9648Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9648Clr.setStatus(
        ""
    )

dpsRTUp9657Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9657)
)
dpsRTUp9657Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9657Clr.setStatus(
        ""
    )

dpsRTUp9658Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9658)
)
dpsRTUp9658Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9658Clr.setStatus(
        ""
    )

dpsRTUp9659Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9659)
)
dpsRTUp9659Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9659Clr.setStatus(
        ""
    )

dpsRTUp9673Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9673)
)
dpsRTUp9673Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9673Clr.setStatus(
        ""
    )

dpsRTUp9676Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9676)
)
dpsRTUp9676Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9676Clr.setStatus(
        ""
    )

dpsRTUp9677Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9677)
)
dpsRTUp9677Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9677Clr.setStatus(
        ""
    )

dpsRTUp9678Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9678)
)
dpsRTUp9678Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9678Clr.setStatus(
        ""
    )

dpsRTUp9681Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9681)
)
dpsRTUp9681Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9681Clr.setStatus(
        ""
    )

dpsRTUp9682Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9682)
)
dpsRTUp9682Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9682Clr.setStatus(
        ""
    )

dpsRTUp9683Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9683)
)
dpsRTUp9683Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9683Clr.setStatus(
        ""
    )

dpsRTUp9684Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9684)
)
dpsRTUp9684Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9684Clr.setStatus(
        ""
    )

dpsRTUp9685Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9685)
)
dpsRTUp9685Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9685Clr.setStatus(
        ""
    )

dpsRTUp9686Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9686)
)
dpsRTUp9686Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9686Clr.setStatus(
        ""
    )

dpsRTUp9687Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9687)
)
dpsRTUp9687Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9687Clr.setStatus(
        ""
    )

dpsRTUp9688Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9688)
)
dpsRTUp9688Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9688Clr.setStatus(
        ""
    )

dpsRTUp9689Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9689)
)
dpsRTUp9689Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9689Clr.setStatus(
        ""
    )

dpsRTUp9690Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9690)
)
dpsRTUp9690Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9690Clr.setStatus(
        ""
    )

dpsRTUp9691Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9691)
)
dpsRTUp9691Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9691Clr.setStatus(
        ""
    )

dpsRTUp9692Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9692)
)
dpsRTUp9692Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9692Clr.setStatus(
        ""
    )

dpsRTUp9693Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9693)
)
dpsRTUp9693Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9693Clr.setStatus(
        ""
    )

dpsRTUp9694Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9694)
)
dpsRTUp9694Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9694Clr.setStatus(
        ""
    )

dpsRTUp9695Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9695)
)
dpsRTUp9695Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9695Clr.setStatus(
        ""
    )

dpsRTUp9696Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9696)
)
dpsRTUp9696Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9696Clr.setStatus(
        ""
    )

dpsRTUp9697Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9697)
)
dpsRTUp9697Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9697Clr.setStatus(
        ""
    )

dpsRTUp9698Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9698)
)
dpsRTUp9698Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9698Clr.setStatus(
        ""
    )

dpsRTUp9699Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9699)
)
dpsRTUp9699Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9699Clr.setStatus(
        ""
    )

dpsRTUp9700Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9700)
)
dpsRTUp9700Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9700Clr.setStatus(
        ""
    )

dpsRTUp9701Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9701)
)
dpsRTUp9701Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9701Clr.setStatus(
        ""
    )

dpsRTUp9702Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9702)
)
dpsRTUp9702Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9702Clr.setStatus(
        ""
    )

dpsRTUp9703Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9703)
)
dpsRTUp9703Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9703Clr.setStatus(
        ""
    )

dpsRTUp9704Clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 9704)
)
dpsRTUp9704Clr.setObjects(
      *(("DPS-MIB-NGD-V10", "sysDescr"),
        ("DPS-MIB-NGD-V10", "sysLocation"),
        ("DPS-MIB-NGD-V10", "dpsRTUDateTime"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPort"),
        ("DPS-MIB-NGD-V10", "dpsRTUCAddress"),
        ("DPS-MIB-NGD-V10", "dpsRTUADisplay"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPoint"),
        ("DPS-MIB-NGD-V10", "dpsRTUAPntDesc"),
        ("DPS-MIB-NGD-V10", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUp9704Clr.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DPS-MIB-NGD-V10",
    **{"dpsRTUp8001Set": dpsRTUp8001Set,
       "dpsRTUp8002Set": dpsRTUp8002Set,
       "dpsRTUp8003Set": dpsRTUp8003Set,
       "dpsRTUp8004Set": dpsRTUp8004Set,
       "dpsRTUp8005Set": dpsRTUp8005Set,
       "dpsRTUp8006Set": dpsRTUp8006Set,
       "dpsRTUp8007Set": dpsRTUp8007Set,
       "dpsRTUp8008Set": dpsRTUp8008Set,
       "dpsRTUp8009Set": dpsRTUp8009Set,
       "dpsRTUp8010Set": dpsRTUp8010Set,
       "dpsRTUp8011Set": dpsRTUp8011Set,
       "dpsRTUp8012Set": dpsRTUp8012Set,
       "dpsRTUp8013Set": dpsRTUp8013Set,
       "dpsRTUp8014Set": dpsRTUp8014Set,
       "dpsRTUp8015Set": dpsRTUp8015Set,
       "dpsRTUp8016Set": dpsRTUp8016Set,
       "dpsRTUp8017Set": dpsRTUp8017Set,
       "dpsRTUp8018Set": dpsRTUp8018Set,
       "dpsRTUp8019Set": dpsRTUp8019Set,
       "dpsRTUp8020Set": dpsRTUp8020Set,
       "dpsRTUp8021Set": dpsRTUp8021Set,
       "dpsRTUp8022Set": dpsRTUp8022Set,
       "dpsRTUp8023Set": dpsRTUp8023Set,
       "dpsRTUp8024Set": dpsRTUp8024Set,
       "dpsRTUp8025Set": dpsRTUp8025Set,
       "dpsRTUp8026Set": dpsRTUp8026Set,
       "dpsRTUp8027Set": dpsRTUp8027Set,
       "dpsRTUp8028Set": dpsRTUp8028Set,
       "dpsRTUp8029Set": dpsRTUp8029Set,
       "dpsRTUp8030Set": dpsRTUp8030Set,
       "dpsRTUp8031Set": dpsRTUp8031Set,
       "dpsRTUp8032Set": dpsRTUp8032Set,
       "dpsRTUp8033Set": dpsRTUp8033Set,
       "dpsRTUp8034Set": dpsRTUp8034Set,
       "dpsRTUp8035Set": dpsRTUp8035Set,
       "dpsRTUp8036Set": dpsRTUp8036Set,
       "dpsRTUp8037Set": dpsRTUp8037Set,
       "dpsRTUp8038Set": dpsRTUp8038Set,
       "dpsRTUp8039Set": dpsRTUp8039Set,
       "dpsRTUp8040Set": dpsRTUp8040Set,
       "dpsRTUp8041Set": dpsRTUp8041Set,
       "dpsRTUp8042Set": dpsRTUp8042Set,
       "dpsRTUp8043Set": dpsRTUp8043Set,
       "dpsRTUp8044Set": dpsRTUp8044Set,
       "dpsRTUp8045Set": dpsRTUp8045Set,
       "dpsRTUp8046Set": dpsRTUp8046Set,
       "dpsRTUp8047Set": dpsRTUp8047Set,
       "dpsRTUp8048Set": dpsRTUp8048Set,
       "dpsRTUp8049Set": dpsRTUp8049Set,
       "dpsRTUp8050Set": dpsRTUp8050Set,
       "dpsRTUp8051Set": dpsRTUp8051Set,
       "dpsRTUp8052Set": dpsRTUp8052Set,
       "dpsRTUp8053Set": dpsRTUp8053Set,
       "dpsRTUp8054Set": dpsRTUp8054Set,
       "dpsRTUp8055Set": dpsRTUp8055Set,
       "dpsRTUp8056Set": dpsRTUp8056Set,
       "dpsRTUp8057Set": dpsRTUp8057Set,
       "dpsRTUp8058Set": dpsRTUp8058Set,
       "dpsRTUp8059Set": dpsRTUp8059Set,
       "dpsRTUp8060Set": dpsRTUp8060Set,
       "dpsRTUp8061Set": dpsRTUp8061Set,
       "dpsRTUp8062Set": dpsRTUp8062Set,
       "dpsRTUp8063Set": dpsRTUp8063Set,
       "dpsRTUp8064Set": dpsRTUp8064Set,
       "dpsRTUp8065Set": dpsRTUp8065Set,
       "dpsRTUp8066Set": dpsRTUp8066Set,
       "dpsRTUp8067Set": dpsRTUp8067Set,
       "dpsRTUp8068Set": dpsRTUp8068Set,
       "dpsRTUp8069Set": dpsRTUp8069Set,
       "dpsRTUp8070Set": dpsRTUp8070Set,
       "dpsRTUp8071Set": dpsRTUp8071Set,
       "dpsRTUp8072Set": dpsRTUp8072Set,
       "dpsRTUp8073Set": dpsRTUp8073Set,
       "dpsRTUp8074Set": dpsRTUp8074Set,
       "dpsRTUp8075Set": dpsRTUp8075Set,
       "dpsRTUp8076Set": dpsRTUp8076Set,
       "dpsRTUp8077Set": dpsRTUp8077Set,
       "dpsRTUp8078Set": dpsRTUp8078Set,
       "dpsRTUp8079Set": dpsRTUp8079Set,
       "dpsRTUp8080Set": dpsRTUp8080Set,
       "dpsRTUp8081Set": dpsRTUp8081Set,
       "dpsRTUp8082Set": dpsRTUp8082Set,
       "dpsRTUp8083Set": dpsRTUp8083Set,
       "dpsRTUp8084Set": dpsRTUp8084Set,
       "dpsRTUp8085Set": dpsRTUp8085Set,
       "dpsRTUp8086Set": dpsRTUp8086Set,
       "dpsRTUp8087Set": dpsRTUp8087Set,
       "dpsRTUp8088Set": dpsRTUp8088Set,
       "dpsRTUp8089Set": dpsRTUp8089Set,
       "dpsRTUp8090Set": dpsRTUp8090Set,
       "dpsRTUp8091Set": dpsRTUp8091Set,
       "dpsRTUp8092Set": dpsRTUp8092Set,
       "dpsRTUp8093Set": dpsRTUp8093Set,
       "dpsRTUp8094Set": dpsRTUp8094Set,
       "dpsRTUp8095Set": dpsRTUp8095Set,
       "dpsRTUp8096Set": dpsRTUp8096Set,
       "dpsRTUp8097Set": dpsRTUp8097Set,
       "dpsRTUp8098Set": dpsRTUp8098Set,
       "dpsRTUp8099Set": dpsRTUp8099Set,
       "dpsRTUp8100Set": dpsRTUp8100Set,
       "dpsRTUp8101Set": dpsRTUp8101Set,
       "dpsRTUp8102Set": dpsRTUp8102Set,
       "dpsRTUp8103Set": dpsRTUp8103Set,
       "dpsRTUp8104Set": dpsRTUp8104Set,
       "dpsRTUp8105Set": dpsRTUp8105Set,
       "dpsRTUp8106Set": dpsRTUp8106Set,
       "dpsRTUp8107Set": dpsRTUp8107Set,
       "dpsRTUp8108Set": dpsRTUp8108Set,
       "dpsRTUp8109Set": dpsRTUp8109Set,
       "dpsRTUp8110Set": dpsRTUp8110Set,
       "dpsRTUp8111Set": dpsRTUp8111Set,
       "dpsRTUp8112Set": dpsRTUp8112Set,
       "dpsRTUp8113Set": dpsRTUp8113Set,
       "dpsRTUp8114Set": dpsRTUp8114Set,
       "dpsRTUp8115Set": dpsRTUp8115Set,
       "dpsRTUp8116Set": dpsRTUp8116Set,
       "dpsRTUp8117Set": dpsRTUp8117Set,
       "dpsRTUp8118Set": dpsRTUp8118Set,
       "dpsRTUp8119Set": dpsRTUp8119Set,
       "dpsRTUp8120Set": dpsRTUp8120Set,
       "dpsRTUp8121Set": dpsRTUp8121Set,
       "dpsRTUp8122Set": dpsRTUp8122Set,
       "dpsRTUp8123Set": dpsRTUp8123Set,
       "dpsRTUp8124Set": dpsRTUp8124Set,
       "dpsRTUp8125Set": dpsRTUp8125Set,
       "dpsRTUp8126Set": dpsRTUp8126Set,
       "dpsRTUp8127Set": dpsRTUp8127Set,
       "dpsRTUp8128Set": dpsRTUp8128Set,
       "dpsRTUp8129Set": dpsRTUp8129Set,
       "dpsRTUp8130Set": dpsRTUp8130Set,
       "dpsRTUp8131Set": dpsRTUp8131Set,
       "dpsRTUp8132Set": dpsRTUp8132Set,
       "dpsRTUp8133Set": dpsRTUp8133Set,
       "dpsRTUp8134Set": dpsRTUp8134Set,
       "dpsRTUp8135Set": dpsRTUp8135Set,
       "dpsRTUp8136Set": dpsRTUp8136Set,
       "dpsRTUp8137Set": dpsRTUp8137Set,
       "dpsRTUp8138Set": dpsRTUp8138Set,
       "dpsRTUp8139Set": dpsRTUp8139Set,
       "dpsRTUp8140Set": dpsRTUp8140Set,
       "dpsRTUp8141Set": dpsRTUp8141Set,
       "dpsRTUp8142Set": dpsRTUp8142Set,
       "dpsRTUp8143Set": dpsRTUp8143Set,
       "dpsRTUp8144Set": dpsRTUp8144Set,
       "dpsRTUp8145Set": dpsRTUp8145Set,
       "dpsRTUp8146Set": dpsRTUp8146Set,
       "dpsRTUp8147Set": dpsRTUp8147Set,
       "dpsRTUp8148Set": dpsRTUp8148Set,
       "dpsRTUp8149Set": dpsRTUp8149Set,
       "dpsRTUp8150Set": dpsRTUp8150Set,
       "dpsRTUp8151Set": dpsRTUp8151Set,
       "dpsRTUp8152Set": dpsRTUp8152Set,
       "dpsRTUp8153Set": dpsRTUp8153Set,
       "dpsRTUp8154Set": dpsRTUp8154Set,
       "dpsRTUp8155Set": dpsRTUp8155Set,
       "dpsRTUp8156Set": dpsRTUp8156Set,
       "dpsRTUp8157Set": dpsRTUp8157Set,
       "dpsRTUp8158Set": dpsRTUp8158Set,
       "dpsRTUp8159Set": dpsRTUp8159Set,
       "dpsRTUp8160Set": dpsRTUp8160Set,
       "dpsRTUp8161Set": dpsRTUp8161Set,
       "dpsRTUp8162Set": dpsRTUp8162Set,
       "dpsRTUp8163Set": dpsRTUp8163Set,
       "dpsRTUp8164Set": dpsRTUp8164Set,
       "dpsRTUp8165Set": dpsRTUp8165Set,
       "dpsRTUp8166Set": dpsRTUp8166Set,
       "dpsRTUp8167Set": dpsRTUp8167Set,
       "dpsRTUp8168Set": dpsRTUp8168Set,
       "dpsRTUp8169Set": dpsRTUp8169Set,
       "dpsRTUp8170Set": dpsRTUp8170Set,
       "dpsRTUp8171Set": dpsRTUp8171Set,
       "dpsRTUp8172Set": dpsRTUp8172Set,
       "dpsRTUp8173Set": dpsRTUp8173Set,
       "dpsRTUp8174Set": dpsRTUp8174Set,
       "dpsRTUp8175Set": dpsRTUp8175Set,
       "dpsRTUp8176Set": dpsRTUp8176Set,
       "dpsRTUp8193Set": dpsRTUp8193Set,
       "dpsRTUp8194Set": dpsRTUp8194Set,
       "dpsRTUp8195Set": dpsRTUp8195Set,
       "dpsRTUp8196Set": dpsRTUp8196Set,
       "dpsRTUp8197Set": dpsRTUp8197Set,
       "dpsRTUp8198Set": dpsRTUp8198Set,
       "dpsRTUp8199Set": dpsRTUp8199Set,
       "dpsRTUp8200Set": dpsRTUp8200Set,
       "dpsRTUp8201Set": dpsRTUp8201Set,
       "dpsRTUp8202Set": dpsRTUp8202Set,
       "dpsRTUp8203Set": dpsRTUp8203Set,
       "dpsRTUp8204Set": dpsRTUp8204Set,
       "dpsRTUp8205Set": dpsRTUp8205Set,
       "dpsRTUp8206Set": dpsRTUp8206Set,
       "dpsRTUp8207Set": dpsRTUp8207Set,
       "dpsRTUp8208Set": dpsRTUp8208Set,
       "dpsRTUp8209Set": dpsRTUp8209Set,
       "dpsRTUp8210Set": dpsRTUp8210Set,
       "dpsRTUp8211Set": dpsRTUp8211Set,
       "dpsRTUp8212Set": dpsRTUp8212Set,
       "dpsRTUp8213Set": dpsRTUp8213Set,
       "dpsRTUp8214Set": dpsRTUp8214Set,
       "dpsRTUp8215Set": dpsRTUp8215Set,
       "dpsRTUp8216Set": dpsRTUp8216Set,
       "dpsRTUp8217Set": dpsRTUp8217Set,
       "dpsRTUp8218Set": dpsRTUp8218Set,
       "dpsRTUp8219Set": dpsRTUp8219Set,
       "dpsRTUp8220Set": dpsRTUp8220Set,
       "dpsRTUp8221Set": dpsRTUp8221Set,
       "dpsRTUp8222Set": dpsRTUp8222Set,
       "dpsRTUp8223Set": dpsRTUp8223Set,
       "dpsRTUp8224Set": dpsRTUp8224Set,
       "dpsRTUp8225Set": dpsRTUp8225Set,
       "dpsRTUp8226Set": dpsRTUp8226Set,
       "dpsRTUp8227Set": dpsRTUp8227Set,
       "dpsRTUp8228Set": dpsRTUp8228Set,
       "dpsRTUp8229Set": dpsRTUp8229Set,
       "dpsRTUp8230Set": dpsRTUp8230Set,
       "dpsRTUp8231Set": dpsRTUp8231Set,
       "dpsRTUp8232Set": dpsRTUp8232Set,
       "dpsRTUp8233Set": dpsRTUp8233Set,
       "dpsRTUp8234Set": dpsRTUp8234Set,
       "dpsRTUp8235Set": dpsRTUp8235Set,
       "dpsRTUp8236Set": dpsRTUp8236Set,
       "dpsRTUp8237Set": dpsRTUp8237Set,
       "dpsRTUp8238Set": dpsRTUp8238Set,
       "dpsRTUp8239Set": dpsRTUp8239Set,
       "dpsRTUp8240Set": dpsRTUp8240Set,
       "dpsRTUp8241Set": dpsRTUp8241Set,
       "dpsRTUp8242Set": dpsRTUp8242Set,
       "dpsRTUp8243Set": dpsRTUp8243Set,
       "dpsRTUp8244Set": dpsRTUp8244Set,
       "dpsRTUp8245Set": dpsRTUp8245Set,
       "dpsRTUp8246Set": dpsRTUp8246Set,
       "dpsRTUp8247Set": dpsRTUp8247Set,
       "dpsRTUp8248Set": dpsRTUp8248Set,
       "dpsRTUp8249Set": dpsRTUp8249Set,
       "dpsRTUp8250Set": dpsRTUp8250Set,
       "dpsRTUp8251Set": dpsRTUp8251Set,
       "dpsRTUp8252Set": dpsRTUp8252Set,
       "dpsRTUp8253Set": dpsRTUp8253Set,
       "dpsRTUp8254Set": dpsRTUp8254Set,
       "dpsRTUp8255Set": dpsRTUp8255Set,
       "dpsRTUp8256Set": dpsRTUp8256Set,
       "dpsRTUp8257Set": dpsRTUp8257Set,
       "dpsRTUp8258Set": dpsRTUp8258Set,
       "dpsRTUp8259Set": dpsRTUp8259Set,
       "dpsRTUp8260Set": dpsRTUp8260Set,
       "dpsRTUp8321Set": dpsRTUp8321Set,
       "dpsRTUp8322Set": dpsRTUp8322Set,
       "dpsRTUp8323Set": dpsRTUp8323Set,
       "dpsRTUp8324Set": dpsRTUp8324Set,
       "dpsRTUp8385Set": dpsRTUp8385Set,
       "dpsRTUp8386Set": dpsRTUp8386Set,
       "dpsRTUp8387Set": dpsRTUp8387Set,
       "dpsRTUp8388Set": dpsRTUp8388Set,
       "dpsRTUp8449Set": dpsRTUp8449Set,
       "dpsRTUp8450Set": dpsRTUp8450Set,
       "dpsRTUp8451Set": dpsRTUp8451Set,
       "dpsRTUp8452Set": dpsRTUp8452Set,
       "dpsRTUp8513Set": dpsRTUp8513Set,
       "dpsRTUp8514Set": dpsRTUp8514Set,
       "dpsRTUp8515Set": dpsRTUp8515Set,
       "dpsRTUp8516Set": dpsRTUp8516Set,
       "dpsRTUp8577Set": dpsRTUp8577Set,
       "dpsRTUp8578Set": dpsRTUp8578Set,
       "dpsRTUp8579Set": dpsRTUp8579Set,
       "dpsRTUp8580Set": dpsRTUp8580Set,
       "dpsRTUp8641Set": dpsRTUp8641Set,
       "dpsRTUp8642Set": dpsRTUp8642Set,
       "dpsRTUp8643Set": dpsRTUp8643Set,
       "dpsRTUp8644Set": dpsRTUp8644Set,
       "dpsRTUp8645Set": dpsRTUp8645Set,
       "dpsRTUp8646Set": dpsRTUp8646Set,
       "dpsRTUp8647Set": dpsRTUp8647Set,
       "dpsRTUp8648Set": dpsRTUp8648Set,
       "dpsRTUp8657Set": dpsRTUp8657Set,
       "dpsRTUp8658Set": dpsRTUp8658Set,
       "dpsRTUp8659Set": dpsRTUp8659Set,
       "dpsRTUp8673Set": dpsRTUp8673Set,
       "dpsRTUp8676Set": dpsRTUp8676Set,
       "dpsRTUp8677Set": dpsRTUp8677Set,
       "dpsRTUp8678Set": dpsRTUp8678Set,
       "dpsRTUp8681Set": dpsRTUp8681Set,
       "dpsRTUp8682Set": dpsRTUp8682Set,
       "dpsRTUp8683Set": dpsRTUp8683Set,
       "dpsRTUp8684Set": dpsRTUp8684Set,
       "dpsRTUp8685Set": dpsRTUp8685Set,
       "dpsRTUp8686Set": dpsRTUp8686Set,
       "dpsRTUp8687Set": dpsRTUp8687Set,
       "dpsRTUp8688Set": dpsRTUp8688Set,
       "dpsRTUp8689Set": dpsRTUp8689Set,
       "dpsRTUp8690Set": dpsRTUp8690Set,
       "dpsRTUp8691Set": dpsRTUp8691Set,
       "dpsRTUp8692Set": dpsRTUp8692Set,
       "dpsRTUp8693Set": dpsRTUp8693Set,
       "dpsRTUp8694Set": dpsRTUp8694Set,
       "dpsRTUp8695Set": dpsRTUp8695Set,
       "dpsRTUp8696Set": dpsRTUp8696Set,
       "dpsRTUp8697Set": dpsRTUp8697Set,
       "dpsRTUp8698Set": dpsRTUp8698Set,
       "dpsRTUp8699Set": dpsRTUp8699Set,
       "dpsRTUp8700Set": dpsRTUp8700Set,
       "dpsRTUp8701Set": dpsRTUp8701Set,
       "dpsRTUp8702Set": dpsRTUp8702Set,
       "dpsRTUp8703Set": dpsRTUp8703Set,
       "dpsRTUp8704Set": dpsRTUp8704Set,
       "dpsRTUp9001Clr": dpsRTUp9001Clr,
       "dpsRTUp9002Clr": dpsRTUp9002Clr,
       "dpsRTUp9003Clr": dpsRTUp9003Clr,
       "dpsRTUp9004Clr": dpsRTUp9004Clr,
       "dpsRTUp9005Clr": dpsRTUp9005Clr,
       "dpsRTUp9006Clr": dpsRTUp9006Clr,
       "dpsRTUp9007Clr": dpsRTUp9007Clr,
       "dpsRTUp9008Clr": dpsRTUp9008Clr,
       "dpsRTUp9009Clr": dpsRTUp9009Clr,
       "dpsRTUp9010Clr": dpsRTUp9010Clr,
       "dpsRTUp9011Clr": dpsRTUp9011Clr,
       "dpsRTUp9012Clr": dpsRTUp9012Clr,
       "dpsRTUp9013Clr": dpsRTUp9013Clr,
       "dpsRTUp9014Clr": dpsRTUp9014Clr,
       "dpsRTUp9015Clr": dpsRTUp9015Clr,
       "dpsRTUp9016Clr": dpsRTUp9016Clr,
       "dpsRTUp9017Clr": dpsRTUp9017Clr,
       "dpsRTUp9018Clr": dpsRTUp9018Clr,
       "dpsRTUp9019Clr": dpsRTUp9019Clr,
       "dpsRTUp9020Clr": dpsRTUp9020Clr,
       "dpsRTUp9021Clr": dpsRTUp9021Clr,
       "dpsRTUp9022Clr": dpsRTUp9022Clr,
       "dpsRTUp9023Clr": dpsRTUp9023Clr,
       "dpsRTUp9024Clr": dpsRTUp9024Clr,
       "dpsRTUp9025Clr": dpsRTUp9025Clr,
       "dpsRTUp9026Clr": dpsRTUp9026Clr,
       "dpsRTUp9027Clr": dpsRTUp9027Clr,
       "dpsRTUp9028Clr": dpsRTUp9028Clr,
       "dpsRTUp9029Clr": dpsRTUp9029Clr,
       "dpsRTUp9030Clr": dpsRTUp9030Clr,
       "dpsRTUp9031Clr": dpsRTUp9031Clr,
       "dpsRTUp9032Clr": dpsRTUp9032Clr,
       "dpsRTUp9033Clr": dpsRTUp9033Clr,
       "dpsRTUp9034Clr": dpsRTUp9034Clr,
       "dpsRTUp9035Clr": dpsRTUp9035Clr,
       "dpsRTUp9036Clr": dpsRTUp9036Clr,
       "dpsRTUp9037Clr": dpsRTUp9037Clr,
       "dpsRTUp9038Clr": dpsRTUp9038Clr,
       "dpsRTUp9039Clr": dpsRTUp9039Clr,
       "dpsRTUp9040Clr": dpsRTUp9040Clr,
       "dpsRTUp9041Clr": dpsRTUp9041Clr,
       "dpsRTUp9042Clr": dpsRTUp9042Clr,
       "dpsRTUp9043Clr": dpsRTUp9043Clr,
       "dpsRTUp9044Clr": dpsRTUp9044Clr,
       "dpsRTUp9045Clr": dpsRTUp9045Clr,
       "dpsRTUp9046Clr": dpsRTUp9046Clr,
       "dpsRTUp9047Clr": dpsRTUp9047Clr,
       "dpsRTUp9048Clr": dpsRTUp9048Clr,
       "dpsRTUp9049Clr": dpsRTUp9049Clr,
       "dpsRTUp9050Clr": dpsRTUp9050Clr,
       "dpsRTUp9051Clr": dpsRTUp9051Clr,
       "dpsRTUp9052Clr": dpsRTUp9052Clr,
       "dpsRTUp9053Clr": dpsRTUp9053Clr,
       "dpsRTUp9054Clr": dpsRTUp9054Clr,
       "dpsRTUp9055Clr": dpsRTUp9055Clr,
       "dpsRTUp9056Clr": dpsRTUp9056Clr,
       "dpsRTUp9057Clr": dpsRTUp9057Clr,
       "dpsRTUp9058Clr": dpsRTUp9058Clr,
       "dpsRTUp9059Clr": dpsRTUp9059Clr,
       "dpsRTUp9060Clr": dpsRTUp9060Clr,
       "dpsRTUp9061Clr": dpsRTUp9061Clr,
       "dpsRTUp9062Clr": dpsRTUp9062Clr,
       "dpsRTUp9063Clr": dpsRTUp9063Clr,
       "dpsRTUp9064Clr": dpsRTUp9064Clr,
       "dpsRTUp9065Clr": dpsRTUp9065Clr,
       "dpsRTUp9066Clr": dpsRTUp9066Clr,
       "dpsRTUp9067Clr": dpsRTUp9067Clr,
       "dpsRTUp9068Clr": dpsRTUp9068Clr,
       "dpsRTUp9069Clr": dpsRTUp9069Clr,
       "dpsRTUp9070Clr": dpsRTUp9070Clr,
       "dpsRTUp9071Clr": dpsRTUp9071Clr,
       "dpsRTUp9072Clr": dpsRTUp9072Clr,
       "dpsRTUp9073Clr": dpsRTUp9073Clr,
       "dpsRTUp9074Clr": dpsRTUp9074Clr,
       "dpsRTUp9075Clr": dpsRTUp9075Clr,
       "dpsRTUp9076Clr": dpsRTUp9076Clr,
       "dpsRTUp9077Clr": dpsRTUp9077Clr,
       "dpsRTUp9078Clr": dpsRTUp9078Clr,
       "dpsRTUp9079Clr": dpsRTUp9079Clr,
       "dpsRTUp9080Clr": dpsRTUp9080Clr,
       "dpsRTUp9081Clr": dpsRTUp9081Clr,
       "dpsRTUp9082Clr": dpsRTUp9082Clr,
       "dpsRTUp9083Clr": dpsRTUp9083Clr,
       "dpsRTUp9084Clr": dpsRTUp9084Clr,
       "dpsRTUp9085Clr": dpsRTUp9085Clr,
       "dpsRTUp9086Clr": dpsRTUp9086Clr,
       "dpsRTUp9087Clr": dpsRTUp9087Clr,
       "dpsRTUp9088Clr": dpsRTUp9088Clr,
       "dpsRTUp9089Clr": dpsRTUp9089Clr,
       "dpsRTUp9090Clr": dpsRTUp9090Clr,
       "dpsRTUp9091Clr": dpsRTUp9091Clr,
       "dpsRTUp9092Clr": dpsRTUp9092Clr,
       "dpsRTUp9093Clr": dpsRTUp9093Clr,
       "dpsRTUp9094Clr": dpsRTUp9094Clr,
       "dpsRTUp9095Clr": dpsRTUp9095Clr,
       "dpsRTUp9096Clr": dpsRTUp9096Clr,
       "dpsRTUp9097Clr": dpsRTUp9097Clr,
       "dpsRTUp9098Clr": dpsRTUp9098Clr,
       "dpsRTUp9099Clr": dpsRTUp9099Clr,
       "dpsRTUp9100Clr": dpsRTUp9100Clr,
       "dpsRTUp9101Clr": dpsRTUp9101Clr,
       "dpsRTUp9102Clr": dpsRTUp9102Clr,
       "dpsRTUp9103Clr": dpsRTUp9103Clr,
       "dpsRTUp9104Clr": dpsRTUp9104Clr,
       "dpsRTUp9105Clr": dpsRTUp9105Clr,
       "dpsRTUp9106Clr": dpsRTUp9106Clr,
       "dpsRTUp9107Clr": dpsRTUp9107Clr,
       "dpsRTUp9108Clr": dpsRTUp9108Clr,
       "dpsRTUp9109Clr": dpsRTUp9109Clr,
       "dpsRTUp9110Clr": dpsRTUp9110Clr,
       "dpsRTUp9111Clr": dpsRTUp9111Clr,
       "dpsRTUp9112Clr": dpsRTUp9112Clr,
       "dpsRTUp9113Clr": dpsRTUp9113Clr,
       "dpsRTUp9114Clr": dpsRTUp9114Clr,
       "dpsRTUp9115Clr": dpsRTUp9115Clr,
       "dpsRTUp9116Clr": dpsRTUp9116Clr,
       "dpsRTUp9117Clr": dpsRTUp9117Clr,
       "dpsRTUp9118Clr": dpsRTUp9118Clr,
       "dpsRTUp9119Clr": dpsRTUp9119Clr,
       "dpsRTUp9120Clr": dpsRTUp9120Clr,
       "dpsRTUp9121Clr": dpsRTUp9121Clr,
       "dpsRTUp9122Clr": dpsRTUp9122Clr,
       "dpsRTUp9123Clr": dpsRTUp9123Clr,
       "dpsRTUp9124Clr": dpsRTUp9124Clr,
       "dpsRTUp9125Clr": dpsRTUp9125Clr,
       "dpsRTUp9126Clr": dpsRTUp9126Clr,
       "dpsRTUp9127Clr": dpsRTUp9127Clr,
       "dpsRTUp9128Clr": dpsRTUp9128Clr,
       "dpsRTUp9129Clr": dpsRTUp9129Clr,
       "dpsRTUp9130Clr": dpsRTUp9130Clr,
       "dpsRTUp9131Clr": dpsRTUp9131Clr,
       "dpsRTUp9132Clr": dpsRTUp9132Clr,
       "dpsRTUp9133Clr": dpsRTUp9133Clr,
       "dpsRTUp9134Clr": dpsRTUp9134Clr,
       "dpsRTUp9135Clr": dpsRTUp9135Clr,
       "dpsRTUp9136Clr": dpsRTUp9136Clr,
       "dpsRTUp9137Clr": dpsRTUp9137Clr,
       "dpsRTUp9138Clr": dpsRTUp9138Clr,
       "dpsRTUp9139Clr": dpsRTUp9139Clr,
       "dpsRTUp9140Clr": dpsRTUp9140Clr,
       "dpsRTUp9141Clr": dpsRTUp9141Clr,
       "dpsRTUp9142Clr": dpsRTUp9142Clr,
       "dpsRTUp9143Clr": dpsRTUp9143Clr,
       "dpsRTUp9144Clr": dpsRTUp9144Clr,
       "dpsRTUp9145Clr": dpsRTUp9145Clr,
       "dpsRTUp9146Clr": dpsRTUp9146Clr,
       "dpsRTUp9147Clr": dpsRTUp9147Clr,
       "dpsRTUp9148Clr": dpsRTUp9148Clr,
       "dpsRTUp9149Clr": dpsRTUp9149Clr,
       "dpsRTUp9150Clr": dpsRTUp9150Clr,
       "dpsRTUp9151Clr": dpsRTUp9151Clr,
       "dpsRTUp9152Clr": dpsRTUp9152Clr,
       "dpsRTUp9153Clr": dpsRTUp9153Clr,
       "dpsRTUp9154Clr": dpsRTUp9154Clr,
       "dpsRTUp9155Clr": dpsRTUp9155Clr,
       "dpsRTUp9156Clr": dpsRTUp9156Clr,
       "dpsRTUp9157Clr": dpsRTUp9157Clr,
       "dpsRTUp9158Clr": dpsRTUp9158Clr,
       "dpsRTUp9159Clr": dpsRTUp9159Clr,
       "dpsRTUp9160Clr": dpsRTUp9160Clr,
       "dpsRTUp9161Clr": dpsRTUp9161Clr,
       "dpsRTUp9162Clr": dpsRTUp9162Clr,
       "dpsRTUp9163Clr": dpsRTUp9163Clr,
       "dpsRTUp9164Clr": dpsRTUp9164Clr,
       "dpsRTUp9165Clr": dpsRTUp9165Clr,
       "dpsRTUp9166Clr": dpsRTUp9166Clr,
       "dpsRTUp9167Clr": dpsRTUp9167Clr,
       "dpsRTUp9168Clr": dpsRTUp9168Clr,
       "dpsRTUp9169Clr": dpsRTUp9169Clr,
       "dpsRTUp9170Clr": dpsRTUp9170Clr,
       "dpsRTUp9171Clr": dpsRTUp9171Clr,
       "dpsRTUp9172Clr": dpsRTUp9172Clr,
       "dpsRTUp9173Clr": dpsRTUp9173Clr,
       "dpsRTUp9174Clr": dpsRTUp9174Clr,
       "dpsRTUp9175Clr": dpsRTUp9175Clr,
       "dpsRTUp9176Clr": dpsRTUp9176Clr,
       "dpsRTUp9193Clr": dpsRTUp9193Clr,
       "dpsRTUp9194Clr": dpsRTUp9194Clr,
       "dpsRTUp9195Clr": dpsRTUp9195Clr,
       "dpsRTUp9196Clr": dpsRTUp9196Clr,
       "dpsRTUp9197Clr": dpsRTUp9197Clr,
       "dpsRTUp9198Clr": dpsRTUp9198Clr,
       "dpsRTUp9199Clr": dpsRTUp9199Clr,
       "dpsRTUp9200Clr": dpsRTUp9200Clr,
       "dpsRTUp9201Clr": dpsRTUp9201Clr,
       "dpsRTUp9202Clr": dpsRTUp9202Clr,
       "dpsRTUp9203Clr": dpsRTUp9203Clr,
       "dpsRTUp9204Clr": dpsRTUp9204Clr,
       "dpsRTUp9205Clr": dpsRTUp9205Clr,
       "dpsRTUp9206Clr": dpsRTUp9206Clr,
       "dpsRTUp9207Clr": dpsRTUp9207Clr,
       "dpsRTUp9208Clr": dpsRTUp9208Clr,
       "dpsRTUp9209Clr": dpsRTUp9209Clr,
       "dpsRTUp9210Clr": dpsRTUp9210Clr,
       "dpsRTUp9211Clr": dpsRTUp9211Clr,
       "dpsRTUp9212Clr": dpsRTUp9212Clr,
       "dpsRTUp9213Clr": dpsRTUp9213Clr,
       "dpsRTUp9214Clr": dpsRTUp9214Clr,
       "dpsRTUp9215Clr": dpsRTUp9215Clr,
       "dpsRTUp9216Clr": dpsRTUp9216Clr,
       "dpsRTUp9217Clr": dpsRTUp9217Clr,
       "dpsRTUp9218Clr": dpsRTUp9218Clr,
       "dpsRTUp9219Clr": dpsRTUp9219Clr,
       "dpsRTUp9220Clr": dpsRTUp9220Clr,
       "dpsRTUp9221Clr": dpsRTUp9221Clr,
       "dpsRTUp9222Clr": dpsRTUp9222Clr,
       "dpsRTUp9223Clr": dpsRTUp9223Clr,
       "dpsRTUp9224Clr": dpsRTUp9224Clr,
       "dpsRTUp9225Clr": dpsRTUp9225Clr,
       "dpsRTUp9226Clr": dpsRTUp9226Clr,
       "dpsRTUp9227Clr": dpsRTUp9227Clr,
       "dpsRTUp9228Clr": dpsRTUp9228Clr,
       "dpsRTUp9229Clr": dpsRTUp9229Clr,
       "dpsRTUp9230Clr": dpsRTUp9230Clr,
       "dpsRTUp9231Clr": dpsRTUp9231Clr,
       "dpsRTUp9232Clr": dpsRTUp9232Clr,
       "dpsRTUp9233Clr": dpsRTUp9233Clr,
       "dpsRTUp9234Clr": dpsRTUp9234Clr,
       "dpsRTUp9235Clr": dpsRTUp9235Clr,
       "dpsRTUp9236Clr": dpsRTUp9236Clr,
       "dpsRTUp9237Clr": dpsRTUp9237Clr,
       "dpsRTUp9238Clr": dpsRTUp9238Clr,
       "dpsRTUp9239Clr": dpsRTUp9239Clr,
       "dpsRTUp9240Clr": dpsRTUp9240Clr,
       "dpsRTUp9241Clr": dpsRTUp9241Clr,
       "dpsRTUp9242Clr": dpsRTUp9242Clr,
       "dpsRTUp9243Clr": dpsRTUp9243Clr,
       "dpsRTUp9244Clr": dpsRTUp9244Clr,
       "dpsRTUp9245Clr": dpsRTUp9245Clr,
       "dpsRTUp9246Clr": dpsRTUp9246Clr,
       "dpsRTUp9247Clr": dpsRTUp9247Clr,
       "dpsRTUp9248Clr": dpsRTUp9248Clr,
       "dpsRTUp9249Clr": dpsRTUp9249Clr,
       "dpsRTUp9250Clr": dpsRTUp9250Clr,
       "dpsRTUp9251Clr": dpsRTUp9251Clr,
       "dpsRTUp9252Clr": dpsRTUp9252Clr,
       "dpsRTUp9253Clr": dpsRTUp9253Clr,
       "dpsRTUp9254Clr": dpsRTUp9254Clr,
       "dpsRTUp9255Clr": dpsRTUp9255Clr,
       "dpsRTUp9256Clr": dpsRTUp9256Clr,
       "dpsRTUp9257Clr": dpsRTUp9257Clr,
       "dpsRTUp9258Clr": dpsRTUp9258Clr,
       "dpsRTUp9259Clr": dpsRTUp9259Clr,
       "dpsRTUp9260Clr": dpsRTUp9260Clr,
       "dpsRTUp9321Clr": dpsRTUp9321Clr,
       "dpsRTUp9322Clr": dpsRTUp9322Clr,
       "dpsRTUp9323Clr": dpsRTUp9323Clr,
       "dpsRTUp9324Clr": dpsRTUp9324Clr,
       "dpsRTUp9385Clr": dpsRTUp9385Clr,
       "dpsRTUp9386Clr": dpsRTUp9386Clr,
       "dpsRTUp9387Clr": dpsRTUp9387Clr,
       "dpsRTUp9388Clr": dpsRTUp9388Clr,
       "dpsRTUp9449Clr": dpsRTUp9449Clr,
       "dpsRTUp9450Clr": dpsRTUp9450Clr,
       "dpsRTUp9451Clr": dpsRTUp9451Clr,
       "dpsRTUp9452Clr": dpsRTUp9452Clr,
       "dpsRTUp9513Clr": dpsRTUp9513Clr,
       "dpsRTUp9514Clr": dpsRTUp9514Clr,
       "dpsRTUp9515Clr": dpsRTUp9515Clr,
       "dpsRTUp9516Clr": dpsRTUp9516Clr,
       "dpsRTUp9577Clr": dpsRTUp9577Clr,
       "dpsRTUp9578Clr": dpsRTUp9578Clr,
       "dpsRTUp9579Clr": dpsRTUp9579Clr,
       "dpsRTUp9580Clr": dpsRTUp9580Clr,
       "dpsRTUp9641Clr": dpsRTUp9641Clr,
       "dpsRTUp9642Clr": dpsRTUp9642Clr,
       "dpsRTUp9643Clr": dpsRTUp9643Clr,
       "dpsRTUp9644Clr": dpsRTUp9644Clr,
       "dpsRTUp9645Clr": dpsRTUp9645Clr,
       "dpsRTUp9646Clr": dpsRTUp9646Clr,
       "dpsRTUp9647Clr": dpsRTUp9647Clr,
       "dpsRTUp9648Clr": dpsRTUp9648Clr,
       "dpsRTUp9657Clr": dpsRTUp9657Clr,
       "dpsRTUp9658Clr": dpsRTUp9658Clr,
       "dpsRTUp9659Clr": dpsRTUp9659Clr,
       "dpsRTUp9673Clr": dpsRTUp9673Clr,
       "dpsRTUp9676Clr": dpsRTUp9676Clr,
       "dpsRTUp9677Clr": dpsRTUp9677Clr,
       "dpsRTUp9678Clr": dpsRTUp9678Clr,
       "dpsRTUp9681Clr": dpsRTUp9681Clr,
       "dpsRTUp9682Clr": dpsRTUp9682Clr,
       "dpsRTUp9683Clr": dpsRTUp9683Clr,
       "dpsRTUp9684Clr": dpsRTUp9684Clr,
       "dpsRTUp9685Clr": dpsRTUp9685Clr,
       "dpsRTUp9686Clr": dpsRTUp9686Clr,
       "dpsRTUp9687Clr": dpsRTUp9687Clr,
       "dpsRTUp9688Clr": dpsRTUp9688Clr,
       "dpsRTUp9689Clr": dpsRTUp9689Clr,
       "dpsRTUp9690Clr": dpsRTUp9690Clr,
       "dpsRTUp9691Clr": dpsRTUp9691Clr,
       "dpsRTUp9692Clr": dpsRTUp9692Clr,
       "dpsRTUp9693Clr": dpsRTUp9693Clr,
       "dpsRTUp9694Clr": dpsRTUp9694Clr,
       "dpsRTUp9695Clr": dpsRTUp9695Clr,
       "dpsRTUp9696Clr": dpsRTUp9696Clr,
       "dpsRTUp9697Clr": dpsRTUp9697Clr,
       "dpsRTUp9698Clr": dpsRTUp9698Clr,
       "dpsRTUp9699Clr": dpsRTUp9699Clr,
       "dpsRTUp9700Clr": dpsRTUp9700Clr,
       "dpsRTUp9701Clr": dpsRTUp9701Clr,
       "dpsRTUp9702Clr": dpsRTUp9702Clr,
       "dpsRTUp9703Clr": dpsRTUp9703Clr,
       "dpsRTUp9704Clr": dpsRTUp9704Clr}
)
