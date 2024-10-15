# SNMP MIB module (CRI-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CRI-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:50 2024
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




class Boolean(Integer32):
    """Custom type Boolean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )





class YesNo(Integer32):
    """Custom type YesNo based on Integer32"""
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




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sun_ObjectIdentity = ObjectIdentity
sun = _Sun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34, 2)
)
_General_ObjectIdentity = ObjectIdentity
general = _General_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34, 2, 1)
)
_Platform_ObjectIdentity = ObjectIdentity
platform = _Platform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 1)
)


class _PlatformType_Type(Integer32):
    """Custom type platformType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ue10000", 1)
    )


_PlatformType_Type.__name__ = "Integer32"
_PlatformType_Object = MibScalar
platformType = _PlatformType_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 1, 1),
    _PlatformType_Type()
)
platformType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformType.setStatus("mandatory")
_PlatformName_Type = DisplayString
_PlatformName_Object = MibScalar
platformName = _PlatformName_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 1, 2),
    _PlatformName_Type()
)
platformName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformName.setStatus("mandatory")
_PlatformAmbientTemp_Type = Integer32
_PlatformAmbientTemp_Object = MibScalar
platformAmbientTemp = _PlatformAmbientTemp_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 1, 3),
    _PlatformAmbientTemp_Type()
)
platformAmbientTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformAmbientTemp.setStatus("mandatory")


class _PlatformReset_Type(Integer32):
    """Custom type platformReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_PlatformReset_Type.__name__ = "Integer32"
_PlatformReset_Object = MibScalar
platformReset = _PlatformReset_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 1, 4),
    _PlatformReset_Type()
)
platformReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    platformReset.setStatus("mandatory")
_PlatformInterconnectClockFreq_Type = Integer32
_PlatformInterconnectClockFreq_Object = MibScalar
platformInterconnectClockFreq = _PlatformInterconnectClockFreq_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 1, 5),
    _PlatformInterconnectClockFreq_Type()
)
platformInterconnectClockFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformInterconnectClockFreq.setStatus("mandatory")
_PlatformProcClockFreq_Type = Integer32
_PlatformProcClockFreq_Object = MibScalar
platformProcClockFreq = _PlatformProcClockFreq_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 1, 6),
    _PlatformProcClockFreq_Type()
)
platformProcClockFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformProcClockFreq.setStatus("mandatory")
_PlatformJtagClockFreq_Type = Integer32
_PlatformJtagClockFreq_Object = MibScalar
platformJtagClockFreq = _PlatformJtagClockFreq_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 1, 7),
    _PlatformJtagClockFreq_Type()
)
platformJtagClockFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformJtagClockFreq.setStatus("mandatory")


class _PlatformTargetInterconnectClockFreq_Type(Integer32):
    """Custom type platformTargetInterconnectClockFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40000000, 120000000),
    )


_PlatformTargetInterconnectClockFreq_Type.__name__ = "Integer32"
_PlatformTargetInterconnectClockFreq_Object = MibScalar
platformTargetInterconnectClockFreq = _PlatformTargetInterconnectClockFreq_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 1, 8),
    _PlatformTargetInterconnectClockFreq_Type()
)
platformTargetInterconnectClockFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    platformTargetInterconnectClockFreq.setStatus("mandatory")


class _PlatformTargetProcClockMultiple_Type(Integer32):
    """Custom type platformTargetProcClockMultiple based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("three-to-one", 2),
          ("three-to-two", 3),
          ("two-to-one", 1))
    )


_PlatformTargetProcClockMultiple_Type.__name__ = "Integer32"
_PlatformTargetProcClockMultiple_Object = MibScalar
platformTargetProcClockMultiple = _PlatformTargetProcClockMultiple_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 1, 9),
    _PlatformTargetProcClockMultiple_Type()
)
platformTargetProcClockMultiple.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    platformTargetProcClockMultiple.setStatus("mandatory")


class _PlatformTargetJtagClockFreq_Type(Integer32):
    """Custom type platformTargetJtagClockFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000000, 12000000),
    )


_PlatformTargetJtagClockFreq_Type.__name__ = "Integer32"
_PlatformTargetJtagClockFreq_Object = MibScalar
platformTargetJtagClockFreq = _PlatformTargetJtagClockFreq_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 1, 10),
    _PlatformTargetJtagClockFreq_Type()
)
platformTargetJtagClockFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformTargetJtagClockFreq.setStatus("mandatory")


class _PlatformMasterConBrd_Type(Integer32):
    """Custom type platformMasterConBrd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_PlatformMasterConBrd_Type.__name__ = "Integer32"
_PlatformMasterConBrd_Object = MibScalar
platformMasterConBrd = _PlatformMasterConBrd_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 1, 11),
    _PlatformMasterConBrd_Type()
)
platformMasterConBrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformMasterConBrd.setStatus("mandatory")


class _PlatformSysClkConBrd_Type(Integer32):
    """Custom type platformSysClkConBrd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_PlatformSysClkConBrd_Type.__name__ = "Integer32"
_PlatformSysClkConBrd_Object = MibScalar
platformSysClkConBrd = _PlatformSysClkConBrd_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 1, 12),
    _PlatformSysClkConBrd_Type()
)
platformSysClkConBrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformSysClkConBrd.setStatus("mandatory")
_Conf_ObjectIdentity = ObjectIdentity
conf = _Conf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 2)
)
_ConfNumDomain_Type = Integer32
_ConfNumDomain_Object = MibScalar
confNumDomain = _ConfNumDomain_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 2, 1),
    _ConfNumDomain_Type()
)
confNumDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confNumDomain.setStatus("mandatory")
_ConfNumSysBrd_Type = Integer32
_ConfNumSysBrd_Object = MibScalar
confNumSysBrd = _ConfNumSysBrd_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 2, 2),
    _ConfNumSysBrd_Type()
)
confNumSysBrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confNumSysBrd.setStatus("mandatory")
_ConfNumProc_Type = Integer32
_ConfNumProc_Object = MibScalar
confNumProc = _ConfNumProc_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 2, 3),
    _ConfNumProc_Type()
)
confNumProc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confNumProc.setStatus("mandatory")
_ConfNumConBrd_Type = Integer32
_ConfNumConBrd_Object = MibScalar
confNumConBrd = _ConfNumConBrd_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 2, 4),
    _ConfNumConBrd_Type()
)
confNumConBrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confNumConBrd.setStatus("mandatory")
_ConfNumCenterplane_Type = Integer32
_ConfNumCenterplane_Object = MibScalar
confNumCenterplane = _ConfNumCenterplane_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 2, 5),
    _ConfNumCenterplane_Type()
)
confNumCenterplane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confNumCenterplane.setStatus("mandatory")
_ConfNumSuppBrd_Type = Integer32
_ConfNumSuppBrd_Object = MibScalar
confNumSuppBrd = _ConfNumSuppBrd_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 2, 6),
    _ConfNumSuppBrd_Type()
)
confNumSuppBrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confNumSuppBrd.setStatus("mandatory")
_ConfNumIoCab_Type = Integer32
_ConfNumIoCab_Object = MibScalar
confNumIoCab = _ConfNumIoCab_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 2, 7),
    _ConfNumIoCab_Type()
)
confNumIoCab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confNumIoCab.setStatus("mandatory")
_ConfNumFanTray_Type = Integer32
_ConfNumFanTray_Object = MibScalar
confNumFanTray = _ConfNumFanTray_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 2, 8),
    _ConfNumFanTray_Type()
)
confNumFanTray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confNumFanTray.setStatus("mandatory")
_ConfNumBulkPower_Type = Integer32
_ConfNumBulkPower_Object = MibScalar
confNumBulkPower = _ConfNumBulkPower_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 2, 9),
    _ConfNumBulkPower_Type()
)
confNumBulkPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confNumBulkPower.setStatus("mandatory")
_ConfNumSysBrdPower_Type = Integer32
_ConfNumSysBrdPower_Object = MibScalar
confNumSysBrdPower = _ConfNumSysBrdPower_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 2, 10),
    _ConfNumSysBrdPower_Type()
)
confNumSysBrdPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confNumSysBrdPower.setStatus("mandatory")
_ConfSysBrdList_Type = DisplayString
_ConfSysBrdList_Object = MibScalar
confSysBrdList = _ConfSysBrdList_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 2, 11),
    _ConfSysBrdList_Type()
)
confSysBrdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confSysBrdList.setStatus("mandatory")
_ConfProcList_Type = DisplayString
_ConfProcList_Object = MibScalar
confProcList = _ConfProcList_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 2, 12),
    _ConfProcList_Type()
)
confProcList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confProcList.setStatus("mandatory")
_ConfConBrdList_Type = DisplayString
_ConfConBrdList_Object = MibScalar
confConBrdList = _ConfConBrdList_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 2, 13),
    _ConfConBrdList_Type()
)
confConBrdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confConBrdList.setStatus("mandatory")
_ConfCenterplaneList_Type = DisplayString
_ConfCenterplaneList_Object = MibScalar
confCenterplaneList = _ConfCenterplaneList_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 2, 14),
    _ConfCenterplaneList_Type()
)
confCenterplaneList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confCenterplaneList.setStatus("mandatory")
_ConfSuppBrdList_Type = DisplayString
_ConfSuppBrdList_Object = MibScalar
confSuppBrdList = _ConfSuppBrdList_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 2, 15),
    _ConfSuppBrdList_Type()
)
confSuppBrdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confSuppBrdList.setStatus("mandatory")
_ConfIoCabList_Type = DisplayString
_ConfIoCabList_Object = MibScalar
confIoCabList = _ConfIoCabList_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 2, 16),
    _ConfIoCabList_Type()
)
confIoCabList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confIoCabList.setStatus("mandatory")
_ConfFanTrayList_Type = DisplayString
_ConfFanTrayList_Object = MibScalar
confFanTrayList = _ConfFanTrayList_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 2, 17),
    _ConfFanTrayList_Type()
)
confFanTrayList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confFanTrayList.setStatus("mandatory")
_ConfBulkPowerList_Type = DisplayString
_ConfBulkPowerList_Object = MibScalar
confBulkPowerList = _ConfBulkPowerList_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 2, 18),
    _ConfBulkPowerList_Type()
)
confBulkPowerList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confBulkPowerList.setStatus("mandatory")
_ConfSysBrdPowerList_Type = DisplayString
_ConfSysBrdPowerList_Object = MibScalar
confSysBrdPowerList = _ConfSysBrdPowerList_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 2, 19),
    _ConfSysBrdPowerList_Type()
)
confSysBrdPowerList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confSysBrdPowerList.setStatus("mandatory")
_ConfMaxProcPerSysBrd_Type = Integer32
_ConfMaxProcPerSysBrd_Object = MibScalar
confMaxProcPerSysBrd = _ConfMaxProcPerSysBrd_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 2, 20),
    _ConfMaxProcPerSysBrd_Type()
)
confMaxProcPerSysBrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confMaxProcPerSysBrd.setStatus("mandatory")
_ConfMaxFanPerTray_Type = Integer32
_ConfMaxFanPerTray_Object = MibScalar
confMaxFanPerTray = _ConfMaxFanPerTray_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 2, 21),
    _ConfMaxFanPerTray_Type()
)
confMaxFanPerTray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confMaxFanPerTray.setStatus("mandatory")
_ConfMaxLEDPerFanTray_Type = Integer32
_ConfMaxLEDPerFanTray_Object = MibScalar
confMaxLEDPerFanTray = _ConfMaxLEDPerFanTray_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 2, 22),
    _ConfMaxLEDPerFanTray_Type()
)
confMaxLEDPerFanTray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confMaxLEDPerFanTray.setStatus("mandatory")
_ConfMaxLEDPerBulkPower_Type = Integer32
_ConfMaxLEDPerBulkPower_Object = MibScalar
confMaxLEDPerBulkPower = _ConfMaxLEDPerBulkPower_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 2, 23),
    _ConfMaxLEDPerBulkPower_Type()
)
confMaxLEDPerBulkPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confMaxLEDPerBulkPower.setStatus("mandatory")
_ConfMaxLEDPerSysBrd_Type = Integer32
_ConfMaxLEDPerSysBrd_Object = MibScalar
confMaxLEDPerSysBrd = _ConfMaxLEDPerSysBrd_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 2, 24),
    _ConfMaxLEDPerSysBrd_Type()
)
confMaxLEDPerSysBrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confMaxLEDPerSysBrd.setStatus("mandatory")


class _ConfMemAddrMap_Type(OctetString):
    """Custom type confMemAddrMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_ConfMemAddrMap_Type.__name__ = "OctetString"
_ConfMemAddrMap_Object = MibScalar
confMemAddrMap = _ConfMemAddrMap_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 2, 25),
    _ConfMemAddrMap_Type()
)
confMemAddrMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confMemAddrMap.setStatus("mandatory")
_DomainTable_Object = MibTable
domainTable = _DomainTable_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 3)
)
if mibBuilder.loadTexts:
    domainTable.setStatus("mandatory")
_DomainEntry_Object = MibTableRow
domainEntry = _DomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 3, 1)
)
domainEntry.setIndexNames(
    (0, "CRI-SERVER-MIB", "domainIndex"),
)
if mibBuilder.loadTexts:
    domainEntry.setStatus("mandatory")
_DomainIndex_Type = Integer32
_DomainIndex_Object = MibTableColumn
domainIndex = _DomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 3, 1, 1),
    _DomainIndex_Type()
)
domainIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainIndex.setStatus("mandatory")
_DomainName_Type = DisplayString
_DomainName_Object = MibTableColumn
domainName = _DomainName_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 3, 1, 2),
    _DomainName_Type()
)
domainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainName.setStatus("mandatory")


class _DomainNumSysBrd_Type(Integer32):
    """Custom type domainNumSysBrd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DomainNumSysBrd_Type.__name__ = "Integer32"
_DomainNumSysBrd_Object = MibTableColumn
domainNumSysBrd = _DomainNumSysBrd_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 3, 1, 3),
    _DomainNumSysBrd_Type()
)
domainNumSysBrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainNumSysBrd.setStatus("mandatory")
_DomainSysBrdList_Type = DisplayString
_DomainSysBrdList_Object = MibTableColumn
domainSysBrdList = _DomainSysBrdList_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 3, 1, 4),
    _DomainSysBrdList_Type()
)
domainSysBrdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainSysBrdList.setStatus("mandatory")
_DomainOSVersion_Type = DisplayString
_DomainOSVersion_Object = MibTableColumn
domainOSVersion = _DomainOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 3, 1, 5),
    _DomainOSVersion_Type()
)
domainOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainOSVersion.setStatus("mandatory")
_DomainProcList_Type = DisplayString
_DomainProcList_Object = MibTableColumn
domainProcList = _DomainProcList_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 3, 1, 6),
    _DomainProcList_Type()
)
domainProcList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainProcList.setStatus("mandatory")
_DomainBootProc_Type = Integer32
_DomainBootProc_Object = MibTableColumn
domainBootProc = _DomainBootProc_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 3, 1, 7),
    _DomainBootProc_Type()
)
domainBootProc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    domainBootProc.setStatus("mandatory")
_DomainInterruptVector_Type = Integer32
_DomainInterruptVector_Object = MibTableColumn
domainInterruptVector = _DomainInterruptVector_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 3, 1, 8),
    _DomainInterruptVector_Type()
)
domainInterruptVector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    domainInterruptVector.setStatus("mandatory")
_DomainSysBrdConfig_Type = DisplayString
_DomainSysBrdConfig_Object = MibTableColumn
domainSysBrdConfig = _DomainSysBrdConfig_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 3, 1, 9),
    _DomainSysBrdConfig_Type()
)
domainSysBrdConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainSysBrdConfig.setStatus("mandatory")
_DomainProcConfig_Type = DisplayString
_DomainProcConfig_Object = MibTableColumn
domainProcConfig = _DomainProcConfig_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 3, 1, 10),
    _DomainProcConfig_Type()
)
domainProcConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainProcConfig.setStatus("mandatory")
_DomainABusConfig_Type = DisplayString
_DomainABusConfig_Object = MibTableColumn
domainABusConfig = _DomainABusConfig_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 3, 1, 11),
    _DomainABusConfig_Type()
)
domainABusConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainABusConfig.setStatus("mandatory")
_DomainDBusConfig_Type = DisplayString
_DomainDBusConfig_Object = MibTableColumn
domainDBusConfig = _DomainDBusConfig_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 3, 1, 12),
    _DomainDBusConfig_Type()
)
domainDBusConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainDBusConfig.setStatus("mandatory")
_SysBrdGenTable_Object = MibTable
sysBrdGenTable = _SysBrdGenTable_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 4)
)
if mibBuilder.loadTexts:
    sysBrdGenTable.setStatus("mandatory")
_SysBrdGenEntry_Object = MibTableRow
sysBrdGenEntry = _SysBrdGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 4, 1)
)
sysBrdGenEntry.setIndexNames(
    (0, "CRI-SERVER-MIB", "sysBrdGenIndex"),
)
if mibBuilder.loadTexts:
    sysBrdGenEntry.setStatus("mandatory")
_SysBrdGenIndex_Type = Integer32
_SysBrdGenIndex_Object = MibTableColumn
sysBrdGenIndex = _SysBrdGenIndex_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 4, 1, 1),
    _SysBrdGenIndex_Type()
)
sysBrdGenIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBrdGenIndex.setStatus("mandatory")
_SysBrdGenNum_Type = Integer32
_SysBrdGenNum_Object = MibTableColumn
sysBrdGenNum = _SysBrdGenNum_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 4, 1, 2),
    _SysBrdGenNum_Type()
)
sysBrdGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBrdGenNum.setStatus("mandatory")


class _SysBrdGenPower_Type(Integer32):
    """Custom type sysBrdGenPower based on Integer32"""
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


_SysBrdGenPower_Type.__name__ = "Integer32"
_SysBrdGenPower_Object = MibTableColumn
sysBrdGenPower = _SysBrdGenPower_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 4, 1, 3),
    _SysBrdGenPower_Type()
)
sysBrdGenPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBrdGenPower.setStatus("mandatory")
_SysBrdGenNumProc_Type = Integer32
_SysBrdGenNumProc_Object = MibTableColumn
sysBrdGenNumProc = _SysBrdGenNumProc_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 4, 1, 4),
    _SysBrdGenNumProc_Type()
)
sysBrdGenNumProc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBrdGenNumProc.setStatus("mandatory")
_SysBrdGenProcList_Type = DisplayString
_SysBrdGenProcList_Object = MibTableColumn
sysBrdGenProcList = _SysBrdGenProcList_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 4, 1, 5),
    _SysBrdGenProcList_Type()
)
sysBrdGenProcList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBrdGenProcList.setStatus("mandatory")


class _SysBrdGenReset_Type(Integer32):
    """Custom type sysBrdGenReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_SysBrdGenReset_Type.__name__ = "Integer32"
_SysBrdGenReset_Object = MibTableColumn
sysBrdGenReset = _SysBrdGenReset_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 4, 1, 6),
    _SysBrdGenReset_Type()
)
sysBrdGenReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysBrdGenReset.setStatus("mandatory")


class _SysBrdGenPowerControl_Type(Integer32):
    """Custom type sysBrdGenPowerControl based on Integer32"""
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


_SysBrdGenPowerControl_Type.__name__ = "Integer32"
_SysBrdGenPowerControl_Object = MibTableColumn
sysBrdGenPowerControl = _SysBrdGenPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 4, 1, 7),
    _SysBrdGenPowerControl_Type()
)
sysBrdGenPowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysBrdGenPowerControl.setStatus("mandatory")
_ProcStateGenTable_Object = MibTable
procStateGenTable = _ProcStateGenTable_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 5)
)
if mibBuilder.loadTexts:
    procStateGenTable.setStatus("mandatory")
_ProcStateGenEntry_Object = MibTableRow
procStateGenEntry = _ProcStateGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 5, 1)
)
procStateGenEntry.setIndexNames(
    (0, "CRI-SERVER-MIB", "procStateGenIndex"),
)
if mibBuilder.loadTexts:
    procStateGenEntry.setStatus("mandatory")
_ProcStateGenIndex_Type = Integer32
_ProcStateGenIndex_Object = MibTableColumn
procStateGenIndex = _ProcStateGenIndex_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 5, 1, 1),
    _ProcStateGenIndex_Type()
)
procStateGenIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procStateGenIndex.setStatus("mandatory")
_ProcStateGenNum_Type = Integer32
_ProcStateGenNum_Object = MibTableColumn
procStateGenNum = _ProcStateGenNum_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 5, 1, 2),
    _ProcStateGenNum_Type()
)
procStateGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procStateGenNum.setStatus("mandatory")
_ProcStateGenHeartbeat_Type = Counter32
_ProcStateGenHeartbeat_Object = MibTableColumn
procStateGenHeartbeat = _ProcStateGenHeartbeat_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 5, 1, 3),
    _ProcStateGenHeartbeat_Type()
)
procStateGenHeartbeat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procStateGenHeartbeat.setStatus("mandatory")


class _ProcStateGenPgmSignature_Type(Integer32):
    """Custom type procStateGenPgmSignature based on Integer32"""
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
        *(("download-helper", 2),
          ("obp", 3),
          ("os", 4),
          ("post", 1),
          ("unknown", 5))
    )


_ProcStateGenPgmSignature_Type.__name__ = "Integer32"
_ProcStateGenPgmSignature_Object = MibTableColumn
procStateGenPgmSignature = _ProcStateGenPgmSignature_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 5, 1, 4),
    _ProcStateGenPgmSignature_Type()
)
procStateGenPgmSignature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procStateGenPgmSignature.setStatus("mandatory")


class _ProcStateGenPgmState_Type(Integer32):
    """Custom type procStateGenPgmState based on Integer32"""
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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("arbstop", 4),
          ("booting", 12),
          ("callback", 8),
          ("detached", 7),
          ("exit", 2),
          ("none", 23),
          ("offline", 11),
          ("poweroff", 6),
          ("prerun", 3),
          ("quiesce-in-progress", 21),
          ("quiesced", 20),
          ("redmode", 18),
          ("redmode-sync", 19),
          ("reset", 5),
          ("resume-in-progress", 22),
          ("run", 1),
          ("sir", 16),
          ("sir-sync", 17),
          ("unknown", 13),
          ("watchdog", 9),
          ("watchdog-sync", 10),
          ("xir", 14),
          ("xir-sync", 15))
    )


_ProcStateGenPgmState_Type.__name__ = "Integer32"
_ProcStateGenPgmState_Object = MibTableColumn
procStateGenPgmState = _ProcStateGenPgmState_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 5, 1, 5),
    _ProcStateGenPgmState_Type()
)
procStateGenPgmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procStateGenPgmState.setStatus("mandatory")


class _ProcStateGenPgmSubState_Type(Integer32):
    """Custom type procStateGenPgmSubState based on Integer32"""
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
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("exit-environ", 2),
          ("exit-extern-init-reset", 11),
          ("exit-halt", 1),
          ("exit-hung", 6),
          ("exit-null", 14),
          ("exit-obp-reset", 13),
          ("exit-panic-reboot", 8),
          ("exit-panic1", 4),
          ("exit-panic2", 5),
          ("exit-reboot", 3),
          ("exit-redmode-reboot", 12),
          ("exit-soft-init-reset", 10),
          ("exit-watch", 7),
          ("exit-watchdog-reboot", 9),
          ("unknown", 15))
    )


_ProcStateGenPgmSubState_Type.__name__ = "Integer32"
_ProcStateGenPgmSubState_Object = MibTableColumn
procStateGenPgmSubState = _ProcStateGenPgmSubState_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 5, 1, 6),
    _ProcStateGenPgmSubState_Type()
)
procStateGenPgmSubState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procStateGenPgmSubState.setStatus("mandatory")
_ProcStateGenTemp_Type = Integer32
_ProcStateGenTemp_Object = MibTableColumn
procStateGenTemp = _ProcStateGenTemp_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 5, 1, 7),
    _ProcStateGenTemp_Type()
)
procStateGenTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procStateGenTemp.setStatus("mandatory")
_ProcCommGenTable_Object = MibTable
procCommGenTable = _ProcCommGenTable_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 6)
)
if mibBuilder.loadTexts:
    procCommGenTable.setStatus("mandatory")
_ProcCommGenEntry_Object = MibTableRow
procCommGenEntry = _ProcCommGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 6, 1)
)
procCommGenEntry.setIndexNames(
    (0, "CRI-SERVER-MIB", "procCommGenIndex"),
)
if mibBuilder.loadTexts:
    procCommGenEntry.setStatus("mandatory")
_ProcCommGenIndex_Type = Integer32
_ProcCommGenIndex_Object = MibTableColumn
procCommGenIndex = _ProcCommGenIndex_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 6, 1, 1),
    _ProcCommGenIndex_Type()
)
procCommGenIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procCommGenIndex.setStatus("mandatory")
_ProcCommGenNum_Type = Integer32
_ProcCommGenNum_Object = MibTableColumn
procCommGenNum = _ProcCommGenNum_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 6, 1, 2),
    _ProcCommGenNum_Type()
)
procCommGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procCommGenNum.setStatus("mandatory")
_ProcCommGenSspMboxLen_Type = Integer32
_ProcCommGenSspMboxLen_Object = MibTableColumn
procCommGenSspMboxLen = _ProcCommGenSspMboxLen_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 6, 1, 3),
    _ProcCommGenSspMboxLen_Type()
)
procCommGenSspMboxLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    procCommGenSspMboxLen.setStatus("mandatory")


class _ProcCommGenSspMboxFlag_Type(Integer32):
    """Custom type procCommGenSspMboxFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_ProcCommGenSspMboxFlag_Type.__name__ = "Integer32"
_ProcCommGenSspMboxFlag_Object = MibTableColumn
procCommGenSspMboxFlag = _ProcCommGenSspMboxFlag_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 6, 1, 4),
    _ProcCommGenSspMboxFlag_Type()
)
procCommGenSspMboxFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    procCommGenSspMboxFlag.setStatus("mandatory")


class _ProcCommGenSspMboxCmd_Type(Integer32):
    """Custom type procCommGenSspMboxCmd based on Integer32"""
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
        *(("command-success", 1),
          ("environ", 4),
          ("goto-obp", 2),
          ("goto-panic", 3))
    )


_ProcCommGenSspMboxCmd_Type.__name__ = "Integer32"
_ProcCommGenSspMboxCmd_Object = MibTableColumn
procCommGenSspMboxCmd = _ProcCommGenSspMboxCmd_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 6, 1, 5),
    _ProcCommGenSspMboxCmd_Type()
)
procCommGenSspMboxCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    procCommGenSspMboxCmd.setStatus("mandatory")


class _ProcCommGenSspMboxData_Type(OctetString):
    """Custom type procCommGenSspMboxData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_ProcCommGenSspMboxData_Type.__name__ = "OctetString"
_ProcCommGenSspMboxData_Object = MibTableColumn
procCommGenSspMboxData = _ProcCommGenSspMboxData_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 6, 1, 6),
    _ProcCommGenSspMboxData_Type()
)
procCommGenSspMboxData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    procCommGenSspMboxData.setStatus("mandatory")
_ProcCommGenHostMboxLen_Type = Integer32
_ProcCommGenHostMboxLen_Object = MibTableColumn
procCommGenHostMboxLen = _ProcCommGenHostMboxLen_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 6, 1, 7),
    _ProcCommGenHostMboxLen_Type()
)
procCommGenHostMboxLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    procCommGenHostMboxLen.setStatus("mandatory")


class _ProcCommGenHostMboxFlag_Type(Integer32):
    """Custom type procCommGenHostMboxFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_ProcCommGenHostMboxFlag_Type.__name__ = "Integer32"
_ProcCommGenHostMboxFlag_Object = MibTableColumn
procCommGenHostMboxFlag = _ProcCommGenHostMboxFlag_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 6, 1, 8),
    _ProcCommGenHostMboxFlag_Type()
)
procCommGenHostMboxFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    procCommGenHostMboxFlag.setStatus("mandatory")


class _ProcCommGenHostMboxCmd_Type(Integer32):
    """Custom type procCommGenHostMboxCmd based on Integer32"""
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
        *(("command-success", 1),
          ("environ", 4),
          ("goto-obp", 2),
          ("goto-panic", 3))
    )


_ProcCommGenHostMboxCmd_Type.__name__ = "Integer32"
_ProcCommGenHostMboxCmd_Object = MibTableColumn
procCommGenHostMboxCmd = _ProcCommGenHostMboxCmd_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 6, 1, 9),
    _ProcCommGenHostMboxCmd_Type()
)
procCommGenHostMboxCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    procCommGenHostMboxCmd.setStatus("mandatory")


class _ProcCommGenHostMboxData_Type(OctetString):
    """Custom type procCommGenHostMboxData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_ProcCommGenHostMboxData_Type.__name__ = "OctetString"
_ProcCommGenHostMboxData_Object = MibTableColumn
procCommGenHostMboxData = _ProcCommGenHostMboxData_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 6, 1, 10),
    _ProcCommGenHostMboxData_Type()
)
procCommGenHostMboxData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    procCommGenHostMboxData.setStatus("mandatory")
_ProcCommGenObpMboxLen_Type = Integer32
_ProcCommGenObpMboxLen_Object = MibTableColumn
procCommGenObpMboxLen = _ProcCommGenObpMboxLen_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 6, 1, 11),
    _ProcCommGenObpMboxLen_Type()
)
procCommGenObpMboxLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    procCommGenObpMboxLen.setStatus("mandatory")


class _ProcCommGenObpMboxFlag_Type(Integer32):
    """Custom type procCommGenObpMboxFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_ProcCommGenObpMboxFlag_Type.__name__ = "Integer32"
_ProcCommGenObpMboxFlag_Object = MibTableColumn
procCommGenObpMboxFlag = _ProcCommGenObpMboxFlag_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 6, 1, 12),
    _ProcCommGenObpMboxFlag_Type()
)
procCommGenObpMboxFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    procCommGenObpMboxFlag.setStatus("mandatory")


class _ProcCommGenObpMboxCmd_Type(Integer32):
    """Custom type procCommGenObpMboxCmd based on Integer32"""
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
        *(("get-ap-database-loc", 7),
          ("get-eeprom-image", 3),
          ("invalidate-reboot-info", 5),
          ("move-cpu0", 6),
          ("put-eeprom-image", 4),
          ("release-slave-cpu", 1),
          ("store-boot-path-info", 8),
          ("time-of-day", 2))
    )


_ProcCommGenObpMboxCmd_Type.__name__ = "Integer32"
_ProcCommGenObpMboxCmd_Object = MibTableColumn
procCommGenObpMboxCmd = _ProcCommGenObpMboxCmd_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 6, 1, 13),
    _ProcCommGenObpMboxCmd_Type()
)
procCommGenObpMboxCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    procCommGenObpMboxCmd.setStatus("mandatory")


class _ProcCommGenObpMboxData_Type(OctetString):
    """Custom type procCommGenObpMboxData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_ProcCommGenObpMboxData_Type.__name__ = "OctetString"
_ProcCommGenObpMboxData_Object = MibTableColumn
procCommGenObpMboxData = _ProcCommGenObpMboxData_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 6, 1, 14),
    _ProcCommGenObpMboxData_Type()
)
procCommGenObpMboxData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    procCommGenObpMboxData.setStatus("mandatory")


class _ProcCommGenCvcInputData_Type(OctetString):
    """Custom type procCommGenCvcInputData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1024, 1024),
    )


_ProcCommGenCvcInputData_Type.__name__ = "OctetString"
_ProcCommGenCvcInputData_Object = MibTableColumn
procCommGenCvcInputData = _ProcCommGenCvcInputData_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 6, 1, 15),
    _ProcCommGenCvcInputData_Type()
)
procCommGenCvcInputData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    procCommGenCvcInputData.setStatus("mandatory")


class _ProcCommGenCvcOutputData_Type(OctetString):
    """Custom type procCommGenCvcOutputData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1024, 1024),
    )


_ProcCommGenCvcOutputData_Type.__name__ = "OctetString"
_ProcCommGenCvcOutputData_Object = MibTableColumn
procCommGenCvcOutputData = _ProcCommGenCvcOutputData_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 6, 1, 16),
    _ProcCommGenCvcOutputData_Type()
)
procCommGenCvcOutputData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    procCommGenCvcOutputData.setStatus("mandatory")
_CbGenTable_Object = MibTable
cbGenTable = _CbGenTable_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 7)
)
if mibBuilder.loadTexts:
    cbGenTable.setStatus("mandatory")
_CbGenEntry_Object = MibTableRow
cbGenEntry = _CbGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 7, 1)
)
cbGenEntry.setIndexNames(
    (0, "CRI-SERVER-MIB", "cbGenIndex"),
)
if mibBuilder.loadTexts:
    cbGenEntry.setStatus("mandatory")
_CbGenIndex_Type = Integer32
_CbGenIndex_Object = MibTableColumn
cbGenIndex = _CbGenIndex_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 7, 1, 1),
    _CbGenIndex_Type()
)
cbGenIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbGenIndex.setStatus("mandatory")
_CbGenNum_Type = Integer32
_CbGenNum_Object = MibTableColumn
cbGenNum = _CbGenNum_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 7, 1, 2),
    _CbGenNum_Type()
)
cbGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbGenNum.setStatus("mandatory")


class _CbGenPower_Type(Integer32):
    """Custom type cbGenPower based on Integer32"""
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


_CbGenPower_Type.__name__ = "Integer32"
_CbGenPower_Object = MibTableColumn
cbGenPower = _CbGenPower_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 7, 1, 3),
    _CbGenPower_Type()
)
cbGenPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbGenPower.setStatus("mandatory")


class _CbGenPowerControl_Type(Integer32):
    """Custom type cbGenPowerControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("off", 1)
    )


_CbGenPowerControl_Type.__name__ = "Integer32"
_CbGenPowerControl_Object = MibTableColumn
cbGenPowerControl = _CbGenPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 7, 1, 4),
    _CbGenPowerControl_Type()
)
cbGenPowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbGenPowerControl.setStatus("mandatory")
_IoCabGenTable_Object = MibTable
ioCabGenTable = _IoCabGenTable_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 8)
)
if mibBuilder.loadTexts:
    ioCabGenTable.setStatus("mandatory")
_IoCabGenEntry_Object = MibTableRow
ioCabGenEntry = _IoCabGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 8, 1)
)
ioCabGenEntry.setIndexNames(
    (0, "CRI-SERVER-MIB", "ioCabGenIndex"),
)
if mibBuilder.loadTexts:
    ioCabGenEntry.setStatus("mandatory")
_IoCabGenIndex_Type = Integer32
_IoCabGenIndex_Object = MibTableColumn
ioCabGenIndex = _IoCabGenIndex_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 8, 1, 1),
    _IoCabGenIndex_Type()
)
ioCabGenIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioCabGenIndex.setStatus("mandatory")
_IoCabGenNum_Type = Integer32
_IoCabGenNum_Object = MibTableColumn
ioCabGenNum = _IoCabGenNum_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 8, 1, 2),
    _IoCabGenNum_Type()
)
ioCabGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioCabGenNum.setStatus("mandatory")


class _IoCabGenPower_Type(Integer32):
    """Custom type ioCabGenPower based on Integer32"""
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


_IoCabGenPower_Type.__name__ = "Integer32"
_IoCabGenPower_Object = MibTableColumn
ioCabGenPower = _IoCabGenPower_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 8, 1, 3),
    _IoCabGenPower_Type()
)
ioCabGenPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ioCabGenPower.setStatus("mandatory")
_FanTrayGenTable_Object = MibTable
fanTrayGenTable = _FanTrayGenTable_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 10)
)
if mibBuilder.loadTexts:
    fanTrayGenTable.setStatus("mandatory")
_FanTrayGenEntry_Object = MibTableRow
fanTrayGenEntry = _FanTrayGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 10, 1)
)
fanTrayGenEntry.setIndexNames(
    (0, "CRI-SERVER-MIB", "fanTrayGenIndex"),
)
if mibBuilder.loadTexts:
    fanTrayGenEntry.setStatus("mandatory")
_FanTrayGenIndex_Type = Integer32
_FanTrayGenIndex_Object = MibTableColumn
fanTrayGenIndex = _FanTrayGenIndex_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 10, 1, 1),
    _FanTrayGenIndex_Type()
)
fanTrayGenIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanTrayGenIndex.setStatus("mandatory")
_FanTrayGenNum_Type = Integer32
_FanTrayGenNum_Object = MibTableColumn
fanTrayGenNum = _FanTrayGenNum_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 10, 1, 2),
    _FanTrayGenNum_Type()
)
fanTrayGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanTrayGenNum.setStatus("mandatory")


class _FanTrayGenPower_Type(Integer32):
    """Custom type fanTrayGenPower based on Integer32"""
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


_FanTrayGenPower_Type.__name__ = "Integer32"
_FanTrayGenPower_Object = MibTableColumn
fanTrayGenPower = _FanTrayGenPower_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 10, 1, 3),
    _FanTrayGenPower_Type()
)
fanTrayGenPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanTrayGenPower.setStatus("mandatory")
_FanGenTable_Object = MibTable
fanGenTable = _FanGenTable_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 11)
)
if mibBuilder.loadTexts:
    fanGenTable.setStatus("mandatory")
_FanGenEntry_Object = MibTableRow
fanGenEntry = _FanGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 11, 1)
)
fanGenEntry.setIndexNames(
    (0, "CRI-SERVER-MIB", "fanGenIndex"),
)
if mibBuilder.loadTexts:
    fanGenEntry.setStatus("mandatory")
_FanGenIndex_Type = Integer32
_FanGenIndex_Object = MibTableColumn
fanGenIndex = _FanGenIndex_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 11, 1, 1),
    _FanGenIndex_Type()
)
fanGenIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanGenIndex.setStatus("mandatory")
_FanGenTraySlotNum_Type = Integer32
_FanGenTraySlotNum_Object = MibTableColumn
fanGenTraySlotNum = _FanGenTraySlotNum_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 11, 1, 2),
    _FanGenTraySlotNum_Type()
)
fanGenTraySlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanGenTraySlotNum.setStatus("mandatory")
_FanGenNum_Type = Integer32
_FanGenNum_Object = MibTableColumn
fanGenNum = _FanGenNum_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 11, 1, 3),
    _FanGenNum_Type()
)
fanGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanGenNum.setStatus("mandatory")


class _FanGenStatus_Type(Integer32):
    """Custom type fanGenStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fail", 3),
          ("off", 2),
          ("on", 1))
    )


_FanGenStatus_Type.__name__ = "Integer32"
_FanGenStatus_Object = MibTableColumn
fanGenStatus = _FanGenStatus_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 11, 1, 4),
    _FanGenStatus_Type()
)
fanGenStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanGenStatus.setStatus("mandatory")


class _FanGenSpeed_Type(Integer32):
    """Custom type fanGenSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fast", 2),
          ("nominal", 1))
    )


_FanGenSpeed_Type.__name__ = "Integer32"
_FanGenSpeed_Object = MibTableColumn
fanGenSpeed = _FanGenSpeed_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 11, 1, 5),
    _FanGenSpeed_Type()
)
fanGenSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanGenSpeed.setStatus("mandatory")


class _FanGenPowerControl_Type(Integer32):
    """Custom type fanGenPowerControl based on Integer32"""
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


_FanGenPowerControl_Type.__name__ = "Integer32"
_FanGenPowerControl_Object = MibTableColumn
fanGenPowerControl = _FanGenPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 11, 1, 6),
    _FanGenPowerControl_Type()
)
fanGenPowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanGenPowerControl.setStatus("mandatory")
_SuppBrdGenTable_Object = MibTable
suppBrdGenTable = _SuppBrdGenTable_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 13)
)
if mibBuilder.loadTexts:
    suppBrdGenTable.setStatus("mandatory")
_SuppBrdGenEntry_Object = MibTableRow
suppBrdGenEntry = _SuppBrdGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 13, 1)
)
suppBrdGenEntry.setIndexNames(
    (0, "CRI-SERVER-MIB", "suppBrdGenIndex"),
)
if mibBuilder.loadTexts:
    suppBrdGenEntry.setStatus("mandatory")
_SuppBrdGenIndex_Type = Integer32
_SuppBrdGenIndex_Object = MibTableColumn
suppBrdGenIndex = _SuppBrdGenIndex_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 13, 1, 1),
    _SuppBrdGenIndex_Type()
)
suppBrdGenIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    suppBrdGenIndex.setStatus("mandatory")
_SuppBrdGenNum_Type = Integer32
_SuppBrdGenNum_Object = MibTableColumn
suppBrdGenNum = _SuppBrdGenNum_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 13, 1, 2),
    _SuppBrdGenNum_Type()
)
suppBrdGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    suppBrdGenNum.setStatus("mandatory")


class _SuppBrdGenPower_Type(Integer32):
    """Custom type suppBrdGenPower based on Integer32"""
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


_SuppBrdGenPower_Type.__name__ = "Integer32"
_SuppBrdGenPower_Object = MibTableColumn
suppBrdGenPower = _SuppBrdGenPower_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 13, 1, 3),
    _SuppBrdGenPower_Type()
)
suppBrdGenPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    suppBrdGenPower.setStatus("mandatory")


class _SuppBrdGenPowerControl_Type(Integer32):
    """Custom type suppBrdGenPowerControl based on Integer32"""
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


_SuppBrdGenPowerControl_Type.__name__ = "Integer32"
_SuppBrdGenPowerControl_Object = MibTableColumn
suppBrdGenPowerControl = _SuppBrdGenPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 13, 1, 4),
    _SuppBrdGenPowerControl_Type()
)
suppBrdGenPowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    suppBrdGenPowerControl.setStatus("mandatory")
_BulkPowerGenTable_Object = MibTable
bulkPowerGenTable = _BulkPowerGenTable_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 14)
)
if mibBuilder.loadTexts:
    bulkPowerGenTable.setStatus("mandatory")
_BulkPowerGenEntry_Object = MibTableRow
bulkPowerGenEntry = _BulkPowerGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 14, 1)
)
bulkPowerGenEntry.setIndexNames(
    (0, "CRI-SERVER-MIB", "bulkPowerGenIndex"),
)
if mibBuilder.loadTexts:
    bulkPowerGenEntry.setStatus("mandatory")
_BulkPowerGenIndex_Type = Integer32
_BulkPowerGenIndex_Object = MibTableColumn
bulkPowerGenIndex = _BulkPowerGenIndex_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 14, 1, 1),
    _BulkPowerGenIndex_Type()
)
bulkPowerGenIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bulkPowerGenIndex.setStatus("mandatory")
_BulkPowerGenNum_Type = Integer32
_BulkPowerGenNum_Object = MibTableColumn
bulkPowerGenNum = _BulkPowerGenNum_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 14, 1, 2),
    _BulkPowerGenNum_Type()
)
bulkPowerGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bulkPowerGenNum.setStatus("mandatory")


class _BulkPowerGenControl_Type(Integer32):
    """Custom type bulkPowerGenControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("off", 1)
    )


_BulkPowerGenControl_Type.__name__ = "Integer32"
_BulkPowerGenControl_Object = MibTableColumn
bulkPowerGenControl = _BulkPowerGenControl_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 14, 1, 3),
    _BulkPowerGenControl_Type()
)
bulkPowerGenControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bulkPowerGenControl.setStatus("mandatory")


class _BulkPowerGenStatus_Type(Integer32):
    """Custom type bulkPowerGenStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("ok", 1))
    )


_BulkPowerGenStatus_Type.__name__ = "Integer32"
_BulkPowerGenStatus_Object = MibTableColumn
bulkPowerGenStatus = _BulkPowerGenStatus_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 1, 14, 1, 4),
    _BulkPowerGenStatus_Type()
)
bulkPowerGenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bulkPowerGenStatus.setStatus("mandatory")
_Ue10000_ObjectIdentity = ObjectIdentity
ue10000 = _Ue10000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34, 2, 2)
)
_SysBrdStarfireTable_Object = MibTable
sysBrdStarfireTable = _SysBrdStarfireTable_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 1)
)
if mibBuilder.loadTexts:
    sysBrdStarfireTable.setStatus("mandatory")
_SysBrdStarfireEntry_Object = MibTableRow
sysBrdStarfireEntry = _SysBrdStarfireEntry_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 1, 1)
)
sysBrdStarfireEntry.setIndexNames(
    (0, "CRI-SERVER-MIB", "sysBrdStarfireIndex"),
)
if mibBuilder.loadTexts:
    sysBrdStarfireEntry.setStatus("mandatory")
_SysBrdStarfireIndex_Type = Integer32
_SysBrdStarfireIndex_Object = MibTableColumn
sysBrdStarfireIndex = _SysBrdStarfireIndex_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 1, 1, 1),
    _SysBrdStarfireIndex_Type()
)
sysBrdStarfireIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBrdStarfireIndex.setStatus("mandatory")
_SysBrdStarfireNum_Type = Integer32
_SysBrdStarfireNum_Object = MibTableColumn
sysBrdStarfireNum = _SysBrdStarfireNum_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 1, 1, 2),
    _SysBrdStarfireNum_Type()
)
sysBrdStarfireNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBrdStarfireNum.setStatus("mandatory")
_SysBrdStarfireCIC0Temp_Type = Integer32
_SysBrdStarfireCIC0Temp_Object = MibTableColumn
sysBrdStarfireCIC0Temp = _SysBrdStarfireCIC0Temp_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 1, 1, 3),
    _SysBrdStarfireCIC0Temp_Type()
)
sysBrdStarfireCIC0Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBrdStarfireCIC0Temp.setStatus("mandatory")
_SysBrdStarfireCIC1Temp_Type = Integer32
_SysBrdStarfireCIC1Temp_Object = MibTableColumn
sysBrdStarfireCIC1Temp = _SysBrdStarfireCIC1Temp_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 1, 1, 4),
    _SysBrdStarfireCIC1Temp_Type()
)
sysBrdStarfireCIC1Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBrdStarfireCIC1Temp.setStatus("mandatory")
_SysBrdStarfireMCTemp_Type = Integer32
_SysBrdStarfireMCTemp_Object = MibTableColumn
sysBrdStarfireMCTemp = _SysBrdStarfireMCTemp_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 1, 1, 5),
    _SysBrdStarfireMCTemp_Type()
)
sysBrdStarfireMCTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBrdStarfireMCTemp.setStatus("mandatory")
_SysBrdStarfireXDB2Temp_Type = Integer32
_SysBrdStarfireXDB2Temp_Object = MibTableColumn
sysBrdStarfireXDB2Temp = _SysBrdStarfireXDB2Temp_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 1, 1, 6),
    _SysBrdStarfireXDB2Temp_Type()
)
sysBrdStarfireXDB2Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBrdStarfireXDB2Temp.setStatus("mandatory")
_SysBrdStarfireXDB3Temp_Type = Integer32
_SysBrdStarfireXDB3Temp_Object = MibTableColumn
sysBrdStarfireXDB3Temp = _SysBrdStarfireXDB3Temp_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 1, 1, 7),
    _SysBrdStarfireXDB3Temp_Type()
)
sysBrdStarfireXDB3Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBrdStarfireXDB3Temp.setStatus("mandatory")
_SysBrdStarfirePROC0Temp_Type = Integer32
_SysBrdStarfirePROC0Temp_Object = MibTableColumn
sysBrdStarfirePROC0Temp = _SysBrdStarfirePROC0Temp_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 1, 1, 8),
    _SysBrdStarfirePROC0Temp_Type()
)
sysBrdStarfirePROC0Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBrdStarfirePROC0Temp.setStatus("mandatory")
_SysBrdStarfirePROC1Temp_Type = Integer32
_SysBrdStarfirePROC1Temp_Object = MibTableColumn
sysBrdStarfirePROC1Temp = _SysBrdStarfirePROC1Temp_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 1, 1, 9),
    _SysBrdStarfirePROC1Temp_Type()
)
sysBrdStarfirePROC1Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBrdStarfirePROC1Temp.setStatus("mandatory")
_SysBrdStarfirePROC2Temp_Type = Integer32
_SysBrdStarfirePROC2Temp_Object = MibTableColumn
sysBrdStarfirePROC2Temp = _SysBrdStarfirePROC2Temp_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 1, 1, 10),
    _SysBrdStarfirePROC2Temp_Type()
)
sysBrdStarfirePROC2Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBrdStarfirePROC2Temp.setStatus("mandatory")
_SysBrdStarfirePROC3Temp_Type = Integer32
_SysBrdStarfirePROC3Temp_Object = MibTableColumn
sysBrdStarfirePROC3Temp = _SysBrdStarfirePROC3Temp_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 1, 1, 11),
    _SysBrdStarfirePROC3Temp_Type()
)
sysBrdStarfirePROC3Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBrdStarfirePROC3Temp.setStatus("mandatory")
_SysBrdStarfire3p3VDCTemp_Type = Integer32
_SysBrdStarfire3p3VDCTemp_Object = MibTableColumn
sysBrdStarfire3p3VDCTemp = _SysBrdStarfire3p3VDCTemp_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 1, 1, 12),
    _SysBrdStarfire3p3VDCTemp_Type()
)
sysBrdStarfire3p3VDCTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBrdStarfire3p3VDCTemp.setStatus("mandatory")
_SysBrdStarfireVDCCoreTemp_Type = Integer32
_SysBrdStarfireVDCCoreTemp_Object = MibTableColumn
sysBrdStarfireVDCCoreTemp = _SysBrdStarfireVDCCoreTemp_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 1, 1, 13),
    _SysBrdStarfireVDCCoreTemp_Type()
)
sysBrdStarfireVDCCoreTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBrdStarfireVDCCoreTemp.setStatus("mandatory")
_SysBrdStarfire5VDCTemp_Type = Integer32
_SysBrdStarfire5VDCTemp_Object = MibTableColumn
sysBrdStarfire5VDCTemp = _SysBrdStarfire5VDCTemp_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 1, 1, 14),
    _SysBrdStarfire5VDCTemp_Type()
)
sysBrdStarfire5VDCTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBrdStarfire5VDCTemp.setStatus("mandatory")
_SysBrdStarfire3p3VDC_Type = Integer32
_SysBrdStarfire3p3VDC_Object = MibTableColumn
sysBrdStarfire3p3VDC = _SysBrdStarfire3p3VDC_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 1, 1, 15),
    _SysBrdStarfire3p3VDC_Type()
)
sysBrdStarfire3p3VDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBrdStarfire3p3VDC.setStatus("mandatory")
_SysBrdStarfire5VDCHK_Type = Integer32
_SysBrdStarfire5VDCHK_Object = MibTableColumn
sysBrdStarfire5VDCHK = _SysBrdStarfire5VDCHK_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 1, 1, 16),
    _SysBrdStarfire5VDCHK_Type()
)
sysBrdStarfire5VDCHK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBrdStarfire5VDCHK.setStatus("mandatory")
_SysBrdStarfire5VDC_Type = Integer32
_SysBrdStarfire5VDC_Object = MibTableColumn
sysBrdStarfire5VDC = _SysBrdStarfire5VDC_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 1, 1, 17),
    _SysBrdStarfire5VDC_Type()
)
sysBrdStarfire5VDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBrdStarfire5VDC.setStatus("mandatory")
_SysBrdStarfireVDCCore_Type = Integer32
_SysBrdStarfireVDCCore_Object = MibTableColumn
sysBrdStarfireVDCCore = _SysBrdStarfireVDCCore_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 1, 1, 18),
    _SysBrdStarfireVDCCore_Type()
)
sysBrdStarfireVDCCore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBrdStarfireVDCCore.setStatus("mandatory")
_SysBrdStarfire3p3VDCHK_Type = Integer32
_SysBrdStarfire3p3VDCHK_Object = MibTableColumn
sysBrdStarfire3p3VDCHK = _SysBrdStarfire3p3VDCHK_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 1, 1, 19),
    _SysBrdStarfire3p3VDCHK_Type()
)
sysBrdStarfire3p3VDCHK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBrdStarfire3p3VDCHK.setStatus("mandatory")
_CbStarfireTable_Object = MibTable
cbStarfireTable = _CbStarfireTable_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 2)
)
if mibBuilder.loadTexts:
    cbStarfireTable.setStatus("mandatory")
_CbStarfireEntry_Object = MibTableRow
cbStarfireEntry = _CbStarfireEntry_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 2, 1)
)
cbStarfireEntry.setIndexNames(
    (0, "CRI-SERVER-MIB", "cbStarfireIndex"),
)
if mibBuilder.loadTexts:
    cbStarfireEntry.setStatus("mandatory")
_CbStarfireIndex_Type = Integer32
_CbStarfireIndex_Object = MibTableColumn
cbStarfireIndex = _CbStarfireIndex_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 2, 1, 1),
    _CbStarfireIndex_Type()
)
cbStarfireIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbStarfireIndex.setStatus("mandatory")
_CbStarfireNum_Type = Integer32
_CbStarfireNum_Object = MibTableColumn
cbStarfireNum = _CbStarfireNum_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 2, 1, 2),
    _CbStarfireNum_Type()
)
cbStarfireNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbStarfireNum.setStatus("mandatory")
_CbStarfireHostName_Type = DisplayString
_CbStarfireHostName_Object = MibTableColumn
cbStarfireHostName = _CbStarfireHostName_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 2, 1, 3),
    _CbStarfireHostName_Type()
)
cbStarfireHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbStarfireHostName.setStatus("mandatory")
_CbStarfire5VDCTemp_Type = Integer32
_CbStarfire5VDCTemp_Object = MibTableColumn
cbStarfire5VDCTemp = _CbStarfire5VDCTemp_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 2, 1, 4),
    _CbStarfire5VDCTemp_Type()
)
cbStarfire5VDCTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbStarfire5VDCTemp.setStatus("mandatory")
_CbStarfire5VDCPerTemp_Type = Integer32
_CbStarfire5VDCPerTemp_Object = MibTableColumn
cbStarfire5VDCPerTemp = _CbStarfire5VDCPerTemp_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 2, 1, 5),
    _CbStarfire5VDCPerTemp_Type()
)
cbStarfire5VDCPerTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbStarfire5VDCPerTemp.setStatus("mandatory")
_CbStarfire5VDCFanTemp_Type = Integer32
_CbStarfire5VDCFanTemp_Object = MibTableColumn
cbStarfire5VDCFanTemp = _CbStarfire5VDCFanTemp_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 2, 1, 6),
    _CbStarfire5VDCFanTemp_Type()
)
cbStarfire5VDCFanTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbStarfire5VDCFanTemp.setStatus("mandatory")
_CbStarfireSen0Temp_Type = Integer32
_CbStarfireSen0Temp_Object = MibTableColumn
cbStarfireSen0Temp = _CbStarfireSen0Temp_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 2, 1, 7),
    _CbStarfireSen0Temp_Type()
)
cbStarfireSen0Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbStarfireSen0Temp.setStatus("mandatory")
_CbStarfireSen1Temp_Type = Integer32
_CbStarfireSen1Temp_Object = MibTableColumn
cbStarfireSen1Temp = _CbStarfireSen1Temp_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 2, 1, 8),
    _CbStarfireSen1Temp_Type()
)
cbStarfireSen1Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbStarfireSen1Temp.setStatus("mandatory")
_CbStarfireSen2Temp_Type = Integer32
_CbStarfireSen2Temp_Object = MibTableColumn
cbStarfireSen2Temp = _CbStarfireSen2Temp_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 2, 1, 9),
    _CbStarfireSen2Temp_Type()
)
cbStarfireSen2Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbStarfireSen2Temp.setStatus("mandatory")
_CbStarfire5VDC_Type = Integer32
_CbStarfire5VDC_Object = MibTableColumn
cbStarfire5VDC = _CbStarfire5VDC_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 2, 1, 10),
    _CbStarfire5VDC_Type()
)
cbStarfire5VDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbStarfire5VDC.setStatus("mandatory")
_CbStarfire5VDCHK_Type = Integer32
_CbStarfire5VDCHK_Object = MibTableColumn
cbStarfire5VDCHK = _CbStarfire5VDCHK_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 2, 1, 11),
    _CbStarfire5VDCHK_Type()
)
cbStarfire5VDCHK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbStarfire5VDCHK.setStatus("mandatory")
_CbStarfire3p3VDCHK_Type = Integer32
_CbStarfire3p3VDCHK_Object = MibTableColumn
cbStarfire3p3VDCHK = _CbStarfire3p3VDCHK_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 2, 1, 12),
    _CbStarfire3p3VDCHK_Type()
)
cbStarfire3p3VDCHK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbStarfire3p3VDCHK.setStatus("mandatory")
_CbStarfire5VDCPer_Type = Integer32
_CbStarfire5VDCPer_Object = MibTableColumn
cbStarfire5VDCPer = _CbStarfire5VDCPer_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 2, 1, 13),
    _CbStarfire5VDCPer_Type()
)
cbStarfire5VDCPer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbStarfire5VDCPer.setStatus("mandatory")
_CbStarfire5VDCFan_Type = Integer32
_CbStarfire5VDCFan_Object = MibTableColumn
cbStarfire5VDCFan = _CbStarfire5VDCFan_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 2, 1, 14),
    _CbStarfire5VDCFan_Type()
)
cbStarfire5VDCFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbStarfire5VDCFan.setStatus("mandatory")
_CenterplaneStarfireTable_Object = MibTable
centerplaneStarfireTable = _CenterplaneStarfireTable_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 3)
)
if mibBuilder.loadTexts:
    centerplaneStarfireTable.setStatus("mandatory")
_CenterplaneStarfireEntry_Object = MibTableRow
centerplaneStarfireEntry = _CenterplaneStarfireEntry_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 3, 1)
)
centerplaneStarfireEntry.setIndexNames(
    (0, "CRI-SERVER-MIB", "centerplaneStarfireIndex"),
)
if mibBuilder.loadTexts:
    centerplaneStarfireEntry.setStatus("mandatory")
_CenterplaneStarfireIndex_Type = Integer32
_CenterplaneStarfireIndex_Object = MibTableColumn
centerplaneStarfireIndex = _CenterplaneStarfireIndex_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 3, 1, 1),
    _CenterplaneStarfireIndex_Type()
)
centerplaneStarfireIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    centerplaneStarfireIndex.setStatus("mandatory")
_CenterplaneStarfireNum_Type = Integer32
_CenterplaneStarfireNum_Object = MibTableColumn
centerplaneStarfireNum = _CenterplaneStarfireNum_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 3, 1, 2),
    _CenterplaneStarfireNum_Type()
)
centerplaneStarfireNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    centerplaneStarfireNum.setStatus("mandatory")
_CenterplaneStarfireTemp0_Type = Integer32
_CenterplaneStarfireTemp0_Object = MibTableColumn
centerplaneStarfireTemp0 = _CenterplaneStarfireTemp0_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 3, 1, 3),
    _CenterplaneStarfireTemp0_Type()
)
centerplaneStarfireTemp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    centerplaneStarfireTemp0.setStatus("mandatory")
_CenterplaneStarfireTemp1_Type = Integer32
_CenterplaneStarfireTemp1_Object = MibTableColumn
centerplaneStarfireTemp1 = _CenterplaneStarfireTemp1_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 3, 1, 4),
    _CenterplaneStarfireTemp1_Type()
)
centerplaneStarfireTemp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    centerplaneStarfireTemp1.setStatus("mandatory")
_CenterplaneStarfireTemp2_Type = Integer32
_CenterplaneStarfireTemp2_Object = MibTableColumn
centerplaneStarfireTemp2 = _CenterplaneStarfireTemp2_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 3, 1, 5),
    _CenterplaneStarfireTemp2_Type()
)
centerplaneStarfireTemp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    centerplaneStarfireTemp2.setStatus("mandatory")
_CenterplaneStarfireTemp3_Type = Integer32
_CenterplaneStarfireTemp3_Object = MibTableColumn
centerplaneStarfireTemp3 = _CenterplaneStarfireTemp3_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 3, 1, 6),
    _CenterplaneStarfireTemp3_Type()
)
centerplaneStarfireTemp3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    centerplaneStarfireTemp3.setStatus("mandatory")
_CenterplaneStarfireTemp4_Type = Integer32
_CenterplaneStarfireTemp4_Object = MibTableColumn
centerplaneStarfireTemp4 = _CenterplaneStarfireTemp4_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 3, 1, 7),
    _CenterplaneStarfireTemp4_Type()
)
centerplaneStarfireTemp4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    centerplaneStarfireTemp4.setStatus("mandatory")
_CenterplaneStarfireTemp5_Type = Integer32
_CenterplaneStarfireTemp5_Object = MibTableColumn
centerplaneStarfireTemp5 = _CenterplaneStarfireTemp5_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 3, 1, 8),
    _CenterplaneStarfireTemp5_Type()
)
centerplaneStarfireTemp5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    centerplaneStarfireTemp5.setStatus("mandatory")
_CenterplaneStarfireTemp6_Type = Integer32
_CenterplaneStarfireTemp6_Object = MibTableColumn
centerplaneStarfireTemp6 = _CenterplaneStarfireTemp6_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 3, 1, 9),
    _CenterplaneStarfireTemp6_Type()
)
centerplaneStarfireTemp6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    centerplaneStarfireTemp6.setStatus("mandatory")
_CenterplaneStarfireTemp7_Type = Integer32
_CenterplaneStarfireTemp7_Object = MibTableColumn
centerplaneStarfireTemp7 = _CenterplaneStarfireTemp7_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 3, 1, 10),
    _CenterplaneStarfireTemp7_Type()
)
centerplaneStarfireTemp7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    centerplaneStarfireTemp7.setStatus("mandatory")
_CenterplaneStarfireTemp8_Type = Integer32
_CenterplaneStarfireTemp8_Object = MibTableColumn
centerplaneStarfireTemp8 = _CenterplaneStarfireTemp8_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 3, 1, 11),
    _CenterplaneStarfireTemp8_Type()
)
centerplaneStarfireTemp8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    centerplaneStarfireTemp8.setStatus("mandatory")
_CenterplaneStarfireTemp9_Type = Integer32
_CenterplaneStarfireTemp9_Object = MibTableColumn
centerplaneStarfireTemp9 = _CenterplaneStarfireTemp9_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 3, 1, 12),
    _CenterplaneStarfireTemp9_Type()
)
centerplaneStarfireTemp9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    centerplaneStarfireTemp9.setStatus("mandatory")
_SuppBrdStarfireTable_Object = MibTable
suppBrdStarfireTable = _SuppBrdStarfireTable_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 4)
)
if mibBuilder.loadTexts:
    suppBrdStarfireTable.setStatus("mandatory")
_SuppBrdStarfireEntry_Object = MibTableRow
suppBrdStarfireEntry = _SuppBrdStarfireEntry_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 4, 1)
)
suppBrdStarfireEntry.setIndexNames(
    (0, "CRI-SERVER-MIB", "suppBrdStarfireIndex"),
)
if mibBuilder.loadTexts:
    suppBrdStarfireEntry.setStatus("mandatory")
_SuppBrdStarfireIndex_Type = Integer32
_SuppBrdStarfireIndex_Object = MibTableColumn
suppBrdStarfireIndex = _SuppBrdStarfireIndex_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 4, 1, 1),
    _SuppBrdStarfireIndex_Type()
)
suppBrdStarfireIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    suppBrdStarfireIndex.setStatus("mandatory")
_SuppBrdStarfireNum_Type = Integer32
_SuppBrdStarfireNum_Object = MibTableColumn
suppBrdStarfireNum = _SuppBrdStarfireNum_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 4, 1, 2),
    _SuppBrdStarfireNum_Type()
)
suppBrdStarfireNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    suppBrdStarfireNum.setStatus("mandatory")
_SuppBrdStarfire3p3VDC1Temp_Type = Integer32
_SuppBrdStarfire3p3VDC1Temp_Object = MibTableColumn
suppBrdStarfire3p3VDC1Temp = _SuppBrdStarfire3p3VDC1Temp_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 4, 1, 3),
    _SuppBrdStarfire3p3VDC1Temp_Type()
)
suppBrdStarfire3p3VDC1Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    suppBrdStarfire3p3VDC1Temp.setStatus("mandatory")
_SuppBrdStarfire3p3VDC2Temp_Type = Integer32
_SuppBrdStarfire3p3VDC2Temp_Object = MibTableColumn
suppBrdStarfire3p3VDC2Temp = _SuppBrdStarfire3p3VDC2Temp_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 4, 1, 4),
    _SuppBrdStarfire3p3VDC2Temp_Type()
)
suppBrdStarfire3p3VDC2Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    suppBrdStarfire3p3VDC2Temp.setStatus("mandatory")
_SuppBrdStarfire5VDCHK_Type = Integer32
_SuppBrdStarfire5VDCHK_Object = MibTableColumn
suppBrdStarfire5VDCHK = _SuppBrdStarfire5VDCHK_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 4, 1, 5),
    _SuppBrdStarfire5VDCHK_Type()
)
suppBrdStarfire5VDCHK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    suppBrdStarfire5VDCHK.setStatus("mandatory")
_SuppBrdStarfire3p3VDCHK_Type = Integer32
_SuppBrdStarfire3p3VDCHK_Object = MibTableColumn
suppBrdStarfire3p3VDCHK = _SuppBrdStarfire3p3VDCHK_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 4, 1, 6),
    _SuppBrdStarfire3p3VDCHK_Type()
)
suppBrdStarfire3p3VDCHK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    suppBrdStarfire3p3VDCHK.setStatus("mandatory")
_SuppBrdStarfire3p3VDC_Type = Integer32
_SuppBrdStarfire3p3VDC_Object = MibTableColumn
suppBrdStarfire3p3VDC = _SuppBrdStarfire3p3VDC_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 2, 4, 1, 7),
    _SuppBrdStarfire3p3VDC_Type()
)
suppBrdStarfire3p3VDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    suppBrdStarfire3p3VDC.setStatus("mandatory")
_Ssp_ObjectIdentity = ObjectIdentity
ssp = _Ssp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34, 2, 3)
)
_SspPlatformApp_ObjectIdentity = ObjectIdentity
sspPlatformApp = _SspPlatformApp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34, 2, 3, 1)
)


class _SspPlatformAppEddControl_Type(Integer32):
    """Custom type sspPlatformAppEddControl based on Integer32"""
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
        *(("reconfig", 3),
          ("start", 1),
          ("stop", 2),
          ("unknown", 4))
    )


_SspPlatformAppEddControl_Type.__name__ = "Integer32"
_SspPlatformAppEddControl_Object = MibScalar
sspPlatformAppEddControl = _SspPlatformAppEddControl_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 3, 1, 1),
    _SspPlatformAppEddControl_Type()
)
sspPlatformAppEddControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sspPlatformAppEddControl.setStatus("mandatory")


class _SspPlatformAppEddState_Type(Integer32):
    """Custom type sspPlatformAppEddState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("started-monitoring", 1),
          ("stopped-monitoring", 2),
          ("unknown", 3))
    )


_SspPlatformAppEddState_Type.__name__ = "Integer32"
_SspPlatformAppEddState_Object = MibScalar
sspPlatformAppEddState = _SspPlatformAppEddState_Object(
    (1, 3, 6, 1, 4, 1, 34, 2, 3, 1, 2),
    _SspPlatformAppEddState_Type()
)
sspPlatformAppEddState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sspPlatformAppEddState.setStatus("mandatory")

# Managed Objects groups


# Notification objects

domainChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 0)
)
domainChange.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "confNumDomain"),
        ("CRI-SERVER-MIB", "domainName"),
        ("CRI-SERVER-MIB", "domainNumSysBrd"),
        ("CRI-SERVER-MIB", "domainSysBrdList"),
        ("CRI-SERVER-MIB", "domainOSVersion"),
        ("CRI-SERVER-MIB", "platformType"),
        ("CRI-SERVER-MIB", "platformName"))
)
if mibBuilder.loadTexts:
    domainChange.setStatus(
        ""
    )

eddControl = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 1)
)
eddControl.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "sspPlatformAppEddControl"))
)
if mibBuilder.loadTexts:
    eddControl.setStatus(
        ""
    )

eddState = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 2)
)
eddState.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "sspPlatformAppEddState"))
)
if mibBuilder.loadTexts:
    eddState.setStatus(
        ""
    )

sysBrdTempNorm = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 3)
)
sysBrdTempNorm.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "sysBrdStarfireNum"),
        ("CRI-SERVER-MIB", "sysBrdStarfireCIC0Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfireCIC1Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfireMCTemp"),
        ("CRI-SERVER-MIB", "sysBrdStarfireXDB2Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfireXDB3Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfirePROC0Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfirePROC1Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfirePROC2Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfirePROC3Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfire3p3VDCTemp"),
        ("CRI-SERVER-MIB", "sysBrdStarfireVDCCoreTemp"),
        ("CRI-SERVER-MIB", "sysBrdStarfire5VDCTemp"))
)
if mibBuilder.loadTexts:
    sysBrdTempNorm.setStatus(
        ""
    )

sysBrdTempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 4)
)
sysBrdTempHigh.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "sysBrdStarfireNum"),
        ("CRI-SERVER-MIB", "sysBrdStarfireCIC0Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfireCIC1Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfireMCTemp"),
        ("CRI-SERVER-MIB", "sysBrdStarfireXDB2Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfireXDB3Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfirePROC0Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfirePROC1Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfirePROC2Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfirePROC3Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfire3p3VDCTemp"),
        ("CRI-SERVER-MIB", "sysBrdStarfireVDCCoreTemp"),
        ("CRI-SERVER-MIB", "sysBrdStarfire5VDCTemp"))
)
if mibBuilder.loadTexts:
    sysBrdTempHigh.setStatus(
        ""
    )

sysBrdTempWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 5)
)
sysBrdTempWarn.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "sysBrdStarfireNum"),
        ("CRI-SERVER-MIB", "sysBrdStarfireCIC0Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfireCIC1Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfireMCTemp"),
        ("CRI-SERVER-MIB", "sysBrdStarfireXDB2Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfireXDB3Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfirePROC0Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfirePROC1Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfirePROC2Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfirePROC3Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfire3p3VDCTemp"),
        ("CRI-SERVER-MIB", "sysBrdStarfireVDCCoreTemp"),
        ("CRI-SERVER-MIB", "sysBrdStarfire5VDCTemp"))
)
if mibBuilder.loadTexts:
    sysBrdTempWarn.setStatus(
        ""
    )

sysBrdTempMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 6)
)
sysBrdTempMax.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "sysBrdStarfireNum"),
        ("CRI-SERVER-MIB", "sysBrdStarfireCIC0Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfireCIC1Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfireMCTemp"),
        ("CRI-SERVER-MIB", "sysBrdStarfireXDB2Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfireXDB3Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfirePROC0Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfirePROC1Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfirePROC2Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfirePROC3Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfire3p3VDCTemp"),
        ("CRI-SERVER-MIB", "sysBrdStarfireVDCCoreTemp"),
        ("CRI-SERVER-MIB", "sysBrdStarfire5VDCTemp"))
)
if mibBuilder.loadTexts:
    sysBrdTempMax.setStatus(
        ""
    )

sysBrdTemp911 = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 7)
)
sysBrdTemp911.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "sysBrdStarfireNum"),
        ("CRI-SERVER-MIB", "sysBrdStarfireCIC0Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfireCIC1Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfireMCTemp"),
        ("CRI-SERVER-MIB", "sysBrdStarfireXDB2Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfireXDB3Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfirePROC0Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfirePROC1Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfirePROC2Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfirePROC3Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfire3p3VDCTemp"),
        ("CRI-SERVER-MIB", "sysBrdStarfireVDCCoreTemp"),
        ("CRI-SERVER-MIB", "sysBrdStarfire5VDCTemp"))
)
if mibBuilder.loadTexts:
    sysBrdTemp911.setStatus(
        ""
    )

sysBrdTempBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 8)
)
sysBrdTempBad.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "sysBrdStarfireNum"),
        ("CRI-SERVER-MIB", "sysBrdStarfireCIC0Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfireCIC1Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfireMCTemp"),
        ("CRI-SERVER-MIB", "sysBrdStarfireXDB2Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfireXDB3Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfirePROC0Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfirePROC1Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfirePROC2Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfirePROC3Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfire3p3VDCTemp"),
        ("CRI-SERVER-MIB", "sysBrdStarfireVDCCoreTemp"),
        ("CRI-SERVER-MIB", "sysBrdStarfire5VDCTemp"))
)
if mibBuilder.loadTexts:
    sysBrdTempBad.setStatus(
        ""
    )

sysBrdTempChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 9)
)
sysBrdTempChange.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "sysBrdStarfireNum"),
        ("CRI-SERVER-MIB", "sysBrdStarfireCIC0Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfireCIC1Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfireMCTemp"),
        ("CRI-SERVER-MIB", "sysBrdStarfireXDB2Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfireXDB3Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfirePROC0Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfirePROC1Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfirePROC2Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfirePROC3Temp"),
        ("CRI-SERVER-MIB", "sysBrdStarfire3p3VDCTemp"),
        ("CRI-SERVER-MIB", "sysBrdStarfireVDCCoreTemp"),
        ("CRI-SERVER-MIB", "sysBrdStarfire5VDCTemp"))
)
if mibBuilder.loadTexts:
    sysBrdTempChange.setStatus(
        ""
    )

cbTempNorm = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 10)
)
cbTempNorm.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "cbStarfireNum"),
        ("CRI-SERVER-MIB", "cbStarfire5VDCTemp"),
        ("CRI-SERVER-MIB", "cbStarfire5VDCPerTemp"),
        ("CRI-SERVER-MIB", "cbStarfire5VDCFanTemp"),
        ("CRI-SERVER-MIB", "cbStarfireSen0Temp"),
        ("CRI-SERVER-MIB", "cbStarfireSen1Temp"),
        ("CRI-SERVER-MIB", "cbStarfireSen2Temp"))
)
if mibBuilder.loadTexts:
    cbTempNorm.setStatus(
        ""
    )

cbTempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 11)
)
cbTempHigh.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "cbStarfireNum"),
        ("CRI-SERVER-MIB", "cbStarfire5VDCTemp"),
        ("CRI-SERVER-MIB", "cbStarfire5VDCPerTemp"),
        ("CRI-SERVER-MIB", "cbStarfire5VDCFanTemp"),
        ("CRI-SERVER-MIB", "cbStarfireSen0Temp"),
        ("CRI-SERVER-MIB", "cbStarfireSen1Temp"),
        ("CRI-SERVER-MIB", "cbStarfireSen2Temp"))
)
if mibBuilder.loadTexts:
    cbTempHigh.setStatus(
        ""
    )

cbTempWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 12)
)
cbTempWarn.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "cbStarfireNum"),
        ("CRI-SERVER-MIB", "cbStarfire5VDCTemp"),
        ("CRI-SERVER-MIB", "cbStarfire5VDCPerTemp"),
        ("CRI-SERVER-MIB", "cbStarfire5VDCFanTemp"),
        ("CRI-SERVER-MIB", "cbStarfireSen0Temp"),
        ("CRI-SERVER-MIB", "cbStarfireSen1Temp"),
        ("CRI-SERVER-MIB", "cbStarfireSen2Temp"))
)
if mibBuilder.loadTexts:
    cbTempWarn.setStatus(
        ""
    )

cbTempMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 13)
)
cbTempMax.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "cbStarfireNum"),
        ("CRI-SERVER-MIB", "cbStarfire5VDCTemp"),
        ("CRI-SERVER-MIB", "cbStarfire5VDCPerTemp"),
        ("CRI-SERVER-MIB", "cbStarfire5VDCFanTemp"),
        ("CRI-SERVER-MIB", "cbStarfireSen0Temp"),
        ("CRI-SERVER-MIB", "cbStarfireSen1Temp"),
        ("CRI-SERVER-MIB", "cbStarfireSen2Temp"))
)
if mibBuilder.loadTexts:
    cbTempMax.setStatus(
        ""
    )

cbTemp911 = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 14)
)
cbTemp911.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "cbStarfireNum"),
        ("CRI-SERVER-MIB", "cbStarfire5VDCTemp"),
        ("CRI-SERVER-MIB", "cbStarfire5VDCPerTemp"),
        ("CRI-SERVER-MIB", "cbStarfire5VDCFanTemp"),
        ("CRI-SERVER-MIB", "cbStarfireSen0Temp"),
        ("CRI-SERVER-MIB", "cbStarfireSen1Temp"),
        ("CRI-SERVER-MIB", "cbStarfireSen2Temp"))
)
if mibBuilder.loadTexts:
    cbTemp911.setStatus(
        ""
    )

cbTempBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 15)
)
cbTempBad.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "cbStarfireNum"),
        ("CRI-SERVER-MIB", "cbStarfire5VDCTemp"),
        ("CRI-SERVER-MIB", "cbStarfire5VDCPerTemp"),
        ("CRI-SERVER-MIB", "cbStarfire5VDCFanTemp"),
        ("CRI-SERVER-MIB", "cbStarfireSen0Temp"),
        ("CRI-SERVER-MIB", "cbStarfireSen1Temp"),
        ("CRI-SERVER-MIB", "cbStarfireSen2Temp"))
)
if mibBuilder.loadTexts:
    cbTempBad.setStatus(
        ""
    )

cbTempChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 16)
)
cbTempChange.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "cbStarfireNum"),
        ("CRI-SERVER-MIB", "cbStarfire5VDCTemp"),
        ("CRI-SERVER-MIB", "cbStarfire5VDCPerTemp"),
        ("CRI-SERVER-MIB", "cbStarfire5VDCFanTemp"),
        ("CRI-SERVER-MIB", "cbStarfireSen0Temp"),
        ("CRI-SERVER-MIB", "cbStarfireSen1Temp"),
        ("CRI-SERVER-MIB", "cbStarfireSen2Temp"))
)
if mibBuilder.loadTexts:
    cbTempChange.setStatus(
        ""
    )

centerplaneTempNorm = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 17)
)
centerplaneTempNorm.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "centerplaneStarfireNum"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp0"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp1"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp2"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp3"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp4"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp5"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp6"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp7"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp8"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp9"))
)
if mibBuilder.loadTexts:
    centerplaneTempNorm.setStatus(
        ""
    )

centerplaneTempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 18)
)
centerplaneTempHigh.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "centerplaneStarfireNum"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp0"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp1"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp2"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp3"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp4"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp5"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp6"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp7"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp8"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp9"))
)
if mibBuilder.loadTexts:
    centerplaneTempHigh.setStatus(
        ""
    )

centerplaneTempWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 19)
)
centerplaneTempWarn.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "centerplaneStarfireNum"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp0"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp1"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp2"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp3"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp4"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp5"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp6"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp7"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp8"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp9"))
)
if mibBuilder.loadTexts:
    centerplaneTempWarn.setStatus(
        ""
    )

centerplaneTempMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 20)
)
centerplaneTempMax.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "centerplaneStarfireNum"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp0"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp1"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp2"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp3"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp4"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp5"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp6"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp7"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp8"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp9"))
)
if mibBuilder.loadTexts:
    centerplaneTempMax.setStatus(
        ""
    )

centerplaneTemp911 = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 21)
)
centerplaneTemp911.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "centerplaneStarfireNum"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp0"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp1"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp2"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp3"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp4"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp5"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp6"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp7"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp8"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp9"))
)
if mibBuilder.loadTexts:
    centerplaneTemp911.setStatus(
        ""
    )

centerplaneTempBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 22)
)
centerplaneTempBad.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "centerplaneStarfireNum"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp0"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp1"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp2"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp3"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp4"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp5"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp6"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp7"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp8"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp9"))
)
if mibBuilder.loadTexts:
    centerplaneTempBad.setStatus(
        ""
    )

centerplaneTempChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 23)
)
centerplaneTempChange.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "centerplaneStarfireNum"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp0"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp1"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp2"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp3"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp4"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp5"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp6"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp7"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp8"),
        ("CRI-SERVER-MIB", "centerplaneStarfireTemp9"))
)
if mibBuilder.loadTexts:
    centerplaneTempChange.setStatus(
        ""
    )

cbeConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 24)
)
cbeConnected.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "platformMasterConBrd"),
        ("CRI-SERVER-MIB", "platformSysClkConBrd"))
)
if mibBuilder.loadTexts:
    cbeConnected.setStatus(
        ""
    )

cbeDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 25)
)
cbeDisconnected.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "platformMasterConBrd"),
        ("CRI-SERVER-MIB", "platformSysClkConBrd"))
)
if mibBuilder.loadTexts:
    cbeDisconnected.setStatus(
        ""
    )

suppBrdTempNorm = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 26)
)
suppBrdTempNorm.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "suppBrdStarfireNum"),
        ("CRI-SERVER-MIB", "suppBrdStarfire3p3VDC1Temp"),
        ("CRI-SERVER-MIB", "suppBrdStarfire3p3VDC2Temp"))
)
if mibBuilder.loadTexts:
    suppBrdTempNorm.setStatus(
        ""
    )

suppBrdTempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 27)
)
suppBrdTempHigh.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "suppBrdStarfireNum"),
        ("CRI-SERVER-MIB", "suppBrdStarfire3p3VDC1Temp"),
        ("CRI-SERVER-MIB", "suppBrdStarfire3p3VDC2Temp"))
)
if mibBuilder.loadTexts:
    suppBrdTempHigh.setStatus(
        ""
    )

suppBrdTempWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 28)
)
suppBrdTempWarn.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "suppBrdStarfireNum"),
        ("CRI-SERVER-MIB", "suppBrdStarfire3p3VDC1Temp"),
        ("CRI-SERVER-MIB", "suppBrdStarfire3p3VDC2Temp"))
)
if mibBuilder.loadTexts:
    suppBrdTempWarn.setStatus(
        ""
    )

suppBrdTempMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 29)
)
suppBrdTempMax.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "suppBrdStarfireNum"),
        ("CRI-SERVER-MIB", "suppBrdStarfire3p3VDC1Temp"),
        ("CRI-SERVER-MIB", "suppBrdStarfire3p3VDC2Temp"))
)
if mibBuilder.loadTexts:
    suppBrdTempMax.setStatus(
        ""
    )

suppBrdTemp911 = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 30)
)
suppBrdTemp911.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "suppBrdStarfireNum"),
        ("CRI-SERVER-MIB", "suppBrdStarfire3p3VDC1Temp"),
        ("CRI-SERVER-MIB", "suppBrdStarfire3p3VDC2Temp"))
)
if mibBuilder.loadTexts:
    suppBrdTemp911.setStatus(
        ""
    )

suppBrdTempBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 31)
)
suppBrdTempBad.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "suppBrdStarfireNum"),
        ("CRI-SERVER-MIB", "suppBrdStarfire3p3VDC1Temp"),
        ("CRI-SERVER-MIB", "suppBrdStarfire3p3VDC2Temp"))
)
if mibBuilder.loadTexts:
    suppBrdTempBad.setStatus(
        ""
    )

suppBrdTempChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 32)
)
suppBrdTempChange.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "suppBrdStarfireNum"),
        ("CRI-SERVER-MIB", "suppBrdStarfire3p3VDC1Temp"),
        ("CRI-SERVER-MIB", "suppBrdStarfire3p3VDC2Temp"))
)
if mibBuilder.loadTexts:
    suppBrdTempChange.setStatus(
        ""
    )

sysBrdVoltNorm = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 33)
)
sysBrdVoltNorm.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "sysBrdStarfireNum"),
        ("CRI-SERVER-MIB", "sysBrdStarfire3p3VDC"),
        ("CRI-SERVER-MIB", "sysBrdStarfire5VDCHK"),
        ("CRI-SERVER-MIB", "sysBrdStarfire5VDC"),
        ("CRI-SERVER-MIB", "sysBrdStarfireVDCCore"),
        ("CRI-SERVER-MIB", "sysBrdStarfire3p3VDCHK"))
)
if mibBuilder.loadTexts:
    sysBrdVoltNorm.setStatus(
        ""
    )

sysBrdVoltMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 34)
)
sysBrdVoltMax.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "sysBrdStarfireNum"),
        ("CRI-SERVER-MIB", "sysBrdStarfire3p3VDC"),
        ("CRI-SERVER-MIB", "sysBrdStarfire5VDCHK"),
        ("CRI-SERVER-MIB", "sysBrdStarfire5VDC"),
        ("CRI-SERVER-MIB", "sysBrdStarfireVDCCore"),
        ("CRI-SERVER-MIB", "sysBrdStarfire3p3VDCHK"))
)
if mibBuilder.loadTexts:
    sysBrdVoltMax.setStatus(
        ""
    )

sysBrdVoltMin = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 35)
)
sysBrdVoltMin.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "sysBrdStarfireNum"),
        ("CRI-SERVER-MIB", "sysBrdStarfire3p3VDC"),
        ("CRI-SERVER-MIB", "sysBrdStarfire5VDCHK"),
        ("CRI-SERVER-MIB", "sysBrdStarfire5VDC"),
        ("CRI-SERVER-MIB", "sysBrdStarfireVDCCore"),
        ("CRI-SERVER-MIB", "sysBrdStarfire3p3VDCHK"))
)
if mibBuilder.loadTexts:
    sysBrdVoltMin.setStatus(
        ""
    )

sysBrdVoltBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 36)
)
sysBrdVoltBad.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "sysBrdStarfireNum"),
        ("CRI-SERVER-MIB", "sysBrdStarfire3p3VDC"),
        ("CRI-SERVER-MIB", "sysBrdStarfire5VDCHK"),
        ("CRI-SERVER-MIB", "sysBrdStarfire5VDC"),
        ("CRI-SERVER-MIB", "sysBrdStarfireVDCCore"),
        ("CRI-SERVER-MIB", "sysBrdStarfire3p3VDCHK"))
)
if mibBuilder.loadTexts:
    sysBrdVoltBad.setStatus(
        ""
    )

sysBrdVoltChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 37)
)
sysBrdVoltChange.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "sysBrdStarfireNum"),
        ("CRI-SERVER-MIB", "sysBrdStarfire3p3VDC"),
        ("CRI-SERVER-MIB", "sysBrdStarfire5VDCHK"),
        ("CRI-SERVER-MIB", "sysBrdStarfire5VDC"),
        ("CRI-SERVER-MIB", "sysBrdStarfireVDCCore"),
        ("CRI-SERVER-MIB", "sysBrdStarfire3p3VDCHK"))
)
if mibBuilder.loadTexts:
    sysBrdVoltChange.setStatus(
        ""
    )

cbVoltNorm = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 38)
)
cbVoltNorm.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "cbStarfireNum"),
        ("CRI-SERVER-MIB", "cbStarfire5VDC"),
        ("CRI-SERVER-MIB", "cbStarfire5VDCHK"),
        ("CRI-SERVER-MIB", "cbStarfire3p3VDCHK"),
        ("CRI-SERVER-MIB", "cbStarfire5VDCPer"),
        ("CRI-SERVER-MIB", "cbStarfire5VDCFan"))
)
if mibBuilder.loadTexts:
    cbVoltNorm.setStatus(
        ""
    )

cbVoltMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 39)
)
cbVoltMax.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "cbStarfireNum"),
        ("CRI-SERVER-MIB", "cbStarfire5VDC"),
        ("CRI-SERVER-MIB", "cbStarfire5VDCHK"),
        ("CRI-SERVER-MIB", "cbStarfire3p3VDCHK"),
        ("CRI-SERVER-MIB", "cbStarfire5VDCPer"),
        ("CRI-SERVER-MIB", "cbStarfire5VDCFan"))
)
if mibBuilder.loadTexts:
    cbVoltMax.setStatus(
        ""
    )

cbVoltMin = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 40)
)
cbVoltMin.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "cbStarfireNum"),
        ("CRI-SERVER-MIB", "cbStarfire5VDC"),
        ("CRI-SERVER-MIB", "cbStarfire5VDCHK"),
        ("CRI-SERVER-MIB", "cbStarfire3p3VDCHK"),
        ("CRI-SERVER-MIB", "cbStarfire5VDCPer"),
        ("CRI-SERVER-MIB", "cbStarfire5VDCFan"))
)
if mibBuilder.loadTexts:
    cbVoltMin.setStatus(
        ""
    )

cbVoltBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 41)
)
cbVoltBad.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "cbStarfireNum"),
        ("CRI-SERVER-MIB", "cbStarfire5VDC"),
        ("CRI-SERVER-MIB", "cbStarfire5VDCHK"),
        ("CRI-SERVER-MIB", "cbStarfire3p3VDCHK"),
        ("CRI-SERVER-MIB", "cbStarfire5VDCPer"),
        ("CRI-SERVER-MIB", "cbStarfire5VDCFan"))
)
if mibBuilder.loadTexts:
    cbVoltBad.setStatus(
        ""
    )

cbVoltChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 42)
)
cbVoltChange.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "cbStarfireNum"),
        ("CRI-SERVER-MIB", "cbStarfire5VDC"),
        ("CRI-SERVER-MIB", "cbStarfire5VDCHK"),
        ("CRI-SERVER-MIB", "cbStarfire3p3VDCHK"),
        ("CRI-SERVER-MIB", "cbStarfire5VDCPer"),
        ("CRI-SERVER-MIB", "cbStarfire5VDCFan"))
)
if mibBuilder.loadTexts:
    cbVoltChange.setStatus(
        ""
    )

centerplaneVoltNorm = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 43)
)
centerplaneVoltNorm.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "centerplaneStarfireNum"))
)
if mibBuilder.loadTexts:
    centerplaneVoltNorm.setStatus(
        ""
    )

centerplaneVoltMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 44)
)
centerplaneVoltMax.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "centerplaneStarfireNum"))
)
if mibBuilder.loadTexts:
    centerplaneVoltMax.setStatus(
        ""
    )

centerplaneVoltMin = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 45)
)
centerplaneVoltMin.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "centerplaneStarfireNum"))
)
if mibBuilder.loadTexts:
    centerplaneVoltMin.setStatus(
        ""
    )

centerplaneVoltBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 46)
)
centerplaneVoltBad.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "centerplaneStarfireNum"))
)
if mibBuilder.loadTexts:
    centerplaneVoltBad.setStatus(
        ""
    )

centerplaneVoltChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 47)
)
centerplaneVoltChange.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "centerplaneStarfireNum"))
)
if mibBuilder.loadTexts:
    centerplaneVoltChange.setStatus(
        ""
    )

suppBrdVoltNorm = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 48)
)
suppBrdVoltNorm.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "suppBrdStarfireNum"),
        ("CRI-SERVER-MIB", "suppBrdStarfire5VDCHK"),
        ("CRI-SERVER-MIB", "suppBrdStarfire3p3VDCHK"))
)
if mibBuilder.loadTexts:
    suppBrdVoltNorm.setStatus(
        ""
    )

suppBrdVoltMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 49)
)
suppBrdVoltMax.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "suppBrdStarfireNum"),
        ("CRI-SERVER-MIB", "suppBrdStarfire5VDCHK"),
        ("CRI-SERVER-MIB", "suppBrdStarfire3p3VDCHK"))
)
if mibBuilder.loadTexts:
    suppBrdVoltMax.setStatus(
        ""
    )

suppBrdVoltMin = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 50)
)
suppBrdVoltMin.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "suppBrdStarfireNum"),
        ("CRI-SERVER-MIB", "suppBrdStarfire5VDCHK"),
        ("CRI-SERVER-MIB", "suppBrdStarfire3p3VDCHK"))
)
if mibBuilder.loadTexts:
    suppBrdVoltMin.setStatus(
        ""
    )

suppBrdVoltBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 51)
)
suppBrdVoltBad.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "suppBrdStarfireNum"),
        ("CRI-SERVER-MIB", "suppBrdStarfire5VDCHK"),
        ("CRI-SERVER-MIB", "suppBrdStarfire3p3VDCHK"))
)
if mibBuilder.loadTexts:
    suppBrdVoltBad.setStatus(
        ""
    )

suppBrdVoltChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 52)
)
suppBrdVoltChange.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "suppBrdStarfireNum"),
        ("CRI-SERVER-MIB", "suppBrdStarfire5VDCHK"),
        ("CRI-SERVER-MIB", "suppBrdStarfire3p3VDCHK"))
)
if mibBuilder.loadTexts:
    suppBrdVoltChange.setStatus(
        ""
    )

fanNorm = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 53)
)
fanNorm.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "fanGenNum"),
        ("CRI-SERVER-MIB", "fanGenTraySlotNum"),
        ("CRI-SERVER-MIB", "fanGenStatus"))
)
if mibBuilder.loadTexts:
    fanNorm.setStatus(
        ""
    )

fanFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 54)
)
fanFail.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "fanGenNum"),
        ("CRI-SERVER-MIB", "fanGenTraySlotNum"))
)
if mibBuilder.loadTexts:
    fanFail.setStatus(
        ""
    )

systemConfigurationChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 55)
)
systemConfigurationChange.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "confSysBrdList"),
        ("CRI-SERVER-MIB", "confProcList"),
        ("CRI-SERVER-MIB", "confConBrdList"),
        ("CRI-SERVER-MIB", "confSuppBrdList"),
        ("CRI-SERVER-MIB", "confFanTrayList"),
        ("CRI-SERVER-MIB", "confBulkPowerList"))
)
if mibBuilder.loadTexts:
    systemConfigurationChange.setStatus(
        ""
    )

arbitrationStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 56)
)
arbitrationStop.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "domainName"))
)
if mibBuilder.loadTexts:
    arbitrationStop.setStatus(
        ""
    )

recordStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 57)
)
recordStop.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "domainName"))
)
if mibBuilder.loadTexts:
    recordStop.setStatus(
        ""
    )

watchdog = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 58)
)
watchdog.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "domainName"))
)
if mibBuilder.loadTexts:
    watchdog.setStatus(
        ""
    )

environmentalShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 59)
)
environmentalShutdown.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "domainName"))
)
if mibBuilder.loadTexts:
    environmentalShutdown.setStatus(
        ""
    )

reboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 60)
)
reboot.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "domainName"))
)
if mibBuilder.loadTexts:
    reboot.setStatus(
        ""
    )

panic1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 61)
)
panic1.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "domainName"))
)
if mibBuilder.loadTexts:
    panic1.setStatus(
        ""
    )

panic2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 62)
)
panic2.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "domainName"))
)
if mibBuilder.loadTexts:
    panic2.setStatus(
        ""
    )

panicReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 63)
)
panicReboot.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "domainName"))
)
if mibBuilder.loadTexts:
    panicReboot.setStatus(
        ""
    )

heartbeatFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 64)
)
heartbeatFailure.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "domainName"))
)
if mibBuilder.loadTexts:
    heartbeatFailure.setStatus(
        ""
    )

signatureBlockChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 65)
)
signatureBlockChange.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "procStateGenNum"),
        ("CRI-SERVER-MIB", "procStateGenPgmSignature"),
        ("CRI-SERVER-MIB", "procStateGenPgmState"),
        ("CRI-SERVER-MIB", "procStateGenPgmSubState"))
)
if mibBuilder.loadTexts:
    signatureBlockChange.setStatus(
        ""
    )

sysbrdPowerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 66)
)
sysbrdPowerOff.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "sysBrdGenNum"))
)
if mibBuilder.loadTexts:
    sysbrdPowerOff.setStatus(
        ""
    )

sysbrdPowerOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 67)
)
sysbrdPowerOn.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "sysBrdGenNum"))
)
if mibBuilder.loadTexts:
    sysbrdPowerOn.setStatus(
        ""
    )

suppbrdPowerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 68)
)
suppbrdPowerOff.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "suppBrdGenNum"))
)
if mibBuilder.loadTexts:
    suppbrdPowerOff.setStatus(
        ""
    )

suppbrdPowerOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 69)
)
suppbrdPowerOn.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "suppBrdGenNum"))
)
if mibBuilder.loadTexts:
    suppbrdPowerOn.setStatus(
        ""
    )

bulkPowerNorm = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 70)
)
bulkPowerNorm.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "bulkPowerGenNum"))
)
if mibBuilder.loadTexts:
    bulkPowerNorm.setStatus(
        ""
    )

bulkPowerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 71)
)
bulkPowerFail.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "bulkPowerGenNum"))
)
if mibBuilder.loadTexts:
    bulkPowerFail.setStatus(
        ""
    )

bootProcChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 72)
)
bootProcChange.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "domainName"),
        ("CRI-SERVER-MIB", "domainBootProc"),
        ("CRI-SERVER-MIB", "domainProcConfig"),
        ("CRI-SERVER-MIB", "domainABusConfig"),
        ("CRI-SERVER-MIB", "domainDBusConfig"))
)
if mibBuilder.loadTexts:
    bootProcChange.setStatus(
        ""
    )

sigObpBooting = NotificationType(
    (1, 3, 6, 1, 4, 1, 34, 0, 73)
)
sigObpBooting.setObjects(
      *(("CRI-SERVER-MIB", "platformName"),
        ("CRI-SERVER-MIB", "procStateGenNum"),
        ("CRI-SERVER-MIB", "domainName"))
)
if mibBuilder.loadTexts:
    sigObpBooting.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CRI-SERVER-MIB",
    **{"DisplayString": DisplayString,
       "Boolean": Boolean,
       "YesNo": YesNo,
       "sun": sun,
       "domainChange": domainChange,
       "eddControl": eddControl,
       "eddState": eddState,
       "sysBrdTempNorm": sysBrdTempNorm,
       "sysBrdTempHigh": sysBrdTempHigh,
       "sysBrdTempWarn": sysBrdTempWarn,
       "sysBrdTempMax": sysBrdTempMax,
       "sysBrdTemp911": sysBrdTemp911,
       "sysBrdTempBad": sysBrdTempBad,
       "sysBrdTempChange": sysBrdTempChange,
       "cbTempNorm": cbTempNorm,
       "cbTempHigh": cbTempHigh,
       "cbTempWarn": cbTempWarn,
       "cbTempMax": cbTempMax,
       "cbTemp911": cbTemp911,
       "cbTempBad": cbTempBad,
       "cbTempChange": cbTempChange,
       "centerplaneTempNorm": centerplaneTempNorm,
       "centerplaneTempHigh": centerplaneTempHigh,
       "centerplaneTempWarn": centerplaneTempWarn,
       "centerplaneTempMax": centerplaneTempMax,
       "centerplaneTemp911": centerplaneTemp911,
       "centerplaneTempBad": centerplaneTempBad,
       "centerplaneTempChange": centerplaneTempChange,
       "cbeConnected": cbeConnected,
       "cbeDisconnected": cbeDisconnected,
       "suppBrdTempNorm": suppBrdTempNorm,
       "suppBrdTempHigh": suppBrdTempHigh,
       "suppBrdTempWarn": suppBrdTempWarn,
       "suppBrdTempMax": suppBrdTempMax,
       "suppBrdTemp911": suppBrdTemp911,
       "suppBrdTempBad": suppBrdTempBad,
       "suppBrdTempChange": suppBrdTempChange,
       "sysBrdVoltNorm": sysBrdVoltNorm,
       "sysBrdVoltMax": sysBrdVoltMax,
       "sysBrdVoltMin": sysBrdVoltMin,
       "sysBrdVoltBad": sysBrdVoltBad,
       "sysBrdVoltChange": sysBrdVoltChange,
       "cbVoltNorm": cbVoltNorm,
       "cbVoltMax": cbVoltMax,
       "cbVoltMin": cbVoltMin,
       "cbVoltBad": cbVoltBad,
       "cbVoltChange": cbVoltChange,
       "centerplaneVoltNorm": centerplaneVoltNorm,
       "centerplaneVoltMax": centerplaneVoltMax,
       "centerplaneVoltMin": centerplaneVoltMin,
       "centerplaneVoltBad": centerplaneVoltBad,
       "centerplaneVoltChange": centerplaneVoltChange,
       "suppBrdVoltNorm": suppBrdVoltNorm,
       "suppBrdVoltMax": suppBrdVoltMax,
       "suppBrdVoltMin": suppBrdVoltMin,
       "suppBrdVoltBad": suppBrdVoltBad,
       "suppBrdVoltChange": suppBrdVoltChange,
       "fanNorm": fanNorm,
       "fanFail": fanFail,
       "systemConfigurationChange": systemConfigurationChange,
       "arbitrationStop": arbitrationStop,
       "recordStop": recordStop,
       "watchdog": watchdog,
       "environmentalShutdown": environmentalShutdown,
       "reboot": reboot,
       "panic1": panic1,
       "panic2": panic2,
       "panicReboot": panicReboot,
       "heartbeatFailure": heartbeatFailure,
       "signatureBlockChange": signatureBlockChange,
       "sysbrdPowerOff": sysbrdPowerOff,
       "sysbrdPowerOn": sysbrdPowerOn,
       "suppbrdPowerOff": suppbrdPowerOff,
       "suppbrdPowerOn": suppbrdPowerOn,
       "bulkPowerNorm": bulkPowerNorm,
       "bulkPowerFail": bulkPowerFail,
       "bootProcChange": bootProcChange,
       "sigObpBooting": sigObpBooting,
       "products": products,
       "general": general,
       "platform": platform,
       "platformType": platformType,
       "platformName": platformName,
       "platformAmbientTemp": platformAmbientTemp,
       "platformReset": platformReset,
       "platformInterconnectClockFreq": platformInterconnectClockFreq,
       "platformProcClockFreq": platformProcClockFreq,
       "platformJtagClockFreq": platformJtagClockFreq,
       "platformTargetInterconnectClockFreq": platformTargetInterconnectClockFreq,
       "platformTargetProcClockMultiple": platformTargetProcClockMultiple,
       "platformTargetJtagClockFreq": platformTargetJtagClockFreq,
       "platformMasterConBrd": platformMasterConBrd,
       "platformSysClkConBrd": platformSysClkConBrd,
       "conf": conf,
       "confNumDomain": confNumDomain,
       "confNumSysBrd": confNumSysBrd,
       "confNumProc": confNumProc,
       "confNumConBrd": confNumConBrd,
       "confNumCenterplane": confNumCenterplane,
       "confNumSuppBrd": confNumSuppBrd,
       "confNumIoCab": confNumIoCab,
       "confNumFanTray": confNumFanTray,
       "confNumBulkPower": confNumBulkPower,
       "confNumSysBrdPower": confNumSysBrdPower,
       "confSysBrdList": confSysBrdList,
       "confProcList": confProcList,
       "confConBrdList": confConBrdList,
       "confCenterplaneList": confCenterplaneList,
       "confSuppBrdList": confSuppBrdList,
       "confIoCabList": confIoCabList,
       "confFanTrayList": confFanTrayList,
       "confBulkPowerList": confBulkPowerList,
       "confSysBrdPowerList": confSysBrdPowerList,
       "confMaxProcPerSysBrd": confMaxProcPerSysBrd,
       "confMaxFanPerTray": confMaxFanPerTray,
       "confMaxLEDPerFanTray": confMaxLEDPerFanTray,
       "confMaxLEDPerBulkPower": confMaxLEDPerBulkPower,
       "confMaxLEDPerSysBrd": confMaxLEDPerSysBrd,
       "confMemAddrMap": confMemAddrMap,
       "domainTable": domainTable,
       "domainEntry": domainEntry,
       "domainIndex": domainIndex,
       "domainName": domainName,
       "domainNumSysBrd": domainNumSysBrd,
       "domainSysBrdList": domainSysBrdList,
       "domainOSVersion": domainOSVersion,
       "domainProcList": domainProcList,
       "domainBootProc": domainBootProc,
       "domainInterruptVector": domainInterruptVector,
       "domainSysBrdConfig": domainSysBrdConfig,
       "domainProcConfig": domainProcConfig,
       "domainABusConfig": domainABusConfig,
       "domainDBusConfig": domainDBusConfig,
       "sysBrdGenTable": sysBrdGenTable,
       "sysBrdGenEntry": sysBrdGenEntry,
       "sysBrdGenIndex": sysBrdGenIndex,
       "sysBrdGenNum": sysBrdGenNum,
       "sysBrdGenPower": sysBrdGenPower,
       "sysBrdGenNumProc": sysBrdGenNumProc,
       "sysBrdGenProcList": sysBrdGenProcList,
       "sysBrdGenReset": sysBrdGenReset,
       "sysBrdGenPowerControl": sysBrdGenPowerControl,
       "procStateGenTable": procStateGenTable,
       "procStateGenEntry": procStateGenEntry,
       "procStateGenIndex": procStateGenIndex,
       "procStateGenNum": procStateGenNum,
       "procStateGenHeartbeat": procStateGenHeartbeat,
       "procStateGenPgmSignature": procStateGenPgmSignature,
       "procStateGenPgmState": procStateGenPgmState,
       "procStateGenPgmSubState": procStateGenPgmSubState,
       "procStateGenTemp": procStateGenTemp,
       "procCommGenTable": procCommGenTable,
       "procCommGenEntry": procCommGenEntry,
       "procCommGenIndex": procCommGenIndex,
       "procCommGenNum": procCommGenNum,
       "procCommGenSspMboxLen": procCommGenSspMboxLen,
       "procCommGenSspMboxFlag": procCommGenSspMboxFlag,
       "procCommGenSspMboxCmd": procCommGenSspMboxCmd,
       "procCommGenSspMboxData": procCommGenSspMboxData,
       "procCommGenHostMboxLen": procCommGenHostMboxLen,
       "procCommGenHostMboxFlag": procCommGenHostMboxFlag,
       "procCommGenHostMboxCmd": procCommGenHostMboxCmd,
       "procCommGenHostMboxData": procCommGenHostMboxData,
       "procCommGenObpMboxLen": procCommGenObpMboxLen,
       "procCommGenObpMboxFlag": procCommGenObpMboxFlag,
       "procCommGenObpMboxCmd": procCommGenObpMboxCmd,
       "procCommGenObpMboxData": procCommGenObpMboxData,
       "procCommGenCvcInputData": procCommGenCvcInputData,
       "procCommGenCvcOutputData": procCommGenCvcOutputData,
       "cbGenTable": cbGenTable,
       "cbGenEntry": cbGenEntry,
       "cbGenIndex": cbGenIndex,
       "cbGenNum": cbGenNum,
       "cbGenPower": cbGenPower,
       "cbGenPowerControl": cbGenPowerControl,
       "ioCabGenTable": ioCabGenTable,
       "ioCabGenEntry": ioCabGenEntry,
       "ioCabGenIndex": ioCabGenIndex,
       "ioCabGenNum": ioCabGenNum,
       "ioCabGenPower": ioCabGenPower,
       "fanTrayGenTable": fanTrayGenTable,
       "fanTrayGenEntry": fanTrayGenEntry,
       "fanTrayGenIndex": fanTrayGenIndex,
       "fanTrayGenNum": fanTrayGenNum,
       "fanTrayGenPower": fanTrayGenPower,
       "fanGenTable": fanGenTable,
       "fanGenEntry": fanGenEntry,
       "fanGenIndex": fanGenIndex,
       "fanGenTraySlotNum": fanGenTraySlotNum,
       "fanGenNum": fanGenNum,
       "fanGenStatus": fanGenStatus,
       "fanGenSpeed": fanGenSpeed,
       "fanGenPowerControl": fanGenPowerControl,
       "suppBrdGenTable": suppBrdGenTable,
       "suppBrdGenEntry": suppBrdGenEntry,
       "suppBrdGenIndex": suppBrdGenIndex,
       "suppBrdGenNum": suppBrdGenNum,
       "suppBrdGenPower": suppBrdGenPower,
       "suppBrdGenPowerControl": suppBrdGenPowerControl,
       "bulkPowerGenTable": bulkPowerGenTable,
       "bulkPowerGenEntry": bulkPowerGenEntry,
       "bulkPowerGenIndex": bulkPowerGenIndex,
       "bulkPowerGenNum": bulkPowerGenNum,
       "bulkPowerGenControl": bulkPowerGenControl,
       "bulkPowerGenStatus": bulkPowerGenStatus,
       "ue10000": ue10000,
       "sysBrdStarfireTable": sysBrdStarfireTable,
       "sysBrdStarfireEntry": sysBrdStarfireEntry,
       "sysBrdStarfireIndex": sysBrdStarfireIndex,
       "sysBrdStarfireNum": sysBrdStarfireNum,
       "sysBrdStarfireCIC0Temp": sysBrdStarfireCIC0Temp,
       "sysBrdStarfireCIC1Temp": sysBrdStarfireCIC1Temp,
       "sysBrdStarfireMCTemp": sysBrdStarfireMCTemp,
       "sysBrdStarfireXDB2Temp": sysBrdStarfireXDB2Temp,
       "sysBrdStarfireXDB3Temp": sysBrdStarfireXDB3Temp,
       "sysBrdStarfirePROC0Temp": sysBrdStarfirePROC0Temp,
       "sysBrdStarfirePROC1Temp": sysBrdStarfirePROC1Temp,
       "sysBrdStarfirePROC2Temp": sysBrdStarfirePROC2Temp,
       "sysBrdStarfirePROC3Temp": sysBrdStarfirePROC3Temp,
       "sysBrdStarfire3p3VDCTemp": sysBrdStarfire3p3VDCTemp,
       "sysBrdStarfireVDCCoreTemp": sysBrdStarfireVDCCoreTemp,
       "sysBrdStarfire5VDCTemp": sysBrdStarfire5VDCTemp,
       "sysBrdStarfire3p3VDC": sysBrdStarfire3p3VDC,
       "sysBrdStarfire5VDCHK": sysBrdStarfire5VDCHK,
       "sysBrdStarfire5VDC": sysBrdStarfire5VDC,
       "sysBrdStarfireVDCCore": sysBrdStarfireVDCCore,
       "sysBrdStarfire3p3VDCHK": sysBrdStarfire3p3VDCHK,
       "cbStarfireTable": cbStarfireTable,
       "cbStarfireEntry": cbStarfireEntry,
       "cbStarfireIndex": cbStarfireIndex,
       "cbStarfireNum": cbStarfireNum,
       "cbStarfireHostName": cbStarfireHostName,
       "cbStarfire5VDCTemp": cbStarfire5VDCTemp,
       "cbStarfire5VDCPerTemp": cbStarfire5VDCPerTemp,
       "cbStarfire5VDCFanTemp": cbStarfire5VDCFanTemp,
       "cbStarfireSen0Temp": cbStarfireSen0Temp,
       "cbStarfireSen1Temp": cbStarfireSen1Temp,
       "cbStarfireSen2Temp": cbStarfireSen2Temp,
       "cbStarfire5VDC": cbStarfire5VDC,
       "cbStarfire5VDCHK": cbStarfire5VDCHK,
       "cbStarfire3p3VDCHK": cbStarfire3p3VDCHK,
       "cbStarfire5VDCPer": cbStarfire5VDCPer,
       "cbStarfire5VDCFan": cbStarfire5VDCFan,
       "centerplaneStarfireTable": centerplaneStarfireTable,
       "centerplaneStarfireEntry": centerplaneStarfireEntry,
       "centerplaneStarfireIndex": centerplaneStarfireIndex,
       "centerplaneStarfireNum": centerplaneStarfireNum,
       "centerplaneStarfireTemp0": centerplaneStarfireTemp0,
       "centerplaneStarfireTemp1": centerplaneStarfireTemp1,
       "centerplaneStarfireTemp2": centerplaneStarfireTemp2,
       "centerplaneStarfireTemp3": centerplaneStarfireTemp3,
       "centerplaneStarfireTemp4": centerplaneStarfireTemp4,
       "centerplaneStarfireTemp5": centerplaneStarfireTemp5,
       "centerplaneStarfireTemp6": centerplaneStarfireTemp6,
       "centerplaneStarfireTemp7": centerplaneStarfireTemp7,
       "centerplaneStarfireTemp8": centerplaneStarfireTemp8,
       "centerplaneStarfireTemp9": centerplaneStarfireTemp9,
       "suppBrdStarfireTable": suppBrdStarfireTable,
       "suppBrdStarfireEntry": suppBrdStarfireEntry,
       "suppBrdStarfireIndex": suppBrdStarfireIndex,
       "suppBrdStarfireNum": suppBrdStarfireNum,
       "suppBrdStarfire3p3VDC1Temp": suppBrdStarfire3p3VDC1Temp,
       "suppBrdStarfire3p3VDC2Temp": suppBrdStarfire3p3VDC2Temp,
       "suppBrdStarfire5VDCHK": suppBrdStarfire5VDCHK,
       "suppBrdStarfire3p3VDCHK": suppBrdStarfire3p3VDCHK,
       "suppBrdStarfire3p3VDC": suppBrdStarfire3p3VDC,
       "ssp": ssp,
       "sspPlatformApp": sspPlatformApp,
       "sspPlatformAppEddControl": sspPlatformAppEddControl,
       "sspPlatformAppEddState": sspPlatformAppEddState}
)
