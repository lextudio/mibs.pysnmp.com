# SNMP MIB module (HH3C-DOT11-WIDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-DOT11-WIDS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:57 2024
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

(Hh3cDot11ChannelScopeType,
 Hh3cDot11ObjectIDType,
 Hh3cDot11RadioScopeType,
 Hh3cDot11RadioType,
 Hh3cDot11SSIDStringType,
 hh3cDot11) = mibBuilder.importSymbols(
    "HH3C-DOT11-REF-MIB",
    "Hh3cDot11ChannelScopeType",
    "Hh3cDot11ObjectIDType",
    "Hh3cDot11RadioScopeType",
    "Hh3cDot11RadioType",
    "Hh3cDot11SSIDStringType",
    "hh3cDot11")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cDot11WIDS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5)
)
hh3cDot11WIDS.setRevisions(
        ("2010-05-31 18:00",
         "2009-07-29 18:00",
         "2009-05-07 20:00",
         "2008-07-25 19:00",
         "2007-06-19 19:00",
         "2007-05-16 19:00",
         "2006-08-20 19:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cDot11WIDSDevType(Integer32, TextualConvention):
    status = "current"
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
        *(("adhoc", 3),
          ("ap", 2),
          ("client", 1),
          ("unknown", 5),
          ("wirelessBridge", 4))
    )



class Hh3cDot11WIDSDevPermitType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("rogue", 2))
    )



class Hh3cDot11WIDSAtkType(Integer32, TextualConvention):
    status = "current"
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
        *(("act", 1),
          ("asr", 2),
          ("aur", 3),
          ("daf", 4),
          ("dar", 5),
          ("ndf", 6),
          ("pbr", 7),
          ("rar", 8),
          ("saf", 9),
          ("sdf", 10),
          ("unknown", 12),
          ("wiv", 11))
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cDot11WIDSConfigGroup_ObjectIdentity = ObjectIdentity
hh3cDot11WIDSConfigGroup = _Hh3cDot11WIDSConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1)
)
_Hh3cDot11WIDSGlobalConfigGroup_ObjectIdentity = ObjectIdentity
hh3cDot11WIDSGlobalConfigGroup = _Hh3cDot11WIDSGlobalConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 1)
)


class _Hh3cDot11WIDSScanMode_Type(Integer32):
    """Custom type hh3cDot11WIDSScanMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("auto", 2))
    )


_Hh3cDot11WIDSScanMode_Type.__name__ = "Integer32"
_Hh3cDot11WIDSScanMode_Object = MibScalar
hh3cDot11WIDSScanMode = _Hh3cDot11WIDSScanMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 1, 1),
    _Hh3cDot11WIDSScanMode_Type()
)
hh3cDot11WIDSScanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIDSScanMode.setStatus("current")


class _Hh3cDot11WIDSScanChannelList_Type(OctetString):
    """Custom type hh3cDot11WIDSScanChannelList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hh3cDot11WIDSScanChannelList_Type.__name__ = "OctetString"
_Hh3cDot11WIDSScanChannelList_Object = MibScalar
hh3cDot11WIDSScanChannelList = _Hh3cDot11WIDSScanChannelList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 1, 2),
    _Hh3cDot11WIDSScanChannelList_Type()
)
hh3cDot11WIDSScanChannelList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIDSScanChannelList.setStatus("obsolete")


class _Hh3cDot11CntMsrMode_Type(Bits):
    """Custom type hh3cDot11CntMsrMode based on Bits"""
    namedValues = NamedValues(
        *(("adhoc", 1),
          ("config", 2),
          ("rogue", 0))
    )

_Hh3cDot11CntMsrMode_Type.__name__ = "Bits"
_Hh3cDot11CntMsrMode_Object = MibScalar
hh3cDot11CntMsrMode = _Hh3cDot11CntMsrMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 1, 3),
    _Hh3cDot11CntMsrMode_Type()
)
hh3cDot11CntMsrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11CntMsrMode.setStatus("current")


class _Hh3cDot11DevAgingTime_Type(Integer32):
    """Custom type hh3cDot11DevAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1800),
    )


_Hh3cDot11DevAgingTime_Type.__name__ = "Integer32"
_Hh3cDot11DevAgingTime_Object = MibScalar
hh3cDot11DevAgingTime = _Hh3cDot11DevAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 1, 4),
    _Hh3cDot11DevAgingTime_Type()
)
hh3cDot11DevAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11DevAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11DevAgingTime.setUnits("second")
_Hh3cDot11DynBlkListEnable_Type = TruthValue
_Hh3cDot11DynBlkListEnable_Object = MibScalar
hh3cDot11DynBlkListEnable = _Hh3cDot11DynBlkListEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 1, 5),
    _Hh3cDot11DynBlkListEnable_Type()
)
hh3cDot11DynBlkListEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11DynBlkListEnable.setStatus("current")


class _Hh3cDot11DynBlkListLifeTime_Type(Integer32):
    """Custom type hh3cDot11DynBlkListLifeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_Hh3cDot11DynBlkListLifeTime_Type.__name__ = "Integer32"
_Hh3cDot11DynBlkListLifeTime_Object = MibScalar
hh3cDot11DynBlkListLifeTime = _Hh3cDot11DynBlkListLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 1, 6),
    _Hh3cDot11DynBlkListLifeTime_Type()
)
hh3cDot11DynBlkListLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11DynBlkListLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11DynBlkListLifeTime.setUnits("second")
_Hh3cDot11FloodAtkDctEnable_Type = TruthValue
_Hh3cDot11FloodAtkDctEnable_Object = MibScalar
hh3cDot11FloodAtkDctEnable = _Hh3cDot11FloodAtkDctEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 1, 7),
    _Hh3cDot11FloodAtkDctEnable_Type()
)
hh3cDot11FloodAtkDctEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11FloodAtkDctEnable.setStatus("current")
_Hh3cDot11SpoofAtkDctEnable_Type = TruthValue
_Hh3cDot11SpoofAtkDctEnable_Object = MibScalar
hh3cDot11SpoofAtkDctEnable = _Hh3cDot11SpoofAtkDctEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 1, 8),
    _Hh3cDot11SpoofAtkDctEnable_Type()
)
hh3cDot11SpoofAtkDctEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11SpoofAtkDctEnable.setStatus("current")
_Hh3cDot11WeakIVAtkDctEnable_Type = TruthValue
_Hh3cDot11WeakIVAtkDctEnable_Object = MibScalar
hh3cDot11WeakIVAtkDctEnable = _Hh3cDot11WeakIVAtkDctEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 1, 9),
    _Hh3cDot11WeakIVAtkDctEnable_Type()
)
hh3cDot11WeakIVAtkDctEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WeakIVAtkDctEnable.setStatus("current")
_Hh3cDot11ResetWIDSRogueHistory_Type = TruthValue
_Hh3cDot11ResetWIDSRogueHistory_Object = MibScalar
hh3cDot11ResetWIDSRogueHistory = _Hh3cDot11ResetWIDSRogueHistory_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 1, 10),
    _Hh3cDot11ResetWIDSRogueHistory_Type()
)
hh3cDot11ResetWIDSRogueHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11ResetWIDSRogueHistory.setStatus("current")
_Hh3cDot11ResetWIDSHistroy_Type = TruthValue
_Hh3cDot11ResetWIDSHistroy_Object = MibScalar
hh3cDot11ResetWIDSHistroy = _Hh3cDot11ResetWIDSHistroy_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 1, 11),
    _Hh3cDot11ResetWIDSHistroy_Type()
)
hh3cDot11ResetWIDSHistroy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11ResetWIDSHistroy.setStatus("current")
_Hh3cDot11ResetWIDSStatistics_Type = TruthValue
_Hh3cDot11ResetWIDSStatistics_Object = MibScalar
hh3cDot11ResetWIDSStatistics = _Hh3cDot11ResetWIDSStatistics_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 1, 12),
    _Hh3cDot11ResetWIDSStatistics_Type()
)
hh3cDot11ResetWIDSStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11ResetWIDSStatistics.setStatus("current")
_Hh3cDot11ResetAllDynBlkList_Type = TruthValue
_Hh3cDot11ResetAllDynBlkList_Object = MibScalar
hh3cDot11ResetAllDynBlkList = _Hh3cDot11ResetAllDynBlkList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 1, 13),
    _Hh3cDot11ResetAllDynBlkList_Type()
)
hh3cDot11ResetAllDynBlkList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11ResetAllDynBlkList.setStatus("current")
_Hh3cDot11ResetAllStcBlkList_Type = TruthValue
_Hh3cDot11ResetAllStcBlkList_Object = MibScalar
hh3cDot11ResetAllStcBlkList = _Hh3cDot11ResetAllStcBlkList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 1, 14),
    _Hh3cDot11ResetAllStcBlkList_Type()
)
hh3cDot11ResetAllStcBlkList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11ResetAllStcBlkList.setStatus("current")
_Hh3cDot11ResetAllWhtBlkList_Type = TruthValue
_Hh3cDot11ResetAllWhtBlkList_Object = MibScalar
hh3cDot11ResetAllWhtBlkList = _Hh3cDot11ResetAllWhtBlkList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 1, 15),
    _Hh3cDot11ResetAllWhtBlkList_Type()
)
hh3cDot11ResetAllWhtBlkList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11ResetAllWhtBlkList.setStatus("current")
_Hh3cDot11ResetAllDctRogueAP_Type = TruthValue
_Hh3cDot11ResetAllDctRogueAP_Object = MibScalar
hh3cDot11ResetAllDctRogueAP = _Hh3cDot11ResetAllDctRogueAP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 1, 16),
    _Hh3cDot11ResetAllDctRogueAP_Type()
)
hh3cDot11ResetAllDctRogueAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11ResetAllDctRogueAP.setStatus("current")
_Hh3cDot11ResetAllDctRogueSta_Type = TruthValue
_Hh3cDot11ResetAllDctRogueSta_Object = MibScalar
hh3cDot11ResetAllDctRogueSta = _Hh3cDot11ResetAllDctRogueSta_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 1, 17),
    _Hh3cDot11ResetAllDctRogueSta_Type()
)
hh3cDot11ResetAllDctRogueSta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11ResetAllDctRogueSta.setStatus("current")
_Hh3cDot11ResetAllDctAdhoc_Type = TruthValue
_Hh3cDot11ResetAllDctAdhoc_Object = MibScalar
hh3cDot11ResetAllDctAdhoc = _Hh3cDot11ResetAllDctAdhoc_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 1, 18),
    _Hh3cDot11ResetAllDctAdhoc_Type()
)
hh3cDot11ResetAllDctAdhoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11ResetAllDctAdhoc.setStatus("current")
_Hh3cDot11ResetAllDctDevice_Type = TruthValue
_Hh3cDot11ResetAllDctDevice_Object = MibScalar
hh3cDot11ResetAllDctDevice = _Hh3cDot11ResetAllDctDevice_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 1, 19),
    _Hh3cDot11ResetAllDctDevice_Type()
)
hh3cDot11ResetAllDctDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11ResetAllDctDevice.setStatus("current")
_Hh3cDot11ResetAllDctSSID_Type = TruthValue
_Hh3cDot11ResetAllDctSSID_Object = MibScalar
hh3cDot11ResetAllDctSSID = _Hh3cDot11ResetAllDctSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 1, 20),
    _Hh3cDot11ResetAllDctSSID_Type()
)
hh3cDot11ResetAllDctSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11ResetAllDctSSID.setStatus("current")


class _Hh3cDot11WidsFloodInterval_Type(Unsigned32):
    """Custom type hh3cDot11WidsFloodInterval based on Unsigned32"""
    defaultValue = 1


_Hh3cDot11WidsFloodInterval_Object = MibScalar
hh3cDot11WidsFloodInterval = _Hh3cDot11WidsFloodInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 1, 21),
    _Hh3cDot11WidsFloodInterval_Type()
)
hh3cDot11WidsFloodInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WidsFloodInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11WidsFloodInterval.setUnits("second")


class _Hh3cDot11WidsBlackListThreshold_Type(Unsigned32):
    """Custom type hh3cDot11WidsBlackListThreshold based on Unsigned32"""
    defaultValue = 100


_Hh3cDot11WidsBlackListThreshold_Object = MibScalar
hh3cDot11WidsBlackListThreshold = _Hh3cDot11WidsBlackListThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 1, 22),
    _Hh3cDot11WidsBlackListThreshold_Type()
)
hh3cDot11WidsBlackListThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WidsBlackListThreshold.setStatus("current")


class _Hh3cDot11SSIDFilterOnOff_Type(Integer32):
    """Custom type hh3cDot11SSIDFilterOnOff based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Hh3cDot11SSIDFilterOnOff_Type.__name__ = "Integer32"
_Hh3cDot11SSIDFilterOnOff_Object = MibScalar
hh3cDot11SSIDFilterOnOff = _Hh3cDot11SSIDFilterOnOff_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 1, 23),
    _Hh3cDot11SSIDFilterOnOff_Type()
)
hh3cDot11SSIDFilterOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11SSIDFilterOnOff.setStatus("current")


class _Hh3cDot11BSSIDFilterOnOff_Type(Integer32):
    """Custom type hh3cDot11BSSIDFilterOnOff based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Hh3cDot11BSSIDFilterOnOff_Type.__name__ = "Integer32"
_Hh3cDot11BSSIDFilterOnOff_Object = MibScalar
hh3cDot11BSSIDFilterOnOff = _Hh3cDot11BSSIDFilterOnOff_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 1, 24),
    _Hh3cDot11BSSIDFilterOnOff_Type()
)
hh3cDot11BSSIDFilterOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11BSSIDFilterOnOff.setStatus("current")
_Hh3cDot11WIDSPermitVendorTable_Object = MibTable
hh3cDot11WIDSPermitVendorTable = _Hh3cDot11WIDSPermitVendorTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cDot11WIDSPermitVendorTable.setStatus("current")
_Hh3cDot11WIDSPermitVendorEntry_Object = MibTableRow
hh3cDot11WIDSPermitVendorEntry = _Hh3cDot11WIDSPermitVendorEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 2, 1)
)
hh3cDot11WIDSPermitVendorEntry.setIndexNames(
    (0, "HH3C-DOT11-WIDS-MIB", "hh3cDot11VendorOUI"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIDSPermitVendorEntry.setStatus("current")


class _Hh3cDot11VendorOUI_Type(OctetString):
    """Custom type hh3cDot11VendorOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_Hh3cDot11VendorOUI_Type.__name__ = "OctetString"
_Hh3cDot11VendorOUI_Object = MibTableColumn
hh3cDot11VendorOUI = _Hh3cDot11VendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 2, 1, 1),
    _Hh3cDot11VendorOUI_Type()
)
hh3cDot11VendorOUI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11VendorOUI.setStatus("current")
_Hh3cDot11PermitVendorRowStatus_Type = RowStatus
_Hh3cDot11PermitVendorRowStatus_Object = MibTableColumn
hh3cDot11PermitVendorRowStatus = _Hh3cDot11PermitVendorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 2, 1, 2),
    _Hh3cDot11PermitVendorRowStatus_Type()
)
hh3cDot11PermitVendorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11PermitVendorRowStatus.setStatus("current")


class _Hh3cDot11VendorName_Type(OctetString):
    """Custom type hh3cDot11VendorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDot11VendorName_Type.__name__ = "OctetString"
_Hh3cDot11VendorName_Object = MibTableColumn
hh3cDot11VendorName = _Hh3cDot11VendorName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 2, 1, 3),
    _Hh3cDot11VendorName_Type()
)
hh3cDot11VendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11VendorName.setStatus("current")
_Hh3cDot11WIDSPermitSSIDTable_Object = MibTable
hh3cDot11WIDSPermitSSIDTable = _Hh3cDot11WIDSPermitSSIDTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cDot11WIDSPermitSSIDTable.setStatus("current")
_Hh3cDot11WIDSPermitSSIDEntry_Object = MibTableRow
hh3cDot11WIDSPermitSSIDEntry = _Hh3cDot11WIDSPermitSSIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 3, 1)
)
hh3cDot11WIDSPermitSSIDEntry.setIndexNames(
    (0, "HH3C-DOT11-WIDS-MIB", "hh3cDot11PermitSSID"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIDSPermitSSIDEntry.setStatus("current")


class _Hh3cDot11PermitSSID_Type(Hh3cDot11SSIDStringType):
    """Custom type hh3cDot11PermitSSID based on Hh3cDot11SSIDStringType"""
    subtypeSpec = Hh3cDot11SSIDStringType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDot11PermitSSID_Type.__name__ = "Hh3cDot11SSIDStringType"
_Hh3cDot11PermitSSID_Object = MibTableColumn
hh3cDot11PermitSSID = _Hh3cDot11PermitSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 3, 1, 1),
    _Hh3cDot11PermitSSID_Type()
)
hh3cDot11PermitSSID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11PermitSSID.setStatus("current")
_Hh3cDot11PermitSSIDRowStatus_Type = RowStatus
_Hh3cDot11PermitSSIDRowStatus_Object = MibTableColumn
hh3cDot11PermitSSIDRowStatus = _Hh3cDot11PermitSSIDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 3, 1, 2),
    _Hh3cDot11PermitSSIDRowStatus_Type()
)
hh3cDot11PermitSSIDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11PermitSSIDRowStatus.setStatus("current")
_Hh3cDot11PermitSSIDDetected_Type = TruthValue
_Hh3cDot11PermitSSIDDetected_Object = MibTableColumn
hh3cDot11PermitSSIDDetected = _Hh3cDot11PermitSSIDDetected_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 3, 1, 3),
    _Hh3cDot11PermitSSIDDetected_Type()
)
hh3cDot11PermitSSIDDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PermitSSIDDetected.setStatus("current")
_Hh3cDot11WIDSIgnoreListTable_Object = MibTable
hh3cDot11WIDSIgnoreListTable = _Hh3cDot11WIDSIgnoreListTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cDot11WIDSIgnoreListTable.setStatus("current")
_Hh3cDot11WIDSIgnoreListEntry_Object = MibTableRow
hh3cDot11WIDSIgnoreListEntry = _Hh3cDot11WIDSIgnoreListEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 4, 1)
)
hh3cDot11WIDSIgnoreListEntry.setIndexNames(
    (0, "HH3C-DOT11-WIDS-MIB", "hh3cDot11IgnoreMAC"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIDSIgnoreListEntry.setStatus("current")
_Hh3cDot11IgnoreMAC_Type = MacAddress
_Hh3cDot11IgnoreMAC_Object = MibTableColumn
hh3cDot11IgnoreMAC = _Hh3cDot11IgnoreMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 4, 1, 1),
    _Hh3cDot11IgnoreMAC_Type()
)
hh3cDot11IgnoreMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11IgnoreMAC.setStatus("current")
_Hh3cDot11IgnoreListRowStatus_Type = RowStatus
_Hh3cDot11IgnoreListRowStatus_Object = MibTableColumn
hh3cDot11IgnoreListRowStatus = _Hh3cDot11IgnoreListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 4, 1, 2),
    _Hh3cDot11IgnoreListRowStatus_Type()
)
hh3cDot11IgnoreListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11IgnoreListRowStatus.setStatus("current")
_Hh3cDot11IgnoreMACDetected_Type = TruthValue
_Hh3cDot11IgnoreMACDetected_Object = MibTableColumn
hh3cDot11IgnoreMACDetected = _Hh3cDot11IgnoreMACDetected_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 4, 1, 3),
    _Hh3cDot11IgnoreMACDetected_Type()
)
hh3cDot11IgnoreMACDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11IgnoreMACDetected.setStatus("current")
_Hh3cDot11IgnoreDevType_Type = Hh3cDot11WIDSDevType
_Hh3cDot11IgnoreDevType_Object = MibTableColumn
hh3cDot11IgnoreDevType = _Hh3cDot11IgnoreDevType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 4, 1, 4),
    _Hh3cDot11IgnoreDevType_Type()
)
hh3cDot11IgnoreDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11IgnoreDevType.setStatus("current")
_Hh3cDot11WIDSAttackListTable_Object = MibTable
hh3cDot11WIDSAttackListTable = _Hh3cDot11WIDSAttackListTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cDot11WIDSAttackListTable.setStatus("current")
_Hh3cDot11WIDSAttackListEntry_Object = MibTableRow
hh3cDot11WIDSAttackListEntry = _Hh3cDot11WIDSAttackListEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 5, 1)
)
hh3cDot11WIDSAttackListEntry.setIndexNames(
    (0, "HH3C-DOT11-WIDS-MIB", "hh3cDot11AttackDeviceMac"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIDSAttackListEntry.setStatus("current")
_Hh3cDot11AttackDeviceMac_Type = MacAddress
_Hh3cDot11AttackDeviceMac_Object = MibTableColumn
hh3cDot11AttackDeviceMac = _Hh3cDot11AttackDeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 5, 1, 1),
    _Hh3cDot11AttackDeviceMac_Type()
)
hh3cDot11AttackDeviceMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11AttackDeviceMac.setStatus("current")
_Hh3cDot11AttackListRowStatus_Type = RowStatus
_Hh3cDot11AttackListRowStatus_Object = MibTableColumn
hh3cDot11AttackListRowStatus = _Hh3cDot11AttackListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 5, 1, 2),
    _Hh3cDot11AttackListRowStatus_Type()
)
hh3cDot11AttackListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11AttackListRowStatus.setStatus("current")
_Hh3cDot11AttackDevDetected_Type = TruthValue
_Hh3cDot11AttackDevDetected_Object = MibTableColumn
hh3cDot11AttackDevDetected = _Hh3cDot11AttackDevDetected_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 5, 1, 3),
    _Hh3cDot11AttackDevDetected_Type()
)
hh3cDot11AttackDevDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11AttackDevDetected.setStatus("current")
_Hh3cDot11AttackDevType_Type = Hh3cDot11WIDSDevType
_Hh3cDot11AttackDevType_Object = MibTableColumn
hh3cDot11AttackDevType = _Hh3cDot11AttackDevType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 5, 1, 4),
    _Hh3cDot11AttackDevType_Type()
)
hh3cDot11AttackDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11AttackDevType.setStatus("current")
_Hh3cDot11StaticWhiteListTable_Object = MibTable
hh3cDot11StaticWhiteListTable = _Hh3cDot11StaticWhiteListTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 6)
)
if mibBuilder.loadTexts:
    hh3cDot11StaticWhiteListTable.setStatus("current")
_Hh3cDot11StaticWhiteListEntry_Object = MibTableRow
hh3cDot11StaticWhiteListEntry = _Hh3cDot11StaticWhiteListEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 6, 1)
)
hh3cDot11StaticWhiteListEntry.setIndexNames(
    (0, "HH3C-DOT11-WIDS-MIB", "hh3cDot11StaticWhiteListMAC"),
)
if mibBuilder.loadTexts:
    hh3cDot11StaticWhiteListEntry.setStatus("current")
_Hh3cDot11StaticWhiteListMAC_Type = MacAddress
_Hh3cDot11StaticWhiteListMAC_Object = MibTableColumn
hh3cDot11StaticWhiteListMAC = _Hh3cDot11StaticWhiteListMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 6, 1, 1),
    _Hh3cDot11StaticWhiteListMAC_Type()
)
hh3cDot11StaticWhiteListMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11StaticWhiteListMAC.setStatus("current")
_Hh3cDot11StaticWhiteListRowStatus_Type = RowStatus
_Hh3cDot11StaticWhiteListRowStatus_Object = MibTableColumn
hh3cDot11StaticWhiteListRowStatus = _Hh3cDot11StaticWhiteListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 6, 1, 2),
    _Hh3cDot11StaticWhiteListRowStatus_Type()
)
hh3cDot11StaticWhiteListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11StaticWhiteListRowStatus.setStatus("current")
_Hh3cDot11StaticBlackListTable_Object = MibTable
hh3cDot11StaticBlackListTable = _Hh3cDot11StaticBlackListTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 7)
)
if mibBuilder.loadTexts:
    hh3cDot11StaticBlackListTable.setStatus("current")
_Hh3cDot11StaticBlackListEntry_Object = MibTableRow
hh3cDot11StaticBlackListEntry = _Hh3cDot11StaticBlackListEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 7, 1)
)
hh3cDot11StaticBlackListEntry.setIndexNames(
    (0, "HH3C-DOT11-WIDS-MIB", "hh3cDot11StaticBlackListMAC"),
)
if mibBuilder.loadTexts:
    hh3cDot11StaticBlackListEntry.setStatus("current")
_Hh3cDot11StaticBlackListMAC_Type = MacAddress
_Hh3cDot11StaticBlackListMAC_Object = MibTableColumn
hh3cDot11StaticBlackListMAC = _Hh3cDot11StaticBlackListMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 7, 1, 1),
    _Hh3cDot11StaticBlackListMAC_Type()
)
hh3cDot11StaticBlackListMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11StaticBlackListMAC.setStatus("current")
_Hh3cDot11StaticBlackListRowStatus_Type = RowStatus
_Hh3cDot11StaticBlackListRowStatus_Object = MibTableColumn
hh3cDot11StaticBlackListRowStatus = _Hh3cDot11StaticBlackListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 7, 1, 2),
    _Hh3cDot11StaticBlackListRowStatus_Type()
)
hh3cDot11StaticBlackListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11StaticBlackListRowStatus.setStatus("current")
_Hh3cDot11WIDSPermitBSSIDTable_Object = MibTable
hh3cDot11WIDSPermitBSSIDTable = _Hh3cDot11WIDSPermitBSSIDTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 8)
)
if mibBuilder.loadTexts:
    hh3cDot11WIDSPermitBSSIDTable.setStatus("current")
_Hh3cDot11WIDSPermitBSSIDEntry_Object = MibTableRow
hh3cDot11WIDSPermitBSSIDEntry = _Hh3cDot11WIDSPermitBSSIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 8, 1)
)
hh3cDot11WIDSPermitBSSIDEntry.setIndexNames(
    (0, "HH3C-DOT11-WIDS-MIB", "hh3cDot11PermitBSSID"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIDSPermitBSSIDEntry.setStatus("current")
_Hh3cDot11PermitBSSID_Type = MacAddress
_Hh3cDot11PermitBSSID_Object = MibTableColumn
hh3cDot11PermitBSSID = _Hh3cDot11PermitBSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 8, 1, 1),
    _Hh3cDot11PermitBSSID_Type()
)
hh3cDot11PermitBSSID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11PermitBSSID.setStatus("current")
_Hh3cDot11PermitBSSIDDetected_Type = TruthValue
_Hh3cDot11PermitBSSIDDetected_Object = MibTableColumn
hh3cDot11PermitBSSIDDetected = _Hh3cDot11PermitBSSIDDetected_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 8, 1, 2),
    _Hh3cDot11PermitBSSIDDetected_Type()
)
hh3cDot11PermitBSSIDDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PermitBSSIDDetected.setStatus("current")
_Hh3cDot11PermitBSSIDRowStatus_Type = RowStatus
_Hh3cDot11PermitBSSIDRowStatus_Object = MibTableColumn
hh3cDot11PermitBSSIDRowStatus = _Hh3cDot11PermitBSSIDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 1, 8, 1, 3),
    _Hh3cDot11PermitBSSIDRowStatus_Type()
)
hh3cDot11PermitBSSIDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11PermitBSSIDRowStatus.setStatus("current")
_Hh3cDot11WIDSDetectGroup_ObjectIdentity = ObjectIdentity
hh3cDot11WIDSDetectGroup = _Hh3cDot11WIDSDetectGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2)
)
_Hh3cDot11WIDSRogueAPTable_Object = MibTable
hh3cDot11WIDSRogueAPTable = _Hh3cDot11WIDSRogueAPTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11WIDSRogueAPTable.setStatus("current")
_Hh3cDot11WIDSRogueAPEntry_Object = MibTableRow
hh3cDot11WIDSRogueAPEntry = _Hh3cDot11WIDSRogueAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 1, 1)
)
hh3cDot11WIDSRogueAPEntry.setIndexNames(
    (0, "HH3C-DOT11-WIDS-MIB", "hh3cDot11RogueAPBSSMAC"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIDSRogueAPEntry.setStatus("current")
_Hh3cDot11RogueAPBSSMAC_Type = MacAddress
_Hh3cDot11RogueAPBSSMAC_Object = MibTableColumn
hh3cDot11RogueAPBSSMAC = _Hh3cDot11RogueAPBSSMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 1, 1, 1),
    _Hh3cDot11RogueAPBSSMAC_Type()
)
hh3cDot11RogueAPBSSMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RogueAPBSSMAC.setStatus("current")


class _Hh3cDot11RogueAPVendorName_Type(OctetString):
    """Custom type hh3cDot11RogueAPVendorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDot11RogueAPVendorName_Type.__name__ = "OctetString"
_Hh3cDot11RogueAPVendorName_Object = MibTableColumn
hh3cDot11RogueAPVendorName = _Hh3cDot11RogueAPVendorName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 1, 1, 2),
    _Hh3cDot11RogueAPVendorName_Type()
)
hh3cDot11RogueAPVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RogueAPVendorName.setStatus("current")
_Hh3cDot11RogueAPMonitorNum_Type = Integer32
_Hh3cDot11RogueAPMonitorNum_Object = MibTableColumn
hh3cDot11RogueAPMonitorNum = _Hh3cDot11RogueAPMonitorNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 1, 1, 3),
    _Hh3cDot11RogueAPMonitorNum_Type()
)
hh3cDot11RogueAPMonitorNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RogueAPMonitorNum.setStatus("current")
_Hh3cDot11RogueAPFirstDetectTm_Type = TimeTicks
_Hh3cDot11RogueAPFirstDetectTm_Object = MibTableColumn
hh3cDot11RogueAPFirstDetectTm = _Hh3cDot11RogueAPFirstDetectTm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 1, 1, 4),
    _Hh3cDot11RogueAPFirstDetectTm_Type()
)
hh3cDot11RogueAPFirstDetectTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RogueAPFirstDetectTm.setStatus("current")
_Hh3cDot11RogueAPLastDetectTm_Type = TimeTicks
_Hh3cDot11RogueAPLastDetectTm_Object = MibTableColumn
hh3cDot11RogueAPLastDetectTm = _Hh3cDot11RogueAPLastDetectTm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 1, 1, 5),
    _Hh3cDot11RogueAPLastDetectTm_Type()
)
hh3cDot11RogueAPLastDetectTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RogueAPLastDetectTm.setStatus("current")
_Hh3cDot11RogueAPSSID_Type = Hh3cDot11SSIDStringType
_Hh3cDot11RogueAPSSID_Object = MibTableColumn
hh3cDot11RogueAPSSID = _Hh3cDot11RogueAPSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 1, 1, 6),
    _Hh3cDot11RogueAPSSID_Type()
)
hh3cDot11RogueAPSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RogueAPSSID.setStatus("current")
_Hh3cDot11RogueAPMaxSigStrength_Type = Integer32
_Hh3cDot11RogueAPMaxSigStrength_Object = MibTableColumn
hh3cDot11RogueAPMaxSigStrength = _Hh3cDot11RogueAPMaxSigStrength_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 1, 1, 7),
    _Hh3cDot11RogueAPMaxSigStrength_Type()
)
hh3cDot11RogueAPMaxSigStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RogueAPMaxSigStrength.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RogueAPMaxSigStrength.setUnits("dBm")
_Hh3cDot11RogueAPChannel_Type = Hh3cDot11ChannelScopeType
_Hh3cDot11RogueAPChannel_Object = MibTableColumn
hh3cDot11RogueAPChannel = _Hh3cDot11RogueAPChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 1, 1, 8),
    _Hh3cDot11RogueAPChannel_Type()
)
hh3cDot11RogueAPChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RogueAPChannel.setStatus("current")
_Hh3cDot11RogueAPBeaconInterval_Type = Integer32
_Hh3cDot11RogueAPBeaconInterval_Object = MibTableColumn
hh3cDot11RogueAPBeaconInterval = _Hh3cDot11RogueAPBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 1, 1, 9),
    _Hh3cDot11RogueAPBeaconInterval_Type()
)
hh3cDot11RogueAPBeaconInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RogueAPBeaconInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RogueAPBeaconInterval.setUnits("millisecond")
_Hh3cDot11RogueAPAttackedStatus_Type = TruthValue
_Hh3cDot11RogueAPAttackedStatus_Object = MibTableColumn
hh3cDot11RogueAPAttackedStatus = _Hh3cDot11RogueAPAttackedStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 1, 1, 10),
    _Hh3cDot11RogueAPAttackedStatus_Type()
)
hh3cDot11RogueAPAttackedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RogueAPAttackedStatus.setStatus("current")


class _Hh3cDot11RogueAPToIgnore_Type(TruthValue):
    """Custom type hh3cDot11RogueAPToIgnore based on TruthValue"""


_Hh3cDot11RogueAPToIgnore_Object = MibTableColumn
hh3cDot11RogueAPToIgnore = _Hh3cDot11RogueAPToIgnore_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 1, 1, 11),
    _Hh3cDot11RogueAPToIgnore_Type()
)
hh3cDot11RogueAPToIgnore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RogueAPToIgnore.setStatus("current")
_Hh3cDot11RogueAPEncryptStatus_Type = TruthValue
_Hh3cDot11RogueAPEncryptStatus_Object = MibTableColumn
hh3cDot11RogueAPEncryptStatus = _Hh3cDot11RogueAPEncryptStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 1, 1, 12),
    _Hh3cDot11RogueAPEncryptStatus_Type()
)
hh3cDot11RogueAPEncryptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RogueAPEncryptStatus.setStatus("current")
_Hh3cDot11RogueAPReset_Type = TruthValue
_Hh3cDot11RogueAPReset_Object = MibTableColumn
hh3cDot11RogueAPReset = _Hh3cDot11RogueAPReset_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 1, 1, 13),
    _Hh3cDot11RogueAPReset_Type()
)
hh3cDot11RogueAPReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RogueAPReset.setStatus("current")
_Hh3cDot11RogueAPFirstDetectTmStr_Type = OctetString
_Hh3cDot11RogueAPFirstDetectTmStr_Object = MibTableColumn
hh3cDot11RogueAPFirstDetectTmStr = _Hh3cDot11RogueAPFirstDetectTmStr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 1, 1, 14),
    _Hh3cDot11RogueAPFirstDetectTmStr_Type()
)
hh3cDot11RogueAPFirstDetectTmStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RogueAPFirstDetectTmStr.setStatus("current")
_Hh3cDot11RogueAPLastDetectTmStr_Type = OctetString
_Hh3cDot11RogueAPLastDetectTmStr_Object = MibTableColumn
hh3cDot11RogueAPLastDetectTmStr = _Hh3cDot11RogueAPLastDetectTmStr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 1, 1, 15),
    _Hh3cDot11RogueAPLastDetectTmStr_Type()
)
hh3cDot11RogueAPLastDetectTmStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RogueAPLastDetectTmStr.setStatus("current")
_Hh3cDot11WIDSRogueAPExtTable_Object = MibTable
hh3cDot11WIDSRogueAPExtTable = _Hh3cDot11WIDSRogueAPExtTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cDot11WIDSRogueAPExtTable.setStatus("current")
_Hh3cDot11WIDSRogueAPExtEntry_Object = MibTableRow
hh3cDot11WIDSRogueAPExtEntry = _Hh3cDot11WIDSRogueAPExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 2, 1)
)
hh3cDot11WIDSRogueAPExtEntry.setIndexNames(
    (0, "HH3C-DOT11-WIDS-MIB", "hh3cDot11RogueAPBSSMAC"),
    (0, "HH3C-DOT11-WIDS-MIB", "hh3cDot11WIDSAPID"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIDSRogueAPExtEntry.setStatus("current")
_Hh3cDot11WIDSAPID_Type = Hh3cDot11ObjectIDType
_Hh3cDot11WIDSAPID_Object = MibTableColumn
hh3cDot11WIDSAPID = _Hh3cDot11WIDSAPID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 2, 1, 1),
    _Hh3cDot11WIDSAPID_Type()
)
hh3cDot11WIDSAPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIDSAPID.setStatus("current")
_Hh3cDot11DetectCurAPSigStrength_Type = Integer32
_Hh3cDot11DetectCurAPSigStrength_Object = MibTableColumn
hh3cDot11DetectCurAPSigStrength = _Hh3cDot11DetectCurAPSigStrength_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 2, 1, 2),
    _Hh3cDot11DetectCurAPSigStrength_Type()
)
hh3cDot11DetectCurAPSigStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11DetectCurAPSigStrength.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11DetectCurAPSigStrength.setUnits("dBm")
_Hh3cDot11DetectAPByChannel_Type = Hh3cDot11ChannelScopeType
_Hh3cDot11DetectAPByChannel_Object = MibTableColumn
hh3cDot11DetectAPByChannel = _Hh3cDot11DetectAPByChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 2, 1, 3),
    _Hh3cDot11DetectAPByChannel_Type()
)
hh3cDot11DetectAPByChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11DetectAPByChannel.setStatus("current")
_Hh3cDot11DetectAPByRadioID_Type = Hh3cDot11RadioScopeType
_Hh3cDot11DetectAPByRadioID_Object = MibTableColumn
hh3cDot11DetectAPByRadioID = _Hh3cDot11DetectAPByRadioID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 2, 1, 4),
    _Hh3cDot11DetectAPByRadioID_Type()
)
hh3cDot11DetectAPByRadioID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11DetectAPByRadioID.setStatus("current")
_Hh3cDot11AttackAPStatus_Type = TruthValue
_Hh3cDot11AttackAPStatus_Object = MibTableColumn
hh3cDot11AttackAPStatus = _Hh3cDot11AttackAPStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 2, 1, 5),
    _Hh3cDot11AttackAPStatus_Type()
)
hh3cDot11AttackAPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11AttackAPStatus.setStatus("current")
_Hh3cDot11DetectAPFirstTm_Type = TimeTicks
_Hh3cDot11DetectAPFirstTm_Object = MibTableColumn
hh3cDot11DetectAPFirstTm = _Hh3cDot11DetectAPFirstTm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 2, 1, 6),
    _Hh3cDot11DetectAPFirstTm_Type()
)
hh3cDot11DetectAPFirstTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11DetectAPFirstTm.setStatus("current")
_Hh3cDot11DetectAPLastTm_Type = TimeTicks
_Hh3cDot11DetectAPLastTm_Object = MibTableColumn
hh3cDot11DetectAPLastTm = _Hh3cDot11DetectAPLastTm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 2, 1, 7),
    _Hh3cDot11DetectAPLastTm_Type()
)
hh3cDot11DetectAPLastTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11DetectAPLastTm.setStatus("current")
_Hh3cDot11WIDSRogueStaTable_Object = MibTable
hh3cDot11WIDSRogueStaTable = _Hh3cDot11WIDSRogueStaTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cDot11WIDSRogueStaTable.setStatus("current")
_Hh3cDot11WIDSRogueStaEntry_Object = MibTableRow
hh3cDot11WIDSRogueStaEntry = _Hh3cDot11WIDSRogueStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 3, 1)
)
hh3cDot11WIDSRogueStaEntry.setIndexNames(
    (0, "HH3C-DOT11-WIDS-MIB", "hh3cDot11RogueStaMAC"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIDSRogueStaEntry.setStatus("current")
_Hh3cDot11RogueStaMAC_Type = MacAddress
_Hh3cDot11RogueStaMAC_Object = MibTableColumn
hh3cDot11RogueStaMAC = _Hh3cDot11RogueStaMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 3, 1, 1),
    _Hh3cDot11RogueStaMAC_Type()
)
hh3cDot11RogueStaMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RogueStaMAC.setStatus("current")


class _Hh3cDot11RogueStaVendorName_Type(OctetString):
    """Custom type hh3cDot11RogueStaVendorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDot11RogueStaVendorName_Type.__name__ = "OctetString"
_Hh3cDot11RogueStaVendorName_Object = MibTableColumn
hh3cDot11RogueStaVendorName = _Hh3cDot11RogueStaVendorName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 3, 1, 2),
    _Hh3cDot11RogueStaVendorName_Type()
)
hh3cDot11RogueStaVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RogueStaVendorName.setStatus("current")
_Hh3cDot11RogueStaMonitorNum_Type = Integer32
_Hh3cDot11RogueStaMonitorNum_Object = MibTableColumn
hh3cDot11RogueStaMonitorNum = _Hh3cDot11RogueStaMonitorNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 3, 1, 3),
    _Hh3cDot11RogueStaMonitorNum_Type()
)
hh3cDot11RogueStaMonitorNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RogueStaMonitorNum.setStatus("current")
_Hh3cDot11RogueStaFirstDetectTm_Type = TimeTicks
_Hh3cDot11RogueStaFirstDetectTm_Object = MibTableColumn
hh3cDot11RogueStaFirstDetectTm = _Hh3cDot11RogueStaFirstDetectTm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 3, 1, 4),
    _Hh3cDot11RogueStaFirstDetectTm_Type()
)
hh3cDot11RogueStaFirstDetectTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RogueStaFirstDetectTm.setStatus("current")
_Hh3cDot11RogueStaLastDetectTm_Type = TimeTicks
_Hh3cDot11RogueStaLastDetectTm_Object = MibTableColumn
hh3cDot11RogueStaLastDetectTm = _Hh3cDot11RogueStaLastDetectTm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 3, 1, 5),
    _Hh3cDot11RogueStaLastDetectTm_Type()
)
hh3cDot11RogueStaLastDetectTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RogueStaLastDetectTm.setStatus("current")
_Hh3cDot11RogueStaAccessBSSID_Type = MacAddress
_Hh3cDot11RogueStaAccessBSSID_Object = MibTableColumn
hh3cDot11RogueStaAccessBSSID = _Hh3cDot11RogueStaAccessBSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 3, 1, 6),
    _Hh3cDot11RogueStaAccessBSSID_Type()
)
hh3cDot11RogueStaAccessBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RogueStaAccessBSSID.setStatus("current")
_Hh3cDot11RogueStaMaxSigStrength_Type = Integer32
_Hh3cDot11RogueStaMaxSigStrength_Object = MibTableColumn
hh3cDot11RogueStaMaxSigStrength = _Hh3cDot11RogueStaMaxSigStrength_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 3, 1, 7),
    _Hh3cDot11RogueStaMaxSigStrength_Type()
)
hh3cDot11RogueStaMaxSigStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RogueStaMaxSigStrength.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RogueStaMaxSigStrength.setUnits("dBm")
_Hh3cDot11RogueStaChannel_Type = Hh3cDot11ChannelScopeType
_Hh3cDot11RogueStaChannel_Object = MibTableColumn
hh3cDot11RogueStaChannel = _Hh3cDot11RogueStaChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 3, 1, 8),
    _Hh3cDot11RogueStaChannel_Type()
)
hh3cDot11RogueStaChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RogueStaChannel.setStatus("current")
_Hh3cDot11RogueStaAttackedStatus_Type = TruthValue
_Hh3cDot11RogueStaAttackedStatus_Object = MibTableColumn
hh3cDot11RogueStaAttackedStatus = _Hh3cDot11RogueStaAttackedStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 3, 1, 9),
    _Hh3cDot11RogueStaAttackedStatus_Type()
)
hh3cDot11RogueStaAttackedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RogueStaAttackedStatus.setStatus("current")


class _Hh3cDot11RogueStaToIgnore_Type(TruthValue):
    """Custom type hh3cDot11RogueStaToIgnore based on TruthValue"""


_Hh3cDot11RogueStaToIgnore_Object = MibTableColumn
hh3cDot11RogueStaToIgnore = _Hh3cDot11RogueStaToIgnore_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 3, 1, 10),
    _Hh3cDot11RogueStaToIgnore_Type()
)
hh3cDot11RogueStaToIgnore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RogueStaToIgnore.setStatus("current")
_Hh3cDot11RogueStaAdHocStatus_Type = TruthValue
_Hh3cDot11RogueStaAdHocStatus_Object = MibTableColumn
hh3cDot11RogueStaAdHocStatus = _Hh3cDot11RogueStaAdHocStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 3, 1, 11),
    _Hh3cDot11RogueStaAdHocStatus_Type()
)
hh3cDot11RogueStaAdHocStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RogueStaAdHocStatus.setStatus("current")
_Hh3cDot11RogueStaReset_Type = TruthValue
_Hh3cDot11RogueStaReset_Object = MibTableColumn
hh3cDot11RogueStaReset = _Hh3cDot11RogueStaReset_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 3, 1, 12),
    _Hh3cDot11RogueStaReset_Type()
)
hh3cDot11RogueStaReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RogueStaReset.setStatus("current")
_Hh3cDot11RogueStaFirstDetectTmStr_Type = OctetString
_Hh3cDot11RogueStaFirstDetectTmStr_Object = MibTableColumn
hh3cDot11RogueStaFirstDetectTmStr = _Hh3cDot11RogueStaFirstDetectTmStr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 3, 1, 13),
    _Hh3cDot11RogueStaFirstDetectTmStr_Type()
)
hh3cDot11RogueStaFirstDetectTmStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RogueStaFirstDetectTmStr.setStatus("current")
_Hh3cDot11RogueStaLastDetectTmStr_Type = OctetString
_Hh3cDot11RogueStaLastDetectTmStr_Object = MibTableColumn
hh3cDot11RogueStaLastDetectTmStr = _Hh3cDot11RogueStaLastDetectTmStr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 3, 1, 14),
    _Hh3cDot11RogueStaLastDetectTmStr_Type()
)
hh3cDot11RogueStaLastDetectTmStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RogueStaLastDetectTmStr.setStatus("current")
_Hh3cDot11WIDSRogueStaExtTable_Object = MibTable
hh3cDot11WIDSRogueStaExtTable = _Hh3cDot11WIDSRogueStaExtTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cDot11WIDSRogueStaExtTable.setStatus("current")
_Hh3cDot11WIDSRogueStaExtEntry_Object = MibTableRow
hh3cDot11WIDSRogueStaExtEntry = _Hh3cDot11WIDSRogueStaExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 4, 1)
)
hh3cDot11WIDSRogueStaExtEntry.setIndexNames(
    (0, "HH3C-DOT11-WIDS-MIB", "hh3cDot11RogueStaMAC"),
    (0, "HH3C-DOT11-WIDS-MIB", "hh3cDot11WIDSAPID"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIDSRogueStaExtEntry.setStatus("current")
_Hh3cDot11DetectCurStaSigStrength_Type = Integer32
_Hh3cDot11DetectCurStaSigStrength_Object = MibTableColumn
hh3cDot11DetectCurStaSigStrength = _Hh3cDot11DetectCurStaSigStrength_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 4, 1, 1),
    _Hh3cDot11DetectCurStaSigStrength_Type()
)
hh3cDot11DetectCurStaSigStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11DetectCurStaSigStrength.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11DetectCurStaSigStrength.setUnits("dBm")
_Hh3cDot11DetectStaByChannel_Type = Hh3cDot11ChannelScopeType
_Hh3cDot11DetectStaByChannel_Object = MibTableColumn
hh3cDot11DetectStaByChannel = _Hh3cDot11DetectStaByChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 4, 1, 2),
    _Hh3cDot11DetectStaByChannel_Type()
)
hh3cDot11DetectStaByChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11DetectStaByChannel.setStatus("current")
_Hh3cDot11DetectStaByRadioID_Type = Hh3cDot11RadioScopeType
_Hh3cDot11DetectStaByRadioID_Object = MibTableColumn
hh3cDot11DetectStaByRadioID = _Hh3cDot11DetectStaByRadioID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 4, 1, 3),
    _Hh3cDot11DetectStaByRadioID_Type()
)
hh3cDot11DetectStaByRadioID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11DetectStaByRadioID.setStatus("current")
_Hh3cDot11AttackStaStatus_Type = TruthValue
_Hh3cDot11AttackStaStatus_Object = MibTableColumn
hh3cDot11AttackStaStatus = _Hh3cDot11AttackStaStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 4, 1, 4),
    _Hh3cDot11AttackStaStatus_Type()
)
hh3cDot11AttackStaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11AttackStaStatus.setStatus("current")
_Hh3cDot11DetectStaFirstTm_Type = TimeTicks
_Hh3cDot11DetectStaFirstTm_Object = MibTableColumn
hh3cDot11DetectStaFirstTm = _Hh3cDot11DetectStaFirstTm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 4, 1, 5),
    _Hh3cDot11DetectStaFirstTm_Type()
)
hh3cDot11DetectStaFirstTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11DetectStaFirstTm.setStatus("current")
_Hh3cDot11DetectStaLastTm_Type = TimeTicks
_Hh3cDot11DetectStaLastTm_Object = MibTableColumn
hh3cDot11DetectStaLastTm = _Hh3cDot11DetectStaLastTm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 4, 1, 6),
    _Hh3cDot11DetectStaLastTm_Type()
)
hh3cDot11DetectStaLastTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11DetectStaLastTm.setStatus("current")
_Hh3cDot11WIDSDetectedDevTable_Object = MibTable
hh3cDot11WIDSDetectedDevTable = _Hh3cDot11WIDSDetectedDevTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 5)
)
if mibBuilder.loadTexts:
    hh3cDot11WIDSDetectedDevTable.setStatus("current")
_Hh3cDot11WIDSDetectedDevEntry_Object = MibTableRow
hh3cDot11WIDSDetectedDevEntry = _Hh3cDot11WIDSDetectedDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 5, 1)
)
hh3cDot11WIDSDetectedDevEntry.setIndexNames(
    (0, "HH3C-DOT11-WIDS-MIB", "hh3cDot11WIDSDevMAC"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIDSDetectedDevEntry.setStatus("current")
_Hh3cDot11WIDSDevMAC_Type = MacAddress
_Hh3cDot11WIDSDevMAC_Object = MibTableColumn
hh3cDot11WIDSDevMAC = _Hh3cDot11WIDSDevMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 5, 1, 1),
    _Hh3cDot11WIDSDevMAC_Type()
)
hh3cDot11WIDSDevMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIDSDevMAC.setStatus("current")
_Hh3cDot11WIDSDevType_Type = Hh3cDot11WIDSDevType
_Hh3cDot11WIDSDevType_Object = MibTableColumn
hh3cDot11WIDSDevType = _Hh3cDot11WIDSDevType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 5, 1, 2),
    _Hh3cDot11WIDSDevType_Type()
)
hh3cDot11WIDSDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIDSDevType.setStatus("current")
_Hh3cDot11WIDSDevPermitType_Type = Hh3cDot11WIDSDevPermitType
_Hh3cDot11WIDSDevPermitType_Object = MibTableColumn
hh3cDot11WIDSDevPermitType = _Hh3cDot11WIDSDevPermitType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 5, 1, 3),
    _Hh3cDot11WIDSDevPermitType_Type()
)
hh3cDot11WIDSDevPermitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIDSDevPermitType.setStatus("current")
_Hh3cDot11WIDSDevVendor_Type = OctetString
_Hh3cDot11WIDSDevVendor_Object = MibTableColumn
hh3cDot11WIDSDevVendor = _Hh3cDot11WIDSDevVendor_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 5, 1, 4),
    _Hh3cDot11WIDSDevVendor_Type()
)
hh3cDot11WIDSDevVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIDSDevVendor.setStatus("current")
_Hh3cDot11WIDSDevMonitorNum_Type = Integer32
_Hh3cDot11WIDSDevMonitorNum_Object = MibTableColumn
hh3cDot11WIDSDevMonitorNum = _Hh3cDot11WIDSDevMonitorNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 5, 1, 5),
    _Hh3cDot11WIDSDevMonitorNum_Type()
)
hh3cDot11WIDSDevMonitorNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIDSDevMonitorNum.setStatus("current")
_Hh3cDot11WIDSDevSSID_Type = OctetString
_Hh3cDot11WIDSDevSSID_Object = MibTableColumn
hh3cDot11WIDSDevSSID = _Hh3cDot11WIDSDevSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 5, 1, 6),
    _Hh3cDot11WIDSDevSSID_Type()
)
hh3cDot11WIDSDevSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIDSDevSSID.setStatus("current")
_Hh3cDot11WIDSDevBSSID_Type = MacAddress
_Hh3cDot11WIDSDevBSSID_Object = MibTableColumn
hh3cDot11WIDSDevBSSID = _Hh3cDot11WIDSDevBSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 5, 1, 7),
    _Hh3cDot11WIDSDevBSSID_Type()
)
hh3cDot11WIDSDevBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIDSDevBSSID.setStatus("current")
_Hh3cDot11WIDSDevChannel_Type = Hh3cDot11ChannelScopeType
_Hh3cDot11WIDSDevChannel_Object = MibTableColumn
hh3cDot11WIDSDevChannel = _Hh3cDot11WIDSDevChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 5, 1, 8),
    _Hh3cDot11WIDSDevChannel_Type()
)
hh3cDot11WIDSDevChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIDSDevChannel.setStatus("current")
_Hh3cDot11WIDSDevMaxRSSI_Type = Integer32
_Hh3cDot11WIDSDevMaxRSSI_Object = MibTableColumn
hh3cDot11WIDSDevMaxRSSI = _Hh3cDot11WIDSDevMaxRSSI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 5, 1, 9),
    _Hh3cDot11WIDSDevMaxRSSI_Type()
)
hh3cDot11WIDSDevMaxRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIDSDevMaxRSSI.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11WIDSDevMaxRSSI.setUnits("dbm")
_Hh3cDot11WIDSDevBeaconIntvl_Type = Integer32
_Hh3cDot11WIDSDevBeaconIntvl_Object = MibTableColumn
hh3cDot11WIDSDevBeaconIntvl = _Hh3cDot11WIDSDevBeaconIntvl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 5, 1, 10),
    _Hh3cDot11WIDSDevBeaconIntvl_Type()
)
hh3cDot11WIDSDevBeaconIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIDSDevBeaconIntvl.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11WIDSDevBeaconIntvl.setUnits("millionsecond")
_Hh3cDot11WIDSDevFstDctTime_Type = DateAndTime
_Hh3cDot11WIDSDevFstDctTime_Object = MibTableColumn
hh3cDot11WIDSDevFstDctTime = _Hh3cDot11WIDSDevFstDctTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 5, 1, 11),
    _Hh3cDot11WIDSDevFstDctTime_Type()
)
hh3cDot11WIDSDevFstDctTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIDSDevFstDctTime.setStatus("current")
_Hh3cDot11WIDSDevLstDctTime_Type = DateAndTime
_Hh3cDot11WIDSDevLstDctTime_Object = MibTableColumn
hh3cDot11WIDSDevLstDctTime = _Hh3cDot11WIDSDevLstDctTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 5, 1, 12),
    _Hh3cDot11WIDSDevLstDctTime_Type()
)
hh3cDot11WIDSDevLstDctTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIDSDevLstDctTime.setStatus("current")
_Hh3cDot11WIDSDevReset_Type = TruthValue
_Hh3cDot11WIDSDevReset_Object = MibTableColumn
hh3cDot11WIDSDevReset = _Hh3cDot11WIDSDevReset_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 5, 1, 13),
    _Hh3cDot11WIDSDevReset_Type()
)
hh3cDot11WIDSDevReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIDSDevReset.setStatus("current")
_Hh3cDot11WIDSDevSnr_Type = Integer32
_Hh3cDot11WIDSDevSnr_Object = MibTableColumn
hh3cDot11WIDSDevSnr = _Hh3cDot11WIDSDevSnr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 5, 1, 14),
    _Hh3cDot11WIDSDevSnr_Type()
)
hh3cDot11WIDSDevSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIDSDevSnr.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11WIDSDevSnr.setUnits("dB")
_Hh3cDot11WIDSRptAPTable_Object = MibTable
hh3cDot11WIDSRptAPTable = _Hh3cDot11WIDSRptAPTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 6)
)
if mibBuilder.loadTexts:
    hh3cDot11WIDSRptAPTable.setStatus("current")
_Hh3cDot11WIDSRptAPEntry_Object = MibTableRow
hh3cDot11WIDSRptAPEntry = _Hh3cDot11WIDSRptAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 6, 1)
)
hh3cDot11WIDSRptAPEntry.setIndexNames(
    (0, "HH3C-DOT11-WIDS-MIB", "hh3cDot11WIDSDevMAC"),
    (0, "HH3C-DOT11-WIDS-MIB", "hh3cDot11WIDSRptAPMAC"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIDSRptAPEntry.setStatus("current")
_Hh3cDot11WIDSRptAPMAC_Type = MacAddress
_Hh3cDot11WIDSRptAPMAC_Object = MibTableColumn
hh3cDot11WIDSRptAPMAC = _Hh3cDot11WIDSRptAPMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 6, 1, 1),
    _Hh3cDot11WIDSRptAPMAC_Type()
)
hh3cDot11WIDSRptAPMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIDSRptAPMAC.setStatus("current")
_Hh3cDot11WIDSRptAPName_Type = OctetString
_Hh3cDot11WIDSRptAPName_Object = MibTableColumn
hh3cDot11WIDSRptAPName = _Hh3cDot11WIDSRptAPName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 6, 1, 2),
    _Hh3cDot11WIDSRptAPName_Type()
)
hh3cDot11WIDSRptAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIDSRptAPName.setStatus("current")
_Hh3cDot11WIDSRptAPRadioID_Type = Hh3cDot11RadioScopeType
_Hh3cDot11WIDSRptAPRadioID_Object = MibTableColumn
hh3cDot11WIDSRptAPRadioID = _Hh3cDot11WIDSRptAPRadioID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 6, 1, 3),
    _Hh3cDot11WIDSRptAPRadioID_Type()
)
hh3cDot11WIDSRptAPRadioID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIDSRptAPRadioID.setStatus("current")
_Hh3cDot11WIDSRptAPMaxRSSI_Type = Integer32
_Hh3cDot11WIDSRptAPMaxRSSI_Object = MibTableColumn
hh3cDot11WIDSRptAPMaxRSSI = _Hh3cDot11WIDSRptAPMaxRSSI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 6, 1, 4),
    _Hh3cDot11WIDSRptAPMaxRSSI_Type()
)
hh3cDot11WIDSRptAPMaxRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIDSRptAPMaxRSSI.setStatus("current")
_Hh3cDot11WIDSRptAPFstDctTime_Type = DateAndTime
_Hh3cDot11WIDSRptAPFstDctTime_Object = MibTableColumn
hh3cDot11WIDSRptAPFstDctTime = _Hh3cDot11WIDSRptAPFstDctTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 6, 1, 5),
    _Hh3cDot11WIDSRptAPFstDctTime_Type()
)
hh3cDot11WIDSRptAPFstDctTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIDSRptAPFstDctTime.setStatus("current")
_Hh3cDot11WIDSRptAPLstDctTime_Type = DateAndTime
_Hh3cDot11WIDSRptAPLstDctTime_Object = MibTableColumn
hh3cDot11WIDSRptAPLstDctTime = _Hh3cDot11WIDSRptAPLstDctTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 6, 1, 6),
    _Hh3cDot11WIDSRptAPLstDctTime_Type()
)
hh3cDot11WIDSRptAPLstDctTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIDSRptAPLstDctTime.setStatus("current")
_Hh3cDot11DynBlackListTable_Object = MibTable
hh3cDot11DynBlackListTable = _Hh3cDot11DynBlackListTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 7)
)
if mibBuilder.loadTexts:
    hh3cDot11DynBlackListTable.setStatus("current")
_Hh3cDot11DynBlackListEntry_Object = MibTableRow
hh3cDot11DynBlackListEntry = _Hh3cDot11DynBlackListEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 7, 1)
)
hh3cDot11DynBlackListEntry.setIndexNames(
    (0, "HH3C-DOT11-WIDS-MIB", "hh3cDot11DynBlackListMAC"),
)
if mibBuilder.loadTexts:
    hh3cDot11DynBlackListEntry.setStatus("current")
_Hh3cDot11DynBlackListMAC_Type = MacAddress
_Hh3cDot11DynBlackListMAC_Object = MibTableColumn
hh3cDot11DynBlackListMAC = _Hh3cDot11DynBlackListMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 7, 1, 1),
    _Hh3cDot11DynBlackListMAC_Type()
)
hh3cDot11DynBlackListMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11DynBlackListMAC.setStatus("current")
_Hh3cDot11DynBlackListTime_Type = Unsigned32
_Hh3cDot11DynBlackListTime_Object = MibTableColumn
hh3cDot11DynBlackListTime = _Hh3cDot11DynBlackListTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 7, 1, 2),
    _Hh3cDot11DynBlackListTime_Type()
)
hh3cDot11DynBlackListTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11DynBlackListTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11DynBlackListTime.setUnits("second")
_Hh3cDot11DynBlackListReason_Type = OctetString
_Hh3cDot11DynBlackListReason_Object = MibTableColumn
hh3cDot11DynBlackListReason = _Hh3cDot11DynBlackListReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 7, 1, 3),
    _Hh3cDot11DynBlackListReason_Type()
)
hh3cDot11DynBlackListReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11DynBlackListReason.setStatus("current")
_Hh3cDot11DynBlackListReset_Type = TruthValue
_Hh3cDot11DynBlackListReset_Object = MibTableColumn
hh3cDot11DynBlackListReset = _Hh3cDot11DynBlackListReset_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 7, 1, 4),
    _Hh3cDot11DynBlackListReset_Type()
)
hh3cDot11DynBlackListReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11DynBlackListReset.setStatus("current")
_Hh3cDot11DynBlackListTimeTicks_Type = TimeTicks
_Hh3cDot11DynBlackListTimeTicks_Object = MibTableColumn
hh3cDot11DynBlackListTimeTicks = _Hh3cDot11DynBlackListTimeTicks_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 7, 1, 5),
    _Hh3cDot11DynBlackListTimeTicks_Type()
)
hh3cDot11DynBlackListTimeTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11DynBlackListTimeTicks.setStatus("current")
_Hh3cDot11WIDSRogueHistoryTable_Object = MibTable
hh3cDot11WIDSRogueHistoryTable = _Hh3cDot11WIDSRogueHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 8)
)
if mibBuilder.loadTexts:
    hh3cDot11WIDSRogueHistoryTable.setStatus("current")
_Hh3cDot11WIDSRogueHistoryEntry_Object = MibTableRow
hh3cDot11WIDSRogueHistoryEntry = _Hh3cDot11WIDSRogueHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 8, 1)
)
hh3cDot11WIDSRogueHistoryEntry.setIndexNames(
    (0, "HH3C-DOT11-WIDS-MIB", "hh3cDot11WIDSRogueHisIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIDSRogueHistoryEntry.setStatus("current")
_Hh3cDot11WIDSRogueHisIndex_Type = Integer32
_Hh3cDot11WIDSRogueHisIndex_Object = MibTableColumn
hh3cDot11WIDSRogueHisIndex = _Hh3cDot11WIDSRogueHisIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 8, 1, 1),
    _Hh3cDot11WIDSRogueHisIndex_Type()
)
hh3cDot11WIDSRogueHisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIDSRogueHisIndex.setStatus("current")
_Hh3cDot11WIDSRogueHisMAC_Type = MacAddress
_Hh3cDot11WIDSRogueHisMAC_Object = MibTableColumn
hh3cDot11WIDSRogueHisMAC = _Hh3cDot11WIDSRogueHisMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 8, 1, 2),
    _Hh3cDot11WIDSRogueHisMAC_Type()
)
hh3cDot11WIDSRogueHisMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIDSRogueHisMAC.setStatus("current")
_Hh3cDot11WIDSRogueHisVendor_Type = OctetString
_Hh3cDot11WIDSRogueHisVendor_Object = MibTableColumn
hh3cDot11WIDSRogueHisVendor = _Hh3cDot11WIDSRogueHisVendor_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 8, 1, 3),
    _Hh3cDot11WIDSRogueHisVendor_Type()
)
hh3cDot11WIDSRogueHisVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIDSRogueHisVendor.setStatus("current")
_Hh3cDot11WIDSRogueHisType_Type = Hh3cDot11WIDSDevType
_Hh3cDot11WIDSRogueHisType_Object = MibTableColumn
hh3cDot11WIDSRogueHisType = _Hh3cDot11WIDSRogueHisType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 8, 1, 4),
    _Hh3cDot11WIDSRogueHisType_Type()
)
hh3cDot11WIDSRogueHisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIDSRogueHisType.setStatus("current")
_Hh3cDot11WIDSRogueHisChl_Type = Hh3cDot11ChannelScopeType
_Hh3cDot11WIDSRogueHisChl_Object = MibTableColumn
hh3cDot11WIDSRogueHisChl = _Hh3cDot11WIDSRogueHisChl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 8, 1, 5),
    _Hh3cDot11WIDSRogueHisChl_Type()
)
hh3cDot11WIDSRogueHisChl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIDSRogueHisChl.setStatus("current")
_Hh3cDot11WIDSRogueHisSSID_Type = OctetString
_Hh3cDot11WIDSRogueHisSSID_Object = MibTableColumn
hh3cDot11WIDSRogueHisSSID = _Hh3cDot11WIDSRogueHisSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 8, 1, 6),
    _Hh3cDot11WIDSRogueHisSSID_Type()
)
hh3cDot11WIDSRogueHisSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIDSRogueHisSSID.setStatus("current")
_Hh3cDot11WIDSRogueHisLastDctTime_Type = DateAndTime
_Hh3cDot11WIDSRogueHisLastDctTime_Object = MibTableColumn
hh3cDot11WIDSRogueHisLastDctTime = _Hh3cDot11WIDSRogueHisLastDctTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 8, 1, 7),
    _Hh3cDot11WIDSRogueHisLastDctTime_Type()
)
hh3cDot11WIDSRogueHisLastDctTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIDSRogueHisLastDctTime.setStatus("current")
_Hh3cDot11WIDSAtkHistroyTable_Object = MibTable
hh3cDot11WIDSAtkHistroyTable = _Hh3cDot11WIDSAtkHistroyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 9)
)
if mibBuilder.loadTexts:
    hh3cDot11WIDSAtkHistroyTable.setStatus("current")
_Hh3cDot11WIDSAtkHistroyEntry_Object = MibTableRow
hh3cDot11WIDSAtkHistroyEntry = _Hh3cDot11WIDSAtkHistroyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 9, 1)
)
hh3cDot11WIDSAtkHistroyEntry.setIndexNames(
    (0, "HH3C-DOT11-WIDS-MIB", "hh3cDot11WIDSAtkHisIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIDSAtkHistroyEntry.setStatus("current")
_Hh3cDot11WIDSAtkHisIndex_Type = Integer32
_Hh3cDot11WIDSAtkHisIndex_Object = MibTableColumn
hh3cDot11WIDSAtkHisIndex = _Hh3cDot11WIDSAtkHisIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 9, 1, 1),
    _Hh3cDot11WIDSAtkHisIndex_Type()
)
hh3cDot11WIDSAtkHisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIDSAtkHisIndex.setStatus("current")
_Hh3cDot11WIDSAtkHisMAC_Type = MacAddress
_Hh3cDot11WIDSAtkHisMAC_Object = MibTableColumn
hh3cDot11WIDSAtkHisMAC = _Hh3cDot11WIDSAtkHisMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 9, 1, 2),
    _Hh3cDot11WIDSAtkHisMAC_Type()
)
hh3cDot11WIDSAtkHisMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIDSAtkHisMAC.setStatus("current")
_Hh3cDot11WIDSAtkHisType_Type = Hh3cDot11WIDSAtkType
_Hh3cDot11WIDSAtkHisType_Object = MibTableColumn
hh3cDot11WIDSAtkHisType = _Hh3cDot11WIDSAtkHisType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 9, 1, 3),
    _Hh3cDot11WIDSAtkHisType_Type()
)
hh3cDot11WIDSAtkHisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIDSAtkHisType.setStatus("current")
_Hh3cDot11WIDSAtkHisChl_Type = Hh3cDot11ChannelScopeType
_Hh3cDot11WIDSAtkHisChl_Object = MibTableColumn
hh3cDot11WIDSAtkHisChl = _Hh3cDot11WIDSAtkHisChl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 9, 1, 4),
    _Hh3cDot11WIDSAtkHisChl_Type()
)
hh3cDot11WIDSAtkHisChl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIDSAtkHisChl.setStatus("current")
_Hh3cDot11WIDSAtkHisRSSI_Type = Integer32
_Hh3cDot11WIDSAtkHisRSSI_Object = MibTableColumn
hh3cDot11WIDSAtkHisRSSI = _Hh3cDot11WIDSAtkHisRSSI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 9, 1, 5),
    _Hh3cDot11WIDSAtkHisRSSI_Type()
)
hh3cDot11WIDSAtkHisRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIDSAtkHisRSSI.setStatus("current")
_Hh3cDot11WIDSAtkHisDctTime_Type = DateAndTime
_Hh3cDot11WIDSAtkHisDctTime_Object = MibTableColumn
hh3cDot11WIDSAtkHisDctTime = _Hh3cDot11WIDSAtkHisDctTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 9, 1, 6),
    _Hh3cDot11WIDSAtkHisDctTime_Type()
)
hh3cDot11WIDSAtkHisDctTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIDSAtkHisDctTime.setStatus("current")
_Hh3cDot11WIDSAtkHisAPName_Type = OctetString
_Hh3cDot11WIDSAtkHisAPName_Object = MibTableColumn
hh3cDot11WIDSAtkHisAPName = _Hh3cDot11WIDSAtkHisAPName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 9, 1, 7),
    _Hh3cDot11WIDSAtkHisAPName_Type()
)
hh3cDot11WIDSAtkHisAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIDSAtkHisAPName.setStatus("current")
_Hh3cDot11WIDSAtkStatis_ObjectIdentity = ObjectIdentity
hh3cDot11WIDSAtkStatis = _Hh3cDot11WIDSAtkStatis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 10)
)
_Hh3cDot11WIDSAtkStasStartTime_Type = DateAndTime
_Hh3cDot11WIDSAtkStasStartTime_Object = MibScalar
hh3cDot11WIDSAtkStasStartTime = _Hh3cDot11WIDSAtkStasStartTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 10, 1),
    _Hh3cDot11WIDSAtkStasStartTime_Type()
)
hh3cDot11WIDSAtkStasStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIDSAtkStasStartTime.setStatus("current")
_Hh3cDot11WIDSAtkStasTable_Object = MibTable
hh3cDot11WIDSAtkStasTable = _Hh3cDot11WIDSAtkStasTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 10, 2)
)
if mibBuilder.loadTexts:
    hh3cDot11WIDSAtkStasTable.setStatus("current")
_Hh3cDot11WIDSAtkStasEntry_Object = MibTableRow
hh3cDot11WIDSAtkStasEntry = _Hh3cDot11WIDSAtkStasEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 10, 2, 1)
)
hh3cDot11WIDSAtkStasEntry.setIndexNames(
    (0, "HH3C-DOT11-WIDS-MIB", "hh3cDot11WIDSAtkStasType"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIDSAtkStasEntry.setStatus("current")
_Hh3cDot11WIDSAtkStasType_Type = Hh3cDot11WIDSAtkType
_Hh3cDot11WIDSAtkStasType_Object = MibTableColumn
hh3cDot11WIDSAtkStasType = _Hh3cDot11WIDSAtkStasType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 10, 2, 1, 1),
    _Hh3cDot11WIDSAtkStasType_Type()
)
hh3cDot11WIDSAtkStasType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIDSAtkStasType.setStatus("current")
_Hh3cDot11WIDSAtkStasCurCnt_Type = Unsigned32
_Hh3cDot11WIDSAtkStasCurCnt_Object = MibTableColumn
hh3cDot11WIDSAtkStasCurCnt = _Hh3cDot11WIDSAtkStasCurCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 10, 2, 1, 2),
    _Hh3cDot11WIDSAtkStasCurCnt_Type()
)
hh3cDot11WIDSAtkStasCurCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIDSAtkStasCurCnt.setStatus("current")
_Hh3cDot11WIDSAtkStasTotalCnt_Type = Unsigned32
_Hh3cDot11WIDSAtkStasTotalCnt_Object = MibTableColumn
hh3cDot11WIDSAtkStasTotalCnt = _Hh3cDot11WIDSAtkStasTotalCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 10, 2, 1, 3),
    _Hh3cDot11WIDSAtkStasTotalCnt_Type()
)
hh3cDot11WIDSAtkStasTotalCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIDSAtkStasTotalCnt.setStatus("current")
_Hh3cDot11BlackListTable_Object = MibTable
hh3cDot11BlackListTable = _Hh3cDot11BlackListTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 11)
)
if mibBuilder.loadTexts:
    hh3cDot11BlackListTable.setStatus("current")
_Hh3cDot11BlackListEntry_Object = MibTableRow
hh3cDot11BlackListEntry = _Hh3cDot11BlackListEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 11, 1)
)
hh3cDot11BlackListEntry.setIndexNames(
    (0, "HH3C-DOT11-WIDS-MIB", "hh3cDot11BlackListMAC"),
)
if mibBuilder.loadTexts:
    hh3cDot11BlackListEntry.setStatus("current")
_Hh3cDot11BlackListMAC_Type = MacAddress
_Hh3cDot11BlackListMAC_Object = MibTableColumn
hh3cDot11BlackListMAC = _Hh3cDot11BlackListMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 11, 1, 1),
    _Hh3cDot11BlackListMAC_Type()
)
hh3cDot11BlackListMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11BlackListMAC.setStatus("current")
_Hh3cDot11BlackListTime_Type = Unsigned32
_Hh3cDot11BlackListTime_Object = MibTableColumn
hh3cDot11BlackListTime = _Hh3cDot11BlackListTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 11, 1, 2),
    _Hh3cDot11BlackListTime_Type()
)
hh3cDot11BlackListTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BlackListTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11BlackListTime.setUnits("minutes")
_Hh3cDot11BlackListReason_Type = OctetString
_Hh3cDot11BlackListReason_Object = MibTableColumn
hh3cDot11BlackListReason = _Hh3cDot11BlackListReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 11, 1, 3),
    _Hh3cDot11BlackListReason_Type()
)
hh3cDot11BlackListReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BlackListReason.setStatus("current")
_Hh3cDot11BlackListRowStatus_Type = RowStatus
_Hh3cDot11BlackListRowStatus_Object = MibTableColumn
hh3cDot11BlackListRowStatus = _Hh3cDot11BlackListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 11, 1, 4),
    _Hh3cDot11BlackListRowStatus_Type()
)
hh3cDot11BlackListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11BlackListRowStatus.setStatus("current")
_Hh3cDot11BlackListTimeTicks_Type = TimeTicks
_Hh3cDot11BlackListTimeTicks_Object = MibTableColumn
hh3cDot11BlackListTimeTicks = _Hh3cDot11BlackListTimeTicks_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 2, 11, 1, 5),
    _Hh3cDot11BlackListTimeTicks_Type()
)
hh3cDot11BlackListTimeTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BlackListTimeTicks.setStatus("current")
_Hh3cDot11WIDSNotifyGroup_ObjectIdentity = ObjectIdentity
hh3cDot11WIDSNotifyGroup = _Hh3cDot11WIDSNotifyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 3)
)
_Hh3cDot11WIDSTraps_ObjectIdentity = ObjectIdentity
hh3cDot11WIDSTraps = _Hh3cDot11WIDSTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 3, 1)
)
_Hh3cDot11WIDSTrapVarObjects_ObjectIdentity = ObjectIdentity
hh3cDot11WIDSTrapVarObjects = _Hh3cDot11WIDSTrapVarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 3, 2)
)
_Hh3cDot11WIDSRogueMAC_Type = MacAddress
_Hh3cDot11WIDSRogueMAC_Object = MibScalar
hh3cDot11WIDSRogueMAC = _Hh3cDot11WIDSRogueMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 3, 2, 1),
    _Hh3cDot11WIDSRogueMAC_Type()
)
hh3cDot11WIDSRogueMAC.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11WIDSRogueMAC.setStatus("current")


class _Hh3cDot11WIDSRogueType_Type(Integer32):
    """Custom type hh3cDot11WIDSRogueType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rogueAp", 1),
          ("rogueStation", 2))
    )


_Hh3cDot11WIDSRogueType_Type.__name__ = "Integer32"
_Hh3cDot11WIDSRogueType_Object = MibScalar
hh3cDot11WIDSRogueType = _Hh3cDot11WIDSRogueType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 3, 2, 2),
    _Hh3cDot11WIDSRogueType_Type()
)
hh3cDot11WIDSRogueType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11WIDSRogueType.setStatus("current")
_Hh3cDot11WIDSMonitorMAC_Type = MacAddress
_Hh3cDot11WIDSMonitorMAC_Object = MibScalar
hh3cDot11WIDSMonitorMAC = _Hh3cDot11WIDSMonitorMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 3, 2, 3),
    _Hh3cDot11WIDSMonitorMAC_Type()
)
hh3cDot11WIDSMonitorMAC.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11WIDSMonitorMAC.setStatus("current")
_Hh3cDot11WIDSAdHocMAC_Type = MacAddress
_Hh3cDot11WIDSAdHocMAC_Object = MibScalar
hh3cDot11WIDSAdHocMAC = _Hh3cDot11WIDSAdHocMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 3, 2, 4),
    _Hh3cDot11WIDSAdHocMAC_Type()
)
hh3cDot11WIDSAdHocMAC.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11WIDSAdHocMAC.setStatus("current")
_Hh3cDot11UnauthorSSIDName_Type = Hh3cDot11SSIDStringType
_Hh3cDot11UnauthorSSIDName_Object = MibScalar
hh3cDot11UnauthorSSIDName = _Hh3cDot11UnauthorSSIDName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 3, 2, 5),
    _Hh3cDot11UnauthorSSIDName_Type()
)
hh3cDot11UnauthorSSIDName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11UnauthorSSIDName.setStatus("current")
_Hh3cDot11MonitorAPID_Type = Hh3cDot11ObjectIDType
_Hh3cDot11MonitorAPID_Object = MibScalar
hh3cDot11MonitorAPID = _Hh3cDot11MonitorAPID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 3, 2, 6),
    _Hh3cDot11MonitorAPID_Type()
)
hh3cDot11MonitorAPID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11MonitorAPID.setStatus("current")
_Hh3cDot11MonitorApRadioID_Type = Hh3cDot11RadioScopeType
_Hh3cDot11MonitorApRadioID_Object = MibScalar
hh3cDot11MonitorApRadioID = _Hh3cDot11MonitorApRadioID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 3, 2, 7),
    _Hh3cDot11MonitorApRadioID_Type()
)
hh3cDot11MonitorApRadioID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11MonitorApRadioID.setStatus("current")
_Hh3cDot11WIDSAtkMac_Type = MacAddress
_Hh3cDot11WIDSAtkMac_Object = MibScalar
hh3cDot11WIDSAtkMac = _Hh3cDot11WIDSAtkMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 3, 2, 8),
    _Hh3cDot11WIDSAtkMac_Type()
)
hh3cDot11WIDSAtkMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11WIDSAtkMac.setStatus("current")
_Hh3cDot11WIDSAtkFrameType_Type = OctetString
_Hh3cDot11WIDSAtkFrameType_Object = MibScalar
hh3cDot11WIDSAtkFrameType = _Hh3cDot11WIDSAtkFrameType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 3, 2, 9),
    _Hh3cDot11WIDSAtkFrameType_Type()
)
hh3cDot11WIDSAtkFrameType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11WIDSAtkFrameType.setStatus("current")
_Hh3cDot11WIDSAtkChannel_Type = Hh3cDot11ChannelScopeType
_Hh3cDot11WIDSAtkChannel_Object = MibScalar
hh3cDot11WIDSAtkChannel = _Hh3cDot11WIDSAtkChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 3, 2, 10),
    _Hh3cDot11WIDSAtkChannel_Type()
)
hh3cDot11WIDSAtkChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11WIDSAtkChannel.setStatus("current")
_Hh3cDot11WIDSAtkTime_Type = OctetString
_Hh3cDot11WIDSAtkTime_Object = MibScalar
hh3cDot11WIDSAtkTime = _Hh3cDot11WIDSAtkTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 3, 2, 11),
    _Hh3cDot11WIDSAtkTime_Type()
)
hh3cDot11WIDSAtkTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11WIDSAtkTime.setStatus("current")
_Hh3cDot11WIDSAtkDestMac_Type = MacAddress
_Hh3cDot11WIDSAtkDestMac_Object = MibScalar
hh3cDot11WIDSAtkDestMac = _Hh3cDot11WIDSAtkDestMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 3, 2, 12),
    _Hh3cDot11WIDSAtkDestMac_Type()
)
hh3cDot11WIDSAtkDestMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11WIDSAtkDestMac.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cDot11WIDSDetectRogueTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 3, 1, 1)
)
hh3cDot11WIDSDetectRogueTrap.setObjects(
      *(("HH3C-DOT11-WIDS-MIB", "hh3cDot11WIDSRogueMAC"),
        ("HH3C-DOT11-WIDS-MIB", "hh3cDot11WIDSRogueType"),
        ("HH3C-DOT11-WIDS-MIB", "hh3cDot11WIDSMonitorMAC"),
        ("HH3C-DOT11-WIDS-MIB", "hh3cDot11MonitorAPID"),
        ("HH3C-DOT11-WIDS-MIB", "hh3cDot11MonitorApRadioID"))
)
if mibBuilder.loadTexts:
    hh3cDot11WIDSDetectRogueTrap.setStatus(
        "current"
    )

hh3cDot11WIDSAdHocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 3, 1, 2)
)
hh3cDot11WIDSAdHocTrap.setObjects(
      *(("HH3C-DOT11-WIDS-MIB", "hh3cDot11WIDSAdHocMAC"),
        ("HH3C-DOT11-WIDS-MIB", "hh3cDot11WIDSMonitorMAC"))
)
if mibBuilder.loadTexts:
    hh3cDot11WIDSAdHocTrap.setStatus(
        "current"
    )

hh3cDot11WIDSUnauthorSSIDTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 3, 1, 3)
)
hh3cDot11WIDSUnauthorSSIDTrap.setObjects(
      *(("HH3C-DOT11-WIDS-MIB", "hh3cDot11UnauthorSSIDName"),
        ("HH3C-DOT11-WIDS-MIB", "hh3cDot11WIDSMonitorMAC"),
        ("HH3C-DOT11-WIDS-MIB", "hh3cDot11MonitorAPID"),
        ("HH3C-DOT11-WIDS-MIB", "hh3cDot11MonitorApRadioID"))
)
if mibBuilder.loadTexts:
    hh3cDot11WIDSUnauthorSSIDTrap.setStatus(
        "current"
    )

hh3cDot11WIDSDisappearRogueTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 3, 1, 4)
)
hh3cDot11WIDSDisappearRogueTrap.setObjects(
    ("HH3C-DOT11-WIDS-MIB", "hh3cDot11WIDSRogueMAC")
)
if mibBuilder.loadTexts:
    hh3cDot11WIDSDisappearRogueTrap.setStatus(
        "current"
    )

hh3cDot11WIDSDetectAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 3, 1, 5)
)
hh3cDot11WIDSDetectAttack.setObjects(
      *(("HH3C-DOT11-WIDS-MIB", "hh3cDot11WIDSAtkHisType"),
        ("HH3C-DOT11-WIDS-MIB", "hh3cDot11WIDSAtkHisChl"),
        ("HH3C-DOT11-WIDS-MIB", "hh3cDot11WIDSAtkHisDctTime"),
        ("HH3C-DOT11-WIDS-MIB", "hh3cDot11WIDSAtkHisAPName"))
)
if mibBuilder.loadTexts:
    hh3cDot11WIDSDetectAttack.setStatus(
        "current"
    )

hh3cDot11WIDSDetectWBridge = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 3, 1, 6)
)
hh3cDot11WIDSDetectWBridge.setObjects(
      *(("HH3C-DOT11-WIDS-MIB", "hh3cDot11WIDSRptAPName"),
        ("HH3C-DOT11-WIDS-MIB", "hh3cDot11WIDSRptAPRadioID"),
        ("HH3C-DOT11-WIDS-MIB", "hh3cDot11WIDSRptAPLstDctTime"))
)
if mibBuilder.loadTexts:
    hh3cDot11WIDSDetectWBridge.setStatus(
        "current"
    )

hh3cDot11WIDSFloodTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 3, 1, 7)
)
hh3cDot11WIDSFloodTrap.setObjects(
      *(("HH3C-DOT11-WIDS-MIB", "hh3cDot11WIDSAtkMac"),
        ("HH3C-DOT11-WIDS-MIB", "hh3cDot11WIDSAtkFrameType"))
)
if mibBuilder.loadTexts:
    hh3cDot11WIDSFloodTrap.setStatus(
        "current"
    )

hh3cDot11WIDSSpoofTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 3, 1, 8)
)
hh3cDot11WIDSSpoofTrap.setObjects(
      *(("HH3C-DOT11-WIDS-MIB", "hh3cDot11WIDSAtkMac"),
        ("HH3C-DOT11-WIDS-MIB", "hh3cDot11WIDSAtkFrameType"),
        ("HH3C-DOT11-WIDS-MIB", "hh3cDot11WIDSAtkChannel"),
        ("HH3C-DOT11-WIDS-MIB", "hh3cDot11WIDSAtkTime"),
        ("HH3C-DOT11-WIDS-MIB", "hh3cDot11WIDSAtkDestMac"))
)
if mibBuilder.loadTexts:
    hh3cDot11WIDSSpoofTrap.setStatus(
        "current"
    )

hh3cDot11WIDSWeakIVTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 5, 3, 1, 9)
)
hh3cDot11WIDSWeakIVTrap.setObjects(
      *(("HH3C-DOT11-WIDS-MIB", "hh3cDot11WIDSAtkMac"),
        ("HH3C-DOT11-WIDS-MIB", "hh3cDot11WIDSAtkChannel"),
        ("HH3C-DOT11-WIDS-MIB", "hh3cDot11WIDSAtkTime"),
        ("HH3C-DOT11-WIDS-MIB", "hh3cDot11WIDSAtkDestMac"))
)
if mibBuilder.loadTexts:
    hh3cDot11WIDSWeakIVTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DOT11-WIDS-MIB",
    **{"Hh3cDot11WIDSDevType": Hh3cDot11WIDSDevType,
       "Hh3cDot11WIDSDevPermitType": Hh3cDot11WIDSDevPermitType,
       "Hh3cDot11WIDSAtkType": Hh3cDot11WIDSAtkType,
       "hh3cDot11WIDS": hh3cDot11WIDS,
       "hh3cDot11WIDSConfigGroup": hh3cDot11WIDSConfigGroup,
       "hh3cDot11WIDSGlobalConfigGroup": hh3cDot11WIDSGlobalConfigGroup,
       "hh3cDot11WIDSScanMode": hh3cDot11WIDSScanMode,
       "hh3cDot11WIDSScanChannelList": hh3cDot11WIDSScanChannelList,
       "hh3cDot11CntMsrMode": hh3cDot11CntMsrMode,
       "hh3cDot11DevAgingTime": hh3cDot11DevAgingTime,
       "hh3cDot11DynBlkListEnable": hh3cDot11DynBlkListEnable,
       "hh3cDot11DynBlkListLifeTime": hh3cDot11DynBlkListLifeTime,
       "hh3cDot11FloodAtkDctEnable": hh3cDot11FloodAtkDctEnable,
       "hh3cDot11SpoofAtkDctEnable": hh3cDot11SpoofAtkDctEnable,
       "hh3cDot11WeakIVAtkDctEnable": hh3cDot11WeakIVAtkDctEnable,
       "hh3cDot11ResetWIDSRogueHistory": hh3cDot11ResetWIDSRogueHistory,
       "hh3cDot11ResetWIDSHistroy": hh3cDot11ResetWIDSHistroy,
       "hh3cDot11ResetWIDSStatistics": hh3cDot11ResetWIDSStatistics,
       "hh3cDot11ResetAllDynBlkList": hh3cDot11ResetAllDynBlkList,
       "hh3cDot11ResetAllStcBlkList": hh3cDot11ResetAllStcBlkList,
       "hh3cDot11ResetAllWhtBlkList": hh3cDot11ResetAllWhtBlkList,
       "hh3cDot11ResetAllDctRogueAP": hh3cDot11ResetAllDctRogueAP,
       "hh3cDot11ResetAllDctRogueSta": hh3cDot11ResetAllDctRogueSta,
       "hh3cDot11ResetAllDctAdhoc": hh3cDot11ResetAllDctAdhoc,
       "hh3cDot11ResetAllDctDevice": hh3cDot11ResetAllDctDevice,
       "hh3cDot11ResetAllDctSSID": hh3cDot11ResetAllDctSSID,
       "hh3cDot11WidsFloodInterval": hh3cDot11WidsFloodInterval,
       "hh3cDot11WidsBlackListThreshold": hh3cDot11WidsBlackListThreshold,
       "hh3cDot11SSIDFilterOnOff": hh3cDot11SSIDFilterOnOff,
       "hh3cDot11BSSIDFilterOnOff": hh3cDot11BSSIDFilterOnOff,
       "hh3cDot11WIDSPermitVendorTable": hh3cDot11WIDSPermitVendorTable,
       "hh3cDot11WIDSPermitVendorEntry": hh3cDot11WIDSPermitVendorEntry,
       "hh3cDot11VendorOUI": hh3cDot11VendorOUI,
       "hh3cDot11PermitVendorRowStatus": hh3cDot11PermitVendorRowStatus,
       "hh3cDot11VendorName": hh3cDot11VendorName,
       "hh3cDot11WIDSPermitSSIDTable": hh3cDot11WIDSPermitSSIDTable,
       "hh3cDot11WIDSPermitSSIDEntry": hh3cDot11WIDSPermitSSIDEntry,
       "hh3cDot11PermitSSID": hh3cDot11PermitSSID,
       "hh3cDot11PermitSSIDRowStatus": hh3cDot11PermitSSIDRowStatus,
       "hh3cDot11PermitSSIDDetected": hh3cDot11PermitSSIDDetected,
       "hh3cDot11WIDSIgnoreListTable": hh3cDot11WIDSIgnoreListTable,
       "hh3cDot11WIDSIgnoreListEntry": hh3cDot11WIDSIgnoreListEntry,
       "hh3cDot11IgnoreMAC": hh3cDot11IgnoreMAC,
       "hh3cDot11IgnoreListRowStatus": hh3cDot11IgnoreListRowStatus,
       "hh3cDot11IgnoreMACDetected": hh3cDot11IgnoreMACDetected,
       "hh3cDot11IgnoreDevType": hh3cDot11IgnoreDevType,
       "hh3cDot11WIDSAttackListTable": hh3cDot11WIDSAttackListTable,
       "hh3cDot11WIDSAttackListEntry": hh3cDot11WIDSAttackListEntry,
       "hh3cDot11AttackDeviceMac": hh3cDot11AttackDeviceMac,
       "hh3cDot11AttackListRowStatus": hh3cDot11AttackListRowStatus,
       "hh3cDot11AttackDevDetected": hh3cDot11AttackDevDetected,
       "hh3cDot11AttackDevType": hh3cDot11AttackDevType,
       "hh3cDot11StaticWhiteListTable": hh3cDot11StaticWhiteListTable,
       "hh3cDot11StaticWhiteListEntry": hh3cDot11StaticWhiteListEntry,
       "hh3cDot11StaticWhiteListMAC": hh3cDot11StaticWhiteListMAC,
       "hh3cDot11StaticWhiteListRowStatus": hh3cDot11StaticWhiteListRowStatus,
       "hh3cDot11StaticBlackListTable": hh3cDot11StaticBlackListTable,
       "hh3cDot11StaticBlackListEntry": hh3cDot11StaticBlackListEntry,
       "hh3cDot11StaticBlackListMAC": hh3cDot11StaticBlackListMAC,
       "hh3cDot11StaticBlackListRowStatus": hh3cDot11StaticBlackListRowStatus,
       "hh3cDot11WIDSPermitBSSIDTable": hh3cDot11WIDSPermitBSSIDTable,
       "hh3cDot11WIDSPermitBSSIDEntry": hh3cDot11WIDSPermitBSSIDEntry,
       "hh3cDot11PermitBSSID": hh3cDot11PermitBSSID,
       "hh3cDot11PermitBSSIDDetected": hh3cDot11PermitBSSIDDetected,
       "hh3cDot11PermitBSSIDRowStatus": hh3cDot11PermitBSSIDRowStatus,
       "hh3cDot11WIDSDetectGroup": hh3cDot11WIDSDetectGroup,
       "hh3cDot11WIDSRogueAPTable": hh3cDot11WIDSRogueAPTable,
       "hh3cDot11WIDSRogueAPEntry": hh3cDot11WIDSRogueAPEntry,
       "hh3cDot11RogueAPBSSMAC": hh3cDot11RogueAPBSSMAC,
       "hh3cDot11RogueAPVendorName": hh3cDot11RogueAPVendorName,
       "hh3cDot11RogueAPMonitorNum": hh3cDot11RogueAPMonitorNum,
       "hh3cDot11RogueAPFirstDetectTm": hh3cDot11RogueAPFirstDetectTm,
       "hh3cDot11RogueAPLastDetectTm": hh3cDot11RogueAPLastDetectTm,
       "hh3cDot11RogueAPSSID": hh3cDot11RogueAPSSID,
       "hh3cDot11RogueAPMaxSigStrength": hh3cDot11RogueAPMaxSigStrength,
       "hh3cDot11RogueAPChannel": hh3cDot11RogueAPChannel,
       "hh3cDot11RogueAPBeaconInterval": hh3cDot11RogueAPBeaconInterval,
       "hh3cDot11RogueAPAttackedStatus": hh3cDot11RogueAPAttackedStatus,
       "hh3cDot11RogueAPToIgnore": hh3cDot11RogueAPToIgnore,
       "hh3cDot11RogueAPEncryptStatus": hh3cDot11RogueAPEncryptStatus,
       "hh3cDot11RogueAPReset": hh3cDot11RogueAPReset,
       "hh3cDot11RogueAPFirstDetectTmStr": hh3cDot11RogueAPFirstDetectTmStr,
       "hh3cDot11RogueAPLastDetectTmStr": hh3cDot11RogueAPLastDetectTmStr,
       "hh3cDot11WIDSRogueAPExtTable": hh3cDot11WIDSRogueAPExtTable,
       "hh3cDot11WIDSRogueAPExtEntry": hh3cDot11WIDSRogueAPExtEntry,
       "hh3cDot11WIDSAPID": hh3cDot11WIDSAPID,
       "hh3cDot11DetectCurAPSigStrength": hh3cDot11DetectCurAPSigStrength,
       "hh3cDot11DetectAPByChannel": hh3cDot11DetectAPByChannel,
       "hh3cDot11DetectAPByRadioID": hh3cDot11DetectAPByRadioID,
       "hh3cDot11AttackAPStatus": hh3cDot11AttackAPStatus,
       "hh3cDot11DetectAPFirstTm": hh3cDot11DetectAPFirstTm,
       "hh3cDot11DetectAPLastTm": hh3cDot11DetectAPLastTm,
       "hh3cDot11WIDSRogueStaTable": hh3cDot11WIDSRogueStaTable,
       "hh3cDot11WIDSRogueStaEntry": hh3cDot11WIDSRogueStaEntry,
       "hh3cDot11RogueStaMAC": hh3cDot11RogueStaMAC,
       "hh3cDot11RogueStaVendorName": hh3cDot11RogueStaVendorName,
       "hh3cDot11RogueStaMonitorNum": hh3cDot11RogueStaMonitorNum,
       "hh3cDot11RogueStaFirstDetectTm": hh3cDot11RogueStaFirstDetectTm,
       "hh3cDot11RogueStaLastDetectTm": hh3cDot11RogueStaLastDetectTm,
       "hh3cDot11RogueStaAccessBSSID": hh3cDot11RogueStaAccessBSSID,
       "hh3cDot11RogueStaMaxSigStrength": hh3cDot11RogueStaMaxSigStrength,
       "hh3cDot11RogueStaChannel": hh3cDot11RogueStaChannel,
       "hh3cDot11RogueStaAttackedStatus": hh3cDot11RogueStaAttackedStatus,
       "hh3cDot11RogueStaToIgnore": hh3cDot11RogueStaToIgnore,
       "hh3cDot11RogueStaAdHocStatus": hh3cDot11RogueStaAdHocStatus,
       "hh3cDot11RogueStaReset": hh3cDot11RogueStaReset,
       "hh3cDot11RogueStaFirstDetectTmStr": hh3cDot11RogueStaFirstDetectTmStr,
       "hh3cDot11RogueStaLastDetectTmStr": hh3cDot11RogueStaLastDetectTmStr,
       "hh3cDot11WIDSRogueStaExtTable": hh3cDot11WIDSRogueStaExtTable,
       "hh3cDot11WIDSRogueStaExtEntry": hh3cDot11WIDSRogueStaExtEntry,
       "hh3cDot11DetectCurStaSigStrength": hh3cDot11DetectCurStaSigStrength,
       "hh3cDot11DetectStaByChannel": hh3cDot11DetectStaByChannel,
       "hh3cDot11DetectStaByRadioID": hh3cDot11DetectStaByRadioID,
       "hh3cDot11AttackStaStatus": hh3cDot11AttackStaStatus,
       "hh3cDot11DetectStaFirstTm": hh3cDot11DetectStaFirstTm,
       "hh3cDot11DetectStaLastTm": hh3cDot11DetectStaLastTm,
       "hh3cDot11WIDSDetectedDevTable": hh3cDot11WIDSDetectedDevTable,
       "hh3cDot11WIDSDetectedDevEntry": hh3cDot11WIDSDetectedDevEntry,
       "hh3cDot11WIDSDevMAC": hh3cDot11WIDSDevMAC,
       "hh3cDot11WIDSDevType": hh3cDot11WIDSDevType,
       "hh3cDot11WIDSDevPermitType": hh3cDot11WIDSDevPermitType,
       "hh3cDot11WIDSDevVendor": hh3cDot11WIDSDevVendor,
       "hh3cDot11WIDSDevMonitorNum": hh3cDot11WIDSDevMonitorNum,
       "hh3cDot11WIDSDevSSID": hh3cDot11WIDSDevSSID,
       "hh3cDot11WIDSDevBSSID": hh3cDot11WIDSDevBSSID,
       "hh3cDot11WIDSDevChannel": hh3cDot11WIDSDevChannel,
       "hh3cDot11WIDSDevMaxRSSI": hh3cDot11WIDSDevMaxRSSI,
       "hh3cDot11WIDSDevBeaconIntvl": hh3cDot11WIDSDevBeaconIntvl,
       "hh3cDot11WIDSDevFstDctTime": hh3cDot11WIDSDevFstDctTime,
       "hh3cDot11WIDSDevLstDctTime": hh3cDot11WIDSDevLstDctTime,
       "hh3cDot11WIDSDevReset": hh3cDot11WIDSDevReset,
       "hh3cDot11WIDSDevSnr": hh3cDot11WIDSDevSnr,
       "hh3cDot11WIDSRptAPTable": hh3cDot11WIDSRptAPTable,
       "hh3cDot11WIDSRptAPEntry": hh3cDot11WIDSRptAPEntry,
       "hh3cDot11WIDSRptAPMAC": hh3cDot11WIDSRptAPMAC,
       "hh3cDot11WIDSRptAPName": hh3cDot11WIDSRptAPName,
       "hh3cDot11WIDSRptAPRadioID": hh3cDot11WIDSRptAPRadioID,
       "hh3cDot11WIDSRptAPMaxRSSI": hh3cDot11WIDSRptAPMaxRSSI,
       "hh3cDot11WIDSRptAPFstDctTime": hh3cDot11WIDSRptAPFstDctTime,
       "hh3cDot11WIDSRptAPLstDctTime": hh3cDot11WIDSRptAPLstDctTime,
       "hh3cDot11DynBlackListTable": hh3cDot11DynBlackListTable,
       "hh3cDot11DynBlackListEntry": hh3cDot11DynBlackListEntry,
       "hh3cDot11DynBlackListMAC": hh3cDot11DynBlackListMAC,
       "hh3cDot11DynBlackListTime": hh3cDot11DynBlackListTime,
       "hh3cDot11DynBlackListReason": hh3cDot11DynBlackListReason,
       "hh3cDot11DynBlackListReset": hh3cDot11DynBlackListReset,
       "hh3cDot11DynBlackListTimeTicks": hh3cDot11DynBlackListTimeTicks,
       "hh3cDot11WIDSRogueHistoryTable": hh3cDot11WIDSRogueHistoryTable,
       "hh3cDot11WIDSRogueHistoryEntry": hh3cDot11WIDSRogueHistoryEntry,
       "hh3cDot11WIDSRogueHisIndex": hh3cDot11WIDSRogueHisIndex,
       "hh3cDot11WIDSRogueHisMAC": hh3cDot11WIDSRogueHisMAC,
       "hh3cDot11WIDSRogueHisVendor": hh3cDot11WIDSRogueHisVendor,
       "hh3cDot11WIDSRogueHisType": hh3cDot11WIDSRogueHisType,
       "hh3cDot11WIDSRogueHisChl": hh3cDot11WIDSRogueHisChl,
       "hh3cDot11WIDSRogueHisSSID": hh3cDot11WIDSRogueHisSSID,
       "hh3cDot11WIDSRogueHisLastDctTime": hh3cDot11WIDSRogueHisLastDctTime,
       "hh3cDot11WIDSAtkHistroyTable": hh3cDot11WIDSAtkHistroyTable,
       "hh3cDot11WIDSAtkHistroyEntry": hh3cDot11WIDSAtkHistroyEntry,
       "hh3cDot11WIDSAtkHisIndex": hh3cDot11WIDSAtkHisIndex,
       "hh3cDot11WIDSAtkHisMAC": hh3cDot11WIDSAtkHisMAC,
       "hh3cDot11WIDSAtkHisType": hh3cDot11WIDSAtkHisType,
       "hh3cDot11WIDSAtkHisChl": hh3cDot11WIDSAtkHisChl,
       "hh3cDot11WIDSAtkHisRSSI": hh3cDot11WIDSAtkHisRSSI,
       "hh3cDot11WIDSAtkHisDctTime": hh3cDot11WIDSAtkHisDctTime,
       "hh3cDot11WIDSAtkHisAPName": hh3cDot11WIDSAtkHisAPName,
       "hh3cDot11WIDSAtkStatis": hh3cDot11WIDSAtkStatis,
       "hh3cDot11WIDSAtkStasStartTime": hh3cDot11WIDSAtkStasStartTime,
       "hh3cDot11WIDSAtkStasTable": hh3cDot11WIDSAtkStasTable,
       "hh3cDot11WIDSAtkStasEntry": hh3cDot11WIDSAtkStasEntry,
       "hh3cDot11WIDSAtkStasType": hh3cDot11WIDSAtkStasType,
       "hh3cDot11WIDSAtkStasCurCnt": hh3cDot11WIDSAtkStasCurCnt,
       "hh3cDot11WIDSAtkStasTotalCnt": hh3cDot11WIDSAtkStasTotalCnt,
       "hh3cDot11BlackListTable": hh3cDot11BlackListTable,
       "hh3cDot11BlackListEntry": hh3cDot11BlackListEntry,
       "hh3cDot11BlackListMAC": hh3cDot11BlackListMAC,
       "hh3cDot11BlackListTime": hh3cDot11BlackListTime,
       "hh3cDot11BlackListReason": hh3cDot11BlackListReason,
       "hh3cDot11BlackListRowStatus": hh3cDot11BlackListRowStatus,
       "hh3cDot11BlackListTimeTicks": hh3cDot11BlackListTimeTicks,
       "hh3cDot11WIDSNotifyGroup": hh3cDot11WIDSNotifyGroup,
       "hh3cDot11WIDSTraps": hh3cDot11WIDSTraps,
       "hh3cDot11WIDSDetectRogueTrap": hh3cDot11WIDSDetectRogueTrap,
       "hh3cDot11WIDSAdHocTrap": hh3cDot11WIDSAdHocTrap,
       "hh3cDot11WIDSUnauthorSSIDTrap": hh3cDot11WIDSUnauthorSSIDTrap,
       "hh3cDot11WIDSDisappearRogueTrap": hh3cDot11WIDSDisappearRogueTrap,
       "hh3cDot11WIDSDetectAttack": hh3cDot11WIDSDetectAttack,
       "hh3cDot11WIDSDetectWBridge": hh3cDot11WIDSDetectWBridge,
       "hh3cDot11WIDSFloodTrap": hh3cDot11WIDSFloodTrap,
       "hh3cDot11WIDSSpoofTrap": hh3cDot11WIDSSpoofTrap,
       "hh3cDot11WIDSWeakIVTrap": hh3cDot11WIDSWeakIVTrap,
       "hh3cDot11WIDSTrapVarObjects": hh3cDot11WIDSTrapVarObjects,
       "hh3cDot11WIDSRogueMAC": hh3cDot11WIDSRogueMAC,
       "hh3cDot11WIDSRogueType": hh3cDot11WIDSRogueType,
       "hh3cDot11WIDSMonitorMAC": hh3cDot11WIDSMonitorMAC,
       "hh3cDot11WIDSAdHocMAC": hh3cDot11WIDSAdHocMAC,
       "hh3cDot11UnauthorSSIDName": hh3cDot11UnauthorSSIDName,
       "hh3cDot11MonitorAPID": hh3cDot11MonitorAPID,
       "hh3cDot11MonitorApRadioID": hh3cDot11MonitorApRadioID,
       "hh3cDot11WIDSAtkMac": hh3cDot11WIDSAtkMac,
       "hh3cDot11WIDSAtkFrameType": hh3cDot11WIDSAtkFrameType,
       "hh3cDot11WIDSAtkChannel": hh3cDot11WIDSAtkChannel,
       "hh3cDot11WIDSAtkTime": hh3cDot11WIDSAtkTime,
       "hh3cDot11WIDSAtkDestMac": hh3cDot11WIDSAtkDestMac}
)
