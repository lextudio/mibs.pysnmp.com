# SNMP MIB module (ADTRAN-ATLAS-HSSI-V35-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTRAN-ATLAS-HSSI-V35-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:22 2024
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

(adATLASModuleInfoFPStatus,) = mibBuilder.importSymbols(
    "ADTRAN-ATLAS-MODULE-MIB",
    "adATLASModuleInfoFPStatus")

(adATLASUnitFPStatus,
 adATLASUnitPortAddress,
 adATLASUnitSlotAddress) = mibBuilder.importSymbols(
    "ADTRAN-ATLAS-UNIT-MIB",
    "adATLASUnitFPStatus",
    "adATLASUnitPortAddress",
    "adATLASUnitSlotAddress")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 NotificationType,
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
    "NotificationType",
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

_Adtran_ObjectIdentity = ObjectIdentity
adtran = _Adtran_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664)
)
_AdMgmt_ObjectIdentity = ObjectIdentity
adMgmt = _AdMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2)
)
_AdATLASmg_ObjectIdentity = ObjectIdentity
adATLASmg = _AdATLASmg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 154)
)
_AdGenATLASmg_ObjectIdentity = ObjectIdentity
adGenATLASmg = _AdGenATLASmg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1)
)
_AdATLASHSSIV35mg_ObjectIdentity = ObjectIdentity
adATLASHSSIV35mg = _AdATLASHSSIV35mg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 11)
)

# Managed Objects groups


# Notification objects

adATLASHSSIV35IfceDeact = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15401100)
)
adATLASHSSIV35IfceDeact.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"))
)
if mibBuilder.loadTexts:
    adATLASHSSIV35IfceDeact.setStatus(
        ""
    )

adATLASHSSIV35IfceReact = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15401101)
)
adATLASHSSIV35IfceReact.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"))
)
if mibBuilder.loadTexts:
    adATLASHSSIV35IfceReact.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-ATLAS-HSSI-V35-MIB",
    **{"adtran": adtran,
       "adMgmt": adMgmt,
       "adATLASmg": adATLASmg,
       "adATLASHSSIV35IfceDeact": adATLASHSSIV35IfceDeact,
       "adATLASHSSIV35IfceReact": adATLASHSSIV35IfceReact,
       "adGenATLASmg": adGenATLASmg,
       "adATLASHSSIV35mg": adATLASHSSIV35mg}
)
