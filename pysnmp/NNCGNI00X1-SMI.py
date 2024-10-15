# SNMP MIB module (NNCGNI00X1-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NNCGNI00X1-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:13 2024
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

_Newbridge_ObjectIdentity = ObjectIdentity
newbridge = _Newbridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123)
)
_NncDeviceIDs_ObjectIdentity = ObjectIdentity
nncDeviceIDs = _NncDeviceIDs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 1)
)
_NncStandalone_ObjectIdentity = ObjectIdentity
nncStandalone = _NncStandalone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 1, 1)
)
_Nnc8230_ObjectIdentity = ObjectIdentity
nnc8230 = _Nnc8230_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 1, 1, 1)
)
_Nnc3604_ObjectIdentity = ObjectIdentity
nnc3604 = _Nnc3604_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 1, 1, 2)
)
_Nnc8231_ObjectIdentity = ObjectIdentity
nnc8231 = _Nnc8231_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 1, 1, 3)
)
_Nnc8251_ObjectIdentity = ObjectIdentity
nnc8251 = _Nnc8251_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 1, 1, 4)
)
_Nnc3601_ObjectIdentity = ObjectIdentity
nnc3601 = _Nnc3601_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 1, 1, 5)
)
_NncIntegral_ObjectIdentity = ObjectIdentity
nncIntegral = _NncIntegral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 1, 2)
)
_NncITB_ObjectIdentity = ObjectIdentity
nncITB = _NncITB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 1, 2, 1)
)
_NncInterimMib_ObjectIdentity = ObjectIdentity
nncInterimMib = _NncInterimMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 2)
)
_NncExtensions_ObjectIdentity = ObjectIdentity
nncExtensions = _NncExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3)
)
_NncExtSystem_ObjectIdentity = ObjectIdentity
nncExtSystem = _NncExtSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 1)
)
_NncExtEnvironmental_ObjectIdentity = ObjectIdentity
nncExtEnvironmental = _NncExtEnvironmental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 2)
)
_NncExtRestart_ObjectIdentity = ObjectIdentity
nncExtRestart = _NncExtRestart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 3)
)
_NncExtCodeSpace_ObjectIdentity = ObjectIdentity
nncExtCodeSpace = _NncExtCodeSpace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 4)
)
_NncExtNVM_ObjectIdentity = ObjectIdentity
nncExtNVM = _NncExtNVM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 5)
)
_NncExtAlarm_ObjectIdentity = ObjectIdentity
nncExtAlarm = _NncExtAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 6)
)
_NncExtNetSynch_ObjectIdentity = ObjectIdentity
nncExtNetSynch = _NncExtNetSynch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 7)
)
_NncExtPosition_ObjectIdentity = ObjectIdentity
nncExtPosition = _NncExtPosition_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 8)
)
_NncExtDevice_ObjectIdentity = ObjectIdentity
nncExtDevice = _NncExtDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 9)
)
_NncExtDs1_ObjectIdentity = ObjectIdentity
nncExtDs1 = _NncExtDs1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 10)
)
_NncExtRptr_ObjectIdentity = ObjectIdentity
nncExtRptr = _NncExtRptr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 11)
)
_NncExtProbe_ObjectIdentity = ObjectIdentity
nncExtProbe = _NncExtProbe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 12)
)
_NncExtDiag_ObjectIdentity = ObjectIdentity
nncExtDiag = _NncExtDiag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 13)
)
_NncExtSyncDataCct_ObjectIdentity = ObjectIdentity
nncExtSyncDataCct = _NncExtSyncDataCct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 14)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NNCGNI00X1-SMI",
    **{"newbridge": newbridge,
       "nncDeviceIDs": nncDeviceIDs,
       "nncStandalone": nncStandalone,
       "nnc8230": nnc8230,
       "nnc3604": nnc3604,
       "nnc8231": nnc8231,
       "nnc8251": nnc8251,
       "nnc3601": nnc3601,
       "nncIntegral": nncIntegral,
       "nncITB": nncITB,
       "nncInterimMib": nncInterimMib,
       "nncExtensions": nncExtensions,
       "nncExtSystem": nncExtSystem,
       "nncExtEnvironmental": nncExtEnvironmental,
       "nncExtRestart": nncExtRestart,
       "nncExtCodeSpace": nncExtCodeSpace,
       "nncExtNVM": nncExtNVM,
       "nncExtAlarm": nncExtAlarm,
       "nncExtNetSynch": nncExtNetSynch,
       "nncExtPosition": nncExtPosition,
       "nncExtDevice": nncExtDevice,
       "nncExtDs1": nncExtDs1,
       "nncExtRptr": nncExtRptr,
       "nncExtProbe": nncExtProbe,
       "nncExtDiag": nncExtDiag,
       "nncExtSyncDataCct": nncExtSyncDataCct}
)
