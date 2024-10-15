# SNMP MIB module (RAISECOM-PONSERIES-BASE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RAISECOM-PONSERIES-BASE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:44:29 2024
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

(ponSeries,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "ponSeries")

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

_RaisecomPonCommon_ObjectIdentity = ObjectIdentity
raisecomPonCommon = _RaisecomPonCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 1)
)
_RaisecomEponMgt_ObjectIdentity = ObjectIdentity
raisecomEponMgt = _RaisecomEponMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 2)
)
_RaisecomGponMgt_ObjectIdentity = ObjectIdentity
raisecomGponMgt = _RaisecomGponMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 3)
)
_RaisecomPonDev_ObjectIdentity = ObjectIdentity
raisecomPonDev = _RaisecomPonDev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 4)
)
_Iscom5504B_ObjectIdentity = ObjectIdentity
iscom5504B = _Iscom5504B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 4, 1)
)
_Iscom5600_12_ObjectIdentity = ObjectIdentity
iscom5600_12 = _Iscom5600_12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 4, 2)
)
_Iscom5800_15_ObjectIdentity = ObjectIdentity
iscom5800_15 = _Iscom5800_15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 4, 3)
)
_Iscom5800e_15_ObjectIdentity = ObjectIdentity
iscom5800e_15 = _Iscom5800e_15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 4, 4)
)
_Iscom5508_ObjectIdentity = ObjectIdentity
iscom5508 = _Iscom5508_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 4, 5)
)
_Iscom5800eb_15_ObjectIdentity = ObjectIdentity
iscom5800eb_15 = _Iscom5800eb_15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 4, 6)
)
_Iscom6800_18_ObjectIdentity = ObjectIdentity
iscom6800_18 = _Iscom6800_18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 4, 7)
)
_Rcvs3200_15_ObjectIdentity = ObjectIdentity
rcvs3200_15 = _Rcvs3200_15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 4, 8)
)
_Iscom5504PI_ObjectIdentity = ObjectIdentity
iscom5504PI = _Iscom5504PI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 4, 9)
)
_Iscom5508B_ObjectIdentity = ObjectIdentity
iscom5508B = _Iscom5508B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 4, 10)
)
_Iscom5508GP_ObjectIdentity = ObjectIdentity
iscom5508GP = _Iscom5508GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 4, 11)
)
_Rcvs3100_ObjectIdentity = ObjectIdentity
rcvs3100 = _Rcvs3100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 4, 13)
)
_Iscom5101_ObjectIdentity = ObjectIdentity
iscom5101 = _Iscom5101_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 4, 101)
)
_Iscom5101_FE_ObjectIdentity = ObjectIdentity
iscom5101_FE = _Iscom5101_FE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 4, 102)
)
_Iscom5104_ObjectIdentity = ObjectIdentity
iscom5104 = _Iscom5104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 4, 103)
)
_Iscom5104_AC60_ObjectIdentity = ObjectIdentity
iscom5104_AC60 = _Iscom5104_AC60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 4, 104)
)
_Iscom5104_LM_ObjectIdentity = ObjectIdentity
iscom5104_LM = _Iscom5104_LM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 4, 105)
)
_Iscom5104Q_ObjectIdentity = ObjectIdentity
iscom5104Q = _Iscom5104Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 4, 106)
)
_Iscom5104P_ObjectIdentity = ObjectIdentity
iscom5104P = _Iscom5104P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 4, 107)
)
_Iscom5104_NP_ObjectIdentity = ObjectIdentity
iscom5104_NP = _Iscom5104_NP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 4, 108)
)
_Iscom5104_4E1T1_ObjectIdentity = ObjectIdentity
iscom5104_4E1T1 = _Iscom5104_4E1T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 4, 109)
)
_Iscom5108_ObjectIdentity = ObjectIdentity
iscom5108 = _Iscom5108_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 4, 110)
)
_Iscom5108_PE_ObjectIdentity = ObjectIdentity
iscom5108_PE = _Iscom5108_PE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 4, 111)
)
_Iscom5108_PSE_ObjectIdentity = ObjectIdentity
iscom5108_PSE = _Iscom5108_PSE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 4, 112)
)
_Iscom5116_ObjectIdentity = ObjectIdentity
iscom5116 = _Iscom5116_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 4, 113)
)
_Iscom5116_PE_ObjectIdentity = ObjectIdentity
iscom5116_PE = _Iscom5116_PE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 4, 114)
)
_Iscom5116_4E1T1_ObjectIdentity = ObjectIdentity
iscom5116_4E1T1 = _Iscom5116_4E1T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 4, 115)
)
_Iscom5124_ObjectIdentity = ObjectIdentity
iscom5124 = _Iscom5124_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 4, 116)
)
_Iscom5124S_ObjectIdentity = ObjectIdentity
iscom5124S = _Iscom5124S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 4, 117)
)
_Iscom5204_ObjectIdentity = ObjectIdentity
iscom5204 = _Iscom5204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 4, 118)
)
_Iscom5304_ObjectIdentity = ObjectIdentity
iscom5304 = _Iscom5304_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 4, 119)
)
_Iscom5304D_ObjectIdentity = ObjectIdentity
iscom5304D = _Iscom5304D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 4, 120)
)
_Iscom5208_ObjectIdentity = ObjectIdentity
iscom5208 = _Iscom5208_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 4, 121)
)
_Iscom5216_ObjectIdentity = ObjectIdentity
iscom5216 = _Iscom5216_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 4, 122)
)
_Iscom5224_ObjectIdentity = ObjectIdentity
iscom5224 = _Iscom5224_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 4, 123)
)
_RaisecomSwitchMgt_ObjectIdentity = ObjectIdentity
raisecomSwitchMgt = _RaisecomSwitchMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 5)
)
_RaisecomVideoMgt_ObjectIdentity = ObjectIdentity
raisecomVideoMgt = _RaisecomVideoMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 6)
)
_RaisecomCwdmMgt_ObjectIdentity = ObjectIdentity
raisecomCwdmMgt = _RaisecomCwdmMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18, 7)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-PONSERIES-BASE-MIB",
    **{"raisecomPonCommon": raisecomPonCommon,
       "raisecomEponMgt": raisecomEponMgt,
       "raisecomGponMgt": raisecomGponMgt,
       "raisecomPonDev": raisecomPonDev,
       "iscom5504B": iscom5504B,
       "iscom5600-12": iscom5600_12,
       "iscom5800-15": iscom5800_15,
       "iscom5800e-15": iscom5800e_15,
       "iscom5508": iscom5508,
       "iscom5800eb-15": iscom5800eb_15,
       "iscom6800-18": iscom6800_18,
       "rcvs3200-15": rcvs3200_15,
       "iscom5504PI": iscom5504PI,
       "iscom5508B": iscom5508B,
       "iscom5508GP": iscom5508GP,
       "rcvs3100": rcvs3100,
       "iscom5101": iscom5101,
       "iscom5101-FE": iscom5101_FE,
       "iscom5104": iscom5104,
       "iscom5104-AC60": iscom5104_AC60,
       "iscom5104-LM": iscom5104_LM,
       "iscom5104Q": iscom5104Q,
       "iscom5104P": iscom5104P,
       "iscom5104-NP": iscom5104_NP,
       "iscom5104-4E1T1": iscom5104_4E1T1,
       "iscom5108": iscom5108,
       "iscom5108-PE": iscom5108_PE,
       "iscom5108-PSE": iscom5108_PSE,
       "iscom5116": iscom5116,
       "iscom5116-PE": iscom5116_PE,
       "iscom5116-4E1T1": iscom5116_4E1T1,
       "iscom5124": iscom5124,
       "iscom5124S": iscom5124S,
       "iscom5204": iscom5204,
       "iscom5304": iscom5304,
       "iscom5304D": iscom5304D,
       "iscom5208": iscom5208,
       "iscom5216": iscom5216,
       "iscom5224": iscom5224,
       "raisecomSwitchMgt": raisecomSwitchMgt,
       "raisecomVideoMgt": raisecomVideoMgt,
       "raisecomCwdmMgt": raisecomCwdmMgt}
)
