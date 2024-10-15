# SNMP MIB module (RADLAN-CDB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-CDB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:41:52 2024
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

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlCDB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 94)
)
rlCDB.setRevisions(
        ("2007-01-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlStartupCDBChanged_Type = TruthValue
_RlStartupCDBChanged_Object = MibScalar
rlStartupCDBChanged = _RlStartupCDBChanged_Object(
    (1, 3, 6, 1, 4, 1, 89, 94, 1),
    _RlStartupCDBChanged_Type()
)
rlStartupCDBChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStartupCDBChanged.setStatus("current")
_RlManualReboot_Type = TruthValue
_RlManualReboot_Object = MibScalar
rlManualReboot = _RlManualReboot_Object(
    (1, 3, 6, 1, 4, 1, 89, 94, 2),
    _RlManualReboot_Type()
)
rlManualReboot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlManualReboot.setStatus("current")
_RlStartupCDBEmpty_Type = TruthValue
_RlStartupCDBEmpty_Object = MibScalar
rlStartupCDBEmpty = _RlStartupCDBEmpty_Object(
    (1, 3, 6, 1, 4, 1, 89, 94, 3),
    _RlStartupCDBEmpty_Type()
)
rlStartupCDBEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStartupCDBEmpty.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-CDB-MIB",
    **{"rlCDB": rlCDB,
       "rlStartupCDBChanged": rlStartupCDBChanged,
       "rlManualReboot": rlManualReboot,
       "rlStartupCDBEmpty": rlStartupCDBEmpty}
)
