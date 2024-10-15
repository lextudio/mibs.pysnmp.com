# SNMP MIB module (PAN-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PAN-PRODUCTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:30 2024
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

(panModules,
 panProductsMibs) = mibBuilder.importSymbols(
    "PAN-GLOBAL-REG",
    "panModules",
    "panProductsMibs")

(TcChassisType,) = mibBuilder.importSymbols(
    "PAN-GLOBAL-TC",
    "TcChassisType")

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

panProductsMibsModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 1, 1, 4)
)
panProductsMibsModule.setRevisions(
        ("2013-04-15 16:50",
         "2011-02-09 16:10")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PanPA_4050_ObjectIdentity = ObjectIdentity
panPA_4050 = _PanPA_4050_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 1)
)
if mibBuilder.loadTexts:
    panPA_4050.setStatus("current")
_PanPA_4020_ObjectIdentity = ObjectIdentity
panPA_4020 = _PanPA_4020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 2)
)
if mibBuilder.loadTexts:
    panPA_4020.setStatus("current")
_PanPA_2050_ObjectIdentity = ObjectIdentity
panPA_2050 = _PanPA_2050_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 3)
)
if mibBuilder.loadTexts:
    panPA_2050.setStatus("current")
_PanPA_2020_ObjectIdentity = ObjectIdentity
panPA_2020 = _PanPA_2020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 4)
)
if mibBuilder.loadTexts:
    panPA_2020.setStatus("current")
_PanPA_4060_ObjectIdentity = ObjectIdentity
panPA_4060 = _PanPA_4060_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 5)
)
if mibBuilder.loadTexts:
    panPA_4060.setStatus("current")
_PanPA_500_ObjectIdentity = ObjectIdentity
panPA_500 = _PanPA_500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 6)
)
if mibBuilder.loadTexts:
    panPA_500.setStatus("current")
_PanPanorama_ObjectIdentity = ObjectIdentity
panPanorama = _PanPanorama_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 7)
)
if mibBuilder.loadTexts:
    panPanorama.setStatus("current")
_PanPA_5060_ObjectIdentity = ObjectIdentity
panPA_5060 = _PanPA_5060_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 8)
)
if mibBuilder.loadTexts:
    panPA_5060.setStatus("current")
_PanPA_5050_ObjectIdentity = ObjectIdentity
panPA_5050 = _PanPA_5050_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 9)
)
if mibBuilder.loadTexts:
    panPA_5050.setStatus("current")
_PanPA_5020_ObjectIdentity = ObjectIdentity
panPA_5020 = _PanPA_5020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 11)
)
if mibBuilder.loadTexts:
    panPA_5020.setStatus("current")
_PanPA_200_ObjectIdentity = ObjectIdentity
panPA_200 = _PanPA_200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 12)
)
if mibBuilder.loadTexts:
    panPA_200.setStatus("current")
_PanPA_3050_ObjectIdentity = ObjectIdentity
panPA_3050 = _PanPA_3050_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 17)
)
if mibBuilder.loadTexts:
    panPA_3050.setStatus("current")
_PanPA_3020_ObjectIdentity = ObjectIdentity
panPA_3020 = _PanPA_3020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 18)
)
if mibBuilder.loadTexts:
    panPA_3020.setStatus("current")
_PanPA_VM_ObjectIdentity = ObjectIdentity
panPA_VM = _PanPA_VM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 29)
)
if mibBuilder.loadTexts:
    panPA_VM.setStatus("current")
_PanM_100_ObjectIdentity = ObjectIdentity
panM_100 = _PanM_100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 30)
)
if mibBuilder.loadTexts:
    panM_100.setStatus("current")
_PanPA_7050_ObjectIdentity = ObjectIdentity
panPA_7050 = _PanPA_7050_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 31)
)
if mibBuilder.loadTexts:
    panPA_7050.setStatus("current")
_PanGP_100_ObjectIdentity = ObjectIdentity
panGP_100 = _PanGP_100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 32)
)
if mibBuilder.loadTexts:
    panGP_100.setStatus("current")
_PanWF_500_ObjectIdentity = ObjectIdentity
panWF_500 = _PanWF_500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 33)
)
if mibBuilder.loadTexts:
    panWF_500.setStatus("current")
_PanProcessingCards_ObjectIdentity = ObjectIdentity
panProcessingCards = _PanProcessingCards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 100)
)
if mibBuilder.loadTexts:
    panProcessingCards.setStatus("current")
_PanPA_7000_SMC_ObjectIdentity = ObjectIdentity
panPA_7000_SMC = _PanPA_7000_SMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 100, 1)
)
if mibBuilder.loadTexts:
    panPA_7000_SMC.setStatus("current")
_PanPA_7000_LPC_ObjectIdentity = ObjectIdentity
panPA_7000_LPC = _PanPA_7000_LPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 100, 2)
)
if mibBuilder.loadTexts:
    panPA_7000_LPC.setStatus("current")
_PanPA_7000_20G_NPC_ObjectIdentity = ObjectIdentity
panPA_7000_20G_NPC = _PanPA_7000_20G_NPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 100, 3)
)
if mibBuilder.loadTexts:
    panPA_7000_20G_NPC.setStatus("current")
_PanFans_ObjectIdentity = ObjectIdentity
panFans = _PanFans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 101)
)
if mibBuilder.loadTexts:
    panFans.setStatus("current")
_PanPowerSupplies_ObjectIdentity = ObjectIdentity
panPowerSupplies = _PanPowerSupplies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 102)
)
if mibBuilder.loadTexts:
    panPowerSupplies.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PAN-PRODUCTS-MIB",
    **{"panProductsMibsModule": panProductsMibsModule,
       "panPA-4050": panPA_4050,
       "panPA-4020": panPA_4020,
       "panPA-2050": panPA_2050,
       "panPA-2020": panPA_2020,
       "panPA-4060": panPA_4060,
       "panPA-500": panPA_500,
       "panPanorama": panPanorama,
       "panPA-5060": panPA_5060,
       "panPA-5050": panPA_5050,
       "panPA-5020": panPA_5020,
       "panPA-200": panPA_200,
       "panPA-3050": panPA_3050,
       "panPA-3020": panPA_3020,
       "panPA-VM": panPA_VM,
       "panM-100": panM_100,
       "panPA-7050": panPA_7050,
       "panGP-100": panGP_100,
       "panWF-500": panWF_500,
       "panProcessingCards": panProcessingCards,
       "panPA-7000-SMC": panPA_7000_SMC,
       "panPA-7000-LPC": panPA_7000_LPC,
       "panPA-7000-20G-NPC": panPA_7000_20G_NPC,
       "panFans": panFans,
       "panPowerSupplies": panPowerSupplies}
)
