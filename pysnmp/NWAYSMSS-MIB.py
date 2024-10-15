# SNMP MIB module (NWAYSMSS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NWAYSMSS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:25 2024
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



class AtmPrivateAddrEsi(OctetString):
    """Custom type AtmPrivateAddrEsi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class AtmSelector(OctetString):
    """Custom type AtmSelector based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )





class AtmVccTrafficType(Integer32):
    """Custom type AtmVccTrafficType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bestEffort", 1),
          ("reservedBandwidth", 2))
    )





class Bandwidth(Integer32):
    """Custom type Bandwidth based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_NwaysMSS_ObjectIdentity = ObjectIdentity
nwaysMSS = _NwaysMSS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118)
)
_MssCommon_ObjectIdentity = ObjectIdentity
mssCommon = _MssCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1)
)
_MssCommonHWVPD_ObjectIdentity = ObjectIdentity
mssCommonHWVPD = _MssCommonHWVPD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 1)
)
_MssCmnSrvrs_ObjectIdentity = ObjectIdentity
mssCmnSrvrs = _MssCmnSrvrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2)
)
_MssServerLanE_ObjectIdentity = ObjectIdentity
mssServerLanE = _MssServerLanE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1)
)
_MssCmnClnts_ObjectIdentity = ObjectIdentity
mssCmnClnts = _MssCmnClnts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NWAYSMSS-MIB",
    **{"AtmPrivateAddrEsi": AtmPrivateAddrEsi,
       "AtmSelector": AtmSelector,
       "AtmVccTrafficType": AtmVccTrafficType,
       "Bandwidth": Bandwidth,
       "ibm": ibm,
       "ibmProd": ibmProd,
       "nwaysMSS": nwaysMSS,
       "mssCommon": mssCommon,
       "mssCommonHWVPD": mssCommonHWVPD,
       "mssCmnSrvrs": mssCmnSrvrs,
       "mssServerLanE": mssServerLanE,
       "mssCmnClnts": mssCmnClnts}
)
