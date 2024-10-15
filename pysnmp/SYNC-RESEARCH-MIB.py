# SNMP MIB module (SYNC-RESEARCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYNC-RESEARCH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:58 2024
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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SyncResearch_ObjectIdentity = ObjectIdentity
syncResearch = _SyncResearch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485)
)
_SyncResearchAgent_ObjectIdentity = ObjectIdentity
syncResearchAgent = _SyncResearchAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1)
)
_SyncProducts_ObjectIdentity = ObjectIdentity
syncProducts = _SyncProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1)
)
_Boundary_ObjectIdentity = ObjectIdentity
boundary = _Boundary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1)
)
_SyncCN2R2b_ObjectIdentity = ObjectIdentity
syncCN2R2b = _SyncCN2R2b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 1)
)
_SyncFN2R2b_ObjectIdentity = ObjectIdentity
syncFN2R2b = _SyncFN2R2b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 2)
)
_SyncCN4R2b_ObjectIdentity = ObjectIdentity
syncCN4R2b = _SyncCN4R2b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 3)
)
_SyncFN4R2b_ObjectIdentity = ObjectIdentity
syncFN4R2b = _SyncFN4R2b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 4)
)
_SyncQN4R2b_ObjectIdentity = ObjectIdentity
syncQN4R2b = _SyncQN4R2b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 5)
)
_SyncCN4R3b_ObjectIdentity = ObjectIdentity
syncCN4R3b = _SyncCN4R3b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 6)
)
_SyncFN4R3b_ObjectIdentity = ObjectIdentity
syncFN4R3b = _SyncFN4R3b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 7)
)
_SyncQN4R3b_ObjectIdentity = ObjectIdentity
syncQN4R3b = _SyncQN4R3b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 8)
)
_SyncCN4R4b_ObjectIdentity = ObjectIdentity
syncCN4R4b = _SyncCN4R4b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 9)
)
_SyncFN4R4b_ObjectIdentity = ObjectIdentity
syncFN4R4b = _SyncFN4R4b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 10)
)
_SyncQN4R4b_ObjectIdentity = ObjectIdentity
syncQN4R4b = _SyncQN4R4b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 11)
)
_SyncCN4R4bu_ObjectIdentity = ObjectIdentity
syncCN4R4bu = _SyncCN4R4bu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 12)
)
_SyncFN4R4bu_ObjectIdentity = ObjectIdentity
syncFN4R4bu = _SyncFN4R4bu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 13)
)
_SyncQN4R4bu_ObjectIdentity = ObjectIdentity
syncQN4R4bu = _SyncQN4R4bu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 14)
)
_SyncCN4R4du_ObjectIdentity = ObjectIdentity
syncCN4R4du = _SyncCN4R4du_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 15)
)
_SyncFN4R4du_ObjectIdentity = ObjectIdentity
syncFN4R4du = _SyncFN4R4du_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 16)
)
_SyncQN4R4du_ObjectIdentity = ObjectIdentity
syncQN4R4du = _SyncQN4R4du_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 17)
)
_SyncCN2R2du_ObjectIdentity = ObjectIdentity
syncCN2R2du = _SyncCN2R2du_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 18)
)
_SyncFN2R2du_ObjectIdentity = ObjectIdentity
syncFN2R2du = _SyncFN2R2du_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 19)
)
_SyncCN3R4bu_ObjectIdentity = ObjectIdentity
syncCN3R4bu = _SyncCN3R4bu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 20)
)
_SyncFN3R4bu_ObjectIdentity = ObjectIdentity
syncFN3R4bu = _SyncFN3R4bu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 21)
)
_SyncCN3R4du_ObjectIdentity = ObjectIdentity
syncCN3R4du = _SyncCN3R4du_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 22)
)
_SyncFN3R4du_ObjectIdentity = ObjectIdentity
syncFN3R4du = _SyncFN3R4du_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 23)
)
_SyncCN4R5b_ObjectIdentity = ObjectIdentity
syncCN4R5b = _SyncCN4R5b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 24)
)
_SyncFN4R5b_ObjectIdentity = ObjectIdentity
syncFN4R5b = _SyncFN4R5b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 25)
)
_SyncQN4R5b_ObjectIdentity = ObjectIdentity
syncQN4R5b = _SyncQN4R5b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 26)
)
_SyncCN4R5bu_ObjectIdentity = ObjectIdentity
syncCN4R5bu = _SyncCN4R5bu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 27)
)
_SyncFN4R5bu_ObjectIdentity = ObjectIdentity
syncFN4R5bu = _SyncFN4R5bu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 28)
)
_SyncQN4R5bu_ObjectIdentity = ObjectIdentity
syncQN4R5bu = _SyncQN4R5bu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 29)
)
_SyncCN4R5du_ObjectIdentity = ObjectIdentity
syncCN4R5du = _SyncCN4R5du_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 30)
)
_SyncFN4R5du_ObjectIdentity = ObjectIdentity
syncFN4R5du = _SyncFN4R5du_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 31)
)
_SyncQN4R5du_ObjectIdentity = ObjectIdentity
syncQN4R5du = _SyncQN4R5du_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 32)
)
_SyncFN5R5du_ObjectIdentity = ObjectIdentity
syncFN5R5du = _SyncFN5R5du_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 33)
)
_SyncBC4R5b_ObjectIdentity = ObjectIdentity
syncBC4R5b = _SyncBC4R5b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 34)
)
_SyncBF4R5b_ObjectIdentity = ObjectIdentity
syncBF4R5b = _SyncBF4R5b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 35)
)
_SyncBF3R5b_ObjectIdentity = ObjectIdentity
syncBF3R5b = _SyncBF3R5b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 36)
)
_SyncBF5R5b_ObjectIdentity = ObjectIdentity
syncBF5R5b = _SyncBF5R5b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 37)
)
_SyncFN3R5du_ObjectIdentity = ObjectIdentity
syncFN3R5du = _SyncFN3R5du_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 38)
)
_SyncCN3R5du_ObjectIdentity = ObjectIdentity
syncCN3R5du = _SyncCN3R5du_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 39)
)
_SyncCN5R5du_ObjectIdentity = ObjectIdentity
syncCN5R5du = _SyncCN5R5du_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 40)
)
_SyncBF3R5_ObjectIdentity = ObjectIdentity
syncBF3R5 = _SyncBF3R5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 41)
)
_SyncBC3R5_ObjectIdentity = ObjectIdentity
syncBC3R5 = _SyncBC3R5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 42)
)
_SyncBF4R5_ObjectIdentity = ObjectIdentity
syncBF4R5 = _SyncBF4R5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 43)
)
_SyncBC4R5_ObjectIdentity = ObjectIdentity
syncBC4R5 = _SyncBC4R5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 44)
)
_SyncBF5R5_ObjectIdentity = ObjectIdentity
syncBF5R5 = _SyncBF5R5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 45)
)
_SyncBC5R5_ObjectIdentity = ObjectIdentity
syncBC5R5 = _SyncBC5R5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 1, 46)
)
_CentralSite_ObjectIdentity = ObjectIdentity
centralSite = _CentralSite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 2)
)
_SyncCN4R2c_ObjectIdentity = ObjectIdentity
syncCN4R2c = _SyncCN4R2c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 2, 1)
)
_SyncFN4R2c_ObjectIdentity = ObjectIdentity
syncFN4R2c = _SyncFN4R2c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 2, 2)
)
_SyncQN4R2c_ObjectIdentity = ObjectIdentity
syncQN4R2c = _SyncQN4R2c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 2, 3)
)
_SyncCN4R3c_ObjectIdentity = ObjectIdentity
syncCN4R3c = _SyncCN4R3c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 2, 4)
)
_SyncFN4R3c_ObjectIdentity = ObjectIdentity
syncFN4R3c = _SyncFN4R3c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 2, 5)
)
_SyncQN4R3c_ObjectIdentity = ObjectIdentity
syncQN4R3c = _SyncQN4R3c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 2, 6)
)
_SyncCN4R4u_ObjectIdentity = ObjectIdentity
syncCN4R4u = _SyncCN4R4u_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 2, 7)
)
_SyncFN4R4u_ObjectIdentity = ObjectIdentity
syncFN4R4u = _SyncFN4R4u_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 2, 8)
)
_SyncQN4R4u_ObjectIdentity = ObjectIdentity
syncQN4R4u = _SyncQN4R4u_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 1, 2, 9)
)
_OemProducts_ObjectIdentity = ObjectIdentity
oemProducts = _OemProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2)
)
_ThreeCom_ObjectIdentity = ObjectIdentity
threeCom = _ThreeCom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 1)
)
_LinkConverter_ObjectIdentity = ObjectIdentity
linkConverter = _LinkConverter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 1, 1)
)
_LinkConverter2_ObjectIdentity = ObjectIdentity
linkConverter2 = _LinkConverter2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 1, 2)
)
_Lc2EN2port_ObjectIdentity = ObjectIdentity
lc2EN2port = _Lc2EN2port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 1, 3)
)
_Lc2EN4port_ObjectIdentity = ObjectIdentity
lc2EN4port = _Lc2EN4port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 1, 4)
)
_Lc2TR2port_ObjectIdentity = ObjectIdentity
lc2TR2port = _Lc2TR2port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 1, 5)
)
_Lc2TR6port_ObjectIdentity = ObjectIdentity
lc2TR6port = _Lc2TR6port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 1, 6)
)
_CableTron_ObjectIdentity = ObjectIdentity
cableTron = _CableTron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 2)
)
_OemSNACXR2C_ObjectIdentity = ObjectIdentity
oemSNACXR2C = _OemSNACXR2C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 2, 1)
)
_OemSNACXR2W_ObjectIdentity = ObjectIdentity
oemSNACXR2W = _OemSNACXR2W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 2, 2)
)
_OemSNACMR2C_ObjectIdentity = ObjectIdentity
oemSNACMR2C = _OemSNACMR2C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 2, 3)
)
_OemSNACMR2W_ObjectIdentity = ObjectIdentity
oemSNACMR2W = _OemSNACMR2W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 2, 4)
)
_OemSNACMIM2_ObjectIdentity = ObjectIdentity
oemSNACMIM2 = _OemSNACMIM2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 2, 5)
)
_OemSNACXR2Q_ObjectIdentity = ObjectIdentity
oemSNACXR2Q = _OemSNACXR2Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 2, 6)
)
_OemSNACMR2Q_ObjectIdentity = ObjectIdentity
oemSNACMR2Q = _OemSNACMR2Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 2, 7)
)
_OemSNACXR3C_ObjectIdentity = ObjectIdentity
oemSNACXR3C = _OemSNACXR3C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 2, 8)
)
_OemSNACXR3W_ObjectIdentity = ObjectIdentity
oemSNACXR3W = _OemSNACXR3W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 2, 9)
)
_OemSNACMR3C_ObjectIdentity = ObjectIdentity
oemSNACMR3C = _OemSNACMR3C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 2, 10)
)
_OemSNACMR3W_ObjectIdentity = ObjectIdentity
oemSNACMR3W = _OemSNACMR3W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 2, 11)
)
_OemSNACXR3Q_ObjectIdentity = ObjectIdentity
oemSNACXR3Q = _OemSNACXR3Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 2, 12)
)
_OemSNACMR3Q_ObjectIdentity = ObjectIdentity
oemSNACMR3Q = _OemSNACMR3Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 2, 13)
)
_OemSNACXR4C_ObjectIdentity = ObjectIdentity
oemSNACXR4C = _OemSNACXR4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 2, 14)
)
_OemSNACXR4W_ObjectIdentity = ObjectIdentity
oemSNACXR4W = _OemSNACXR4W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 2, 15)
)
_OemSNACMR4C_ObjectIdentity = ObjectIdentity
oemSNACMR4C = _OemSNACMR4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 2, 16)
)
_OemSNACMR4W_ObjectIdentity = ObjectIdentity
oemSNACMR4W = _OemSNACMR4W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 2, 17)
)
_OemSNACXR4Q_ObjectIdentity = ObjectIdentity
oemSNACXR4Q = _OemSNACXR4Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 2, 18)
)
_OemSNACMR4Q_ObjectIdentity = ObjectIdentity
oemSNACMR4Q = _OemSNACMR4Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 2, 19)
)
_Chipcom_ObjectIdentity = ObjectIdentity
chipcom = _Chipcom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 3)
)
_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 4)
)
_Oem2490R22F_ObjectIdentity = ObjectIdentity
oem2490R22F = _Oem2490R22F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 4, 1)
)
_Oem2490R22C_ObjectIdentity = ObjectIdentity
oem2490R22C = _Oem2490R22C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 4, 2)
)
_Oem22181FR4_ObjectIdentity = ObjectIdentity
oem22181FR4 = _Oem22181FR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 4, 3)
)
_Oem22181CR4_ObjectIdentity = ObjectIdentity
oem22181CR4 = _Oem22181CR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 4, 4)
)
_Oem22183FR4_ObjectIdentity = ObjectIdentity
oem22183FR4 = _Oem22183FR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 4, 5)
)
_Oem22183CR4_ObjectIdentity = ObjectIdentity
oem22183CR4 = _Oem22183CR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 4, 6)
)
_Oem22181FR5_ObjectIdentity = ObjectIdentity
oem22181FR5 = _Oem22181FR5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 4, 7)
)
_Oem22181CR5_ObjectIdentity = ObjectIdentity
oem22181CR5 = _Oem22181CR5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 4, 8)
)
_Oem22183FR5_ObjectIdentity = ObjectIdentity
oem22183FR5 = _Oem22183FR5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 4, 9)
)
_Oem22183CR5_ObjectIdentity = ObjectIdentity
oem22183CR5 = _Oem22183CR5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 4, 10)
)
_Oem22185FR5_ObjectIdentity = ObjectIdentity
oem22185FR5 = _Oem22185FR5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 4, 11)
)
_Oem22185CR5_ObjectIdentity = ObjectIdentity
oem22185CR5 = _Oem22185CR5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 4, 12)
)
_Oem22183BF5_ObjectIdentity = ObjectIdentity
oem22183BF5 = _Oem22183BF5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 4, 13)
)
_Oem22183BC5_ObjectIdentity = ObjectIdentity
oem22183BC5 = _Oem22183BC5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 4, 14)
)
_Oem22184BF5_ObjectIdentity = ObjectIdentity
oem22184BF5 = _Oem22184BF5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 4, 15)
)
_Oem22184BC5_ObjectIdentity = ObjectIdentity
oem22184BC5 = _Oem22184BC5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 4, 16)
)
_Oem22185BF5_ObjectIdentity = ObjectIdentity
oem22185BF5 = _Oem22185BF5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 4, 17)
)
_Oem22185BC5_ObjectIdentity = ObjectIdentity
oem22185BC5 = _Oem22185BC5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 1, 2, 4, 18)
)
_SrCommTrapGroup_ObjectIdentity = ObjectIdentity
srCommTrapGroup = _SrCommTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 2)
)


class _CommCount_Type(Integer32):
    """Custom type commCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_CommCount_Type.__name__ = "Integer32"
_CommCount_Object = MibScalar
commCount = _CommCount_Object(
    (1, 3, 6, 1, 4, 1, 485, 2, 1),
    _CommCount_Type()
)
commCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commCount.setStatus("mandatory")
_CommTable_Object = MibTable
commTable = _CommTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 2, 2)
)
if mibBuilder.loadTexts:
    commTable.setStatus("mandatory")
_CommEntry_Object = MibTableRow
commEntry = _CommEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 2, 2, 1)
)
commEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "commIndex"),
)
if mibBuilder.loadTexts:
    commEntry.setStatus("mandatory")
_CommIndex_Type = Integer32
_CommIndex_Object = MibTableColumn
commIndex = _CommIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 2, 2, 1, 1),
    _CommIndex_Type()
)
commIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commIndex.setStatus("mandatory")
_CommName_Type = OctetString
_CommName_Object = MibTableColumn
commName = _CommName_Object(
    (1, 3, 6, 1, 4, 1, 485, 2, 2, 1, 2),
    _CommName_Type()
)
commName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commName.setStatus("mandatory")


class _CommTrap_Type(Integer32):
    """Custom type commTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trapoff", 1),
          ("trapon", 2))
    )


_CommTrap_Type.__name__ = "Integer32"
_CommTrap_Object = MibTableColumn
commTrap = _CommTrap_Object(
    (1, 3, 6, 1, 4, 1, 485, 2, 2, 1, 3),
    _CommTrap_Type()
)
commTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commTrap.setStatus("mandatory")
_CommIPAddr_Type = IpAddress
_CommIPAddr_Object = MibTableColumn
commIPAddr = _CommIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 485, 2, 2, 1, 4),
    _CommIPAddr_Type()
)
commIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commIPAddr.setStatus("mandatory")
_CommMACAddr_Type = OctetString
_CommMACAddr_Object = MibTableColumn
commMACAddr = _CommMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 485, 2, 2, 1, 5),
    _CommMACAddr_Type()
)
commMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commMACAddr.setStatus("mandatory")


class _CommAccess_Type(Integer32):
    """Custom type commAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noAccess", 1),
          ("ro", 2),
          ("rw", 3),
          ("su", 4))
    )


_CommAccess_Type.__name__ = "Integer32"
_CommAccess_Object = MibTableColumn
commAccess = _CommAccess_Object(
    (1, 3, 6, 1, 4, 1, 485, 2, 2, 1, 6),
    _CommAccess_Type()
)
commAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commAccess.setStatus("mandatory")
_SrNodeGroup_ObjectIdentity = ObjectIdentity
srNodeGroup = _SrNodeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3)
)
_NodeUnitGroup_ObjectIdentity = ObjectIdentity
nodeUnitGroup = _NodeUnitGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 1)
)
_UnitControlGroup_ObjectIdentity = ObjectIdentity
unitControlGroup = _UnitControlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 1)
)


class _UnitRestart_Type(Integer32):
    """Custom type unitRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dummy-restart", 2),
          ("restart-unit", 1))
    )


_UnitRestart_Type.__name__ = "Integer32"
_UnitRestart_Object = MibScalar
unitRestart = _UnitRestart_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 1, 1),
    _UnitRestart_Type()
)
unitRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitRestart.setStatus("mandatory")


class _DumpOnRestart_Type(Integer32):
    """Custom type dumpOnRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-dump", 2),
          ("dump-on-start", 1))
    )


_DumpOnRestart_Type.__name__ = "Integer32"
_DumpOnRestart_Object = MibScalar
dumpOnRestart = _DumpOnRestart_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 1, 2),
    _DumpOnRestart_Type()
)
dumpOnRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dumpOnRestart.setStatus("mandatory")


class _InitiateInstall_Type(Integer32):
    """Custom type initiateInstall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dummy-install", 2),
          ("start-install", 1))
    )


_InitiateInstall_Type.__name__ = "Integer32"
_InitiateInstall_Object = MibScalar
initiateInstall = _InitiateInstall_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 1, 3),
    _InitiateInstall_Type()
)
initiateInstall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    initiateInstall.setStatus("mandatory")


class _InitializeStats_Type(Integer32):
    """Custom type initializeStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dummy-init-stats", 2),
          ("init-stats", 1))
    )


_InitializeStats_Type.__name__ = "Integer32"
_InitializeStats_Object = MibScalar
initializeStats = _InitializeStats_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 1, 4),
    _InitializeStats_Type()
)
initializeStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    initializeStats.setStatus("mandatory")


class _ClearDump_Type(Integer32):
    """Custom type clearDump based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear-dump-file", 1),
          ("dummy-clear", 2))
    )


_ClearDump_Type.__name__ = "Integer32"
_ClearDump_Object = MibScalar
clearDump = _ClearDump_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 1, 5),
    _ClearDump_Type()
)
clearDump.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearDump.setStatus("mandatory")


class _AcknowledgeAllStatuses_Type(Integer32):
    """Custom type acknowledgeAllStatuses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AcknowledgeAllStatuses_Type.__name__ = "Integer32"
_AcknowledgeAllStatuses_Object = MibScalar
acknowledgeAllStatuses = _AcknowledgeAllStatuses_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 1, 6),
    _AcknowledgeAllStatuses_Type()
)
acknowledgeAllStatuses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acknowledgeAllStatuses.setStatus("mandatory")


class _ConsolidatedUnitStatus_Type(Integer32):
    """Custom type consolidatedUnitStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("critical", 9),
          ("disabled", 4),
          ("informational", 3),
          ("major", 8),
          ("marginal", 5),
          ("minor", 7),
          ("normal", 2),
          ("unknown", 1),
          ("warning", 6))
    )


_ConsolidatedUnitStatus_Type.__name__ = "Integer32"
_ConsolidatedUnitStatus_Object = MibScalar
consolidatedUnitStatus = _ConsolidatedUnitStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 1, 7),
    _ConsolidatedUnitStatus_Type()
)
consolidatedUnitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consolidatedUnitStatus.setStatus("mandatory")


class _HomeDialBackup_Type(Integer32):
    """Custom type homeDialBackup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dummy-home", 2),
          ("home-dial-backup", 1))
    )


_HomeDialBackup_Type.__name__ = "Integer32"
_HomeDialBackup_Object = MibScalar
homeDialBackup = _HomeDialBackup_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 1, 8),
    _HomeDialBackup_Type()
)
homeDialBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    homeDialBackup.setStatus("mandatory")
_UnitStatusGroup_ObjectIdentity = ObjectIdentity
unitStatusGroup = _UnitStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 2)
)


class _UnitModel_Type(Integer32):
    """Custom type unitModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("boundary", 1),
          ("chipcomPED", 3),
          ("ibm", 10),
          ("ibm3600", 12),
          ("lic", 2),
          ("linkConverter", 6),
          ("linkConverterII", 9),
          ("microMac", 5),
          ("snacMIM", 4),
          ("sync3600", 11),
          ("universal-boundary", 7),
          ("universal-desktop", 8))
    )


_UnitModel_Type.__name__ = "Integer32"
_UnitModel_Object = MibScalar
unitModel = _UnitModel_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 2, 1),
    _UnitModel_Type()
)
unitModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitModel.setStatus("mandatory")


class _SoftwareVersion_Type(DisplayString):
    """Custom type softwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_SoftwareVersion_Type.__name__ = "DisplayString"
_SoftwareVersion_Object = MibScalar
softwareVersion = _SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 2, 2),
    _SoftwareVersion_Type()
)
softwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareVersion.setStatus("mandatory")


class _ProductType_Type(DisplayString):
    """Custom type productType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_ProductType_Type.__name__ = "DisplayString"
_ProductType_Object = MibScalar
productType = _ProductType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 2, 3),
    _ProductType_Type()
)
productType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productType.setStatus("mandatory")
_MaxPortNumber_Type = Integer32
_MaxPortNumber_Object = MibScalar
maxPortNumber = _MaxPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 2, 4),
    _MaxPortNumber_Type()
)
maxPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxPortNumber.setStatus("mandatory")
_MaxPU_Type = Integer32
_MaxPU_Object = MibScalar
maxPU = _MaxPU_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 2, 5),
    _MaxPU_Type()
)
maxPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxPU.setStatus("mandatory")
_MaxSession_Type = Integer32
_MaxSession_Object = MibScalar
maxSession = _MaxSession_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 2, 6),
    _MaxSession_Type()
)
maxSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxSession.setStatus("mandatory")
_MaxDevice_Type = Integer32
_MaxDevice_Object = MibScalar
maxDevice = _MaxDevice_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 2, 7),
    _MaxDevice_Type()
)
maxDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxDevice.setStatus("mandatory")


class _MsBoardType_Type(Integer32):
    """Custom type msBoardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              16,
              17,
              18,
              22,
              23,
              26,
              30)
        )
    )
    namedValues = NamedValues(
        *(("not-expected", 1),
          ("rs422-RS232", 23),
          ("two-port-RS232", 16),
          ("two-port-RS422", 17),
          ("two-port-V35", 18),
          ("two-port-iusc-RS232", 30),
          ("two-port-universal", 26),
          ("v35-RS232", 22))
    )


_MsBoardType_Type.__name__ = "Integer32"
_MsBoardType_Object = MibScalar
msBoardType = _MsBoardType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 2, 8),
    _MsBoardType_Type()
)
msBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msBoardType.setStatus("mandatory")


class _MsExtBoardType_Type(Integer32):
    """Custom type msExtBoardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              19,
              20,
              21,
              24,
              25,
              27,
              28,
              29)
        )
    )
    namedValues = NamedValues(
        *(("four-port-universal", 28),
          ("not-present", 1),
          ("six-port-universal", 29),
          ("two-port-RS232", 19),
          ("two-port-RS422", 20),
          ("two-port-V35", 21),
          ("two-port-hspeedRS232", 24),
          ("two-port-hspeedV35", 25),
          ("two-port-universal", 27))
    )


_MsExtBoardType_Type.__name__ = "Integer32"
_MsExtBoardType_Object = MibScalar
msExtBoardType = _MsExtBoardType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 2, 9),
    _MsExtBoardType_Type()
)
msExtBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msExtBoardType.setStatus("mandatory")


class _DumpFileStatus_Type(Integer32):
    """Custom type dumpFileStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dump-available", 2),
          ("none", 1))
    )


_DumpFileStatus_Type.__name__ = "Integer32"
_DumpFileStatus_Object = MibScalar
dumpFileStatus = _DumpFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 2, 10),
    _DumpFileStatus_Type()
)
dumpFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dumpFileStatus.setStatus("mandatory")


class _DumpFileName_Type(DisplayString):
    """Custom type dumpFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 11),
    )


_DumpFileName_Type.__name__ = "DisplayString"
_DumpFileName_Object = MibScalar
dumpFileName = _DumpFileName_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 2, 11),
    _DumpFileName_Type()
)
dumpFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dumpFileName.setStatus("mandatory")


class _UnitSerialNumber_Type(DisplayString):
    """Custom type unitSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_UnitSerialNumber_Type.__name__ = "DisplayString"
_UnitSerialNumber_Object = MibScalar
unitSerialNumber = _UnitSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 2, 12),
    _UnitSerialNumber_Type()
)
unitSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitSerialNumber.setStatus("mandatory")


class _ExpansionSerialNumber_Type(DisplayString):
    """Custom type expansionSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_ExpansionSerialNumber_Type.__name__ = "DisplayString"
_ExpansionSerialNumber_Object = MibScalar
expansionSerialNumber = _ExpansionSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 2, 13),
    _ExpansionSerialNumber_Type()
)
expansionSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expansionSerialNumber.setStatus("mandatory")


class _RomVersion_Type(DisplayString):
    """Custom type romVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_RomVersion_Type.__name__ = "DisplayString"
_RomVersion_Object = MibScalar
romVersion = _RomVersion_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 2, 14),
    _RomVersion_Type()
)
romVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    romVersion.setStatus("mandatory")


class _ProcessorType_Type(Integer32):
    """Custom type processorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("i286", 1),
          ("i386", 2),
          ("i486DX", 4),
          ("i486DX-2", 5),
          ("i486DX-4", 6),
          ("i486SX", 3))
    )


_ProcessorType_Type.__name__ = "Integer32"
_ProcessorType_Object = MibScalar
processorType = _ProcessorType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 2, 15),
    _ProcessorType_Type()
)
processorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorType.setStatus("mandatory")


class _ChassisSlot_Type(Integer32):
    """Custom type chassisSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_ChassisSlot_Type.__name__ = "Integer32"
_ChassisSlot_Object = MibScalar
chassisSlot = _ChassisSlot_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 2, 16),
    _ChassisSlot_Type()
)
chassisSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSlot.setStatus("mandatory")


class _LastTrapSeqNumber_Type(Integer32):
    """Custom type lastTrapSeqNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LastTrapSeqNumber_Type.__name__ = "Integer32"
_LastTrapSeqNumber_Object = MibScalar
lastTrapSeqNumber = _LastTrapSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 2, 17),
    _LastTrapSeqNumber_Type()
)
lastTrapSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastTrapSeqNumber.setStatus("mandatory")


class _LastInstallErrCode_Type(Integer32):
    """Custom type lastInstallErrCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_LastInstallErrCode_Type.__name__ = "Integer32"
_LastInstallErrCode_Object = MibScalar
lastInstallErrCode = _LastInstallErrCode_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 2, 18),
    _LastInstallErrCode_Type()
)
lastInstallErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastInstallErrCode.setStatus("mandatory")


class _UnitPartNumber_Type(DisplayString):
    """Custom type unitPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_UnitPartNumber_Type.__name__ = "DisplayString"
_UnitPartNumber_Object = MibScalar
unitPartNumber = _UnitPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 2, 19),
    _UnitPartNumber_Type()
)
unitPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitPartNumber.setStatus("mandatory")


class _ExpansionPartNumber_Type(DisplayString):
    """Custom type expansionPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_ExpansionPartNumber_Type.__name__ = "DisplayString"
_ExpansionPartNumber_Object = MibScalar
expansionPartNumber = _ExpansionPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 2, 20),
    _ExpansionPartNumber_Type()
)
expansionPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expansionPartNumber.setStatus("mandatory")


class _Wan1BoardType_Type(Integer32):
    """Custom type wan1BoardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              31)
        )
    )
    namedValues = NamedValues(
        *(("dsu-csu", 31),
          ("not-present", 1))
    )


_Wan1BoardType_Type.__name__ = "Integer32"
_Wan1BoardType_Object = MibScalar
wan1BoardType = _Wan1BoardType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 2, 21),
    _Wan1BoardType_Type()
)
wan1BoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan1BoardType.setStatus("mandatory")


class _Wan2BoardType_Type(Integer32):
    """Custom type wan2BoardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              31,
              32)
        )
    )
    namedValues = NamedValues(
        *(("dsu-csu", 31),
          ("isdn", 32),
          ("not-present", 1))
    )


_Wan2BoardType_Type.__name__ = "Integer32"
_Wan2BoardType_Object = MibScalar
wan2BoardType = _Wan2BoardType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 2, 22),
    _Wan2BoardType_Type()
)
wan2BoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wan2BoardType.setStatus("mandatory")


class _PatchId_Type(DisplayString):
    """Custom type patchId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_PatchId_Type.__name__ = "DisplayString"
_PatchId_Object = MibScalar
patchId = _PatchId_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 2, 23),
    _PatchId_Type()
)
patchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    patchId.setStatus("mandatory")
_UnitConfigGroup_ObjectIdentity = ObjectIdentity
unitConfigGroup = _UnitConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 3)
)


class _UnitId_Type(DisplayString):
    """Custom type unitId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_UnitId_Type.__name__ = "DisplayString"
_UnitId_Object = MibScalar
unitId = _UnitId_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 3, 1),
    _UnitId_Type()
)
unitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitId.setStatus("mandatory")


class _NmsSerialSpeed_Type(Integer32):
    """Custom type nmsSerialSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(12,
              24,
              48,
              96,
              192)
        )
    )
    namedValues = NamedValues(
        *(("speed1200", 12),
          ("speed19200", 192),
          ("speed2400", 24),
          ("speed4800", 48),
          ("speed9600", 96))
    )


_NmsSerialSpeed_Type.__name__ = "Integer32"
_NmsSerialSpeed_Object = MibScalar
nmsSerialSpeed = _NmsSerialSpeed_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 3, 2),
    _NmsSerialSpeed_Type()
)
nmsSerialSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsSerialSpeed.setStatus("mandatory")


class _SerialPortLogoffTimer_Type(Integer32):
    """Custom type serialPortLogoffTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_SerialPortLogoffTimer_Type.__name__ = "Integer32"
_SerialPortLogoffTimer_Object = MibScalar
serialPortLogoffTimer = _SerialPortLogoffTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 3, 3),
    _SerialPortLogoffTimer_Type()
)
serialPortLogoffTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortLogoffTimer.setStatus("mandatory")


class _CallRetryTimer_Type(Integer32):
    """Custom type callRetryTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 999),
    )


_CallRetryTimer_Type.__name__ = "Integer32"
_CallRetryTimer_Object = MibScalar
callRetryTimer = _CallRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 3, 4),
    _CallRetryTimer_Type()
)
callRetryTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callRetryTimer.setStatus("mandatory")


class _Password_Type(DisplayString):
    """Custom type password based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_Password_Type.__name__ = "DisplayString"
_Password_Object = MibScalar
password = _Password_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 3, 5),
    _Password_Type()
)
password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    password.setStatus("mandatory")


class _ConfigPassword_Type(DisplayString):
    """Custom type configPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_ConfigPassword_Type.__name__ = "DisplayString"
_ConfigPassword_Object = MibScalar
configPassword = _ConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 3, 6),
    _ConfigPassword_Type()
)
configPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPassword.setStatus("mandatory")


class _DateTimeField_Type(OctetString):
    """Custom type dateTimeField based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_DateTimeField_Type.__name__ = "OctetString"
_DateTimeField_Object = MibScalar
dateTimeField = _DateTimeField_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 3, 7),
    _DateTimeField_Type()
)
dateTimeField.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeField.setStatus("mandatory")


class _ConfigId_Type(DisplayString):
    """Custom type configId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_ConfigId_Type.__name__ = "DisplayString"
_ConfigId_Object = MibScalar
configId = _ConfigId_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 3, 8),
    _ConfigId_Type()
)
configId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configId.setStatus("mandatory")
_InternalMacAddress_Type = PhysAddress
_InternalMacAddress_Object = MibScalar
internalMacAddress = _InternalMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 3, 9),
    _InternalMacAddress_Type()
)
internalMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalMacAddress.setStatus("mandatory")


class _InternalRingNumber_Type(Integer32):
    """Custom type internalRingNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_InternalRingNumber_Type.__name__ = "Integer32"
_InternalRingNumber_Object = MibScalar
internalRingNumber = _InternalRingNumber_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 3, 10),
    _InternalRingNumber_Type()
)
internalRingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalRingNumber.setStatus("mandatory")


class _InternalBridgeNumber_Type(Integer32):
    """Custom type internalBridgeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_InternalBridgeNumber_Type.__name__ = "Integer32"
_InternalBridgeNumber_Object = MibScalar
internalBridgeNumber = _InternalBridgeNumber_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 3, 11),
    _InternalBridgeNumber_Type()
)
internalBridgeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalBridgeNumber.setStatus("mandatory")
_InternalMacAddress2_Type = PhysAddress
_InternalMacAddress2_Object = MibScalar
internalMacAddress2 = _InternalMacAddress2_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 3, 12),
    _InternalMacAddress2_Type()
)
internalMacAddress2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalMacAddress2.setStatus("mandatory")


class _InternalRingNumber2_Type(Integer32):
    """Custom type internalRingNumber2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_InternalRingNumber2_Type.__name__ = "Integer32"
_InternalRingNumber2_Object = MibScalar
internalRingNumber2 = _InternalRingNumber2_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 3, 13),
    _InternalRingNumber2_Type()
)
internalRingNumber2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalRingNumber2.setStatus("mandatory")
_AssociatedPortNumber2_Type = Integer32
_AssociatedPortNumber2_Object = MibScalar
associatedPortNumber2 = _AssociatedPortNumber2_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 3, 14),
    _AssociatedPortNumber2_Type()
)
associatedPortNumber2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    associatedPortNumber2.setStatus("mandatory")


class _AssociatedDLCI2_Type(Integer32):
    """Custom type associatedDLCI2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_AssociatedDLCI2_Type.__name__ = "Integer32"
_AssociatedDLCI2_Object = MibScalar
associatedDLCI2 = _AssociatedDLCI2_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 3, 15),
    _AssociatedDLCI2_Type()
)
associatedDLCI2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    associatedDLCI2.setStatus("mandatory")
_InternalMacAddress3_Type = PhysAddress
_InternalMacAddress3_Object = MibScalar
internalMacAddress3 = _InternalMacAddress3_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 3, 16),
    _InternalMacAddress3_Type()
)
internalMacAddress3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalMacAddress3.setStatus("mandatory")


class _InternalRingNumber3_Type(Integer32):
    """Custom type internalRingNumber3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_InternalRingNumber3_Type.__name__ = "Integer32"
_InternalRingNumber3_Object = MibScalar
internalRingNumber3 = _InternalRingNumber3_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 3, 17),
    _InternalRingNumber3_Type()
)
internalRingNumber3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalRingNumber3.setStatus("mandatory")
_AssociatedPortNumber3_Type = Integer32
_AssociatedPortNumber3_Object = MibScalar
associatedPortNumber3 = _AssociatedPortNumber3_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 3, 18),
    _AssociatedPortNumber3_Type()
)
associatedPortNumber3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    associatedPortNumber3.setStatus("mandatory")


class _AssociatedDLCI3_Type(Integer32):
    """Custom type associatedDLCI3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_AssociatedDLCI3_Type.__name__ = "Integer32"
_AssociatedDLCI3_Object = MibScalar
associatedDLCI3 = _AssociatedDLCI3_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 3, 19),
    _AssociatedDLCI3_Type()
)
associatedDLCI3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    associatedDLCI3.setStatus("mandatory")
_InternalMacAddress4_Type = PhysAddress
_InternalMacAddress4_Object = MibScalar
internalMacAddress4 = _InternalMacAddress4_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 3, 20),
    _InternalMacAddress4_Type()
)
internalMacAddress4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalMacAddress4.setStatus("mandatory")


class _InternalRingNumber4_Type(Integer32):
    """Custom type internalRingNumber4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_InternalRingNumber4_Type.__name__ = "Integer32"
_InternalRingNumber4_Object = MibScalar
internalRingNumber4 = _InternalRingNumber4_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 3, 21),
    _InternalRingNumber4_Type()
)
internalRingNumber4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalRingNumber4.setStatus("mandatory")
_AssociatedPortNumber4_Type = Integer32
_AssociatedPortNumber4_Object = MibScalar
associatedPortNumber4 = _AssociatedPortNumber4_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 3, 22),
    _AssociatedPortNumber4_Type()
)
associatedPortNumber4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    associatedPortNumber4.setStatus("mandatory")


class _AssociatedDLCI4_Type(Integer32):
    """Custom type associatedDLCI4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_AssociatedDLCI4_Type.__name__ = "Integer32"
_AssociatedDLCI4_Object = MibScalar
associatedDLCI4 = _AssociatedDLCI4_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 3, 23),
    _AssociatedDLCI4_Type()
)
associatedDLCI4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    associatedDLCI4.setStatus("mandatory")


class _IpInactivityTimer_Type(Integer32):
    """Custom type ipInactivityTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_IpInactivityTimer_Type.__name__ = "Integer32"
_IpInactivityTimer_Object = MibScalar
ipInactivityTimer = _IpInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 3, 24),
    _IpInactivityTimer_Type()
)
ipInactivityTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInactivityTimer.setStatus("mandatory")


class _ExcessBurstGovernor_Type(Integer32):
    """Custom type excessBurstGovernor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_ExcessBurstGovernor_Type.__name__ = "Integer32"
_ExcessBurstGovernor_Object = MibScalar
excessBurstGovernor = _ExcessBurstGovernor_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 3, 25),
    _ExcessBurstGovernor_Type()
)
excessBurstGovernor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excessBurstGovernor.setStatus("mandatory")


class _MeasurementPeriod_Type(Integer32):
    """Custom type measurementPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_MeasurementPeriod_Type.__name__ = "Integer32"
_MeasurementPeriod_Object = MibScalar
measurementPeriod = _MeasurementPeriod_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 3, 26),
    _MeasurementPeriod_Type()
)
measurementPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementPeriod.setStatus("mandatory")


class _MarkDEBit_Type(Integer32):
    """Custom type markDEBit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MarkDEBit_Type.__name__ = "Integer32"
_MarkDEBit_Object = MibScalar
markDEBit = _MarkDEBit_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 3, 27),
    _MarkDEBit_Type()
)
markDEBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    markDEBit.setStatus("mandatory")
_UnitStatisticsGroup_ObjectIdentity = ObjectIdentity
unitStatisticsGroup = _UnitStatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 4)
)
_NumberSamples_Type = Counter32
_NumberSamples_Object = MibScalar
numberSamples = _NumberSamples_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 4, 1),
    _NumberSamples_Type()
)
numberSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberSamples.setStatus("mandatory")
_SystemBufferFreeCounts_Type = Integer32
_SystemBufferFreeCounts_Object = MibScalar
systemBufferFreeCounts = _SystemBufferFreeCounts_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 4, 2),
    _SystemBufferFreeCounts_Type()
)
systemBufferFreeCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBufferFreeCounts.setStatus("mandatory")
_CpuIdleSumCounts_Type = Counter32
_CpuIdleSumCounts_Object = MibScalar
cpuIdleSumCounts = _CpuIdleSumCounts_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 1, 4, 3),
    _CpuIdleSumCounts_Type()
)
cpuIdleSumCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuIdleSumCounts.setStatus("mandatory")
_NodeNetViewPUGroup_ObjectIdentity = ObjectIdentity
nodeNetViewPUGroup = _NodeNetViewPUGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 2)
)
_NetViewPUStatusGroup_ObjectIdentity = ObjectIdentity
netViewPUStatusGroup = _NetViewPUStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 2, 1)
)


class _NetviewConnectionStatus_Type(Integer32):
    """Custom type netviewConnectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("not-connected", 2))
    )


_NetviewConnectionStatus_Type.__name__ = "Integer32"
_NetviewConnectionStatus_Object = MibScalar
netviewConnectionStatus = _NetviewConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 2, 1, 1),
    _NetviewConnectionStatus_Type()
)
netviewConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netviewConnectionStatus.setStatus("mandatory")


class _NetviewLastClearCode_Type(OctetString):
    """Custom type netviewLastClearCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_NetviewLastClearCode_Type.__name__ = "OctetString"
_NetviewLastClearCode_Object = MibScalar
netviewLastClearCode = _NetviewLastClearCode_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 2, 1, 2),
    _NetviewLastClearCode_Type()
)
netviewLastClearCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netviewLastClearCode.setStatus("mandatory")


class _NetviewAltConnectionStatus_Type(Integer32):
    """Custom type netviewAltConnectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("not-connected", 2))
    )


_NetviewAltConnectionStatus_Type.__name__ = "Integer32"
_NetviewAltConnectionStatus_Object = MibScalar
netviewAltConnectionStatus = _NetviewAltConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 2, 1, 3),
    _NetviewAltConnectionStatus_Type()
)
netviewAltConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netviewAltConnectionStatus.setStatus("mandatory")


class _NetviewAltLastClearCode_Type(OctetString):
    """Custom type netviewAltLastClearCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_NetviewAltLastClearCode_Type.__name__ = "OctetString"
_NetviewAltLastClearCode_Object = MibScalar
netviewAltLastClearCode = _NetviewAltLastClearCode_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 2, 1, 4),
    _NetviewAltLastClearCode_Type()
)
netviewAltLastClearCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netviewAltLastClearCode.setStatus("mandatory")
_NetviewConnectionAttemptCount_Type = Integer32
_NetviewConnectionAttemptCount_Object = MibScalar
netviewConnectionAttemptCount = _NetviewConnectionAttemptCount_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 2, 1, 5),
    _NetviewConnectionAttemptCount_Type()
)
netviewConnectionAttemptCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netviewConnectionAttemptCount.setStatus("mandatory")
_NetviewAltConnectionAttemptCount_Type = Integer32
_NetviewAltConnectionAttemptCount_Object = MibScalar
netviewAltConnectionAttemptCount = _NetviewAltConnectionAttemptCount_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 2, 1, 6),
    _NetviewAltConnectionAttemptCount_Type()
)
netviewAltConnectionAttemptCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netviewAltConnectionAttemptCount.setStatus("mandatory")


class _NetviewStatusIgnored_Type(Integer32):
    """Custom type netviewStatusIgnored based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_NetviewStatusIgnored_Type.__name__ = "Integer32"
_NetviewStatusIgnored_Object = MibScalar
netviewStatusIgnored = _NetviewStatusIgnored_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 2, 1, 7),
    _NetviewStatusIgnored_Type()
)
netviewStatusIgnored.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netviewStatusIgnored.setStatus("mandatory")


class _NetviewStatusAcknowledged_Type(Integer32):
    """Custom type netviewStatusAcknowledged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_NetviewStatusAcknowledged_Type.__name__ = "Integer32"
_NetviewStatusAcknowledged_Object = MibScalar
netviewStatusAcknowledged = _NetviewStatusAcknowledged_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 2, 1, 8),
    _NetviewStatusAcknowledged_Type()
)
netviewStatusAcknowledged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netviewStatusAcknowledged.setStatus("mandatory")


class _NetviewAltStatusIgnored_Type(Integer32):
    """Custom type netviewAltStatusIgnored based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_NetviewAltStatusIgnored_Type.__name__ = "Integer32"
_NetviewAltStatusIgnored_Object = MibScalar
netviewAltStatusIgnored = _NetviewAltStatusIgnored_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 2, 1, 9),
    _NetviewAltStatusIgnored_Type()
)
netviewAltStatusIgnored.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netviewAltStatusIgnored.setStatus("mandatory")


class _NetviewAltStatusAcknowledged_Type(Integer32):
    """Custom type netviewAltStatusAcknowledged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_NetviewAltStatusAcknowledged_Type.__name__ = "Integer32"
_NetviewAltStatusAcknowledged_Object = MibScalar
netviewAltStatusAcknowledged = _NetviewAltStatusAcknowledged_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 2, 1, 10),
    _NetviewAltStatusAcknowledged_Type()
)
netviewAltStatusAcknowledged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netviewAltStatusAcknowledged.setStatus("mandatory")
_NetViewPUConfigGroup_ObjectIdentity = ObjectIdentity
netViewPUConfigGroup = _NetViewPUConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 2, 2)
)


class _NetviewPUXID_Type(OctetString):
    """Custom type netviewPUXID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_NetviewPUXID_Type.__name__ = "OctetString"
_NetviewPUXID_Object = MibScalar
netviewPUXID = _NetviewPUXID_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 2, 2, 1),
    _NetviewPUXID_Type()
)
netviewPUXID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netviewPUXID.setStatus("mandatory")


class _AlternateNetviewPUXID_Type(OctetString):
    """Custom type alternateNetviewPUXID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_AlternateNetviewPUXID_Type.__name__ = "OctetString"
_AlternateNetviewPUXID_Object = MibScalar
alternateNetviewPUXID = _AlternateNetviewPUXID_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 2, 2, 2),
    _AlternateNetviewPUXID_Type()
)
alternateNetviewPUXID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alternateNetviewPUXID.setStatus("mandatory")


class _NetviewConnectID_Type(OctetString):
    """Custom type netviewConnectID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_NetviewConnectID_Type.__name__ = "OctetString"
_NetviewConnectID_Object = MibScalar
netviewConnectID = _NetviewConnectID_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 2, 2, 3),
    _NetviewConnectID_Type()
)
netviewConnectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netviewConnectID.setStatus("mandatory")


class _AlternateNetviewConnectID_Type(OctetString):
    """Custom type alternateNetviewConnectID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AlternateNetviewConnectID_Type.__name__ = "OctetString"
_AlternateNetviewConnectID_Object = MibScalar
alternateNetviewConnectID = _AlternateNetviewConnectID_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 2, 2, 4),
    _AlternateNetviewConnectID_Type()
)
alternateNetviewConnectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alternateNetviewConnectID.setStatus("mandatory")


class _NetviewSpecialConnect_Type(Integer32):
    """Custom type netviewSpecialConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("answer", 1),
          ("originate", 2))
    )


_NetviewSpecialConnect_Type.__name__ = "Integer32"
_NetviewSpecialConnect_Object = MibScalar
netviewSpecialConnect = _NetviewSpecialConnect_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 2, 2, 5),
    _NetviewSpecialConnect_Type()
)
netviewSpecialConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netviewSpecialConnect.setStatus("mandatory")


class _AlternateNetviewSpecialConnect_Type(Integer32):
    """Custom type alternateNetviewSpecialConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("answer", 1),
          ("originate", 2))
    )


_AlternateNetviewSpecialConnect_Type.__name__ = "Integer32"
_AlternateNetviewSpecialConnect_Object = MibScalar
alternateNetviewSpecialConnect = _AlternateNetviewSpecialConnect_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 2, 2, 6),
    _AlternateNetviewSpecialConnect_Type()
)
alternateNetviewSpecialConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alternateNetviewSpecialConnect.setStatus("mandatory")
_NodeBridgeGroup_ObjectIdentity = ObjectIdentity
nodeBridgeGroup = _NodeBridgeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 3)
)
_BridgeConfigGroup_ObjectIdentity = ObjectIdentity
bridgeConfigGroup = _BridgeConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 1)
)


class _BrEnableBridging_Type(Integer32):
    """Custom type brEnableBridging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_BrEnableBridging_Type.__name__ = "Integer32"
_BrEnableBridging_Object = MibScalar
brEnableBridging = _BrEnableBridging_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 1, 1),
    _BrEnableBridging_Type()
)
brEnableBridging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brEnableBridging.setStatus("mandatory")


class _BridgePriority_Type(Integer32):
    """Custom type bridgePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BridgePriority_Type.__name__ = "Integer32"
_BridgePriority_Object = MibScalar
bridgePriority = _BridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 1, 2),
    _BridgePriority_Type()
)
bridgePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgePriority.setStatus("mandatory")


class _BrMaxAge_Type(Integer32):
    """Custom type brMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_BrMaxAge_Type.__name__ = "Integer32"
_BrMaxAge_Object = MibScalar
brMaxAge = _BrMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 1, 3),
    _BrMaxAge_Type()
)
brMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMaxAge.setStatus("mandatory")


class _BrHelloTimer_Type(Integer32):
    """Custom type brHelloTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_BrHelloTimer_Type.__name__ = "Integer32"
_BrHelloTimer_Object = MibScalar
brHelloTimer = _BrHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 1, 4),
    _BrHelloTimer_Type()
)
brHelloTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brHelloTimer.setStatus("mandatory")


class _BrFilterIPX_Type(Integer32):
    """Custom type brFilterIPX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_BrFilterIPX_Type.__name__ = "Integer32"
_BrFilterIPX_Object = MibScalar
brFilterIPX = _BrFilterIPX_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 1, 5),
    _BrFilterIPX_Type()
)
brFilterIPX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFilterIPX.setStatus("mandatory")


class _BrFilterIP_Type(Integer32):
    """Custom type brFilterIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_BrFilterIP_Type.__name__ = "Integer32"
_BrFilterIP_Object = MibScalar
brFilterIP = _BrFilterIP_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 1, 6),
    _BrFilterIP_Type()
)
brFilterIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFilterIP.setStatus("mandatory")


class _BrFilterNetBIOS_Type(Integer32):
    """Custom type brFilterNetBIOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_BrFilterNetBIOS_Type.__name__ = "Integer32"
_BrFilterNetBIOS_Object = MibScalar
brFilterNetBIOS = _BrFilterNetBIOS_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 1, 7),
    _BrFilterNetBIOS_Type()
)
brFilterNetBIOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFilterNetBIOS.setStatus("mandatory")


class _BrFilterLLC2_Type(Integer32):
    """Custom type brFilterLLC2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_BrFilterLLC2_Type.__name__ = "Integer32"
_BrFilterLLC2_Object = MibScalar
brFilterLLC2 = _BrFilterLLC2_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 1, 8),
    _BrFilterLLC2_Type()
)
brFilterLLC2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFilterLLC2.setStatus("mandatory")


class _BrFilterSMAN_Type(Integer32):
    """Custom type brFilterSMAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_BrFilterSMAN_Type.__name__ = "Integer32"
_BrFilterSMAN_Object = MibScalar
brFilterSMAN = _BrFilterSMAN_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 1, 9),
    _BrFilterSMAN_Type()
)
brFilterSMAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFilterSMAN.setStatus("mandatory")


class _BrForwardOther_Type(Integer32):
    """Custom type brForwardOther based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_BrForwardOther_Type.__name__ = "Integer32"
_BrForwardOther_Object = MibScalar
brForwardOther = _BrForwardOther_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 1, 10),
    _BrForwardOther_Type()
)
brForwardOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brForwardOther.setStatus("mandatory")
_BrIPXtargetPort_Type = Integer32
_BrIPXtargetPort_Object = MibScalar
brIPXtargetPort = _BrIPXtargetPort_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 1, 11),
    _BrIPXtargetPort_Type()
)
brIPXtargetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIPXtargetPort.setStatus("mandatory")


class _BrIPXtargetDLCI_Type(Integer32):
    """Custom type brIPXtargetDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_BrIPXtargetDLCI_Type.__name__ = "Integer32"
_BrIPXtargetDLCI_Object = MibScalar
brIPXtargetDLCI = _BrIPXtargetDLCI_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 1, 12),
    _BrIPXtargetDLCI_Type()
)
brIPXtargetDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIPXtargetDLCI.setStatus("mandatory")
_BrIPtargetPort_Type = Integer32
_BrIPtargetPort_Object = MibScalar
brIPtargetPort = _BrIPtargetPort_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 1, 13),
    _BrIPtargetPort_Type()
)
brIPtargetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIPtargetPort.setStatus("mandatory")
_BrIPtargetDLCI_Type = Integer32
_BrIPtargetDLCI_Object = MibScalar
brIPtargetDLCI = _BrIPtargetDLCI_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 1, 14),
    _BrIPtargetDLCI_Type()
)
brIPtargetDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIPtargetDLCI.setStatus("mandatory")
_BrNetBIOStargetPort_Type = Integer32
_BrNetBIOStargetPort_Object = MibScalar
brNetBIOStargetPort = _BrNetBIOStargetPort_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 1, 15),
    _BrNetBIOStargetPort_Type()
)
brNetBIOStargetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brNetBIOStargetPort.setStatus("mandatory")
_BrNetBIOStargetDLCI_Type = Integer32
_BrNetBIOStargetDLCI_Object = MibScalar
brNetBIOStargetDLCI = _BrNetBIOStargetDLCI_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 1, 16),
    _BrNetBIOStargetDLCI_Type()
)
brNetBIOStargetDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brNetBIOStargetDLCI.setStatus("mandatory")
_BrLLC2targetPort_Type = Integer32
_BrLLC2targetPort_Object = MibScalar
brLLC2targetPort = _BrLLC2targetPort_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 1, 17),
    _BrLLC2targetPort_Type()
)
brLLC2targetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLLC2targetPort.setStatus("mandatory")
_BrLLC2targetDLCI_Type = Integer32
_BrLLC2targetDLCI_Object = MibScalar
brLLC2targetDLCI = _BrLLC2targetDLCI_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 1, 18),
    _BrLLC2targetDLCI_Type()
)
brLLC2targetDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLLC2targetDLCI.setStatus("mandatory")
_BrOthertargetPort_Type = Integer32
_BrOthertargetPort_Object = MibScalar
brOthertargetPort = _BrOthertargetPort_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 1, 19),
    _BrOthertargetPort_Type()
)
brOthertargetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brOthertargetPort.setStatus("mandatory")
_BrOthertargetDLCI_Type = Integer32
_BrOthertargetDLCI_Object = MibScalar
brOthertargetDLCI = _BrOthertargetDLCI_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 1, 20),
    _BrOthertargetDLCI_Type()
)
brOthertargetDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brOthertargetDLCI.setStatus("mandatory")


class _BrSerialPriority_Type(Integer32):
    """Custom type brSerialPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 4),
          ("medium", 3),
          ("urgent", 1))
    )


_BrSerialPriority_Type.__name__ = "Integer32"
_BrSerialPriority_Object = MibScalar
brSerialPriority = _BrSerialPriority_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 1, 21),
    _BrSerialPriority_Type()
)
brSerialPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brSerialPriority.setStatus("mandatory")


class _BrTerminatedLLC2Priority_Type(Integer32):
    """Custom type brTerminatedLLC2Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 4),
          ("medium", 3),
          ("urgent", 1))
    )


_BrTerminatedLLC2Priority_Type.__name__ = "Integer32"
_BrTerminatedLLC2Priority_Object = MibScalar
brTerminatedLLC2Priority = _BrTerminatedLLC2Priority_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 1, 22),
    _BrTerminatedLLC2Priority_Type()
)
brTerminatedLLC2Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brTerminatedLLC2Priority.setStatus("mandatory")


class _BrLLC2Priority_Type(Integer32):
    """Custom type brLLC2Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 4),
          ("medium", 3),
          ("urgent", 1))
    )


_BrLLC2Priority_Type.__name__ = "Integer32"
_BrLLC2Priority_Object = MibScalar
brLLC2Priority = _BrLLC2Priority_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 1, 23),
    _BrLLC2Priority_Type()
)
brLLC2Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLLC2Priority.setStatus("mandatory")


class _BrIPXPriority_Type(Integer32):
    """Custom type brIPXPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 4),
          ("medium", 3),
          ("urgent", 1))
    )


_BrIPXPriority_Type.__name__ = "Integer32"
_BrIPXPriority_Object = MibScalar
brIPXPriority = _BrIPXPriority_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 1, 24),
    _BrIPXPriority_Type()
)
brIPXPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIPXPriority.setStatus("mandatory")


class _BrIPPriority_Type(Integer32):
    """Custom type brIPPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 4),
          ("medium", 3),
          ("urgent", 1))
    )


_BrIPPriority_Type.__name__ = "Integer32"
_BrIPPriority_Object = MibScalar
brIPPriority = _BrIPPriority_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 1, 25),
    _BrIPPriority_Type()
)
brIPPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIPPriority.setStatus("mandatory")


class _BrNetBIOSPriority_Type(Integer32):
    """Custom type brNetBIOSPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 4),
          ("medium", 3),
          ("urgent", 1))
    )


_BrNetBIOSPriority_Type.__name__ = "Integer32"
_BrNetBIOSPriority_Object = MibScalar
brNetBIOSPriority = _BrNetBIOSPriority_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 1, 26),
    _BrNetBIOSPriority_Type()
)
brNetBIOSPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brNetBIOSPriority.setStatus("mandatory")


class _BrOtherPriority_Type(Integer32):
    """Custom type brOtherPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 4),
          ("medium", 3),
          ("urgent", 1))
    )


_BrOtherPriority_Type.__name__ = "Integer32"
_BrOtherPriority_Object = MibScalar
brOtherPriority = _BrOtherPriority_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 1, 27),
    _BrOtherPriority_Type()
)
brOtherPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brOtherPriority.setStatus("mandatory")


class _BrHighPriorityBandwidth_Type(Integer32):
    """Custom type brHighPriorityBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BrHighPriorityBandwidth_Type.__name__ = "Integer32"
_BrHighPriorityBandwidth_Object = MibScalar
brHighPriorityBandwidth = _BrHighPriorityBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 1, 28),
    _BrHighPriorityBandwidth_Type()
)
brHighPriorityBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brHighPriorityBandwidth.setStatus("mandatory")


class _BrMediumPriorityBandwidth_Type(Integer32):
    """Custom type brMediumPriorityBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BrMediumPriorityBandwidth_Type.__name__ = "Integer32"
_BrMediumPriorityBandwidth_Object = MibScalar
brMediumPriorityBandwidth = _BrMediumPriorityBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 1, 29),
    _BrMediumPriorityBandwidth_Type()
)
brMediumPriorityBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMediumPriorityBandwidth.setStatus("mandatory")


class _BrLowPriorityBandwidth_Type(Integer32):
    """Custom type brLowPriorityBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BrLowPriorityBandwidth_Type.__name__ = "Integer32"
_BrLowPriorityBandwidth_Object = MibScalar
brLowPriorityBandwidth = _BrLowPriorityBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 1, 30),
    _BrLowPriorityBandwidth_Type()
)
brLowPriorityBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLowPriorityBandwidth.setStatus("mandatory")


class _BrDelayTimer_Type(Integer32):
    """Custom type brDelayTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BrDelayTimer_Type.__name__ = "Integer32"
_BrDelayTimer_Object = MibScalar
brDelayTimer = _BrDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 1, 31),
    _BrDelayTimer_Type()
)
brDelayTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brDelayTimer.setStatus("mandatory")


class _BrEnableIPXBridging_Type(Integer32):
    """Custom type brEnableIPXBridging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_BrEnableIPXBridging_Type.__name__ = "Integer32"
_BrEnableIPXBridging_Object = MibScalar
brEnableIPXBridging = _BrEnableIPXBridging_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 1, 32),
    _BrEnableIPXBridging_Type()
)
brEnableIPXBridging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brEnableIPXBridging.setStatus("mandatory")


class _BrEnableIPBridging_Type(Integer32):
    """Custom type brEnableIPBridging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_BrEnableIPBridging_Type.__name__ = "Integer32"
_BrEnableIPBridging_Object = MibScalar
brEnableIPBridging = _BrEnableIPBridging_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 1, 33),
    _BrEnableIPBridging_Type()
)
brEnableIPBridging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brEnableIPBridging.setStatus("mandatory")


class _BrEnableNetBiosBridging_Type(Integer32):
    """Custom type brEnableNetBiosBridging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_BrEnableNetBiosBridging_Type.__name__ = "Integer32"
_BrEnableNetBiosBridging_Object = MibScalar
brEnableNetBiosBridging = _BrEnableNetBiosBridging_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 1, 34),
    _BrEnableNetBiosBridging_Type()
)
brEnableNetBiosBridging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brEnableNetBiosBridging.setStatus("mandatory")


class _BrEnableSNABridging_Type(Integer32):
    """Custom type brEnableSNABridging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_BrEnableSNABridging_Type.__name__ = "Integer32"
_BrEnableSNABridging_Object = MibScalar
brEnableSNABridging = _BrEnableSNABridging_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 1, 35),
    _BrEnableSNABridging_Type()
)
brEnableSNABridging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brEnableSNABridging.setStatus("mandatory")


class _BrEnableSyncManBridging_Type(Integer32):
    """Custom type brEnableSyncManBridging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_BrEnableSyncManBridging_Type.__name__ = "Integer32"
_BrEnableSyncManBridging_Object = MibScalar
brEnableSyncManBridging = _BrEnableSyncManBridging_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 1, 36),
    _BrEnableSyncManBridging_Type()
)
brEnableSyncManBridging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brEnableSyncManBridging.setStatus("mandatory")


class _BrEnableOtherBridging_Type(Integer32):
    """Custom type brEnableOtherBridging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_BrEnableOtherBridging_Type.__name__ = "Integer32"
_BrEnableOtherBridging_Object = MibScalar
brEnableOtherBridging = _BrEnableOtherBridging_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 1, 37),
    _BrEnableOtherBridging_Type()
)
brEnableOtherBridging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brEnableOtherBridging.setStatus("mandatory")
_BridgeStatsGroup_ObjectIdentity = ObjectIdentity
bridgeStatsGroup = _BridgeStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 2)
)
_IpxStatsTable_Object = MibTable
ipxStatsTable = _IpxStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    ipxStatsTable.setStatus("mandatory")
_IpxStatsEntry_Object = MibTableRow
ipxStatsEntry = _IpxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 2, 1, 1)
)
ipxStatsEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "ipxStatsIndex"),
)
if mibBuilder.loadTexts:
    ipxStatsEntry.setStatus("mandatory")
_IpxStatsIndex_Type = Integer32
_IpxStatsIndex_Object = MibTableColumn
ipxStatsIndex = _IpxStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 2, 1, 1, 1),
    _IpxStatsIndex_Type()
)
ipxStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxStatsIndex.setStatus("mandatory")
_IpxRipRcvdFwdInterval_Type = Counter32
_IpxRipRcvdFwdInterval_Object = MibTableColumn
ipxRipRcvdFwdInterval = _IpxRipRcvdFwdInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 2, 1, 1, 2),
    _IpxRipRcvdFwdInterval_Type()
)
ipxRipRcvdFwdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRipRcvdFwdInterval.setStatus("mandatory")
_IpxRipRcvdFiltInterval_Type = Counter32
_IpxRipRcvdFiltInterval_Object = MibTableColumn
ipxRipRcvdFiltInterval = _IpxRipRcvdFiltInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 2, 1, 1, 3),
    _IpxRipRcvdFiltInterval_Type()
)
ipxRipRcvdFiltInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRipRcvdFiltInterval.setStatus("mandatory")
_IpxSapRcvdFwdInterval_Type = Counter32
_IpxSapRcvdFwdInterval_Object = MibTableColumn
ipxSapRcvdFwdInterval = _IpxSapRcvdFwdInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 2, 1, 1, 4),
    _IpxSapRcvdFwdInterval_Type()
)
ipxSapRcvdFwdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSapRcvdFwdInterval.setStatus("mandatory")
_IpxSapRcvdFiltInterval_Type = Counter32
_IpxSapRcvdFiltInterval_Object = MibTableColumn
ipxSapRcvdFiltInterval = _IpxSapRcvdFiltInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 3, 2, 1, 1, 5),
    _IpxSapRcvdFiltInterval_Type()
)
ipxSapRcvdFiltInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSapRcvdFiltInterval.setStatus("mandatory")
_NodeLANGroup_ObjectIdentity = ObjectIdentity
nodeLANGroup = _NodeLANGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 4)
)
_LanControlGroup_ObjectIdentity = ObjectIdentity
lanControlGroup = _LanControlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 1)
)
_LanControlTable_Object = MibTable
lanControlTable = _LanControlTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 1, 1)
)
if mibBuilder.loadTexts:
    lanControlTable.setStatus("mandatory")
_LanControlEntry_Object = MibTableRow
lanControlEntry = _LanControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 1, 1, 1)
)
lanControlEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "lanControlIndex"),
)
if mibBuilder.loadTexts:
    lanControlEntry.setStatus("mandatory")
_LanControlIndex_Type = Integer32
_LanControlIndex_Object = MibTableColumn
lanControlIndex = _LanControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 1, 1, 1, 1),
    _LanControlIndex_Type()
)
lanControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanControlIndex.setStatus("mandatory")


class _LanControlType_Type(Integer32):
    """Custom type lanControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(17,
              21)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-type", 17),
          ("token-ring-type", 21))
    )


_LanControlType_Type.__name__ = "Integer32"
_LanControlType_Object = MibTableColumn
lanControlType = _LanControlType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 1, 1, 1, 2),
    _LanControlType_Type()
)
lanControlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanControlType.setStatus("mandatory")


class _LanStatus_Type(Integer32):
    """Custom type lanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("failed", 3),
          ("restart", 4))
    )


_LanStatus_Type.__name__ = "Integer32"
_LanStatus_Object = MibTableColumn
lanStatus = _LanStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 1, 1, 1, 3),
    _LanStatus_Type()
)
lanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanStatus.setStatus("mandatory")


class _LanControlFailureCode_Type(OctetString):
    """Custom type lanControlFailureCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_LanControlFailureCode_Type.__name__ = "OctetString"
_LanControlFailureCode_Object = MibTableColumn
lanControlFailureCode = _LanControlFailureCode_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 1, 1, 1, 4),
    _LanControlFailureCode_Type()
)
lanControlFailureCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanControlFailureCode.setStatus("mandatory")


class _LanControlNAUName_Type(DisplayString):
    """Custom type lanControlNAUName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_LanControlNAUName_Type.__name__ = "DisplayString"
_LanControlNAUName_Object = MibTableColumn
lanControlNAUName = _LanControlNAUName_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 1, 1, 1, 5),
    _LanControlNAUName_Type()
)
lanControlNAUName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanControlNAUName.setStatus("mandatory")


class _LanStatusIgnored_Type(Integer32):
    """Custom type lanStatusIgnored based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_LanStatusIgnored_Type.__name__ = "Integer32"
_LanStatusIgnored_Object = MibTableColumn
lanStatusIgnored = _LanStatusIgnored_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 1, 1, 1, 6),
    _LanStatusIgnored_Type()
)
lanStatusIgnored.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanStatusIgnored.setStatus("mandatory")


class _LanStatusAcknowledged_Type(Integer32):
    """Custom type lanStatusAcknowledged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_LanStatusAcknowledged_Type.__name__ = "Integer32"
_LanStatusAcknowledged_Object = MibTableColumn
lanStatusAcknowledged = _LanStatusAcknowledged_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 1, 1, 1, 7),
    _LanStatusAcknowledged_Type()
)
lanStatusAcknowledged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanStatusAcknowledged.setStatus("mandatory")
_LanTokenRingGroup_ObjectIdentity = ObjectIdentity
lanTokenRingGroup = _LanTokenRingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 2)
)
_LanPortTable_Object = MibTable
lanPortTable = _LanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    lanPortTable.setStatus("mandatory")
_LanPortEntry_Object = MibTableRow
lanPortEntry = _LanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 2, 1, 1)
)
lanPortEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "lanPortIndex"),
)
if mibBuilder.loadTexts:
    lanPortEntry.setStatus("mandatory")
_LanPortIndex_Type = Integer32
_LanPortIndex_Object = MibTableColumn
lanPortIndex = _LanPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 2, 1, 1, 1),
    _LanPortIndex_Type()
)
lanPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanPortIndex.setStatus("mandatory")


class _LanPortType_Type(Integer32):
    """Custom type lanPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(17,
              21)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-type", 17),
          ("token-ring-type", 21))
    )


_LanPortType_Type.__name__ = "Integer32"
_LanPortType_Object = MibTableColumn
lanPortType = _LanPortType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 2, 1, 1, 2),
    _LanPortType_Type()
)
lanPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanPortType.setStatus("mandatory")
_LanMACAddress_Type = PhysAddress
_LanMACAddress_Object = MibTableColumn
lanMACAddress = _LanMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 2, 1, 1, 3),
    _LanMACAddress_Type()
)
lanMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanMACAddress.setStatus("mandatory")
_LanPROMMACAddress_Type = PhysAddress
_LanPROMMACAddress_Object = MibTableColumn
lanPROMMACAddress = _LanPROMMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 2, 1, 1, 4),
    _LanPROMMACAddress_Type()
)
lanPROMMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanPROMMACAddress.setStatus("mandatory")


class _LanSpeed_Type(Integer32):
    """Custom type lanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              10,
              16)
        )
    )
    namedValues = NamedValues(
        *(("speed-10Mbs", 10),
          ("speed-16Mbs", 16),
          ("speed-4Mbs", 4))
    )


_LanSpeed_Type.__name__ = "Integer32"
_LanSpeed_Object = MibTableColumn
lanSpeed = _LanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 2, 1, 1, 5),
    _LanSpeed_Type()
)
lanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanSpeed.setStatus("mandatory")


class _LanT1Timer_Type(Integer32):
    """Custom type lanT1Timer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_LanT1Timer_Type.__name__ = "Integer32"
_LanT1Timer_Object = MibTableColumn
lanT1Timer = _LanT1Timer_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 2, 1, 1, 6),
    _LanT1Timer_Type()
)
lanT1Timer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanT1Timer.setStatus("mandatory")


class _LanT2Timer_Type(Integer32):
    """Custom type lanT2Timer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_LanT2Timer_Type.__name__ = "Integer32"
_LanT2Timer_Object = MibTableColumn
lanT2Timer = _LanT2Timer_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 2, 1, 1, 7),
    _LanT2Timer_Type()
)
lanT2Timer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanT2Timer.setStatus("mandatory")


class _LanTiTimer_Type(Integer32):
    """Custom type lanTiTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 50),
    )


_LanTiTimer_Type.__name__ = "Integer32"
_LanTiTimer_Object = MibTableColumn
lanTiTimer = _LanTiTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 2, 1, 1, 8),
    _LanTiTimer_Type()
)
lanTiTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanTiTimer.setStatus("mandatory")


class _LanRxWindowSize_Type(Integer32):
    """Custom type lanRxWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_LanRxWindowSize_Type.__name__ = "Integer32"
_LanRxWindowSize_Object = MibTableColumn
lanRxWindowSize = _LanRxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 2, 1, 1, 9),
    _LanRxWindowSize_Type()
)
lanRxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanRxWindowSize.setStatus("mandatory")


class _LanTxWindowSize_Type(Integer32):
    """Custom type lanTxWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_LanTxWindowSize_Type.__name__ = "Integer32"
_LanTxWindowSize_Object = MibTableColumn
lanTxWindowSize = _LanTxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 2, 1, 1, 10),
    _LanTxWindowSize_Type()
)
lanTxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanTxWindowSize.setStatus("mandatory")


class _LanMaxRetries_Type(Integer32):
    """Custom type lanMaxRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_LanMaxRetries_Type.__name__ = "Integer32"
_LanMaxRetries_Object = MibTableColumn
lanMaxRetries = _LanMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 2, 1, 1, 11),
    _LanMaxRetries_Type()
)
lanMaxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanMaxRetries.setStatus("mandatory")


class _LanRingNumber_Type(Integer32):
    """Custom type lanRingNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_LanRingNumber_Type.__name__ = "Integer32"
_LanRingNumber_Object = MibTableColumn
lanRingNumber = _LanRingNumber_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 2, 1, 1, 12),
    _LanRingNumber_Type()
)
lanRingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanRingNumber.setStatus("mandatory")


class _LanBridgeNumber_Type(Integer32):
    """Custom type lanBridgeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_LanBridgeNumber_Type.__name__ = "Integer32"
_LanBridgeNumber_Object = MibTableColumn
lanBridgeNumber = _LanBridgeNumber_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 2, 1, 1, 13),
    _LanBridgeNumber_Type()
)
lanBridgeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBridgeNumber.setStatus("mandatory")


class _LanEthernetFrameFormat_Type(Integer32):
    """Custom type lanEthernetFrameFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("e802-3-type", 2),
          ("ethernet-type-2", 3),
          ("not-applicable", 1))
    )


_LanEthernetFrameFormat_Type.__name__ = "Integer32"
_LanEthernetFrameFormat_Object = MibTableColumn
lanEthernetFrameFormat = _LanEthernetFrameFormat_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 2, 1, 1, 14),
    _LanEthernetFrameFormat_Type()
)
lanEthernetFrameFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanEthernetFrameFormat.setStatus("mandatory")


class _LanSendLocalTest_Type(Integer32):
    """Custom type lanSendLocalTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 3),
          ("not-applicable", 1),
          ("yes", 2))
    )


_LanSendLocalTest_Type.__name__ = "Integer32"
_LanSendLocalTest_Object = MibTableColumn
lanSendLocalTest = _LanSendLocalTest_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 2, 1, 1, 15),
    _LanSendLocalTest_Type()
)
lanSendLocalTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanSendLocalTest.setStatus("mandatory")


class _LanBroadcastType_Type(Integer32):
    """Custom type lanBroadcastType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("all-bc", 3),
          ("none-bc", 2),
          ("not-applicable", 1),
          ("single-bc", 4))
    )


_LanBroadcastType_Type.__name__ = "Integer32"
_LanBroadcastType_Object = MibTableColumn
lanBroadcastType = _LanBroadcastType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 2, 1, 1, 16),
    _LanBroadcastType_Type()
)
lanBroadcastType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanBroadcastType.setStatus("mandatory")
_LanIPAddress_Type = IpAddress
_LanIPAddress_Object = MibTableColumn
lanIPAddress = _LanIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 2, 1, 1, 17),
    _LanIPAddress_Type()
)
lanIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanIPAddress.setStatus("mandatory")
_LanNetworkMask_Type = IpAddress
_LanNetworkMask_Object = MibTableColumn
lanNetworkMask = _LanNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 2, 1, 1, 18),
    _LanNetworkMask_Type()
)
lanNetworkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanNetworkMask.setStatus("mandatory")
_LanDefaultGateway_Type = IpAddress
_LanDefaultGateway_Object = MibTableColumn
lanDefaultGateway = _LanDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 2, 1, 1, 19),
    _LanDefaultGateway_Type()
)
lanDefaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanDefaultGateway.setStatus("mandatory")


class _LanNAUName_Type(DisplayString):
    """Custom type lanNAUName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_LanNAUName_Type.__name__ = "DisplayString"
_LanNAUName_Object = MibTableColumn
lanNAUName = _LanNAUName_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 2, 1, 1, 20),
    _LanNAUName_Type()
)
lanNAUName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanNAUName.setStatus("mandatory")


class _LanInterfaceType_Type(Integer32):
    """Custom type lanInterfaceType based on Integer32"""
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
        *(("aui", 2),
          ("bnc", 3),
          ("not-applicable", 1),
          ("stp", 5),
          ("utp", 4))
    )


_LanInterfaceType_Type.__name__ = "Integer32"
_LanInterfaceType_Object = MibTableColumn
lanInterfaceType = _LanInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 2, 1, 1, 21),
    _LanInterfaceType_Type()
)
lanInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanInterfaceType.setStatus("mandatory")


class _LanIPEthernetFrameType_Type(Integer32):
    """Custom type lanIPEthernetFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("e802-3-type", 2),
          ("ethernet-type-2", 3),
          ("not-applicable", 1))
    )


_LanIPEthernetFrameType_Type.__name__ = "Integer32"
_LanIPEthernetFrameType_Object = MibTableColumn
lanIPEthernetFrameType = _LanIPEthernetFrameType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 2, 1, 1, 22),
    _LanIPEthernetFrameType_Type()
)
lanIPEthernetFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanIPEthernetFrameType.setStatus("mandatory")


class _LanInitState_Type(Integer32):
    """Custom type lanInitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in-service", 1),
          ("out-of-service", 2))
    )


_LanInitState_Type.__name__ = "Integer32"
_LanInitState_Object = MibTableColumn
lanInitState = _LanInitState_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 2, 1, 1, 23),
    _LanInitState_Type()
)
lanInitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanInitState.setStatus("mandatory")
_LanSecondDefaultGateway_Type = IpAddress
_LanSecondDefaultGateway_Object = MibTableColumn
lanSecondDefaultGateway = _LanSecondDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 2, 1, 1, 24),
    _LanSecondDefaultGateway_Type()
)
lanSecondDefaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanSecondDefaultGateway.setStatus("mandatory")


class _LanRIPUpdtTimer_Type(Integer32):
    """Custom type lanRIPUpdtTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 180),
    )


_LanRIPUpdtTimer_Type.__name__ = "Integer32"
_LanRIPUpdtTimer_Object = MibTableColumn
lanRIPUpdtTimer = _LanRIPUpdtTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 2, 1, 1, 25),
    _LanRIPUpdtTimer_Type()
)
lanRIPUpdtTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanRIPUpdtTimer.setStatus("mandatory")


class _LanRIPAge_Type(Integer32):
    """Custom type lanRIPAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 540),
    )


_LanRIPAge_Type.__name__ = "Integer32"
_LanRIPAge_Object = MibTableColumn
lanRIPAge = _LanRIPAge_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 2, 1, 1, 26),
    _LanRIPAge_Type()
)
lanRIPAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanRIPAge.setStatus("mandatory")


class _LanSAPUpdtTimer_Type(Integer32):
    """Custom type lanSAPUpdtTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 180),
    )


_LanSAPUpdtTimer_Type.__name__ = "Integer32"
_LanSAPUpdtTimer_Object = MibTableColumn
lanSAPUpdtTimer = _LanSAPUpdtTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 2, 1, 1, 27),
    _LanSAPUpdtTimer_Type()
)
lanSAPUpdtTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanSAPUpdtTimer.setStatus("mandatory")


class _LanSAPAge_Type(Integer32):
    """Custom type lanSAPAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 720),
    )


_LanSAPAge_Type.__name__ = "Integer32"
_LanSAPAge_Object = MibTableColumn
lanSAPAge = _LanSAPAge_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 2, 1, 1, 28),
    _LanSAPAge_Type()
)
lanSAPAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanSAPAge.setStatus("mandatory")


class _LanRSM_Type(Integer32):
    """Custom type lanRSM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_LanRSM_Type.__name__ = "Integer32"
_LanRSM_Object = MibTableColumn
lanRSM = _LanRSM_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 4, 2, 1, 1, 29),
    _LanRSM_Type()
)
lanRSM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanRSM.setStatus("mandatory")
_NodeLineGroup_ObjectIdentity = ObjectIdentity
nodeLineGroup = _NodeLineGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 5)
)
_LineControlGroup_ObjectIdentity = ObjectIdentity
lineControlGroup = _LineControlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 1)
)
_LineControlTable_Object = MibTable
lineControlTable = _LineControlTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 1, 1)
)
if mibBuilder.loadTexts:
    lineControlTable.setStatus("mandatory")
_LineControlEntry_Object = MibTableRow
lineControlEntry = _LineControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 1, 1, 1)
)
lineControlEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "lineControlIndex"),
)
if mibBuilder.loadTexts:
    lineControlEntry.setStatus("mandatory")
_LineControlIndex_Type = Integer32
_LineControlIndex_Object = MibTableColumn
lineControlIndex = _LineControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 1, 1, 1, 1),
    _LineControlIndex_Type()
)
lineControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineControlIndex.setStatus("mandatory")


class _LineControlType_Type(Integer32):
    """Custom type lineControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("dial-backup-type", 20),
          ("frameRelay-type", 19),
          ("hasc-type", 9),
          ("hbsc-type", 1),
          ("hsdlc-type", 11),
          ("primaryRJE-type", 14),
          ("secondaryRJE-type", 13),
          ("tasc-type", 10),
          ("tbsc-type", 2),
          ("tsdlc-type", 12),
          ("x25dce-type", 8),
          ("x25dte-type", 7))
    )


_LineControlType_Type.__name__ = "Integer32"
_LineControlType_Object = MibTableColumn
lineControlType = _LineControlType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 1, 1, 1, 2),
    _LineControlType_Type()
)
lineControlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineControlType.setStatus("mandatory")


class _LineStatus_Type(Integer32):
    """Custom type lineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("enable-all", 5),
          ("failed", 3),
          ("not-in-use", 6),
          ("restart", 4))
    )


_LineStatus_Type.__name__ = "Integer32"
_LineStatus_Object = MibTableColumn
lineStatus = _LineStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 1, 1, 1, 3),
    _LineStatus_Type()
)
lineStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineStatus.setStatus("mandatory")


class _LineControlFailureCode_Type(OctetString):
    """Custom type lineControlFailureCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_LineControlFailureCode_Type.__name__ = "OctetString"
_LineControlFailureCode_Object = MibTableColumn
lineControlFailureCode = _LineControlFailureCode_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 1, 1, 1, 4),
    _LineControlFailureCode_Type()
)
lineControlFailureCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineControlFailureCode.setStatus("mandatory")


class _LineControlNAUName_Type(DisplayString):
    """Custom type lineControlNAUName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_LineControlNAUName_Type.__name__ = "DisplayString"
_LineControlNAUName_Object = MibTableColumn
lineControlNAUName = _LineControlNAUName_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 1, 1, 1, 5),
    _LineControlNAUName_Type()
)
lineControlNAUName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineControlNAUName.setStatus("mandatory")


class _LineStatusIgnored_Type(Integer32):
    """Custom type lineStatusIgnored based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_LineStatusIgnored_Type.__name__ = "Integer32"
_LineStatusIgnored_Object = MibTableColumn
lineStatusIgnored = _LineStatusIgnored_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 1, 1, 1, 6),
    _LineStatusIgnored_Type()
)
lineStatusIgnored.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineStatusIgnored.setStatus("mandatory")


class _LineStatusAcknowledged_Type(Integer32):
    """Custom type lineStatusAcknowledged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_LineStatusAcknowledged_Type.__name__ = "Integer32"
_LineStatusAcknowledged_Object = MibTableColumn
lineStatusAcknowledged = _LineStatusAcknowledged_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 1, 1, 1, 7),
    _LineStatusAcknowledged_Type()
)
lineStatusAcknowledged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineStatusAcknowledged.setStatus("mandatory")


class _LoopbackTest_Type(Integer32):
    """Custom type loopbackTest based on Integer32"""
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
        *(("local", 1),
          ("network-or-full", 2),
          ("passive", 5),
          ("remote", 3),
          ("stop-test", 4))
    )


_LoopbackTest_Type.__name__ = "Integer32"
_LoopbackTest_Object = MibTableColumn
loopbackTest = _LoopbackTest_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 1, 1, 1, 8),
    _LoopbackTest_Type()
)
loopbackTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopbackTest.setStatus("mandatory")
_LinePhysicalGroup_ObjectIdentity = ObjectIdentity
linePhysicalGroup = _LinePhysicalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2)
)
_LinePhysicalTable_Object = MibTable
linePhysicalTable = _LinePhysicalTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 1)
)
if mibBuilder.loadTexts:
    linePhysicalTable.setStatus("mandatory")
_LinePhysicalEntry_Object = MibTableRow
linePhysicalEntry = _LinePhysicalEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 1, 1)
)
linePhysicalEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "linePhysicalIndex"),
)
if mibBuilder.loadTexts:
    linePhysicalEntry.setStatus("mandatory")
_LinePhysicalIndex_Type = Integer32
_LinePhysicalIndex_Object = MibTableColumn
linePhysicalIndex = _LinePhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 1, 1, 1),
    _LinePhysicalIndex_Type()
)
linePhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linePhysicalIndex.setStatus("mandatory")


class _LinePhysicalType_Type(Integer32):
    """Custom type linePhysicalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("dial-backup-type", 20),
          ("frameRelay-type", 19),
          ("hasc-type", 10),
          ("hbsc-type", 1),
          ("hsdlc-type", 11),
          ("primaryRJE-type", 14),
          ("secondaryRJE-type", 13),
          ("tasc-type", 9),
          ("tbsc-type", 2),
          ("tsdlc-type", 12),
          ("x25dce-type", 8),
          ("x25dte-type", 7))
    )


_LinePhysicalType_Type.__name__ = "Integer32"
_LinePhysicalType_Object = MibTableColumn
linePhysicalType = _LinePhysicalType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 1, 1, 2),
    _LinePhysicalType_Type()
)
linePhysicalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linePhysicalType.setStatus("mandatory")


class _LineEIAStatus_Type(Integer32):
    """Custom type lineEIAStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LineEIAStatus_Type.__name__ = "Integer32"
_LineEIAStatus_Object = MibTableColumn
lineEIAStatus = _LineEIAStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 1, 1, 3),
    _LineEIAStatus_Type()
)
lineEIAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineEIAStatus.setStatus("mandatory")
_LineQualityFrameCount_Type = Counter32
_LineQualityFrameCount_Object = MibTableColumn
lineQualityFrameCount = _LineQualityFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 1, 1, 4),
    _LineQualityFrameCount_Type()
)
lineQualityFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineQualityFrameCount.setStatus("mandatory")
_LineQualityCRCErrors_Type = Counter32
_LineQualityCRCErrors_Object = MibTableColumn
lineQualityCRCErrors = _LineQualityCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 1, 1, 5),
    _LineQualityCRCErrors_Type()
)
lineQualityCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineQualityCRCErrors.setStatus("mandatory")
_LineQualityAborts_Type = Counter32
_LineQualityAborts_Object = MibTableColumn
lineQualityAborts = _LineQualityAborts_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 1, 1, 6),
    _LineQualityAborts_Type()
)
lineQualityAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineQualityAborts.setStatus("mandatory")


class _LineInterfaceType_Type(Integer32):
    """Custom type lineInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dsu-csu", 5),
          ("isdn", 6),
          ("line-RS232", 1),
          ("line-RS530", 3),
          ("line-V35", 2),
          ("line-universal", 4))
    )


_LineInterfaceType_Type.__name__ = "Integer32"
_LineInterfaceType_Object = MibTableColumn
lineInterfaceType = _LineInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 1, 1, 7),
    _LineInterfaceType_Type()
)
lineInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineInterfaceType.setStatus("mandatory")


class _LineCableType_Type(Integer32):
    """Custom type lineCableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("indeterminate-cable", 2),
          ("no-cable-attached", 3),
          ("not-applicable", 1),
          ("rs232-DCE-cable", 5),
          ("rs232-DTE-cable", 4),
          ("rs530-DCE-cable", 11),
          ("rs530-DTE-cable", 10),
          ("v35-DCE-cable", 7),
          ("v35-DTE-cable", 6),
          ("x21-DCE-cable", 9),
          ("x21-DTE-cable", 8))
    )


_LineCableType_Type.__name__ = "Integer32"
_LineCableType_Object = MibTableColumn
lineCableType = _LineCableType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 1, 1, 8),
    _LineCableType_Type()
)
lineCableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineCableType.setStatus("mandatory")


class _LineSwitchedConnection_Type(Integer32):
    """Custom type lineSwitchedConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dedicated", 2),
          ("not-applicable", 1),
          ("switched", 3))
    )


_LineSwitchedConnection_Type.__name__ = "Integer32"
_LineSwitchedConnection_Object = MibTableColumn
lineSwitchedConnection = _LineSwitchedConnection_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 1, 1, 9),
    _LineSwitchedConnection_Type()
)
lineSwitchedConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineSwitchedConnection.setStatus("mandatory")
_IsdnControlGroup_ObjectIdentity = ObjectIdentity
isdnControlGroup = _IsdnControlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 2)
)
_IsdndeviceConfigTable_Object = MibTable
isdndeviceConfigTable = _IsdndeviceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 2, 1)
)
if mibBuilder.loadTexts:
    isdndeviceConfigTable.setStatus("mandatory")
_IsdndeviceConfigEntry_Object = MibTableRow
isdndeviceConfigEntry = _IsdndeviceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 2, 1, 1)
)
isdndeviceConfigEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "isdnLineIndex"),
)
if mibBuilder.loadTexts:
    isdndeviceConfigEntry.setStatus("mandatory")
_IsdnLineIndex_Type = Integer32
_IsdnLineIndex_Object = MibTableColumn
isdnLineIndex = _IsdnLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 2, 1, 1, 1),
    _IsdnLineIndex_Type()
)
isdnLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnLineIndex.setStatus("mandatory")
_ServiceType_Type = Integer32
_ServiceType_Object = MibTableColumn
serviceType = _ServiceType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 2, 1, 1, 2),
    _ServiceType_Type()
)
serviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceType.setStatus("mandatory")


class _IsdnSpeed_Type(Integer32):
    """Custom type isdnSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(560,
              640)
        )
    )
    namedValues = NamedValues(
        *(("speed56000", 560),
          ("speed64000", 640))
    )


_IsdnSpeed_Type.__name__ = "Integer32"
_IsdnSpeed_Object = MibTableColumn
isdnSpeed = _IsdnSpeed_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 2, 1, 1, 3),
    _IsdnSpeed_Type()
)
isdnSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnSpeed.setStatus("mandatory")
_ConnectionTimeOut_Type = Integer32
_ConnectionTimeOut_Object = MibTableColumn
connectionTimeOut = _ConnectionTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 2, 1, 1, 4),
    _ConnectionTimeOut_Type()
)
connectionTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionTimeOut.setStatus("mandatory")
_NosConnectAttempts_Type = Integer32
_NosConnectAttempts_Object = MibTableColumn
nosConnectAttempts = _NosConnectAttempts_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 2, 1, 1, 5),
    _NosConnectAttempts_Type()
)
nosConnectAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nosConnectAttempts.setStatus("mandatory")
_FarEndNumberType_Type = Integer32
_FarEndNumberType_Object = MibTableColumn
farEndNumberType = _FarEndNumberType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 2, 1, 1, 6),
    _FarEndNumberType_Type()
)
farEndNumberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    farEndNumberType.setStatus("mandatory")
_FarEndNumberPlan_Type = Integer32
_FarEndNumberPlan_Object = MibTableColumn
farEndNumberPlan = _FarEndNumberPlan_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 2, 1, 1, 7),
    _FarEndNumberPlan_Type()
)
farEndNumberPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    farEndNumberPlan.setStatus("mandatory")
_FarEndNumber_Type = Integer32
_FarEndNumber_Object = MibTableColumn
farEndNumber = _FarEndNumber_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 2, 1, 1, 8),
    _FarEndNumber_Type()
)
farEndNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    farEndNumber.setStatus("mandatory")
_LocalNumberType_Type = Integer32
_LocalNumberType_Object = MibTableColumn
localNumberType = _LocalNumberType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 2, 1, 1, 9),
    _LocalNumberType_Type()
)
localNumberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localNumberType.setStatus("mandatory")
_LocalNumberPlan_Type = Integer32
_LocalNumberPlan_Object = MibTableColumn
localNumberPlan = _LocalNumberPlan_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 2, 1, 1, 10),
    _LocalNumberPlan_Type()
)
localNumberPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localNumberPlan.setStatus("mandatory")
_LocalNumber_Type = Integer32
_LocalNumber_Object = MibTableColumn
localNumber = _LocalNumber_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 2, 1, 1, 11),
    _LocalNumber_Type()
)
localNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localNumber.setStatus("mandatory")


class _Spid_Type(OctetString):
    """Custom type spid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_Spid_Type.__name__ = "OctetString"
_Spid_Object = MibTableColumn
spid = _Spid_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 2, 1, 1, 12),
    _Spid_Type()
)
spid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spid.setStatus("mandatory")
_IsdndeviceStatsTable_Object = MibTable
isdndeviceStatsTable = _IsdndeviceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 2, 2)
)
if mibBuilder.loadTexts:
    isdndeviceStatsTable.setStatus("mandatory")
_IsdndeviceStatsEntry_Object = MibTableRow
isdndeviceStatsEntry = _IsdndeviceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 2, 2, 1)
)
isdndeviceStatsEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "isdnIndex"),
)
if mibBuilder.loadTexts:
    isdndeviceStatsEntry.setStatus("mandatory")
_IsdnIndex_Type = Integer32
_IsdnIndex_Object = MibTableColumn
isdnIndex = _IsdnIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 2, 2, 1, 1),
    _IsdnIndex_Type()
)
isdnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnIndex.setStatus("mandatory")
_ChannelID_Type = Integer32
_ChannelID_Object = MibTableColumn
channelID = _ChannelID_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 2, 2, 1, 2),
    _ChannelID_Type()
)
channelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelID.setStatus("mandatory")
_KbytesTransmitted_Type = Counter32
_KbytesTransmitted_Object = MibTableColumn
kbytesTransmitted = _KbytesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 2, 2, 1, 3),
    _KbytesTransmitted_Type()
)
kbytesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbytesTransmitted.setStatus("mandatory")
_KbytesReceived_Type = Counter32
_KbytesReceived_Object = MibTableColumn
kbytesReceived = _KbytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 2, 2, 1, 4),
    _KbytesReceived_Type()
)
kbytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbytesReceived.setStatus("mandatory")
_PacketsTransmitted_Type = Counter32
_PacketsTransmitted_Object = MibTableColumn
packetsTransmitted = _PacketsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 2, 2, 1, 5),
    _PacketsTransmitted_Type()
)
packetsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetsTransmitted.setStatus("mandatory")
_PacketsReceived_Type = Counter32
_PacketsReceived_Object = MibTableColumn
packetsReceived = _PacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 2, 2, 1, 6),
    _PacketsReceived_Type()
)
packetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetsReceived.setStatus("mandatory")
_IsdnloopbackbytesTransmitted_Type = Counter32
_IsdnloopbackbytesTransmitted_Object = MibTableColumn
isdnloopbackbytesTransmitted = _IsdnloopbackbytesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 2, 2, 1, 7),
    _IsdnloopbackbytesTransmitted_Type()
)
isdnloopbackbytesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnloopbackbytesTransmitted.setStatus("mandatory")
_IsdnloopbackbytesReceived_Type = Counter32
_IsdnloopbackbytesReceived_Object = MibTableColumn
isdnloopbackbytesReceived = _IsdnloopbackbytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 2, 2, 1, 8),
    _IsdnloopbackbytesReceived_Type()
)
isdnloopbackbytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnloopbackbytesReceived.setStatus("mandatory")
_IsdnCRCErrors_Type = Counter32
_IsdnCRCErrors_Object = MibTableColumn
isdnCRCErrors = _IsdnCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 2, 2, 1, 9),
    _IsdnCRCErrors_Type()
)
isdnCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCRCErrors.setStatus("mandatory")
_DsucsuControlGroup_ObjectIdentity = ObjectIdentity
dsucsuControlGroup = _DsucsuControlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 3)
)
_DsucsudeviceConfigTable_Object = MibTable
dsucsudeviceConfigTable = _DsucsudeviceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 3, 1)
)
if mibBuilder.loadTexts:
    dsucsudeviceConfigTable.setStatus("mandatory")
_DsucsudeviceConfigEntry_Object = MibTableRow
dsucsudeviceConfigEntry = _DsucsudeviceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 3, 1, 1)
)
dsucsudeviceConfigEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "dsucsuLineNumber"),
)
if mibBuilder.loadTexts:
    dsucsudeviceConfigEntry.setStatus("mandatory")
_DsucsuLineNumber_Type = Integer32
_DsucsuLineNumber_Object = MibTableColumn
dsucsuLineNumber = _DsucsuLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 3, 1, 1, 1),
    _DsucsuLineNumber_Type()
)
dsucsuLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuLineNumber.setStatus("mandatory")


class _DsucsuType_Type(Integer32):
    """Custom type dsucsuType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dsu-csu-async-dial", 2),
          ("dsu-csu-dds", 1))
    )


_DsucsuType_Type.__name__ = "Integer32"
_DsucsuType_Object = MibTableColumn
dsucsuType = _DsucsuType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 3, 1, 1, 2),
    _DsucsuType_Type()
)
dsucsuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuType.setStatus("mandatory")


class _DsucsuClocking_Type(Integer32):
    """Custom type dsucsuClocking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("internal", 2))
    )


_DsucsuClocking_Type.__name__ = "Integer32"
_DsucsuClocking_Object = MibTableColumn
dsucsuClocking = _DsucsuClocking_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 3, 1, 1, 3),
    _DsucsuClocking_Type()
)
dsucsuClocking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuClocking.setStatus("mandatory")


class _DsucsuSpeed_Type(Integer32):
    """Custom type dsucsuSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(560,
              640)
        )
    )
    namedValues = NamedValues(
        *(("speed56000", 560),
          ("speed64000", 640))
    )


_DsucsuSpeed_Type.__name__ = "Integer32"
_DsucsuSpeed_Object = MibTableColumn
dsucsuSpeed = _DsucsuSpeed_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 3, 1, 1, 4),
    _DsucsuSpeed_Type()
)
dsucsuSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuSpeed.setStatus("mandatory")
_DsucsudeviceStatsTable_Object = MibTable
dsucsudeviceStatsTable = _DsucsudeviceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 3, 2)
)
if mibBuilder.loadTexts:
    dsucsudeviceStatsTable.setStatus("mandatory")
_DsucsudeviceStatsEntry_Object = MibTableRow
dsucsudeviceStatsEntry = _DsucsudeviceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 3, 2, 1)
)
dsucsudeviceStatsEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "dsucsuLine"),
)
if mibBuilder.loadTexts:
    dsucsudeviceStatsEntry.setStatus("mandatory")
_DsucsuLine_Type = Integer32
_DsucsuLine_Object = MibTableColumn
dsucsuLine = _DsucsuLine_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 3, 2, 1, 1),
    _DsucsuLine_Type()
)
dsucsuLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuLine.setStatus("mandatory")
_DsucsuloopbackbytesTransmitted_Type = Counter32
_DsucsuloopbackbytesTransmitted_Object = MibTableColumn
dsucsuloopbackbytesTransmitted = _DsucsuloopbackbytesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 3, 2, 1, 2),
    _DsucsuloopbackbytesTransmitted_Type()
)
dsucsuloopbackbytesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuloopbackbytesTransmitted.setStatus("mandatory")
_DsucsuloopbackbytesReceived_Type = Counter32
_DsucsuloopbackbytesReceived_Object = MibTableColumn
dsucsuloopbackbytesReceived = _DsucsuloopbackbytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 2, 3, 2, 1, 3),
    _DsucsuloopbackbytesReceived_Type()
)
dsucsuloopbackbytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuloopbackbytesReceived.setStatus("mandatory")
_LineSDLCGroup_ObjectIdentity = ObjectIdentity
lineSDLCGroup = _LineSDLCGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 3)
)
_SdlcConfigTable_Object = MibTable
sdlcConfigTable = _SdlcConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 3, 1)
)
if mibBuilder.loadTexts:
    sdlcConfigTable.setStatus("mandatory")
_SdlcConfigEntry_Object = MibTableRow
sdlcConfigEntry = _SdlcConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 3, 1, 1)
)
sdlcConfigEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "sdlcConfigPortIndex"),
)
if mibBuilder.loadTexts:
    sdlcConfigEntry.setStatus("mandatory")
_SdlcConfigPortIndex_Type = Integer32
_SdlcConfigPortIndex_Object = MibTableColumn
sdlcConfigPortIndex = _SdlcConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 3, 1, 1, 1),
    _SdlcConfigPortIndex_Type()
)
sdlcConfigPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcConfigPortIndex.setStatus("mandatory")


class _SdlcConfigType_Type(Integer32):
    """Custom type sdlcConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("hsdlc-type", 11),
          ("tsdlc-type", 12))
    )


_SdlcConfigType_Type.__name__ = "Integer32"
_SdlcConfigType_Object = MibTableColumn
sdlcConfigType = _SdlcConfigType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 3, 1, 1, 2),
    _SdlcConfigType_Type()
)
sdlcConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcConfigType.setStatus("mandatory")


class _SdlcInitState_Type(Integer32):
    """Custom type sdlcInitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in-service", 1),
          ("out-of-service", 2))
    )


_SdlcInitState_Type.__name__ = "Integer32"
_SdlcInitState_Object = MibTableColumn
sdlcInitState = _SdlcInitState_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 3, 1, 1, 3),
    _SdlcInitState_Type()
)
sdlcInitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcInitState.setStatus("mandatory")


class _SdlcCarrier_Type(Integer32):
    """Custom type sdlcCarrier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("constant", 1),
          ("switched", 2))
    )


_SdlcCarrier_Type.__name__ = "Integer32"
_SdlcCarrier_Object = MibTableColumn
sdlcCarrier = _SdlcCarrier_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 3, 1, 1, 4),
    _SdlcCarrier_Type()
)
sdlcCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCarrier.setStatus("mandatory")


class _SdlcClocking_Type(Integer32):
    """Custom type sdlcClocking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("internal", 2),
          ("x21-external", 3),
          ("x21-internal", 4))
    )


_SdlcClocking_Type.__name__ = "Integer32"
_SdlcClocking_Object = MibTableColumn
sdlcClocking = _SdlcClocking_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 3, 1, 1, 5),
    _SdlcClocking_Type()
)
sdlcClocking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcClocking.setStatus("mandatory")


class _SdlcSpeed_Type(Integer32):
    """Custom type sdlcSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(12,
              20,
              24,
              36,
              48,
              72,
              96,
              144,
              192,
              288,
              480,
              560,
              640,
              1280)
        )
    )
    namedValues = NamedValues(
        *(("speed1200", 12),
          ("speed128000", 1280),
          ("speed14400", 144),
          ("speed19200", 192),
          ("speed2000", 20),
          ("speed2400", 24),
          ("speed28800", 288),
          ("speed3600", 36),
          ("speed4800", 48),
          ("speed48000", 480),
          ("speed56000", 560),
          ("speed64000", 640),
          ("speed7200", 72),
          ("speed9600", 96))
    )


_SdlcSpeed_Type.__name__ = "Integer32"
_SdlcSpeed_Object = MibTableColumn
sdlcSpeed = _SdlcSpeed_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 3, 1, 1, 6),
    _SdlcSpeed_Type()
)
sdlcSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcSpeed.setStatus("mandatory")
_SdlcPause_Type = Integer32
_SdlcPause_Object = MibTableColumn
sdlcPause = _SdlcPause_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 3, 1, 1, 7),
    _SdlcPause_Type()
)
sdlcPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPause.setStatus("mandatory")


class _SdlcNRZI_Type(Integer32):
    """Custom type sdlcNRZI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SdlcNRZI_Type.__name__ = "Integer32"
_SdlcNRZI_Object = MibTableColumn
sdlcNRZI = _SdlcNRZI_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 3, 1, 1, 8),
    _SdlcNRZI_Type()
)
sdlcNRZI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcNRZI.setStatus("mandatory")
_SdlcT1Timer_Type = Integer32
_SdlcT1Timer_Object = MibTableColumn
sdlcT1Timer = _SdlcT1Timer_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 3, 1, 1, 9),
    _SdlcT1Timer_Type()
)
sdlcT1Timer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcT1Timer.setStatus("mandatory")
_SdlcSlowPollTimer_Type = Integer32
_SdlcSlowPollTimer_Object = MibTableColumn
sdlcSlowPollTimer = _SdlcSlowPollTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 3, 1, 1, 10),
    _SdlcSlowPollTimer_Type()
)
sdlcSlowPollTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcSlowPollTimer.setStatus("mandatory")


class _SdlcMaxRetries_Type(Integer32):
    """Custom type sdlcMaxRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_SdlcMaxRetries_Type.__name__ = "Integer32"
_SdlcMaxRetries_Object = MibTableColumn
sdlcMaxRetries = _SdlcMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 3, 1, 1, 11),
    _SdlcMaxRetries_Type()
)
sdlcMaxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcMaxRetries.setStatus("mandatory")


class _SdlcNAUName_Type(DisplayString):
    """Custom type sdlcNAUName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_SdlcNAUName_Type.__name__ = "DisplayString"
_SdlcNAUName_Object = MibTableColumn
sdlcNAUName = _SdlcNAUName_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 3, 1, 1, 12),
    _SdlcNAUName_Type()
)
sdlcNAUName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcNAUName.setStatus("mandatory")


class _SdlcMultiFlagInsertion_Type(Integer32):
    """Custom type sdlcMultiFlagInsertion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SdlcMultiFlagInsertion_Type.__name__ = "Integer32"
_SdlcMultiFlagInsertion_Object = MibTableColumn
sdlcMultiFlagInsertion = _SdlcMultiFlagInsertion_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 3, 1, 1, 13),
    _SdlcMultiFlagInsertion_Type()
)
sdlcMultiFlagInsertion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcMultiFlagInsertion.setStatus("mandatory")


class _SdlcCTS_Type(Integer32):
    """Custom type sdlcCTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SdlcCTS_Type.__name__ = "Integer32"
_SdlcCTS_Object = MibTableColumn
sdlcCTS = _SdlcCTS_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 3, 1, 1, 14),
    _SdlcCTS_Type()
)
sdlcCTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCTS.setStatus("mandatory")


class _SdlcDCD_Type(Integer32):
    """Custom type sdlcDCD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SdlcDCD_Type.__name__ = "Integer32"
_SdlcDCD_Object = MibTableColumn
sdlcDCD = _SdlcDCD_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 3, 1, 1, 15),
    _SdlcDCD_Type()
)
sdlcDCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcDCD.setStatus("mandatory")


class _SdlcDSR_Type(Integer32):
    """Custom type sdlcDSR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SdlcDSR_Type.__name__ = "Integer32"
_SdlcDSR_Object = MibTableColumn
sdlcDSR = _SdlcDSR_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 3, 1, 1, 16),
    _SdlcDSR_Type()
)
sdlcDSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcDSR.setStatus("mandatory")


class _SdlcDTR_Type(Integer32):
    """Custom type sdlcDTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SdlcDTR_Type.__name__ = "Integer32"
_SdlcDTR_Object = MibTableColumn
sdlcDTR = _SdlcDTR_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 3, 1, 1, 17),
    _SdlcDTR_Type()
)
sdlcDTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcDTR.setStatus("mandatory")


class _SdlcRTS_Type(Integer32):
    """Custom type sdlcRTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SdlcRTS_Type.__name__ = "Integer32"
_SdlcRTS_Object = MibTableColumn
sdlcRTS = _SdlcRTS_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 3, 1, 1, 18),
    _SdlcRTS_Type()
)
sdlcRTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcRTS.setStatus("mandatory")


class _SdlcReturnClock_Type(Integer32):
    """Custom type sdlcReturnClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("no", 2),
          ("yes", 1))
    )


_SdlcReturnClock_Type.__name__ = "Integer32"
_SdlcReturnClock_Object = MibTableColumn
sdlcReturnClock = _SdlcReturnClock_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 3, 1, 1, 19),
    _SdlcReturnClock_Type()
)
sdlcReturnClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcReturnClock.setStatus("mandatory")
_SdlcStatsTable_Object = MibTable
sdlcStatsTable = _SdlcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 3, 2)
)
if mibBuilder.loadTexts:
    sdlcStatsTable.setStatus("mandatory")
_SdlcStatsEntry_Object = MibTableRow
sdlcStatsEntry = _SdlcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 3, 2, 1)
)
sdlcStatsEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "sdlcStatsPortIndex"),
)
if mibBuilder.loadTexts:
    sdlcStatsEntry.setStatus("mandatory")
_SdlcStatsPortIndex_Type = Integer32
_SdlcStatsPortIndex_Object = MibTableColumn
sdlcStatsPortIndex = _SdlcStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 3, 2, 1, 1),
    _SdlcStatsPortIndex_Type()
)
sdlcStatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcStatsPortIndex.setStatus("mandatory")


class _SdlcPortType_Type(Integer32):
    """Custom type sdlcPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("hsdlc-type", 11),
          ("tsdlc-type", 12))
    )


_SdlcPortType_Type.__name__ = "Integer32"
_SdlcPortType_Object = MibTableColumn
sdlcPortType = _SdlcPortType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 3, 2, 1, 2),
    _SdlcPortType_Type()
)
sdlcPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortType.setStatus("mandatory")
_SdlcInOctets_Type = Counter32
_SdlcInOctets_Object = MibTableColumn
sdlcInOctets = _SdlcInOctets_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 3, 2, 1, 3),
    _SdlcInOctets_Type()
)
sdlcInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcInOctets.setStatus("mandatory")
_SdlcOutOctets_Type = Counter32
_SdlcOutOctets_Object = MibTableColumn
sdlcOutOctets = _SdlcOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 3, 2, 1, 4),
    _SdlcOutOctets_Type()
)
sdlcOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcOutOctets.setStatus("mandatory")
_SdlcInFrames_Type = Counter32
_SdlcInFrames_Object = MibTableColumn
sdlcInFrames = _SdlcInFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 3, 2, 1, 5),
    _SdlcInFrames_Type()
)
sdlcInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcInFrames.setStatus("mandatory")
_SdlcOutFrames_Type = Counter32
_SdlcOutFrames_Object = MibTableColumn
sdlcOutFrames = _SdlcOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 3, 2, 1, 6),
    _SdlcOutFrames_Type()
)
sdlcOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcOutFrames.setStatus("mandatory")
_SdlcOverruns_Type = Counter32
_SdlcOverruns_Object = MibTableColumn
sdlcOverruns = _SdlcOverruns_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 3, 2, 1, 7),
    _SdlcOverruns_Type()
)
sdlcOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcOverruns.setStatus("mandatory")
_SdlcCRCErrors_Type = Counter32
_SdlcCRCErrors_Object = MibTableColumn
sdlcCRCErrors = _SdlcCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 3, 2, 1, 8),
    _SdlcCRCErrors_Type()
)
sdlcCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCRCErrors.setStatus("mandatory")
_SdlcRecvAborts_Type = Counter32
_SdlcRecvAborts_Object = MibTableColumn
sdlcRecvAborts = _SdlcRecvAborts_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 3, 2, 1, 9),
    _SdlcRecvAborts_Type()
)
sdlcRecvAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcRecvAborts.setStatus("mandatory")
_Sdlcpollrsptimeouts_Type = Counter32
_Sdlcpollrsptimeouts_Object = MibTableColumn
sdlcpollrsptimeouts = _Sdlcpollrsptimeouts_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 3, 2, 1, 10),
    _Sdlcpollrsptimeouts_Type()
)
sdlcpollrsptimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcpollrsptimeouts.setStatus("mandatory")
_Sdlciframetrans_Type = Counter32
_Sdlciframetrans_Object = MibTableColumn
sdlciframetrans = _Sdlciframetrans_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 3, 2, 1, 11),
    _Sdlciframetrans_Type()
)
sdlciframetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlciframetrans.setStatus("mandatory")
_LineBisyncGroup_ObjectIdentity = ObjectIdentity
lineBisyncGroup = _LineBisyncGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 4)
)
_BisyncConfigTable_Object = MibTable
bisyncConfigTable = _BisyncConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 4, 1)
)
if mibBuilder.loadTexts:
    bisyncConfigTable.setStatus("mandatory")
_BisyncConfigEntry_Object = MibTableRow
bisyncConfigEntry = _BisyncConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 4, 1, 1)
)
bisyncConfigEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "bisyncConfigPortIndex"),
)
if mibBuilder.loadTexts:
    bisyncConfigEntry.setStatus("mandatory")
_BisyncConfigPortIndex_Type = Integer32
_BisyncConfigPortIndex_Object = MibTableColumn
bisyncConfigPortIndex = _BisyncConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 4, 1, 1, 1),
    _BisyncConfigPortIndex_Type()
)
bisyncConfigPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncConfigPortIndex.setStatus("mandatory")


class _BisyncConfigType_Type(Integer32):
    """Custom type bisyncConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hbsc-type", 1),
          ("tbsc-type", 2))
    )


_BisyncConfigType_Type.__name__ = "Integer32"
_BisyncConfigType_Object = MibTableColumn
bisyncConfigType = _BisyncConfigType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 4, 1, 1, 2),
    _BisyncConfigType_Type()
)
bisyncConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncConfigType.setStatus("mandatory")


class _BisyncNAUName_Type(DisplayString):
    """Custom type bisyncNAUName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_BisyncNAUName_Type.__name__ = "DisplayString"
_BisyncNAUName_Object = MibTableColumn
bisyncNAUName = _BisyncNAUName_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 4, 1, 1, 3),
    _BisyncNAUName_Type()
)
bisyncNAUName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncNAUName.setStatus("mandatory")


class _BisyncInitState_Type(Integer32):
    """Custom type bisyncInitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in-service", 1),
          ("out-of-service", 2))
    )


_BisyncInitState_Type.__name__ = "Integer32"
_BisyncInitState_Object = MibTableColumn
bisyncInitState = _BisyncInitState_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 4, 1, 1, 4),
    _BisyncInitState_Type()
)
bisyncInitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncInitState.setStatus("mandatory")


class _BisyncCarrier_Type(Integer32):
    """Custom type bisyncCarrier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("constant", 1),
          ("switched", 2))
    )


_BisyncCarrier_Type.__name__ = "Integer32"
_BisyncCarrier_Object = MibTableColumn
bisyncCarrier = _BisyncCarrier_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 4, 1, 1, 5),
    _BisyncCarrier_Type()
)
bisyncCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncCarrier.setStatus("mandatory")


class _BisyncClocking_Type(Integer32):
    """Custom type bisyncClocking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("internal", 2),
          ("x21-external", 3),
          ("x21-internal", 4))
    )


_BisyncClocking_Type.__name__ = "Integer32"
_BisyncClocking_Object = MibTableColumn
bisyncClocking = _BisyncClocking_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 4, 1, 1, 6),
    _BisyncClocking_Type()
)
bisyncClocking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncClocking.setStatus("mandatory")


class _BisyncSpeed_Type(Integer32):
    """Custom type bisyncSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(12,
              20,
              24,
              36,
              48,
              72,
              96,
              144,
              192,
              288,
              480,
              560,
              640)
        )
    )
    namedValues = NamedValues(
        *(("speed1200", 12),
          ("speed14400", 144),
          ("speed19200", 192),
          ("speed2000", 20),
          ("speed2400", 24),
          ("speed28800", 288),
          ("speed3600", 36),
          ("speed4800", 48),
          ("speed48000", 480),
          ("speed56000", 560),
          ("speed64000", 640),
          ("speed7200", 72),
          ("speed9600", 96))
    )


_BisyncSpeed_Type.__name__ = "Integer32"
_BisyncSpeed_Object = MibTableColumn
bisyncSpeed = _BisyncSpeed_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 4, 1, 1, 7),
    _BisyncSpeed_Type()
)
bisyncSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncSpeed.setStatus("mandatory")
_BisyncPause_Type = Integer32
_BisyncPause_Object = MibTableColumn
bisyncPause = _BisyncPause_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 4, 1, 1, 8),
    _BisyncPause_Type()
)
bisyncPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncPause.setStatus("mandatory")


class _BisyncReplyTimer_Type(Integer32):
    """Custom type bisyncReplyTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_BisyncReplyTimer_Type.__name__ = "Integer32"
_BisyncReplyTimer_Object = MibTableColumn
bisyncReplyTimer = _BisyncReplyTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 4, 1, 1, 9),
    _BisyncReplyTimer_Type()
)
bisyncReplyTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncReplyTimer.setStatus("mandatory")


class _BisyncRetries_Type(Integer32):
    """Custom type bisyncRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_BisyncRetries_Type.__name__ = "Integer32"
_BisyncRetries_Object = MibTableColumn
bisyncRetries = _BisyncRetries_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 4, 1, 1, 10),
    _BisyncRetries_Type()
)
bisyncRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncRetries.setStatus("mandatory")


class _BisyncSlowpollTimer_Type(Integer32):
    """Custom type bisyncSlowpollTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_BisyncSlowpollTimer_Type.__name__ = "Integer32"
_BisyncSlowpollTimer_Object = MibTableColumn
bisyncSlowpollTimer = _BisyncSlowpollTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 4, 1, 1, 11),
    _BisyncSlowpollTimer_Type()
)
bisyncSlowpollTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncSlowpollTimer.setStatus("mandatory")


class _BisyncSessTerm_Type(Integer32):
    """Custom type bisyncSessTerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("interventionReq", 2),
          ("none", 1),
          ("unformattedLogoff", 3))
    )


_BisyncSessTerm_Type.__name__ = "Integer32"
_BisyncSessTerm_Object = MibTableColumn
bisyncSessTerm = _BisyncSessTerm_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 4, 1, 1, 12),
    _BisyncSessTerm_Type()
)
bisyncSessTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncSessTerm.setStatus("mandatory")


class _BisyncIBS_Type(Integer32):
    """Custom type bisyncIBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_BisyncIBS_Type.__name__ = "Integer32"
_BisyncIBS_Object = MibTableColumn
bisyncIBS = _BisyncIBS_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 4, 1, 1, 13),
    _BisyncIBS_Type()
)
bisyncIBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncIBS.setStatus("mandatory")


class _BisyncCTS_Type(Integer32):
    """Custom type bisyncCTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_BisyncCTS_Type.__name__ = "Integer32"
_BisyncCTS_Object = MibTableColumn
bisyncCTS = _BisyncCTS_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 4, 1, 1, 14),
    _BisyncCTS_Type()
)
bisyncCTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncCTS.setStatus("mandatory")


class _BisyncDCD_Type(Integer32):
    """Custom type bisyncDCD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_BisyncDCD_Type.__name__ = "Integer32"
_BisyncDCD_Object = MibTableColumn
bisyncDCD = _BisyncDCD_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 4, 1, 1, 15),
    _BisyncDCD_Type()
)
bisyncDCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncDCD.setStatus("mandatory")


class _BisyncDSR_Type(Integer32):
    """Custom type bisyncDSR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_BisyncDSR_Type.__name__ = "Integer32"
_BisyncDSR_Object = MibTableColumn
bisyncDSR = _BisyncDSR_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 4, 1, 1, 16),
    _BisyncDSR_Type()
)
bisyncDSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncDSR.setStatus("mandatory")


class _BisyncDTR_Type(Integer32):
    """Custom type bisyncDTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_BisyncDTR_Type.__name__ = "Integer32"
_BisyncDTR_Object = MibTableColumn
bisyncDTR = _BisyncDTR_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 4, 1, 1, 17),
    _BisyncDTR_Type()
)
bisyncDTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncDTR.setStatus("mandatory")


class _BisyncRTS_Type(Integer32):
    """Custom type bisyncRTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_BisyncRTS_Type.__name__ = "Integer32"
_BisyncRTS_Object = MibTableColumn
bisyncRTS = _BisyncRTS_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 4, 1, 1, 18),
    _BisyncRTS_Type()
)
bisyncRTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncRTS.setStatus("mandatory")


class _BisyncReturnClock_Type(Integer32):
    """Custom type bisyncReturnClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("no", 2),
          ("yes", 1))
    )


_BisyncReturnClock_Type.__name__ = "Integer32"
_BisyncReturnClock_Object = MibTableColumn
bisyncReturnClock = _BisyncReturnClock_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 4, 1, 1, 19),
    _BisyncReturnClock_Type()
)
bisyncReturnClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncReturnClock.setStatus("mandatory")
_BisyncStatsTable_Object = MibTable
bisyncStatsTable = _BisyncStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 4, 2)
)
if mibBuilder.loadTexts:
    bisyncStatsTable.setStatus("mandatory")
_BisyncStatsEntry_Object = MibTableRow
bisyncStatsEntry = _BisyncStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 4, 2, 1)
)
bisyncStatsEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "bisyncStatsPortIndex"),
)
if mibBuilder.loadTexts:
    bisyncStatsEntry.setStatus("mandatory")
_BisyncStatsPortIndex_Type = Integer32
_BisyncStatsPortIndex_Object = MibTableColumn
bisyncStatsPortIndex = _BisyncStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 4, 2, 1, 1),
    _BisyncStatsPortIndex_Type()
)
bisyncStatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncStatsPortIndex.setStatus("mandatory")


class _BisyncPortType_Type(Integer32):
    """Custom type bisyncPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hbsc-type", 1),
          ("tbsc-type", 2))
    )


_BisyncPortType_Type.__name__ = "Integer32"
_BisyncPortType_Object = MibTableColumn
bisyncPortType = _BisyncPortType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 4, 2, 1, 2),
    _BisyncPortType_Type()
)
bisyncPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncPortType.setStatus("mandatory")
_BisyncInOctets_Type = Counter32
_BisyncInOctets_Object = MibTableColumn
bisyncInOctets = _BisyncInOctets_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 4, 2, 1, 3),
    _BisyncInOctets_Type()
)
bisyncInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncInOctets.setStatus("mandatory")
_BisyncOutOctets_Type = Counter32
_BisyncOutOctets_Object = MibTableColumn
bisyncOutOctets = _BisyncOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 4, 2, 1, 4),
    _BisyncOutOctets_Type()
)
bisyncOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncOutOctets.setStatus("mandatory")
_BisyncOverruns_Type = Counter32
_BisyncOverruns_Object = MibTableColumn
bisyncOverruns = _BisyncOverruns_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 4, 2, 1, 5),
    _BisyncOverruns_Type()
)
bisyncOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncOverruns.setStatus("mandatory")
_BisyncCRCErrors_Type = Counter32
_BisyncCRCErrors_Object = MibTableColumn
bisyncCRCErrors = _BisyncCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 4, 2, 1, 6),
    _BisyncCRCErrors_Type()
)
bisyncCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncCRCErrors.setStatus("mandatory")
_BisyncRcvTimeout_Type = Counter32
_BisyncRcvTimeout_Object = MibTableColumn
bisyncRcvTimeout = _BisyncRcvTimeout_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 4, 2, 1, 7),
    _BisyncRcvTimeout_Type()
)
bisyncRcvTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncRcvTimeout.setStatus("mandatory")
_BisyncXmtTimeout_Type = Counter32
_BisyncXmtTimeout_Object = MibTableColumn
bisyncXmtTimeout = _BisyncXmtTimeout_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 4, 2, 1, 8),
    _BisyncXmtTimeout_Type()
)
bisyncXmtTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncXmtTimeout.setStatus("mandatory")
_LineFrameRelayGroup_ObjectIdentity = ObjectIdentity
lineFrameRelayGroup = _LineFrameRelayGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5)
)
_FrameRelayConfigTable_Object = MibTable
frameRelayConfigTable = _FrameRelayConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1)
)
if mibBuilder.loadTexts:
    frameRelayConfigTable.setStatus("mandatory")
_FrameRelayConfigEntry_Object = MibTableRow
frameRelayConfigEntry = _FrameRelayConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1)
)
frameRelayConfigEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "frameRelayConfigPortIndex"),
)
if mibBuilder.loadTexts:
    frameRelayConfigEntry.setStatus("mandatory")
_FrameRelayConfigPortIndex_Type = Integer32
_FrameRelayConfigPortIndex_Object = MibTableColumn
frameRelayConfigPortIndex = _FrameRelayConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 1),
    _FrameRelayConfigPortIndex_Type()
)
frameRelayConfigPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayConfigPortIndex.setStatus("mandatory")


class _FrameRelayPortType_Type(Integer32):
    """Custom type frameRelayPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("frame-relay-dialbackup-type", 20),
          ("frame-relay-type", 19))
    )


_FrameRelayPortType_Type.__name__ = "Integer32"
_FrameRelayPortType_Object = MibTableColumn
frameRelayPortType = _FrameRelayPortType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 2),
    _FrameRelayPortType_Type()
)
frameRelayPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayPortType.setStatus("mandatory")


class _FrameRelayInitState_Type(Integer32):
    """Custom type frameRelayInitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in-service", 1),
          ("out-of-service", 2))
    )


_FrameRelayInitState_Type.__name__ = "Integer32"
_FrameRelayInitState_Object = MibTableColumn
frameRelayInitState = _FrameRelayInitState_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 3),
    _FrameRelayInitState_Type()
)
frameRelayInitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayInitState.setStatus("mandatory")


class _FrameRelayClocking_Type(Integer32):
    """Custom type frameRelayClocking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("internal", 2),
          ("x21-external", 3),
          ("x21-internal", 4))
    )


_FrameRelayClocking_Type.__name__ = "Integer32"
_FrameRelayClocking_Object = MibTableColumn
frameRelayClocking = _FrameRelayClocking_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 4),
    _FrameRelayClocking_Type()
)
frameRelayClocking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayClocking.setStatus("mandatory")


class _FrameRelaySpeed_Type(Integer32):
    """Custom type frameRelaySpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(12,
              20,
              24,
              36,
              48,
              72,
              96,
              144,
              192,
              288,
              480,
              560,
              640,
              1280,
              2560,
              5120,
              10240,
              15440,
              20480)
        )
    )
    namedValues = NamedValues(
        *(("speed102400", 10240),
          ("speed1200", 12),
          ("speed128000", 1280),
          ("speed14400", 144),
          ("speed154400", 15440),
          ("speed19200", 192),
          ("speed2000", 20),
          ("speed204800", 20480),
          ("speed2400", 24),
          ("speed256000", 2560),
          ("speed28800", 288),
          ("speed3600", 36),
          ("speed4800", 48),
          ("speed48000", 480),
          ("speed512000", 5120),
          ("speed56000", 560),
          ("speed64000", 640),
          ("speed7200", 72),
          ("speed9600", 96))
    )


_FrameRelaySpeed_Type.__name__ = "Integer32"
_FrameRelaySpeed_Object = MibTableColumn
frameRelaySpeed = _FrameRelaySpeed_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 5),
    _FrameRelaySpeed_Type()
)
frameRelaySpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelaySpeed.setStatus("mandatory")


class _FrameRelayLocalManagementProtocol_Type(Integer32):
    """Custom type frameRelayLocalManagementProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("annexA", 3),
          ("annexD", 1),
          ("lmi", 2))
    )


_FrameRelayLocalManagementProtocol_Type.__name__ = "Integer32"
_FrameRelayLocalManagementProtocol_Object = MibTableColumn
frameRelayLocalManagementProtocol = _FrameRelayLocalManagementProtocol_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 6),
    _FrameRelayLocalManagementProtocol_Type()
)
frameRelayLocalManagementProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayLocalManagementProtocol.setStatus("mandatory")


class _FrameRelayLinkPollingTimer_Type(Integer32):
    """Custom type frameRelayLinkPollingTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_FrameRelayLinkPollingTimer_Type.__name__ = "Integer32"
_FrameRelayLinkPollingTimer_Object = MibTableColumn
frameRelayLinkPollingTimer = _FrameRelayLinkPollingTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 7),
    _FrameRelayLinkPollingTimer_Type()
)
frameRelayLinkPollingTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayLinkPollingTimer.setStatus("mandatory")


class _FrameRelayFullStatusPollingCount_Type(Integer32):
    """Custom type frameRelayFullStatusPollingCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FrameRelayFullStatusPollingCount_Type.__name__ = "Integer32"
_FrameRelayFullStatusPollingCount_Object = MibTableColumn
frameRelayFullStatusPollingCount = _FrameRelayFullStatusPollingCount_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 8),
    _FrameRelayFullStatusPollingCount_Type()
)
frameRelayFullStatusPollingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayFullStatusPollingCount.setStatus("mandatory")


class _FrameRelayT1Timer_Type(Integer32):
    """Custom type frameRelayT1Timer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_FrameRelayT1Timer_Type.__name__ = "Integer32"
_FrameRelayT1Timer_Object = MibTableColumn
frameRelayT1Timer = _FrameRelayT1Timer_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 9),
    _FrameRelayT1Timer_Type()
)
frameRelayT1Timer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayT1Timer.setStatus("mandatory")


class _FrameRelayT2Timer_Type(Integer32):
    """Custom type frameRelayT2Timer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_FrameRelayT2Timer_Type.__name__ = "Integer32"
_FrameRelayT2Timer_Object = MibTableColumn
frameRelayT2Timer = _FrameRelayT2Timer_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 10),
    _FrameRelayT2Timer_Type()
)
frameRelayT2Timer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayT2Timer.setStatus("mandatory")


class _FrameRelayTiTimer_Type(Integer32):
    """Custom type frameRelayTiTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 50),
    )


_FrameRelayTiTimer_Type.__name__ = "Integer32"
_FrameRelayTiTimer_Object = MibTableColumn
frameRelayTiTimer = _FrameRelayTiTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 11),
    _FrameRelayTiTimer_Type()
)
frameRelayTiTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayTiTimer.setStatus("mandatory")


class _FrameRelayRxWindowSize_Type(Integer32):
    """Custom type frameRelayRxWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_FrameRelayRxWindowSize_Type.__name__ = "Integer32"
_FrameRelayRxWindowSize_Object = MibTableColumn
frameRelayRxWindowSize = _FrameRelayRxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 12),
    _FrameRelayRxWindowSize_Type()
)
frameRelayRxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayRxWindowSize.setStatus("mandatory")


class _FrameRelayTxWindowSize_Type(Integer32):
    """Custom type frameRelayTxWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_FrameRelayTxWindowSize_Type.__name__ = "Integer32"
_FrameRelayTxWindowSize_Object = MibTableColumn
frameRelayTxWindowSize = _FrameRelayTxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 13),
    _FrameRelayTxWindowSize_Type()
)
frameRelayTxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayTxWindowSize.setStatus("mandatory")


class _FrameRelayMaxRetries_Type(Integer32):
    """Custom type frameRelayMaxRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_FrameRelayMaxRetries_Type.__name__ = "Integer32"
_FrameRelayMaxRetries_Object = MibTableColumn
frameRelayMaxRetries = _FrameRelayMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 14),
    _FrameRelayMaxRetries_Type()
)
frameRelayMaxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayMaxRetries.setStatus("mandatory")


class _FrameRelayNAUName_Type(DisplayString):
    """Custom type frameRelayNAUName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_FrameRelayNAUName_Type.__name__ = "DisplayString"
_FrameRelayNAUName_Object = MibTableColumn
frameRelayNAUName = _FrameRelayNAUName_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 15),
    _FrameRelayNAUName_Type()
)
frameRelayNAUName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayNAUName.setStatus("mandatory")
_FrameRelayVirtualMACAddress_Type = PhysAddress
_FrameRelayVirtualMACAddress_Object = MibTableColumn
frameRelayVirtualMACAddress = _FrameRelayVirtualMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 16),
    _FrameRelayVirtualMACAddress_Type()
)
frameRelayVirtualMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayVirtualMACAddress.setStatus("mandatory")


class _FrameRelayVirtualRingNumber_Type(Integer32):
    """Custom type frameRelayVirtualRingNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_FrameRelayVirtualRingNumber_Type.__name__ = "Integer32"
_FrameRelayVirtualRingNumber_Object = MibTableColumn
frameRelayVirtualRingNumber = _FrameRelayVirtualRingNumber_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 17),
    _FrameRelayVirtualRingNumber_Type()
)
frameRelayVirtualRingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayVirtualRingNumber.setStatus("mandatory")


class _FrameRelayVirtualBridgeNumber_Type(Integer32):
    """Custom type frameRelayVirtualBridgeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_FrameRelayVirtualBridgeNumber_Type.__name__ = "Integer32"
_FrameRelayVirtualBridgeNumber_Object = MibTableColumn
frameRelayVirtualBridgeNumber = _FrameRelayVirtualBridgeNumber_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 18),
    _FrameRelayVirtualBridgeNumber_Type()
)
frameRelayVirtualBridgeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayVirtualBridgeNumber.setStatus("mandatory")
_FrameRelayIPAddress_Type = IpAddress
_FrameRelayIPAddress_Object = MibTableColumn
frameRelayIPAddress = _FrameRelayIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 19),
    _FrameRelayIPAddress_Type()
)
frameRelayIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayIPAddress.setStatus("mandatory")
_FrameRelayNetworkMask_Type = IpAddress
_FrameRelayNetworkMask_Object = MibTableColumn
frameRelayNetworkMask = _FrameRelayNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 20),
    _FrameRelayNetworkMask_Type()
)
frameRelayNetworkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayNetworkMask.setStatus("mandatory")
_FrameRelayDefaultGatewayAddress_Type = IpAddress
_FrameRelayDefaultGatewayAddress_Object = MibTableColumn
frameRelayDefaultGatewayAddress = _FrameRelayDefaultGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 21),
    _FrameRelayDefaultGatewayAddress_Type()
)
frameRelayDefaultGatewayAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayDefaultGatewayAddress.setStatus("mandatory")


class _FrameRelaySessSwitchThreshold_Type(Integer32):
    """Custom type frameRelaySessSwitchThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FrameRelaySessSwitchThreshold_Type.__name__ = "Integer32"
_FrameRelaySessSwitchThreshold_Object = MibTableColumn
frameRelaySessSwitchThreshold = _FrameRelaySessSwitchThreshold_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 22),
    _FrameRelaySessSwitchThreshold_Type()
)
frameRelaySessSwitchThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelaySessSwitchThreshold.setStatus("mandatory")


class _FrameRelaySwitchedBackup_Type(Integer32):
    """Custom type frameRelaySwitchedBackup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("racal-dtr-initiated", 2))
    )


_FrameRelaySwitchedBackup_Type.__name__ = "Integer32"
_FrameRelaySwitchedBackup_Object = MibTableColumn
frameRelaySwitchedBackup = _FrameRelaySwitchedBackup_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 23),
    _FrameRelaySwitchedBackup_Type()
)
frameRelaySwitchedBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelaySwitchedBackup.setStatus("mandatory")


class _FrameRelaySwitchedLineWaitTimer_Type(Integer32):
    """Custom type frameRelaySwitchedLineWaitTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_FrameRelaySwitchedLineWaitTimer_Type.__name__ = "Integer32"
_FrameRelaySwitchedLineWaitTimer_Object = MibTableColumn
frameRelaySwitchedLineWaitTimer = _FrameRelaySwitchedLineWaitTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 24),
    _FrameRelaySwitchedLineWaitTimer_Type()
)
frameRelaySwitchedLineWaitTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelaySwitchedLineWaitTimer.setStatus("mandatory")


class _FrameRelayDedLineWaitTimer_Type(Integer32):
    """Custom type frameRelayDedLineWaitTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120),
    )


_FrameRelayDedLineWaitTimer_Type.__name__ = "Integer32"
_FrameRelayDedLineWaitTimer_Object = MibTableColumn
frameRelayDedLineWaitTimer = _FrameRelayDedLineWaitTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 25),
    _FrameRelayDedLineWaitTimer_Type()
)
frameRelayDedLineWaitTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayDedLineWaitTimer.setStatus("mandatory")
_FrameRelayCommittedBurst_Type = Integer32
_FrameRelayCommittedBurst_Object = MibTableColumn
frameRelayCommittedBurst = _FrameRelayCommittedBurst_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 26),
    _FrameRelayCommittedBurst_Type()
)
frameRelayCommittedBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayCommittedBurst.setStatus("mandatory")
_FrameRelayExcessBurst_Type = Integer32
_FrameRelayExcessBurst_Object = MibTableColumn
frameRelayExcessBurst = _FrameRelayExcessBurst_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 27),
    _FrameRelayExcessBurst_Type()
)
frameRelayExcessBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayExcessBurst.setStatus("mandatory")


class _FrameRelayBridgingProtocol_Type(Integer32):
    """Custom type frameRelayBridgingProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("srb", 1),
          ("tbr", 2))
    )


_FrameRelayBridgingProtocol_Type.__name__ = "Integer32"
_FrameRelayBridgingProtocol_Object = MibTableColumn
frameRelayBridgingProtocol = _FrameRelayBridgingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 28),
    _FrameRelayBridgingProtocol_Type()
)
frameRelayBridgingProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayBridgingProtocol.setStatus("mandatory")


class _FrameRelayProxyARP_Type(Integer32):
    """Custom type frameRelayProxyARP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_FrameRelayProxyARP_Type.__name__ = "Integer32"
_FrameRelayProxyARP_Object = MibTableColumn
frameRelayProxyARP = _FrameRelayProxyARP_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 29),
    _FrameRelayProxyARP_Type()
)
frameRelayProxyARP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayProxyARP.setStatus("mandatory")
_FrameRelaySecondDefaultGatewayAddress_Type = IpAddress
_FrameRelaySecondDefaultGatewayAddress_Object = MibTableColumn
frameRelaySecondDefaultGatewayAddress = _FrameRelaySecondDefaultGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 30),
    _FrameRelaySecondDefaultGatewayAddress_Type()
)
frameRelaySecondDefaultGatewayAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelaySecondDefaultGatewayAddress.setStatus("mandatory")
_FrameRelayAlternateIPAddress_Type = IpAddress
_FrameRelayAlternateIPAddress_Object = MibTableColumn
frameRelayAlternateIPAddress = _FrameRelayAlternateIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 31),
    _FrameRelayAlternateIPAddress_Type()
)
frameRelayAlternateIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayAlternateIPAddress.setStatus("mandatory")
_FrameRelayAlternateNetmask_Type = IpAddress
_FrameRelayAlternateNetmask_Object = MibTableColumn
frameRelayAlternateNetmask = _FrameRelayAlternateNetmask_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 32),
    _FrameRelayAlternateNetmask_Type()
)
frameRelayAlternateNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayAlternateNetmask.setStatus("mandatory")


class _FrameRelayLLC2FrameFormat_Type(Integer32):
    """Custom type frameRelayLLC2FrameFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("all", 4),
          ("ethernetVersiontwo", 2),
          ("iEEEeightotwothree", 3),
          ("tokenRing", 1))
    )


_FrameRelayLLC2FrameFormat_Type.__name__ = "Integer32"
_FrameRelayLLC2FrameFormat_Object = MibTableColumn
frameRelayLLC2FrameFormat = _FrameRelayLLC2FrameFormat_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 33),
    _FrameRelayLLC2FrameFormat_Type()
)
frameRelayLLC2FrameFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayLLC2FrameFormat.setStatus("mandatory")


class _FrameRelayMultiflagSeparation_Type(Integer32):
    """Custom type frameRelayMultiflagSeparation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_FrameRelayMultiflagSeparation_Type.__name__ = "Integer32"
_FrameRelayMultiflagSeparation_Object = MibTableColumn
frameRelayMultiflagSeparation = _FrameRelayMultiflagSeparation_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 34),
    _FrameRelayMultiflagSeparation_Type()
)
frameRelayMultiflagSeparation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayMultiflagSeparation.setStatus("mandatory")


class _FrameRelayRestrictTerminateSessUsage_Type(Integer32):
    """Custom type frameRelayRestrictTerminateSessUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("spanningTree", 2))
    )


_FrameRelayRestrictTerminateSessUsage_Type.__name__ = "Integer32"
_FrameRelayRestrictTerminateSessUsage_Object = MibTableColumn
frameRelayRestrictTerminateSessUsage = _FrameRelayRestrictTerminateSessUsage_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 35),
    _FrameRelayRestrictTerminateSessUsage_Type()
)
frameRelayRestrictTerminateSessUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayRestrictTerminateSessUsage.setStatus("mandatory")


class _FrameRelayRIPUpdtTimer_Type(Integer32):
    """Custom type frameRelayRIPUpdtTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 180),
    )


_FrameRelayRIPUpdtTimer_Type.__name__ = "Integer32"
_FrameRelayRIPUpdtTimer_Object = MibTableColumn
frameRelayRIPUpdtTimer = _FrameRelayRIPUpdtTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 36),
    _FrameRelayRIPUpdtTimer_Type()
)
frameRelayRIPUpdtTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayRIPUpdtTimer.setStatus("mandatory")


class _FrameRelayRIPAge_Type(Integer32):
    """Custom type frameRelayRIPAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 540),
    )


_FrameRelayRIPAge_Type.__name__ = "Integer32"
_FrameRelayRIPAge_Object = MibTableColumn
frameRelayRIPAge = _FrameRelayRIPAge_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 37),
    _FrameRelayRIPAge_Type()
)
frameRelayRIPAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayRIPAge.setStatus("mandatory")


class _FrameRelaySAPUpdtTimer_Type(Integer32):
    """Custom type frameRelaySAPUpdtTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 180),
    )


_FrameRelaySAPUpdtTimer_Type.__name__ = "Integer32"
_FrameRelaySAPUpdtTimer_Object = MibTableColumn
frameRelaySAPUpdtTimer = _FrameRelaySAPUpdtTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 38),
    _FrameRelaySAPUpdtTimer_Type()
)
frameRelaySAPUpdtTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelaySAPUpdtTimer.setStatus("mandatory")


class _FrameRelaySAPAge_Type(Integer32):
    """Custom type frameRelaySAPAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 720),
    )


_FrameRelaySAPAge_Type.__name__ = "Integer32"
_FrameRelaySAPAge_Object = MibTableColumn
frameRelaySAPAge = _FrameRelaySAPAge_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 39),
    _FrameRelaySAPAge_Type()
)
frameRelaySAPAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelaySAPAge.setStatus("mandatory")


class _FrameRelayRSM_Type(Integer32):
    """Custom type frameRelayRSM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_FrameRelayRSM_Type.__name__ = "Integer32"
_FrameRelayRSM_Object = MibTableColumn
frameRelayRSM = _FrameRelayRSM_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 40),
    _FrameRelayRSM_Type()
)
frameRelayRSM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayRSM.setStatus("mandatory")


class _FrameRelayARP_Type(Integer32):
    """Custom type frameRelayARP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("ethernetVersiontwo", 5),
          ("iEEEeightotwothree", 6),
          ("inverseArp", 2),
          ("none", 7),
          ("routedArp", 3),
          ("tokenRing", 4))
    )


_FrameRelayARP_Type.__name__ = "Integer32"
_FrameRelayARP_Object = MibTableColumn
frameRelayARP = _FrameRelayARP_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 41),
    _FrameRelayARP_Type()
)
frameRelayARP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayARP.setStatus("mandatory")


class _FrameRelayCTS_Type(Integer32):
    """Custom type frameRelayCTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_FrameRelayCTS_Type.__name__ = "Integer32"
_FrameRelayCTS_Object = MibTableColumn
frameRelayCTS = _FrameRelayCTS_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 42),
    _FrameRelayCTS_Type()
)
frameRelayCTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayCTS.setStatus("mandatory")


class _FrameRelayDCD_Type(Integer32):
    """Custom type frameRelayDCD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_FrameRelayDCD_Type.__name__ = "Integer32"
_FrameRelayDCD_Object = MibTableColumn
frameRelayDCD = _FrameRelayDCD_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 43),
    _FrameRelayDCD_Type()
)
frameRelayDCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayDCD.setStatus("mandatory")


class _FrameRelayDSR_Type(Integer32):
    """Custom type frameRelayDSR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_FrameRelayDSR_Type.__name__ = "Integer32"
_FrameRelayDSR_Object = MibTableColumn
frameRelayDSR = _FrameRelayDSR_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 44),
    _FrameRelayDSR_Type()
)
frameRelayDSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayDSR.setStatus("mandatory")


class _FrameRelayDTR_Type(Integer32):
    """Custom type frameRelayDTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_FrameRelayDTR_Type.__name__ = "Integer32"
_FrameRelayDTR_Object = MibTableColumn
frameRelayDTR = _FrameRelayDTR_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 45),
    _FrameRelayDTR_Type()
)
frameRelayDTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayDTR.setStatus("mandatory")


class _FrameRelayRTS_Type(Integer32):
    """Custom type frameRelayRTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_FrameRelayRTS_Type.__name__ = "Integer32"
_FrameRelayRTS_Object = MibTableColumn
frameRelayRTS = _FrameRelayRTS_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 46),
    _FrameRelayRTS_Type()
)
frameRelayRTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayRTS.setStatus("mandatory")


class _FrameRelayReturnClock_Type(Integer32):
    """Custom type frameRelayReturnClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("no", 2),
          ("yes", 1))
    )


_FrameRelayReturnClock_Type.__name__ = "Integer32"
_FrameRelayReturnClock_Object = MibTableColumn
frameRelayReturnClock = _FrameRelayReturnClock_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 1, 1, 47),
    _FrameRelayReturnClock_Type()
)
frameRelayReturnClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayReturnClock.setStatus("mandatory")
_FrameRelayStatsTable_Object = MibTable
frameRelayStatsTable = _FrameRelayStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 2)
)
if mibBuilder.loadTexts:
    frameRelayStatsTable.setStatus("mandatory")
_FrameRelayStatsEntry_Object = MibTableRow
frameRelayStatsEntry = _FrameRelayStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 2, 1)
)
frameRelayStatsEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "frameRelayStatsPortIndex"),
)
if mibBuilder.loadTexts:
    frameRelayStatsEntry.setStatus("mandatory")
_FrameRelayStatsPortIndex_Type = Integer32
_FrameRelayStatsPortIndex_Object = MibTableColumn
frameRelayStatsPortIndex = _FrameRelayStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 2, 1, 1),
    _FrameRelayStatsPortIndex_Type()
)
frameRelayStatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayStatsPortIndex.setStatus("mandatory")
_FrameRelayInOctets_Type = Counter32
_FrameRelayInOctets_Object = MibTableColumn
frameRelayInOctets = _FrameRelayInOctets_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 2, 1, 2),
    _FrameRelayInOctets_Type()
)
frameRelayInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayInOctets.setStatus("mandatory")
_FrameRelayOutOctets_Type = Counter32
_FrameRelayOutOctets_Object = MibTableColumn
frameRelayOutOctets = _FrameRelayOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 2, 1, 3),
    _FrameRelayOutOctets_Type()
)
frameRelayOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayOutOctets.setStatus("mandatory")
_FrameRelaySampleDuration_Type = Integer32
_FrameRelaySampleDuration_Object = MibTableColumn
frameRelaySampleDuration = _FrameRelaySampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 2, 1, 4),
    _FrameRelaySampleDuration_Type()
)
frameRelaySampleDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelaySampleDuration.setStatus("mandatory")
_FrameRelayOverruns_Type = Counter32
_FrameRelayOverruns_Object = MibTableColumn
frameRelayOverruns = _FrameRelayOverruns_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 2, 1, 5),
    _FrameRelayOverruns_Type()
)
frameRelayOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayOverruns.setStatus("mandatory")
_FrameRelayCRCErrors_Type = Counter32
_FrameRelayCRCErrors_Object = MibTableColumn
frameRelayCRCErrors = _FrameRelayCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 2, 1, 6),
    _FrameRelayCRCErrors_Type()
)
frameRelayCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayCRCErrors.setStatus("mandatory")
_FrameRelayRecvAborts_Type = Counter32
_FrameRelayRecvAborts_Object = MibTableColumn
frameRelayRecvAborts = _FrameRelayRecvAborts_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 2, 1, 7),
    _FrameRelayRecvAborts_Type()
)
frameRelayRecvAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayRecvAborts.setStatus("mandatory")
_FrameRelayTxDe_Type = Counter32
_FrameRelayTxDe_Object = MibTableColumn
frameRelayTxDe = _FrameRelayTxDe_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 2, 1, 8),
    _FrameRelayTxDe_Type()
)
frameRelayTxDe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayTxDe.setStatus("mandatory")
_FrameRelayRxDe_Type = Counter32
_FrameRelayRxDe_Object = MibTableColumn
frameRelayRxDe = _FrameRelayRxDe_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 2, 1, 9),
    _FrameRelayRxDe_Type()
)
frameRelayRxDe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayRxDe.setStatus("mandatory")
_FrameRelaySwitchedAttempts_Type = Counter32
_FrameRelaySwitchedAttempts_Object = MibTableColumn
frameRelaySwitchedAttempts = _FrameRelaySwitchedAttempts_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 2, 1, 10),
    _FrameRelaySwitchedAttempts_Type()
)
frameRelaySwitchedAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelaySwitchedAttempts.setStatus("mandatory")
_FrameRelaySwitchedAttemptsSuccessful_Type = Counter32
_FrameRelaySwitchedAttemptsSuccessful_Object = MibTableColumn
frameRelaySwitchedAttemptsSuccessful = _FrameRelaySwitchedAttemptsSuccessful_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 5, 2, 1, 11),
    _FrameRelaySwitchedAttemptsSuccessful_Type()
)
frameRelaySwitchedAttemptsSuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelaySwitchedAttemptsSuccessful.setStatus("mandatory")
_LineAsyncGroup_ObjectIdentity = ObjectIdentity
lineAsyncGroup = _LineAsyncGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6)
)
_AsyncConfigTable_Object = MibTable
asyncConfigTable = _AsyncConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 1)
)
if mibBuilder.loadTexts:
    asyncConfigTable.setStatus("mandatory")
_AsyncConfigEntry_Object = MibTableRow
asyncConfigEntry = _AsyncConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 1, 1)
)
asyncConfigEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "asyncConfigPortIndex"),
)
if mibBuilder.loadTexts:
    asyncConfigEntry.setStatus("mandatory")
_AsyncConfigPortIndex_Type = Integer32
_AsyncConfigPortIndex_Object = MibTableColumn
asyncConfigPortIndex = _AsyncConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 1, 1, 1),
    _AsyncConfigPortIndex_Type()
)
asyncConfigPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncConfigPortIndex.setStatus("mandatory")


class _AsyncConfigType_Type(Integer32):
    """Custom type asyncConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("hasc-type", 9),
          ("tasc-type", 10))
    )


_AsyncConfigType_Type.__name__ = "Integer32"
_AsyncConfigType_Object = MibTableColumn
asyncConfigType = _AsyncConfigType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 1, 1, 2),
    _AsyncConfigType_Type()
)
asyncConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncConfigType.setStatus("mandatory")


class _AsyncNAUName_Type(DisplayString):
    """Custom type asyncNAUName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AsyncNAUName_Type.__name__ = "DisplayString"
_AsyncNAUName_Object = MibTableColumn
asyncNAUName = _AsyncNAUName_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 1, 1, 3),
    _AsyncNAUName_Type()
)
asyncNAUName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncNAUName.setStatus("mandatory")


class _AsyncInitState_Type(Integer32):
    """Custom type asyncInitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in-service", 1),
          ("out-of-service", 2))
    )


_AsyncInitState_Type.__name__ = "Integer32"
_AsyncInitState_Object = MibTableColumn
asyncInitState = _AsyncInitState_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 1, 1, 4),
    _AsyncInitState_Type()
)
asyncInitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncInitState.setStatus("mandatory")


class _AsyncCarrier_Type(Integer32):
    """Custom type asyncCarrier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("constant", 1),
          ("switched", 2))
    )


_AsyncCarrier_Type.__name__ = "Integer32"
_AsyncCarrier_Object = MibTableColumn
asyncCarrier = _AsyncCarrier_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 1, 1, 5),
    _AsyncCarrier_Type()
)
asyncCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncCarrier.setStatus("mandatory")


class _AsyncSpeed_Type(Integer32):
    """Custom type asyncSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(75,
              150,
              300,
              600,
              1200,
              2400,
              4800,
              9600,
              19200)
        )
    )
    namedValues = NamedValues(
        *(("speed1200", 1200),
          ("speed150", 150),
          ("speed19200", 19200),
          ("speed2400", 2400),
          ("speed300", 300),
          ("speed4800", 4800),
          ("speed600", 600),
          ("speed75", 75),
          ("speed9600", 9600))
    )


_AsyncSpeed_Type.__name__ = "Integer32"
_AsyncSpeed_Object = MibTableColumn
asyncSpeed = _AsyncSpeed_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 1, 1, 6),
    _AsyncSpeed_Type()
)
asyncSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncSpeed.setStatus("mandatory")


class _AsyncPhysicalType_Type(Integer32):
    """Custom type asyncPhysicalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 2),
          ("dte", 1))
    )


_AsyncPhysicalType_Type.__name__ = "Integer32"
_AsyncPhysicalType_Object = MibTableColumn
asyncPhysicalType = _AsyncPhysicalType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 1, 1, 7),
    _AsyncPhysicalType_Type()
)
asyncPhysicalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncPhysicalType.setStatus("mandatory")


class _AsyncStopBits_Type(Integer32):
    """Custom type asyncStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sto1", 1),
          ("sto1-5", 2),
          ("sto2", 3))
    )


_AsyncStopBits_Type.__name__ = "Integer32"
_AsyncStopBits_Object = MibTableColumn
asyncStopBits = _AsyncStopBits_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 1, 1, 8),
    _AsyncStopBits_Type()
)
asyncStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncStopBits.setStatus("mandatory")


class _AsyncParity_Type(Integer32):
    """Custom type asyncParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even", 2),
          ("none", 3),
          ("odd", 1))
    )


_AsyncParity_Type.__name__ = "Integer32"
_AsyncParity_Object = MibTableColumn
asyncParity = _AsyncParity_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 1, 1, 9),
    _AsyncParity_Type()
)
asyncParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncParity.setStatus("mandatory")


class _AsyncDataBits_Type(Integer32):
    """Custom type asyncDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 8),
    )


_AsyncDataBits_Type.__name__ = "Integer32"
_AsyncDataBits_Object = MibTableColumn
asyncDataBits = _AsyncDataBits_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 1, 1, 10),
    _AsyncDataBits_Type()
)
asyncDataBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncDataBits.setStatus("mandatory")


class _AsyncIdleTimer_Type(Integer32):
    """Custom type asyncIdleTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AsyncIdleTimer_Type.__name__ = "Integer32"
_AsyncIdleTimer_Object = MibTableColumn
asyncIdleTimer = _AsyncIdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 1, 1, 11),
    _AsyncIdleTimer_Type()
)
asyncIdleTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncIdleTimer.setStatus("mandatory")


class _AsyncTxFrameGap_Type(Integer32):
    """Custom type asyncTxFrameGap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AsyncTxFrameGap_Type.__name__ = "Integer32"
_AsyncTxFrameGap_Object = MibTableColumn
asyncTxFrameGap = _AsyncTxFrameGap_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 1, 1, 12),
    _AsyncTxFrameGap_Type()
)
asyncTxFrameGap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncTxFrameGap.setStatus("mandatory")


class _AsyncRxForwardingCount_Type(Integer32):
    """Custom type asyncRxForwardingCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_AsyncRxForwardingCount_Type.__name__ = "Integer32"
_AsyncRxForwardingCount_Object = MibTableColumn
asyncRxForwardingCount = _AsyncRxForwardingCount_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 1, 1, 13),
    _AsyncRxForwardingCount_Type()
)
asyncRxForwardingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncRxForwardingCount.setStatus("mandatory")


class _AsyncEiaSignalForwarding_Type(Integer32):
    """Custom type asyncEiaSignalForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AsyncEiaSignalForwarding_Type.__name__ = "Integer32"
_AsyncEiaSignalForwarding_Object = MibTableColumn
asyncEiaSignalForwarding = _AsyncEiaSignalForwarding_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 1, 1, 14),
    _AsyncEiaSignalForwarding_Type()
)
asyncEiaSignalForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncEiaSignalForwarding.setStatus("mandatory")


class _AsyncAddressOffset_Type(Integer32):
    """Custom type asyncAddressOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AsyncAddressOffset_Type.__name__ = "Integer32"
_AsyncAddressOffset_Object = MibTableColumn
asyncAddressOffset = _AsyncAddressOffset_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 1, 1, 15),
    _AsyncAddressOffset_Type()
)
asyncAddressOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncAddressOffset.setStatus("mandatory")


class _AsyncRTC_Type(OctetString):
    """Custom type asyncRTC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AsyncRTC_Type.__name__ = "OctetString"
_AsyncRTC_Object = MibTableColumn
asyncRTC = _AsyncRTC_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 1, 1, 16),
    _AsyncRTC_Type()
)
asyncRTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncRTC.setStatus("mandatory")


class _AsyncCTS_Type(Integer32):
    """Custom type asyncCTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AsyncCTS_Type.__name__ = "Integer32"
_AsyncCTS_Object = MibTableColumn
asyncCTS = _AsyncCTS_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 1, 1, 17),
    _AsyncCTS_Type()
)
asyncCTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncCTS.setStatus("mandatory")


class _AsyncDCD_Type(Integer32):
    """Custom type asyncDCD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AsyncDCD_Type.__name__ = "Integer32"
_AsyncDCD_Object = MibTableColumn
asyncDCD = _AsyncDCD_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 1, 1, 18),
    _AsyncDCD_Type()
)
asyncDCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncDCD.setStatus("mandatory")


class _AsyncDSR_Type(Integer32):
    """Custom type asyncDSR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AsyncDSR_Type.__name__ = "Integer32"
_AsyncDSR_Object = MibTableColumn
asyncDSR = _AsyncDSR_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 1, 1, 19),
    _AsyncDSR_Type()
)
asyncDSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncDSR.setStatus("mandatory")


class _AsyncDTR_Type(Integer32):
    """Custom type asyncDTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AsyncDTR_Type.__name__ = "Integer32"
_AsyncDTR_Object = MibTableColumn
asyncDTR = _AsyncDTR_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 1, 1, 20),
    _AsyncDTR_Type()
)
asyncDTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncDTR.setStatus("mandatory")


class _AsyncRTS_Type(Integer32):
    """Custom type asyncRTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AsyncRTS_Type.__name__ = "Integer32"
_AsyncRTS_Object = MibTableColumn
asyncRTS = _AsyncRTS_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 1, 1, 21),
    _AsyncRTS_Type()
)
asyncRTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncRTS.setStatus("mandatory")


class _AsyncReturnClock_Type(Integer32):
    """Custom type asyncReturnClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("no", 2),
          ("yes", 1))
    )


_AsyncReturnClock_Type.__name__ = "Integer32"
_AsyncReturnClock_Object = MibTableColumn
asyncReturnClock = _AsyncReturnClock_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 1, 1, 22),
    _AsyncReturnClock_Type()
)
asyncReturnClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncReturnClock.setStatus("mandatory")


class _AsyncOrt_Type(Integer32):
    """Custom type asyncOrt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AsyncOrt_Type.__name__ = "Integer32"
_AsyncOrt_Object = MibTableColumn
asyncOrt = _AsyncOrt_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 1, 1, 23),
    _AsyncOrt_Type()
)
asyncOrt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncOrt.setStatus("mandatory")
_AsyncStatsTable_Object = MibTable
asyncStatsTable = _AsyncStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 2)
)
if mibBuilder.loadTexts:
    asyncStatsTable.setStatus("mandatory")
_AsyncStatsEntry_Object = MibTableRow
asyncStatsEntry = _AsyncStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 2, 1)
)
asyncStatsEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "asyncStatsPortIndex"),
)
if mibBuilder.loadTexts:
    asyncStatsEntry.setStatus("mandatory")
_AsyncStatsPortIndex_Type = Integer32
_AsyncStatsPortIndex_Object = MibTableColumn
asyncStatsPortIndex = _AsyncStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 2, 1, 1),
    _AsyncStatsPortIndex_Type()
)
asyncStatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncStatsPortIndex.setStatus("mandatory")


class _AsyncPortType_Type(Integer32):
    """Custom type asyncPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("hasc-type", 9),
          ("tasc-type", 10))
    )


_AsyncPortType_Type.__name__ = "Integer32"
_AsyncPortType_Object = MibTableColumn
asyncPortType = _AsyncPortType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 2, 1, 2),
    _AsyncPortType_Type()
)
asyncPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncPortType.setStatus("mandatory")
_AsyncInOctets_Type = Counter32
_AsyncInOctets_Object = MibTableColumn
asyncInOctets = _AsyncInOctets_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 2, 1, 3),
    _AsyncInOctets_Type()
)
asyncInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncInOctets.setStatus("mandatory")
_AsyncOutOctets_Type = Counter32
_AsyncOutOctets_Object = MibTableColumn
asyncOutOctets = _AsyncOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 2, 1, 4),
    _AsyncOutOctets_Type()
)
asyncOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncOutOctets.setStatus("mandatory")
_AsyncInMessages_Type = Counter32
_AsyncInMessages_Object = MibTableColumn
asyncInMessages = _AsyncInMessages_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 2, 1, 5),
    _AsyncInMessages_Type()
)
asyncInMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncInMessages.setStatus("mandatory")
_AsyncOutMessages_Type = Counter32
_AsyncOutMessages_Object = MibTableColumn
asyncOutMessages = _AsyncOutMessages_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 2, 1, 6),
    _AsyncOutMessages_Type()
)
asyncOutMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncOutMessages.setStatus("mandatory")
_AsyncInMsgDiscarded_Type = Counter32
_AsyncInMsgDiscarded_Object = MibTableColumn
asyncInMsgDiscarded = _AsyncInMsgDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 2, 1, 7),
    _AsyncInMsgDiscarded_Type()
)
asyncInMsgDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncInMsgDiscarded.setStatus("mandatory")
_AsyncOutMsgDiscarded_Type = Counter32
_AsyncOutMsgDiscarded_Object = MibTableColumn
asyncOutMsgDiscarded = _AsyncOutMsgDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 2, 1, 8),
    _AsyncOutMsgDiscarded_Type()
)
asyncOutMsgDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncOutMsgDiscarded.setStatus("mandatory")
_AsyncXmtFailures_Type = Counter32
_AsyncXmtFailures_Object = MibTableColumn
asyncXmtFailures = _AsyncXmtFailures_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 2, 1, 9),
    _AsyncXmtFailures_Type()
)
asyncXmtFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncXmtFailures.setStatus("mandatory")
_AsyncRcvMsgForwarded_Type = Counter32
_AsyncRcvMsgForwarded_Object = MibTableColumn
asyncRcvMsgForwarded = _AsyncRcvMsgForwarded_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 2, 1, 10),
    _AsyncRcvMsgForwarded_Type()
)
asyncRcvMsgForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncRcvMsgForwarded.setStatus("mandatory")
_AsyncRcvMsgErrors_Type = Counter32
_AsyncRcvMsgErrors_Object = MibTableColumn
asyncRcvMsgErrors = _AsyncRcvMsgErrors_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 2, 1, 11),
    _AsyncRcvMsgErrors_Type()
)
asyncRcvMsgErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncRcvMsgErrors.setStatus("mandatory")
_AsyncRcvCharsDiscarded_Type = Counter32
_AsyncRcvCharsDiscarded_Object = MibTableColumn
asyncRcvCharsDiscarded = _AsyncRcvCharsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 2, 1, 12),
    _AsyncRcvCharsDiscarded_Type()
)
asyncRcvCharsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncRcvCharsDiscarded.setStatus("mandatory")
_AsyncRcvParityErrors_Type = Counter32
_AsyncRcvParityErrors_Object = MibTableColumn
asyncRcvParityErrors = _AsyncRcvParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 2, 1, 13),
    _AsyncRcvParityErrors_Type()
)
asyncRcvParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncRcvParityErrors.setStatus("mandatory")
_AsyncRcvFramingErrors_Type = Counter32
_AsyncRcvFramingErrors_Object = MibTableColumn
asyncRcvFramingErrors = _AsyncRcvFramingErrors_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 2, 1, 14),
    _AsyncRcvFramingErrors_Type()
)
asyncRcvFramingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncRcvFramingErrors.setStatus("mandatory")
_AsyncRcvFifoOverruns_Type = Counter32
_AsyncRcvFifoOverruns_Object = MibTableColumn
asyncRcvFifoOverruns = _AsyncRcvFifoOverruns_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 2, 1, 15),
    _AsyncRcvFifoOverruns_Type()
)
asyncRcvFifoOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncRcvFifoOverruns.setStatus("mandatory")
_AsyncRcvCharsOverruns_Type = Counter32
_AsyncRcvCharsOverruns_Object = MibTableColumn
asyncRcvCharsOverruns = _AsyncRcvCharsOverruns_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 2, 1, 16),
    _AsyncRcvCharsOverruns_Type()
)
asyncRcvCharsOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncRcvCharsOverruns.setStatus("mandatory")
_AsyncRcvBreakConditions_Type = Counter32
_AsyncRcvBreakConditions_Object = MibTableColumn
asyncRcvBreakConditions = _AsyncRcvBreakConditions_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 6, 2, 1, 17),
    _AsyncRcvBreakConditions_Type()
)
asyncRcvBreakConditions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncRcvBreakConditions.setStatus("mandatory")
_LineBisyncRjeGroup_ObjectIdentity = ObjectIdentity
lineBisyncRjeGroup = _LineBisyncRjeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 7)
)
_BisyncrjeConfigTable_Object = MibTable
bisyncrjeConfigTable = _BisyncrjeConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 7, 1)
)
if mibBuilder.loadTexts:
    bisyncrjeConfigTable.setStatus("mandatory")
_BisyncrjeConfigEntry_Object = MibTableRow
bisyncrjeConfigEntry = _BisyncrjeConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 7, 1, 1)
)
bisyncrjeConfigEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "bisyncrjeConfigPortIndex"),
)
if mibBuilder.loadTexts:
    bisyncrjeConfigEntry.setStatus("mandatory")
_BisyncrjeConfigPortIndex_Type = Integer32
_BisyncrjeConfigPortIndex_Object = MibTableColumn
bisyncrjeConfigPortIndex = _BisyncrjeConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 7, 1, 1, 1),
    _BisyncrjeConfigPortIndex_Type()
)
bisyncrjeConfigPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjeConfigPortIndex.setStatus("mandatory")


class _BisyncrjeConfigType_Type(Integer32):
    """Custom type bisyncrjeConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("primaryRJE-type", 14),
          ("secondaryRJE-type", 13))
    )


_BisyncrjeConfigType_Type.__name__ = "Integer32"
_BisyncrjeConfigType_Object = MibTableColumn
bisyncrjeConfigType = _BisyncrjeConfigType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 7, 1, 1, 2),
    _BisyncrjeConfigType_Type()
)
bisyncrjeConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjeConfigType.setStatus("mandatory")


class _BisyncrjeNAUName_Type(DisplayString):
    """Custom type bisyncrjeNAUName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_BisyncrjeNAUName_Type.__name__ = "DisplayString"
_BisyncrjeNAUName_Object = MibTableColumn
bisyncrjeNAUName = _BisyncrjeNAUName_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 7, 1, 1, 3),
    _BisyncrjeNAUName_Type()
)
bisyncrjeNAUName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjeNAUName.setStatus("mandatory")


class _BisyncrjeInitState_Type(Integer32):
    """Custom type bisyncrjeInitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in-service", 1),
          ("out-of-service", 2))
    )


_BisyncrjeInitState_Type.__name__ = "Integer32"
_BisyncrjeInitState_Object = MibTableColumn
bisyncrjeInitState = _BisyncrjeInitState_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 7, 1, 1, 4),
    _BisyncrjeInitState_Type()
)
bisyncrjeInitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjeInitState.setStatus("mandatory")


class _BisyncrjeCarrier_Type(Integer32):
    """Custom type bisyncrjeCarrier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("constant", 1),
          ("switched", 2))
    )


_BisyncrjeCarrier_Type.__name__ = "Integer32"
_BisyncrjeCarrier_Object = MibTableColumn
bisyncrjeCarrier = _BisyncrjeCarrier_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 7, 1, 1, 5),
    _BisyncrjeCarrier_Type()
)
bisyncrjeCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjeCarrier.setStatus("mandatory")


class _BisyncrjeClocking_Type(Integer32):
    """Custom type bisyncrjeClocking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("internal", 2))
    )


_BisyncrjeClocking_Type.__name__ = "Integer32"
_BisyncrjeClocking_Object = MibTableColumn
bisyncrjeClocking = _BisyncrjeClocking_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 7, 1, 1, 6),
    _BisyncrjeClocking_Type()
)
bisyncrjeClocking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjeClocking.setStatus("mandatory")


class _BisyncrjeSpeed_Type(Integer32):
    """Custom type bisyncrjeSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(12,
              20,
              24,
              36,
              48,
              72,
              96,
              144,
              192,
              288,
              480,
              560,
              640,
              1280)
        )
    )
    namedValues = NamedValues(
        *(("speed1200", 12),
          ("speed128000", 1280),
          ("speed14400", 144),
          ("speed19200", 192),
          ("speed2000", 20),
          ("speed2400", 24),
          ("speed28800", 288),
          ("speed3600", 36),
          ("speed4800", 48),
          ("speed48000", 480),
          ("speed56000", 560),
          ("speed64000", 640),
          ("speed7200", 72),
          ("speed9600", 96))
    )


_BisyncrjeSpeed_Type.__name__ = "Integer32"
_BisyncrjeSpeed_Object = MibTableColumn
bisyncrjeSpeed = _BisyncrjeSpeed_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 7, 1, 1, 7),
    _BisyncrjeSpeed_Type()
)
bisyncrjeSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjeSpeed.setStatus("mandatory")


class _BisyncrjeReplyTimer_Type(Integer32):
    """Custom type bisyncrjeReplyTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_BisyncrjeReplyTimer_Type.__name__ = "Integer32"
_BisyncrjeReplyTimer_Object = MibTableColumn
bisyncrjeReplyTimer = _BisyncrjeReplyTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 7, 1, 1, 8),
    _BisyncrjeReplyTimer_Type()
)
bisyncrjeReplyTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjeReplyTimer.setStatus("mandatory")


class _BisyncrjeRetries_Type(Integer32):
    """Custom type bisyncrjeRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_BisyncrjeRetries_Type.__name__ = "Integer32"
_BisyncrjeRetries_Object = MibTableColumn
bisyncrjeRetries = _BisyncrjeRetries_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 7, 1, 1, 9),
    _BisyncrjeRetries_Type()
)
bisyncrjeRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjeRetries.setStatus("mandatory")


class _BisyncrjeCodeSet_Type(Integer32):
    """Custom type bisyncrjeCodeSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("ebcdic", 2))
    )


_BisyncrjeCodeSet_Type.__name__ = "Integer32"
_BisyncrjeCodeSet_Object = MibTableColumn
bisyncrjeCodeSet = _BisyncrjeCodeSet_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 7, 1, 1, 10),
    _BisyncrjeCodeSet_Type()
)
bisyncrjeCodeSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjeCodeSet.setStatus("mandatory")


class _BisyncrjeCTS_Type(Integer32):
    """Custom type bisyncrjeCTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_BisyncrjeCTS_Type.__name__ = "Integer32"
_BisyncrjeCTS_Object = MibTableColumn
bisyncrjeCTS = _BisyncrjeCTS_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 7, 1, 1, 11),
    _BisyncrjeCTS_Type()
)
bisyncrjeCTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjeCTS.setStatus("mandatory")


class _BisyncrjeDCD_Type(Integer32):
    """Custom type bisyncrjeDCD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_BisyncrjeDCD_Type.__name__ = "Integer32"
_BisyncrjeDCD_Object = MibTableColumn
bisyncrjeDCD = _BisyncrjeDCD_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 7, 1, 1, 12),
    _BisyncrjeDCD_Type()
)
bisyncrjeDCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjeDCD.setStatus("mandatory")


class _BisyncrjeDSR_Type(Integer32):
    """Custom type bisyncrjeDSR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_BisyncrjeDSR_Type.__name__ = "Integer32"
_BisyncrjeDSR_Object = MibTableColumn
bisyncrjeDSR = _BisyncrjeDSR_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 7, 1, 1, 13),
    _BisyncrjeDSR_Type()
)
bisyncrjeDSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjeDSR.setStatus("mandatory")


class _BisyncrjeDTR_Type(Integer32):
    """Custom type bisyncrjeDTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_BisyncrjeDTR_Type.__name__ = "Integer32"
_BisyncrjeDTR_Object = MibTableColumn
bisyncrjeDTR = _BisyncrjeDTR_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 7, 1, 1, 14),
    _BisyncrjeDTR_Type()
)
bisyncrjeDTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjeDTR.setStatus("mandatory")


class _BisyncrjeRTS_Type(Integer32):
    """Custom type bisyncrjeRTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_BisyncrjeRTS_Type.__name__ = "Integer32"
_BisyncrjeRTS_Object = MibTableColumn
bisyncrjeRTS = _BisyncrjeRTS_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 7, 1, 1, 15),
    _BisyncrjeRTS_Type()
)
bisyncrjeRTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjeRTS.setStatus("mandatory")


class _BisyncrjeReturnClock_Type(Integer32):
    """Custom type bisyncrjeReturnClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("no", 2),
          ("yes", 1))
    )


_BisyncrjeReturnClock_Type.__name__ = "Integer32"
_BisyncrjeReturnClock_Object = MibTableColumn
bisyncrjeReturnClock = _BisyncrjeReturnClock_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 7, 1, 1, 16),
    _BisyncrjeReturnClock_Type()
)
bisyncrjeReturnClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjeReturnClock.setStatus("mandatory")
_BisyncrjeStatsTable_Object = MibTable
bisyncrjeStatsTable = _BisyncrjeStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 7, 2)
)
if mibBuilder.loadTexts:
    bisyncrjeStatsTable.setStatus("mandatory")
_BisyncrjeStatsEntry_Object = MibTableRow
bisyncrjeStatsEntry = _BisyncrjeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 7, 2, 1)
)
bisyncrjeStatsEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "bisyncrjeStatsPortIndex"),
)
if mibBuilder.loadTexts:
    bisyncrjeStatsEntry.setStatus("mandatory")
_BisyncrjeStatsPortIndex_Type = Integer32
_BisyncrjeStatsPortIndex_Object = MibTableColumn
bisyncrjeStatsPortIndex = _BisyncrjeStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 7, 2, 1, 1),
    _BisyncrjeStatsPortIndex_Type()
)
bisyncrjeStatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjeStatsPortIndex.setStatus("mandatory")


class _BisyncrjePortType_Type(Integer32):
    """Custom type bisyncrjePortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("prje-PrimaryRJE", 14),
          ("srje-SecondaryRJE", 13))
    )


_BisyncrjePortType_Type.__name__ = "Integer32"
_BisyncrjePortType_Object = MibTableColumn
bisyncrjePortType = _BisyncrjePortType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 7, 2, 1, 2),
    _BisyncrjePortType_Type()
)
bisyncrjePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjePortType.setStatus("mandatory")
_BisyncrjeInChrs_Type = Counter32
_BisyncrjeInChrs_Object = MibTableColumn
bisyncrjeInChrs = _BisyncrjeInChrs_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 7, 2, 1, 3),
    _BisyncrjeInChrs_Type()
)
bisyncrjeInChrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjeInChrs.setStatus("mandatory")
_BisyncrjeOutChrs_Type = Counter32
_BisyncrjeOutChrs_Object = MibTableColumn
bisyncrjeOutChrs = _BisyncrjeOutChrs_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 7, 2, 1, 4),
    _BisyncrjeOutChrs_Type()
)
bisyncrjeOutChrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjeOutChrs.setStatus("mandatory")
_BisyncrjeInTrns_Type = Counter32
_BisyncrjeInTrns_Object = MibTableColumn
bisyncrjeInTrns = _BisyncrjeInTrns_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 7, 2, 1, 5),
    _BisyncrjeInTrns_Type()
)
bisyncrjeInTrns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjeInTrns.setStatus("mandatory")
_BisyncrjeOutTrns_Type = Counter32
_BisyncrjeOutTrns_Object = MibTableColumn
bisyncrjeOutTrns = _BisyncrjeOutTrns_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 7, 2, 1, 6),
    _BisyncrjeOutTrns_Type()
)
bisyncrjeOutTrns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjeOutTrns.setStatus("mandatory")
_BisyncrjeInRetr_Type = Counter32
_BisyncrjeInRetr_Object = MibTableColumn
bisyncrjeInRetr = _BisyncrjeInRetr_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 7, 2, 1, 7),
    _BisyncrjeInRetr_Type()
)
bisyncrjeInRetr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjeInRetr.setStatus("mandatory")
_BisyncrjeOutRetr_Type = Counter32
_BisyncrjeOutRetr_Object = MibTableColumn
bisyncrjeOutRetr = _BisyncrjeOutRetr_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 7, 2, 1, 8),
    _BisyncrjeOutRetr_Type()
)
bisyncrjeOutRetr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjeOutRetr.setStatus("mandatory")
_BisyncrjeInEnq_Type = Counter32
_BisyncrjeInEnq_Object = MibTableColumn
bisyncrjeInEnq = _BisyncrjeInEnq_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 7, 2, 1, 9),
    _BisyncrjeInEnq_Type()
)
bisyncrjeInEnq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjeInEnq.setStatus("mandatory")
_BisyncrjeOutEnq_Type = Counter32
_BisyncrjeOutEnq_Object = MibTableColumn
bisyncrjeOutEnq = _BisyncrjeOutEnq_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 7, 2, 1, 10),
    _BisyncrjeOutEnq_Type()
)
bisyncrjeOutEnq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjeOutEnq.setStatus("mandatory")
_BisyncrjeInEtb_Type = Counter32
_BisyncrjeInEtb_Object = MibTableColumn
bisyncrjeInEtb = _BisyncrjeInEtb_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 7, 2, 1, 11),
    _BisyncrjeInEtb_Type()
)
bisyncrjeInEtb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjeInEtb.setStatus("mandatory")
_BisyncrjeOutEtb_Type = Counter32
_BisyncrjeOutEtb_Object = MibTableColumn
bisyncrjeOutEtb = _BisyncrjeOutEtb_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 7, 2, 1, 12),
    _BisyncrjeOutEtb_Type()
)
bisyncrjeOutEtb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjeOutEtb.setStatus("mandatory")
_BisyncrjeInEtx_Type = Counter32
_BisyncrjeInEtx_Object = MibTableColumn
bisyncrjeInEtx = _BisyncrjeInEtx_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 7, 2, 1, 13),
    _BisyncrjeInEtx_Type()
)
bisyncrjeInEtx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjeInEtx.setStatus("mandatory")
_BisyncrjeOutEtx_Type = Counter32
_BisyncrjeOutEtx_Object = MibTableColumn
bisyncrjeOutEtx = _BisyncrjeOutEtx_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 7, 2, 1, 14),
    _BisyncrjeOutEtx_Type()
)
bisyncrjeOutEtx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjeOutEtx.setStatus("mandatory")
_BisyncrjeWack_Type = Counter32
_BisyncrjeWack_Object = MibTableColumn
bisyncrjeWack = _BisyncrjeWack_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 7, 2, 1, 15),
    _BisyncrjeWack_Type()
)
bisyncrjeWack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjeWack.setStatus("mandatory")
_BisyncrjeRvi_Type = Counter32
_BisyncrjeRvi_Object = MibTableColumn
bisyncrjeRvi = _BisyncrjeRvi_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 7, 2, 1, 16),
    _BisyncrjeRvi_Type()
)
bisyncrjeRvi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjeRvi.setStatus("mandatory")
_LineDialBackupGroup_ObjectIdentity = ObjectIdentity
lineDialBackupGroup = _LineDialBackupGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 8)
)
_DialbackupConfigTable_Object = MibTable
dialbackupConfigTable = _DialbackupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 8, 1)
)
if mibBuilder.loadTexts:
    dialbackupConfigTable.setStatus("mandatory")
_DialbackupConfigEntry_Object = MibTableRow
dialbackupConfigEntry = _DialbackupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 8, 1, 1)
)
dialbackupConfigEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "dialbackupConfigPortIndex"),
)
if mibBuilder.loadTexts:
    dialbackupConfigEntry.setStatus("mandatory")
_DialbackupConfigPortIndex_Type = Integer32
_DialbackupConfigPortIndex_Object = MibTableColumn
dialbackupConfigPortIndex = _DialbackupConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 8, 1, 1, 1),
    _DialbackupConfigPortIndex_Type()
)
dialbackupConfigPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialbackupConfigPortIndex.setStatus("mandatory")


class _DialbackupPortType_Type(Integer32):
    """Custom type dialbackupPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            20
        )
    )
    namedValues = NamedValues(
        ("frame-relay-dialbackup-type", 20)
    )


_DialbackupPortType_Type.__name__ = "Integer32"
_DialbackupPortType_Object = MibTableColumn
dialbackupPortType = _DialbackupPortType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 8, 1, 1, 2),
    _DialbackupPortType_Type()
)
dialbackupPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialbackupPortType.setStatus("mandatory")


class _DialbackupConnectType_Type(Integer32):
    """Custom type dialbackupConnectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hayes", 1),
          ("nullmodem", 3),
          ("vtwentyfivebis", 2))
    )


_DialbackupConnectType_Type.__name__ = "Integer32"
_DialbackupConnectType_Object = MibTableColumn
dialbackupConnectType = _DialbackupConnectType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 8, 1, 1, 3),
    _DialbackupConnectType_Type()
)
dialbackupConnectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialbackupConnectType.setStatus("mandatory")
_DialbackupFirstDedicatedPort_Type = Integer32
_DialbackupFirstDedicatedPort_Object = MibTableColumn
dialbackupFirstDedicatedPort = _DialbackupFirstDedicatedPort_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 8, 1, 1, 4),
    _DialbackupFirstDedicatedPort_Type()
)
dialbackupFirstDedicatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialbackupFirstDedicatedPort.setStatus("mandatory")
_DialbackupassociatedDLCIDedicated_Type = Integer32
_DialbackupassociatedDLCIDedicated_Object = MibTableColumn
dialbackupassociatedDLCIDedicated = _DialbackupassociatedDLCIDedicated_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 8, 1, 1, 5),
    _DialbackupassociatedDLCIDedicated_Type()
)
dialbackupassociatedDLCIDedicated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialbackupassociatedDLCIDedicated.setStatus("mandatory")
_DialbackupSecondDedicatedPort_Type = Integer32
_DialbackupSecondDedicatedPort_Object = MibTableColumn
dialbackupSecondDedicatedPort = _DialbackupSecondDedicatedPort_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 8, 1, 1, 6),
    _DialbackupSecondDedicatedPort_Type()
)
dialbackupSecondDedicatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialbackupSecondDedicatedPort.setStatus("mandatory")
_DialbackupassociatedDLCISecond_Type = Integer32
_DialbackupassociatedDLCISecond_Object = MibTableColumn
dialbackupassociatedDLCISecond = _DialbackupassociatedDLCISecond_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 8, 1, 1, 7),
    _DialbackupassociatedDLCISecond_Type()
)
dialbackupassociatedDLCISecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialbackupassociatedDLCISecond.setStatus("mandatory")
_DialbackupDedicatedPort_Type = Integer32
_DialbackupDedicatedPort_Object = MibTableColumn
dialbackupDedicatedPort = _DialbackupDedicatedPort_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 8, 1, 1, 8),
    _DialbackupDedicatedPort_Type()
)
dialbackupDedicatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialbackupDedicatedPort.setStatus("mandatory")
_DialbackupDedicatedLMIPort_Type = Integer32
_DialbackupDedicatedLMIPort_Object = MibTableColumn
dialbackupDedicatedLMIPort = _DialbackupDedicatedLMIPort_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 8, 1, 1, 9),
    _DialbackupDedicatedLMIPort_Type()
)
dialbackupDedicatedLMIPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialbackupDedicatedLMIPort.setStatus("mandatory")


class _DialbackupDialInactivityTimer_Type(Integer32):
    """Custom type dialbackupDialInactivityTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_DialbackupDialInactivityTimer_Type.__name__ = "Integer32"
_DialbackupDialInactivityTimer_Object = MibTableColumn
dialbackupDialInactivityTimer = _DialbackupDialInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 8, 1, 1, 10),
    _DialbackupDialInactivityTimer_Type()
)
dialbackupDialInactivityTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialbackupDialInactivityTimer.setStatus("mandatory")


class _DialbackupDialSuspendTimer_Type(Integer32):
    """Custom type dialbackupDialSuspendTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_DialbackupDialSuspendTimer_Type.__name__ = "Integer32"
_DialbackupDialSuspendTimer_Object = MibTableColumn
dialbackupDialSuspendTimer = _DialbackupDialSuspendTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 8, 1, 1, 11),
    _DialbackupDialSuspendTimer_Type()
)
dialbackupDialSuspendTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialbackupDialSuspendTimer.setStatus("mandatory")


class _DialbackupModemInitString_Type(DisplayString):
    """Custom type dialbackupModemInitString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_DialbackupModemInitString_Type.__name__ = "DisplayString"
_DialbackupModemInitString_Object = MibTableColumn
dialbackupModemInitString = _DialbackupModemInitString_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 8, 1, 1, 12),
    _DialbackupModemInitString_Type()
)
dialbackupModemInitString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialbackupModemInitString.setStatus("mandatory")


class _DialbackupModemDialString_Type(DisplayString):
    """Custom type dialbackupModemDialString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_DialbackupModemDialString_Type.__name__ = "DisplayString"
_DialbackupModemDialString_Object = MibTableColumn
dialbackupModemDialString = _DialbackupModemDialString_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 8, 1, 1, 13),
    _DialbackupModemDialString_Type()
)
dialbackupModemDialString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialbackupModemDialString.setStatus("mandatory")


class _DialbackupModemHangString_Type(DisplayString):
    """Custom type dialbackupModemHangString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_DialbackupModemHangString_Type.__name__ = "DisplayString"
_DialbackupModemHangString_Object = MibTableColumn
dialbackupModemHangString = _DialbackupModemHangString_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 8, 1, 1, 14),
    _DialbackupModemHangString_Type()
)
dialbackupModemHangString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialbackupModemHangString.setStatus("mandatory")


class _DialbackupDialDelayTimer_Type(Integer32):
    """Custom type dialbackupDialDelayTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_DialbackupDialDelayTimer_Type.__name__ = "Integer32"
_DialbackupDialDelayTimer_Object = MibTableColumn
dialbackupDialDelayTimer = _DialbackupDialDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 8, 1, 1, 15),
    _DialbackupDialDelayTimer_Type()
)
dialbackupDialDelayTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialbackupDialDelayTimer.setStatus("mandatory")


class _DialbackupTreatLLCControlCharacters_Type(Integer32):
    """Custom type dialbackupTreatLLCControlCharacters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_DialbackupTreatLLCControlCharacters_Type.__name__ = "Integer32"
_DialbackupTreatLLCControlCharacters_Object = MibTableColumn
dialbackupTreatLLCControlCharacters = _DialbackupTreatLLCControlCharacters_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 8, 1, 1, 16),
    _DialbackupTreatLLCControlCharacters_Type()
)
dialbackupTreatLLCControlCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialbackupTreatLLCControlCharacters.setStatus("mandatory")
_DialbackupStatsTable_Object = MibTable
dialbackupStatsTable = _DialbackupStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 8, 2)
)
if mibBuilder.loadTexts:
    dialbackupStatsTable.setStatus("mandatory")
_DialbackupStatsEntry_Object = MibTableRow
dialbackupStatsEntry = _DialbackupStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 8, 2, 1)
)
dialbackupStatsEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "dialbackupStatsPortIndex"),
)
if mibBuilder.loadTexts:
    dialbackupStatsEntry.setStatus("mandatory")
_DialbackupStatsPortIndex_Type = Integer32
_DialbackupStatsPortIndex_Object = MibTableColumn
dialbackupStatsPortIndex = _DialbackupStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 8, 2, 1, 1),
    _DialbackupStatsPortIndex_Type()
)
dialbackupStatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialbackupStatsPortIndex.setStatus("mandatory")
_DialbackupSuccatmpt_Type = Counter32
_DialbackupSuccatmpt_Object = MibTableColumn
dialbackupSuccatmpt = _DialbackupSuccatmpt_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 8, 2, 1, 2),
    _DialbackupSuccatmpt_Type()
)
dialbackupSuccatmpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialbackupSuccatmpt.setStatus("mandatory")
_Dialbackupunsuccatmpt_Type = Counter32
_Dialbackupunsuccatmpt_Object = MibTableColumn
dialbackupunsuccatmpt = _Dialbackupunsuccatmpt_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 8, 2, 1, 3),
    _Dialbackupunsuccatmpt_Type()
)
dialbackupunsuccatmpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialbackupunsuccatmpt.setStatus("mandatory")
_Dialbackupinact_Type = Counter32
_Dialbackupinact_Object = MibTableColumn
dialbackupinact = _Dialbackupinact_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 8, 2, 1, 4),
    _Dialbackupinact_Type()
)
dialbackupinact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialbackupinact.setStatus("mandatory")
_LineX25Group_ObjectIdentity = ObjectIdentity
lineX25Group = _LineX25Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9)
)
_X25ConfigTable_Object = MibTable
x25ConfigTable = _X25ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 1)
)
if mibBuilder.loadTexts:
    x25ConfigTable.setStatus("mandatory")
_X25ConfigEntry_Object = MibTableRow
x25ConfigEntry = _X25ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 1, 1)
)
x25ConfigEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "x25ConfigPortIndex"),
)
if mibBuilder.loadTexts:
    x25ConfigEntry.setStatus("mandatory")
_X25ConfigPortIndex_Type = Integer32
_X25ConfigPortIndex_Object = MibTableColumn
x25ConfigPortIndex = _X25ConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 1, 1, 1),
    _X25ConfigPortIndex_Type()
)
x25ConfigPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ConfigPortIndex.setStatus("mandatory")


class _X25ConfigType_Type(Integer32):
    """Custom type x25ConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("xDCE-XLogicalDCE", 8),
          ("xDTE-XLogicalDTE", 7))
    )


_X25ConfigType_Type.__name__ = "Integer32"
_X25ConfigType_Object = MibTableColumn
x25ConfigType = _X25ConfigType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 1, 1, 2),
    _X25ConfigType_Type()
)
x25ConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ConfigType.setStatus("mandatory")


class _X25NAUName_Type(DisplayString):
    """Custom type x25NAUName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_X25NAUName_Type.__name__ = "DisplayString"
_X25NAUName_Object = MibTableColumn
x25NAUName = _X25NAUName_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 1, 1, 3),
    _X25NAUName_Type()
)
x25NAUName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25NAUName.setStatus("mandatory")


class _X25InitState_Type(Integer32):
    """Custom type x25InitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in-service", 1),
          ("out-of-service", 2))
    )


_X25InitState_Type.__name__ = "Integer32"
_X25InitState_Object = MibTableColumn
x25InitState = _X25InitState_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 1, 1, 4),
    _X25InitState_Type()
)
x25InitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25InitState.setStatus("mandatory")


class _X25Clocking_Type(Integer32):
    """Custom type x25Clocking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("internal", 2),
          ("x21-external", 3),
          ("x21-internal", 4))
    )


_X25Clocking_Type.__name__ = "Integer32"
_X25Clocking_Object = MibTableColumn
x25Clocking = _X25Clocking_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 1, 1, 5),
    _X25Clocking_Type()
)
x25Clocking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25Clocking.setStatus("mandatory")
_X25DTEAddress_Type = OctetString
_X25DTEAddress_Object = MibTableColumn
x25DTEAddress = _X25DTEAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 1, 1, 6),
    _X25DTEAddress_Type()
)
x25DTEAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DTEAddress.setStatus("mandatory")


class _X25LinkWindowSize_Type(Integer32):
    """Custom type x25LinkWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_X25LinkWindowSize_Type.__name__ = "Integer32"
_X25LinkWindowSize_Object = MibTableColumn
x25LinkWindowSize = _X25LinkWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 1, 1, 7),
    _X25LinkWindowSize_Type()
)
x25LinkWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LinkWindowSize.setStatus("mandatory")


class _X25T1Timer_Type(Integer32):
    """Custom type x25T1Timer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1980),
    )


_X25T1Timer_Type.__name__ = "Integer32"
_X25T1Timer_Object = MibTableColumn
x25T1Timer = _X25T1Timer_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 1, 1, 8),
    _X25T1Timer_Type()
)
x25T1Timer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25T1Timer.setStatus("mandatory")


class _X25MaxRetries_Type(Integer32):
    """Custom type x25MaxRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_X25MaxRetries_Type.__name__ = "Integer32"
_X25MaxRetries_Object = MibTableColumn
x25MaxRetries = _X25MaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 1, 1, 9),
    _X25MaxRetries_Type()
)
x25MaxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25MaxRetries.setStatus("mandatory")


class _X25PortSpeed_Type(Integer32):
    """Custom type x25PortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(20,
              24,
              36,
              48,
              72,
              96,
              144,
              192,
              288,
              480,
              560,
              640,
              1280,
              2560)
        )
    )
    namedValues = NamedValues(
        *(("speed128000", 1280),
          ("speed14400", 144),
          ("speed19200", 192),
          ("speed2000", 20),
          ("speed2400", 24),
          ("speed256000", 2560),
          ("speed28800", 288),
          ("speed3600", 36),
          ("speed4800", 48),
          ("speed48000", 480),
          ("speed56000", 560),
          ("speed64000", 640),
          ("speed7200", 72),
          ("speed9600", 96))
    )


_X25PortSpeed_Type.__name__ = "Integer32"
_X25PortSpeed_Object = MibTableColumn
x25PortSpeed = _X25PortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 1, 1, 10),
    _X25PortSpeed_Type()
)
x25PortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25PortSpeed.setStatus("mandatory")


class _X25ReceiveWindowSize_Type(Integer32):
    """Custom type x25ReceiveWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_X25ReceiveWindowSize_Type.__name__ = "Integer32"
_X25ReceiveWindowSize_Object = MibTableColumn
x25ReceiveWindowSize = _X25ReceiveWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 1, 1, 11),
    _X25ReceiveWindowSize_Type()
)
x25ReceiveWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ReceiveWindowSize.setStatus("mandatory")


class _X25TransmitWindowSize_Type(Integer32):
    """Custom type x25TransmitWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_X25TransmitWindowSize_Type.__name__ = "Integer32"
_X25TransmitWindowSize_Object = MibTableColumn
x25TransmitWindowSize = _X25TransmitWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 1, 1, 12),
    _X25TransmitWindowSize_Type()
)
x25TransmitWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25TransmitWindowSize.setStatus("mandatory")


class _X25ReceivePacketSize_Type(Integer32):
    """Custom type x25ReceivePacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              32,
              128,
              256,
              512,
              1024)
        )
    )
    namedValues = NamedValues(
        *(("fivetwelve", 512),
          ("onethousand", 1024),
          ("onetwentyeight", 128),
          ("sixteen", 16),
          ("thirtytwo", 32),
          ("twofiftsix", 256))
    )


_X25ReceivePacketSize_Type.__name__ = "Integer32"
_X25ReceivePacketSize_Object = MibTableColumn
x25ReceivePacketSize = _X25ReceivePacketSize_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 1, 1, 13),
    _X25ReceivePacketSize_Type()
)
x25ReceivePacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ReceivePacketSize.setStatus("mandatory")


class _X25TransmitPacketSize_Type(Integer32):
    """Custom type x25TransmitPacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              32,
              128,
              256,
              512,
              1024)
        )
    )
    namedValues = NamedValues(
        *(("fivetwelve", 512),
          ("onethousand", 1024),
          ("onetwentyeight", 128),
          ("sixteen", 16),
          ("thirtytwo", 32),
          ("twofiftsix", 256))
    )


_X25TransmitPacketSize_Type.__name__ = "Integer32"
_X25TransmitPacketSize_Object = MibTableColumn
x25TransmitPacketSize = _X25TransmitPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 1, 1, 14),
    _X25TransmitPacketSize_Type()
)
x25TransmitPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25TransmitPacketSize.setStatus("mandatory")


class _X25LowTwoWayChannel_Type(Integer32):
    """Custom type x25LowTwoWayChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_X25LowTwoWayChannel_Type.__name__ = "Integer32"
_X25LowTwoWayChannel_Object = MibTableColumn
x25LowTwoWayChannel = _X25LowTwoWayChannel_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 1, 1, 15),
    _X25LowTwoWayChannel_Type()
)
x25LowTwoWayChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25LowTwoWayChannel.setStatus("mandatory")


class _X25HighTwoWayChannel_Type(Integer32):
    """Custom type x25HighTwoWayChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_X25HighTwoWayChannel_Type.__name__ = "Integer32"
_X25HighTwoWayChannel_Object = MibTableColumn
x25HighTwoWayChannel = _X25HighTwoWayChannel_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 1, 1, 16),
    _X25HighTwoWayChannel_Type()
)
x25HighTwoWayChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25HighTwoWayChannel.setStatus("mandatory")


class _X25UseCallingAddress_Type(Integer32):
    """Custom type x25UseCallingAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_X25UseCallingAddress_Type.__name__ = "Integer32"
_X25UseCallingAddress_Object = MibTableColumn
x25UseCallingAddress = _X25UseCallingAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 1, 1, 17),
    _X25UseCallingAddress_Type()
)
x25UseCallingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25UseCallingAddress.setStatus("mandatory")


class _X25ForwardingUnit_Type(Integer32):
    """Custom type x25ForwardingUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("eom", 8),
          ("five", 5),
          ("four", 4),
          ("one", 1),
          ("seven", 7),
          ("six", 6),
          ("three", 3),
          ("two", 2))
    )


_X25ForwardingUnit_Type.__name__ = "Integer32"
_X25ForwardingUnit_Object = MibTableColumn
x25ForwardingUnit = _X25ForwardingUnit_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 1, 1, 18),
    _X25ForwardingUnit_Type()
)
x25ForwardingUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ForwardingUnit.setStatus("mandatory")


class _X25DevicePacketSize_Type(Integer32):
    """Custom type x25DevicePacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              32,
              128,
              256,
              512,
              1024)
        )
    )
    namedValues = NamedValues(
        *(("fivetwelve", 512),
          ("none", 1),
          ("onethousand", 1024),
          ("onetwentyeight", 128),
          ("thirtytwo", 32),
          ("twofiftsix", 256))
    )


_X25DevicePacketSize_Type.__name__ = "Integer32"
_X25DevicePacketSize_Object = MibTableColumn
x25DevicePacketSize = _X25DevicePacketSize_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 1, 1, 19),
    _X25DevicePacketSize_Type()
)
x25DevicePacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DevicePacketSize.setStatus("mandatory")


class _X25DeviceWindowSize_Type(Integer32):
    """Custom type x25DeviceWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("five", 5),
          ("four", 4),
          ("none", 8),
          ("one", 1),
          ("seven", 7),
          ("six", 6),
          ("three", 3),
          ("two", 2))
    )


_X25DeviceWindowSize_Type.__name__ = "Integer32"
_X25DeviceWindowSize_Object = MibTableColumn
x25DeviceWindowSize = _X25DeviceWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 1, 1, 20),
    _X25DeviceWindowSize_Type()
)
x25DeviceWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DeviceWindowSize.setStatus("mandatory")


class _X25PlaceReverseChargeCalls_Type(Integer32):
    """Custom type x25PlaceReverseChargeCalls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_X25PlaceReverseChargeCalls_Type.__name__ = "Integer32"
_X25PlaceReverseChargeCalls_Object = MibTableColumn
x25PlaceReverseChargeCalls = _X25PlaceReverseChargeCalls_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 1, 1, 21),
    _X25PlaceReverseChargeCalls_Type()
)
x25PlaceReverseChargeCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25PlaceReverseChargeCalls.setStatus("mandatory")


class _X25AcceptReverseChargeCalls_Type(Integer32):
    """Custom type x25AcceptReverseChargeCalls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_X25AcceptReverseChargeCalls_Type.__name__ = "Integer32"
_X25AcceptReverseChargeCalls_Object = MibTableColumn
x25AcceptReverseChargeCalls = _X25AcceptReverseChargeCalls_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 1, 1, 22),
    _X25AcceptReverseChargeCalls_Type()
)
x25AcceptReverseChargeCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25AcceptReverseChargeCalls.setStatus("mandatory")


class _X25NPS_Type(Integer32):
    """Custom type x25NPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_X25NPS_Type.__name__ = "Integer32"
_X25NPS_Object = MibTableColumn
x25NPS = _X25NPS_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 1, 1, 23),
    _X25NPS_Type()
)
x25NPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25NPS.setStatus("mandatory")


class _X25CTS_Type(Integer32):
    """Custom type x25CTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_X25CTS_Type.__name__ = "Integer32"
_X25CTS_Object = MibTableColumn
x25CTS = _X25CTS_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 1, 1, 24),
    _X25CTS_Type()
)
x25CTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CTS.setStatus("mandatory")


class _X25DCD_Type(Integer32):
    """Custom type x25DCD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_X25DCD_Type.__name__ = "Integer32"
_X25DCD_Object = MibTableColumn
x25DCD = _X25DCD_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 1, 1, 25),
    _X25DCD_Type()
)
x25DCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DCD.setStatus("mandatory")


class _X25DSR_Type(Integer32):
    """Custom type x25DSR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_X25DSR_Type.__name__ = "Integer32"
_X25DSR_Object = MibTableColumn
x25DSR = _X25DSR_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 1, 1, 26),
    _X25DSR_Type()
)
x25DSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DSR.setStatus("mandatory")


class _X25DTR_Type(Integer32):
    """Custom type x25DTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_X25DTR_Type.__name__ = "Integer32"
_X25DTR_Object = MibTableColumn
x25DTR = _X25DTR_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 1, 1, 27),
    _X25DTR_Type()
)
x25DTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DTR.setStatus("mandatory")


class _X25RTS_Type(Integer32):
    """Custom type x25RTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_X25RTS_Type.__name__ = "Integer32"
_X25RTS_Object = MibTableColumn
x25RTS = _X25RTS_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 1, 1, 28),
    _X25RTS_Type()
)
x25RTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25RTS.setStatus("mandatory")


class _X25ReturnClock_Type(Integer32):
    """Custom type x25ReturnClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("no", 2),
          ("yes", 1))
    )


_X25ReturnClock_Type.__name__ = "Integer32"
_X25ReturnClock_Object = MibTableColumn
x25ReturnClock = _X25ReturnClock_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 1, 1, 29),
    _X25ReturnClock_Type()
)
x25ReturnClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ReturnClock.setStatus("mandatory")
_X25IPAddress_Type = IpAddress
_X25IPAddress_Object = MibTableColumn
x25IPAddress = _X25IPAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 1, 1, 30),
    _X25IPAddress_Type()
)
x25IPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25IPAddress.setStatus("mandatory")
_X25NetworkMask_Type = IpAddress
_X25NetworkMask_Object = MibTableColumn
x25NetworkMask = _X25NetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 1, 1, 31),
    _X25NetworkMask_Type()
)
x25NetworkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25NetworkMask.setStatus("mandatory")
_X25DefaultGatewayAddress_Type = IpAddress
_X25DefaultGatewayAddress_Object = MibTableColumn
x25DefaultGatewayAddress = _X25DefaultGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 1, 1, 32),
    _X25DefaultGatewayAddress_Type()
)
x25DefaultGatewayAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DefaultGatewayAddress.setStatus("mandatory")
_X25SecondDefaultGatewayAddress_Type = IpAddress
_X25SecondDefaultGatewayAddress_Object = MibTableColumn
x25SecondDefaultGatewayAddress = _X25SecondDefaultGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 1, 1, 33),
    _X25SecondDefaultGatewayAddress_Type()
)
x25SecondDefaultGatewayAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SecondDefaultGatewayAddress.setStatus("mandatory")
_X25StatsTable_Object = MibTable
x25StatsTable = _X25StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 2)
)
if mibBuilder.loadTexts:
    x25StatsTable.setStatus("mandatory")
_X25StatsEntry_Object = MibTableRow
x25StatsEntry = _X25StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 2, 1)
)
x25StatsEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "x25StatsPortIndex"),
)
if mibBuilder.loadTexts:
    x25StatsEntry.setStatus("mandatory")
_X25StatsPortIndex_Type = Integer32
_X25StatsPortIndex_Object = MibTableColumn
x25StatsPortIndex = _X25StatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 2, 1, 1),
    _X25StatsPortIndex_Type()
)
x25StatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatsPortIndex.setStatus("mandatory")


class _X25PortType_Type(Integer32):
    """Custom type x25PortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("xDCE-XLogicalDCE", 8),
          ("xDTE-XLogicalDTE", 7))
    )


_X25PortType_Type.__name__ = "Integer32"
_X25PortType_Object = MibTableColumn
x25PortType = _X25PortType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 2, 1, 2),
    _X25PortType_Type()
)
x25PortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25PortType.setStatus("mandatory")
_X25InFrames_Type = Counter32
_X25InFrames_Object = MibTableColumn
x25InFrames = _X25InFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 2, 1, 3),
    _X25InFrames_Type()
)
x25InFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25InFrames.setStatus("mandatory")
_X25OutFrames_Type = Counter32
_X25OutFrames_Object = MibTableColumn
x25OutFrames = _X25OutFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 2, 1, 4),
    _X25OutFrames_Type()
)
x25OutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25OutFrames.setStatus("mandatory")
_X25CInFrames_Type = Counter32
_X25CInFrames_Object = MibTableColumn
x25CInFrames = _X25CInFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 2, 1, 5),
    _X25CInFrames_Type()
)
x25CInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CInFrames.setStatus("mandatory")
_X25COutFrames_Type = Counter32
_X25COutFrames_Object = MibTableColumn
x25COutFrames = _X25COutFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 2, 1, 6),
    _X25COutFrames_Type()
)
x25COutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25COutFrames.setStatus("mandatory")
_X25FRMRInFrames_Type = Counter32
_X25FRMRInFrames_Object = MibTableColumn
x25FRMRInFrames = _X25FRMRInFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 2, 1, 7),
    _X25FRMRInFrames_Type()
)
x25FRMRInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25FRMRInFrames.setStatus("mandatory")
_X25FRMROutFrames_Type = Counter32
_X25FRMROutFrames_Object = MibTableColumn
x25FRMROutFrames = _X25FRMROutFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 2, 1, 8),
    _X25FRMROutFrames_Type()
)
x25FRMROutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25FRMROutFrames.setStatus("mandatory")
_X25Timeouts_Type = Counter32
_X25Timeouts_Object = MibTableColumn
x25Timeouts = _X25Timeouts_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 2, 1, 9),
    _X25Timeouts_Type()
)
x25Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25Timeouts.setStatus("mandatory")
_X25UFrames_Type = Counter32
_X25UFrames_Object = MibTableColumn
x25UFrames = _X25UFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 2, 1, 10),
    _X25UFrames_Type()
)
x25UFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25UFrames.setStatus("mandatory")
_X25Samples_Type = Counter32
_X25Samples_Object = MibTableColumn
x25Samples = _X25Samples_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 2, 1, 11),
    _X25Samples_Type()
)
x25Samples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25Samples.setStatus("mandatory")
_X25Sum_Type = Counter32
_X25Sum_Object = MibTableColumn
x25Sum = _X25Sum_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 2, 1, 12),
    _X25Sum_Type()
)
x25Sum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25Sum.setStatus("mandatory")
_X25SumsQ_Type = Counter32
_X25SumsQ_Object = MibTableColumn
x25SumsQ = _X25SumsQ_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 2, 1, 13),
    _X25SumsQ_Type()
)
x25SumsQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SumsQ.setStatus("mandatory")
_X25DataInPkts_Type = Counter32
_X25DataInPkts_Object = MibTableColumn
x25DataInPkts = _X25DataInPkts_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 2, 1, 14),
    _X25DataInPkts_Type()
)
x25DataInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DataInPkts.setStatus("mandatory")
_X25DataOutPkts_Type = Counter32
_X25DataOutPkts_Object = MibTableColumn
x25DataOutPkts = _X25DataOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 2, 1, 15),
    _X25DataOutPkts_Type()
)
x25DataOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DataOutPkts.setStatus("mandatory")
_X25DataInChrs_Type = Counter32
_X25DataInChrs_Object = MibTableColumn
x25DataInChrs = _X25DataInChrs_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 2, 1, 16),
    _X25DataInChrs_Type()
)
x25DataInChrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DataInChrs.setStatus("mandatory")
_X25DataOutChrs_Type = Counter32
_X25DataOutChrs_Object = MibTableColumn
x25DataOutChrs = _X25DataOutChrs_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 2, 1, 17),
    _X25DataOutChrs_Type()
)
x25DataOutChrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25DataOutChrs.setStatus("mandatory")
_X25QInPkts_Type = Counter32
_X25QInPkts_Object = MibTableColumn
x25QInPkts = _X25QInPkts_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 2, 1, 18),
    _X25QInPkts_Type()
)
x25QInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25QInPkts.setStatus("mandatory")
_X25QOutPkts_Type = Counter32
_X25QOutPkts_Object = MibTableColumn
x25QOutPkts = _X25QOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 2, 1, 19),
    _X25QOutPkts_Type()
)
x25QOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25QOutPkts.setStatus("mandatory")
_X25QInChrs_Type = Counter32
_X25QInChrs_Object = MibTableColumn
x25QInChrs = _X25QInChrs_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 2, 1, 20),
    _X25QInChrs_Type()
)
x25QInChrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25QInChrs.setStatus("mandatory")
_X25QOutChrs_Type = Counter32
_X25QOutChrs_Object = MibTableColumn
x25QOutChrs = _X25QOutChrs_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 2, 1, 21),
    _X25QOutChrs_Type()
)
x25QOutChrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25QOutChrs.setStatus("mandatory")
_X25SigInPkts_Type = Counter32
_X25SigInPkts_Object = MibTableColumn
x25SigInPkts = _X25SigInPkts_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 2, 1, 22),
    _X25SigInPkts_Type()
)
x25SigInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SigInPkts.setStatus("mandatory")
_X25SigOutPkts_Type = Counter32
_X25SigOutPkts_Object = MibTableColumn
x25SigOutPkts = _X25SigOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 2, 1, 23),
    _X25SigOutPkts_Type()
)
x25SigOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SigOutPkts.setStatus("mandatory")
_X25InResets_Type = Counter32
_X25InResets_Object = MibTableColumn
x25InResets = _X25InResets_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 2, 1, 24),
    _X25InResets_Type()
)
x25InResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25InResets.setStatus("mandatory")
_X25OutResets_Type = Counter32
_X25OutResets_Object = MibTableColumn
x25OutResets = _X25OutResets_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 2, 1, 25),
    _X25OutResets_Type()
)
x25OutResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25OutResets.setStatus("mandatory")
_X25InRestarts_Type = Counter32
_X25InRestarts_Object = MibTableColumn
x25InRestarts = _X25InRestarts_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 2, 1, 26),
    _X25InRestarts_Type()
)
x25InRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25InRestarts.setStatus("mandatory")
_X25OutRestarts_Type = Counter32
_X25OutRestarts_Object = MibTableColumn
x25OutRestarts = _X25OutRestarts_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 9, 2, 1, 27),
    _X25OutRestarts_Type()
)
x25OutRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25OutRestarts.setStatus("mandatory")
_LineAlcGroup_ObjectIdentity = ObjectIdentity
lineAlcGroup = _LineAlcGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 10)
)
_AlcConfigTable_Object = MibTable
alcConfigTable = _AlcConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 10, 1)
)
if mibBuilder.loadTexts:
    alcConfigTable.setStatus("mandatory")
_AlcConfigEntry_Object = MibTableRow
alcConfigEntry = _AlcConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 10, 1, 1)
)
alcConfigEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "alcConfigPortIndex"),
)
if mibBuilder.loadTexts:
    alcConfigEntry.setStatus("mandatory")
_AlcConfigPortIndex_Type = Integer32
_AlcConfigPortIndex_Object = MibTableColumn
alcConfigPortIndex = _AlcConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 10, 1, 1, 1),
    _AlcConfigPortIndex_Type()
)
alcConfigPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcConfigPortIndex.setStatus("mandatory")


class _AlcConfigType_Type(Integer32):
    """Custom type alcConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("hALC-HostALC", 24),
          ("tALC-TerminalALC", 23))
    )


_AlcConfigType_Type.__name__ = "Integer32"
_AlcConfigType_Object = MibTableColumn
alcConfigType = _AlcConfigType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 10, 1, 1, 2),
    _AlcConfigType_Type()
)
alcConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcConfigType.setStatus("mandatory")


class _AlcNAUName_Type(DisplayString):
    """Custom type alcNAUName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AlcNAUName_Type.__name__ = "DisplayString"
_AlcNAUName_Object = MibTableColumn
alcNAUName = _AlcNAUName_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 10, 1, 1, 3),
    _AlcNAUName_Type()
)
alcNAUName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcNAUName.setStatus("mandatory")


class _AlcInitState_Type(Integer32):
    """Custom type alcInitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in-service", 1),
          ("out-of-service", 2))
    )


_AlcInitState_Type.__name__ = "Integer32"
_AlcInitState_Object = MibTableColumn
alcInitState = _AlcInitState_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 10, 1, 1, 4),
    _AlcInitState_Type()
)
alcInitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcInitState.setStatus("mandatory")


class _AlcClocking_Type(Integer32):
    """Custom type alcClocking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("internal", 2))
    )


_AlcClocking_Type.__name__ = "Integer32"
_AlcClocking_Object = MibTableColumn
alcClocking = _AlcClocking_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 10, 1, 1, 5),
    _AlcClocking_Type()
)
alcClocking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcClocking.setStatus("mandatory")


class _AlcPortSpeed_Type(Integer32):
    """Custom type alcPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(12,
              24,
              48,
              96,
              192)
        )
    )
    namedValues = NamedValues(
        *(("speed1200", 12),
          ("speed19200", 192),
          ("speed2400", 24),
          ("speed4800", 48),
          ("speed9600", 96))
    )


_AlcPortSpeed_Type.__name__ = "Integer32"
_AlcPortSpeed_Object = MibTableColumn
alcPortSpeed = _AlcPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 10, 1, 1, 6),
    _AlcPortSpeed_Type()
)
alcPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPortSpeed.setStatus("mandatory")


class _AlcLimitSegsCharsBetweenPolls_Type(Integer32):
    """Custom type alcLimitSegsCharsBetweenPolls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlcLimitSegsCharsBetweenPolls_Type.__name__ = "Integer32"
_AlcLimitSegsCharsBetweenPolls_Object = MibTableColumn
alcLimitSegsCharsBetweenPolls = _AlcLimitSegsCharsBetweenPolls_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 10, 1, 1, 7),
    _AlcLimitSegsCharsBetweenPolls_Type()
)
alcLimitSegsCharsBetweenPolls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcLimitSegsCharsBetweenPolls.setStatus("mandatory")


class _AlcNumberOfSegments_Type(Integer32):
    """Custom type alcNumberOfSegments based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 99),
    )


_AlcNumberOfSegments_Type.__name__ = "Integer32"
_AlcNumberOfSegments_Object = MibTableColumn
alcNumberOfSegments = _AlcNumberOfSegments_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 10, 1, 1, 8),
    _AlcNumberOfSegments_Type()
)
alcNumberOfSegments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcNumberOfSegments.setStatus("mandatory")


class _AlcNumberOfCharacters_Type(Integer32):
    """Custom type alcNumberOfCharacters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 9999),
    )


_AlcNumberOfCharacters_Type.__name__ = "Integer32"
_AlcNumberOfCharacters_Object = MibTableColumn
alcNumberOfCharacters = _AlcNumberOfCharacters_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 10, 1, 1, 9),
    _AlcNumberOfCharacters_Type()
)
alcNumberOfCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcNumberOfCharacters.setStatus("mandatory")


class _AlcNumberOfNullSeg_Type(Integer32):
    """Custom type alcNumberOfNullSeg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_AlcNumberOfNullSeg_Type.__name__ = "Integer32"
_AlcNumberOfNullSeg_Object = MibTableColumn
alcNumberOfNullSeg = _AlcNumberOfNullSeg_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 10, 1, 1, 10),
    _AlcNumberOfNullSeg_Type()
)
alcNumberOfNullSeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcNumberOfNullSeg.setStatus("mandatory")


class _AlcCTS_Type(Integer32):
    """Custom type alcCTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlcCTS_Type.__name__ = "Integer32"
_AlcCTS_Object = MibTableColumn
alcCTS = _AlcCTS_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 10, 1, 1, 11),
    _AlcCTS_Type()
)
alcCTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcCTS.setStatus("mandatory")


class _AlcDCD_Type(Integer32):
    """Custom type alcDCD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlcDCD_Type.__name__ = "Integer32"
_AlcDCD_Object = MibTableColumn
alcDCD = _AlcDCD_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 10, 1, 1, 12),
    _AlcDCD_Type()
)
alcDCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcDCD.setStatus("mandatory")


class _AlcDSR_Type(Integer32):
    """Custom type alcDSR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlcDSR_Type.__name__ = "Integer32"
_AlcDSR_Object = MibTableColumn
alcDSR = _AlcDSR_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 10, 1, 1, 13),
    _AlcDSR_Type()
)
alcDSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcDSR.setStatus("mandatory")


class _AlcDTR_Type(Integer32):
    """Custom type alcDTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlcDTR_Type.__name__ = "Integer32"
_AlcDTR_Object = MibTableColumn
alcDTR = _AlcDTR_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 10, 1, 1, 14),
    _AlcDTR_Type()
)
alcDTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcDTR.setStatus("mandatory")


class _AlcRTS_Type(Integer32):
    """Custom type alcRTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlcRTS_Type.__name__ = "Integer32"
_AlcRTS_Object = MibTableColumn
alcRTS = _AlcRTS_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 10, 1, 1, 15),
    _AlcRTS_Type()
)
alcRTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcRTS.setStatus("mandatory")


class _AlcReturnClock_Type(Integer32):
    """Custom type alcReturnClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("no", 2),
          ("yes", 1))
    )


_AlcReturnClock_Type.__name__ = "Integer32"
_AlcReturnClock_Object = MibTableColumn
alcReturnClock = _AlcReturnClock_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 10, 1, 1, 16),
    _AlcReturnClock_Type()
)
alcReturnClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcReturnClock.setStatus("mandatory")
_AlcStatsTable_Object = MibTable
alcStatsTable = _AlcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 10, 2)
)
if mibBuilder.loadTexts:
    alcStatsTable.setStatus("mandatory")
_AlcStatsEntry_Object = MibTableRow
alcStatsEntry = _AlcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 10, 2, 1)
)
alcStatsEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "alcStatsPortIndex"),
)
if mibBuilder.loadTexts:
    alcStatsEntry.setStatus("mandatory")
_AlcStatsPortIndex_Type = Integer32
_AlcStatsPortIndex_Object = MibTableColumn
alcStatsPortIndex = _AlcStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 10, 2, 1, 1),
    _AlcStatsPortIndex_Type()
)
alcStatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcStatsPortIndex.setStatus("mandatory")


class _AlcPortType_Type(Integer32):
    """Custom type alcPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("hALC-HostALC", 24),
          ("tALC-TerminalALC", 23))
    )


_AlcPortType_Type.__name__ = "Integer32"
_AlcPortType_Object = MibTableColumn
alcPortType = _AlcPortType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 10, 2, 1, 2),
    _AlcPortType_Type()
)
alcPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPortType.setStatus("mandatory")
_AlcRxOverruns_Type = Counter32
_AlcRxOverruns_Object = MibTableColumn
alcRxOverruns = _AlcRxOverruns_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 10, 2, 1, 3),
    _AlcRxOverruns_Type()
)
alcRxOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcRxOverruns.setStatus("mandatory")
_AlcBytesRx_Type = Counter32
_AlcBytesRx_Object = MibTableColumn
alcBytesRx = _AlcBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 10, 2, 1, 4),
    _AlcBytesRx_Type()
)
alcBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcBytesRx.setStatus("mandatory")
_AlcBytesTx_Type = Counter32
_AlcBytesTx_Object = MibTableColumn
alcBytesTx = _AlcBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 10, 2, 1, 5),
    _AlcBytesTx_Type()
)
alcBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcBytesTx.setStatus("mandatory")
_AlcBytesRxDisc_Type = Counter32
_AlcBytesRxDisc_Object = MibTableColumn
alcBytesRxDisc = _AlcBytesRxDisc_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 10, 2, 1, 6),
    _AlcBytesRxDisc_Type()
)
alcBytesRxDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcBytesRxDisc.setStatus("mandatory")
_AlcBytesTxDisc_Type = Counter32
_AlcBytesTxDisc_Object = MibTableColumn
alcBytesTxDisc = _AlcBytesTxDisc_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 10, 2, 1, 7),
    _AlcBytesTxDisc_Type()
)
alcBytesTxDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcBytesTxDisc.setStatus("mandatory")
_AlcPortFaults_Type = Counter32
_AlcPortFaults_Object = MibTableColumn
alcPortFaults = _AlcPortFaults_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 10, 2, 1, 8),
    _AlcPortFaults_Type()
)
alcPortFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPortFaults.setStatus("mandatory")
_AlcRcvCCCErrors_Type = Counter32
_AlcRcvCCCErrors_Object = MibTableColumn
alcRcvCCCErrors = _AlcRcvCCCErrors_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 10, 2, 1, 9),
    _AlcRcvCCCErrors_Type()
)
alcRcvCCCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcRcvCCCErrors.setStatus("mandatory")
_AlcPollTx_Type = Counter32
_AlcPollTx_Object = MibTableColumn
alcPollTx = _AlcPollTx_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 10, 2, 1, 10),
    _AlcPollTx_Type()
)
alcPollTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPollTx.setStatus("mandatory")
_AlcResponseTimeouts_Type = Counter32
_AlcResponseTimeouts_Object = MibTableColumn
alcResponseTimeouts = _AlcResponseTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 10, 2, 1, 11),
    _AlcResponseTimeouts_Type()
)
alcResponseTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcResponseTimeouts.setStatus("mandatory")
_AlcSegRx_Type = Counter32
_AlcSegRx_Object = MibTableColumn
alcSegRx = _AlcSegRx_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 10, 2, 1, 12),
    _AlcSegRx_Type()
)
alcSegRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcSegRx.setStatus("mandatory")
_AlcSegTx_Type = Counter32
_AlcSegTx_Object = MibTableColumn
alcSegTx = _AlcSegTx_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 10, 2, 1, 13),
    _AlcSegTx_Type()
)
alcSegTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcSegTx.setStatus("mandatory")
_AlcSegRxDisc_Type = Counter32
_AlcSegRxDisc_Object = MibTableColumn
alcSegRxDisc = _AlcSegRxDisc_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 10, 2, 1, 14),
    _AlcSegRxDisc_Type()
)
alcSegRxDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcSegRxDisc.setStatus("mandatory")
_AlcSegTxDisc_Type = Counter32
_AlcSegTxDisc_Object = MibTableColumn
alcSegTxDisc = _AlcSegTxDisc_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 5, 10, 2, 1, 15),
    _AlcSegTxDisc_Type()
)
alcSegTxDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcSegTxDisc.setStatus("mandatory")
_NodePUGroup_ObjectIdentity = ObjectIdentity
nodePUGroup = _NodePUGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 6)
)
_PuControlGroup_ObjectIdentity = ObjectIdentity
puControlGroup = _PuControlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 1)
)
_PuControlTable_Object = MibTable
puControlTable = _PuControlTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 1, 1)
)
if mibBuilder.loadTexts:
    puControlTable.setStatus("mandatory")
_PuControlEntry_Object = MibTableRow
puControlEntry = _PuControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 1, 1, 1)
)
puControlEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "puControlLineIndex"),
    (0, "SYNC-RESEARCH-MIB", "puControlPUAddress"),
)
if mibBuilder.loadTexts:
    puControlEntry.setStatus("mandatory")
_PuControlLineIndex_Type = Integer32
_PuControlLineIndex_Object = MibTableColumn
puControlLineIndex = _PuControlLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 1, 1, 1, 1),
    _PuControlLineIndex_Type()
)
puControlLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puControlLineIndex.setStatus("mandatory")


class _PuControlPUAddress_Type(OctetString):
    """Custom type puControlPUAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_PuControlPUAddress_Type.__name__ = "OctetString"
_PuControlPUAddress_Object = MibTableColumn
puControlPUAddress = _PuControlPUAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 1, 1, 1, 2),
    _PuControlPUAddress_Type()
)
puControlPUAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puControlPUAddress.setStatus("mandatory")


class _PuStatus_Type(Integer32):
    """Custom type puStatus based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("enable-all", 5),
          ("failed", 3),
          ("restart", 4))
    )


_PuStatus_Type.__name__ = "Integer32"
_PuStatus_Object = MibTableColumn
puStatus = _PuStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 1, 1, 1, 3),
    _PuStatus_Type()
)
puStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puStatus.setStatus("mandatory")


class _PuConnectionStatus_Type(Integer32):
    """Custom type puConnectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("not-connected", 2))
    )


_PuConnectionStatus_Type.__name__ = "Integer32"
_PuConnectionStatus_Object = MibTableColumn
puConnectionStatus = _PuConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 1, 1, 1, 4),
    _PuConnectionStatus_Type()
)
puConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puConnectionStatus.setStatus("mandatory")


class _PuLastClearCode_Type(OctetString):
    """Custom type puLastClearCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_PuLastClearCode_Type.__name__ = "OctetString"
_PuLastClearCode_Object = MibTableColumn
puLastClearCode = _PuLastClearCode_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 1, 1, 1, 5),
    _PuLastClearCode_Type()
)
puLastClearCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puLastClearCode.setStatus("mandatory")


class _PuControlFailureCode_Type(OctetString):
    """Custom type puControlFailureCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_PuControlFailureCode_Type.__name__ = "OctetString"
_PuControlFailureCode_Object = MibTableColumn
puControlFailureCode = _PuControlFailureCode_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 1, 1, 1, 6),
    _PuControlFailureCode_Type()
)
puControlFailureCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puControlFailureCode.setStatus("mandatory")


class _PuControlNAUName_Type(DisplayString):
    """Custom type puControlNAUName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_PuControlNAUName_Type.__name__ = "DisplayString"
_PuControlNAUName_Object = MibTableColumn
puControlNAUName = _PuControlNAUName_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 1, 1, 1, 7),
    _PuControlNAUName_Type()
)
puControlNAUName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puControlNAUName.setStatus("mandatory")
_PuConnectionAttemptCount_Type = Integer32
_PuConnectionAttemptCount_Object = MibTableColumn
puConnectionAttemptCount = _PuConnectionAttemptCount_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 1, 1, 1, 8),
    _PuConnectionAttemptCount_Type()
)
puConnectionAttemptCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puConnectionAttemptCount.setStatus("mandatory")


class _PuStatusIgnored_Type(Integer32):
    """Custom type puStatusIgnored based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_PuStatusIgnored_Type.__name__ = "Integer32"
_PuStatusIgnored_Object = MibTableColumn
puStatusIgnored = _PuStatusIgnored_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 1, 1, 1, 9),
    _PuStatusIgnored_Type()
)
puStatusIgnored.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puStatusIgnored.setStatus("mandatory")


class _PuStatusAcknowledged_Type(Integer32):
    """Custom type puStatusAcknowledged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_PuStatusAcknowledged_Type.__name__ = "Integer32"
_PuStatusAcknowledged_Object = MibTableColumn
puStatusAcknowledged = _PuStatusAcknowledged_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 1, 1, 1, 10),
    _PuStatusAcknowledged_Type()
)
puStatusAcknowledged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puStatusAcknowledged.setStatus("mandatory")
_PuLastDlciCleared_Type = Integer32
_PuLastDlciCleared_Object = MibTableColumn
puLastDlciCleared = _PuLastDlciCleared_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 1, 1, 1, 11),
    _PuLastDlciCleared_Type()
)
puLastDlciCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puLastDlciCleared.setStatus("mandatory")
_PuCurrentDlci_Type = Integer32
_PuCurrentDlci_Object = MibTableColumn
puCurrentDlci = _PuCurrentDlci_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 1, 1, 1, 12),
    _PuCurrentDlci_Type()
)
puCurrentDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puCurrentDlci.setStatus("mandatory")
_PuLastMACCleared_Type = PhysAddress
_PuLastMACCleared_Object = MibTableColumn
puLastMACCleared = _PuLastMACCleared_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 1, 1, 1, 13),
    _PuLastMACCleared_Type()
)
puLastMACCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puLastMACCleared.setStatus("mandatory")
_PuCurrentMAC_Type = PhysAddress
_PuCurrentMAC_Object = MibTableColumn
puCurrentMAC = _PuCurrentMAC_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 1, 1, 1, 14),
    _PuCurrentMAC_Type()
)
puCurrentMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puCurrentMAC.setStatus("mandatory")


class _PuNetworkType_Type(Integer32):
    """Custom type puNetworkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8,
              17,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-type", 17),
          ("frame-relay-dialbackup-type", 20),
          ("frame-relay-type", 19),
          ("token-ring-type", 21),
          ("xDCE-XLogicalDCE", 8),
          ("xDTE-XLogicalDTE", 7))
    )


_PuNetworkType_Type.__name__ = "Integer32"
_PuNetworkType_Object = MibTableColumn
puNetworkType = _PuNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 1, 1, 1, 15),
    _PuNetworkType_Type()
)
puNetworkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puNetworkType.setStatus("mandatory")


class _PuCurrentConnectionType_Type(Integer32):
    """Custom type puCurrentConnectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dsp", 1),
          ("llc2", 3),
          ("qllc", 2))
    )


_PuCurrentConnectionType_Type.__name__ = "Integer32"
_PuCurrentConnectionType_Object = MibTableColumn
puCurrentConnectionType = _PuCurrentConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 1, 1, 1, 16),
    _PuCurrentConnectionType_Type()
)
puCurrentConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puCurrentConnectionType.setStatus("mandatory")
_PuLastSVCCleared_Type = Integer32
_PuLastSVCCleared_Object = MibTableColumn
puLastSVCCleared = _PuLastSVCCleared_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 1, 1, 1, 17),
    _PuLastSVCCleared_Type()
)
puLastSVCCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puLastSVCCleared.setStatus("mandatory")
_PuCurrentSVC_Type = Integer32
_PuCurrentSVC_Object = MibTableColumn
puCurrentSVC = _PuCurrentSVC_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 1, 1, 1, 18),
    _PuCurrentSVC_Type()
)
puCurrentSVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puCurrentSVC.setStatus("mandatory")
_PuLastLocalDTECleared_Type = OctetString
_PuLastLocalDTECleared_Object = MibTableColumn
puLastLocalDTECleared = _PuLastLocalDTECleared_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 1, 1, 1, 19),
    _PuLastLocalDTECleared_Type()
)
puLastLocalDTECleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puLastLocalDTECleared.setStatus("mandatory")
_PuLastRemoteDTECleared_Type = OctetString
_PuLastRemoteDTECleared_Object = MibTableColumn
puLastRemoteDTECleared = _PuLastRemoteDTECleared_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 1, 1, 1, 20),
    _PuLastRemoteDTECleared_Type()
)
puLastRemoteDTECleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puLastRemoteDTECleared.setStatus("mandatory")
_PuCurrentLocalDTE_Type = OctetString
_PuCurrentLocalDTE_Object = MibTableColumn
puCurrentLocalDTE = _PuCurrentLocalDTE_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 1, 1, 1, 21),
    _PuCurrentLocalDTE_Type()
)
puCurrentLocalDTE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puCurrentLocalDTE.setStatus("mandatory")
_PuCurrentRemoteDTE_Type = OctetString
_PuCurrentRemoteDTE_Object = MibTableColumn
puCurrentRemoteDTE = _PuCurrentRemoteDTE_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 1, 1, 1, 22),
    _PuCurrentRemoteDTE_Type()
)
puCurrentRemoteDTE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puCurrentRemoteDTE.setStatus("mandatory")


class _PuIsDynamic_Type(Integer32):
    """Custom type puIsDynamic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_PuIsDynamic_Type.__name__ = "Integer32"
_PuIsDynamic_Object = MibTableColumn
puIsDynamic = _PuIsDynamic_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 1, 1, 1, 23),
    _PuIsDynamic_Type()
)
puIsDynamic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puIsDynamic.setStatus("mandatory")
_PuSDLCGroup_ObjectIdentity = ObjectIdentity
puSDLCGroup = _PuSDLCGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2)
)
_SdlcPuConfigTable_Object = MibTable
sdlcPuConfigTable = _SdlcPuConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 1)
)
if mibBuilder.loadTexts:
    sdlcPuConfigTable.setStatus("mandatory")
_SdlcPuConfigEntry_Object = MibTableRow
sdlcPuConfigEntry = _SdlcPuConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 1, 1)
)
sdlcPuConfigEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "sdlcPuConfigLineIndex"),
    (0, "SYNC-RESEARCH-MIB", "sdlcPuConfigAddress"),
)
if mibBuilder.loadTexts:
    sdlcPuConfigEntry.setStatus("mandatory")
_SdlcPuConfigLineIndex_Type = Integer32
_SdlcPuConfigLineIndex_Object = MibTableColumn
sdlcPuConfigLineIndex = _SdlcPuConfigLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 1, 1, 1),
    _SdlcPuConfigLineIndex_Type()
)
sdlcPuConfigLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPuConfigLineIndex.setStatus("mandatory")


class _SdlcPuConfigAddress_Type(OctetString):
    """Custom type sdlcPuConfigAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_SdlcPuConfigAddress_Type.__name__ = "OctetString"
_SdlcPuConfigAddress_Object = MibTableColumn
sdlcPuConfigAddress = _SdlcPuConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 1, 1, 2),
    _SdlcPuConfigAddress_Type()
)
sdlcPuConfigAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPuConfigAddress.setStatus("mandatory")


class _SdlcPuNAUName_Type(DisplayString):
    """Custom type sdlcPuNAUName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_SdlcPuNAUName_Type.__name__ = "DisplayString"
_SdlcPuNAUName_Object = MibTableColumn
sdlcPuNAUName = _SdlcPuNAUName_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 1, 1, 3),
    _SdlcPuNAUName_Type()
)
sdlcPuNAUName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPuNAUName.setStatus("mandatory")


class _SdlcPuInitialState_Type(Integer32):
    """Custom type sdlcPuInitialState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in-service", 1),
          ("out-of-service", 2))
    )


_SdlcPuInitialState_Type.__name__ = "Integer32"
_SdlcPuInitialState_Object = MibTableColumn
sdlcPuInitialState = _SdlcPuInitialState_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 1, 1, 4),
    _SdlcPuInitialState_Type()
)
sdlcPuInitialState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPuInitialState.setStatus("mandatory")


class _SdlcPuXID_Type(OctetString):
    """Custom type sdlcPuXID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SdlcPuXID_Type.__name__ = "OctetString"
_SdlcPuXID_Object = MibTableColumn
sdlcPuXID = _SdlcPuXID_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 1, 1, 5),
    _SdlcPuXID_Type()
)
sdlcPuXID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPuXID.setStatus("mandatory")


class _SdlcPuType_Type(Integer32):
    """Custom type sdlcPuType based on Integer32"""
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
        *(("type1", 1),
          ("type2", 2),
          ("type2-1", 3),
          ("type4", 4),
          ("type5", 5))
    )


_SdlcPuType_Type.__name__ = "Integer32"
_SdlcPuType_Object = MibTableColumn
sdlcPuType = _SdlcPuType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 1, 1, 6),
    _SdlcPuType_Type()
)
sdlcPuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPuType.setStatus("mandatory")


class _SdlcPuGroupPollAddress_Type(OctetString):
    """Custom type sdlcPuGroupPollAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_SdlcPuGroupPollAddress_Type.__name__ = "OctetString"
_SdlcPuGroupPollAddress_Object = MibTableColumn
sdlcPuGroupPollAddress = _SdlcPuGroupPollAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 1, 1, 7),
    _SdlcPuGroupPollAddress_Type()
)
sdlcPuGroupPollAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPuGroupPollAddress.setStatus("mandatory")


class _SdlcPuConnectionID_Type(OctetString):
    """Custom type sdlcPuConnectionID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SdlcPuConnectionID_Type.__name__ = "OctetString"
_SdlcPuConnectionID_Object = MibTableColumn
sdlcPuConnectionID = _SdlcPuConnectionID_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 1, 1, 8),
    _SdlcPuConnectionID_Type()
)
sdlcPuConnectionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPuConnectionID.setStatus("mandatory")
_SdlcPuMAXOUT_Type = Integer32
_SdlcPuMAXOUT_Object = MibTableColumn
sdlcPuMAXOUT = _SdlcPuMAXOUT_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 1, 1, 9),
    _SdlcPuMAXOUT_Type()
)
sdlcPuMAXOUT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPuMAXOUT.setStatus("mandatory")


class _SdlcPuConnectType_Type(Integer32):
    """Custom type sdlcPuConnectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("answer", 1),
          ("originate", 2))
    )


_SdlcPuConnectType_Type.__name__ = "Integer32"
_SdlcPuConnectType_Object = MibTableColumn
sdlcPuConnectType = _SdlcPuConnectType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 1, 1, 10),
    _SdlcPuConnectType_Type()
)
sdlcPuConnectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPuConnectType.setStatus("mandatory")
_SdlcPuStatsTable_Object = MibTable
sdlcPuStatsTable = _SdlcPuStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 2)
)
if mibBuilder.loadTexts:
    sdlcPuStatsTable.setStatus("mandatory")
_SdlcPuStatsEntry_Object = MibTableRow
sdlcPuStatsEntry = _SdlcPuStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 2, 1)
)
sdlcPuStatsEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "sdlcPuStatsLineIndex"),
    (0, "SYNC-RESEARCH-MIB", "sdlcPuStatsAddress"),
)
if mibBuilder.loadTexts:
    sdlcPuStatsEntry.setStatus("mandatory")
_SdlcPuStatsLineIndex_Type = Integer32
_SdlcPuStatsLineIndex_Object = MibTableColumn
sdlcPuStatsLineIndex = _SdlcPuStatsLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 2, 1, 1),
    _SdlcPuStatsLineIndex_Type()
)
sdlcPuStatsLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPuStatsLineIndex.setStatus("mandatory")


class _SdlcPuStatsAddress_Type(OctetString):
    """Custom type sdlcPuStatsAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_SdlcPuStatsAddress_Type.__name__ = "OctetString"
_SdlcPuStatsAddress_Object = MibTableColumn
sdlcPuStatsAddress = _SdlcPuStatsAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 2, 1, 2),
    _SdlcPuStatsAddress_Type()
)
sdlcPuStatsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPuStatsAddress.setStatus("mandatory")
_SdlcPuInIFrames_Type = Counter32
_SdlcPuInIFrames_Object = MibTableColumn
sdlcPuInIFrames = _SdlcPuInIFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 2, 1, 3),
    _SdlcPuInIFrames_Type()
)
sdlcPuInIFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPuInIFrames.setStatus("mandatory")
_SdlcPuOutIFrames_Type = Counter32
_SdlcPuOutIFrames_Object = MibTableColumn
sdlcPuOutIFrames = _SdlcPuOutIFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 2, 1, 4),
    _SdlcPuOutIFrames_Type()
)
sdlcPuOutIFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPuOutIFrames.setStatus("mandatory")
_SdlcPuInRRFrames_Type = Counter32
_SdlcPuInRRFrames_Object = MibTableColumn
sdlcPuInRRFrames = _SdlcPuInRRFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 2, 1, 5),
    _SdlcPuInRRFrames_Type()
)
sdlcPuInRRFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPuInRRFrames.setStatus("mandatory")
_SdlcPuOutRRFrames_Type = Counter32
_SdlcPuOutRRFrames_Object = MibTableColumn
sdlcPuOutRRFrames = _SdlcPuOutRRFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 2, 1, 6),
    _SdlcPuOutRRFrames_Type()
)
sdlcPuOutRRFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPuOutRRFrames.setStatus("mandatory")
_SdlcPuInRNRFrames_Type = Counter32
_SdlcPuInRNRFrames_Object = MibTableColumn
sdlcPuInRNRFrames = _SdlcPuInRNRFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 2, 1, 7),
    _SdlcPuInRNRFrames_Type()
)
sdlcPuInRNRFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPuInRNRFrames.setStatus("mandatory")
_SdlcPuOutRNRFrames_Type = Counter32
_SdlcPuOutRNRFrames_Object = MibTableColumn
sdlcPuOutRNRFrames = _SdlcPuOutRNRFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 2, 1, 8),
    _SdlcPuOutRNRFrames_Type()
)
sdlcPuOutRNRFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPuOutRNRFrames.setStatus("mandatory")
_SdlcPuInXIDFrames_Type = Counter32
_SdlcPuInXIDFrames_Object = MibTableColumn
sdlcPuInXIDFrames = _SdlcPuInXIDFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 2, 1, 9),
    _SdlcPuInXIDFrames_Type()
)
sdlcPuInXIDFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPuInXIDFrames.setStatus("mandatory")
_SdlcPuOutXIDFrames_Type = Counter32
_SdlcPuOutXIDFrames_Object = MibTableColumn
sdlcPuOutXIDFrames = _SdlcPuOutXIDFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 2, 1, 10),
    _SdlcPuOutXIDFrames_Type()
)
sdlcPuOutXIDFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPuOutXIDFrames.setStatus("mandatory")
_SdlcPuInTESTFrames_Type = Counter32
_SdlcPuInTESTFrames_Object = MibTableColumn
sdlcPuInTESTFrames = _SdlcPuInTESTFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 2, 1, 11),
    _SdlcPuInTESTFrames_Type()
)
sdlcPuInTESTFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPuInTESTFrames.setStatus("mandatory")
_SdlcPuOutTESTFrames_Type = Counter32
_SdlcPuOutTESTFrames_Object = MibTableColumn
sdlcPuOutTESTFrames = _SdlcPuOutTESTFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 2, 1, 12),
    _SdlcPuOutTESTFrames_Type()
)
sdlcPuOutTESTFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPuOutTESTFrames.setStatus("mandatory")
_SdlcPuInSNRMFrames_Type = Counter32
_SdlcPuInSNRMFrames_Object = MibTableColumn
sdlcPuInSNRMFrames = _SdlcPuInSNRMFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 2, 1, 13),
    _SdlcPuInSNRMFrames_Type()
)
sdlcPuInSNRMFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPuInSNRMFrames.setStatus("mandatory")
_SdlcPuOutSNRMFrames_Type = Counter32
_SdlcPuOutSNRMFrames_Object = MibTableColumn
sdlcPuOutSNRMFrames = _SdlcPuOutSNRMFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 2, 1, 14),
    _SdlcPuOutSNRMFrames_Type()
)
sdlcPuOutSNRMFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPuOutSNRMFrames.setStatus("mandatory")
_SdlcPuInDISCFrames_Type = Counter32
_SdlcPuInDISCFrames_Object = MibTableColumn
sdlcPuInDISCFrames = _SdlcPuInDISCFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 2, 1, 15),
    _SdlcPuInDISCFrames_Type()
)
sdlcPuInDISCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPuInDISCFrames.setStatus("mandatory")
_SdlcPuOutDISCFrames_Type = Counter32
_SdlcPuOutDISCFrames_Object = MibTableColumn
sdlcPuOutDISCFrames = _SdlcPuOutDISCFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 2, 1, 16),
    _SdlcPuOutDISCFrames_Type()
)
sdlcPuOutDISCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPuOutDISCFrames.setStatus("mandatory")
_SdlcPuInDMFrames_Type = Counter32
_SdlcPuInDMFrames_Object = MibTableColumn
sdlcPuInDMFrames = _SdlcPuInDMFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 2, 1, 17),
    _SdlcPuInDMFrames_Type()
)
sdlcPuInDMFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPuInDMFrames.setStatus("mandatory")
_SdlcPuOutDMFrames_Type = Counter32
_SdlcPuOutDMFrames_Object = MibTableColumn
sdlcPuOutDMFrames = _SdlcPuOutDMFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 2, 1, 18),
    _SdlcPuOutDMFrames_Type()
)
sdlcPuOutDMFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPuOutDMFrames.setStatus("mandatory")
_SdlcPuInUAFrames_Type = Counter32
_SdlcPuInUAFrames_Object = MibTableColumn
sdlcPuInUAFrames = _SdlcPuInUAFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 2, 1, 19),
    _SdlcPuInUAFrames_Type()
)
sdlcPuInUAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPuInUAFrames.setStatus("mandatory")
_SdlcPuOutUAFrames_Type = Counter32
_SdlcPuOutUAFrames_Object = MibTableColumn
sdlcPuOutUAFrames = _SdlcPuOutUAFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 2, 1, 20),
    _SdlcPuOutUAFrames_Type()
)
sdlcPuOutUAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPuOutUAFrames.setStatus("mandatory")
_SdlcPuInFRMRFrames_Type = Counter32
_SdlcPuInFRMRFrames_Object = MibTableColumn
sdlcPuInFRMRFrames = _SdlcPuInFRMRFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 2, 1, 21),
    _SdlcPuInFRMRFrames_Type()
)
sdlcPuInFRMRFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPuInFRMRFrames.setStatus("mandatory")
_SdlcPuOutFRMRFrames_Type = Counter32
_SdlcPuOutFRMRFrames_Object = MibTableColumn
sdlcPuOutFRMRFrames = _SdlcPuOutFRMRFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 2, 1, 22),
    _SdlcPuOutFRMRFrames_Type()
)
sdlcPuOutFRMRFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPuOutFRMRFrames.setStatus("mandatory")
_SdlcPuInRDFrames_Type = Counter32
_SdlcPuInRDFrames_Object = MibTableColumn
sdlcPuInRDFrames = _SdlcPuInRDFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 2, 1, 23),
    _SdlcPuInRDFrames_Type()
)
sdlcPuInRDFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPuInRDFrames.setStatus("mandatory")
_SdlcPuOutRDFrames_Type = Counter32
_SdlcPuOutRDFrames_Object = MibTableColumn
sdlcPuOutRDFrames = _SdlcPuOutRDFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 2, 1, 24),
    _SdlcPuOutRDFrames_Type()
)
sdlcPuOutRDFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPuOutRDFrames.setStatus("mandatory")
_SdlcPuInUIFrames_Type = Counter32
_SdlcPuInUIFrames_Object = MibTableColumn
sdlcPuInUIFrames = _SdlcPuInUIFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 2, 1, 25),
    _SdlcPuInUIFrames_Type()
)
sdlcPuInUIFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPuInUIFrames.setStatus("mandatory")
_SdlcPuOutUIFrames_Type = Counter32
_SdlcPuOutUIFrames_Object = MibTableColumn
sdlcPuOutUIFrames = _SdlcPuOutUIFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 2, 1, 26),
    _SdlcPuOutUIFrames_Type()
)
sdlcPuOutUIFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPuOutUIFrames.setStatus("mandatory")
_SdlcPuReTxIFrames_Type = Counter32
_SdlcPuReTxIFrames_Object = MibTableColumn
sdlcPuReTxIFrames = _SdlcPuReTxIFrames_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 2, 1, 27),
    _SdlcPuReTxIFrames_Type()
)
sdlcPuReTxIFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPuReTxIFrames.setStatus("mandatory")
_SdlcPuPollResponseTimeouts_Type = Counter32
_SdlcPuPollResponseTimeouts_Object = MibTableColumn
sdlcPuPollResponseTimeouts = _SdlcPuPollResponseTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 2, 2, 1, 28),
    _SdlcPuPollResponseTimeouts_Type()
)
sdlcPuPollResponseTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPuPollResponseTimeouts.setStatus("mandatory")
_PuBisyncGroup_ObjectIdentity = ObjectIdentity
puBisyncGroup = _PuBisyncGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 3)
)
_BisyncPuConfigTable_Object = MibTable
bisyncPuConfigTable = _BisyncPuConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 3, 1)
)
if mibBuilder.loadTexts:
    bisyncPuConfigTable.setStatus("mandatory")
_BisyncPuConfigEntry_Object = MibTableRow
bisyncPuConfigEntry = _BisyncPuConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 3, 1, 1)
)
bisyncPuConfigEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "bisyncPuConfigLineIndex"),
    (0, "SYNC-RESEARCH-MIB", "bisyncPuConfigAddress"),
)
if mibBuilder.loadTexts:
    bisyncPuConfigEntry.setStatus("mandatory")
_BisyncPuConfigLineIndex_Type = Integer32
_BisyncPuConfigLineIndex_Object = MibTableColumn
bisyncPuConfigLineIndex = _BisyncPuConfigLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 3, 1, 1, 1),
    _BisyncPuConfigLineIndex_Type()
)
bisyncPuConfigLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncPuConfigLineIndex.setStatus("mandatory")


class _BisyncPuConfigAddress_Type(OctetString):
    """Custom type bisyncPuConfigAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_BisyncPuConfigAddress_Type.__name__ = "OctetString"
_BisyncPuConfigAddress_Object = MibTableColumn
bisyncPuConfigAddress = _BisyncPuConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 3, 1, 1, 2),
    _BisyncPuConfigAddress_Type()
)
bisyncPuConfigAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncPuConfigAddress.setStatus("mandatory")


class _BisyncPuNAUName_Type(DisplayString):
    """Custom type bisyncPuNAUName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_BisyncPuNAUName_Type.__name__ = "DisplayString"
_BisyncPuNAUName_Object = MibTableColumn
bisyncPuNAUName = _BisyncPuNAUName_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 3, 1, 1, 3),
    _BisyncPuNAUName_Type()
)
bisyncPuNAUName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncPuNAUName.setStatus("mandatory")


class _BisyncPuInitialState_Type(Integer32):
    """Custom type bisyncPuInitialState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in-service", 1),
          ("out-of-service", 2))
    )


_BisyncPuInitialState_Type.__name__ = "Integer32"
_BisyncPuInitialState_Object = MibTableColumn
bisyncPuInitialState = _BisyncPuInitialState_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 3, 1, 1, 4),
    _BisyncPuInitialState_Type()
)
bisyncPuInitialState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncPuInitialState.setStatus("mandatory")


class _BisyncPuXID_Type(OctetString):
    """Custom type bisyncPuXID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_BisyncPuXID_Type.__name__ = "OctetString"
_BisyncPuXID_Object = MibTableColumn
bisyncPuXID = _BisyncPuXID_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 3, 1, 1, 5),
    _BisyncPuXID_Type()
)
bisyncPuXID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncPuXID.setStatus("mandatory")


class _BisyncPuTargetHostType_Type(Integer32):
    """Custom type bisyncPuTargetHostType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bisync-host-type", 2),
          ("ice-host-type", 3),
          ("sna-host-type", 1))
    )


_BisyncPuTargetHostType_Type.__name__ = "Integer32"
_BisyncPuTargetHostType_Object = MibTableColumn
bisyncPuTargetHostType = _BisyncPuTargetHostType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 3, 1, 1, 6),
    _BisyncPuTargetHostType_Type()
)
bisyncPuTargetHostType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncPuTargetHostType.setStatus("mandatory")
_BisyncPuMaxData_Type = Integer32
_BisyncPuMaxData_Object = MibTableColumn
bisyncPuMaxData = _BisyncPuMaxData_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 3, 1, 1, 7),
    _BisyncPuMaxData_Type()
)
bisyncPuMaxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncPuMaxData.setStatus("mandatory")


class _BisyncPuConnectionID_Type(OctetString):
    """Custom type bisyncPuConnectionID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_BisyncPuConnectionID_Type.__name__ = "OctetString"
_BisyncPuConnectionID_Object = MibTableColumn
bisyncPuConnectionID = _BisyncPuConnectionID_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 3, 1, 1, 8),
    _BisyncPuConnectionID_Type()
)
bisyncPuConnectionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncPuConnectionID.setStatus("mandatory")


class _BisyncPuConnectType_Type(Integer32):
    """Custom type bisyncPuConnectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("answer", 1),
          ("originate", 2))
    )


_BisyncPuConnectType_Type.__name__ = "Integer32"
_BisyncPuConnectType_Object = MibTableColumn
bisyncPuConnectType = _BisyncPuConnectType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 3, 1, 1, 9),
    _BisyncPuConnectType_Type()
)
bisyncPuConnectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncPuConnectType.setStatus("mandatory")
_BisyncPuStatsTable_Object = MibTable
bisyncPuStatsTable = _BisyncPuStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 3, 2)
)
if mibBuilder.loadTexts:
    bisyncPuStatsTable.setStatus("mandatory")
_BisyncPuStatsEntry_Object = MibTableRow
bisyncPuStatsEntry = _BisyncPuStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 3, 2, 1)
)
bisyncPuStatsEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "bisyncPuStatsLineIndex"),
    (0, "SYNC-RESEARCH-MIB", "bisyncPuStatsAddress"),
)
if mibBuilder.loadTexts:
    bisyncPuStatsEntry.setStatus("mandatory")
_BisyncPuStatsLineIndex_Type = Integer32
_BisyncPuStatsLineIndex_Object = MibTableColumn
bisyncPuStatsLineIndex = _BisyncPuStatsLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 3, 2, 1, 1),
    _BisyncPuStatsLineIndex_Type()
)
bisyncPuStatsLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncPuStatsLineIndex.setStatus("mandatory")


class _BisyncPuStatsAddress_Type(OctetString):
    """Custom type bisyncPuStatsAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_BisyncPuStatsAddress_Type.__name__ = "OctetString"
_BisyncPuStatsAddress_Object = MibTableColumn
bisyncPuStatsAddress = _BisyncPuStatsAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 3, 2, 1, 2),
    _BisyncPuStatsAddress_Type()
)
bisyncPuStatsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncPuStatsAddress.setStatus("mandatory")
_BisyncPuInTransactions_Type = Counter32
_BisyncPuInTransactions_Object = MibTableColumn
bisyncPuInTransactions = _BisyncPuInTransactions_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 3, 2, 1, 3),
    _BisyncPuInTransactions_Type()
)
bisyncPuInTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncPuInTransactions.setStatus("mandatory")
_BisyncPuOutTransactions_Type = Counter32
_BisyncPuOutTransactions_Object = MibTableColumn
bisyncPuOutTransactions = _BisyncPuOutTransactions_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 3, 2, 1, 4),
    _BisyncPuOutTransactions_Type()
)
bisyncPuOutTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncPuOutTransactions.setStatus("mandatory")
_BisyncPuSlowPolls_Type = Counter32
_BisyncPuSlowPolls_Object = MibTableColumn
bisyncPuSlowPolls = _BisyncPuSlowPolls_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 3, 2, 1, 5),
    _BisyncPuSlowPolls_Type()
)
bisyncPuSlowPolls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncPuSlowPolls.setStatus("mandatory")
_BisyncPuPolls_Type = Counter32
_BisyncPuPolls_Object = MibTableColumn
bisyncPuPolls = _BisyncPuPolls_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 3, 2, 1, 6),
    _BisyncPuPolls_Type()
)
bisyncPuPolls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncPuPolls.setStatus("mandatory")
_PuMappingGroup_ObjectIdentity = ObjectIdentity
puMappingGroup = _PuMappingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 4)
)
_MappingPuConfigTable_Object = MibTable
mappingPuConfigTable = _MappingPuConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 4, 1)
)
if mibBuilder.loadTexts:
    mappingPuConfigTable.setStatus("mandatory")
_MappingPuConfigEntry_Object = MibTableRow
mappingPuConfigEntry = _MappingPuConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 4, 1, 1)
)
mappingPuConfigEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "mappingPuConfigLineIndex"),
    (0, "SYNC-RESEARCH-MIB", "mappingPuConfigAddress"),
)
if mibBuilder.loadTexts:
    mappingPuConfigEntry.setStatus("mandatory")
_MappingPuConfigLineIndex_Type = Integer32
_MappingPuConfigLineIndex_Object = MibTableColumn
mappingPuConfigLineIndex = _MappingPuConfigLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 4, 1, 1, 1),
    _MappingPuConfigLineIndex_Type()
)
mappingPuConfigLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mappingPuConfigLineIndex.setStatus("mandatory")


class _MappingPuConfigAddress_Type(OctetString):
    """Custom type mappingPuConfigAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MappingPuConfigAddress_Type.__name__ = "OctetString"
_MappingPuConfigAddress_Object = MibTableColumn
mappingPuConfigAddress = _MappingPuConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 4, 1, 1, 2),
    _MappingPuConfigAddress_Type()
)
mappingPuConfigAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mappingPuConfigAddress.setStatus("mandatory")


class _MappingPuSourceSAP_Type(OctetString):
    """Custom type mappingPuSourceSAP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MappingPuSourceSAP_Type.__name__ = "OctetString"
_MappingPuSourceSAP_Object = MibTableColumn
mappingPuSourceSAP = _MappingPuSourceSAP_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 4, 1, 1, 3),
    _MappingPuSourceSAP_Type()
)
mappingPuSourceSAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mappingPuSourceSAP.setStatus("mandatory")


class _MappingPuDestinationSAP_Type(OctetString):
    """Custom type mappingPuDestinationSAP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MappingPuDestinationSAP_Type.__name__ = "OctetString"
_MappingPuDestinationSAP_Object = MibTableColumn
mappingPuDestinationSAP = _MappingPuDestinationSAP_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 4, 1, 1, 4),
    _MappingPuDestinationSAP_Type()
)
mappingPuDestinationSAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mappingPuDestinationSAP.setStatus("mandatory")
_MappingPuDestinationMAC_Type = PhysAddress
_MappingPuDestinationMAC_Object = MibTableColumn
mappingPuDestinationMAC = _MappingPuDestinationMAC_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 4, 1, 1, 5),
    _MappingPuDestinationMAC_Type()
)
mappingPuDestinationMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mappingPuDestinationMAC.setStatus("mandatory")
_MappingPuPartnerConfigLineIndex_Type = Integer32
_MappingPuPartnerConfigLineIndex_Object = MibTableColumn
mappingPuPartnerConfigLineIndex = _MappingPuPartnerConfigLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 4, 1, 1, 6),
    _MappingPuPartnerConfigLineIndex_Type()
)
mappingPuPartnerConfigLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mappingPuPartnerConfigLineIndex.setStatus("mandatory")


class _MappingPuPartnerConfigAddress_Type(OctetString):
    """Custom type mappingPuPartnerConfigAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MappingPuPartnerConfigAddress_Type.__name__ = "OctetString"
_MappingPuPartnerConfigAddress_Object = MibTableColumn
mappingPuPartnerConfigAddress = _MappingPuPartnerConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 4, 1, 1, 7),
    _MappingPuPartnerConfigAddress_Type()
)
mappingPuPartnerConfigAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mappingPuPartnerConfigAddress.setStatus("mandatory")


class _MappingPuPartnerSourceSAP_Type(OctetString):
    """Custom type mappingPuPartnerSourceSAP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MappingPuPartnerSourceSAP_Type.__name__ = "OctetString"
_MappingPuPartnerSourceSAP_Object = MibTableColumn
mappingPuPartnerSourceSAP = _MappingPuPartnerSourceSAP_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 4, 1, 1, 8),
    _MappingPuPartnerSourceSAP_Type()
)
mappingPuPartnerSourceSAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mappingPuPartnerSourceSAP.setStatus("mandatory")


class _MappingPuPartnerDestSAP_Type(OctetString):
    """Custom type mappingPuPartnerDestSAP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MappingPuPartnerDestSAP_Type.__name__ = "OctetString"
_MappingPuPartnerDestSAP_Object = MibTableColumn
mappingPuPartnerDestSAP = _MappingPuPartnerDestSAP_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 4, 1, 1, 9),
    _MappingPuPartnerDestSAP_Type()
)
mappingPuPartnerDestSAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mappingPuPartnerDestSAP.setStatus("mandatory")
_MappingPuPartnerDestMAC_Type = PhysAddress
_MappingPuPartnerDestMAC_Object = MibTableColumn
mappingPuPartnerDestMAC = _MappingPuPartnerDestMAC_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 4, 1, 1, 10),
    _MappingPuPartnerDestMAC_Type()
)
mappingPuPartnerDestMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mappingPuPartnerDestMAC.setStatus("mandatory")


class _MappingPuNAU_Type(DisplayString):
    """Custom type mappingPuNAU based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_MappingPuNAU_Type.__name__ = "DisplayString"
_MappingPuNAU_Object = MibTableColumn
mappingPuNAU = _MappingPuNAU_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 4, 1, 1, 11),
    _MappingPuNAU_Type()
)
mappingPuNAU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mappingPuNAU.setStatus("mandatory")


class _MappingPuConnectID_Type(OctetString):
    """Custom type mappingPuConnectID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MappingPuConnectID_Type.__name__ = "OctetString"
_MappingPuConnectID_Object = MibTableColumn
mappingPuConnectID = _MappingPuConnectID_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 4, 1, 1, 12),
    _MappingPuConnectID_Type()
)
mappingPuConnectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mappingPuConnectID.setStatus("mandatory")


class _MappingPuXID_Type(OctetString):
    """Custom type mappingPuXID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_MappingPuXID_Type.__name__ = "OctetString"
_MappingPuXID_Object = MibTableColumn
mappingPuXID = _MappingPuXID_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 4, 1, 1, 13),
    _MappingPuXID_Type()
)
mappingPuXID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mappingPuXID.setStatus("mandatory")


class _MappingPuDirectDLCI_Type(OctetString):
    """Custom type mappingPuDirectDLCI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_MappingPuDirectDLCI_Type.__name__ = "OctetString"
_MappingPuDirectDLCI_Object = MibTableColumn
mappingPuDirectDLCI = _MappingPuDirectDLCI_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 4, 1, 1, 14),
    _MappingPuDirectDLCI_Type()
)
mappingPuDirectDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mappingPuDirectDLCI.setStatus("mandatory")


class _MappingPuLastClearCode_Type(OctetString):
    """Custom type mappingPuLastClearCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MappingPuLastClearCode_Type.__name__ = "OctetString"
_MappingPuLastClearCode_Object = MibTableColumn
mappingPuLastClearCode = _MappingPuLastClearCode_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 4, 1, 1, 15),
    _MappingPuLastClearCode_Type()
)
mappingPuLastClearCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mappingPuLastClearCode.setStatus("mandatory")
_MappingPuConnAttemptCnt_Type = Counter32
_MappingPuConnAttemptCnt_Object = MibTableColumn
mappingPuConnAttemptCnt = _MappingPuConnAttemptCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 4, 1, 1, 16),
    _MappingPuConnAttemptCnt_Type()
)
mappingPuConnAttemptCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mappingPuConnAttemptCnt.setStatus("mandatory")


class _MappingPuPartnerLastClearCode_Type(OctetString):
    """Custom type mappingPuPartnerLastClearCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MappingPuPartnerLastClearCode_Type.__name__ = "OctetString"
_MappingPuPartnerLastClearCode_Object = MibTableColumn
mappingPuPartnerLastClearCode = _MappingPuPartnerLastClearCode_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 4, 1, 1, 17),
    _MappingPuPartnerLastClearCode_Type()
)
mappingPuPartnerLastClearCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mappingPuPartnerLastClearCode.setStatus("mandatory")
_MappingPuPartnerConnAttemptCnt_Type = Counter32
_MappingPuPartnerConnAttemptCnt_Object = MibTableColumn
mappingPuPartnerConnAttemptCnt = _MappingPuPartnerConnAttemptCnt_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 4, 1, 1, 18),
    _MappingPuPartnerConnAttemptCnt_Type()
)
mappingPuPartnerConnAttemptCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mappingPuPartnerConnAttemptCnt.setStatus("mandatory")
_PuAsyncGroup_ObjectIdentity = ObjectIdentity
puAsyncGroup = _PuAsyncGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 5)
)
_AsyncPuConfigTable_Object = MibTable
asyncPuConfigTable = _AsyncPuConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 5, 1)
)
if mibBuilder.loadTexts:
    asyncPuConfigTable.setStatus("mandatory")
_AsyncPuConfigEntry_Object = MibTableRow
asyncPuConfigEntry = _AsyncPuConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 5, 1, 1)
)
asyncPuConfigEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "asyncPuConfigLineIndex"),
    (0, "SYNC-RESEARCH-MIB", "asyncPuConfigAddress"),
)
if mibBuilder.loadTexts:
    asyncPuConfigEntry.setStatus("mandatory")
_AsyncPuConfigLineIndex_Type = Integer32
_AsyncPuConfigLineIndex_Object = MibTableColumn
asyncPuConfigLineIndex = _AsyncPuConfigLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 5, 1, 1, 1),
    _AsyncPuConfigLineIndex_Type()
)
asyncPuConfigLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncPuConfigLineIndex.setStatus("mandatory")


class _AsyncPuConfigAddress_Type(OctetString):
    """Custom type asyncPuConfigAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AsyncPuConfigAddress_Type.__name__ = "OctetString"
_AsyncPuConfigAddress_Object = MibTableColumn
asyncPuConfigAddress = _AsyncPuConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 5, 1, 1, 2),
    _AsyncPuConfigAddress_Type()
)
asyncPuConfigAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncPuConfigAddress.setStatus("mandatory")


class _AsyncPuNAUName_Type(DisplayString):
    """Custom type asyncPuNAUName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AsyncPuNAUName_Type.__name__ = "DisplayString"
_AsyncPuNAUName_Object = MibTableColumn
asyncPuNAUName = _AsyncPuNAUName_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 5, 1, 1, 3),
    _AsyncPuNAUName_Type()
)
asyncPuNAUName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncPuNAUName.setStatus("mandatory")


class _AsyncPuInitialState_Type(Integer32):
    """Custom type asyncPuInitialState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in-service", 1),
          ("out-of-service", 2))
    )


_AsyncPuInitialState_Type.__name__ = "Integer32"
_AsyncPuInitialState_Object = MibTableColumn
asyncPuInitialState = _AsyncPuInitialState_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 5, 1, 1, 4),
    _AsyncPuInitialState_Type()
)
asyncPuInitialState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncPuInitialState.setStatus("mandatory")


class _AsyncPuXID_Type(OctetString):
    """Custom type asyncPuXID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_AsyncPuXID_Type.__name__ = "OctetString"
_AsyncPuXID_Object = MibTableColumn
asyncPuXID = _AsyncPuXID_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 5, 1, 1, 5),
    _AsyncPuXID_Type()
)
asyncPuXID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncPuXID.setStatus("mandatory")


class _AsyncPuConnectionID_Type(OctetString):
    """Custom type asyncPuConnectionID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AsyncPuConnectionID_Type.__name__ = "OctetString"
_AsyncPuConnectionID_Object = MibTableColumn
asyncPuConnectionID = _AsyncPuConnectionID_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 5, 1, 1, 6),
    _AsyncPuConnectionID_Type()
)
asyncPuConnectionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncPuConnectionID.setStatus("mandatory")


class _AsyncPuConnectType_Type(Integer32):
    """Custom type asyncPuConnectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("answer", 1),
          ("originate", 2))
    )


_AsyncPuConnectType_Type.__name__ = "Integer32"
_AsyncPuConnectType_Object = MibTableColumn
asyncPuConnectType = _AsyncPuConnectType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 5, 1, 1, 7),
    _AsyncPuConnectType_Type()
)
asyncPuConnectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncPuConnectType.setStatus("mandatory")


class _AsyncPuDeviceRangeLow_Type(OctetString):
    """Custom type asyncPuDeviceRangeLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AsyncPuDeviceRangeLow_Type.__name__ = "OctetString"
_AsyncPuDeviceRangeLow_Object = MibTableColumn
asyncPuDeviceRangeLow = _AsyncPuDeviceRangeLow_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 5, 1, 1, 8),
    _AsyncPuDeviceRangeLow_Type()
)
asyncPuDeviceRangeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncPuDeviceRangeLow.setStatus("mandatory")


class _AsyncPuDeviceRangeHigh_Type(OctetString):
    """Custom type asyncPuDeviceRangeHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AsyncPuDeviceRangeHigh_Type.__name__ = "OctetString"
_AsyncPuDeviceRangeHigh_Object = MibTableColumn
asyncPuDeviceRangeHigh = _AsyncPuDeviceRangeHigh_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 5, 1, 1, 9),
    _AsyncPuDeviceRangeHigh_Type()
)
asyncPuDeviceRangeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncPuDeviceRangeHigh.setStatus("mandatory")
_AsyncPuStatsTable_Object = MibTable
asyncPuStatsTable = _AsyncPuStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 5, 2)
)
if mibBuilder.loadTexts:
    asyncPuStatsTable.setStatus("mandatory")
_AsyncPuStatsEntry_Object = MibTableRow
asyncPuStatsEntry = _AsyncPuStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 5, 2, 1)
)
asyncPuStatsEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "asyncPuStatsLineIndex"),
    (0, "SYNC-RESEARCH-MIB", "asyncPuStatsAddress"),
)
if mibBuilder.loadTexts:
    asyncPuStatsEntry.setStatus("mandatory")
_AsyncPuStatsLineIndex_Type = Integer32
_AsyncPuStatsLineIndex_Object = MibTableColumn
asyncPuStatsLineIndex = _AsyncPuStatsLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 5, 2, 1, 1),
    _AsyncPuStatsLineIndex_Type()
)
asyncPuStatsLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncPuStatsLineIndex.setStatus("mandatory")


class _AsyncPuStatsAddress_Type(OctetString):
    """Custom type asyncPuStatsAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AsyncPuStatsAddress_Type.__name__ = "OctetString"
_AsyncPuStatsAddress_Object = MibTableColumn
asyncPuStatsAddress = _AsyncPuStatsAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 5, 2, 1, 2),
    _AsyncPuStatsAddress_Type()
)
asyncPuStatsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncPuStatsAddress.setStatus("mandatory")
_AsyncPuInChars_Type = Counter32
_AsyncPuInChars_Object = MibTableColumn
asyncPuInChars = _AsyncPuInChars_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 5, 2, 1, 3),
    _AsyncPuInChars_Type()
)
asyncPuInChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncPuInChars.setStatus("mandatory")
_AsyncPuOutChars_Type = Counter32
_AsyncPuOutChars_Object = MibTableColumn
asyncPuOutChars = _AsyncPuOutChars_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 5, 2, 1, 4),
    _AsyncPuOutChars_Type()
)
asyncPuOutChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncPuOutChars.setStatus("mandatory")
_AsyncPuInMessages_Type = Counter32
_AsyncPuInMessages_Object = MibTableColumn
asyncPuInMessages = _AsyncPuInMessages_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 5, 2, 1, 5),
    _AsyncPuInMessages_Type()
)
asyncPuInMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncPuInMessages.setStatus("mandatory")
_AsyncPuOutMessages_Type = Counter32
_AsyncPuOutMessages_Object = MibTableColumn
asyncPuOutMessages = _AsyncPuOutMessages_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 5, 2, 1, 6),
    _AsyncPuOutMessages_Type()
)
asyncPuOutMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncPuOutMessages.setStatus("mandatory")
_PuLanGroup_ObjectIdentity = ObjectIdentity
puLanGroup = _PuLanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 6)
)
_LanPuConfigTable_Object = MibTable
lanPuConfigTable = _LanPuConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 6, 1)
)
if mibBuilder.loadTexts:
    lanPuConfigTable.setStatus("mandatory")
_LanPuConfigEntry_Object = MibTableRow
lanPuConfigEntry = _LanPuConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 6, 1, 1)
)
lanPuConfigEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "lanPuConfigLineIndex"),
    (0, "SYNC-RESEARCH-MIB", "lanPuConfigAddress"),
)
if mibBuilder.loadTexts:
    lanPuConfigEntry.setStatus("mandatory")
_LanPuConfigLineIndex_Type = Integer32
_LanPuConfigLineIndex_Object = MibTableColumn
lanPuConfigLineIndex = _LanPuConfigLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 6, 1, 1, 1),
    _LanPuConfigLineIndex_Type()
)
lanPuConfigLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanPuConfigLineIndex.setStatus("mandatory")


class _LanPuConfigAddress_Type(OctetString):
    """Custom type lanPuConfigAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LanPuConfigAddress_Type.__name__ = "OctetString"
_LanPuConfigAddress_Object = MibTableColumn
lanPuConfigAddress = _LanPuConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 6, 1, 1, 2),
    _LanPuConfigAddress_Type()
)
lanPuConfigAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanPuConfigAddress.setStatus("mandatory")


class _LanPuNAUName_Type(DisplayString):
    """Custom type lanPuNAUName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_LanPuNAUName_Type.__name__ = "DisplayString"
_LanPuNAUName_Object = MibTableColumn
lanPuNAUName = _LanPuNAUName_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 6, 1, 1, 3),
    _LanPuNAUName_Type()
)
lanPuNAUName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanPuNAUName.setStatus("mandatory")


class _LanPuXID_Type(OctetString):
    """Custom type lanPuXID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_LanPuXID_Type.__name__ = "OctetString"
_LanPuXID_Object = MibTableColumn
lanPuXID = _LanPuXID_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 6, 1, 1, 4),
    _LanPuXID_Type()
)
lanPuXID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanPuXID.setStatus("mandatory")


class _LanPuConnectionID_Type(OctetString):
    """Custom type lanPuConnectionID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_LanPuConnectionID_Type.__name__ = "OctetString"
_LanPuConnectionID_Object = MibTableColumn
lanPuConnectionID = _LanPuConnectionID_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 6, 1, 1, 5),
    _LanPuConnectionID_Type()
)
lanPuConnectionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanPuConnectionID.setStatus("mandatory")


class _LanPuSourceSAP_Type(OctetString):
    """Custom type lanPuSourceSAP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LanPuSourceSAP_Type.__name__ = "OctetString"
_LanPuSourceSAP_Object = MibTableColumn
lanPuSourceSAP = _LanPuSourceSAP_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 6, 1, 1, 6),
    _LanPuSourceSAP_Type()
)
lanPuSourceSAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanPuSourceSAP.setStatus("mandatory")


class _LanPuDestinationSAP_Type(OctetString):
    """Custom type lanPuDestinationSAP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LanPuDestinationSAP_Type.__name__ = "OctetString"
_LanPuDestinationSAP_Object = MibTableColumn
lanPuDestinationSAP = _LanPuDestinationSAP_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 6, 1, 1, 7),
    _LanPuDestinationSAP_Type()
)
lanPuDestinationSAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanPuDestinationSAP.setStatus("mandatory")
_LanPuMAC_Type = PhysAddress
_LanPuMAC_Object = MibTableColumn
lanPuMAC = _LanPuMAC_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 6, 1, 1, 8),
    _LanPuMAC_Type()
)
lanPuMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanPuMAC.setStatus("mandatory")
_LanPuAlternateMACAddress_Type = PhysAddress
_LanPuAlternateMACAddress_Object = MibTableColumn
lanPuAlternateMACAddress = _LanPuAlternateMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 6, 1, 1, 9),
    _LanPuAlternateMACAddress_Type()
)
lanPuAlternateMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanPuAlternateMACAddress.setStatus("mandatory")
_PuRemoteGroup_ObjectIdentity = ObjectIdentity
puRemoteGroup = _PuRemoteGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 7)
)
_RemotePuConfigTable_Object = MibTable
remotePuConfigTable = _RemotePuConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 7, 1)
)
if mibBuilder.loadTexts:
    remotePuConfigTable.setStatus("mandatory")
_RemotePuConfigEntry_Object = MibTableRow
remotePuConfigEntry = _RemotePuConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 7, 1, 1)
)
remotePuConfigEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "accessPuConfigLineIndex"),
    (0, "SYNC-RESEARCH-MIB", "accessPuConfigAddress"),
)
if mibBuilder.loadTexts:
    remotePuConfigEntry.setStatus("mandatory")
_AccessPuConfigLineIndex_Type = Integer32
_AccessPuConfigLineIndex_Object = MibTableColumn
accessPuConfigLineIndex = _AccessPuConfigLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 7, 1, 1, 1),
    _AccessPuConfigLineIndex_Type()
)
accessPuConfigLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessPuConfigLineIndex.setStatus("mandatory")


class _AccessPuConfigAddress_Type(OctetString):
    """Custom type accessPuConfigAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AccessPuConfigAddress_Type.__name__ = "OctetString"
_AccessPuConfigAddress_Object = MibTableColumn
accessPuConfigAddress = _AccessPuConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 7, 1, 1, 2),
    _AccessPuConfigAddress_Type()
)
accessPuConfigAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessPuConfigAddress.setStatus("mandatory")
_RemotePuConfigLineIndex_Type = Integer32
_RemotePuConfigLineIndex_Object = MibTableColumn
remotePuConfigLineIndex = _RemotePuConfigLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 7, 1, 1, 3),
    _RemotePuConfigLineIndex_Type()
)
remotePuConfigLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePuConfigLineIndex.setStatus("mandatory")


class _RemotePuConfigAddress_Type(OctetString):
    """Custom type remotePuConfigAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_RemotePuConfigAddress_Type.__name__ = "OctetString"
_RemotePuConfigAddress_Object = MibTableColumn
remotePuConfigAddress = _RemotePuConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 7, 1, 1, 4),
    _RemotePuConfigAddress_Type()
)
remotePuConfigAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePuConfigAddress.setStatus("mandatory")


class _RemotePuSourceSAP_Type(OctetString):
    """Custom type remotePuSourceSAP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_RemotePuSourceSAP_Type.__name__ = "OctetString"
_RemotePuSourceSAP_Object = MibTableColumn
remotePuSourceSAP = _RemotePuSourceSAP_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 7, 1, 1, 5),
    _RemotePuSourceSAP_Type()
)
remotePuSourceSAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePuSourceSAP.setStatus("mandatory")


class _RemotePuDestinationSAP_Type(OctetString):
    """Custom type remotePuDestinationSAP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_RemotePuDestinationSAP_Type.__name__ = "OctetString"
_RemotePuDestinationSAP_Object = MibTableColumn
remotePuDestinationSAP = _RemotePuDestinationSAP_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 7, 1, 1, 6),
    _RemotePuDestinationSAP_Type()
)
remotePuDestinationSAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePuDestinationSAP.setStatus("mandatory")
_RemotePuMAC_Type = PhysAddress
_RemotePuMAC_Object = MibTableColumn
remotePuMAC = _RemotePuMAC_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 7, 1, 1, 7),
    _RemotePuMAC_Type()
)
remotePuMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePuMAC.setStatus("mandatory")


class _RemotePuPrimaryDLCI_Type(Integer32):
    """Custom type remotePuPrimaryDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_RemotePuPrimaryDLCI_Type.__name__ = "Integer32"
_RemotePuPrimaryDLCI_Object = MibTableColumn
remotePuPrimaryDLCI = _RemotePuPrimaryDLCI_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 7, 1, 1, 8),
    _RemotePuPrimaryDLCI_Type()
)
remotePuPrimaryDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePuPrimaryDLCI.setStatus("mandatory")


class _RemotePuParallelDLCI_Type(Integer32):
    """Custom type remotePuParallelDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_RemotePuParallelDLCI_Type.__name__ = "Integer32"
_RemotePuParallelDLCI_Object = MibTableColumn
remotePuParallelDLCI = _RemotePuParallelDLCI_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 7, 1, 1, 9),
    _RemotePuParallelDLCI_Type()
)
remotePuParallelDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePuParallelDLCI.setStatus("mandatory")


class _RemotePuAlternateDLCI_Type(Integer32):
    """Custom type remotePuAlternateDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_RemotePuAlternateDLCI_Type.__name__ = "Integer32"
_RemotePuAlternateDLCI_Object = MibTableColumn
remotePuAlternateDLCI = _RemotePuAlternateDLCI_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 7, 1, 1, 10),
    _RemotePuAlternateDLCI_Type()
)
remotePuAlternateDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePuAlternateDLCI.setStatus("mandatory")
_RemotePuAlternateMACAddress_Type = PhysAddress
_RemotePuAlternateMACAddress_Object = MibTableColumn
remotePuAlternateMACAddress = _RemotePuAlternateMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 7, 1, 1, 11),
    _RemotePuAlternateMACAddress_Type()
)
remotePuAlternateMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePuAlternateMACAddress.setStatus("mandatory")
_RemotePuTransmitPriority_Type = Integer32
_RemotePuTransmitPriority_Object = MibTableColumn
remotePuTransmitPriority = _RemotePuTransmitPriority_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 7, 1, 1, 12),
    _RemotePuTransmitPriority_Type()
)
remotePuTransmitPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePuTransmitPriority.setStatus("mandatory")


class _RemotePuBroadcastAllDLCI_Type(Integer32):
    """Custom type remotePuBroadcastAllDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_RemotePuBroadcastAllDLCI_Type.__name__ = "Integer32"
_RemotePuBroadcastAllDLCI_Object = MibTableColumn
remotePuBroadcastAllDLCI = _RemotePuBroadcastAllDLCI_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 7, 1, 1, 13),
    _RemotePuBroadcastAllDLCI_Type()
)
remotePuBroadcastAllDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePuBroadcastAllDLCI.setStatus("mandatory")
_RemotePuLocalDTE_Type = OctetString
_RemotePuLocalDTE_Object = MibTableColumn
remotePuLocalDTE = _RemotePuLocalDTE_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 7, 1, 1, 14),
    _RemotePuLocalDTE_Type()
)
remotePuLocalDTE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePuLocalDTE.setStatus("mandatory")
_RemotePuRemoteDTE_Type = OctetString
_RemotePuRemoteDTE_Object = MibTableColumn
remotePuRemoteDTE = _RemotePuRemoteDTE_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 7, 1, 1, 15),
    _RemotePuRemoteDTE_Type()
)
remotePuRemoteDTE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePuRemoteDTE.setStatus("mandatory")
_PuX25Group_ObjectIdentity = ObjectIdentity
puX25Group = _PuX25Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 8)
)
_X25PuConfigTable_Object = MibTable
x25PuConfigTable = _X25PuConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 8, 1)
)
if mibBuilder.loadTexts:
    x25PuConfigTable.setStatus("mandatory")
_X25PuConfigEntry_Object = MibTableRow
x25PuConfigEntry = _X25PuConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 8, 1, 1)
)
x25PuConfigEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "x25PuConfigLineIndex"),
    (0, "SYNC-RESEARCH-MIB", "x25PuConfigAddress"),
)
if mibBuilder.loadTexts:
    x25PuConfigEntry.setStatus("mandatory")
_X25PuConfigLineIndex_Type = Integer32
_X25PuConfigLineIndex_Object = MibTableColumn
x25PuConfigLineIndex = _X25PuConfigLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 8, 1, 1, 1),
    _X25PuConfigLineIndex_Type()
)
x25PuConfigLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25PuConfigLineIndex.setStatus("mandatory")


class _X25PuConfigAddress_Type(OctetString):
    """Custom type x25PuConfigAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_X25PuConfigAddress_Type.__name__ = "OctetString"
_X25PuConfigAddress_Object = MibTableColumn
x25PuConfigAddress = _X25PuConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 8, 1, 1, 2),
    _X25PuConfigAddress_Type()
)
x25PuConfigAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25PuConfigAddress.setStatus("mandatory")


class _X25PuNAUName_Type(DisplayString):
    """Custom type x25PuNAUName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_X25PuNAUName_Type.__name__ = "DisplayString"
_X25PuNAUName_Object = MibTableColumn
x25PuNAUName = _X25PuNAUName_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 8, 1, 1, 3),
    _X25PuNAUName_Type()
)
x25PuNAUName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25PuNAUName.setStatus("mandatory")


class _X25PuConnectionID_Type(OctetString):
    """Custom type x25PuConnectionID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_X25PuConnectionID_Type.__name__ = "OctetString"
_X25PuConnectionID_Object = MibTableColumn
x25PuConnectionID = _X25PuConnectionID_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 8, 1, 1, 4),
    _X25PuConnectionID_Type()
)
x25PuConnectionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25PuConnectionID.setStatus("mandatory")


class _X25PuXID_Type(OctetString):
    """Custom type x25PuXID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_X25PuXID_Type.__name__ = "OctetString"
_X25PuXID_Object = MibTableColumn
x25PuXID = _X25PuXID_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 8, 1, 1, 5),
    _X25PuXID_Type()
)
x25PuXID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25PuXID.setStatus("mandatory")


class _X25PuSolicitXID_Type(Integer32):
    """Custom type x25PuSolicitXID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_X25PuSolicitXID_Type.__name__ = "Integer32"
_X25PuSolicitXID_Object = MibTableColumn
x25PuSolicitXID = _X25PuSolicitXID_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 8, 1, 1, 6),
    _X25PuSolicitXID_Type()
)
x25PuSolicitXID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25PuSolicitXID.setStatus("mandatory")
_X25PuSourceAddress_Type = OctetString
_X25PuSourceAddress_Object = MibTableColumn
x25PuSourceAddress = _X25PuSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 8, 1, 1, 7),
    _X25PuSourceAddress_Type()
)
x25PuSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25PuSourceAddress.setStatus("mandatory")
_X25PuRemoteDTEAddress_Type = OctetString
_X25PuRemoteDTEAddress_Object = MibTableColumn
x25PuRemoteDTEAddress = _X25PuRemoteDTEAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 8, 1, 1, 8),
    _X25PuRemoteDTEAddress_Type()
)
x25PuRemoteDTEAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25PuRemoteDTEAddress.setStatus("mandatory")
_PuAlcGroup_ObjectIdentity = ObjectIdentity
puAlcGroup = _PuAlcGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 9)
)
_AlcPuConfigTable_Object = MibTable
alcPuConfigTable = _AlcPuConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 9, 1)
)
if mibBuilder.loadTexts:
    alcPuConfigTable.setStatus("mandatory")
_AlcPuConfigEntry_Object = MibTableRow
alcPuConfigEntry = _AlcPuConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 9, 1, 1)
)
alcPuConfigEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "alcPuConfigAddress"),
)
if mibBuilder.loadTexts:
    alcPuConfigEntry.setStatus("mandatory")
_AlcPuConfigLineIndex_Type = Integer32
_AlcPuConfigLineIndex_Object = MibTableColumn
alcPuConfigLineIndex = _AlcPuConfigLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 9, 1, 1, 1),
    _AlcPuConfigLineIndex_Type()
)
alcPuConfigLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPuConfigLineIndex.setStatus("mandatory")


class _AlcPuConfigAddress_Type(OctetString):
    """Custom type alcPuConfigAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AlcPuConfigAddress_Type.__name__ = "OctetString"
_AlcPuConfigAddress_Object = MibTableColumn
alcPuConfigAddress = _AlcPuConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 9, 1, 1, 2),
    _AlcPuConfigAddress_Type()
)
alcPuConfigAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPuConfigAddress.setStatus("mandatory")


class _AlcPuNAUName_Type(DisplayString):
    """Custom type alcPuNAUName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AlcPuNAUName_Type.__name__ = "DisplayString"
_AlcPuNAUName_Object = MibTableColumn
alcPuNAUName = _AlcPuNAUName_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 9, 1, 1, 3),
    _AlcPuNAUName_Type()
)
alcPuNAUName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPuNAUName.setStatus("mandatory")


class _AlcPuCSS_Type(Integer32):
    """Custom type alcPuCSS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in-service", 1),
          ("out-of-service", 2))
    )


_AlcPuCSS_Type.__name__ = "Integer32"
_AlcPuCSS_Object = MibTableColumn
alcPuCSS = _AlcPuCSS_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 9, 1, 1, 4),
    _AlcPuCSS_Type()
)
alcPuCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPuCSS.setStatus("mandatory")


class _AlcPuConnectionID_Type(OctetString):
    """Custom type alcPuConnectionID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AlcPuConnectionID_Type.__name__ = "OctetString"
_AlcPuConnectionID_Object = MibTableColumn
alcPuConnectionID = _AlcPuConnectionID_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 9, 1, 1, 5),
    _AlcPuConnectionID_Type()
)
alcPuConnectionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPuConnectionID.setStatus("mandatory")


class _AlcPuXID_Type(OctetString):
    """Custom type alcPuXID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_AlcPuXID_Type.__name__ = "OctetString"
_AlcPuXID_Object = MibTableColumn
alcPuXID = _AlcPuXID_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 9, 1, 1, 6),
    _AlcPuXID_Type()
)
alcPuXID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPuXID.setStatus("mandatory")


class _AlcPuConnectType_Type(Integer32):
    """Custom type alcPuConnectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("answer", 1),
          ("originate", 2))
    )


_AlcPuConnectType_Type.__name__ = "Integer32"
_AlcPuConnectType_Object = MibTableColumn
alcPuConnectType = _AlcPuConnectType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 9, 1, 1, 7),
    _AlcPuConnectType_Type()
)
alcPuConnectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPuConnectType.setStatus("mandatory")


class _AlcPuLineNumber_Type(OctetString):
    """Custom type alcPuLineNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AlcPuLineNumber_Type.__name__ = "OctetString"
_AlcPuLineNumber_Object = MibTableColumn
alcPuLineNumber = _AlcPuLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 9, 1, 1, 8),
    _AlcPuLineNumber_Type()
)
alcPuLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPuLineNumber.setStatus("mandatory")


class _AlcPuMaximumFastPoll_Type(Integer32):
    """Custom type alcPuMaximumFastPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_AlcPuMaximumFastPoll_Type.__name__ = "Integer32"
_AlcPuMaximumFastPoll_Object = MibTableColumn
alcPuMaximumFastPoll = _AlcPuMaximumFastPoll_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 9, 1, 1, 9),
    _AlcPuMaximumFastPoll_Type()
)
alcPuMaximumFastPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPuMaximumFastPoll.setStatus("mandatory")


class _AlcPuMinimumFastPoll_Type(Integer32):
    """Custom type alcPuMinimumFastPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65500),
    )


_AlcPuMinimumFastPoll_Type.__name__ = "Integer32"
_AlcPuMinimumFastPoll_Object = MibTableColumn
alcPuMinimumFastPoll = _AlcPuMinimumFastPoll_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 9, 1, 1, 10),
    _AlcPuMinimumFastPoll_Type()
)
alcPuMinimumFastPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPuMinimumFastPoll.setStatus("mandatory")


class _AlcPuMaximumSlowPollInterval_Type(Integer32):
    """Custom type alcPuMaximumSlowPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_AlcPuMaximumSlowPollInterval_Type.__name__ = "Integer32"
_AlcPuMaximumSlowPollInterval_Object = MibTableColumn
alcPuMaximumSlowPollInterval = _AlcPuMaximumSlowPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 9, 1, 1, 11),
    _AlcPuMaximumSlowPollInterval_Type()
)
alcPuMaximumSlowPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPuMaximumSlowPollInterval.setStatus("mandatory")


class _AlcPuMinimumSlowPollInterval_Type(Integer32):
    """Custom type alcPuMinimumSlowPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 990),
    )


_AlcPuMinimumSlowPollInterval_Type.__name__ = "Integer32"
_AlcPuMinimumSlowPollInterval_Object = MibTableColumn
alcPuMinimumSlowPollInterval = _AlcPuMinimumSlowPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 9, 1, 1, 12),
    _AlcPuMinimumSlowPollInterval_Type()
)
alcPuMinimumSlowPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPuMinimumSlowPollInterval.setStatus("mandatory")


class _AlcPuResponseTimeout_Type(Integer32):
    """Custom type alcPuResponseTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_AlcPuResponseTimeout_Type.__name__ = "Integer32"
_AlcPuResponseTimeout_Object = MibTableColumn
alcPuResponseTimeout = _AlcPuResponseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 9, 1, 1, 13),
    _AlcPuResponseTimeout_Type()
)
alcPuResponseTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPuResponseTimeout.setStatus("mandatory")


class _AlcPuUserData_Type(OctetString):
    """Custom type alcPuUserData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_AlcPuUserData_Type.__name__ = "OctetString"
_AlcPuUserData_Object = MibTableColumn
alcPuUserData = _AlcPuUserData_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 9, 1, 1, 14),
    _AlcPuUserData_Type()
)
alcPuUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPuUserData.setStatus("mandatory")
_AlcSourceDTEAddress_Type = OctetString
_AlcSourceDTEAddress_Object = MibTableColumn
alcSourceDTEAddress = _AlcSourceDTEAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 9, 1, 1, 15),
    _AlcSourceDTEAddress_Type()
)
alcSourceDTEAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcSourceDTEAddress.setStatus("mandatory")
_AlcDestinationDTEAddress_Type = OctetString
_AlcDestinationDTEAddress_Object = MibTableColumn
alcDestinationDTEAddress = _AlcDestinationDTEAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 9, 1, 1, 16),
    _AlcDestinationDTEAddress_Type()
)
alcDestinationDTEAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcDestinationDTEAddress.setStatus("mandatory")
_AlcPuStatsTable_Object = MibTable
alcPuStatsTable = _AlcPuStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 9, 2)
)
if mibBuilder.loadTexts:
    alcPuStatsTable.setStatus("mandatory")
_AlcPuStatsEntry_Object = MibTableRow
alcPuStatsEntry = _AlcPuStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 9, 2, 1)
)
alcPuStatsEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "alcPuStatsLineIndex"),
    (0, "SYNC-RESEARCH-MIB", "alcPuStatsAddress"),
)
if mibBuilder.loadTexts:
    alcPuStatsEntry.setStatus("mandatory")
_AlcPuStatsLineIndex_Type = Integer32
_AlcPuStatsLineIndex_Object = MibTableColumn
alcPuStatsLineIndex = _AlcPuStatsLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 9, 2, 1, 1),
    _AlcPuStatsLineIndex_Type()
)
alcPuStatsLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPuStatsLineIndex.setStatus("mandatory")


class _AlcPuStatsAddress_Type(OctetString):
    """Custom type alcPuStatsAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AlcPuStatsAddress_Type.__name__ = "OctetString"
_AlcPuStatsAddress_Object = MibTableColumn
alcPuStatsAddress = _AlcPuStatsAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 9, 2, 1, 2),
    _AlcPuStatsAddress_Type()
)
alcPuStatsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPuStatsAddress.setStatus("mandatory")
_AlcPuPolls_Type = Counter32
_AlcPuPolls_Object = MibTableColumn
alcPuPolls = _AlcPuPolls_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 9, 2, 1, 3),
    _AlcPuPolls_Type()
)
alcPuPolls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPuPolls.setStatus("mandatory")
_AlcPuDeviceFaults_Type = Counter32
_AlcPuDeviceFaults_Object = MibTableColumn
alcPuDeviceFaults = _AlcPuDeviceFaults_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 9, 2, 1, 4),
    _AlcPuDeviceFaults_Type()
)
alcPuDeviceFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPuDeviceFaults.setStatus("mandatory")
_AlcPuBytesRcv_Type = Counter32
_AlcPuBytesRcv_Object = MibTableColumn
alcPuBytesRcv = _AlcPuBytesRcv_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 9, 2, 1, 5),
    _AlcPuBytesRcv_Type()
)
alcPuBytesRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPuBytesRcv.setStatus("mandatory")
_AlcPuBytesXmit_Type = Counter32
_AlcPuBytesXmit_Object = MibTableColumn
alcPuBytesXmit = _AlcPuBytesXmit_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 9, 2, 1, 6),
    _AlcPuBytesXmit_Type()
)
alcPuBytesXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPuBytesXmit.setStatus("mandatory")
_AlcPuSegRcv_Type = Counter32
_AlcPuSegRcv_Object = MibTableColumn
alcPuSegRcv = _AlcPuSegRcv_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 9, 2, 1, 7),
    _AlcPuSegRcv_Type()
)
alcPuSegRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPuSegRcv.setStatus("mandatory")
_AlcPuSegXmit_Type = Counter32
_AlcPuSegXmit_Object = MibTableColumn
alcPuSegXmit = _AlcPuSegXmit_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 9, 2, 1, 8),
    _AlcPuSegXmit_Type()
)
alcPuSegXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPuSegXmit.setStatus("mandatory")
_PuBisyncRjeGroup_ObjectIdentity = ObjectIdentity
puBisyncRjeGroup = _PuBisyncRjeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 10)
)
_BisyncrjePuConfigTable_Object = MibTable
bisyncrjePuConfigTable = _BisyncrjePuConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 10, 1)
)
if mibBuilder.loadTexts:
    bisyncrjePuConfigTable.setStatus("mandatory")
_BisyncrjePuConfigEntry_Object = MibTableRow
bisyncrjePuConfigEntry = _BisyncrjePuConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 10, 1, 1)
)
bisyncrjePuConfigEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "bisyncrjePuConfigLineIndex"),
    (0, "SYNC-RESEARCH-MIB", "bisyncrjePuConfigAddress"),
)
if mibBuilder.loadTexts:
    bisyncrjePuConfigEntry.setStatus("mandatory")
_BisyncrjePuConfigLineIndex_Type = Integer32
_BisyncrjePuConfigLineIndex_Object = MibTableColumn
bisyncrjePuConfigLineIndex = _BisyncrjePuConfigLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 10, 1, 1, 1),
    _BisyncrjePuConfigLineIndex_Type()
)
bisyncrjePuConfigLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjePuConfigLineIndex.setStatus("mandatory")


class _BisyncrjePuConfigAddress_Type(OctetString):
    """Custom type bisyncrjePuConfigAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_BisyncrjePuConfigAddress_Type.__name__ = "OctetString"
_BisyncrjePuConfigAddress_Object = MibTableColumn
bisyncrjePuConfigAddress = _BisyncrjePuConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 10, 1, 1, 2),
    _BisyncrjePuConfigAddress_Type()
)
bisyncrjePuConfigAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjePuConfigAddress.setStatus("mandatory")


class _BisyncrjePuNAUName_Type(DisplayString):
    """Custom type bisyncrjePuNAUName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_BisyncrjePuNAUName_Type.__name__ = "DisplayString"
_BisyncrjePuNAUName_Object = MibTableColumn
bisyncrjePuNAUName = _BisyncrjePuNAUName_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 10, 1, 1, 3),
    _BisyncrjePuNAUName_Type()
)
bisyncrjePuNAUName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjePuNAUName.setStatus("mandatory")


class _BisyncrjePuInitialState_Type(Integer32):
    """Custom type bisyncrjePuInitialState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in-service", 1),
          ("out-of-service", 2))
    )


_BisyncrjePuInitialState_Type.__name__ = "Integer32"
_BisyncrjePuInitialState_Object = MibTableColumn
bisyncrjePuInitialState = _BisyncrjePuInitialState_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 10, 1, 1, 4),
    _BisyncrjePuInitialState_Type()
)
bisyncrjePuInitialState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjePuInitialState.setStatus("mandatory")


class _BisyncrjePuConnectionID_Type(OctetString):
    """Custom type bisyncrjePuConnectionID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_BisyncrjePuConnectionID_Type.__name__ = "OctetString"
_BisyncrjePuConnectionID_Object = MibTableColumn
bisyncrjePuConnectionID = _BisyncrjePuConnectionID_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 10, 1, 1, 5),
    _BisyncrjePuConnectionID_Type()
)
bisyncrjePuConnectionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjePuConnectionID.setStatus("mandatory")


class _BisyncrjePuXID_Type(OctetString):
    """Custom type bisyncrjePuXID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_BisyncrjePuXID_Type.__name__ = "OctetString"
_BisyncrjePuXID_Object = MibTableColumn
bisyncrjePuXID = _BisyncrjePuXID_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 10, 1, 1, 6),
    _BisyncrjePuXID_Type()
)
bisyncrjePuXID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjePuXID.setStatus("mandatory")


class _BisyncrjePuConnectType_Type(Integer32):
    """Custom type bisyncrjePuConnectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("answer", 1),
          ("originate", 2))
    )


_BisyncrjePuConnectType_Type.__name__ = "Integer32"
_BisyncrjePuConnectType_Object = MibTableColumn
bisyncrjePuConnectType = _BisyncrjePuConnectType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 6, 10, 1, 1, 7),
    _BisyncrjePuConnectType_Type()
)
bisyncrjePuConnectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bisyncrjePuConnectType.setStatus("mandatory")
_NodeDeviceGroup_ObjectIdentity = ObjectIdentity
nodeDeviceGroup = _NodeDeviceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 7)
)
_DeviceControlGroup_ObjectIdentity = ObjectIdentity
deviceControlGroup = _DeviceControlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 7, 1)
)
_DeviceControlTable_Object = MibTable
deviceControlTable = _DeviceControlTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 7, 1, 1)
)
if mibBuilder.loadTexts:
    deviceControlTable.setStatus("mandatory")
_DeviceControlEntry_Object = MibTableRow
deviceControlEntry = _DeviceControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 7, 1, 1, 1)
)
deviceControlEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "deviceControlIndex"),
    (0, "SYNC-RESEARCH-MIB", "deviceControlCUIndex"),
    (0, "SYNC-RESEARCH-MIB", "deviceControlAddress"),
)
if mibBuilder.loadTexts:
    deviceControlEntry.setStatus("mandatory")
_DeviceControlIndex_Type = Integer32
_DeviceControlIndex_Object = MibTableColumn
deviceControlIndex = _DeviceControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 7, 1, 1, 1, 1),
    _DeviceControlIndex_Type()
)
deviceControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceControlIndex.setStatus("mandatory")
_DeviceControlCUIndex_Type = Integer32
_DeviceControlCUIndex_Object = MibTableColumn
deviceControlCUIndex = _DeviceControlCUIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 7, 1, 1, 1, 2),
    _DeviceControlCUIndex_Type()
)
deviceControlCUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceControlCUIndex.setStatus("mandatory")


class _DeviceControlAddress_Type(OctetString):
    """Custom type deviceControlAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DeviceControlAddress_Type.__name__ = "OctetString"
_DeviceControlAddress_Object = MibTableColumn
deviceControlAddress = _DeviceControlAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 7, 1, 1, 1, 3),
    _DeviceControlAddress_Type()
)
deviceControlAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceControlAddress.setStatus("mandatory")


class _DeviceStatus_Type(Integer32):
    """Custom type deviceStatus based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("enable-all", 5),
          ("failed", 3),
          ("restart", 4))
    )


_DeviceStatus_Type.__name__ = "Integer32"
_DeviceStatus_Object = MibTableColumn
deviceStatus = _DeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 7, 1, 1, 1, 4),
    _DeviceStatus_Type()
)
deviceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceStatus.setStatus("mandatory")


class _DeviceControlFailureCode_Type(OctetString):
    """Custom type deviceControlFailureCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_DeviceControlFailureCode_Type.__name__ = "OctetString"
_DeviceControlFailureCode_Object = MibTableColumn
deviceControlFailureCode = _DeviceControlFailureCode_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 7, 1, 1, 1, 5),
    _DeviceControlFailureCode_Type()
)
deviceControlFailureCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceControlFailureCode.setStatus("mandatory")
_DeviceBSCGroup_ObjectIdentity = ObjectIdentity
deviceBSCGroup = _DeviceBSCGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 7, 2)
)
_DeviceConfigTable_Object = MibTable
deviceConfigTable = _DeviceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 7, 2, 1)
)
if mibBuilder.loadTexts:
    deviceConfigTable.setStatus("mandatory")
_DeviceConfigEntry_Object = MibTableRow
deviceConfigEntry = _DeviceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 7, 2, 1, 1)
)
deviceConfigEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "deviceConfigLineIndex"),
    (0, "SYNC-RESEARCH-MIB", "deviceConfigCUIndex"),
    (0, "SYNC-RESEARCH-MIB", "deviceConfigAddress"),
)
if mibBuilder.loadTexts:
    deviceConfigEntry.setStatus("mandatory")
_DeviceConfigLineIndex_Type = Integer32
_DeviceConfigLineIndex_Object = MibTableColumn
deviceConfigLineIndex = _DeviceConfigLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 7, 2, 1, 1, 1),
    _DeviceConfigLineIndex_Type()
)
deviceConfigLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceConfigLineIndex.setStatus("mandatory")
_DeviceConfigCUIndex_Type = Integer32
_DeviceConfigCUIndex_Object = MibTableColumn
deviceConfigCUIndex = _DeviceConfigCUIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 7, 2, 1, 1, 2),
    _DeviceConfigCUIndex_Type()
)
deviceConfigCUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceConfigCUIndex.setStatus("mandatory")


class _DeviceConfigAddress_Type(OctetString):
    """Custom type deviceConfigAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DeviceConfigAddress_Type.__name__ = "OctetString"
_DeviceConfigAddress_Object = MibTableColumn
deviceConfigAddress = _DeviceConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 7, 2, 1, 1, 3),
    _DeviceConfigAddress_Type()
)
deviceConfigAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceConfigAddress.setStatus("mandatory")


class _DeviceConfigType_Type(Integer32):
    """Custom type deviceConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crt", 1),
          ("printer", 2))
    )


_DeviceConfigType_Type.__name__ = "Integer32"
_DeviceConfigType_Object = MibTableColumn
deviceConfigType = _DeviceConfigType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 7, 2, 1, 1, 4),
    _DeviceConfigType_Type()
)
deviceConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceConfigType.setStatus("mandatory")
_DeviceStatsTable_Object = MibTable
deviceStatsTable = _DeviceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 7, 2, 2)
)
if mibBuilder.loadTexts:
    deviceStatsTable.setStatus("mandatory")
_DeviceStatsEntry_Object = MibTableRow
deviceStatsEntry = _DeviceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 7, 2, 2, 1)
)
deviceStatsEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "bscDeviceLineIndex"),
    (0, "SYNC-RESEARCH-MIB", "bscDeviceCUIndex"),
    (0, "SYNC-RESEARCH-MIB", "bscDeviceAddress"),
)
if mibBuilder.loadTexts:
    deviceStatsEntry.setStatus("mandatory")
_BscDeviceLineIndex_Type = Integer32
_BscDeviceLineIndex_Object = MibTableColumn
bscDeviceLineIndex = _BscDeviceLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 7, 2, 2, 1, 1),
    _BscDeviceLineIndex_Type()
)
bscDeviceLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDeviceLineIndex.setStatus("mandatory")
_BscDeviceCUIndex_Type = Integer32
_BscDeviceCUIndex_Object = MibTableColumn
bscDeviceCUIndex = _BscDeviceCUIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 7, 2, 2, 1, 2),
    _BscDeviceCUIndex_Type()
)
bscDeviceCUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDeviceCUIndex.setStatus("mandatory")


class _BscDeviceAddress_Type(OctetString):
    """Custom type bscDeviceAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_BscDeviceAddress_Type.__name__ = "OctetString"
_BscDeviceAddress_Object = MibTableColumn
bscDeviceAddress = _BscDeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 7, 2, 2, 1, 3),
    _BscDeviceAddress_Type()
)
bscDeviceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDeviceAddress.setStatus("mandatory")
_BscDeviceInTransactions_Type = Counter32
_BscDeviceInTransactions_Object = MibTableColumn
bscDeviceInTransactions = _BscDeviceInTransactions_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 7, 2, 2, 1, 4),
    _BscDeviceInTransactions_Type()
)
bscDeviceInTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDeviceInTransactions.setStatus("mandatory")
_BscDeviceOutTransactions_Type = Counter32
_BscDeviceOutTransactions_Object = MibTableColumn
bscDeviceOutTransactions = _BscDeviceOutTransactions_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 7, 2, 2, 1, 5),
    _BscDeviceOutTransactions_Type()
)
bscDeviceOutTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDeviceOutTransactions.setStatus("mandatory")
_BscDeviceSumCount_Type = Counter32
_BscDeviceSumCount_Object = MibTableColumn
bscDeviceSumCount = _BscDeviceSumCount_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 7, 2, 2, 1, 6),
    _BscDeviceSumCount_Type()
)
bscDeviceSumCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDeviceSumCount.setStatus("mandatory")
_BscDeviceResponseDelaySum_Type = Counter32
_BscDeviceResponseDelaySum_Object = MibTableColumn
bscDeviceResponseDelaySum = _BscDeviceResponseDelaySum_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 7, 2, 2, 1, 7),
    _BscDeviceResponseDelaySum_Type()
)
bscDeviceResponseDelaySum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDeviceResponseDelaySum.setStatus("mandatory")
_BscDeviceResponseDelaySqSum_Type = Counter32
_BscDeviceResponseDelaySqSum_Object = MibTableColumn
bscDeviceResponseDelaySqSum = _BscDeviceResponseDelaySqSum_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 7, 2, 2, 1, 8),
    _BscDeviceResponseDelaySqSum_Type()
)
bscDeviceResponseDelaySqSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDeviceResponseDelaySqSum.setStatus("mandatory")
_DeviceALCGroup_ObjectIdentity = ObjectIdentity
deviceALCGroup = _DeviceALCGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 7, 3)
)
_AlcdeviceConfigTable_Object = MibTable
alcdeviceConfigTable = _AlcdeviceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 7, 3, 1)
)
if mibBuilder.loadTexts:
    alcdeviceConfigTable.setStatus("mandatory")
_AlcdeviceConfigEntry_Object = MibTableRow
alcdeviceConfigEntry = _AlcdeviceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 7, 3, 1, 1)
)
alcdeviceConfigEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "alcdeviceConfigLineIndex"),
    (0, "SYNC-RESEARCH-MIB", "alcdeviceConfigCUIndex"),
    (0, "SYNC-RESEARCH-MIB", "deviceConfigAddress"),
)
if mibBuilder.loadTexts:
    alcdeviceConfigEntry.setStatus("mandatory")
_AlcdeviceConfigLineIndex_Type = Integer32
_AlcdeviceConfigLineIndex_Object = MibTableColumn
alcdeviceConfigLineIndex = _AlcdeviceConfigLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 7, 3, 1, 1, 1),
    _AlcdeviceConfigLineIndex_Type()
)
alcdeviceConfigLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcdeviceConfigLineIndex.setStatus("mandatory")
_AlcdeviceConfigCUIndex_Type = Integer32
_AlcdeviceConfigCUIndex_Object = MibTableColumn
alcdeviceConfigCUIndex = _AlcdeviceConfigCUIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 7, 3, 1, 1, 2),
    _AlcdeviceConfigCUIndex_Type()
)
alcdeviceConfigCUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcdeviceConfigCUIndex.setStatus("mandatory")


class _AlcdeviceConfigAddress_Type(OctetString):
    """Custom type alcdeviceConfigAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AlcdeviceConfigAddress_Type.__name__ = "OctetString"
_AlcdeviceConfigAddress_Object = MibTableColumn
alcdeviceConfigAddress = _AlcdeviceConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 7, 3, 1, 1, 3),
    _AlcdeviceConfigAddress_Type()
)
alcdeviceConfigAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcdeviceConfigAddress.setStatus("mandatory")


class _AlcdeviceConfigType_Type(Integer32):
    """Custom type alcdeviceConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crt", 1),
          ("printer", 2))
    )


_AlcdeviceConfigType_Type.__name__ = "Integer32"
_AlcdeviceConfigType_Object = MibTableColumn
alcdeviceConfigType = _AlcdeviceConfigType_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 7, 3, 1, 1, 4),
    _AlcdeviceConfigType_Type()
)
alcdeviceConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcdeviceConfigType.setStatus("mandatory")
_NodeT7Group_ObjectIdentity = ObjectIdentity
nodeT7Group = _NodeT7Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 8)
)
_T7ConfigGroup_ObjectIdentity = ObjectIdentity
t7ConfigGroup = _T7ConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 8, 1)
)
_T7ConfigTable_Object = MibTable
t7ConfigTable = _T7ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 8, 1, 1)
)
if mibBuilder.loadTexts:
    t7ConfigTable.setStatus("mandatory")
_T7ConfigEntry_Object = MibTableRow
t7ConfigEntry = _T7ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 8, 1, 1, 1)
)
t7ConfigEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "t7ConfigIndex"),
)
if mibBuilder.loadTexts:
    t7ConfigEntry.setStatus("mandatory")
_T7ConfigIndex_Type = Integer32
_T7ConfigIndex_Object = MibTableColumn
t7ConfigIndex = _T7ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 8, 1, 1, 1, 1),
    _T7ConfigIndex_Type()
)
t7ConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t7ConfigIndex.setStatus("mandatory")


class _T7ProtocolEnabled_Type(Integer32):
    """Custom type t7ProtocolEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_T7ProtocolEnabled_Type.__name__ = "Integer32"
_T7ProtocolEnabled_Object = MibTableColumn
t7ProtocolEnabled = _T7ProtocolEnabled_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 8, 1, 1, 1, 2),
    _T7ProtocolEnabled_Type()
)
t7ProtocolEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t7ProtocolEnabled.setStatus("mandatory")


class _T7PortSpeed_Type(Integer32):
    """Custom type t7PortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(75,
              150,
              300,
              600,
              1200,
              2400,
              4800,
              9600,
              19200)
        )
    )
    namedValues = NamedValues(
        *(("speed1200", 1200),
          ("speed150", 150),
          ("speed19200", 19200),
          ("speed2400", 2400),
          ("speed300", 300),
          ("speed4800", 4800),
          ("speed600", 600),
          ("speed75", 75),
          ("speed9600", 9600))
    )


_T7PortSpeed_Type.__name__ = "Integer32"
_T7PortSpeed_Object = MibTableColumn
t7PortSpeed = _T7PortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 8, 1, 1, 1, 3),
    _T7PortSpeed_Type()
)
t7PortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t7PortSpeed.setStatus("mandatory")


class _T7StopBits_Type(Integer32):
    """Custom type t7StopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_T7StopBits_Type.__name__ = "Integer32"
_T7StopBits_Object = MibTableColumn
t7StopBits = _T7StopBits_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 8, 1, 1, 1, 4),
    _T7StopBits_Type()
)
t7StopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t7StopBits.setStatus("mandatory")


class _T7PortParity_Type(Integer32):
    """Custom type t7PortParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even", 2),
          ("none", 3),
          ("odd", 1))
    )


_T7PortParity_Type.__name__ = "Integer32"
_T7PortParity_Object = MibTableColumn
t7PortParity = _T7PortParity_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 8, 1, 1, 1, 5),
    _T7PortParity_Type()
)
t7PortParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t7PortParity.setStatus("mandatory")


class _T7DataBits_Type(Integer32):
    """Custom type t7DataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 8),
    )


_T7DataBits_Type.__name__ = "Integer32"
_T7DataBits_Object = MibTableColumn
t7DataBits = _T7DataBits_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 8, 1, 1, 1, 6),
    _T7DataBits_Type()
)
t7DataBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t7DataBits.setStatus("mandatory")


class _T7IdleTimer_Type(Integer32):
    """Custom type t7IdleTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_T7IdleTimer_Type.__name__ = "Integer32"
_T7IdleTimer_Object = MibTableColumn
t7IdleTimer = _T7IdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 8, 1, 1, 1, 7),
    _T7IdleTimer_Type()
)
t7IdleTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t7IdleTimer.setStatus("mandatory")


class _T7PortTxFrameGap_Type(Integer32):
    """Custom type t7PortTxFrameGap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_T7PortTxFrameGap_Type.__name__ = "Integer32"
_T7PortTxFrameGap_Object = MibTableColumn
t7PortTxFrameGap = _T7PortTxFrameGap_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 8, 1, 1, 1, 8),
    _T7PortTxFrameGap_Type()
)
t7PortTxFrameGap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t7PortTxFrameGap.setStatus("mandatory")


class _T7RxForwardingCount_Type(Integer32):
    """Custom type t7RxForwardingCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_T7RxForwardingCount_Type.__name__ = "Integer32"
_T7RxForwardingCount_Object = MibTableColumn
t7RxForwardingCount = _T7RxForwardingCount_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 8, 1, 1, 1, 9),
    _T7RxForwardingCount_Type()
)
t7RxForwardingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t7RxForwardingCount.setStatus("mandatory")
_T7PortIPAddress_Type = IpAddress
_T7PortIPAddress_Object = MibTableColumn
t7PortIPAddress = _T7PortIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 8, 1, 1, 1, 10),
    _T7PortIPAddress_Type()
)
t7PortIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t7PortIPAddress.setStatus("mandatory")


class _T7UDPPortNumber_Type(Integer32):
    """Custom type t7UDPPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_T7UDPPortNumber_Type.__name__ = "Integer32"
_T7UDPPortNumber_Object = MibTableColumn
t7UDPPortNumber = _T7UDPPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 8, 1, 1, 1, 11),
    _T7UDPPortNumber_Type()
)
t7UDPPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t7UDPPortNumber.setStatus("mandatory")
_T7StatsGroup_ObjectIdentity = ObjectIdentity
t7StatsGroup = _T7StatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 8, 2)
)
_T7StatsTable_Object = MibTable
t7StatsTable = _T7StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 8, 2, 1)
)
if mibBuilder.loadTexts:
    t7StatsTable.setStatus("mandatory")
_T7StatsEntry_Object = MibTableRow
t7StatsEntry = _T7StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 8, 2, 1, 1)
)
t7StatsEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "t7StatsIndex"),
)
if mibBuilder.loadTexts:
    t7StatsEntry.setStatus("mandatory")
_T7StatsIndex_Type = Integer32
_T7StatsIndex_Object = MibTableColumn
t7StatsIndex = _T7StatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 8, 2, 1, 1, 1),
    _T7StatsIndex_Type()
)
t7StatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t7StatsIndex.setStatus("mandatory")
_T7InOctets_Type = Counter32
_T7InOctets_Object = MibTableColumn
t7InOctets = _T7InOctets_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 8, 2, 1, 1, 2),
    _T7InOctets_Type()
)
t7InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t7InOctets.setStatus("mandatory")
_T7OutOctets_Type = Counter32
_T7OutOctets_Object = MibTableColumn
t7OutOctets = _T7OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 8, 2, 1, 1, 3),
    _T7OutOctets_Type()
)
t7OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t7OutOctets.setStatus("mandatory")
_T7InMessages_Type = Counter32
_T7InMessages_Object = MibTableColumn
t7InMessages = _T7InMessages_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 8, 2, 1, 1, 4),
    _T7InMessages_Type()
)
t7InMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t7InMessages.setStatus("mandatory")
_T7OutMessages_Type = Counter32
_T7OutMessages_Object = MibTableColumn
t7OutMessages = _T7OutMessages_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 8, 2, 1, 1, 5),
    _T7OutMessages_Type()
)
t7OutMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t7OutMessages.setStatus("mandatory")
_T7InMsgDiscarded_Type = Counter32
_T7InMsgDiscarded_Object = MibTableColumn
t7InMsgDiscarded = _T7InMsgDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 8, 2, 1, 1, 6),
    _T7InMsgDiscarded_Type()
)
t7InMsgDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t7InMsgDiscarded.setStatus("mandatory")
_T7OutMsgDiscarded_Type = Counter32
_T7OutMsgDiscarded_Object = MibTableColumn
t7OutMsgDiscarded = _T7OutMsgDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 8, 2, 1, 1, 7),
    _T7OutMsgDiscarded_Type()
)
t7OutMsgDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t7OutMsgDiscarded.setStatus("mandatory")
_T7XmtFailures_Type = Counter32
_T7XmtFailures_Object = MibTableColumn
t7XmtFailures = _T7XmtFailures_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 8, 2, 1, 1, 8),
    _T7XmtFailures_Type()
)
t7XmtFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t7XmtFailures.setStatus("mandatory")
_T7RcvMsgForwarded_Type = Counter32
_T7RcvMsgForwarded_Object = MibTableColumn
t7RcvMsgForwarded = _T7RcvMsgForwarded_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 8, 2, 1, 1, 9),
    _T7RcvMsgForwarded_Type()
)
t7RcvMsgForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t7RcvMsgForwarded.setStatus("mandatory")
_T7RcvMsgErrors_Type = Counter32
_T7RcvMsgErrors_Object = MibTableColumn
t7RcvMsgErrors = _T7RcvMsgErrors_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 8, 2, 1, 1, 10),
    _T7RcvMsgErrors_Type()
)
t7RcvMsgErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t7RcvMsgErrors.setStatus("mandatory")
_T7RcvCharsDiscarded_Type = Counter32
_T7RcvCharsDiscarded_Object = MibTableColumn
t7RcvCharsDiscarded = _T7RcvCharsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 8, 2, 1, 1, 11),
    _T7RcvCharsDiscarded_Type()
)
t7RcvCharsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t7RcvCharsDiscarded.setStatus("mandatory")
_T7RcvParityErrors_Type = Counter32
_T7RcvParityErrors_Object = MibTableColumn
t7RcvParityErrors = _T7RcvParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 8, 2, 1, 1, 12),
    _T7RcvParityErrors_Type()
)
t7RcvParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t7RcvParityErrors.setStatus("mandatory")
_T7RcvFramingErrors_Type = Counter32
_T7RcvFramingErrors_Object = MibTableColumn
t7RcvFramingErrors = _T7RcvFramingErrors_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 8, 2, 1, 1, 13),
    _T7RcvFramingErrors_Type()
)
t7RcvFramingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t7RcvFramingErrors.setStatus("mandatory")
_T7RcvFifoOverruns_Type = Counter32
_T7RcvFifoOverruns_Object = MibTableColumn
t7RcvFifoOverruns = _T7RcvFifoOverruns_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 8, 2, 1, 1, 14),
    _T7RcvFifoOverruns_Type()
)
t7RcvFifoOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t7RcvFifoOverruns.setStatus("mandatory")
_T7RcvCharsOverruns_Type = Counter32
_T7RcvCharsOverruns_Object = MibTableColumn
t7RcvCharsOverruns = _T7RcvCharsOverruns_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 8, 2, 1, 1, 15),
    _T7RcvCharsOverruns_Type()
)
t7RcvCharsOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t7RcvCharsOverruns.setStatus("mandatory")
_T7RcvBreakConditions_Type = Counter32
_T7RcvBreakConditions_Object = MibTableColumn
t7RcvBreakConditions = _T7RcvBreakConditions_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 8, 2, 1, 1, 16),
    _T7RcvBreakConditions_Type()
)
t7RcvBreakConditions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t7RcvBreakConditions.setStatus("mandatory")
_NodeFrCirGroup_ObjectIdentity = ObjectIdentity
nodeFrCirGroup = _NodeFrCirGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 9)
)
_FrExtCircuitTable_Object = MibTable
frExtCircuitTable = _FrExtCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 9, 1)
)
if mibBuilder.loadTexts:
    frExtCircuitTable.setStatus("mandatory")
_FrExtCircuitEntry_Object = MibTableRow
frExtCircuitEntry = _FrExtCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 9, 1, 1)
)
frExtCircuitEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "frExtCircuitIfIndex"),
    (0, "SYNC-RESEARCH-MIB", "frExtCircuitDlci"),
)
if mibBuilder.loadTexts:
    frExtCircuitEntry.setStatus("mandatory")
_FrExtCircuitIfIndex_Type = Integer32
_FrExtCircuitIfIndex_Object = MibTableColumn
frExtCircuitIfIndex = _FrExtCircuitIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 9, 1, 1, 1),
    _FrExtCircuitIfIndex_Type()
)
frExtCircuitIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frExtCircuitIfIndex.setStatus("mandatory")
_FrExtCircuitDlci_Type = Integer32
_FrExtCircuitDlci_Object = MibTableColumn
frExtCircuitDlci = _FrExtCircuitDlci_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 9, 1, 1, 2),
    _FrExtCircuitDlci_Type()
)
frExtCircuitDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frExtCircuitDlci.setStatus("mandatory")


class _FrExtCircuitStatusIgnored_Type(Integer32):
    """Custom type frExtCircuitStatusIgnored based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_FrExtCircuitStatusIgnored_Type.__name__ = "Integer32"
_FrExtCircuitStatusIgnored_Object = MibTableColumn
frExtCircuitStatusIgnored = _FrExtCircuitStatusIgnored_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 9, 1, 1, 3),
    _FrExtCircuitStatusIgnored_Type()
)
frExtCircuitStatusIgnored.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frExtCircuitStatusIgnored.setStatus("mandatory")


class _FrExtCircuitStatusAcknowledged_Type(Integer32):
    """Custom type frExtCircuitStatusAcknowledged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_FrExtCircuitStatusAcknowledged_Type.__name__ = "Integer32"
_FrExtCircuitStatusAcknowledged_Object = MibTableColumn
frExtCircuitStatusAcknowledged = _FrExtCircuitStatusAcknowledged_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 9, 1, 1, 4),
    _FrExtCircuitStatusAcknowledged_Type()
)
frExtCircuitStatusAcknowledged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frExtCircuitStatusAcknowledged.setStatus("mandatory")


class _FrExtCircuitPartnerId_Type(DisplayString):
    """Custom type frExtCircuitPartnerId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_FrExtCircuitPartnerId_Type.__name__ = "DisplayString"
_FrExtCircuitPartnerId_Object = MibTableColumn
frExtCircuitPartnerId = _FrExtCircuitPartnerId_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 9, 1, 1, 5),
    _FrExtCircuitPartnerId_Type()
)
frExtCircuitPartnerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frExtCircuitPartnerId.setStatus("mandatory")
_FrExtCircuitTxDe_Type = Counter32
_FrExtCircuitTxDe_Object = MibTableColumn
frExtCircuitTxDe = _FrExtCircuitTxDe_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 9, 1, 1, 6),
    _FrExtCircuitTxDe_Type()
)
frExtCircuitTxDe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frExtCircuitTxDe.setStatus("mandatory")
_FrExtCircuitRxDe_Type = Counter32
_FrExtCircuitRxDe_Object = MibTableColumn
frExtCircuitRxDe = _FrExtCircuitRxDe_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 9, 1, 1, 7),
    _FrExtCircuitRxDe_Type()
)
frExtCircuitRxDe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frExtCircuitRxDe.setStatus("mandatory")
_FrExtCircuitMinBits_Type = Gauge32
_FrExtCircuitMinBits_Object = MibTableColumn
frExtCircuitMinBits = _FrExtCircuitMinBits_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 9, 1, 1, 8),
    _FrExtCircuitMinBits_Type()
)
frExtCircuitMinBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frExtCircuitMinBits.setStatus("mandatory")
_FrExtCircuitMaxBits_Type = Gauge32
_FrExtCircuitMaxBits_Object = MibTableColumn
frExtCircuitMaxBits = _FrExtCircuitMaxBits_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 9, 1, 1, 9),
    _FrExtCircuitMaxBits_Type()
)
frExtCircuitMaxBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frExtCircuitMaxBits.setStatus("mandatory")
_FrExtCircuitQOctets_Type = Counter32
_FrExtCircuitQOctets_Object = MibTableColumn
frExtCircuitQOctets = _FrExtCircuitQOctets_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 9, 1, 1, 10),
    _FrExtCircuitQOctets_Type()
)
frExtCircuitQOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frExtCircuitQOctets.setStatus("mandatory")
_NodeSlipGroup_ObjectIdentity = ObjectIdentity
nodeSlipGroup = _NodeSlipGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 10)
)
_SlipConfigGroup_ObjectIdentity = ObjectIdentity
slipConfigGroup = _SlipConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 10, 1)
)
_SlipConfigTable_Object = MibTable
slipConfigTable = _SlipConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 10, 1, 1)
)
if mibBuilder.loadTexts:
    slipConfigTable.setStatus("mandatory")
_SlipConfigEntry_Object = MibTableRow
slipConfigEntry = _SlipConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 10, 1, 1, 1)
)
slipConfigEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "slipConfigIndex"),
)
if mibBuilder.loadTexts:
    slipConfigEntry.setStatus("mandatory")
_SlipConfigIndex_Type = Integer32
_SlipConfigIndex_Object = MibTableColumn
slipConfigIndex = _SlipConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 10, 1, 1, 1, 1),
    _SlipConfigIndex_Type()
)
slipConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipConfigIndex.setStatus("mandatory")


class _SlipProtocolEnabled_Type(Integer32):
    """Custom type slipProtocolEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SlipProtocolEnabled_Type.__name__ = "Integer32"
_SlipProtocolEnabled_Object = MibTableColumn
slipProtocolEnabled = _SlipProtocolEnabled_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 10, 1, 1, 1, 2),
    _SlipProtocolEnabled_Type()
)
slipProtocolEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipProtocolEnabled.setStatus("mandatory")


class _SlipPortSpeed_Type(Integer32):
    """Custom type slipPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(75,
              150,
              300,
              600,
              1200,
              2400,
              4800,
              9600,
              19200)
        )
    )
    namedValues = NamedValues(
        *(("speed1200", 1200),
          ("speed150", 150),
          ("speed19200", 19200),
          ("speed2400", 2400),
          ("speed300", 300),
          ("speed4800", 4800),
          ("speed600", 600),
          ("speed75", 75),
          ("speed9600", 9600))
    )


_SlipPortSpeed_Type.__name__ = "Integer32"
_SlipPortSpeed_Object = MibTableColumn
slipPortSpeed = _SlipPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 10, 1, 1, 1, 3),
    _SlipPortSpeed_Type()
)
slipPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipPortSpeed.setStatus("mandatory")


class _SlipStopBits_Type(Integer32):
    """Custom type slipStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SlipStopBits_Type.__name__ = "Integer32"
_SlipStopBits_Object = MibTableColumn
slipStopBits = _SlipStopBits_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 10, 1, 1, 1, 4),
    _SlipStopBits_Type()
)
slipStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipStopBits.setStatus("mandatory")


class _SlipIdleTimer_Type(Integer32):
    """Custom type slipIdleTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_SlipIdleTimer_Type.__name__ = "Integer32"
_SlipIdleTimer_Object = MibTableColumn
slipIdleTimer = _SlipIdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 10, 1, 1, 1, 5),
    _SlipIdleTimer_Type()
)
slipIdleTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipIdleTimer.setStatus("mandatory")
_SlipPortIPAddress_Type = IpAddress
_SlipPortIPAddress_Object = MibTableColumn
slipPortIPAddress = _SlipPortIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 10, 1, 1, 1, 6),
    _SlipPortIPAddress_Type()
)
slipPortIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipPortIPAddress.setStatus("mandatory")


class _SlipUsage_Type(Integer32):
    """Custom type slipUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip-routing", 3),
          ("ipend-node", 2),
          ("modem-management", 1))
    )


_SlipUsage_Type.__name__ = "Integer32"
_SlipUsage_Object = MibTableColumn
slipUsage = _SlipUsage_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 10, 1, 1, 1, 7),
    _SlipUsage_Type()
)
slipUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipUsage.setStatus("mandatory")
_SlipNetworkMask_Type = IpAddress
_SlipNetworkMask_Object = MibTableColumn
slipNetworkMask = _SlipNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 10, 1, 1, 1, 8),
    _SlipNetworkMask_Type()
)
slipNetworkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipNetworkMask.setStatus("mandatory")
_SlipDefaultGateway_Type = IpAddress
_SlipDefaultGateway_Object = MibTableColumn
slipDefaultGateway = _SlipDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 10, 1, 1, 1, 9),
    _SlipDefaultGateway_Type()
)
slipDefaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipDefaultGateway.setStatus("mandatory")


class _SlipEnableRIP_Type(Integer32):
    """Custom type slipEnableRIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SlipEnableRIP_Type.__name__ = "Integer32"
_SlipEnableRIP_Object = MibTableColumn
slipEnableRIP = _SlipEnableRIP_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 10, 1, 1, 1, 10),
    _SlipEnableRIP_Type()
)
slipEnableRIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipEnableRIP.setStatus("mandatory")
_SlipStatsGroup_ObjectIdentity = ObjectIdentity
slipStatsGroup = _SlipStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 10, 2)
)
_SlipStatsTable_Object = MibTable
slipStatsTable = _SlipStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 10, 2, 1)
)
if mibBuilder.loadTexts:
    slipStatsTable.setStatus("mandatory")
_SlipStatsEntry_Object = MibTableRow
slipStatsEntry = _SlipStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 10, 2, 1, 1)
)
slipStatsEntry.setIndexNames(
    (0, "SYNC-RESEARCH-MIB", "slipStatsIndex"),
)
if mibBuilder.loadTexts:
    slipStatsEntry.setStatus("mandatory")
_SlipStatsIndex_Type = Integer32
_SlipStatsIndex_Object = MibTableColumn
slipStatsIndex = _SlipStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 10, 2, 1, 1, 1),
    _SlipStatsIndex_Type()
)
slipStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipStatsIndex.setStatus("mandatory")
_SlipInChrs_Type = Counter32
_SlipInChrs_Object = MibTableColumn
slipInChrs = _SlipInChrs_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 10, 2, 1, 1, 2),
    _SlipInChrs_Type()
)
slipInChrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipInChrs.setStatus("mandatory")
_SlipOutChrs_Type = Counter32
_SlipOutChrs_Object = MibTableColumn
slipOutChrs = _SlipOutChrs_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 10, 2, 1, 1, 3),
    _SlipOutChrs_Type()
)
slipOutChrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipOutChrs.setStatus("mandatory")
_SlipInMessages_Type = Counter32
_SlipInMessages_Object = MibTableColumn
slipInMessages = _SlipInMessages_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 10, 2, 1, 1, 4),
    _SlipInMessages_Type()
)
slipInMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipInMessages.setStatus("mandatory")
_SlipOutMessages_Type = Counter32
_SlipOutMessages_Object = MibTableColumn
slipOutMessages = _SlipOutMessages_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 10, 2, 1, 1, 5),
    _SlipOutMessages_Type()
)
slipOutMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipOutMessages.setStatus("mandatory")
_SlipInMsgDiscarded_Type = Counter32
_SlipInMsgDiscarded_Object = MibTableColumn
slipInMsgDiscarded = _SlipInMsgDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 10, 2, 1, 1, 6),
    _SlipInMsgDiscarded_Type()
)
slipInMsgDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipInMsgDiscarded.setStatus("mandatory")
_SlipOutMsgDiscarded_Type = Counter32
_SlipOutMsgDiscarded_Object = MibTableColumn
slipOutMsgDiscarded = _SlipOutMsgDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 10, 2, 1, 1, 7),
    _SlipOutMsgDiscarded_Type()
)
slipOutMsgDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipOutMsgDiscarded.setStatus("mandatory")
_SlipXmtFailures_Type = Counter32
_SlipXmtFailures_Object = MibTableColumn
slipXmtFailures = _SlipXmtFailures_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 10, 2, 1, 1, 8),
    _SlipXmtFailures_Type()
)
slipXmtFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipXmtFailures.setStatus("mandatory")
_SlipRcvMsgForwarded_Type = Counter32
_SlipRcvMsgForwarded_Object = MibTableColumn
slipRcvMsgForwarded = _SlipRcvMsgForwarded_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 10, 2, 1, 1, 9),
    _SlipRcvMsgForwarded_Type()
)
slipRcvMsgForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipRcvMsgForwarded.setStatus("mandatory")
_SlipRcvMsgErrors_Type = Counter32
_SlipRcvMsgErrors_Object = MibTableColumn
slipRcvMsgErrors = _SlipRcvMsgErrors_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 10, 2, 1, 1, 10),
    _SlipRcvMsgErrors_Type()
)
slipRcvMsgErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipRcvMsgErrors.setStatus("mandatory")
_SlipRcvCharsDiscarded_Type = Counter32
_SlipRcvCharsDiscarded_Object = MibTableColumn
slipRcvCharsDiscarded = _SlipRcvCharsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 10, 2, 1, 1, 11),
    _SlipRcvCharsDiscarded_Type()
)
slipRcvCharsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipRcvCharsDiscarded.setStatus("mandatory")
_SlipRcvParityErrors_Type = Counter32
_SlipRcvParityErrors_Object = MibTableColumn
slipRcvParityErrors = _SlipRcvParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 10, 2, 1, 1, 12),
    _SlipRcvParityErrors_Type()
)
slipRcvParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipRcvParityErrors.setStatus("mandatory")
_SlipRcvFramingErrors_Type = Counter32
_SlipRcvFramingErrors_Object = MibTableColumn
slipRcvFramingErrors = _SlipRcvFramingErrors_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 10, 2, 1, 1, 13),
    _SlipRcvFramingErrors_Type()
)
slipRcvFramingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipRcvFramingErrors.setStatus("mandatory")
_SlipRcvFifoOverruns_Type = Counter32
_SlipRcvFifoOverruns_Object = MibTableColumn
slipRcvFifoOverruns = _SlipRcvFifoOverruns_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 10, 2, 1, 1, 14),
    _SlipRcvFifoOverruns_Type()
)
slipRcvFifoOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipRcvFifoOverruns.setStatus("mandatory")
_SlipRcvCharsOverruns_Type = Counter32
_SlipRcvCharsOverruns_Object = MibTableColumn
slipRcvCharsOverruns = _SlipRcvCharsOverruns_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 10, 2, 1, 1, 15),
    _SlipRcvCharsOverruns_Type()
)
slipRcvCharsOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipRcvCharsOverruns.setStatus("mandatory")
_SlipRcvBreakConditions_Type = Counter32
_SlipRcvBreakConditions_Object = MibTableColumn
slipRcvBreakConditions = _SlipRcvBreakConditions_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 10, 2, 1, 1, 16),
    _SlipRcvBreakConditions_Type()
)
slipRcvBreakConditions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipRcvBreakConditions.setStatus("mandatory")
_NodeIpxGroup_ObjectIdentity = ObjectIdentity
nodeIpxGroup = _NodeIpxGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 11)
)
_IpxConfigGroup_ObjectIdentity = ObjectIdentity
ipxConfigGroup = _IpxConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 11, 1)
)


class _IpxEnableRouting_Type(Integer32):
    """Custom type ipxEnableRouting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IpxEnableRouting_Type.__name__ = "Integer32"
_IpxEnableRouting_Object = MibScalar
ipxEnableRouting = _IpxEnableRouting_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 11, 1, 1),
    _IpxEnableRouting_Type()
)
ipxEnableRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxEnableRouting.setStatus("mandatory")


class _IpxRoutedTxPriority_Type(Integer32):
    """Custom type ipxRoutedTxPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 4),
          ("medium", 3),
          ("urgent", 1))
    )


_IpxRoutedTxPriority_Type.__name__ = "Integer32"
_IpxRoutedTxPriority_Object = MibScalar
ipxRoutedTxPriority = _IpxRoutedTxPriority_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 11, 1, 2),
    _IpxRoutedTxPriority_Type()
)
ipxRoutedTxPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRoutedTxPriority.setStatus("mandatory")


class _IpxEnableRipBroadcast_Type(Integer32):
    """Custom type ipxEnableRipBroadcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IpxEnableRipBroadcast_Type.__name__ = "Integer32"
_IpxEnableRipBroadcast_Object = MibScalar
ipxEnableRipBroadcast = _IpxEnableRipBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 11, 1, 3),
    _IpxEnableRipBroadcast_Type()
)
ipxEnableRipBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxEnableRipBroadcast.setStatus("mandatory")


class _IpxEnableSapBroadcast_Type(Integer32):
    """Custom type ipxEnableSapBroadcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IpxEnableSapBroadcast_Type.__name__ = "Integer32"
_IpxEnableSapBroadcast_Object = MibScalar
ipxEnableSapBroadcast = _IpxEnableSapBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 11, 1, 4),
    _IpxEnableSapBroadcast_Type()
)
ipxEnableSapBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxEnableSapBroadcast.setStatus("mandatory")


class _IpxEnableNetBIOS_Type(Integer32):
    """Custom type ipxEnableNetBIOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IpxEnableNetBIOS_Type.__name__ = "Integer32"
_IpxEnableNetBIOS_Object = MibScalar
ipxEnableNetBIOS = _IpxEnableNetBIOS_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 11, 1, 5),
    _IpxEnableNetBIOS_Type()
)
ipxEnableNetBIOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxEnableNetBIOS.setStatus("mandatory")


class _IpxGlobalNodeId_Type(OctetString):
    """Custom type ipxGlobalNodeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IpxGlobalNodeId_Type.__name__ = "OctetString"
_IpxGlobalNodeId_Object = MibScalar
ipxGlobalNodeId = _IpxGlobalNodeId_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 11, 1, 6),
    _IpxGlobalNodeId_Type()
)
ipxGlobalNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxGlobalNodeId.setStatus("mandatory")
_NodeIpGroup_ObjectIdentity = ObjectIdentity
nodeIpGroup = _NodeIpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 12)
)
_IpConfigGroup_ObjectIdentity = ObjectIdentity
ipConfigGroup = _IpConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 485, 3, 12, 1)
)
_PriIPHelperAddress_Type = IpAddress
_PriIPHelperAddress_Object = MibScalar
priIPHelperAddress = _PriIPHelperAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 12, 1, 1),
    _PriIPHelperAddress_Type()
)
priIPHelperAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    priIPHelperAddress.setStatus("mandatory")
_SecIPHelperAddress_Type = IpAddress
_SecIPHelperAddress_Object = MibScalar
secIPHelperAddress = _SecIPHelperAddress_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 12, 1, 2),
    _SecIPHelperAddress_Type()
)
secIPHelperAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secIPHelperAddress.setStatus("mandatory")
_InternalIPAddr_Type = IpAddress
_InternalIPAddr_Object = MibScalar
internalIPAddr = _InternalIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 12, 1, 3),
    _InternalIPAddr_Type()
)
internalIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalIPAddr.setStatus("mandatory")
_InternalIPNetmask_Type = IpAddress
_InternalIPNetmask_Object = MibScalar
internalIPNetmask = _InternalIPNetmask_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 12, 1, 4),
    _InternalIPNetmask_Type()
)
internalIPNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalIPNetmask.setStatus("mandatory")


class _EnableIpRouting_Type(Integer32):
    """Custom type enableIpRouting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_EnableIpRouting_Type.__name__ = "Integer32"
_EnableIpRouting_Object = MibScalar
enableIpRouting = _EnableIpRouting_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 12, 1, 5),
    _EnableIpRouting_Type()
)
enableIpRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enableIpRouting.setStatus("mandatory")


class _EnableIpBridging_Type(Integer32):
    """Custom type enableIpBridging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_EnableIpBridging_Type.__name__ = "Integer32"
_EnableIpBridging_Object = MibScalar
enableIpBridging = _EnableIpBridging_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 12, 1, 6),
    _EnableIpBridging_Type()
)
enableIpBridging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enableIpBridging.setStatus("mandatory")


class _EnableRipBroadcast_Type(Integer32):
    """Custom type enableRipBroadcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_EnableRipBroadcast_Type.__name__ = "Integer32"
_EnableRipBroadcast_Object = MibScalar
enableRipBroadcast = _EnableRipBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 485, 3, 12, 1, 7),
    _EnableRipBroadcast_Type()
)
enableRipBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enableRipBroadcast.setStatus("mandatory")

# Managed Objects groups


# Notification objects

configChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 0, 800)
)
configChanged.setObjects(
      *(("SYNC-RESEARCH-MIB", "lastTrapSeqNumber"),
        ("SYNC-RESEARCH-MIB", "configId"))
)
if mibBuilder.loadTexts:
    configChanged.setStatus(
        ""
    )

configError = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 0, 801)
)
configError.setObjects(
      *(("SYNC-RESEARCH-MIB", "lastTrapSeqNumber"),
        ("SYNC-RESEARCH-MIB", "lastInstallErrCode"))
)
if mibBuilder.loadTexts:
    configError.setStatus(
        ""
    )

dumpExists = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 0, 802)
)
dumpExists.setObjects(
      *(("SYNC-RESEARCH-MIB", "lastTrapSeqNumber"),
        ("SYNC-RESEARCH-MIB", "dumpFileName"))
)
if mibBuilder.loadTexts:
    dumpExists.setStatus(
        ""
    )

dumpArchived = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 0, 803)
)
dumpArchived.setObjects(
    ("SYNC-RESEARCH-MIB", "lastTrapSeqNumber")
)
if mibBuilder.loadTexts:
    dumpArchived.setStatus(
        ""
    )

lineStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 0, 804)
)
lineStatusChanged.setObjects(
      *(("SYNC-RESEARCH-MIB", "lastTrapSeqNumber"),
        ("SYNC-RESEARCH-MIB", "lineStatus"),
        ("SYNC-RESEARCH-MIB", "lineControlFailureCode"),
        ("SYNC-RESEARCH-MIB", "linePhysicalIndex"),
        ("SYNC-RESEARCH-MIB", "lineCableType"))
)
if mibBuilder.loadTexts:
    lineStatusChanged.setStatus(
        ""
    )

lanStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 0, 805)
)
lanStatusChanged.setObjects(
      *(("SYNC-RESEARCH-MIB", "lastTrapSeqNumber"),
        ("SYNC-RESEARCH-MIB", "lanStatus"),
        ("SYNC-RESEARCH-MIB", "lanControlFailureCode"))
)
if mibBuilder.loadTexts:
    lanStatusChanged.setStatus(
        ""
    )

lineQuality = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 0, 806)
)
lineQuality.setObjects(
      *(("SYNC-RESEARCH-MIB", "lastTrapSeqNumber"),
        ("SYNC-RESEARCH-MIB", "lineQualityFrameCount"),
        ("SYNC-RESEARCH-MIB", "lineQualityCRCErrors"),
        ("SYNC-RESEARCH-MIB", "lineQualityAborts"),
        ("SYNC-RESEARCH-MIB", "linePhysicalIndex"))
)
if mibBuilder.loadTexts:
    lineQuality.setStatus(
        ""
    )

puStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 0, 807)
)
puStatusChanged.setObjects(
      *(("SYNC-RESEARCH-MIB", "lastTrapSeqNumber"),
        ("SYNC-RESEARCH-MIB", "puStatus"),
        ("SYNC-RESEARCH-MIB", "puControlFailureCode"),
        ("SYNC-RESEARCH-MIB", "linePhysicalIndex"),
        ("SYNC-RESEARCH-MIB", "puControlPUAddress"))
)
if mibBuilder.loadTexts:
    puStatusChanged.setStatus(
        ""
    )

puConnectionStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 0, 808)
)
puConnectionStatusChanged.setObjects(
      *(("SYNC-RESEARCH-MIB", "lastTrapSeqNumber"),
        ("SYNC-RESEARCH-MIB", "puConnectionStatus"),
        ("SYNC-RESEARCH-MIB", "puLastClearCode"))
)
if mibBuilder.loadTexts:
    puConnectionStatusChanged.setStatus(
        ""
    )

netviewConnectionStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 0, 809)
)
netviewConnectionStatusChanged.setObjects(
      *(("SYNC-RESEARCH-MIB", "lastTrapSeqNumber"),
        ("SYNC-RESEARCH-MIB", "netviewConnectionStatus"),
        ("SYNC-RESEARCH-MIB", "netviewLastClearCode"))
)
if mibBuilder.loadTexts:
    netviewConnectionStatusChanged.setStatus(
        ""
    )

netviewAltConnectionStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 0, 810)
)
netviewAltConnectionStatusChanged.setObjects(
      *(("SYNC-RESEARCH-MIB", "lastTrapSeqNumber"),
        ("SYNC-RESEARCH-MIB", "netviewAltConnectionStatus"),
        ("SYNC-RESEARCH-MIB", "netviewAltLastClearCode"))
)
if mibBuilder.loadTexts:
    netviewAltConnectionStatusChanged.setStatus(
        ""
    )

puConnectionStatusUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 0, 811)
)
puConnectionStatusUp.setObjects(
      *(("SYNC-RESEARCH-MIB", "lastTrapSeqNumber"),
        ("SYNC-RESEARCH-MIB", "linePhysicalIndex"),
        ("SYNC-RESEARCH-MIB", "puControlPUAddress"))
)
if mibBuilder.loadTexts:
    puConnectionStatusUp.setStatus(
        ""
    )

puConnectionStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 0, 812)
)
puConnectionStatusDown.setObjects(
      *(("SYNC-RESEARCH-MIB", "lastTrapSeqNumber"),
        ("SYNC-RESEARCH-MIB", "linePhysicalIndex"),
        ("SYNC-RESEARCH-MIB", "puControlPUAddress"),
        ("SYNC-RESEARCH-MIB", "puLastClearCode"))
)
if mibBuilder.loadTexts:
    puConnectionStatusDown.setStatus(
        ""
    )

netviewConnectionStatusUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 0, 813)
)
netviewConnectionStatusUp.setObjects(
    ("SYNC-RESEARCH-MIB", "lastTrapSeqNumber")
)
if mibBuilder.loadTexts:
    netviewConnectionStatusUp.setStatus(
        ""
    )

netviewConnectionStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 0, 814)
)
netviewConnectionStatusDown.setObjects(
      *(("SYNC-RESEARCH-MIB", "lastTrapSeqNumber"),
        ("SYNC-RESEARCH-MIB", "netviewLastClearCode"))
)
if mibBuilder.loadTexts:
    netviewConnectionStatusDown.setStatus(
        ""
    )

netviewAltConnectionStatusUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 0, 815)
)
netviewAltConnectionStatusUp.setObjects(
    ("SYNC-RESEARCH-MIB", "lastTrapSeqNumber")
)
if mibBuilder.loadTexts:
    netviewAltConnectionStatusUp.setStatus(
        ""
    )

netviewAltConnectionStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 0, 816)
)
netviewAltConnectionStatusDown.setObjects(
      *(("SYNC-RESEARCH-MIB", "lastTrapSeqNumber"),
        ("SYNC-RESEARCH-MIB", "netviewAltLastClearCode"))
)
if mibBuilder.loadTexts:
    netviewAltConnectionStatusDown.setStatus(
        ""
    )

sessSwitchedToPrimaryDLCI = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 0, 817)
)
sessSwitchedToPrimaryDLCI.setObjects(
      *(("SYNC-RESEARCH-MIB", "lastTrapSeqNumber"),
        ("SYNC-RESEARCH-MIB", "puControlLineIndex"),
        ("SYNC-RESEARCH-MIB", "puControlPUAddress"),
        ("SYNC-RESEARCH-MIB", "puCurrentDlci"),
        ("SYNC-RESEARCH-MIB", "puIsDynamic"))
)
if mibBuilder.loadTexts:
    sessSwitchedToPrimaryDLCI.setStatus(
        ""
    )

sessSwitchedToParallelDLCI = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 0, 818)
)
sessSwitchedToParallelDLCI.setObjects(
      *(("SYNC-RESEARCH-MIB", "lastTrapSeqNumber"),
        ("SYNC-RESEARCH-MIB", "puControlLineIndex"),
        ("SYNC-RESEARCH-MIB", "puControlPUAddress"),
        ("SYNC-RESEARCH-MIB", "puCurrentDlci"),
        ("SYNC-RESEARCH-MIB", "puIsDynamic"))
)
if mibBuilder.loadTexts:
    sessSwitchedToParallelDLCI.setStatus(
        ""
    )

sessUpOnPrimaryDLCI = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 0, 819)
)
sessUpOnPrimaryDLCI.setObjects(
      *(("SYNC-RESEARCH-MIB", "lastTrapSeqNumber"),
        ("SYNC-RESEARCH-MIB", "puControlLineIndex"),
        ("SYNC-RESEARCH-MIB", "puControlPUAddress"),
        ("SYNC-RESEARCH-MIB", "puCurrentDlci"),
        ("SYNC-RESEARCH-MIB", "puCurrentMAC"),
        ("SYNC-RESEARCH-MIB", "puIsDynamic"))
)
if mibBuilder.loadTexts:
    sessUpOnPrimaryDLCI.setStatus(
        ""
    )

sessUpOnParallelDLCI = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 0, 820)
)
sessUpOnParallelDLCI.setObjects(
      *(("SYNC-RESEARCH-MIB", "lastTrapSeqNumber"),
        ("SYNC-RESEARCH-MIB", "puControlLineIndex"),
        ("SYNC-RESEARCH-MIB", "puControlPUAddress"),
        ("SYNC-RESEARCH-MIB", "puCurrentDlci"),
        ("SYNC-RESEARCH-MIB", "puCurrentMAC"),
        ("SYNC-RESEARCH-MIB", "puIsDynamic"))
)
if mibBuilder.loadTexts:
    sessUpOnParallelDLCI.setStatus(
        ""
    )

sessUpOnAlternateDLCI = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 0, 821)
)
sessUpOnAlternateDLCI.setObjects(
      *(("SYNC-RESEARCH-MIB", "lastTrapSeqNumber"),
        ("SYNC-RESEARCH-MIB", "puControlLineIndex"),
        ("SYNC-RESEARCH-MIB", "puControlPUAddress"),
        ("SYNC-RESEARCH-MIB", "puCurrentDlci"),
        ("SYNC-RESEARCH-MIB", "puCurrentMAC"),
        ("SYNC-RESEARCH-MIB", "puIsDynamic"))
)
if mibBuilder.loadTexts:
    sessUpOnAlternateDLCI.setStatus(
        ""
    )

sessUpOnPrimaryMAC = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 0, 822)
)
sessUpOnPrimaryMAC.setObjects(
      *(("SYNC-RESEARCH-MIB", "lastTrapSeqNumber"),
        ("SYNC-RESEARCH-MIB", "puControlLineIndex"),
        ("SYNC-RESEARCH-MIB", "puControlPUAddress"),
        ("SYNC-RESEARCH-MIB", "puCurrentDlci"),
        ("SYNC-RESEARCH-MIB", "puCurrentMAC"),
        ("SYNC-RESEARCH-MIB", "linePhysicalType"),
        ("SYNC-RESEARCH-MIB", "puIsDynamic"))
)
if mibBuilder.loadTexts:
    sessUpOnPrimaryMAC.setStatus(
        ""
    )

sessUpOnAlternateMAC = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 0, 823)
)
sessUpOnAlternateMAC.setObjects(
      *(("SYNC-RESEARCH-MIB", "lastTrapSeqNumber"),
        ("SYNC-RESEARCH-MIB", "puControlLineIndex"),
        ("SYNC-RESEARCH-MIB", "puControlPUAddress"),
        ("SYNC-RESEARCH-MIB", "puCurrentDlci"),
        ("SYNC-RESEARCH-MIB", "puCurrentMAC"),
        ("SYNC-RESEARCH-MIB", "linePhysicalType"),
        ("SYNC-RESEARCH-MIB", "puIsDynamic"))
)
if mibBuilder.loadTexts:
    sessUpOnAlternateMAC.setStatus(
        ""
    )

sessDownOnPrimaryMAC = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 0, 824)
)
sessDownOnPrimaryMAC.setObjects(
      *(("SYNC-RESEARCH-MIB", "lastTrapSeqNumber"),
        ("SYNC-RESEARCH-MIB", "puControlLineIndex"),
        ("SYNC-RESEARCH-MIB", "puControlPUAddress"),
        ("SYNC-RESEARCH-MIB", "puLastClearCode"),
        ("SYNC-RESEARCH-MIB", "puLastDlciCleared"),
        ("SYNC-RESEARCH-MIB", "puLastMACCleared"),
        ("SYNC-RESEARCH-MIB", "linePhysicalType"),
        ("SYNC-RESEARCH-MIB", "puIsDynamic"))
)
if mibBuilder.loadTexts:
    sessDownOnPrimaryMAC.setStatus(
        ""
    )

sessDownOnAlternateMAC = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 0, 825)
)
sessDownOnAlternateMAC.setObjects(
      *(("SYNC-RESEARCH-MIB", "lastTrapSeqNumber"),
        ("SYNC-RESEARCH-MIB", "puControlLineIndex"),
        ("SYNC-RESEARCH-MIB", "puControlPUAddress"),
        ("SYNC-RESEARCH-MIB", "puLastClearCode"),
        ("SYNC-RESEARCH-MIB", "puLastDlciCleared"),
        ("SYNC-RESEARCH-MIB", "puLastMACCleared"),
        ("SYNC-RESEARCH-MIB", "linePhysicalType"),
        ("SYNC-RESEARCH-MIB", "puIsDynamic"))
)
if mibBuilder.loadTexts:
    sessDownOnAlternateMAC.setStatus(
        ""
    )

lostUNI = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 0, 826)
)
lostUNI.setObjects(
      *(("SYNC-RESEARCH-MIB", "lastTrapSeqNumber"),
        ("SYNC-RESEARCH-MIB", "linePhysicalIndex"))
)
if mibBuilder.loadTexts:
    lostUNI.setStatus(
        ""
    )

restoredUNI = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 0, 827)
)
restoredUNI.setObjects(
      *(("SYNC-RESEARCH-MIB", "lastTrapSeqNumber"),
        ("SYNC-RESEARCH-MIB", "linePhysicalIndex"))
)
if mibBuilder.loadTexts:
    restoredUNI.setStatus(
        ""
    )

switchedToBackup = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 0, 828)
)
switchedToBackup.setObjects(
      *(("SYNC-RESEARCH-MIB", "lastTrapSeqNumber"),
        ("SYNC-RESEARCH-MIB", "linePhysicalIndex"))
)
if mibBuilder.loadTexts:
    switchedToBackup.setStatus(
        ""
    )

switchedToDed = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 0, 829)
)
switchedToDed.setObjects(
      *(("SYNC-RESEARCH-MIB", "lastTrapSeqNumber"),
        ("SYNC-RESEARCH-MIB", "linePhysicalIndex"))
)
if mibBuilder.loadTexts:
    switchedToDed.setStatus(
        ""
    )

dialConnStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 0, 830)
)
dialConnStatusChanged.setObjects(
      *(("SYNC-RESEARCH-MIB", "lastTrapSeqNumber"),
        ("SYNC-RESEARCH-MIB", "lineStatus"),
        ("SYNC-RESEARCH-MIB", "lineControlFailureCode"),
        ("SYNC-RESEARCH-MIB", "linePhysicalIndex"))
)
if mibBuilder.loadTexts:
    dialConnStatusChanged.setStatus(
        ""
    )

sessUpOnSVC = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 0, 831)
)
sessUpOnSVC.setObjects(
      *(("SYNC-RESEARCH-MIB", "lastTrapSeqNumber"),
        ("SYNC-RESEARCH-MIB", "puControlLineIndex"),
        ("SYNC-RESEARCH-MIB", "puControlPUAddress"),
        ("SYNC-RESEARCH-MIB", "puCurrentSVC"),
        ("SYNC-RESEARCH-MIB", "puCurrentLocalDTE"),
        ("SYNC-RESEARCH-MIB", "puCurrentRemoteDTE"),
        ("SYNC-RESEARCH-MIB", "puIsDynamic"))
)
if mibBuilder.loadTexts:
    sessUpOnSVC.setStatus(
        ""
    )

sessDownOnSVC = NotificationType(
    (1, 3, 6, 1, 4, 1, 485, 0, 832)
)
sessDownOnSVC.setObjects(
      *(("SYNC-RESEARCH-MIB", "lastTrapSeqNumber"),
        ("SYNC-RESEARCH-MIB", "puControlLineIndex"),
        ("SYNC-RESEARCH-MIB", "puControlPUAddress"),
        ("SYNC-RESEARCH-MIB", "puLastClearCode"),
        ("SYNC-RESEARCH-MIB", "puLastSVCCleared"),
        ("SYNC-RESEARCH-MIB", "puLastLocalDTECleared"),
        ("SYNC-RESEARCH-MIB", "puLastRemoteDTECleared"),
        ("SYNC-RESEARCH-MIB", "puIsDynamic"))
)
if mibBuilder.loadTexts:
    sessDownOnSVC.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYNC-RESEARCH-MIB",
    **{"DisplayString": DisplayString,
       "PhysAddress": PhysAddress,
       "syncResearch": syncResearch,
       "configChanged": configChanged,
       "configError": configError,
       "dumpExists": dumpExists,
       "dumpArchived": dumpArchived,
       "lineStatusChanged": lineStatusChanged,
       "lanStatusChanged": lanStatusChanged,
       "lineQuality": lineQuality,
       "puStatusChanged": puStatusChanged,
       "puConnectionStatusChanged": puConnectionStatusChanged,
       "netviewConnectionStatusChanged": netviewConnectionStatusChanged,
       "netviewAltConnectionStatusChanged": netviewAltConnectionStatusChanged,
       "puConnectionStatusUp": puConnectionStatusUp,
       "puConnectionStatusDown": puConnectionStatusDown,
       "netviewConnectionStatusUp": netviewConnectionStatusUp,
       "netviewConnectionStatusDown": netviewConnectionStatusDown,
       "netviewAltConnectionStatusUp": netviewAltConnectionStatusUp,
       "netviewAltConnectionStatusDown": netviewAltConnectionStatusDown,
       "sessSwitchedToPrimaryDLCI": sessSwitchedToPrimaryDLCI,
       "sessSwitchedToParallelDLCI": sessSwitchedToParallelDLCI,
       "sessUpOnPrimaryDLCI": sessUpOnPrimaryDLCI,
       "sessUpOnParallelDLCI": sessUpOnParallelDLCI,
       "sessUpOnAlternateDLCI": sessUpOnAlternateDLCI,
       "sessUpOnPrimaryMAC": sessUpOnPrimaryMAC,
       "sessUpOnAlternateMAC": sessUpOnAlternateMAC,
       "sessDownOnPrimaryMAC": sessDownOnPrimaryMAC,
       "sessDownOnAlternateMAC": sessDownOnAlternateMAC,
       "lostUNI": lostUNI,
       "restoredUNI": restoredUNI,
       "switchedToBackup": switchedToBackup,
       "switchedToDed": switchedToDed,
       "dialConnStatusChanged": dialConnStatusChanged,
       "sessUpOnSVC": sessUpOnSVC,
       "sessDownOnSVC": sessDownOnSVC,
       "syncResearchAgent": syncResearchAgent,
       "syncProducts": syncProducts,
       "boundary": boundary,
       "syncCN2R2b": syncCN2R2b,
       "syncFN2R2b": syncFN2R2b,
       "syncCN4R2b": syncCN4R2b,
       "syncFN4R2b": syncFN4R2b,
       "syncQN4R2b": syncQN4R2b,
       "syncCN4R3b": syncCN4R3b,
       "syncFN4R3b": syncFN4R3b,
       "syncQN4R3b": syncQN4R3b,
       "syncCN4R4b": syncCN4R4b,
       "syncFN4R4b": syncFN4R4b,
       "syncQN4R4b": syncQN4R4b,
       "syncCN4R4bu": syncCN4R4bu,
       "syncFN4R4bu": syncFN4R4bu,
       "syncQN4R4bu": syncQN4R4bu,
       "syncCN4R4du": syncCN4R4du,
       "syncFN4R4du": syncFN4R4du,
       "syncQN4R4du": syncQN4R4du,
       "syncCN2R2du": syncCN2R2du,
       "syncFN2R2du": syncFN2R2du,
       "syncCN3R4bu": syncCN3R4bu,
       "syncFN3R4bu": syncFN3R4bu,
       "syncCN3R4du": syncCN3R4du,
       "syncFN3R4du": syncFN3R4du,
       "syncCN4R5b": syncCN4R5b,
       "syncFN4R5b": syncFN4R5b,
       "syncQN4R5b": syncQN4R5b,
       "syncCN4R5bu": syncCN4R5bu,
       "syncFN4R5bu": syncFN4R5bu,
       "syncQN4R5bu": syncQN4R5bu,
       "syncCN4R5du": syncCN4R5du,
       "syncFN4R5du": syncFN4R5du,
       "syncQN4R5du": syncQN4R5du,
       "syncFN5R5du": syncFN5R5du,
       "syncBC4R5b": syncBC4R5b,
       "syncBF4R5b": syncBF4R5b,
       "syncBF3R5b": syncBF3R5b,
       "syncBF5R5b": syncBF5R5b,
       "syncFN3R5du": syncFN3R5du,
       "syncCN3R5du": syncCN3R5du,
       "syncCN5R5du": syncCN5R5du,
       "syncBF3R5": syncBF3R5,
       "syncBC3R5": syncBC3R5,
       "syncBF4R5": syncBF4R5,
       "syncBC4R5": syncBC4R5,
       "syncBF5R5": syncBF5R5,
       "syncBC5R5": syncBC5R5,
       "centralSite": centralSite,
       "syncCN4R2c": syncCN4R2c,
       "syncFN4R2c": syncFN4R2c,
       "syncQN4R2c": syncQN4R2c,
       "syncCN4R3c": syncCN4R3c,
       "syncFN4R3c": syncFN4R3c,
       "syncQN4R3c": syncQN4R3c,
       "syncCN4R4u": syncCN4R4u,
       "syncFN4R4u": syncFN4R4u,
       "syncQN4R4u": syncQN4R4u,
       "oemProducts": oemProducts,
       "threeCom": threeCom,
       "linkConverter": linkConverter,
       "linkConverter2": linkConverter2,
       "lc2EN2port": lc2EN2port,
       "lc2EN4port": lc2EN4port,
       "lc2TR2port": lc2TR2port,
       "lc2TR6port": lc2TR6port,
       "cableTron": cableTron,
       "oemSNACXR2C": oemSNACXR2C,
       "oemSNACXR2W": oemSNACXR2W,
       "oemSNACMR2C": oemSNACMR2C,
       "oemSNACMR2W": oemSNACMR2W,
       "oemSNACMIM2": oemSNACMIM2,
       "oemSNACXR2Q": oemSNACXR2Q,
       "oemSNACMR2Q": oemSNACMR2Q,
       "oemSNACXR3C": oemSNACXR3C,
       "oemSNACXR3W": oemSNACXR3W,
       "oemSNACMR3C": oemSNACMR3C,
       "oemSNACMR3W": oemSNACMR3W,
       "oemSNACXR3Q": oemSNACXR3Q,
       "oemSNACMR3Q": oemSNACMR3Q,
       "oemSNACXR4C": oemSNACXR4C,
       "oemSNACXR4W": oemSNACXR4W,
       "oemSNACMR4C": oemSNACMR4C,
       "oemSNACMR4W": oemSNACMR4W,
       "oemSNACXR4Q": oemSNACXR4Q,
       "oemSNACMR4Q": oemSNACMR4Q,
       "chipcom": chipcom,
       "ibm": ibm,
       "oem2490R22F": oem2490R22F,
       "oem2490R22C": oem2490R22C,
       "oem22181FR4": oem22181FR4,
       "oem22181CR4": oem22181CR4,
       "oem22183FR4": oem22183FR4,
       "oem22183CR4": oem22183CR4,
       "oem22181FR5": oem22181FR5,
       "oem22181CR5": oem22181CR5,
       "oem22183FR5": oem22183FR5,
       "oem22183CR5": oem22183CR5,
       "oem22185FR5": oem22185FR5,
       "oem22185CR5": oem22185CR5,
       "oem22183BF5": oem22183BF5,
       "oem22183BC5": oem22183BC5,
       "oem22184BF5": oem22184BF5,
       "oem22184BC5": oem22184BC5,
       "oem22185BF5": oem22185BF5,
       "oem22185BC5": oem22185BC5,
       "srCommTrapGroup": srCommTrapGroup,
       "commCount": commCount,
       "commTable": commTable,
       "commEntry": commEntry,
       "commIndex": commIndex,
       "commName": commName,
       "commTrap": commTrap,
       "commIPAddr": commIPAddr,
       "commMACAddr": commMACAddr,
       "commAccess": commAccess,
       "srNodeGroup": srNodeGroup,
       "nodeUnitGroup": nodeUnitGroup,
       "unitControlGroup": unitControlGroup,
       "unitRestart": unitRestart,
       "dumpOnRestart": dumpOnRestart,
       "initiateInstall": initiateInstall,
       "initializeStats": initializeStats,
       "clearDump": clearDump,
       "acknowledgeAllStatuses": acknowledgeAllStatuses,
       "consolidatedUnitStatus": consolidatedUnitStatus,
       "homeDialBackup": homeDialBackup,
       "unitStatusGroup": unitStatusGroup,
       "unitModel": unitModel,
       "softwareVersion": softwareVersion,
       "productType": productType,
       "maxPortNumber": maxPortNumber,
       "maxPU": maxPU,
       "maxSession": maxSession,
       "maxDevice": maxDevice,
       "msBoardType": msBoardType,
       "msExtBoardType": msExtBoardType,
       "dumpFileStatus": dumpFileStatus,
       "dumpFileName": dumpFileName,
       "unitSerialNumber": unitSerialNumber,
       "expansionSerialNumber": expansionSerialNumber,
       "romVersion": romVersion,
       "processorType": processorType,
       "chassisSlot": chassisSlot,
       "lastTrapSeqNumber": lastTrapSeqNumber,
       "lastInstallErrCode": lastInstallErrCode,
       "unitPartNumber": unitPartNumber,
       "expansionPartNumber": expansionPartNumber,
       "wan1BoardType": wan1BoardType,
       "wan2BoardType": wan2BoardType,
       "patchId": patchId,
       "unitConfigGroup": unitConfigGroup,
       "unitId": unitId,
       "nmsSerialSpeed": nmsSerialSpeed,
       "serialPortLogoffTimer": serialPortLogoffTimer,
       "callRetryTimer": callRetryTimer,
       "password": password,
       "configPassword": configPassword,
       "dateTimeField": dateTimeField,
       "configId": configId,
       "internalMacAddress": internalMacAddress,
       "internalRingNumber": internalRingNumber,
       "internalBridgeNumber": internalBridgeNumber,
       "internalMacAddress2": internalMacAddress2,
       "internalRingNumber2": internalRingNumber2,
       "associatedPortNumber2": associatedPortNumber2,
       "associatedDLCI2": associatedDLCI2,
       "internalMacAddress3": internalMacAddress3,
       "internalRingNumber3": internalRingNumber3,
       "associatedPortNumber3": associatedPortNumber3,
       "associatedDLCI3": associatedDLCI3,
       "internalMacAddress4": internalMacAddress4,
       "internalRingNumber4": internalRingNumber4,
       "associatedPortNumber4": associatedPortNumber4,
       "associatedDLCI4": associatedDLCI4,
       "ipInactivityTimer": ipInactivityTimer,
       "excessBurstGovernor": excessBurstGovernor,
       "measurementPeriod": measurementPeriod,
       "markDEBit": markDEBit,
       "unitStatisticsGroup": unitStatisticsGroup,
       "numberSamples": numberSamples,
       "systemBufferFreeCounts": systemBufferFreeCounts,
       "cpuIdleSumCounts": cpuIdleSumCounts,
       "nodeNetViewPUGroup": nodeNetViewPUGroup,
       "netViewPUStatusGroup": netViewPUStatusGroup,
       "netviewConnectionStatus": netviewConnectionStatus,
       "netviewLastClearCode": netviewLastClearCode,
       "netviewAltConnectionStatus": netviewAltConnectionStatus,
       "netviewAltLastClearCode": netviewAltLastClearCode,
       "netviewConnectionAttemptCount": netviewConnectionAttemptCount,
       "netviewAltConnectionAttemptCount": netviewAltConnectionAttemptCount,
       "netviewStatusIgnored": netviewStatusIgnored,
       "netviewStatusAcknowledged": netviewStatusAcknowledged,
       "netviewAltStatusIgnored": netviewAltStatusIgnored,
       "netviewAltStatusAcknowledged": netviewAltStatusAcknowledged,
       "netViewPUConfigGroup": netViewPUConfigGroup,
       "netviewPUXID": netviewPUXID,
       "alternateNetviewPUXID": alternateNetviewPUXID,
       "netviewConnectID": netviewConnectID,
       "alternateNetviewConnectID": alternateNetviewConnectID,
       "netviewSpecialConnect": netviewSpecialConnect,
       "alternateNetviewSpecialConnect": alternateNetviewSpecialConnect,
       "nodeBridgeGroup": nodeBridgeGroup,
       "bridgeConfigGroup": bridgeConfigGroup,
       "brEnableBridging": brEnableBridging,
       "bridgePriority": bridgePriority,
       "brMaxAge": brMaxAge,
       "brHelloTimer": brHelloTimer,
       "brFilterIPX": brFilterIPX,
       "brFilterIP": brFilterIP,
       "brFilterNetBIOS": brFilterNetBIOS,
       "brFilterLLC2": brFilterLLC2,
       "brFilterSMAN": brFilterSMAN,
       "brForwardOther": brForwardOther,
       "brIPXtargetPort": brIPXtargetPort,
       "brIPXtargetDLCI": brIPXtargetDLCI,
       "brIPtargetPort": brIPtargetPort,
       "brIPtargetDLCI": brIPtargetDLCI,
       "brNetBIOStargetPort": brNetBIOStargetPort,
       "brNetBIOStargetDLCI": brNetBIOStargetDLCI,
       "brLLC2targetPort": brLLC2targetPort,
       "brLLC2targetDLCI": brLLC2targetDLCI,
       "brOthertargetPort": brOthertargetPort,
       "brOthertargetDLCI": brOthertargetDLCI,
       "brSerialPriority": brSerialPriority,
       "brTerminatedLLC2Priority": brTerminatedLLC2Priority,
       "brLLC2Priority": brLLC2Priority,
       "brIPXPriority": brIPXPriority,
       "brIPPriority": brIPPriority,
       "brNetBIOSPriority": brNetBIOSPriority,
       "brOtherPriority": brOtherPriority,
       "brHighPriorityBandwidth": brHighPriorityBandwidth,
       "brMediumPriorityBandwidth": brMediumPriorityBandwidth,
       "brLowPriorityBandwidth": brLowPriorityBandwidth,
       "brDelayTimer": brDelayTimer,
       "brEnableIPXBridging": brEnableIPXBridging,
       "brEnableIPBridging": brEnableIPBridging,
       "brEnableNetBiosBridging": brEnableNetBiosBridging,
       "brEnableSNABridging": brEnableSNABridging,
       "brEnableSyncManBridging": brEnableSyncManBridging,
       "brEnableOtherBridging": brEnableOtherBridging,
       "bridgeStatsGroup": bridgeStatsGroup,
       "ipxStatsTable": ipxStatsTable,
       "ipxStatsEntry": ipxStatsEntry,
       "ipxStatsIndex": ipxStatsIndex,
       "ipxRipRcvdFwdInterval": ipxRipRcvdFwdInterval,
       "ipxRipRcvdFiltInterval": ipxRipRcvdFiltInterval,
       "ipxSapRcvdFwdInterval": ipxSapRcvdFwdInterval,
       "ipxSapRcvdFiltInterval": ipxSapRcvdFiltInterval,
       "nodeLANGroup": nodeLANGroup,
       "lanControlGroup": lanControlGroup,
       "lanControlTable": lanControlTable,
       "lanControlEntry": lanControlEntry,
       "lanControlIndex": lanControlIndex,
       "lanControlType": lanControlType,
       "lanStatus": lanStatus,
       "lanControlFailureCode": lanControlFailureCode,
       "lanControlNAUName": lanControlNAUName,
       "lanStatusIgnored": lanStatusIgnored,
       "lanStatusAcknowledged": lanStatusAcknowledged,
       "lanTokenRingGroup": lanTokenRingGroup,
       "lanPortTable": lanPortTable,
       "lanPortEntry": lanPortEntry,
       "lanPortIndex": lanPortIndex,
       "lanPortType": lanPortType,
       "lanMACAddress": lanMACAddress,
       "lanPROMMACAddress": lanPROMMACAddress,
       "lanSpeed": lanSpeed,
       "lanT1Timer": lanT1Timer,
       "lanT2Timer": lanT2Timer,
       "lanTiTimer": lanTiTimer,
       "lanRxWindowSize": lanRxWindowSize,
       "lanTxWindowSize": lanTxWindowSize,
       "lanMaxRetries": lanMaxRetries,
       "lanRingNumber": lanRingNumber,
       "lanBridgeNumber": lanBridgeNumber,
       "lanEthernetFrameFormat": lanEthernetFrameFormat,
       "lanSendLocalTest": lanSendLocalTest,
       "lanBroadcastType": lanBroadcastType,
       "lanIPAddress": lanIPAddress,
       "lanNetworkMask": lanNetworkMask,
       "lanDefaultGateway": lanDefaultGateway,
       "lanNAUName": lanNAUName,
       "lanInterfaceType": lanInterfaceType,
       "lanIPEthernetFrameType": lanIPEthernetFrameType,
       "lanInitState": lanInitState,
       "lanSecondDefaultGateway": lanSecondDefaultGateway,
       "lanRIPUpdtTimer": lanRIPUpdtTimer,
       "lanRIPAge": lanRIPAge,
       "lanSAPUpdtTimer": lanSAPUpdtTimer,
       "lanSAPAge": lanSAPAge,
       "lanRSM": lanRSM,
       "nodeLineGroup": nodeLineGroup,
       "lineControlGroup": lineControlGroup,
       "lineControlTable": lineControlTable,
       "lineControlEntry": lineControlEntry,
       "lineControlIndex": lineControlIndex,
       "lineControlType": lineControlType,
       "lineStatus": lineStatus,
       "lineControlFailureCode": lineControlFailureCode,
       "lineControlNAUName": lineControlNAUName,
       "lineStatusIgnored": lineStatusIgnored,
       "lineStatusAcknowledged": lineStatusAcknowledged,
       "loopbackTest": loopbackTest,
       "linePhysicalGroup": linePhysicalGroup,
       "linePhysicalTable": linePhysicalTable,
       "linePhysicalEntry": linePhysicalEntry,
       "linePhysicalIndex": linePhysicalIndex,
       "linePhysicalType": linePhysicalType,
       "lineEIAStatus": lineEIAStatus,
       "lineQualityFrameCount": lineQualityFrameCount,
       "lineQualityCRCErrors": lineQualityCRCErrors,
       "lineQualityAborts": lineQualityAborts,
       "lineInterfaceType": lineInterfaceType,
       "lineCableType": lineCableType,
       "lineSwitchedConnection": lineSwitchedConnection,
       "isdnControlGroup": isdnControlGroup,
       "isdndeviceConfigTable": isdndeviceConfigTable,
       "isdndeviceConfigEntry": isdndeviceConfigEntry,
       "isdnLineIndex": isdnLineIndex,
       "serviceType": serviceType,
       "isdnSpeed": isdnSpeed,
       "connectionTimeOut": connectionTimeOut,
       "nosConnectAttempts": nosConnectAttempts,
       "farEndNumberType": farEndNumberType,
       "farEndNumberPlan": farEndNumberPlan,
       "farEndNumber": farEndNumber,
       "localNumberType": localNumberType,
       "localNumberPlan": localNumberPlan,
       "localNumber": localNumber,
       "spid": spid,
       "isdndeviceStatsTable": isdndeviceStatsTable,
       "isdndeviceStatsEntry": isdndeviceStatsEntry,
       "isdnIndex": isdnIndex,
       "channelID": channelID,
       "kbytesTransmitted": kbytesTransmitted,
       "kbytesReceived": kbytesReceived,
       "packetsTransmitted": packetsTransmitted,
       "packetsReceived": packetsReceived,
       "isdnloopbackbytesTransmitted": isdnloopbackbytesTransmitted,
       "isdnloopbackbytesReceived": isdnloopbackbytesReceived,
       "isdnCRCErrors": isdnCRCErrors,
       "dsucsuControlGroup": dsucsuControlGroup,
       "dsucsudeviceConfigTable": dsucsudeviceConfigTable,
       "dsucsudeviceConfigEntry": dsucsudeviceConfigEntry,
       "dsucsuLineNumber": dsucsuLineNumber,
       "dsucsuType": dsucsuType,
       "dsucsuClocking": dsucsuClocking,
       "dsucsuSpeed": dsucsuSpeed,
       "dsucsudeviceStatsTable": dsucsudeviceStatsTable,
       "dsucsudeviceStatsEntry": dsucsudeviceStatsEntry,
       "dsucsuLine": dsucsuLine,
       "dsucsuloopbackbytesTransmitted": dsucsuloopbackbytesTransmitted,
       "dsucsuloopbackbytesReceived": dsucsuloopbackbytesReceived,
       "lineSDLCGroup": lineSDLCGroup,
       "sdlcConfigTable": sdlcConfigTable,
       "sdlcConfigEntry": sdlcConfigEntry,
       "sdlcConfigPortIndex": sdlcConfigPortIndex,
       "sdlcConfigType": sdlcConfigType,
       "sdlcInitState": sdlcInitState,
       "sdlcCarrier": sdlcCarrier,
       "sdlcClocking": sdlcClocking,
       "sdlcSpeed": sdlcSpeed,
       "sdlcPause": sdlcPause,
       "sdlcNRZI": sdlcNRZI,
       "sdlcT1Timer": sdlcT1Timer,
       "sdlcSlowPollTimer": sdlcSlowPollTimer,
       "sdlcMaxRetries": sdlcMaxRetries,
       "sdlcNAUName": sdlcNAUName,
       "sdlcMultiFlagInsertion": sdlcMultiFlagInsertion,
       "sdlcCTS": sdlcCTS,
       "sdlcDCD": sdlcDCD,
       "sdlcDSR": sdlcDSR,
       "sdlcDTR": sdlcDTR,
       "sdlcRTS": sdlcRTS,
       "sdlcReturnClock": sdlcReturnClock,
       "sdlcStatsTable": sdlcStatsTable,
       "sdlcStatsEntry": sdlcStatsEntry,
       "sdlcStatsPortIndex": sdlcStatsPortIndex,
       "sdlcPortType": sdlcPortType,
       "sdlcInOctets": sdlcInOctets,
       "sdlcOutOctets": sdlcOutOctets,
       "sdlcInFrames": sdlcInFrames,
       "sdlcOutFrames": sdlcOutFrames,
       "sdlcOverruns": sdlcOverruns,
       "sdlcCRCErrors": sdlcCRCErrors,
       "sdlcRecvAborts": sdlcRecvAborts,
       "sdlcpollrsptimeouts": sdlcpollrsptimeouts,
       "sdlciframetrans": sdlciframetrans,
       "lineBisyncGroup": lineBisyncGroup,
       "bisyncConfigTable": bisyncConfigTable,
       "bisyncConfigEntry": bisyncConfigEntry,
       "bisyncConfigPortIndex": bisyncConfigPortIndex,
       "bisyncConfigType": bisyncConfigType,
       "bisyncNAUName": bisyncNAUName,
       "bisyncInitState": bisyncInitState,
       "bisyncCarrier": bisyncCarrier,
       "bisyncClocking": bisyncClocking,
       "bisyncSpeed": bisyncSpeed,
       "bisyncPause": bisyncPause,
       "bisyncReplyTimer": bisyncReplyTimer,
       "bisyncRetries": bisyncRetries,
       "bisyncSlowpollTimer": bisyncSlowpollTimer,
       "bisyncSessTerm": bisyncSessTerm,
       "bisyncIBS": bisyncIBS,
       "bisyncCTS": bisyncCTS,
       "bisyncDCD": bisyncDCD,
       "bisyncDSR": bisyncDSR,
       "bisyncDTR": bisyncDTR,
       "bisyncRTS": bisyncRTS,
       "bisyncReturnClock": bisyncReturnClock,
       "bisyncStatsTable": bisyncStatsTable,
       "bisyncStatsEntry": bisyncStatsEntry,
       "bisyncStatsPortIndex": bisyncStatsPortIndex,
       "bisyncPortType": bisyncPortType,
       "bisyncInOctets": bisyncInOctets,
       "bisyncOutOctets": bisyncOutOctets,
       "bisyncOverruns": bisyncOverruns,
       "bisyncCRCErrors": bisyncCRCErrors,
       "bisyncRcvTimeout": bisyncRcvTimeout,
       "bisyncXmtTimeout": bisyncXmtTimeout,
       "lineFrameRelayGroup": lineFrameRelayGroup,
       "frameRelayConfigTable": frameRelayConfigTable,
       "frameRelayConfigEntry": frameRelayConfigEntry,
       "frameRelayConfigPortIndex": frameRelayConfigPortIndex,
       "frameRelayPortType": frameRelayPortType,
       "frameRelayInitState": frameRelayInitState,
       "frameRelayClocking": frameRelayClocking,
       "frameRelaySpeed": frameRelaySpeed,
       "frameRelayLocalManagementProtocol": frameRelayLocalManagementProtocol,
       "frameRelayLinkPollingTimer": frameRelayLinkPollingTimer,
       "frameRelayFullStatusPollingCount": frameRelayFullStatusPollingCount,
       "frameRelayT1Timer": frameRelayT1Timer,
       "frameRelayT2Timer": frameRelayT2Timer,
       "frameRelayTiTimer": frameRelayTiTimer,
       "frameRelayRxWindowSize": frameRelayRxWindowSize,
       "frameRelayTxWindowSize": frameRelayTxWindowSize,
       "frameRelayMaxRetries": frameRelayMaxRetries,
       "frameRelayNAUName": frameRelayNAUName,
       "frameRelayVirtualMACAddress": frameRelayVirtualMACAddress,
       "frameRelayVirtualRingNumber": frameRelayVirtualRingNumber,
       "frameRelayVirtualBridgeNumber": frameRelayVirtualBridgeNumber,
       "frameRelayIPAddress": frameRelayIPAddress,
       "frameRelayNetworkMask": frameRelayNetworkMask,
       "frameRelayDefaultGatewayAddress": frameRelayDefaultGatewayAddress,
       "frameRelaySessSwitchThreshold": frameRelaySessSwitchThreshold,
       "frameRelaySwitchedBackup": frameRelaySwitchedBackup,
       "frameRelaySwitchedLineWaitTimer": frameRelaySwitchedLineWaitTimer,
       "frameRelayDedLineWaitTimer": frameRelayDedLineWaitTimer,
       "frameRelayCommittedBurst": frameRelayCommittedBurst,
       "frameRelayExcessBurst": frameRelayExcessBurst,
       "frameRelayBridgingProtocol": frameRelayBridgingProtocol,
       "frameRelayProxyARP": frameRelayProxyARP,
       "frameRelaySecondDefaultGatewayAddress": frameRelaySecondDefaultGatewayAddress,
       "frameRelayAlternateIPAddress": frameRelayAlternateIPAddress,
       "frameRelayAlternateNetmask": frameRelayAlternateNetmask,
       "frameRelayLLC2FrameFormat": frameRelayLLC2FrameFormat,
       "frameRelayMultiflagSeparation": frameRelayMultiflagSeparation,
       "frameRelayRestrictTerminateSessUsage": frameRelayRestrictTerminateSessUsage,
       "frameRelayRIPUpdtTimer": frameRelayRIPUpdtTimer,
       "frameRelayRIPAge": frameRelayRIPAge,
       "frameRelaySAPUpdtTimer": frameRelaySAPUpdtTimer,
       "frameRelaySAPAge": frameRelaySAPAge,
       "frameRelayRSM": frameRelayRSM,
       "frameRelayARP": frameRelayARP,
       "frameRelayCTS": frameRelayCTS,
       "frameRelayDCD": frameRelayDCD,
       "frameRelayDSR": frameRelayDSR,
       "frameRelayDTR": frameRelayDTR,
       "frameRelayRTS": frameRelayRTS,
       "frameRelayReturnClock": frameRelayReturnClock,
       "frameRelayStatsTable": frameRelayStatsTable,
       "frameRelayStatsEntry": frameRelayStatsEntry,
       "frameRelayStatsPortIndex": frameRelayStatsPortIndex,
       "frameRelayInOctets": frameRelayInOctets,
       "frameRelayOutOctets": frameRelayOutOctets,
       "frameRelaySampleDuration": frameRelaySampleDuration,
       "frameRelayOverruns": frameRelayOverruns,
       "frameRelayCRCErrors": frameRelayCRCErrors,
       "frameRelayRecvAborts": frameRelayRecvAborts,
       "frameRelayTxDe": frameRelayTxDe,
       "frameRelayRxDe": frameRelayRxDe,
       "frameRelaySwitchedAttempts": frameRelaySwitchedAttempts,
       "frameRelaySwitchedAttemptsSuccessful": frameRelaySwitchedAttemptsSuccessful,
       "lineAsyncGroup": lineAsyncGroup,
       "asyncConfigTable": asyncConfigTable,
       "asyncConfigEntry": asyncConfigEntry,
       "asyncConfigPortIndex": asyncConfigPortIndex,
       "asyncConfigType": asyncConfigType,
       "asyncNAUName": asyncNAUName,
       "asyncInitState": asyncInitState,
       "asyncCarrier": asyncCarrier,
       "asyncSpeed": asyncSpeed,
       "asyncPhysicalType": asyncPhysicalType,
       "asyncStopBits": asyncStopBits,
       "asyncParity": asyncParity,
       "asyncDataBits": asyncDataBits,
       "asyncIdleTimer": asyncIdleTimer,
       "asyncTxFrameGap": asyncTxFrameGap,
       "asyncRxForwardingCount": asyncRxForwardingCount,
       "asyncEiaSignalForwarding": asyncEiaSignalForwarding,
       "asyncAddressOffset": asyncAddressOffset,
       "asyncRTC": asyncRTC,
       "asyncCTS": asyncCTS,
       "asyncDCD": asyncDCD,
       "asyncDSR": asyncDSR,
       "asyncDTR": asyncDTR,
       "asyncRTS": asyncRTS,
       "asyncReturnClock": asyncReturnClock,
       "asyncOrt": asyncOrt,
       "asyncStatsTable": asyncStatsTable,
       "asyncStatsEntry": asyncStatsEntry,
       "asyncStatsPortIndex": asyncStatsPortIndex,
       "asyncPortType": asyncPortType,
       "asyncInOctets": asyncInOctets,
       "asyncOutOctets": asyncOutOctets,
       "asyncInMessages": asyncInMessages,
       "asyncOutMessages": asyncOutMessages,
       "asyncInMsgDiscarded": asyncInMsgDiscarded,
       "asyncOutMsgDiscarded": asyncOutMsgDiscarded,
       "asyncXmtFailures": asyncXmtFailures,
       "asyncRcvMsgForwarded": asyncRcvMsgForwarded,
       "asyncRcvMsgErrors": asyncRcvMsgErrors,
       "asyncRcvCharsDiscarded": asyncRcvCharsDiscarded,
       "asyncRcvParityErrors": asyncRcvParityErrors,
       "asyncRcvFramingErrors": asyncRcvFramingErrors,
       "asyncRcvFifoOverruns": asyncRcvFifoOverruns,
       "asyncRcvCharsOverruns": asyncRcvCharsOverruns,
       "asyncRcvBreakConditions": asyncRcvBreakConditions,
       "lineBisyncRjeGroup": lineBisyncRjeGroup,
       "bisyncrjeConfigTable": bisyncrjeConfigTable,
       "bisyncrjeConfigEntry": bisyncrjeConfigEntry,
       "bisyncrjeConfigPortIndex": bisyncrjeConfigPortIndex,
       "bisyncrjeConfigType": bisyncrjeConfigType,
       "bisyncrjeNAUName": bisyncrjeNAUName,
       "bisyncrjeInitState": bisyncrjeInitState,
       "bisyncrjeCarrier": bisyncrjeCarrier,
       "bisyncrjeClocking": bisyncrjeClocking,
       "bisyncrjeSpeed": bisyncrjeSpeed,
       "bisyncrjeReplyTimer": bisyncrjeReplyTimer,
       "bisyncrjeRetries": bisyncrjeRetries,
       "bisyncrjeCodeSet": bisyncrjeCodeSet,
       "bisyncrjeCTS": bisyncrjeCTS,
       "bisyncrjeDCD": bisyncrjeDCD,
       "bisyncrjeDSR": bisyncrjeDSR,
       "bisyncrjeDTR": bisyncrjeDTR,
       "bisyncrjeRTS": bisyncrjeRTS,
       "bisyncrjeReturnClock": bisyncrjeReturnClock,
       "bisyncrjeStatsTable": bisyncrjeStatsTable,
       "bisyncrjeStatsEntry": bisyncrjeStatsEntry,
       "bisyncrjeStatsPortIndex": bisyncrjeStatsPortIndex,
       "bisyncrjePortType": bisyncrjePortType,
       "bisyncrjeInChrs": bisyncrjeInChrs,
       "bisyncrjeOutChrs": bisyncrjeOutChrs,
       "bisyncrjeInTrns": bisyncrjeInTrns,
       "bisyncrjeOutTrns": bisyncrjeOutTrns,
       "bisyncrjeInRetr": bisyncrjeInRetr,
       "bisyncrjeOutRetr": bisyncrjeOutRetr,
       "bisyncrjeInEnq": bisyncrjeInEnq,
       "bisyncrjeOutEnq": bisyncrjeOutEnq,
       "bisyncrjeInEtb": bisyncrjeInEtb,
       "bisyncrjeOutEtb": bisyncrjeOutEtb,
       "bisyncrjeInEtx": bisyncrjeInEtx,
       "bisyncrjeOutEtx": bisyncrjeOutEtx,
       "bisyncrjeWack": bisyncrjeWack,
       "bisyncrjeRvi": bisyncrjeRvi,
       "lineDialBackupGroup": lineDialBackupGroup,
       "dialbackupConfigTable": dialbackupConfigTable,
       "dialbackupConfigEntry": dialbackupConfigEntry,
       "dialbackupConfigPortIndex": dialbackupConfigPortIndex,
       "dialbackupPortType": dialbackupPortType,
       "dialbackupConnectType": dialbackupConnectType,
       "dialbackupFirstDedicatedPort": dialbackupFirstDedicatedPort,
       "dialbackupassociatedDLCIDedicated": dialbackupassociatedDLCIDedicated,
       "dialbackupSecondDedicatedPort": dialbackupSecondDedicatedPort,
       "dialbackupassociatedDLCISecond": dialbackupassociatedDLCISecond,
       "dialbackupDedicatedPort": dialbackupDedicatedPort,
       "dialbackupDedicatedLMIPort": dialbackupDedicatedLMIPort,
       "dialbackupDialInactivityTimer": dialbackupDialInactivityTimer,
       "dialbackupDialSuspendTimer": dialbackupDialSuspendTimer,
       "dialbackupModemInitString": dialbackupModemInitString,
       "dialbackupModemDialString": dialbackupModemDialString,
       "dialbackupModemHangString": dialbackupModemHangString,
       "dialbackupDialDelayTimer": dialbackupDialDelayTimer,
       "dialbackupTreatLLCControlCharacters": dialbackupTreatLLCControlCharacters,
       "dialbackupStatsTable": dialbackupStatsTable,
       "dialbackupStatsEntry": dialbackupStatsEntry,
       "dialbackupStatsPortIndex": dialbackupStatsPortIndex,
       "dialbackupSuccatmpt": dialbackupSuccatmpt,
       "dialbackupunsuccatmpt": dialbackupunsuccatmpt,
       "dialbackupinact": dialbackupinact,
       "lineX25Group": lineX25Group,
       "x25ConfigTable": x25ConfigTable,
       "x25ConfigEntry": x25ConfigEntry,
       "x25ConfigPortIndex": x25ConfigPortIndex,
       "x25ConfigType": x25ConfigType,
       "x25NAUName": x25NAUName,
       "x25InitState": x25InitState,
       "x25Clocking": x25Clocking,
       "x25DTEAddress": x25DTEAddress,
       "x25LinkWindowSize": x25LinkWindowSize,
       "x25T1Timer": x25T1Timer,
       "x25MaxRetries": x25MaxRetries,
       "x25PortSpeed": x25PortSpeed,
       "x25ReceiveWindowSize": x25ReceiveWindowSize,
       "x25TransmitWindowSize": x25TransmitWindowSize,
       "x25ReceivePacketSize": x25ReceivePacketSize,
       "x25TransmitPacketSize": x25TransmitPacketSize,
       "x25LowTwoWayChannel": x25LowTwoWayChannel,
       "x25HighTwoWayChannel": x25HighTwoWayChannel,
       "x25UseCallingAddress": x25UseCallingAddress,
       "x25ForwardingUnit": x25ForwardingUnit,
       "x25DevicePacketSize": x25DevicePacketSize,
       "x25DeviceWindowSize": x25DeviceWindowSize,
       "x25PlaceReverseChargeCalls": x25PlaceReverseChargeCalls,
       "x25AcceptReverseChargeCalls": x25AcceptReverseChargeCalls,
       "x25NPS": x25NPS,
       "x25CTS": x25CTS,
       "x25DCD": x25DCD,
       "x25DSR": x25DSR,
       "x25DTR": x25DTR,
       "x25RTS": x25RTS,
       "x25ReturnClock": x25ReturnClock,
       "x25IPAddress": x25IPAddress,
       "x25NetworkMask": x25NetworkMask,
       "x25DefaultGatewayAddress": x25DefaultGatewayAddress,
       "x25SecondDefaultGatewayAddress": x25SecondDefaultGatewayAddress,
       "x25StatsTable": x25StatsTable,
       "x25StatsEntry": x25StatsEntry,
       "x25StatsPortIndex": x25StatsPortIndex,
       "x25PortType": x25PortType,
       "x25InFrames": x25InFrames,
       "x25OutFrames": x25OutFrames,
       "x25CInFrames": x25CInFrames,
       "x25COutFrames": x25COutFrames,
       "x25FRMRInFrames": x25FRMRInFrames,
       "x25FRMROutFrames": x25FRMROutFrames,
       "x25Timeouts": x25Timeouts,
       "x25UFrames": x25UFrames,
       "x25Samples": x25Samples,
       "x25Sum": x25Sum,
       "x25SumsQ": x25SumsQ,
       "x25DataInPkts": x25DataInPkts,
       "x25DataOutPkts": x25DataOutPkts,
       "x25DataInChrs": x25DataInChrs,
       "x25DataOutChrs": x25DataOutChrs,
       "x25QInPkts": x25QInPkts,
       "x25QOutPkts": x25QOutPkts,
       "x25QInChrs": x25QInChrs,
       "x25QOutChrs": x25QOutChrs,
       "x25SigInPkts": x25SigInPkts,
       "x25SigOutPkts": x25SigOutPkts,
       "x25InResets": x25InResets,
       "x25OutResets": x25OutResets,
       "x25InRestarts": x25InRestarts,
       "x25OutRestarts": x25OutRestarts,
       "lineAlcGroup": lineAlcGroup,
       "alcConfigTable": alcConfigTable,
       "alcConfigEntry": alcConfigEntry,
       "alcConfigPortIndex": alcConfigPortIndex,
       "alcConfigType": alcConfigType,
       "alcNAUName": alcNAUName,
       "alcInitState": alcInitState,
       "alcClocking": alcClocking,
       "alcPortSpeed": alcPortSpeed,
       "alcLimitSegsCharsBetweenPolls": alcLimitSegsCharsBetweenPolls,
       "alcNumberOfSegments": alcNumberOfSegments,
       "alcNumberOfCharacters": alcNumberOfCharacters,
       "alcNumberOfNullSeg": alcNumberOfNullSeg,
       "alcCTS": alcCTS,
       "alcDCD": alcDCD,
       "alcDSR": alcDSR,
       "alcDTR": alcDTR,
       "alcRTS": alcRTS,
       "alcReturnClock": alcReturnClock,
       "alcStatsTable": alcStatsTable,
       "alcStatsEntry": alcStatsEntry,
       "alcStatsPortIndex": alcStatsPortIndex,
       "alcPortType": alcPortType,
       "alcRxOverruns": alcRxOverruns,
       "alcBytesRx": alcBytesRx,
       "alcBytesTx": alcBytesTx,
       "alcBytesRxDisc": alcBytesRxDisc,
       "alcBytesTxDisc": alcBytesTxDisc,
       "alcPortFaults": alcPortFaults,
       "alcRcvCCCErrors": alcRcvCCCErrors,
       "alcPollTx": alcPollTx,
       "alcResponseTimeouts": alcResponseTimeouts,
       "alcSegRx": alcSegRx,
       "alcSegTx": alcSegTx,
       "alcSegRxDisc": alcSegRxDisc,
       "alcSegTxDisc": alcSegTxDisc,
       "nodePUGroup": nodePUGroup,
       "puControlGroup": puControlGroup,
       "puControlTable": puControlTable,
       "puControlEntry": puControlEntry,
       "puControlLineIndex": puControlLineIndex,
       "puControlPUAddress": puControlPUAddress,
       "puStatus": puStatus,
       "puConnectionStatus": puConnectionStatus,
       "puLastClearCode": puLastClearCode,
       "puControlFailureCode": puControlFailureCode,
       "puControlNAUName": puControlNAUName,
       "puConnectionAttemptCount": puConnectionAttemptCount,
       "puStatusIgnored": puStatusIgnored,
       "puStatusAcknowledged": puStatusAcknowledged,
       "puLastDlciCleared": puLastDlciCleared,
       "puCurrentDlci": puCurrentDlci,
       "puLastMACCleared": puLastMACCleared,
       "puCurrentMAC": puCurrentMAC,
       "puNetworkType": puNetworkType,
       "puCurrentConnectionType": puCurrentConnectionType,
       "puLastSVCCleared": puLastSVCCleared,
       "puCurrentSVC": puCurrentSVC,
       "puLastLocalDTECleared": puLastLocalDTECleared,
       "puLastRemoteDTECleared": puLastRemoteDTECleared,
       "puCurrentLocalDTE": puCurrentLocalDTE,
       "puCurrentRemoteDTE": puCurrentRemoteDTE,
       "puIsDynamic": puIsDynamic,
       "puSDLCGroup": puSDLCGroup,
       "sdlcPuConfigTable": sdlcPuConfigTable,
       "sdlcPuConfigEntry": sdlcPuConfigEntry,
       "sdlcPuConfigLineIndex": sdlcPuConfigLineIndex,
       "sdlcPuConfigAddress": sdlcPuConfigAddress,
       "sdlcPuNAUName": sdlcPuNAUName,
       "sdlcPuInitialState": sdlcPuInitialState,
       "sdlcPuXID": sdlcPuXID,
       "sdlcPuType": sdlcPuType,
       "sdlcPuGroupPollAddress": sdlcPuGroupPollAddress,
       "sdlcPuConnectionID": sdlcPuConnectionID,
       "sdlcPuMAXOUT": sdlcPuMAXOUT,
       "sdlcPuConnectType": sdlcPuConnectType,
       "sdlcPuStatsTable": sdlcPuStatsTable,
       "sdlcPuStatsEntry": sdlcPuStatsEntry,
       "sdlcPuStatsLineIndex": sdlcPuStatsLineIndex,
       "sdlcPuStatsAddress": sdlcPuStatsAddress,
       "sdlcPuInIFrames": sdlcPuInIFrames,
       "sdlcPuOutIFrames": sdlcPuOutIFrames,
       "sdlcPuInRRFrames": sdlcPuInRRFrames,
       "sdlcPuOutRRFrames": sdlcPuOutRRFrames,
       "sdlcPuInRNRFrames": sdlcPuInRNRFrames,
       "sdlcPuOutRNRFrames": sdlcPuOutRNRFrames,
       "sdlcPuInXIDFrames": sdlcPuInXIDFrames,
       "sdlcPuOutXIDFrames": sdlcPuOutXIDFrames,
       "sdlcPuInTESTFrames": sdlcPuInTESTFrames,
       "sdlcPuOutTESTFrames": sdlcPuOutTESTFrames,
       "sdlcPuInSNRMFrames": sdlcPuInSNRMFrames,
       "sdlcPuOutSNRMFrames": sdlcPuOutSNRMFrames,
       "sdlcPuInDISCFrames": sdlcPuInDISCFrames,
       "sdlcPuOutDISCFrames": sdlcPuOutDISCFrames,
       "sdlcPuInDMFrames": sdlcPuInDMFrames,
       "sdlcPuOutDMFrames": sdlcPuOutDMFrames,
       "sdlcPuInUAFrames": sdlcPuInUAFrames,
       "sdlcPuOutUAFrames": sdlcPuOutUAFrames,
       "sdlcPuInFRMRFrames": sdlcPuInFRMRFrames,
       "sdlcPuOutFRMRFrames": sdlcPuOutFRMRFrames,
       "sdlcPuInRDFrames": sdlcPuInRDFrames,
       "sdlcPuOutRDFrames": sdlcPuOutRDFrames,
       "sdlcPuInUIFrames": sdlcPuInUIFrames,
       "sdlcPuOutUIFrames": sdlcPuOutUIFrames,
       "sdlcPuReTxIFrames": sdlcPuReTxIFrames,
       "sdlcPuPollResponseTimeouts": sdlcPuPollResponseTimeouts,
       "puBisyncGroup": puBisyncGroup,
       "bisyncPuConfigTable": bisyncPuConfigTable,
       "bisyncPuConfigEntry": bisyncPuConfigEntry,
       "bisyncPuConfigLineIndex": bisyncPuConfigLineIndex,
       "bisyncPuConfigAddress": bisyncPuConfigAddress,
       "bisyncPuNAUName": bisyncPuNAUName,
       "bisyncPuInitialState": bisyncPuInitialState,
       "bisyncPuXID": bisyncPuXID,
       "bisyncPuTargetHostType": bisyncPuTargetHostType,
       "bisyncPuMaxData": bisyncPuMaxData,
       "bisyncPuConnectionID": bisyncPuConnectionID,
       "bisyncPuConnectType": bisyncPuConnectType,
       "bisyncPuStatsTable": bisyncPuStatsTable,
       "bisyncPuStatsEntry": bisyncPuStatsEntry,
       "bisyncPuStatsLineIndex": bisyncPuStatsLineIndex,
       "bisyncPuStatsAddress": bisyncPuStatsAddress,
       "bisyncPuInTransactions": bisyncPuInTransactions,
       "bisyncPuOutTransactions": bisyncPuOutTransactions,
       "bisyncPuSlowPolls": bisyncPuSlowPolls,
       "bisyncPuPolls": bisyncPuPolls,
       "puMappingGroup": puMappingGroup,
       "mappingPuConfigTable": mappingPuConfigTable,
       "mappingPuConfigEntry": mappingPuConfigEntry,
       "mappingPuConfigLineIndex": mappingPuConfigLineIndex,
       "mappingPuConfigAddress": mappingPuConfigAddress,
       "mappingPuSourceSAP": mappingPuSourceSAP,
       "mappingPuDestinationSAP": mappingPuDestinationSAP,
       "mappingPuDestinationMAC": mappingPuDestinationMAC,
       "mappingPuPartnerConfigLineIndex": mappingPuPartnerConfigLineIndex,
       "mappingPuPartnerConfigAddress": mappingPuPartnerConfigAddress,
       "mappingPuPartnerSourceSAP": mappingPuPartnerSourceSAP,
       "mappingPuPartnerDestSAP": mappingPuPartnerDestSAP,
       "mappingPuPartnerDestMAC": mappingPuPartnerDestMAC,
       "mappingPuNAU": mappingPuNAU,
       "mappingPuConnectID": mappingPuConnectID,
       "mappingPuXID": mappingPuXID,
       "mappingPuDirectDLCI": mappingPuDirectDLCI,
       "mappingPuLastClearCode": mappingPuLastClearCode,
       "mappingPuConnAttemptCnt": mappingPuConnAttemptCnt,
       "mappingPuPartnerLastClearCode": mappingPuPartnerLastClearCode,
       "mappingPuPartnerConnAttemptCnt": mappingPuPartnerConnAttemptCnt,
       "puAsyncGroup": puAsyncGroup,
       "asyncPuConfigTable": asyncPuConfigTable,
       "asyncPuConfigEntry": asyncPuConfigEntry,
       "asyncPuConfigLineIndex": asyncPuConfigLineIndex,
       "asyncPuConfigAddress": asyncPuConfigAddress,
       "asyncPuNAUName": asyncPuNAUName,
       "asyncPuInitialState": asyncPuInitialState,
       "asyncPuXID": asyncPuXID,
       "asyncPuConnectionID": asyncPuConnectionID,
       "asyncPuConnectType": asyncPuConnectType,
       "asyncPuDeviceRangeLow": asyncPuDeviceRangeLow,
       "asyncPuDeviceRangeHigh": asyncPuDeviceRangeHigh,
       "asyncPuStatsTable": asyncPuStatsTable,
       "asyncPuStatsEntry": asyncPuStatsEntry,
       "asyncPuStatsLineIndex": asyncPuStatsLineIndex,
       "asyncPuStatsAddress": asyncPuStatsAddress,
       "asyncPuInChars": asyncPuInChars,
       "asyncPuOutChars": asyncPuOutChars,
       "asyncPuInMessages": asyncPuInMessages,
       "asyncPuOutMessages": asyncPuOutMessages,
       "puLanGroup": puLanGroup,
       "lanPuConfigTable": lanPuConfigTable,
       "lanPuConfigEntry": lanPuConfigEntry,
       "lanPuConfigLineIndex": lanPuConfigLineIndex,
       "lanPuConfigAddress": lanPuConfigAddress,
       "lanPuNAUName": lanPuNAUName,
       "lanPuXID": lanPuXID,
       "lanPuConnectionID": lanPuConnectionID,
       "lanPuSourceSAP": lanPuSourceSAP,
       "lanPuDestinationSAP": lanPuDestinationSAP,
       "lanPuMAC": lanPuMAC,
       "lanPuAlternateMACAddress": lanPuAlternateMACAddress,
       "puRemoteGroup": puRemoteGroup,
       "remotePuConfigTable": remotePuConfigTable,
       "remotePuConfigEntry": remotePuConfigEntry,
       "accessPuConfigLineIndex": accessPuConfigLineIndex,
       "accessPuConfigAddress": accessPuConfigAddress,
       "remotePuConfigLineIndex": remotePuConfigLineIndex,
       "remotePuConfigAddress": remotePuConfigAddress,
       "remotePuSourceSAP": remotePuSourceSAP,
       "remotePuDestinationSAP": remotePuDestinationSAP,
       "remotePuMAC": remotePuMAC,
       "remotePuPrimaryDLCI": remotePuPrimaryDLCI,
       "remotePuParallelDLCI": remotePuParallelDLCI,
       "remotePuAlternateDLCI": remotePuAlternateDLCI,
       "remotePuAlternateMACAddress": remotePuAlternateMACAddress,
       "remotePuTransmitPriority": remotePuTransmitPriority,
       "remotePuBroadcastAllDLCI": remotePuBroadcastAllDLCI,
       "remotePuLocalDTE": remotePuLocalDTE,
       "remotePuRemoteDTE": remotePuRemoteDTE,
       "puX25Group": puX25Group,
       "x25PuConfigTable": x25PuConfigTable,
       "x25PuConfigEntry": x25PuConfigEntry,
       "x25PuConfigLineIndex": x25PuConfigLineIndex,
       "x25PuConfigAddress": x25PuConfigAddress,
       "x25PuNAUName": x25PuNAUName,
       "x25PuConnectionID": x25PuConnectionID,
       "x25PuXID": x25PuXID,
       "x25PuSolicitXID": x25PuSolicitXID,
       "x25PuSourceAddress": x25PuSourceAddress,
       "x25PuRemoteDTEAddress": x25PuRemoteDTEAddress,
       "puAlcGroup": puAlcGroup,
       "alcPuConfigTable": alcPuConfigTable,
       "alcPuConfigEntry": alcPuConfigEntry,
       "alcPuConfigLineIndex": alcPuConfigLineIndex,
       "alcPuConfigAddress": alcPuConfigAddress,
       "alcPuNAUName": alcPuNAUName,
       "alcPuCSS": alcPuCSS,
       "alcPuConnectionID": alcPuConnectionID,
       "alcPuXID": alcPuXID,
       "alcPuConnectType": alcPuConnectType,
       "alcPuLineNumber": alcPuLineNumber,
       "alcPuMaximumFastPoll": alcPuMaximumFastPoll,
       "alcPuMinimumFastPoll": alcPuMinimumFastPoll,
       "alcPuMaximumSlowPollInterval": alcPuMaximumSlowPollInterval,
       "alcPuMinimumSlowPollInterval": alcPuMinimumSlowPollInterval,
       "alcPuResponseTimeout": alcPuResponseTimeout,
       "alcPuUserData": alcPuUserData,
       "alcSourceDTEAddress": alcSourceDTEAddress,
       "alcDestinationDTEAddress": alcDestinationDTEAddress,
       "alcPuStatsTable": alcPuStatsTable,
       "alcPuStatsEntry": alcPuStatsEntry,
       "alcPuStatsLineIndex": alcPuStatsLineIndex,
       "alcPuStatsAddress": alcPuStatsAddress,
       "alcPuPolls": alcPuPolls,
       "alcPuDeviceFaults": alcPuDeviceFaults,
       "alcPuBytesRcv": alcPuBytesRcv,
       "alcPuBytesXmit": alcPuBytesXmit,
       "alcPuSegRcv": alcPuSegRcv,
       "alcPuSegXmit": alcPuSegXmit,
       "puBisyncRjeGroup": puBisyncRjeGroup,
       "bisyncrjePuConfigTable": bisyncrjePuConfigTable,
       "bisyncrjePuConfigEntry": bisyncrjePuConfigEntry,
       "bisyncrjePuConfigLineIndex": bisyncrjePuConfigLineIndex,
       "bisyncrjePuConfigAddress": bisyncrjePuConfigAddress,
       "bisyncrjePuNAUName": bisyncrjePuNAUName,
       "bisyncrjePuInitialState": bisyncrjePuInitialState,
       "bisyncrjePuConnectionID": bisyncrjePuConnectionID,
       "bisyncrjePuXID": bisyncrjePuXID,
       "bisyncrjePuConnectType": bisyncrjePuConnectType,
       "nodeDeviceGroup": nodeDeviceGroup,
       "deviceControlGroup": deviceControlGroup,
       "deviceControlTable": deviceControlTable,
       "deviceControlEntry": deviceControlEntry,
       "deviceControlIndex": deviceControlIndex,
       "deviceControlCUIndex": deviceControlCUIndex,
       "deviceControlAddress": deviceControlAddress,
       "deviceStatus": deviceStatus,
       "deviceControlFailureCode": deviceControlFailureCode,
       "deviceBSCGroup": deviceBSCGroup,
       "deviceConfigTable": deviceConfigTable,
       "deviceConfigEntry": deviceConfigEntry,
       "deviceConfigLineIndex": deviceConfigLineIndex,
       "deviceConfigCUIndex": deviceConfigCUIndex,
       "deviceConfigAddress": deviceConfigAddress,
       "deviceConfigType": deviceConfigType,
       "deviceStatsTable": deviceStatsTable,
       "deviceStatsEntry": deviceStatsEntry,
       "bscDeviceLineIndex": bscDeviceLineIndex,
       "bscDeviceCUIndex": bscDeviceCUIndex,
       "bscDeviceAddress": bscDeviceAddress,
       "bscDeviceInTransactions": bscDeviceInTransactions,
       "bscDeviceOutTransactions": bscDeviceOutTransactions,
       "bscDeviceSumCount": bscDeviceSumCount,
       "bscDeviceResponseDelaySum": bscDeviceResponseDelaySum,
       "bscDeviceResponseDelaySqSum": bscDeviceResponseDelaySqSum,
       "deviceALCGroup": deviceALCGroup,
       "alcdeviceConfigTable": alcdeviceConfigTable,
       "alcdeviceConfigEntry": alcdeviceConfigEntry,
       "alcdeviceConfigLineIndex": alcdeviceConfigLineIndex,
       "alcdeviceConfigCUIndex": alcdeviceConfigCUIndex,
       "alcdeviceConfigAddress": alcdeviceConfigAddress,
       "alcdeviceConfigType": alcdeviceConfigType,
       "nodeT7Group": nodeT7Group,
       "t7ConfigGroup": t7ConfigGroup,
       "t7ConfigTable": t7ConfigTable,
       "t7ConfigEntry": t7ConfigEntry,
       "t7ConfigIndex": t7ConfigIndex,
       "t7ProtocolEnabled": t7ProtocolEnabled,
       "t7PortSpeed": t7PortSpeed,
       "t7StopBits": t7StopBits,
       "t7PortParity": t7PortParity,
       "t7DataBits": t7DataBits,
       "t7IdleTimer": t7IdleTimer,
       "t7PortTxFrameGap": t7PortTxFrameGap,
       "t7RxForwardingCount": t7RxForwardingCount,
       "t7PortIPAddress": t7PortIPAddress,
       "t7UDPPortNumber": t7UDPPortNumber,
       "t7StatsGroup": t7StatsGroup,
       "t7StatsTable": t7StatsTable,
       "t7StatsEntry": t7StatsEntry,
       "t7StatsIndex": t7StatsIndex,
       "t7InOctets": t7InOctets,
       "t7OutOctets": t7OutOctets,
       "t7InMessages": t7InMessages,
       "t7OutMessages": t7OutMessages,
       "t7InMsgDiscarded": t7InMsgDiscarded,
       "t7OutMsgDiscarded": t7OutMsgDiscarded,
       "t7XmtFailures": t7XmtFailures,
       "t7RcvMsgForwarded": t7RcvMsgForwarded,
       "t7RcvMsgErrors": t7RcvMsgErrors,
       "t7RcvCharsDiscarded": t7RcvCharsDiscarded,
       "t7RcvParityErrors": t7RcvParityErrors,
       "t7RcvFramingErrors": t7RcvFramingErrors,
       "t7RcvFifoOverruns": t7RcvFifoOverruns,
       "t7RcvCharsOverruns": t7RcvCharsOverruns,
       "t7RcvBreakConditions": t7RcvBreakConditions,
       "nodeFrCirGroup": nodeFrCirGroup,
       "frExtCircuitTable": frExtCircuitTable,
       "frExtCircuitEntry": frExtCircuitEntry,
       "frExtCircuitIfIndex": frExtCircuitIfIndex,
       "frExtCircuitDlci": frExtCircuitDlci,
       "frExtCircuitStatusIgnored": frExtCircuitStatusIgnored,
       "frExtCircuitStatusAcknowledged": frExtCircuitStatusAcknowledged,
       "frExtCircuitPartnerId": frExtCircuitPartnerId,
       "frExtCircuitTxDe": frExtCircuitTxDe,
       "frExtCircuitRxDe": frExtCircuitRxDe,
       "frExtCircuitMinBits": frExtCircuitMinBits,
       "frExtCircuitMaxBits": frExtCircuitMaxBits,
       "frExtCircuitQOctets": frExtCircuitQOctets,
       "nodeSlipGroup": nodeSlipGroup,
       "slipConfigGroup": slipConfigGroup,
       "slipConfigTable": slipConfigTable,
       "slipConfigEntry": slipConfigEntry,
       "slipConfigIndex": slipConfigIndex,
       "slipProtocolEnabled": slipProtocolEnabled,
       "slipPortSpeed": slipPortSpeed,
       "slipStopBits": slipStopBits,
       "slipIdleTimer": slipIdleTimer,
       "slipPortIPAddress": slipPortIPAddress,
       "slipUsage": slipUsage,
       "slipNetworkMask": slipNetworkMask,
       "slipDefaultGateway": slipDefaultGateway,
       "slipEnableRIP": slipEnableRIP,
       "slipStatsGroup": slipStatsGroup,
       "slipStatsTable": slipStatsTable,
       "slipStatsEntry": slipStatsEntry,
       "slipStatsIndex": slipStatsIndex,
       "slipInChrs": slipInChrs,
       "slipOutChrs": slipOutChrs,
       "slipInMessages": slipInMessages,
       "slipOutMessages": slipOutMessages,
       "slipInMsgDiscarded": slipInMsgDiscarded,
       "slipOutMsgDiscarded": slipOutMsgDiscarded,
       "slipXmtFailures": slipXmtFailures,
       "slipRcvMsgForwarded": slipRcvMsgForwarded,
       "slipRcvMsgErrors": slipRcvMsgErrors,
       "slipRcvCharsDiscarded": slipRcvCharsDiscarded,
       "slipRcvParityErrors": slipRcvParityErrors,
       "slipRcvFramingErrors": slipRcvFramingErrors,
       "slipRcvFifoOverruns": slipRcvFifoOverruns,
       "slipRcvCharsOverruns": slipRcvCharsOverruns,
       "slipRcvBreakConditions": slipRcvBreakConditions,
       "nodeIpxGroup": nodeIpxGroup,
       "ipxConfigGroup": ipxConfigGroup,
       "ipxEnableRouting": ipxEnableRouting,
       "ipxRoutedTxPriority": ipxRoutedTxPriority,
       "ipxEnableRipBroadcast": ipxEnableRipBroadcast,
       "ipxEnableSapBroadcast": ipxEnableSapBroadcast,
       "ipxEnableNetBIOS": ipxEnableNetBIOS,
       "ipxGlobalNodeId": ipxGlobalNodeId,
       "nodeIpGroup": nodeIpGroup,
       "ipConfigGroup": ipConfigGroup,
       "priIPHelperAddress": priIPHelperAddress,
       "secIPHelperAddress": secIPHelperAddress,
       "internalIPAddr": internalIPAddr,
       "internalIPNetmask": internalIPNetmask,
       "enableIpRouting": enableIpRouting,
       "enableIpBridging": enableIpBridging,
       "enableRipBroadcast": enableRipBroadcast}
)
