# SNMP MIB module (GEN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GEN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:51 2024
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

_Lannet_ObjectIdentity = ObjectIdentity
lannet = _Lannet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81)
)
_LntOID_ObjectIdentity = ObjectIdentity
lntOID = _LntOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17)
)
_LBoxOID_ObjectIdentity = ObjectIdentity
lBoxOID = _LBoxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 1)
)
_LUnknownBoxOID_ObjectIdentity = ObjectIdentity
lUnknownBoxOID = _LUnknownBoxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 1, 1)
)
_LLET18BoxOID_ObjectIdentity = ObjectIdentity
lLET18BoxOID = _LLET18BoxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 1, 2)
)
_LLET3BoxOID_ObjectIdentity = ObjectIdentity
lLET3BoxOID = _LLET3BoxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 1, 3)
)
_LLET36BoxOID_ObjectIdentity = ObjectIdentity
lLET36BoxOID = _LLET36BoxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 1, 4)
)
_LLET18EBoxOID_ObjectIdentity = ObjectIdentity
lLET18EBoxOID = _LLET18EBoxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 1, 5)
)
_LLERT40BoxOID_ObjectIdentity = ObjectIdentity
lLERT40BoxOID = _LLERT40BoxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 1, 6)
)
_LLET10BoxOID_ObjectIdentity = ObjectIdentity
lLET10BoxOID = _LLET10BoxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 1, 7)
)
_LFDX100BoxOID_ObjectIdentity = ObjectIdentity
lFDX100BoxOID = _LFDX100BoxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 1, 8)
)
_LSTACKBoxOID_ObjectIdentity = ObjectIdentity
lSTACKBoxOID = _LSTACKBoxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 1, 9)
)
_LLET20BoxOID_ObjectIdentity = ObjectIdentity
lLET20BoxOID = _LLET20BoxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 1, 10)
)
_LLET36_01_02BoxOID_ObjectIdentity = ObjectIdentity
lLET36_01_02BoxOID = _LLET36_01_02BoxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 1, 11)
)
_VisageBoxOID_ObjectIdentity = ObjectIdentity
visageBoxOID = _VisageBoxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 1, 12)
)
_Visage16155BoxOID_ObjectIdentity = ObjectIdentity
visage16155BoxOID = _Visage16155BoxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 1, 13)
)
_LetM770BoxOID_ObjectIdentity = ObjectIdentity
letM770BoxOID = _LetM770BoxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 1, 14)
)
_M770BoxOID_ObjectIdentity = ObjectIdentity
m770BoxOID = _M770BoxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 1, 15)
)
_M770AtmOID_ObjectIdentity = ObjectIdentity
m770AtmOID = _M770AtmOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 1, 16)
)
_CajunP330OID_ObjectIdentity = ObjectIdentity
cajunP330OID = _CajunP330OID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 1, 17)
)
_CajunP130OID_ObjectIdentity = ObjectIdentity
cajunP130OID = _CajunP130OID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 1, 18)
)
_CajunP360OID_ObjectIdentity = ObjectIdentity
cajunP360OID = _CajunP360OID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 1, 19)
)
_SmartDevicesOID_ObjectIdentity = ObjectIdentity
smartDevicesOID = _SmartDevicesOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 2)
)
_UnknownDeviceOID_ObjectIdentity = ObjectIdentity
unknownDeviceOID = _UnknownDeviceOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 2, 1)
)
_LsaOID_ObjectIdentity = ObjectIdentity
lsaOID = _LsaOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 2, 2)
)
_IasOID_ObjectIdentity = ObjectIdentity
iasOID = _IasOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 2, 3)
)
_Collage530OID_ObjectIdentity = ObjectIdentity
collage530OID = _Collage530OID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 2, 4)
)
_EaxOID_ObjectIdentity = ObjectIdentity
eaxOID = _EaxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 2, 5)
)
_LsfOID_ObjectIdentity = ObjectIdentity
lsfOID = _LsfOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 2, 6)
)
_Lsa2OID_ObjectIdentity = ObjectIdentity
lsa2OID = _Lsa2OID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 2, 7)
)
_MmlsOID_ObjectIdentity = ObjectIdentity
mmlsOID = _MmlsOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 2, 8)
)
_Visage26OID_ObjectIdentity = ObjectIdentity
visage26OID = _Visage26OID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 2, 9)
)
_Lbt155plusOID_ObjectIdentity = ObjectIdentity
lbt155plusOID = _Lbt155plusOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 2, 10)
)
_CajunP120OID_ObjectIdentity = ObjectIdentity
cajunP120OID = _CajunP120OID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 2, 11)
)
_Visage26PlusOID_ObjectIdentity = ObjectIdentity
visage26PlusOID = _Visage26PlusOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 2, 12)
)
_CajunP333ROID_ObjectIdentity = ObjectIdentity
cajunP333ROID = _CajunP333ROID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 2, 13)
)
_CajunP122OID_ObjectIdentity = ObjectIdentity
cajunP122OID = _CajunP122OID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 2, 14)
)
_CajunP330AtmOID_ObjectIdentity = ObjectIdentity
cajunP330AtmOID = _CajunP330AtmOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 2, 15)
)
_DeviceMgr_ObjectIdentity = ObjectIdentity
deviceMgr = _DeviceMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 20)
)
_Probe_ObjectIdentity = ObjectIdentity
probe = _Probe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 22)
)
_Madge_ObjectIdentity = ObjectIdentity
madge = _Madge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GEN-MIB",
    **{"lannet": lannet,
       "lntOID": lntOID,
       "lBoxOID": lBoxOID,
       "lUnknownBoxOID": lUnknownBoxOID,
       "lLET18BoxOID": lLET18BoxOID,
       "lLET3BoxOID": lLET3BoxOID,
       "lLET36BoxOID": lLET36BoxOID,
       "lLET18EBoxOID": lLET18EBoxOID,
       "lLERT40BoxOID": lLERT40BoxOID,
       "lLET10BoxOID": lLET10BoxOID,
       "lFDX100BoxOID": lFDX100BoxOID,
       "lSTACKBoxOID": lSTACKBoxOID,
       "lLET20BoxOID": lLET20BoxOID,
       "lLET36-01-02BoxOID": lLET36_01_02BoxOID,
       "visageBoxOID": visageBoxOID,
       "visage16155BoxOID": visage16155BoxOID,
       "letM770BoxOID": letM770BoxOID,
       "m770BoxOID": m770BoxOID,
       "m770AtmOID": m770AtmOID,
       "cajunP330OID": cajunP330OID,
       "cajunP130OID": cajunP130OID,
       "cajunP360OID": cajunP360OID,
       "smartDevicesOID": smartDevicesOID,
       "unknownDeviceOID": unknownDeviceOID,
       "lsaOID": lsaOID,
       "iasOID": iasOID,
       "collage530OID": collage530OID,
       "eaxOID": eaxOID,
       "lsfOID": lsfOID,
       "lsa2OID": lsa2OID,
       "mmlsOID": mmlsOID,
       "visage26OID": visage26OID,
       "lbt155plusOID": lbt155plusOID,
       "cajunP120OID": cajunP120OID,
       "visage26PlusOID": visage26PlusOID,
       "cajunP333ROID": cajunP333ROID,
       "cajunP122OID": cajunP122OID,
       "cajunP330AtmOID": cajunP330AtmOID,
       "deviceMgr": deviceMgr,
       "probe": probe,
       "madge": madge}
)
