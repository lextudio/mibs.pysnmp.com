# SNMP MIB module (HPN-ICF-DOT11-WIDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-DOT11-WIDS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:56 2024
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

(HpnicfDot11ChannelScopeType,
 HpnicfDot11ObjectIDType,
 HpnicfDot11RadioScopeType,
 HpnicfDot11RadioType,
 HpnicfDot11SSIDStringType,
 hpnicfDot11) = mibBuilder.importSymbols(
    "HPN-ICF-DOT11-REF-MIB",
    "HpnicfDot11ChannelScopeType",
    "HpnicfDot11ObjectIDType",
    "HpnicfDot11RadioScopeType",
    "HpnicfDot11RadioType",
    "HpnicfDot11SSIDStringType",
    "hpnicfDot11")

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

hpnicfDot11WIDS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5)
)
hpnicfDot11WIDS.setRevisions(
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



class HpnicfDot11WIDSDevType(Integer32, TextualConvention):
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



class HpnicfDot11WIDSDevPermitType(Integer32, TextualConvention):
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



class HpnicfDot11WIDSAtkType(Integer32, TextualConvention):
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

_HpnicfDot11WIDSConfigGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11WIDSConfigGroup = _HpnicfDot11WIDSConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1)
)
_HpnicfDot11WIDSGlobalConfigGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11WIDSGlobalConfigGroup = _HpnicfDot11WIDSGlobalConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 1)
)


class _HpnicfDot11WIDSScanMode_Type(Integer32):
    """Custom type hpnicfDot11WIDSScanMode based on Integer32"""
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


_HpnicfDot11WIDSScanMode_Type.__name__ = "Integer32"
_HpnicfDot11WIDSScanMode_Object = MibScalar
hpnicfDot11WIDSScanMode = _HpnicfDot11WIDSScanMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 1, 1),
    _HpnicfDot11WIDSScanMode_Type()
)
hpnicfDot11WIDSScanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSScanMode.setStatus("current")


class _HpnicfDot11WIDSScanChannelList_Type(OctetString):
    """Custom type hpnicfDot11WIDSScanChannelList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpnicfDot11WIDSScanChannelList_Type.__name__ = "OctetString"
_HpnicfDot11WIDSScanChannelList_Object = MibScalar
hpnicfDot11WIDSScanChannelList = _HpnicfDot11WIDSScanChannelList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 1, 2),
    _HpnicfDot11WIDSScanChannelList_Type()
)
hpnicfDot11WIDSScanChannelList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSScanChannelList.setStatus("obsolete")


class _HpnicfDot11CntMsrMode_Type(Bits):
    """Custom type hpnicfDot11CntMsrMode based on Bits"""
    namedValues = NamedValues(
        *(("adhoc", 1),
          ("config", 2),
          ("rogue", 0))
    )

_HpnicfDot11CntMsrMode_Type.__name__ = "Bits"
_HpnicfDot11CntMsrMode_Object = MibScalar
hpnicfDot11CntMsrMode = _HpnicfDot11CntMsrMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 1, 3),
    _HpnicfDot11CntMsrMode_Type()
)
hpnicfDot11CntMsrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11CntMsrMode.setStatus("current")


class _HpnicfDot11DevAgingTime_Type(Integer32):
    """Custom type hpnicfDot11DevAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1800),
    )


_HpnicfDot11DevAgingTime_Type.__name__ = "Integer32"
_HpnicfDot11DevAgingTime_Object = MibScalar
hpnicfDot11DevAgingTime = _HpnicfDot11DevAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 1, 4),
    _HpnicfDot11DevAgingTime_Type()
)
hpnicfDot11DevAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11DevAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11DevAgingTime.setUnits("second")
_HpnicfDot11DynBlkListEnable_Type = TruthValue
_HpnicfDot11DynBlkListEnable_Object = MibScalar
hpnicfDot11DynBlkListEnable = _HpnicfDot11DynBlkListEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 1, 5),
    _HpnicfDot11DynBlkListEnable_Type()
)
hpnicfDot11DynBlkListEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11DynBlkListEnable.setStatus("current")


class _HpnicfDot11DynBlkListLifeTime_Type(Integer32):
    """Custom type hpnicfDot11DynBlkListLifeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_HpnicfDot11DynBlkListLifeTime_Type.__name__ = "Integer32"
_HpnicfDot11DynBlkListLifeTime_Object = MibScalar
hpnicfDot11DynBlkListLifeTime = _HpnicfDot11DynBlkListLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 1, 6),
    _HpnicfDot11DynBlkListLifeTime_Type()
)
hpnicfDot11DynBlkListLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11DynBlkListLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11DynBlkListLifeTime.setUnits("second")
_HpnicfDot11FloodAtkDctEnable_Type = TruthValue
_HpnicfDot11FloodAtkDctEnable_Object = MibScalar
hpnicfDot11FloodAtkDctEnable = _HpnicfDot11FloodAtkDctEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 1, 7),
    _HpnicfDot11FloodAtkDctEnable_Type()
)
hpnicfDot11FloodAtkDctEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11FloodAtkDctEnable.setStatus("current")
_HpnicfDot11SpoofAtkDctEnable_Type = TruthValue
_HpnicfDot11SpoofAtkDctEnable_Object = MibScalar
hpnicfDot11SpoofAtkDctEnable = _HpnicfDot11SpoofAtkDctEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 1, 8),
    _HpnicfDot11SpoofAtkDctEnable_Type()
)
hpnicfDot11SpoofAtkDctEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11SpoofAtkDctEnable.setStatus("current")
_HpnicfDot11WeakIVAtkDctEnable_Type = TruthValue
_HpnicfDot11WeakIVAtkDctEnable_Object = MibScalar
hpnicfDot11WeakIVAtkDctEnable = _HpnicfDot11WeakIVAtkDctEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 1, 9),
    _HpnicfDot11WeakIVAtkDctEnable_Type()
)
hpnicfDot11WeakIVAtkDctEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11WeakIVAtkDctEnable.setStatus("current")
_HpnicfDot11ResetWIDSRogueHistory_Type = TruthValue
_HpnicfDot11ResetWIDSRogueHistory_Object = MibScalar
hpnicfDot11ResetWIDSRogueHistory = _HpnicfDot11ResetWIDSRogueHistory_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 1, 10),
    _HpnicfDot11ResetWIDSRogueHistory_Type()
)
hpnicfDot11ResetWIDSRogueHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11ResetWIDSRogueHistory.setStatus("current")
_HpnicfDot11ResetWIDSHistroy_Type = TruthValue
_HpnicfDot11ResetWIDSHistroy_Object = MibScalar
hpnicfDot11ResetWIDSHistroy = _HpnicfDot11ResetWIDSHistroy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 1, 11),
    _HpnicfDot11ResetWIDSHistroy_Type()
)
hpnicfDot11ResetWIDSHistroy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11ResetWIDSHistroy.setStatus("current")
_HpnicfDot11ResetWIDSStatistics_Type = TruthValue
_HpnicfDot11ResetWIDSStatistics_Object = MibScalar
hpnicfDot11ResetWIDSStatistics = _HpnicfDot11ResetWIDSStatistics_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 1, 12),
    _HpnicfDot11ResetWIDSStatistics_Type()
)
hpnicfDot11ResetWIDSStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11ResetWIDSStatistics.setStatus("current")
_HpnicfDot11ResetAllDynBlkList_Type = TruthValue
_HpnicfDot11ResetAllDynBlkList_Object = MibScalar
hpnicfDot11ResetAllDynBlkList = _HpnicfDot11ResetAllDynBlkList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 1, 13),
    _HpnicfDot11ResetAllDynBlkList_Type()
)
hpnicfDot11ResetAllDynBlkList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11ResetAllDynBlkList.setStatus("current")
_HpnicfDot11ResetAllStcBlkList_Type = TruthValue
_HpnicfDot11ResetAllStcBlkList_Object = MibScalar
hpnicfDot11ResetAllStcBlkList = _HpnicfDot11ResetAllStcBlkList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 1, 14),
    _HpnicfDot11ResetAllStcBlkList_Type()
)
hpnicfDot11ResetAllStcBlkList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11ResetAllStcBlkList.setStatus("current")
_HpnicfDot11ResetAllWhtBlkList_Type = TruthValue
_HpnicfDot11ResetAllWhtBlkList_Object = MibScalar
hpnicfDot11ResetAllWhtBlkList = _HpnicfDot11ResetAllWhtBlkList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 1, 15),
    _HpnicfDot11ResetAllWhtBlkList_Type()
)
hpnicfDot11ResetAllWhtBlkList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11ResetAllWhtBlkList.setStatus("current")
_HpnicfDot11ResetAllDctRogueAP_Type = TruthValue
_HpnicfDot11ResetAllDctRogueAP_Object = MibScalar
hpnicfDot11ResetAllDctRogueAP = _HpnicfDot11ResetAllDctRogueAP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 1, 16),
    _HpnicfDot11ResetAllDctRogueAP_Type()
)
hpnicfDot11ResetAllDctRogueAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11ResetAllDctRogueAP.setStatus("current")
_HpnicfDot11ResetAllDctRogueSta_Type = TruthValue
_HpnicfDot11ResetAllDctRogueSta_Object = MibScalar
hpnicfDot11ResetAllDctRogueSta = _HpnicfDot11ResetAllDctRogueSta_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 1, 17),
    _HpnicfDot11ResetAllDctRogueSta_Type()
)
hpnicfDot11ResetAllDctRogueSta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11ResetAllDctRogueSta.setStatus("current")
_HpnicfDot11ResetAllDctAdhoc_Type = TruthValue
_HpnicfDot11ResetAllDctAdhoc_Object = MibScalar
hpnicfDot11ResetAllDctAdhoc = _HpnicfDot11ResetAllDctAdhoc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 1, 18),
    _HpnicfDot11ResetAllDctAdhoc_Type()
)
hpnicfDot11ResetAllDctAdhoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11ResetAllDctAdhoc.setStatus("current")
_HpnicfDot11ResetAllDctDevice_Type = TruthValue
_HpnicfDot11ResetAllDctDevice_Object = MibScalar
hpnicfDot11ResetAllDctDevice = _HpnicfDot11ResetAllDctDevice_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 1, 19),
    _HpnicfDot11ResetAllDctDevice_Type()
)
hpnicfDot11ResetAllDctDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11ResetAllDctDevice.setStatus("current")
_HpnicfDot11ResetAllDctSSID_Type = TruthValue
_HpnicfDot11ResetAllDctSSID_Object = MibScalar
hpnicfDot11ResetAllDctSSID = _HpnicfDot11ResetAllDctSSID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 1, 20),
    _HpnicfDot11ResetAllDctSSID_Type()
)
hpnicfDot11ResetAllDctSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11ResetAllDctSSID.setStatus("current")


class _HpnicfDot11WidsFloodInterval_Type(Unsigned32):
    """Custom type hpnicfDot11WidsFloodInterval based on Unsigned32"""
    defaultValue = 1


_HpnicfDot11WidsFloodInterval_Object = MibScalar
hpnicfDot11WidsFloodInterval = _HpnicfDot11WidsFloodInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 1, 21),
    _HpnicfDot11WidsFloodInterval_Type()
)
hpnicfDot11WidsFloodInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11WidsFloodInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11WidsFloodInterval.setUnits("second")


class _HpnicfDot11WidsBlackListThreshold_Type(Unsigned32):
    """Custom type hpnicfDot11WidsBlackListThreshold based on Unsigned32"""
    defaultValue = 100


_HpnicfDot11WidsBlackListThreshold_Object = MibScalar
hpnicfDot11WidsBlackListThreshold = _HpnicfDot11WidsBlackListThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 1, 22),
    _HpnicfDot11WidsBlackListThreshold_Type()
)
hpnicfDot11WidsBlackListThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11WidsBlackListThreshold.setStatus("current")


class _HpnicfDot11SSIDFilterOnOff_Type(Integer32):
    """Custom type hpnicfDot11SSIDFilterOnOff based on Integer32"""
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


_HpnicfDot11SSIDFilterOnOff_Type.__name__ = "Integer32"
_HpnicfDot11SSIDFilterOnOff_Object = MibScalar
hpnicfDot11SSIDFilterOnOff = _HpnicfDot11SSIDFilterOnOff_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 1, 23),
    _HpnicfDot11SSIDFilterOnOff_Type()
)
hpnicfDot11SSIDFilterOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11SSIDFilterOnOff.setStatus("current")


class _HpnicfDot11BSSIDFilterOnOff_Type(Integer32):
    """Custom type hpnicfDot11BSSIDFilterOnOff based on Integer32"""
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


_HpnicfDot11BSSIDFilterOnOff_Type.__name__ = "Integer32"
_HpnicfDot11BSSIDFilterOnOff_Object = MibScalar
hpnicfDot11BSSIDFilterOnOff = _HpnicfDot11BSSIDFilterOnOff_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 1, 24),
    _HpnicfDot11BSSIDFilterOnOff_Type()
)
hpnicfDot11BSSIDFilterOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11BSSIDFilterOnOff.setStatus("current")
_HpnicfDot11WIDSPermitVendorTable_Object = MibTable
hpnicfDot11WIDSPermitVendorTable = _HpnicfDot11WIDSPermitVendorTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfDot11WIDSPermitVendorTable.setStatus("current")
_HpnicfDot11WIDSPermitVendorEntry_Object = MibTableRow
hpnicfDot11WIDSPermitVendorEntry = _HpnicfDot11WIDSPermitVendorEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 2, 1)
)
hpnicfDot11WIDSPermitVendorEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11VendorOUI"),
)
if mibBuilder.loadTexts:
    hpnicfDot11WIDSPermitVendorEntry.setStatus("current")


class _HpnicfDot11VendorOUI_Type(OctetString):
    """Custom type hpnicfDot11VendorOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_HpnicfDot11VendorOUI_Type.__name__ = "OctetString"
_HpnicfDot11VendorOUI_Object = MibTableColumn
hpnicfDot11VendorOUI = _HpnicfDot11VendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 2, 1, 1),
    _HpnicfDot11VendorOUI_Type()
)
hpnicfDot11VendorOUI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11VendorOUI.setStatus("current")
_HpnicfDot11PermitVendorRowStatus_Type = RowStatus
_HpnicfDot11PermitVendorRowStatus_Object = MibTableColumn
hpnicfDot11PermitVendorRowStatus = _HpnicfDot11PermitVendorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 2, 1, 2),
    _HpnicfDot11PermitVendorRowStatus_Type()
)
hpnicfDot11PermitVendorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11PermitVendorRowStatus.setStatus("current")


class _HpnicfDot11VendorName_Type(OctetString):
    """Custom type hpnicfDot11VendorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfDot11VendorName_Type.__name__ = "OctetString"
_HpnicfDot11VendorName_Object = MibTableColumn
hpnicfDot11VendorName = _HpnicfDot11VendorName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 2, 1, 3),
    _HpnicfDot11VendorName_Type()
)
hpnicfDot11VendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11VendorName.setStatus("current")
_HpnicfDot11WIDSPermitSSIDTable_Object = MibTable
hpnicfDot11WIDSPermitSSIDTable = _HpnicfDot11WIDSPermitSSIDTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfDot11WIDSPermitSSIDTable.setStatus("current")
_HpnicfDot11WIDSPermitSSIDEntry_Object = MibTableRow
hpnicfDot11WIDSPermitSSIDEntry = _HpnicfDot11WIDSPermitSSIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 3, 1)
)
hpnicfDot11WIDSPermitSSIDEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11PermitSSID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11WIDSPermitSSIDEntry.setStatus("current")


class _HpnicfDot11PermitSSID_Type(HpnicfDot11SSIDStringType):
    """Custom type hpnicfDot11PermitSSID based on HpnicfDot11SSIDStringType"""
    subtypeSpec = HpnicfDot11SSIDStringType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfDot11PermitSSID_Type.__name__ = "HpnicfDot11SSIDStringType"
_HpnicfDot11PermitSSID_Object = MibTableColumn
hpnicfDot11PermitSSID = _HpnicfDot11PermitSSID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 3, 1, 1),
    _HpnicfDot11PermitSSID_Type()
)
hpnicfDot11PermitSSID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11PermitSSID.setStatus("current")
_HpnicfDot11PermitSSIDRowStatus_Type = RowStatus
_HpnicfDot11PermitSSIDRowStatus_Object = MibTableColumn
hpnicfDot11PermitSSIDRowStatus = _HpnicfDot11PermitSSIDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 3, 1, 2),
    _HpnicfDot11PermitSSIDRowStatus_Type()
)
hpnicfDot11PermitSSIDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11PermitSSIDRowStatus.setStatus("current")
_HpnicfDot11PermitSSIDDetected_Type = TruthValue
_HpnicfDot11PermitSSIDDetected_Object = MibTableColumn
hpnicfDot11PermitSSIDDetected = _HpnicfDot11PermitSSIDDetected_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 3, 1, 3),
    _HpnicfDot11PermitSSIDDetected_Type()
)
hpnicfDot11PermitSSIDDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11PermitSSIDDetected.setStatus("current")
_HpnicfDot11WIDSIgnoreListTable_Object = MibTable
hpnicfDot11WIDSIgnoreListTable = _HpnicfDot11WIDSIgnoreListTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfDot11WIDSIgnoreListTable.setStatus("current")
_HpnicfDot11WIDSIgnoreListEntry_Object = MibTableRow
hpnicfDot11WIDSIgnoreListEntry = _HpnicfDot11WIDSIgnoreListEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 4, 1)
)
hpnicfDot11WIDSIgnoreListEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11IgnoreMAC"),
)
if mibBuilder.loadTexts:
    hpnicfDot11WIDSIgnoreListEntry.setStatus("current")
_HpnicfDot11IgnoreMAC_Type = MacAddress
_HpnicfDot11IgnoreMAC_Object = MibTableColumn
hpnicfDot11IgnoreMAC = _HpnicfDot11IgnoreMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 4, 1, 1),
    _HpnicfDot11IgnoreMAC_Type()
)
hpnicfDot11IgnoreMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11IgnoreMAC.setStatus("current")
_HpnicfDot11IgnoreListRowStatus_Type = RowStatus
_HpnicfDot11IgnoreListRowStatus_Object = MibTableColumn
hpnicfDot11IgnoreListRowStatus = _HpnicfDot11IgnoreListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 4, 1, 2),
    _HpnicfDot11IgnoreListRowStatus_Type()
)
hpnicfDot11IgnoreListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11IgnoreListRowStatus.setStatus("current")
_HpnicfDot11IgnoreMACDetected_Type = TruthValue
_HpnicfDot11IgnoreMACDetected_Object = MibTableColumn
hpnicfDot11IgnoreMACDetected = _HpnicfDot11IgnoreMACDetected_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 4, 1, 3),
    _HpnicfDot11IgnoreMACDetected_Type()
)
hpnicfDot11IgnoreMACDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11IgnoreMACDetected.setStatus("current")
_HpnicfDot11IgnoreDevType_Type = HpnicfDot11WIDSDevType
_HpnicfDot11IgnoreDevType_Object = MibTableColumn
hpnicfDot11IgnoreDevType = _HpnicfDot11IgnoreDevType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 4, 1, 4),
    _HpnicfDot11IgnoreDevType_Type()
)
hpnicfDot11IgnoreDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11IgnoreDevType.setStatus("current")
_HpnicfDot11WIDSAttackListTable_Object = MibTable
hpnicfDot11WIDSAttackListTable = _HpnicfDot11WIDSAttackListTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 5)
)
if mibBuilder.loadTexts:
    hpnicfDot11WIDSAttackListTable.setStatus("current")
_HpnicfDot11WIDSAttackListEntry_Object = MibTableRow
hpnicfDot11WIDSAttackListEntry = _HpnicfDot11WIDSAttackListEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 5, 1)
)
hpnicfDot11WIDSAttackListEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11AttackDeviceMac"),
)
if mibBuilder.loadTexts:
    hpnicfDot11WIDSAttackListEntry.setStatus("current")
_HpnicfDot11AttackDeviceMac_Type = MacAddress
_HpnicfDot11AttackDeviceMac_Object = MibTableColumn
hpnicfDot11AttackDeviceMac = _HpnicfDot11AttackDeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 5, 1, 1),
    _HpnicfDot11AttackDeviceMac_Type()
)
hpnicfDot11AttackDeviceMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11AttackDeviceMac.setStatus("current")
_HpnicfDot11AttackListRowStatus_Type = RowStatus
_HpnicfDot11AttackListRowStatus_Object = MibTableColumn
hpnicfDot11AttackListRowStatus = _HpnicfDot11AttackListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 5, 1, 2),
    _HpnicfDot11AttackListRowStatus_Type()
)
hpnicfDot11AttackListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11AttackListRowStatus.setStatus("current")
_HpnicfDot11AttackDevDetected_Type = TruthValue
_HpnicfDot11AttackDevDetected_Object = MibTableColumn
hpnicfDot11AttackDevDetected = _HpnicfDot11AttackDevDetected_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 5, 1, 3),
    _HpnicfDot11AttackDevDetected_Type()
)
hpnicfDot11AttackDevDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11AttackDevDetected.setStatus("current")
_HpnicfDot11AttackDevType_Type = HpnicfDot11WIDSDevType
_HpnicfDot11AttackDevType_Object = MibTableColumn
hpnicfDot11AttackDevType = _HpnicfDot11AttackDevType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 5, 1, 4),
    _HpnicfDot11AttackDevType_Type()
)
hpnicfDot11AttackDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11AttackDevType.setStatus("current")
_HpnicfDot11StaticWhiteListTable_Object = MibTable
hpnicfDot11StaticWhiteListTable = _HpnicfDot11StaticWhiteListTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 6)
)
if mibBuilder.loadTexts:
    hpnicfDot11StaticWhiteListTable.setStatus("current")
_HpnicfDot11StaticWhiteListEntry_Object = MibTableRow
hpnicfDot11StaticWhiteListEntry = _HpnicfDot11StaticWhiteListEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 6, 1)
)
hpnicfDot11StaticWhiteListEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11StaticWhiteListMAC"),
)
if mibBuilder.loadTexts:
    hpnicfDot11StaticWhiteListEntry.setStatus("current")
_HpnicfDot11StaticWhiteListMAC_Type = MacAddress
_HpnicfDot11StaticWhiteListMAC_Object = MibTableColumn
hpnicfDot11StaticWhiteListMAC = _HpnicfDot11StaticWhiteListMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 6, 1, 1),
    _HpnicfDot11StaticWhiteListMAC_Type()
)
hpnicfDot11StaticWhiteListMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11StaticWhiteListMAC.setStatus("current")
_HpnicfDot11StaticWhiteListRowStatus_Type = RowStatus
_HpnicfDot11StaticWhiteListRowStatus_Object = MibTableColumn
hpnicfDot11StaticWhiteListRowStatus = _HpnicfDot11StaticWhiteListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 6, 1, 2),
    _HpnicfDot11StaticWhiteListRowStatus_Type()
)
hpnicfDot11StaticWhiteListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11StaticWhiteListRowStatus.setStatus("current")
_HpnicfDot11StaticBlackListTable_Object = MibTable
hpnicfDot11StaticBlackListTable = _HpnicfDot11StaticBlackListTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 7)
)
if mibBuilder.loadTexts:
    hpnicfDot11StaticBlackListTable.setStatus("current")
_HpnicfDot11StaticBlackListEntry_Object = MibTableRow
hpnicfDot11StaticBlackListEntry = _HpnicfDot11StaticBlackListEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 7, 1)
)
hpnicfDot11StaticBlackListEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11StaticBlackListMAC"),
)
if mibBuilder.loadTexts:
    hpnicfDot11StaticBlackListEntry.setStatus("current")
_HpnicfDot11StaticBlackListMAC_Type = MacAddress
_HpnicfDot11StaticBlackListMAC_Object = MibTableColumn
hpnicfDot11StaticBlackListMAC = _HpnicfDot11StaticBlackListMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 7, 1, 1),
    _HpnicfDot11StaticBlackListMAC_Type()
)
hpnicfDot11StaticBlackListMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11StaticBlackListMAC.setStatus("current")
_HpnicfDot11StaticBlackListRowStatus_Type = RowStatus
_HpnicfDot11StaticBlackListRowStatus_Object = MibTableColumn
hpnicfDot11StaticBlackListRowStatus = _HpnicfDot11StaticBlackListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 7, 1, 2),
    _HpnicfDot11StaticBlackListRowStatus_Type()
)
hpnicfDot11StaticBlackListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11StaticBlackListRowStatus.setStatus("current")
_HpnicfDot11WIDSPermitBSSIDTable_Object = MibTable
hpnicfDot11WIDSPermitBSSIDTable = _HpnicfDot11WIDSPermitBSSIDTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 8)
)
if mibBuilder.loadTexts:
    hpnicfDot11WIDSPermitBSSIDTable.setStatus("current")
_HpnicfDot11WIDSPermitBSSIDEntry_Object = MibTableRow
hpnicfDot11WIDSPermitBSSIDEntry = _HpnicfDot11WIDSPermitBSSIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 8, 1)
)
hpnicfDot11WIDSPermitBSSIDEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11PermitBSSID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11WIDSPermitBSSIDEntry.setStatus("current")
_HpnicfDot11PermitBSSID_Type = MacAddress
_HpnicfDot11PermitBSSID_Object = MibTableColumn
hpnicfDot11PermitBSSID = _HpnicfDot11PermitBSSID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 8, 1, 1),
    _HpnicfDot11PermitBSSID_Type()
)
hpnicfDot11PermitBSSID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11PermitBSSID.setStatus("current")
_HpnicfDot11PermitBSSIDDetected_Type = TruthValue
_HpnicfDot11PermitBSSIDDetected_Object = MibTableColumn
hpnicfDot11PermitBSSIDDetected = _HpnicfDot11PermitBSSIDDetected_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 8, 1, 2),
    _HpnicfDot11PermitBSSIDDetected_Type()
)
hpnicfDot11PermitBSSIDDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11PermitBSSIDDetected.setStatus("current")
_HpnicfDot11PermitBSSIDRowStatus_Type = RowStatus
_HpnicfDot11PermitBSSIDRowStatus_Object = MibTableColumn
hpnicfDot11PermitBSSIDRowStatus = _HpnicfDot11PermitBSSIDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 1, 8, 1, 3),
    _HpnicfDot11PermitBSSIDRowStatus_Type()
)
hpnicfDot11PermitBSSIDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11PermitBSSIDRowStatus.setStatus("current")
_HpnicfDot11WIDSDetectGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11WIDSDetectGroup = _HpnicfDot11WIDSDetectGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2)
)
_HpnicfDot11WIDSRogueAPTable_Object = MibTable
hpnicfDot11WIDSRogueAPTable = _HpnicfDot11WIDSRogueAPTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfDot11WIDSRogueAPTable.setStatus("current")
_HpnicfDot11WIDSRogueAPEntry_Object = MibTableRow
hpnicfDot11WIDSRogueAPEntry = _HpnicfDot11WIDSRogueAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 1, 1)
)
hpnicfDot11WIDSRogueAPEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11RogueAPBSSMAC"),
)
if mibBuilder.loadTexts:
    hpnicfDot11WIDSRogueAPEntry.setStatus("current")
_HpnicfDot11RogueAPBSSMAC_Type = MacAddress
_HpnicfDot11RogueAPBSSMAC_Object = MibTableColumn
hpnicfDot11RogueAPBSSMAC = _HpnicfDot11RogueAPBSSMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 1, 1, 1),
    _HpnicfDot11RogueAPBSSMAC_Type()
)
hpnicfDot11RogueAPBSSMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11RogueAPBSSMAC.setStatus("current")


class _HpnicfDot11RogueAPVendorName_Type(OctetString):
    """Custom type hpnicfDot11RogueAPVendorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfDot11RogueAPVendorName_Type.__name__ = "OctetString"
_HpnicfDot11RogueAPVendorName_Object = MibTableColumn
hpnicfDot11RogueAPVendorName = _HpnicfDot11RogueAPVendorName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 1, 1, 2),
    _HpnicfDot11RogueAPVendorName_Type()
)
hpnicfDot11RogueAPVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RogueAPVendorName.setStatus("current")
_HpnicfDot11RogueAPMonitorNum_Type = Integer32
_HpnicfDot11RogueAPMonitorNum_Object = MibTableColumn
hpnicfDot11RogueAPMonitorNum = _HpnicfDot11RogueAPMonitorNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 1, 1, 3),
    _HpnicfDot11RogueAPMonitorNum_Type()
)
hpnicfDot11RogueAPMonitorNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RogueAPMonitorNum.setStatus("current")
_HpnicfDot11RogueAPFirstDetectTm_Type = TimeTicks
_HpnicfDot11RogueAPFirstDetectTm_Object = MibTableColumn
hpnicfDot11RogueAPFirstDetectTm = _HpnicfDot11RogueAPFirstDetectTm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 1, 1, 4),
    _HpnicfDot11RogueAPFirstDetectTm_Type()
)
hpnicfDot11RogueAPFirstDetectTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RogueAPFirstDetectTm.setStatus("current")
_HpnicfDot11RogueAPLastDetectTm_Type = TimeTicks
_HpnicfDot11RogueAPLastDetectTm_Object = MibTableColumn
hpnicfDot11RogueAPLastDetectTm = _HpnicfDot11RogueAPLastDetectTm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 1, 1, 5),
    _HpnicfDot11RogueAPLastDetectTm_Type()
)
hpnicfDot11RogueAPLastDetectTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RogueAPLastDetectTm.setStatus("current")
_HpnicfDot11RogueAPSSID_Type = HpnicfDot11SSIDStringType
_HpnicfDot11RogueAPSSID_Object = MibTableColumn
hpnicfDot11RogueAPSSID = _HpnicfDot11RogueAPSSID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 1, 1, 6),
    _HpnicfDot11RogueAPSSID_Type()
)
hpnicfDot11RogueAPSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RogueAPSSID.setStatus("current")
_HpnicfDot11RogueAPMaxSigStrength_Type = Integer32
_HpnicfDot11RogueAPMaxSigStrength_Object = MibTableColumn
hpnicfDot11RogueAPMaxSigStrength = _HpnicfDot11RogueAPMaxSigStrength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 1, 1, 7),
    _HpnicfDot11RogueAPMaxSigStrength_Type()
)
hpnicfDot11RogueAPMaxSigStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RogueAPMaxSigStrength.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RogueAPMaxSigStrength.setUnits("dBm")
_HpnicfDot11RogueAPChannel_Type = HpnicfDot11ChannelScopeType
_HpnicfDot11RogueAPChannel_Object = MibTableColumn
hpnicfDot11RogueAPChannel = _HpnicfDot11RogueAPChannel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 1, 1, 8),
    _HpnicfDot11RogueAPChannel_Type()
)
hpnicfDot11RogueAPChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RogueAPChannel.setStatus("current")
_HpnicfDot11RogueAPBeaconInterval_Type = Integer32
_HpnicfDot11RogueAPBeaconInterval_Object = MibTableColumn
hpnicfDot11RogueAPBeaconInterval = _HpnicfDot11RogueAPBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 1, 1, 9),
    _HpnicfDot11RogueAPBeaconInterval_Type()
)
hpnicfDot11RogueAPBeaconInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RogueAPBeaconInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RogueAPBeaconInterval.setUnits("millisecond")
_HpnicfDot11RogueAPAttackedStatus_Type = TruthValue
_HpnicfDot11RogueAPAttackedStatus_Object = MibTableColumn
hpnicfDot11RogueAPAttackedStatus = _HpnicfDot11RogueAPAttackedStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 1, 1, 10),
    _HpnicfDot11RogueAPAttackedStatus_Type()
)
hpnicfDot11RogueAPAttackedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RogueAPAttackedStatus.setStatus("current")


class _HpnicfDot11RogueAPToIgnore_Type(TruthValue):
    """Custom type hpnicfDot11RogueAPToIgnore based on TruthValue"""


_HpnicfDot11RogueAPToIgnore_Object = MibTableColumn
hpnicfDot11RogueAPToIgnore = _HpnicfDot11RogueAPToIgnore_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 1, 1, 11),
    _HpnicfDot11RogueAPToIgnore_Type()
)
hpnicfDot11RogueAPToIgnore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RogueAPToIgnore.setStatus("current")
_HpnicfDot11RogueAPEncryptStatus_Type = TruthValue
_HpnicfDot11RogueAPEncryptStatus_Object = MibTableColumn
hpnicfDot11RogueAPEncryptStatus = _HpnicfDot11RogueAPEncryptStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 1, 1, 12),
    _HpnicfDot11RogueAPEncryptStatus_Type()
)
hpnicfDot11RogueAPEncryptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RogueAPEncryptStatus.setStatus("current")
_HpnicfDot11RogueAPReset_Type = TruthValue
_HpnicfDot11RogueAPReset_Object = MibTableColumn
hpnicfDot11RogueAPReset = _HpnicfDot11RogueAPReset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 1, 1, 13),
    _HpnicfDot11RogueAPReset_Type()
)
hpnicfDot11RogueAPReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RogueAPReset.setStatus("current")
_HpnicfDot11RogueAPFirstDetectTmStr_Type = OctetString
_HpnicfDot11RogueAPFirstDetectTmStr_Object = MibTableColumn
hpnicfDot11RogueAPFirstDetectTmStr = _HpnicfDot11RogueAPFirstDetectTmStr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 1, 1, 14),
    _HpnicfDot11RogueAPFirstDetectTmStr_Type()
)
hpnicfDot11RogueAPFirstDetectTmStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RogueAPFirstDetectTmStr.setStatus("current")
_HpnicfDot11RogueAPLastDetectTmStr_Type = OctetString
_HpnicfDot11RogueAPLastDetectTmStr_Object = MibTableColumn
hpnicfDot11RogueAPLastDetectTmStr = _HpnicfDot11RogueAPLastDetectTmStr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 1, 1, 15),
    _HpnicfDot11RogueAPLastDetectTmStr_Type()
)
hpnicfDot11RogueAPLastDetectTmStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RogueAPLastDetectTmStr.setStatus("current")
_HpnicfDot11WIDSRogueAPExtTable_Object = MibTable
hpnicfDot11WIDSRogueAPExtTable = _HpnicfDot11WIDSRogueAPExtTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfDot11WIDSRogueAPExtTable.setStatus("current")
_HpnicfDot11WIDSRogueAPExtEntry_Object = MibTableRow
hpnicfDot11WIDSRogueAPExtEntry = _HpnicfDot11WIDSRogueAPExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 2, 1)
)
hpnicfDot11WIDSRogueAPExtEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11RogueAPBSSMAC"),
    (0, "HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11WIDSAPID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11WIDSRogueAPExtEntry.setStatus("current")
_HpnicfDot11WIDSAPID_Type = HpnicfDot11ObjectIDType
_HpnicfDot11WIDSAPID_Object = MibTableColumn
hpnicfDot11WIDSAPID = _HpnicfDot11WIDSAPID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 2, 1, 1),
    _HpnicfDot11WIDSAPID_Type()
)
hpnicfDot11WIDSAPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSAPID.setStatus("current")
_HpnicfDot11DetectCurAPSigStrength_Type = Integer32
_HpnicfDot11DetectCurAPSigStrength_Object = MibTableColumn
hpnicfDot11DetectCurAPSigStrength = _HpnicfDot11DetectCurAPSigStrength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 2, 1, 2),
    _HpnicfDot11DetectCurAPSigStrength_Type()
)
hpnicfDot11DetectCurAPSigStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11DetectCurAPSigStrength.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11DetectCurAPSigStrength.setUnits("dBm")
_HpnicfDot11DetectAPByChannel_Type = HpnicfDot11ChannelScopeType
_HpnicfDot11DetectAPByChannel_Object = MibTableColumn
hpnicfDot11DetectAPByChannel = _HpnicfDot11DetectAPByChannel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 2, 1, 3),
    _HpnicfDot11DetectAPByChannel_Type()
)
hpnicfDot11DetectAPByChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11DetectAPByChannel.setStatus("current")
_HpnicfDot11DetectAPByRadioID_Type = HpnicfDot11RadioScopeType
_HpnicfDot11DetectAPByRadioID_Object = MibTableColumn
hpnicfDot11DetectAPByRadioID = _HpnicfDot11DetectAPByRadioID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 2, 1, 4),
    _HpnicfDot11DetectAPByRadioID_Type()
)
hpnicfDot11DetectAPByRadioID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11DetectAPByRadioID.setStatus("current")
_HpnicfDot11AttackAPStatus_Type = TruthValue
_HpnicfDot11AttackAPStatus_Object = MibTableColumn
hpnicfDot11AttackAPStatus = _HpnicfDot11AttackAPStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 2, 1, 5),
    _HpnicfDot11AttackAPStatus_Type()
)
hpnicfDot11AttackAPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11AttackAPStatus.setStatus("current")
_HpnicfDot11DetectAPFirstTm_Type = TimeTicks
_HpnicfDot11DetectAPFirstTm_Object = MibTableColumn
hpnicfDot11DetectAPFirstTm = _HpnicfDot11DetectAPFirstTm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 2, 1, 6),
    _HpnicfDot11DetectAPFirstTm_Type()
)
hpnicfDot11DetectAPFirstTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11DetectAPFirstTm.setStatus("current")
_HpnicfDot11DetectAPLastTm_Type = TimeTicks
_HpnicfDot11DetectAPLastTm_Object = MibTableColumn
hpnicfDot11DetectAPLastTm = _HpnicfDot11DetectAPLastTm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 2, 1, 7),
    _HpnicfDot11DetectAPLastTm_Type()
)
hpnicfDot11DetectAPLastTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11DetectAPLastTm.setStatus("current")
_HpnicfDot11WIDSRogueStaTable_Object = MibTable
hpnicfDot11WIDSRogueStaTable = _HpnicfDot11WIDSRogueStaTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfDot11WIDSRogueStaTable.setStatus("current")
_HpnicfDot11WIDSRogueStaEntry_Object = MibTableRow
hpnicfDot11WIDSRogueStaEntry = _HpnicfDot11WIDSRogueStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 3, 1)
)
hpnicfDot11WIDSRogueStaEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11RogueStaMAC"),
)
if mibBuilder.loadTexts:
    hpnicfDot11WIDSRogueStaEntry.setStatus("current")
_HpnicfDot11RogueStaMAC_Type = MacAddress
_HpnicfDot11RogueStaMAC_Object = MibTableColumn
hpnicfDot11RogueStaMAC = _HpnicfDot11RogueStaMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 3, 1, 1),
    _HpnicfDot11RogueStaMAC_Type()
)
hpnicfDot11RogueStaMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11RogueStaMAC.setStatus("current")


class _HpnicfDot11RogueStaVendorName_Type(OctetString):
    """Custom type hpnicfDot11RogueStaVendorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfDot11RogueStaVendorName_Type.__name__ = "OctetString"
_HpnicfDot11RogueStaVendorName_Object = MibTableColumn
hpnicfDot11RogueStaVendorName = _HpnicfDot11RogueStaVendorName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 3, 1, 2),
    _HpnicfDot11RogueStaVendorName_Type()
)
hpnicfDot11RogueStaVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RogueStaVendorName.setStatus("current")
_HpnicfDot11RogueStaMonitorNum_Type = Integer32
_HpnicfDot11RogueStaMonitorNum_Object = MibTableColumn
hpnicfDot11RogueStaMonitorNum = _HpnicfDot11RogueStaMonitorNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 3, 1, 3),
    _HpnicfDot11RogueStaMonitorNum_Type()
)
hpnicfDot11RogueStaMonitorNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RogueStaMonitorNum.setStatus("current")
_HpnicfDot11RogueStaFirstDetectTm_Type = TimeTicks
_HpnicfDot11RogueStaFirstDetectTm_Object = MibTableColumn
hpnicfDot11RogueStaFirstDetectTm = _HpnicfDot11RogueStaFirstDetectTm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 3, 1, 4),
    _HpnicfDot11RogueStaFirstDetectTm_Type()
)
hpnicfDot11RogueStaFirstDetectTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RogueStaFirstDetectTm.setStatus("current")
_HpnicfDot11RogueStaLastDetectTm_Type = TimeTicks
_HpnicfDot11RogueStaLastDetectTm_Object = MibTableColumn
hpnicfDot11RogueStaLastDetectTm = _HpnicfDot11RogueStaLastDetectTm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 3, 1, 5),
    _HpnicfDot11RogueStaLastDetectTm_Type()
)
hpnicfDot11RogueStaLastDetectTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RogueStaLastDetectTm.setStatus("current")
_HpnicfDot11RogueStaAccessBSSID_Type = MacAddress
_HpnicfDot11RogueStaAccessBSSID_Object = MibTableColumn
hpnicfDot11RogueStaAccessBSSID = _HpnicfDot11RogueStaAccessBSSID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 3, 1, 6),
    _HpnicfDot11RogueStaAccessBSSID_Type()
)
hpnicfDot11RogueStaAccessBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RogueStaAccessBSSID.setStatus("current")
_HpnicfDot11RogueStaMaxSigStrength_Type = Integer32
_HpnicfDot11RogueStaMaxSigStrength_Object = MibTableColumn
hpnicfDot11RogueStaMaxSigStrength = _HpnicfDot11RogueStaMaxSigStrength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 3, 1, 7),
    _HpnicfDot11RogueStaMaxSigStrength_Type()
)
hpnicfDot11RogueStaMaxSigStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RogueStaMaxSigStrength.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RogueStaMaxSigStrength.setUnits("dBm")
_HpnicfDot11RogueStaChannel_Type = HpnicfDot11ChannelScopeType
_HpnicfDot11RogueStaChannel_Object = MibTableColumn
hpnicfDot11RogueStaChannel = _HpnicfDot11RogueStaChannel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 3, 1, 8),
    _HpnicfDot11RogueStaChannel_Type()
)
hpnicfDot11RogueStaChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RogueStaChannel.setStatus("current")
_HpnicfDot11RogueStaAttackedStatus_Type = TruthValue
_HpnicfDot11RogueStaAttackedStatus_Object = MibTableColumn
hpnicfDot11RogueStaAttackedStatus = _HpnicfDot11RogueStaAttackedStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 3, 1, 9),
    _HpnicfDot11RogueStaAttackedStatus_Type()
)
hpnicfDot11RogueStaAttackedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RogueStaAttackedStatus.setStatus("current")


class _HpnicfDot11RogueStaToIgnore_Type(TruthValue):
    """Custom type hpnicfDot11RogueStaToIgnore based on TruthValue"""


_HpnicfDot11RogueStaToIgnore_Object = MibTableColumn
hpnicfDot11RogueStaToIgnore = _HpnicfDot11RogueStaToIgnore_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 3, 1, 10),
    _HpnicfDot11RogueStaToIgnore_Type()
)
hpnicfDot11RogueStaToIgnore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RogueStaToIgnore.setStatus("current")
_HpnicfDot11RogueStaAdHocStatus_Type = TruthValue
_HpnicfDot11RogueStaAdHocStatus_Object = MibTableColumn
hpnicfDot11RogueStaAdHocStatus = _HpnicfDot11RogueStaAdHocStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 3, 1, 11),
    _HpnicfDot11RogueStaAdHocStatus_Type()
)
hpnicfDot11RogueStaAdHocStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RogueStaAdHocStatus.setStatus("current")
_HpnicfDot11RogueStaReset_Type = TruthValue
_HpnicfDot11RogueStaReset_Object = MibTableColumn
hpnicfDot11RogueStaReset = _HpnicfDot11RogueStaReset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 3, 1, 12),
    _HpnicfDot11RogueStaReset_Type()
)
hpnicfDot11RogueStaReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RogueStaReset.setStatus("current")
_HpnicfDot11RogueStaFirstDetectTmStr_Type = OctetString
_HpnicfDot11RogueStaFirstDetectTmStr_Object = MibTableColumn
hpnicfDot11RogueStaFirstDetectTmStr = _HpnicfDot11RogueStaFirstDetectTmStr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 3, 1, 13),
    _HpnicfDot11RogueStaFirstDetectTmStr_Type()
)
hpnicfDot11RogueStaFirstDetectTmStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RogueStaFirstDetectTmStr.setStatus("current")
_HpnicfDot11RogueStaLastDetectTmStr_Type = OctetString
_HpnicfDot11RogueStaLastDetectTmStr_Object = MibTableColumn
hpnicfDot11RogueStaLastDetectTmStr = _HpnicfDot11RogueStaLastDetectTmStr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 3, 1, 14),
    _HpnicfDot11RogueStaLastDetectTmStr_Type()
)
hpnicfDot11RogueStaLastDetectTmStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RogueStaLastDetectTmStr.setStatus("current")
_HpnicfDot11WIDSRogueStaExtTable_Object = MibTable
hpnicfDot11WIDSRogueStaExtTable = _HpnicfDot11WIDSRogueStaExtTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 4)
)
if mibBuilder.loadTexts:
    hpnicfDot11WIDSRogueStaExtTable.setStatus("current")
_HpnicfDot11WIDSRogueStaExtEntry_Object = MibTableRow
hpnicfDot11WIDSRogueStaExtEntry = _HpnicfDot11WIDSRogueStaExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 4, 1)
)
hpnicfDot11WIDSRogueStaExtEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11RogueStaMAC"),
    (0, "HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11WIDSAPID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11WIDSRogueStaExtEntry.setStatus("current")
_HpnicfDot11DetectCurStaSigStrength_Type = Integer32
_HpnicfDot11DetectCurStaSigStrength_Object = MibTableColumn
hpnicfDot11DetectCurStaSigStrength = _HpnicfDot11DetectCurStaSigStrength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 4, 1, 1),
    _HpnicfDot11DetectCurStaSigStrength_Type()
)
hpnicfDot11DetectCurStaSigStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11DetectCurStaSigStrength.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11DetectCurStaSigStrength.setUnits("dBm")
_HpnicfDot11DetectStaByChannel_Type = HpnicfDot11ChannelScopeType
_HpnicfDot11DetectStaByChannel_Object = MibTableColumn
hpnicfDot11DetectStaByChannel = _HpnicfDot11DetectStaByChannel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 4, 1, 2),
    _HpnicfDot11DetectStaByChannel_Type()
)
hpnicfDot11DetectStaByChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11DetectStaByChannel.setStatus("current")
_HpnicfDot11DetectStaByRadioID_Type = HpnicfDot11RadioScopeType
_HpnicfDot11DetectStaByRadioID_Object = MibTableColumn
hpnicfDot11DetectStaByRadioID = _HpnicfDot11DetectStaByRadioID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 4, 1, 3),
    _HpnicfDot11DetectStaByRadioID_Type()
)
hpnicfDot11DetectStaByRadioID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11DetectStaByRadioID.setStatus("current")
_HpnicfDot11AttackStaStatus_Type = TruthValue
_HpnicfDot11AttackStaStatus_Object = MibTableColumn
hpnicfDot11AttackStaStatus = _HpnicfDot11AttackStaStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 4, 1, 4),
    _HpnicfDot11AttackStaStatus_Type()
)
hpnicfDot11AttackStaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11AttackStaStatus.setStatus("current")
_HpnicfDot11DetectStaFirstTm_Type = TimeTicks
_HpnicfDot11DetectStaFirstTm_Object = MibTableColumn
hpnicfDot11DetectStaFirstTm = _HpnicfDot11DetectStaFirstTm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 4, 1, 5),
    _HpnicfDot11DetectStaFirstTm_Type()
)
hpnicfDot11DetectStaFirstTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11DetectStaFirstTm.setStatus("current")
_HpnicfDot11DetectStaLastTm_Type = TimeTicks
_HpnicfDot11DetectStaLastTm_Object = MibTableColumn
hpnicfDot11DetectStaLastTm = _HpnicfDot11DetectStaLastTm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 4, 1, 6),
    _HpnicfDot11DetectStaLastTm_Type()
)
hpnicfDot11DetectStaLastTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11DetectStaLastTm.setStatus("current")
_HpnicfDot11WIDSDetectedDevTable_Object = MibTable
hpnicfDot11WIDSDetectedDevTable = _HpnicfDot11WIDSDetectedDevTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 5)
)
if mibBuilder.loadTexts:
    hpnicfDot11WIDSDetectedDevTable.setStatus("current")
_HpnicfDot11WIDSDetectedDevEntry_Object = MibTableRow
hpnicfDot11WIDSDetectedDevEntry = _HpnicfDot11WIDSDetectedDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 5, 1)
)
hpnicfDot11WIDSDetectedDevEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11WIDSDevMAC"),
)
if mibBuilder.loadTexts:
    hpnicfDot11WIDSDetectedDevEntry.setStatus("current")
_HpnicfDot11WIDSDevMAC_Type = MacAddress
_HpnicfDot11WIDSDevMAC_Object = MibTableColumn
hpnicfDot11WIDSDevMAC = _HpnicfDot11WIDSDevMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 5, 1, 1),
    _HpnicfDot11WIDSDevMAC_Type()
)
hpnicfDot11WIDSDevMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSDevMAC.setStatus("current")
_HpnicfDot11WIDSDevType_Type = HpnicfDot11WIDSDevType
_HpnicfDot11WIDSDevType_Object = MibTableColumn
hpnicfDot11WIDSDevType = _HpnicfDot11WIDSDevType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 5, 1, 2),
    _HpnicfDot11WIDSDevType_Type()
)
hpnicfDot11WIDSDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSDevType.setStatus("current")
_HpnicfDot11WIDSDevPermitType_Type = HpnicfDot11WIDSDevPermitType
_HpnicfDot11WIDSDevPermitType_Object = MibTableColumn
hpnicfDot11WIDSDevPermitType = _HpnicfDot11WIDSDevPermitType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 5, 1, 3),
    _HpnicfDot11WIDSDevPermitType_Type()
)
hpnicfDot11WIDSDevPermitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSDevPermitType.setStatus("current")
_HpnicfDot11WIDSDevVendor_Type = OctetString
_HpnicfDot11WIDSDevVendor_Object = MibTableColumn
hpnicfDot11WIDSDevVendor = _HpnicfDot11WIDSDevVendor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 5, 1, 4),
    _HpnicfDot11WIDSDevVendor_Type()
)
hpnicfDot11WIDSDevVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSDevVendor.setStatus("current")
_HpnicfDot11WIDSDevMonitorNum_Type = Integer32
_HpnicfDot11WIDSDevMonitorNum_Object = MibTableColumn
hpnicfDot11WIDSDevMonitorNum = _HpnicfDot11WIDSDevMonitorNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 5, 1, 5),
    _HpnicfDot11WIDSDevMonitorNum_Type()
)
hpnicfDot11WIDSDevMonitorNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSDevMonitorNum.setStatus("current")
_HpnicfDot11WIDSDevSSID_Type = OctetString
_HpnicfDot11WIDSDevSSID_Object = MibTableColumn
hpnicfDot11WIDSDevSSID = _HpnicfDot11WIDSDevSSID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 5, 1, 6),
    _HpnicfDot11WIDSDevSSID_Type()
)
hpnicfDot11WIDSDevSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSDevSSID.setStatus("current")
_HpnicfDot11WIDSDevBSSID_Type = MacAddress
_HpnicfDot11WIDSDevBSSID_Object = MibTableColumn
hpnicfDot11WIDSDevBSSID = _HpnicfDot11WIDSDevBSSID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 5, 1, 7),
    _HpnicfDot11WIDSDevBSSID_Type()
)
hpnicfDot11WIDSDevBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSDevBSSID.setStatus("current")
_HpnicfDot11WIDSDevChannel_Type = HpnicfDot11ChannelScopeType
_HpnicfDot11WIDSDevChannel_Object = MibTableColumn
hpnicfDot11WIDSDevChannel = _HpnicfDot11WIDSDevChannel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 5, 1, 8),
    _HpnicfDot11WIDSDevChannel_Type()
)
hpnicfDot11WIDSDevChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSDevChannel.setStatus("current")
_HpnicfDot11WIDSDevMaxRSSI_Type = Integer32
_HpnicfDot11WIDSDevMaxRSSI_Object = MibTableColumn
hpnicfDot11WIDSDevMaxRSSI = _HpnicfDot11WIDSDevMaxRSSI_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 5, 1, 9),
    _HpnicfDot11WIDSDevMaxRSSI_Type()
)
hpnicfDot11WIDSDevMaxRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSDevMaxRSSI.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSDevMaxRSSI.setUnits("dbm")
_HpnicfDot11WIDSDevBeaconIntvl_Type = Integer32
_HpnicfDot11WIDSDevBeaconIntvl_Object = MibTableColumn
hpnicfDot11WIDSDevBeaconIntvl = _HpnicfDot11WIDSDevBeaconIntvl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 5, 1, 10),
    _HpnicfDot11WIDSDevBeaconIntvl_Type()
)
hpnicfDot11WIDSDevBeaconIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSDevBeaconIntvl.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSDevBeaconIntvl.setUnits("millionsecond")
_HpnicfDot11WIDSDevFstDctTime_Type = DateAndTime
_HpnicfDot11WIDSDevFstDctTime_Object = MibTableColumn
hpnicfDot11WIDSDevFstDctTime = _HpnicfDot11WIDSDevFstDctTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 5, 1, 11),
    _HpnicfDot11WIDSDevFstDctTime_Type()
)
hpnicfDot11WIDSDevFstDctTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSDevFstDctTime.setStatus("current")
_HpnicfDot11WIDSDevLstDctTime_Type = DateAndTime
_HpnicfDot11WIDSDevLstDctTime_Object = MibTableColumn
hpnicfDot11WIDSDevLstDctTime = _HpnicfDot11WIDSDevLstDctTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 5, 1, 12),
    _HpnicfDot11WIDSDevLstDctTime_Type()
)
hpnicfDot11WIDSDevLstDctTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSDevLstDctTime.setStatus("current")
_HpnicfDot11WIDSDevReset_Type = TruthValue
_HpnicfDot11WIDSDevReset_Object = MibTableColumn
hpnicfDot11WIDSDevReset = _HpnicfDot11WIDSDevReset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 5, 1, 13),
    _HpnicfDot11WIDSDevReset_Type()
)
hpnicfDot11WIDSDevReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSDevReset.setStatus("current")
_HpnicfDot11WIDSDevSnr_Type = Integer32
_HpnicfDot11WIDSDevSnr_Object = MibTableColumn
hpnicfDot11WIDSDevSnr = _HpnicfDot11WIDSDevSnr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 5, 1, 14),
    _HpnicfDot11WIDSDevSnr_Type()
)
hpnicfDot11WIDSDevSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSDevSnr.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSDevSnr.setUnits("dB")
_HpnicfDot11WIDSRptAPTable_Object = MibTable
hpnicfDot11WIDSRptAPTable = _HpnicfDot11WIDSRptAPTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 6)
)
if mibBuilder.loadTexts:
    hpnicfDot11WIDSRptAPTable.setStatus("current")
_HpnicfDot11WIDSRptAPEntry_Object = MibTableRow
hpnicfDot11WIDSRptAPEntry = _HpnicfDot11WIDSRptAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 6, 1)
)
hpnicfDot11WIDSRptAPEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11WIDSDevMAC"),
    (0, "HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11WIDSRptAPMAC"),
)
if mibBuilder.loadTexts:
    hpnicfDot11WIDSRptAPEntry.setStatus("current")
_HpnicfDot11WIDSRptAPMAC_Type = MacAddress
_HpnicfDot11WIDSRptAPMAC_Object = MibTableColumn
hpnicfDot11WIDSRptAPMAC = _HpnicfDot11WIDSRptAPMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 6, 1, 1),
    _HpnicfDot11WIDSRptAPMAC_Type()
)
hpnicfDot11WIDSRptAPMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSRptAPMAC.setStatus("current")
_HpnicfDot11WIDSRptAPName_Type = OctetString
_HpnicfDot11WIDSRptAPName_Object = MibTableColumn
hpnicfDot11WIDSRptAPName = _HpnicfDot11WIDSRptAPName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 6, 1, 2),
    _HpnicfDot11WIDSRptAPName_Type()
)
hpnicfDot11WIDSRptAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSRptAPName.setStatus("current")
_HpnicfDot11WIDSRptAPRadioID_Type = HpnicfDot11RadioScopeType
_HpnicfDot11WIDSRptAPRadioID_Object = MibTableColumn
hpnicfDot11WIDSRptAPRadioID = _HpnicfDot11WIDSRptAPRadioID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 6, 1, 3),
    _HpnicfDot11WIDSRptAPRadioID_Type()
)
hpnicfDot11WIDSRptAPRadioID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSRptAPRadioID.setStatus("current")
_HpnicfDot11WIDSRptAPMaxRSSI_Type = Integer32
_HpnicfDot11WIDSRptAPMaxRSSI_Object = MibTableColumn
hpnicfDot11WIDSRptAPMaxRSSI = _HpnicfDot11WIDSRptAPMaxRSSI_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 6, 1, 4),
    _HpnicfDot11WIDSRptAPMaxRSSI_Type()
)
hpnicfDot11WIDSRptAPMaxRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSRptAPMaxRSSI.setStatus("current")
_HpnicfDot11WIDSRptAPFstDctTime_Type = DateAndTime
_HpnicfDot11WIDSRptAPFstDctTime_Object = MibTableColumn
hpnicfDot11WIDSRptAPFstDctTime = _HpnicfDot11WIDSRptAPFstDctTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 6, 1, 5),
    _HpnicfDot11WIDSRptAPFstDctTime_Type()
)
hpnicfDot11WIDSRptAPFstDctTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSRptAPFstDctTime.setStatus("current")
_HpnicfDot11WIDSRptAPLstDctTime_Type = DateAndTime
_HpnicfDot11WIDSRptAPLstDctTime_Object = MibTableColumn
hpnicfDot11WIDSRptAPLstDctTime = _HpnicfDot11WIDSRptAPLstDctTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 6, 1, 6),
    _HpnicfDot11WIDSRptAPLstDctTime_Type()
)
hpnicfDot11WIDSRptAPLstDctTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSRptAPLstDctTime.setStatus("current")
_HpnicfDot11DynBlackListTable_Object = MibTable
hpnicfDot11DynBlackListTable = _HpnicfDot11DynBlackListTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 7)
)
if mibBuilder.loadTexts:
    hpnicfDot11DynBlackListTable.setStatus("current")
_HpnicfDot11DynBlackListEntry_Object = MibTableRow
hpnicfDot11DynBlackListEntry = _HpnicfDot11DynBlackListEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 7, 1)
)
hpnicfDot11DynBlackListEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11DynBlackListMAC"),
)
if mibBuilder.loadTexts:
    hpnicfDot11DynBlackListEntry.setStatus("current")
_HpnicfDot11DynBlackListMAC_Type = MacAddress
_HpnicfDot11DynBlackListMAC_Object = MibTableColumn
hpnicfDot11DynBlackListMAC = _HpnicfDot11DynBlackListMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 7, 1, 1),
    _HpnicfDot11DynBlackListMAC_Type()
)
hpnicfDot11DynBlackListMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11DynBlackListMAC.setStatus("current")
_HpnicfDot11DynBlackListTime_Type = Unsigned32
_HpnicfDot11DynBlackListTime_Object = MibTableColumn
hpnicfDot11DynBlackListTime = _HpnicfDot11DynBlackListTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 7, 1, 2),
    _HpnicfDot11DynBlackListTime_Type()
)
hpnicfDot11DynBlackListTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11DynBlackListTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11DynBlackListTime.setUnits("second")
_HpnicfDot11DynBlackListReason_Type = OctetString
_HpnicfDot11DynBlackListReason_Object = MibTableColumn
hpnicfDot11DynBlackListReason = _HpnicfDot11DynBlackListReason_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 7, 1, 3),
    _HpnicfDot11DynBlackListReason_Type()
)
hpnicfDot11DynBlackListReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11DynBlackListReason.setStatus("current")
_HpnicfDot11DynBlackListReset_Type = TruthValue
_HpnicfDot11DynBlackListReset_Object = MibTableColumn
hpnicfDot11DynBlackListReset = _HpnicfDot11DynBlackListReset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 7, 1, 4),
    _HpnicfDot11DynBlackListReset_Type()
)
hpnicfDot11DynBlackListReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11DynBlackListReset.setStatus("current")
_HpnicfDot11DynBlackListTimeTicks_Type = TimeTicks
_HpnicfDot11DynBlackListTimeTicks_Object = MibTableColumn
hpnicfDot11DynBlackListTimeTicks = _HpnicfDot11DynBlackListTimeTicks_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 7, 1, 5),
    _HpnicfDot11DynBlackListTimeTicks_Type()
)
hpnicfDot11DynBlackListTimeTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11DynBlackListTimeTicks.setStatus("current")
_HpnicfDot11WIDSRogueHistoryTable_Object = MibTable
hpnicfDot11WIDSRogueHistoryTable = _HpnicfDot11WIDSRogueHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 8)
)
if mibBuilder.loadTexts:
    hpnicfDot11WIDSRogueHistoryTable.setStatus("current")
_HpnicfDot11WIDSRogueHistoryEntry_Object = MibTableRow
hpnicfDot11WIDSRogueHistoryEntry = _HpnicfDot11WIDSRogueHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 8, 1)
)
hpnicfDot11WIDSRogueHistoryEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11WIDSRogueHisIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot11WIDSRogueHistoryEntry.setStatus("current")
_HpnicfDot11WIDSRogueHisIndex_Type = Integer32
_HpnicfDot11WIDSRogueHisIndex_Object = MibTableColumn
hpnicfDot11WIDSRogueHisIndex = _HpnicfDot11WIDSRogueHisIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 8, 1, 1),
    _HpnicfDot11WIDSRogueHisIndex_Type()
)
hpnicfDot11WIDSRogueHisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSRogueHisIndex.setStatus("current")
_HpnicfDot11WIDSRogueHisMAC_Type = MacAddress
_HpnicfDot11WIDSRogueHisMAC_Object = MibTableColumn
hpnicfDot11WIDSRogueHisMAC = _HpnicfDot11WIDSRogueHisMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 8, 1, 2),
    _HpnicfDot11WIDSRogueHisMAC_Type()
)
hpnicfDot11WIDSRogueHisMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSRogueHisMAC.setStatus("current")
_HpnicfDot11WIDSRogueHisVendor_Type = OctetString
_HpnicfDot11WIDSRogueHisVendor_Object = MibTableColumn
hpnicfDot11WIDSRogueHisVendor = _HpnicfDot11WIDSRogueHisVendor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 8, 1, 3),
    _HpnicfDot11WIDSRogueHisVendor_Type()
)
hpnicfDot11WIDSRogueHisVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSRogueHisVendor.setStatus("current")
_HpnicfDot11WIDSRogueHisType_Type = HpnicfDot11WIDSDevType
_HpnicfDot11WIDSRogueHisType_Object = MibTableColumn
hpnicfDot11WIDSRogueHisType = _HpnicfDot11WIDSRogueHisType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 8, 1, 4),
    _HpnicfDot11WIDSRogueHisType_Type()
)
hpnicfDot11WIDSRogueHisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSRogueHisType.setStatus("current")
_HpnicfDot11WIDSRogueHisChl_Type = HpnicfDot11ChannelScopeType
_HpnicfDot11WIDSRogueHisChl_Object = MibTableColumn
hpnicfDot11WIDSRogueHisChl = _HpnicfDot11WIDSRogueHisChl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 8, 1, 5),
    _HpnicfDot11WIDSRogueHisChl_Type()
)
hpnicfDot11WIDSRogueHisChl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSRogueHisChl.setStatus("current")
_HpnicfDot11WIDSRogueHisSSID_Type = OctetString
_HpnicfDot11WIDSRogueHisSSID_Object = MibTableColumn
hpnicfDot11WIDSRogueHisSSID = _HpnicfDot11WIDSRogueHisSSID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 8, 1, 6),
    _HpnicfDot11WIDSRogueHisSSID_Type()
)
hpnicfDot11WIDSRogueHisSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSRogueHisSSID.setStatus("current")
_HpnicfDot11WIDSRogueHisLastDctTime_Type = DateAndTime
_HpnicfDot11WIDSRogueHisLastDctTime_Object = MibTableColumn
hpnicfDot11WIDSRogueHisLastDctTime = _HpnicfDot11WIDSRogueHisLastDctTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 8, 1, 7),
    _HpnicfDot11WIDSRogueHisLastDctTime_Type()
)
hpnicfDot11WIDSRogueHisLastDctTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSRogueHisLastDctTime.setStatus("current")
_HpnicfDot11WIDSAtkHistroyTable_Object = MibTable
hpnicfDot11WIDSAtkHistroyTable = _HpnicfDot11WIDSAtkHistroyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 9)
)
if mibBuilder.loadTexts:
    hpnicfDot11WIDSAtkHistroyTable.setStatus("current")
_HpnicfDot11WIDSAtkHistroyEntry_Object = MibTableRow
hpnicfDot11WIDSAtkHistroyEntry = _HpnicfDot11WIDSAtkHistroyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 9, 1)
)
hpnicfDot11WIDSAtkHistroyEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11WIDSAtkHisIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot11WIDSAtkHistroyEntry.setStatus("current")
_HpnicfDot11WIDSAtkHisIndex_Type = Integer32
_HpnicfDot11WIDSAtkHisIndex_Object = MibTableColumn
hpnicfDot11WIDSAtkHisIndex = _HpnicfDot11WIDSAtkHisIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 9, 1, 1),
    _HpnicfDot11WIDSAtkHisIndex_Type()
)
hpnicfDot11WIDSAtkHisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSAtkHisIndex.setStatus("current")
_HpnicfDot11WIDSAtkHisMAC_Type = MacAddress
_HpnicfDot11WIDSAtkHisMAC_Object = MibTableColumn
hpnicfDot11WIDSAtkHisMAC = _HpnicfDot11WIDSAtkHisMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 9, 1, 2),
    _HpnicfDot11WIDSAtkHisMAC_Type()
)
hpnicfDot11WIDSAtkHisMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSAtkHisMAC.setStatus("current")
_HpnicfDot11WIDSAtkHisType_Type = HpnicfDot11WIDSAtkType
_HpnicfDot11WIDSAtkHisType_Object = MibTableColumn
hpnicfDot11WIDSAtkHisType = _HpnicfDot11WIDSAtkHisType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 9, 1, 3),
    _HpnicfDot11WIDSAtkHisType_Type()
)
hpnicfDot11WIDSAtkHisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSAtkHisType.setStatus("current")
_HpnicfDot11WIDSAtkHisChl_Type = HpnicfDot11ChannelScopeType
_HpnicfDot11WIDSAtkHisChl_Object = MibTableColumn
hpnicfDot11WIDSAtkHisChl = _HpnicfDot11WIDSAtkHisChl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 9, 1, 4),
    _HpnicfDot11WIDSAtkHisChl_Type()
)
hpnicfDot11WIDSAtkHisChl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSAtkHisChl.setStatus("current")
_HpnicfDot11WIDSAtkHisRSSI_Type = Integer32
_HpnicfDot11WIDSAtkHisRSSI_Object = MibTableColumn
hpnicfDot11WIDSAtkHisRSSI = _HpnicfDot11WIDSAtkHisRSSI_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 9, 1, 5),
    _HpnicfDot11WIDSAtkHisRSSI_Type()
)
hpnicfDot11WIDSAtkHisRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSAtkHisRSSI.setStatus("current")
_HpnicfDot11WIDSAtkHisDctTime_Type = DateAndTime
_HpnicfDot11WIDSAtkHisDctTime_Object = MibTableColumn
hpnicfDot11WIDSAtkHisDctTime = _HpnicfDot11WIDSAtkHisDctTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 9, 1, 6),
    _HpnicfDot11WIDSAtkHisDctTime_Type()
)
hpnicfDot11WIDSAtkHisDctTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSAtkHisDctTime.setStatus("current")
_HpnicfDot11WIDSAtkHisAPName_Type = OctetString
_HpnicfDot11WIDSAtkHisAPName_Object = MibTableColumn
hpnicfDot11WIDSAtkHisAPName = _HpnicfDot11WIDSAtkHisAPName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 9, 1, 7),
    _HpnicfDot11WIDSAtkHisAPName_Type()
)
hpnicfDot11WIDSAtkHisAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSAtkHisAPName.setStatus("current")
_HpnicfDot11WIDSAtkStatis_ObjectIdentity = ObjectIdentity
hpnicfDot11WIDSAtkStatis = _HpnicfDot11WIDSAtkStatis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 10)
)
_HpnicfDot11WIDSAtkStasStartTime_Type = DateAndTime
_HpnicfDot11WIDSAtkStasStartTime_Object = MibScalar
hpnicfDot11WIDSAtkStasStartTime = _HpnicfDot11WIDSAtkStasStartTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 10, 1),
    _HpnicfDot11WIDSAtkStasStartTime_Type()
)
hpnicfDot11WIDSAtkStasStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSAtkStasStartTime.setStatus("current")
_HpnicfDot11WIDSAtkStasTable_Object = MibTable
hpnicfDot11WIDSAtkStasTable = _HpnicfDot11WIDSAtkStasTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 10, 2)
)
if mibBuilder.loadTexts:
    hpnicfDot11WIDSAtkStasTable.setStatus("current")
_HpnicfDot11WIDSAtkStasEntry_Object = MibTableRow
hpnicfDot11WIDSAtkStasEntry = _HpnicfDot11WIDSAtkStasEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 10, 2, 1)
)
hpnicfDot11WIDSAtkStasEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11WIDSAtkStasType"),
)
if mibBuilder.loadTexts:
    hpnicfDot11WIDSAtkStasEntry.setStatus("current")
_HpnicfDot11WIDSAtkStasType_Type = HpnicfDot11WIDSAtkType
_HpnicfDot11WIDSAtkStasType_Object = MibTableColumn
hpnicfDot11WIDSAtkStasType = _HpnicfDot11WIDSAtkStasType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 10, 2, 1, 1),
    _HpnicfDot11WIDSAtkStasType_Type()
)
hpnicfDot11WIDSAtkStasType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSAtkStasType.setStatus("current")
_HpnicfDot11WIDSAtkStasCurCnt_Type = Unsigned32
_HpnicfDot11WIDSAtkStasCurCnt_Object = MibTableColumn
hpnicfDot11WIDSAtkStasCurCnt = _HpnicfDot11WIDSAtkStasCurCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 10, 2, 1, 2),
    _HpnicfDot11WIDSAtkStasCurCnt_Type()
)
hpnicfDot11WIDSAtkStasCurCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSAtkStasCurCnt.setStatus("current")
_HpnicfDot11WIDSAtkStasTotalCnt_Type = Unsigned32
_HpnicfDot11WIDSAtkStasTotalCnt_Object = MibTableColumn
hpnicfDot11WIDSAtkStasTotalCnt = _HpnicfDot11WIDSAtkStasTotalCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 10, 2, 1, 3),
    _HpnicfDot11WIDSAtkStasTotalCnt_Type()
)
hpnicfDot11WIDSAtkStasTotalCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSAtkStasTotalCnt.setStatus("current")
_HpnicfDot11BlackListTable_Object = MibTable
hpnicfDot11BlackListTable = _HpnicfDot11BlackListTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 11)
)
if mibBuilder.loadTexts:
    hpnicfDot11BlackListTable.setStatus("current")
_HpnicfDot11BlackListEntry_Object = MibTableRow
hpnicfDot11BlackListEntry = _HpnicfDot11BlackListEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 11, 1)
)
hpnicfDot11BlackListEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11BlackListMAC"),
)
if mibBuilder.loadTexts:
    hpnicfDot11BlackListEntry.setStatus("current")
_HpnicfDot11BlackListMAC_Type = MacAddress
_HpnicfDot11BlackListMAC_Object = MibTableColumn
hpnicfDot11BlackListMAC = _HpnicfDot11BlackListMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 11, 1, 1),
    _HpnicfDot11BlackListMAC_Type()
)
hpnicfDot11BlackListMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11BlackListMAC.setStatus("current")
_HpnicfDot11BlackListTime_Type = Unsigned32
_HpnicfDot11BlackListTime_Object = MibTableColumn
hpnicfDot11BlackListTime = _HpnicfDot11BlackListTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 11, 1, 2),
    _HpnicfDot11BlackListTime_Type()
)
hpnicfDot11BlackListTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BlackListTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11BlackListTime.setUnits("minutes")
_HpnicfDot11BlackListReason_Type = OctetString
_HpnicfDot11BlackListReason_Object = MibTableColumn
hpnicfDot11BlackListReason = _HpnicfDot11BlackListReason_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 11, 1, 3),
    _HpnicfDot11BlackListReason_Type()
)
hpnicfDot11BlackListReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BlackListReason.setStatus("current")
_HpnicfDot11BlackListRowStatus_Type = RowStatus
_HpnicfDot11BlackListRowStatus_Object = MibTableColumn
hpnicfDot11BlackListRowStatus = _HpnicfDot11BlackListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 11, 1, 4),
    _HpnicfDot11BlackListRowStatus_Type()
)
hpnicfDot11BlackListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11BlackListRowStatus.setStatus("current")
_HpnicfDot11BlackListTimeTicks_Type = TimeTicks
_HpnicfDot11BlackListTimeTicks_Object = MibTableColumn
hpnicfDot11BlackListTimeTicks = _HpnicfDot11BlackListTimeTicks_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 2, 11, 1, 5),
    _HpnicfDot11BlackListTimeTicks_Type()
)
hpnicfDot11BlackListTimeTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BlackListTimeTicks.setStatus("current")
_HpnicfDot11WIDSNotifyGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11WIDSNotifyGroup = _HpnicfDot11WIDSNotifyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 3)
)
_HpnicfDot11WIDSTraps_ObjectIdentity = ObjectIdentity
hpnicfDot11WIDSTraps = _HpnicfDot11WIDSTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 3, 1)
)
_HpnicfDot11WIDSTrapVarObjects_ObjectIdentity = ObjectIdentity
hpnicfDot11WIDSTrapVarObjects = _HpnicfDot11WIDSTrapVarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 3, 2)
)
_HpnicfDot11WIDSRogueMAC_Type = MacAddress
_HpnicfDot11WIDSRogueMAC_Object = MibScalar
hpnicfDot11WIDSRogueMAC = _HpnicfDot11WIDSRogueMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 3, 2, 1),
    _HpnicfDot11WIDSRogueMAC_Type()
)
hpnicfDot11WIDSRogueMAC.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSRogueMAC.setStatus("current")


class _HpnicfDot11WIDSRogueType_Type(Integer32):
    """Custom type hpnicfDot11WIDSRogueType based on Integer32"""
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


_HpnicfDot11WIDSRogueType_Type.__name__ = "Integer32"
_HpnicfDot11WIDSRogueType_Object = MibScalar
hpnicfDot11WIDSRogueType = _HpnicfDot11WIDSRogueType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 3, 2, 2),
    _HpnicfDot11WIDSRogueType_Type()
)
hpnicfDot11WIDSRogueType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSRogueType.setStatus("current")
_HpnicfDot11WIDSMonitorMAC_Type = MacAddress
_HpnicfDot11WIDSMonitorMAC_Object = MibScalar
hpnicfDot11WIDSMonitorMAC = _HpnicfDot11WIDSMonitorMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 3, 2, 3),
    _HpnicfDot11WIDSMonitorMAC_Type()
)
hpnicfDot11WIDSMonitorMAC.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSMonitorMAC.setStatus("current")
_HpnicfDot11WIDSAdHocMAC_Type = MacAddress
_HpnicfDot11WIDSAdHocMAC_Object = MibScalar
hpnicfDot11WIDSAdHocMAC = _HpnicfDot11WIDSAdHocMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 3, 2, 4),
    _HpnicfDot11WIDSAdHocMAC_Type()
)
hpnicfDot11WIDSAdHocMAC.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSAdHocMAC.setStatus("current")
_HpnicfDot11UnauthorSSIDName_Type = HpnicfDot11SSIDStringType
_HpnicfDot11UnauthorSSIDName_Object = MibScalar
hpnicfDot11UnauthorSSIDName = _HpnicfDot11UnauthorSSIDName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 3, 2, 5),
    _HpnicfDot11UnauthorSSIDName_Type()
)
hpnicfDot11UnauthorSSIDName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11UnauthorSSIDName.setStatus("current")
_HpnicfDot11MonitorAPID_Type = HpnicfDot11ObjectIDType
_HpnicfDot11MonitorAPID_Object = MibScalar
hpnicfDot11MonitorAPID = _HpnicfDot11MonitorAPID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 3, 2, 6),
    _HpnicfDot11MonitorAPID_Type()
)
hpnicfDot11MonitorAPID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11MonitorAPID.setStatus("current")
_HpnicfDot11MonitorApRadioID_Type = HpnicfDot11RadioScopeType
_HpnicfDot11MonitorApRadioID_Object = MibScalar
hpnicfDot11MonitorApRadioID = _HpnicfDot11MonitorApRadioID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 3, 2, 7),
    _HpnicfDot11MonitorApRadioID_Type()
)
hpnicfDot11MonitorApRadioID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11MonitorApRadioID.setStatus("current")
_HpnicfDot11WIDSAtkMac_Type = MacAddress
_HpnicfDot11WIDSAtkMac_Object = MibScalar
hpnicfDot11WIDSAtkMac = _HpnicfDot11WIDSAtkMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 3, 2, 8),
    _HpnicfDot11WIDSAtkMac_Type()
)
hpnicfDot11WIDSAtkMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSAtkMac.setStatus("current")
_HpnicfDot11WIDSAtkFrameType_Type = OctetString
_HpnicfDot11WIDSAtkFrameType_Object = MibScalar
hpnicfDot11WIDSAtkFrameType = _HpnicfDot11WIDSAtkFrameType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 3, 2, 9),
    _HpnicfDot11WIDSAtkFrameType_Type()
)
hpnicfDot11WIDSAtkFrameType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSAtkFrameType.setStatus("current")
_HpnicfDot11WIDSAtkChannel_Type = HpnicfDot11ChannelScopeType
_HpnicfDot11WIDSAtkChannel_Object = MibScalar
hpnicfDot11WIDSAtkChannel = _HpnicfDot11WIDSAtkChannel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 3, 2, 10),
    _HpnicfDot11WIDSAtkChannel_Type()
)
hpnicfDot11WIDSAtkChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSAtkChannel.setStatus("current")
_HpnicfDot11WIDSAtkTime_Type = OctetString
_HpnicfDot11WIDSAtkTime_Object = MibScalar
hpnicfDot11WIDSAtkTime = _HpnicfDot11WIDSAtkTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 3, 2, 11),
    _HpnicfDot11WIDSAtkTime_Type()
)
hpnicfDot11WIDSAtkTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSAtkTime.setStatus("current")
_HpnicfDot11WIDSAtkDestMac_Type = MacAddress
_HpnicfDot11WIDSAtkDestMac_Object = MibScalar
hpnicfDot11WIDSAtkDestMac = _HpnicfDot11WIDSAtkDestMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 3, 2, 12),
    _HpnicfDot11WIDSAtkDestMac_Type()
)
hpnicfDot11WIDSAtkDestMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSAtkDestMac.setStatus("current")
_HpnicfDot11WIDSFirstTrapTime_Type = TimeTicks
_HpnicfDot11WIDSFirstTrapTime_Object = MibScalar
hpnicfDot11WIDSFirstTrapTime = _HpnicfDot11WIDSFirstTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 3, 2, 13),
    _HpnicfDot11WIDSFirstTrapTime_Type()
)
hpnicfDot11WIDSFirstTrapTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11WIDSFirstTrapTime.setStatus("current")

# Managed Objects groups


# Notification objects

hpnicfDot11WIDSDetectRogueTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 3, 1, 1)
)
hpnicfDot11WIDSDetectRogueTrap.setObjects(
      *(("HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11WIDSRogueMAC"),
        ("HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11WIDSRogueType"),
        ("HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11WIDSMonitorMAC"),
        ("HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11MonitorAPID"),
        ("HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11MonitorApRadioID"))
)
if mibBuilder.loadTexts:
    hpnicfDot11WIDSDetectRogueTrap.setStatus(
        "current"
    )

hpnicfDot11WIDSAdHocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 3, 1, 2)
)
hpnicfDot11WIDSAdHocTrap.setObjects(
      *(("HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11WIDSAdHocMAC"),
        ("HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11WIDSMonitorMAC"))
)
if mibBuilder.loadTexts:
    hpnicfDot11WIDSAdHocTrap.setStatus(
        "current"
    )

hpnicfDot11WIDSUnauthorSSIDTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 3, 1, 3)
)
hpnicfDot11WIDSUnauthorSSIDTrap.setObjects(
      *(("HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11UnauthorSSIDName"),
        ("HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11WIDSMonitorMAC"),
        ("HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11MonitorAPID"),
        ("HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11MonitorApRadioID"))
)
if mibBuilder.loadTexts:
    hpnicfDot11WIDSUnauthorSSIDTrap.setStatus(
        "current"
    )

hpnicfDot11WIDSDisappearRogueTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 3, 1, 4)
)
hpnicfDot11WIDSDisappearRogueTrap.setObjects(
    ("HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11WIDSRogueMAC")
)
if mibBuilder.loadTexts:
    hpnicfDot11WIDSDisappearRogueTrap.setStatus(
        "current"
    )

hpnicfDot11WIDSDetectAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 3, 1, 5)
)
hpnicfDot11WIDSDetectAttack.setObjects(
      *(("HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11WIDSAtkHisType"),
        ("HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11WIDSAtkHisChl"),
        ("HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11WIDSAtkHisDctTime"),
        ("HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11WIDSAtkHisAPName"))
)
if mibBuilder.loadTexts:
    hpnicfDot11WIDSDetectAttack.setStatus(
        "current"
    )

hpnicfDot11WIDSDetectWBridge = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 3, 1, 6)
)
hpnicfDot11WIDSDetectWBridge.setObjects(
      *(("HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11WIDSRptAPName"),
        ("HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11WIDSRptAPRadioID"),
        ("HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11WIDSRptAPLstDctTime"))
)
if mibBuilder.loadTexts:
    hpnicfDot11WIDSDetectWBridge.setStatus(
        "current"
    )

hpnicfDot11WIDSFloodTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 3, 1, 7)
)
hpnicfDot11WIDSFloodTrap.setObjects(
      *(("HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11WIDSAtkMac"),
        ("HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11WIDSAtkFrameType"),
        ("HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11WIDSFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hpnicfDot11WIDSFloodTrap.setStatus(
        "current"
    )

hpnicfDot11WIDSSpoofTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 3, 1, 8)
)
hpnicfDot11WIDSSpoofTrap.setObjects(
      *(("HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11WIDSAtkMac"),
        ("HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11WIDSAtkFrameType"),
        ("HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11WIDSAtkChannel"),
        ("HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11WIDSAtkTime"),
        ("HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11WIDSAtkDestMac"),
        ("HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11WIDSFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hpnicfDot11WIDSSpoofTrap.setStatus(
        "current"
    )

hpnicfDot11WIDSWeakIVTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 5, 3, 1, 9)
)
hpnicfDot11WIDSWeakIVTrap.setObjects(
      *(("HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11WIDSAtkMac"),
        ("HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11WIDSAtkChannel"),
        ("HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11WIDSAtkTime"),
        ("HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11WIDSAtkDestMac"),
        ("HPN-ICF-DOT11-WIDS-MIB", "hpnicfDot11WIDSFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hpnicfDot11WIDSWeakIVTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-DOT11-WIDS-MIB",
    **{"HpnicfDot11WIDSDevType": HpnicfDot11WIDSDevType,
       "HpnicfDot11WIDSDevPermitType": HpnicfDot11WIDSDevPermitType,
       "HpnicfDot11WIDSAtkType": HpnicfDot11WIDSAtkType,
       "hpnicfDot11WIDS": hpnicfDot11WIDS,
       "hpnicfDot11WIDSConfigGroup": hpnicfDot11WIDSConfigGroup,
       "hpnicfDot11WIDSGlobalConfigGroup": hpnicfDot11WIDSGlobalConfigGroup,
       "hpnicfDot11WIDSScanMode": hpnicfDot11WIDSScanMode,
       "hpnicfDot11WIDSScanChannelList": hpnicfDot11WIDSScanChannelList,
       "hpnicfDot11CntMsrMode": hpnicfDot11CntMsrMode,
       "hpnicfDot11DevAgingTime": hpnicfDot11DevAgingTime,
       "hpnicfDot11DynBlkListEnable": hpnicfDot11DynBlkListEnable,
       "hpnicfDot11DynBlkListLifeTime": hpnicfDot11DynBlkListLifeTime,
       "hpnicfDot11FloodAtkDctEnable": hpnicfDot11FloodAtkDctEnable,
       "hpnicfDot11SpoofAtkDctEnable": hpnicfDot11SpoofAtkDctEnable,
       "hpnicfDot11WeakIVAtkDctEnable": hpnicfDot11WeakIVAtkDctEnable,
       "hpnicfDot11ResetWIDSRogueHistory": hpnicfDot11ResetWIDSRogueHistory,
       "hpnicfDot11ResetWIDSHistroy": hpnicfDot11ResetWIDSHistroy,
       "hpnicfDot11ResetWIDSStatistics": hpnicfDot11ResetWIDSStatistics,
       "hpnicfDot11ResetAllDynBlkList": hpnicfDot11ResetAllDynBlkList,
       "hpnicfDot11ResetAllStcBlkList": hpnicfDot11ResetAllStcBlkList,
       "hpnicfDot11ResetAllWhtBlkList": hpnicfDot11ResetAllWhtBlkList,
       "hpnicfDot11ResetAllDctRogueAP": hpnicfDot11ResetAllDctRogueAP,
       "hpnicfDot11ResetAllDctRogueSta": hpnicfDot11ResetAllDctRogueSta,
       "hpnicfDot11ResetAllDctAdhoc": hpnicfDot11ResetAllDctAdhoc,
       "hpnicfDot11ResetAllDctDevice": hpnicfDot11ResetAllDctDevice,
       "hpnicfDot11ResetAllDctSSID": hpnicfDot11ResetAllDctSSID,
       "hpnicfDot11WidsFloodInterval": hpnicfDot11WidsFloodInterval,
       "hpnicfDot11WidsBlackListThreshold": hpnicfDot11WidsBlackListThreshold,
       "hpnicfDot11SSIDFilterOnOff": hpnicfDot11SSIDFilterOnOff,
       "hpnicfDot11BSSIDFilterOnOff": hpnicfDot11BSSIDFilterOnOff,
       "hpnicfDot11WIDSPermitVendorTable": hpnicfDot11WIDSPermitVendorTable,
       "hpnicfDot11WIDSPermitVendorEntry": hpnicfDot11WIDSPermitVendorEntry,
       "hpnicfDot11VendorOUI": hpnicfDot11VendorOUI,
       "hpnicfDot11PermitVendorRowStatus": hpnicfDot11PermitVendorRowStatus,
       "hpnicfDot11VendorName": hpnicfDot11VendorName,
       "hpnicfDot11WIDSPermitSSIDTable": hpnicfDot11WIDSPermitSSIDTable,
       "hpnicfDot11WIDSPermitSSIDEntry": hpnicfDot11WIDSPermitSSIDEntry,
       "hpnicfDot11PermitSSID": hpnicfDot11PermitSSID,
       "hpnicfDot11PermitSSIDRowStatus": hpnicfDot11PermitSSIDRowStatus,
       "hpnicfDot11PermitSSIDDetected": hpnicfDot11PermitSSIDDetected,
       "hpnicfDot11WIDSIgnoreListTable": hpnicfDot11WIDSIgnoreListTable,
       "hpnicfDot11WIDSIgnoreListEntry": hpnicfDot11WIDSIgnoreListEntry,
       "hpnicfDot11IgnoreMAC": hpnicfDot11IgnoreMAC,
       "hpnicfDot11IgnoreListRowStatus": hpnicfDot11IgnoreListRowStatus,
       "hpnicfDot11IgnoreMACDetected": hpnicfDot11IgnoreMACDetected,
       "hpnicfDot11IgnoreDevType": hpnicfDot11IgnoreDevType,
       "hpnicfDot11WIDSAttackListTable": hpnicfDot11WIDSAttackListTable,
       "hpnicfDot11WIDSAttackListEntry": hpnicfDot11WIDSAttackListEntry,
       "hpnicfDot11AttackDeviceMac": hpnicfDot11AttackDeviceMac,
       "hpnicfDot11AttackListRowStatus": hpnicfDot11AttackListRowStatus,
       "hpnicfDot11AttackDevDetected": hpnicfDot11AttackDevDetected,
       "hpnicfDot11AttackDevType": hpnicfDot11AttackDevType,
       "hpnicfDot11StaticWhiteListTable": hpnicfDot11StaticWhiteListTable,
       "hpnicfDot11StaticWhiteListEntry": hpnicfDot11StaticWhiteListEntry,
       "hpnicfDot11StaticWhiteListMAC": hpnicfDot11StaticWhiteListMAC,
       "hpnicfDot11StaticWhiteListRowStatus": hpnicfDot11StaticWhiteListRowStatus,
       "hpnicfDot11StaticBlackListTable": hpnicfDot11StaticBlackListTable,
       "hpnicfDot11StaticBlackListEntry": hpnicfDot11StaticBlackListEntry,
       "hpnicfDot11StaticBlackListMAC": hpnicfDot11StaticBlackListMAC,
       "hpnicfDot11StaticBlackListRowStatus": hpnicfDot11StaticBlackListRowStatus,
       "hpnicfDot11WIDSPermitBSSIDTable": hpnicfDot11WIDSPermitBSSIDTable,
       "hpnicfDot11WIDSPermitBSSIDEntry": hpnicfDot11WIDSPermitBSSIDEntry,
       "hpnicfDot11PermitBSSID": hpnicfDot11PermitBSSID,
       "hpnicfDot11PermitBSSIDDetected": hpnicfDot11PermitBSSIDDetected,
       "hpnicfDot11PermitBSSIDRowStatus": hpnicfDot11PermitBSSIDRowStatus,
       "hpnicfDot11WIDSDetectGroup": hpnicfDot11WIDSDetectGroup,
       "hpnicfDot11WIDSRogueAPTable": hpnicfDot11WIDSRogueAPTable,
       "hpnicfDot11WIDSRogueAPEntry": hpnicfDot11WIDSRogueAPEntry,
       "hpnicfDot11RogueAPBSSMAC": hpnicfDot11RogueAPBSSMAC,
       "hpnicfDot11RogueAPVendorName": hpnicfDot11RogueAPVendorName,
       "hpnicfDot11RogueAPMonitorNum": hpnicfDot11RogueAPMonitorNum,
       "hpnicfDot11RogueAPFirstDetectTm": hpnicfDot11RogueAPFirstDetectTm,
       "hpnicfDot11RogueAPLastDetectTm": hpnicfDot11RogueAPLastDetectTm,
       "hpnicfDot11RogueAPSSID": hpnicfDot11RogueAPSSID,
       "hpnicfDot11RogueAPMaxSigStrength": hpnicfDot11RogueAPMaxSigStrength,
       "hpnicfDot11RogueAPChannel": hpnicfDot11RogueAPChannel,
       "hpnicfDot11RogueAPBeaconInterval": hpnicfDot11RogueAPBeaconInterval,
       "hpnicfDot11RogueAPAttackedStatus": hpnicfDot11RogueAPAttackedStatus,
       "hpnicfDot11RogueAPToIgnore": hpnicfDot11RogueAPToIgnore,
       "hpnicfDot11RogueAPEncryptStatus": hpnicfDot11RogueAPEncryptStatus,
       "hpnicfDot11RogueAPReset": hpnicfDot11RogueAPReset,
       "hpnicfDot11RogueAPFirstDetectTmStr": hpnicfDot11RogueAPFirstDetectTmStr,
       "hpnicfDot11RogueAPLastDetectTmStr": hpnicfDot11RogueAPLastDetectTmStr,
       "hpnicfDot11WIDSRogueAPExtTable": hpnicfDot11WIDSRogueAPExtTable,
       "hpnicfDot11WIDSRogueAPExtEntry": hpnicfDot11WIDSRogueAPExtEntry,
       "hpnicfDot11WIDSAPID": hpnicfDot11WIDSAPID,
       "hpnicfDot11DetectCurAPSigStrength": hpnicfDot11DetectCurAPSigStrength,
       "hpnicfDot11DetectAPByChannel": hpnicfDot11DetectAPByChannel,
       "hpnicfDot11DetectAPByRadioID": hpnicfDot11DetectAPByRadioID,
       "hpnicfDot11AttackAPStatus": hpnicfDot11AttackAPStatus,
       "hpnicfDot11DetectAPFirstTm": hpnicfDot11DetectAPFirstTm,
       "hpnicfDot11DetectAPLastTm": hpnicfDot11DetectAPLastTm,
       "hpnicfDot11WIDSRogueStaTable": hpnicfDot11WIDSRogueStaTable,
       "hpnicfDot11WIDSRogueStaEntry": hpnicfDot11WIDSRogueStaEntry,
       "hpnicfDot11RogueStaMAC": hpnicfDot11RogueStaMAC,
       "hpnicfDot11RogueStaVendorName": hpnicfDot11RogueStaVendorName,
       "hpnicfDot11RogueStaMonitorNum": hpnicfDot11RogueStaMonitorNum,
       "hpnicfDot11RogueStaFirstDetectTm": hpnicfDot11RogueStaFirstDetectTm,
       "hpnicfDot11RogueStaLastDetectTm": hpnicfDot11RogueStaLastDetectTm,
       "hpnicfDot11RogueStaAccessBSSID": hpnicfDot11RogueStaAccessBSSID,
       "hpnicfDot11RogueStaMaxSigStrength": hpnicfDot11RogueStaMaxSigStrength,
       "hpnicfDot11RogueStaChannel": hpnicfDot11RogueStaChannel,
       "hpnicfDot11RogueStaAttackedStatus": hpnicfDot11RogueStaAttackedStatus,
       "hpnicfDot11RogueStaToIgnore": hpnicfDot11RogueStaToIgnore,
       "hpnicfDot11RogueStaAdHocStatus": hpnicfDot11RogueStaAdHocStatus,
       "hpnicfDot11RogueStaReset": hpnicfDot11RogueStaReset,
       "hpnicfDot11RogueStaFirstDetectTmStr": hpnicfDot11RogueStaFirstDetectTmStr,
       "hpnicfDot11RogueStaLastDetectTmStr": hpnicfDot11RogueStaLastDetectTmStr,
       "hpnicfDot11WIDSRogueStaExtTable": hpnicfDot11WIDSRogueStaExtTable,
       "hpnicfDot11WIDSRogueStaExtEntry": hpnicfDot11WIDSRogueStaExtEntry,
       "hpnicfDot11DetectCurStaSigStrength": hpnicfDot11DetectCurStaSigStrength,
       "hpnicfDot11DetectStaByChannel": hpnicfDot11DetectStaByChannel,
       "hpnicfDot11DetectStaByRadioID": hpnicfDot11DetectStaByRadioID,
       "hpnicfDot11AttackStaStatus": hpnicfDot11AttackStaStatus,
       "hpnicfDot11DetectStaFirstTm": hpnicfDot11DetectStaFirstTm,
       "hpnicfDot11DetectStaLastTm": hpnicfDot11DetectStaLastTm,
       "hpnicfDot11WIDSDetectedDevTable": hpnicfDot11WIDSDetectedDevTable,
       "hpnicfDot11WIDSDetectedDevEntry": hpnicfDot11WIDSDetectedDevEntry,
       "hpnicfDot11WIDSDevMAC": hpnicfDot11WIDSDevMAC,
       "hpnicfDot11WIDSDevType": hpnicfDot11WIDSDevType,
       "hpnicfDot11WIDSDevPermitType": hpnicfDot11WIDSDevPermitType,
       "hpnicfDot11WIDSDevVendor": hpnicfDot11WIDSDevVendor,
       "hpnicfDot11WIDSDevMonitorNum": hpnicfDot11WIDSDevMonitorNum,
       "hpnicfDot11WIDSDevSSID": hpnicfDot11WIDSDevSSID,
       "hpnicfDot11WIDSDevBSSID": hpnicfDot11WIDSDevBSSID,
       "hpnicfDot11WIDSDevChannel": hpnicfDot11WIDSDevChannel,
       "hpnicfDot11WIDSDevMaxRSSI": hpnicfDot11WIDSDevMaxRSSI,
       "hpnicfDot11WIDSDevBeaconIntvl": hpnicfDot11WIDSDevBeaconIntvl,
       "hpnicfDot11WIDSDevFstDctTime": hpnicfDot11WIDSDevFstDctTime,
       "hpnicfDot11WIDSDevLstDctTime": hpnicfDot11WIDSDevLstDctTime,
       "hpnicfDot11WIDSDevReset": hpnicfDot11WIDSDevReset,
       "hpnicfDot11WIDSDevSnr": hpnicfDot11WIDSDevSnr,
       "hpnicfDot11WIDSRptAPTable": hpnicfDot11WIDSRptAPTable,
       "hpnicfDot11WIDSRptAPEntry": hpnicfDot11WIDSRptAPEntry,
       "hpnicfDot11WIDSRptAPMAC": hpnicfDot11WIDSRptAPMAC,
       "hpnicfDot11WIDSRptAPName": hpnicfDot11WIDSRptAPName,
       "hpnicfDot11WIDSRptAPRadioID": hpnicfDot11WIDSRptAPRadioID,
       "hpnicfDot11WIDSRptAPMaxRSSI": hpnicfDot11WIDSRptAPMaxRSSI,
       "hpnicfDot11WIDSRptAPFstDctTime": hpnicfDot11WIDSRptAPFstDctTime,
       "hpnicfDot11WIDSRptAPLstDctTime": hpnicfDot11WIDSRptAPLstDctTime,
       "hpnicfDot11DynBlackListTable": hpnicfDot11DynBlackListTable,
       "hpnicfDot11DynBlackListEntry": hpnicfDot11DynBlackListEntry,
       "hpnicfDot11DynBlackListMAC": hpnicfDot11DynBlackListMAC,
       "hpnicfDot11DynBlackListTime": hpnicfDot11DynBlackListTime,
       "hpnicfDot11DynBlackListReason": hpnicfDot11DynBlackListReason,
       "hpnicfDot11DynBlackListReset": hpnicfDot11DynBlackListReset,
       "hpnicfDot11DynBlackListTimeTicks": hpnicfDot11DynBlackListTimeTicks,
       "hpnicfDot11WIDSRogueHistoryTable": hpnicfDot11WIDSRogueHistoryTable,
       "hpnicfDot11WIDSRogueHistoryEntry": hpnicfDot11WIDSRogueHistoryEntry,
       "hpnicfDot11WIDSRogueHisIndex": hpnicfDot11WIDSRogueHisIndex,
       "hpnicfDot11WIDSRogueHisMAC": hpnicfDot11WIDSRogueHisMAC,
       "hpnicfDot11WIDSRogueHisVendor": hpnicfDot11WIDSRogueHisVendor,
       "hpnicfDot11WIDSRogueHisType": hpnicfDot11WIDSRogueHisType,
       "hpnicfDot11WIDSRogueHisChl": hpnicfDot11WIDSRogueHisChl,
       "hpnicfDot11WIDSRogueHisSSID": hpnicfDot11WIDSRogueHisSSID,
       "hpnicfDot11WIDSRogueHisLastDctTime": hpnicfDot11WIDSRogueHisLastDctTime,
       "hpnicfDot11WIDSAtkHistroyTable": hpnicfDot11WIDSAtkHistroyTable,
       "hpnicfDot11WIDSAtkHistroyEntry": hpnicfDot11WIDSAtkHistroyEntry,
       "hpnicfDot11WIDSAtkHisIndex": hpnicfDot11WIDSAtkHisIndex,
       "hpnicfDot11WIDSAtkHisMAC": hpnicfDot11WIDSAtkHisMAC,
       "hpnicfDot11WIDSAtkHisType": hpnicfDot11WIDSAtkHisType,
       "hpnicfDot11WIDSAtkHisChl": hpnicfDot11WIDSAtkHisChl,
       "hpnicfDot11WIDSAtkHisRSSI": hpnicfDot11WIDSAtkHisRSSI,
       "hpnicfDot11WIDSAtkHisDctTime": hpnicfDot11WIDSAtkHisDctTime,
       "hpnicfDot11WIDSAtkHisAPName": hpnicfDot11WIDSAtkHisAPName,
       "hpnicfDot11WIDSAtkStatis": hpnicfDot11WIDSAtkStatis,
       "hpnicfDot11WIDSAtkStasStartTime": hpnicfDot11WIDSAtkStasStartTime,
       "hpnicfDot11WIDSAtkStasTable": hpnicfDot11WIDSAtkStasTable,
       "hpnicfDot11WIDSAtkStasEntry": hpnicfDot11WIDSAtkStasEntry,
       "hpnicfDot11WIDSAtkStasType": hpnicfDot11WIDSAtkStasType,
       "hpnicfDot11WIDSAtkStasCurCnt": hpnicfDot11WIDSAtkStasCurCnt,
       "hpnicfDot11WIDSAtkStasTotalCnt": hpnicfDot11WIDSAtkStasTotalCnt,
       "hpnicfDot11BlackListTable": hpnicfDot11BlackListTable,
       "hpnicfDot11BlackListEntry": hpnicfDot11BlackListEntry,
       "hpnicfDot11BlackListMAC": hpnicfDot11BlackListMAC,
       "hpnicfDot11BlackListTime": hpnicfDot11BlackListTime,
       "hpnicfDot11BlackListReason": hpnicfDot11BlackListReason,
       "hpnicfDot11BlackListRowStatus": hpnicfDot11BlackListRowStatus,
       "hpnicfDot11BlackListTimeTicks": hpnicfDot11BlackListTimeTicks,
       "hpnicfDot11WIDSNotifyGroup": hpnicfDot11WIDSNotifyGroup,
       "hpnicfDot11WIDSTraps": hpnicfDot11WIDSTraps,
       "hpnicfDot11WIDSDetectRogueTrap": hpnicfDot11WIDSDetectRogueTrap,
       "hpnicfDot11WIDSAdHocTrap": hpnicfDot11WIDSAdHocTrap,
       "hpnicfDot11WIDSUnauthorSSIDTrap": hpnicfDot11WIDSUnauthorSSIDTrap,
       "hpnicfDot11WIDSDisappearRogueTrap": hpnicfDot11WIDSDisappearRogueTrap,
       "hpnicfDot11WIDSDetectAttack": hpnicfDot11WIDSDetectAttack,
       "hpnicfDot11WIDSDetectWBridge": hpnicfDot11WIDSDetectWBridge,
       "hpnicfDot11WIDSFloodTrap": hpnicfDot11WIDSFloodTrap,
       "hpnicfDot11WIDSSpoofTrap": hpnicfDot11WIDSSpoofTrap,
       "hpnicfDot11WIDSWeakIVTrap": hpnicfDot11WIDSWeakIVTrap,
       "hpnicfDot11WIDSTrapVarObjects": hpnicfDot11WIDSTrapVarObjects,
       "hpnicfDot11WIDSRogueMAC": hpnicfDot11WIDSRogueMAC,
       "hpnicfDot11WIDSRogueType": hpnicfDot11WIDSRogueType,
       "hpnicfDot11WIDSMonitorMAC": hpnicfDot11WIDSMonitorMAC,
       "hpnicfDot11WIDSAdHocMAC": hpnicfDot11WIDSAdHocMAC,
       "hpnicfDot11UnauthorSSIDName": hpnicfDot11UnauthorSSIDName,
       "hpnicfDot11MonitorAPID": hpnicfDot11MonitorAPID,
       "hpnicfDot11MonitorApRadioID": hpnicfDot11MonitorApRadioID,
       "hpnicfDot11WIDSAtkMac": hpnicfDot11WIDSAtkMac,
       "hpnicfDot11WIDSAtkFrameType": hpnicfDot11WIDSAtkFrameType,
       "hpnicfDot11WIDSAtkChannel": hpnicfDot11WIDSAtkChannel,
       "hpnicfDot11WIDSAtkTime": hpnicfDot11WIDSAtkTime,
       "hpnicfDot11WIDSAtkDestMac": hpnicfDot11WIDSAtkDestMac,
       "hpnicfDot11WIDSFirstTrapTime": hpnicfDot11WIDSFirstTrapTime}
)
