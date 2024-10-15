# SNMP MIB module (ZYXEL-ES-CAPWAP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-ES-CAPWAP
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:39 2024
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
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

esCAPWAP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CapwapInfo_ObjectIdentity = ObjectIdentity
capwapInfo = _CapwapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 1)
)
if mibBuilder.loadTexts:
    capwapInfo.setStatus("current")
_CapwapOnlineAP_Type = Integer32
_CapwapOnlineAP_Object = MibScalar
capwapOnlineAP = _CapwapOnlineAP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 1, 1),
    _CapwapOnlineAP_Type()
)
capwapOnlineAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapOnlineAP.setStatus("current")
_CapwapOfflineAP_Type = Integer32
_CapwapOfflineAP_Object = MibScalar
capwapOfflineAP = _CapwapOfflineAP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 1, 2),
    _CapwapOfflineAP_Type()
)
capwapOfflineAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapOfflineAP.setStatus("current")
_CapwapUnMgntAP_Type = Integer32
_CapwapUnMgntAP_Object = MibScalar
capwapUnMgntAP = _CapwapUnMgntAP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 1, 3),
    _CapwapUnMgntAP_Type()
)
capwapUnMgntAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapUnMgntAP.setStatus("current")
_CapwapTotalStation_Type = Integer32
_CapwapTotalStation_Object = MibScalar
capwapTotalStation = _CapwapTotalStation_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 1, 4),
    _CapwapTotalStation_Type()
)
capwapTotalStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapTotalStation.setStatus("current")
_CapwapTraps_ObjectIdentity = ObjectIdentity
capwapTraps = _CapwapTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 2)
)
if mibBuilder.loadTexts:
    capwapTraps.setStatus("current")


class _CapwapTrapsControl_Type(Integer32):
    """Custom type capwapTrapsControl based on Integer32"""
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


_CapwapTrapsControl_Type.__name__ = "Integer32"
_CapwapTrapsControl_Object = MibScalar
capwapTrapsControl = _CapwapTrapsControl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 2, 1),
    _CapwapTrapsControl_Type()
)
capwapTrapsControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapTrapsControl.setStatus("current")
_CapwapTrapsItems_ObjectIdentity = ObjectIdentity
capwapTrapsItems = _CapwapTrapsItems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 2, 2)
)
if mibBuilder.loadTexts:
    capwapTrapsItems.setStatus("current")

# Managed Objects groups


# Notification objects

capwapWTPOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    capwapWTPOnline.setStatus(
        "current"
    )

capwapWTPOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    capwapWTPOffline.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-ES-CAPWAP",
    **{"esCAPWAP": esCAPWAP,
       "capwapInfo": capwapInfo,
       "capwapOnlineAP": capwapOnlineAP,
       "capwapOfflineAP": capwapOfflineAP,
       "capwapUnMgntAP": capwapUnMgntAP,
       "capwapTotalStation": capwapTotalStation,
       "capwapTraps": capwapTraps,
       "capwapTrapsControl": capwapTrapsControl,
       "capwapTrapsItems": capwapTrapsItems,
       "capwapWTPOnline": capwapWTPOnline,
       "capwapWTPOffline": capwapWTPOffline}
)
