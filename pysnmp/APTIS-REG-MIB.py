# SNMP MIB module (APTIS-REG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APTIS-REG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:03 2024
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

(aptis_reg,) = mibBuilder.importSymbols(
    "APTIS-MIB",
    "aptis-reg")

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

aptisRegModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2637, 1, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Aptis_modules_ObjectIdentity = ObjectIdentity
aptis_modules = _Aptis_modules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2637, 1, 1)
)
if mibBuilder.loadTexts:
    aptis_modules.setStatus("current")
_Aptis_systems_ObjectIdentity = ObjectIdentity
aptis_systems = _Aptis_systems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2637, 1, 2)
)
if mibBuilder.loadTexts:
    aptis_systems.setStatus("current")
_Cvx_ObjectIdentity = ObjectIdentity
cvx = _Cvx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2637, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cvx.setStatus("current")
_Cvx_1800_ObjectIdentity = ObjectIdentity
cvx_1800 = _Cvx_1800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2637, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cvx_1800.setStatus("current")
_Cvx_600_ObjectIdentity = ObjectIdentity
cvx_600 = _Cvx_600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2637, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cvx_600.setStatus("current")
_Aptis_cards_ObjectIdentity = ObjectIdentity
aptis_cards = _Aptis_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2637, 1, 3)
)
if mibBuilder.loadTexts:
    aptis_cards.setStatus("deprecated")
_Assy_725_ObjectIdentity = ObjectIdentity
assy_725 = _Assy_725_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2637, 1, 3, 725)
)
if mibBuilder.loadTexts:
    assy_725.setStatus("deprecated")
_Mam_main_board_ObjectIdentity = ObjectIdentity
mam_main_board = _Mam_main_board_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2637, 1, 3, 725, 3)
)
if mibBuilder.loadTexts:
    mam_main_board.setStatus("deprecated")
_Dmm_board_ObjectIdentity = ObjectIdentity
dmm_board = _Dmm_board_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2637, 1, 3, 725, 4)
)
if mibBuilder.loadTexts:
    dmm_board.setStatus("deprecated")
_Tsc_main_board_ObjectIdentity = ObjectIdentity
tsc_main_board = _Tsc_main_board_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2637, 1, 3, 725, 5)
)
if mibBuilder.loadTexts:
    tsc_main_board.setStatus("deprecated")
_Assy_750_ObjectIdentity = ObjectIdentity
assy_750 = _Assy_750_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2637, 1, 3, 750)
)
if mibBuilder.loadTexts:
    assy_750.setStatus("deprecated")
_Aptis_components_ObjectIdentity = ObjectIdentity
aptis_components = _Aptis_components_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2637, 1, 4)
)
if mibBuilder.loadTexts:
    aptis_components.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APTIS-REG-MIB",
    **{"aptis-modules": aptis_modules,
       "aptisRegModule": aptisRegModule,
       "aptis-systems": aptis_systems,
       "cvx": cvx,
       "cvx-1800": cvx_1800,
       "cvx-600": cvx_600,
       "aptis-cards": aptis_cards,
       "assy-725": assy_725,
       "mam-main-board": mam_main_board,
       "dmm-board": dmm_board,
       "tsc-main-board": tsc_main_board,
       "assy-750": assy_750,
       "aptis-components": aptis_components}
)
