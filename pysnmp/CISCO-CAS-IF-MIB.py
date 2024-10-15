# SNMP MIB module (CISCO-CAS-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CAS-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:56 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CountryCode,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CountryCode")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoCasIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 85)
)
ciscoCasIfMIB.setRevisions(
        ("2004-10-13 00:00",
         "2004-09-30 00:00",
         "2004-01-15 00:00",
         "2003-04-18 00:00",
         "2002-10-02 00:00",
         "1999-01-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CcasIfObjects_ObjectIdentity = ObjectIdentity
ccasIfObjects = _CcasIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1)
)
_CcasDS1Objects_ObjectIdentity = ObjectIdentity
ccasDS1Objects = _CcasDS1Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 1)
)
_CcasDs1IfCfgTable_Object = MibTable
ccasDs1IfCfgTable = _CcasDs1IfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ccasDs1IfCfgTable.setStatus("current")
_CcasDs1IfCfgEntry_Object = MibTableRow
ccasDs1IfCfgEntry = _CcasDs1IfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 1, 1, 1)
)
ccasDs1IfCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ccasDs1IfCfgEntry.setStatus("current")


class _CcasDs1IfCfgDs0ChannelsConfigurable_Type(OctetString):
    """Custom type ccasDs1IfCfgDs0ChannelsConfigurable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_CcasDs1IfCfgDs0ChannelsConfigurable_Type.__name__ = "OctetString"
_CcasDs1IfCfgDs0ChannelsConfigurable_Object = MibTableColumn
ccasDs1IfCfgDs0ChannelsConfigurable = _CcasDs1IfCfgDs0ChannelsConfigurable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 1, 1, 1, 1),
    _CcasDs1IfCfgDs0ChannelsConfigurable_Type()
)
ccasDs1IfCfgDs0ChannelsConfigurable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccasDs1IfCfgDs0ChannelsConfigurable.setStatus("current")
_CcasGrpObjects_ObjectIdentity = ObjectIdentity
ccasGrpObjects = _CcasGrpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2)
)
_CcasGrpGeneralObjects_ObjectIdentity = ObjectIdentity
ccasGrpGeneralObjects = _CcasGrpGeneralObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 1)
)
_CcasGrpCfgTable_Object = MibTable
ccasGrpCfgTable = _CcasGrpCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ccasGrpCfgTable.setStatus("current")
_CcasGrpCfgEntry_Object = MibTableRow
ccasGrpCfgEntry = _CcasGrpCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 1, 1, 1)
)
ccasGrpCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CAS-IF-MIB", "ccasGrpCfgIndex"),
)
if mibBuilder.loadTexts:
    ccasGrpCfgEntry.setStatus("current")


class _CcasGrpCfgIndex_Type(Integer32):
    """Custom type ccasGrpCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_CcasGrpCfgIndex_Type.__name__ = "Integer32"
_CcasGrpCfgIndex_Object = MibTableColumn
ccasGrpCfgIndex = _CcasGrpCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 1, 1, 1, 1),
    _CcasGrpCfgIndex_Type()
)
ccasGrpCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccasGrpCfgIndex.setStatus("current")


class _CcasGrpCfgType_Type(Integer32):
    """Custom type ccasGrpCfgType based on Integer32"""
    defaultValue = 1

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
              23,
              24,
              25,
              26,
              27)
        )
    )
    namedValues = NamedValues(
        *(("emDelayDial", 4),
          ("emImmedStart", 3),
          ("emLmr", 27),
          ("emMelDelayDial", 23),
          ("emMelImmedStart", 21),
          ("emMelWink", 22),
          ("emWinkStart", 1),
          ("emWinkStartFgd", 2),
          ("extsig", 26),
          ("fgdEANA", 20),
          ("fgdOS", 15),
          ("fxoGroundStart", 14),
          ("fxoLoopStart", 13),
          ("fxoMelcas", 25),
          ("fxsGroundStart", 6),
          ("fxsLoopStart", 5),
          ("fxsMelcas", 24),
          ("nullSignaling", 16),
          ("p7", 12),
          ("r1Itu", 17),
          ("r1Modified", 18),
          ("r1Turkey", 19),
          ("r2Analog", 9),
          ("r2Digital", 10),
          ("r2Pulse", 11),
          ("sasGroundStart", 8),
          ("sasLoopStart", 7))
    )


_CcasGrpCfgType_Type.__name__ = "Integer32"
_CcasGrpCfgType_Object = MibTableColumn
ccasGrpCfgType = _CcasGrpCfgType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 1, 1, 1, 2),
    _CcasGrpCfgType_Type()
)
ccasGrpCfgType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasGrpCfgType.setStatus("current")


class _CcasGrpCfgDs0Channels_Type(OctetString):
    """Custom type ccasGrpCfgDs0Channels based on OctetString"""
    defaultHexValue = "00000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CcasGrpCfgDs0Channels_Type.__name__ = "OctetString"
_CcasGrpCfgDs0Channels_Object = MibTableColumn
ccasGrpCfgDs0Channels = _CcasGrpCfgDs0Channels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 1, 1, 1, 3),
    _CcasGrpCfgDs0Channels_Type()
)
ccasGrpCfgDs0Channels.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasGrpCfgDs0Channels.setStatus("current")
_CcasGrpCfgRowStatus_Type = RowStatus
_CcasGrpCfgRowStatus_Object = MibTableColumn
ccasGrpCfgRowStatus = _CcasGrpCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 1, 1, 1, 4),
    _CcasGrpCfgRowStatus_Type()
)
ccasGrpCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasGrpCfgRowStatus.setStatus("current")


class _CcasGrpCfgServiceType_Type(Integer32):
    """Custom type ccasGrpCfgServiceType based on Integer32"""
    defaultValue = 1

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
        *(("casServAuto", 4),
          ("casServModem", 3),
          ("casServSw56", 2),
          ("ds0xconn", 10),
          ("h248", 9),
          ("mgcp", 6),
          ("none", 1),
          ("other", 7),
          ("sgcp", 5),
          ("trunkingService", 8),
          ("xgcp", 11))
    )


_CcasGrpCfgServiceType_Type.__name__ = "Integer32"
_CcasGrpCfgServiceType_Object = MibTableColumn
ccasGrpCfgServiceType = _CcasGrpCfgServiceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 1, 1, 1, 5),
    _CcasGrpCfgServiceType_Type()
)
ccasGrpCfgServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasGrpCfgServiceType.setStatus("current")
_CcasGrpEMObjects_ObjectIdentity = ObjectIdentity
ccasGrpEMObjects = _CcasGrpEMObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 2)
)
_CcasGrpEMCfgTable_Object = MibTable
ccasGrpEMCfgTable = _CcasGrpEMCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ccasGrpEMCfgTable.setStatus("current")
_CcasGrpEMCfgEntry_Object = MibTableRow
ccasGrpEMCfgEntry = _CcasGrpEMCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 2, 1, 1)
)
ccasGrpEMCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CAS-IF-MIB", "ccasGrpCfgIndex"),
)
if mibBuilder.loadTexts:
    ccasGrpEMCfgEntry.setStatus("current")


class _CcasGrpEMCfgDialType_Type(Integer32):
    """Custom type ccasGrpEMCfgDialType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dtmf", 1),
          ("mf", 3),
          ("pulse", 2))
    )


_CcasGrpEMCfgDialType_Type.__name__ = "Integer32"
_CcasGrpEMCfgDialType_Object = MibTableColumn
ccasGrpEMCfgDialType = _CcasGrpEMCfgDialType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 2, 1, 1, 1),
    _CcasGrpEMCfgDialType_Type()
)
ccasGrpEMCfgDialType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasGrpEMCfgDialType.setStatus("current")


class _CcasGrpEMCfgDnisAni_Type(Bits):
    """Custom type ccasGrpEMCfgDnisAni based on Bits"""
    namedValues = NamedValues(
        *(("incomingAni", 1),
          ("incomingDnis", 0),
          ("outgoingAni", 3),
          ("outgoingDnis", 2))
    )

_CcasGrpEMCfgDnisAni_Type.__name__ = "Bits"
_CcasGrpEMCfgDnisAni_Object = MibTableColumn
ccasGrpEMCfgDnisAni = _CcasGrpEMCfgDnisAni_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 2, 1, 1, 2),
    _CcasGrpEMCfgDnisAni_Type()
)
ccasGrpEMCfgDnisAni.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasGrpEMCfgDnisAni.setStatus("current")


class _CcasGrpEMCfgLmrMCap_Type(Integer32):
    """Custom type ccasGrpEMCfgLmrMCap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("audio", 2),
          ("dial", 3),
          ("inact", 1))
    )


_CcasGrpEMCfgLmrMCap_Type.__name__ = "Integer32"
_CcasGrpEMCfgLmrMCap_Object = MibTableColumn
ccasGrpEMCfgLmrMCap = _CcasGrpEMCfgLmrMCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 2, 1, 1, 3),
    _CcasGrpEMCfgLmrMCap_Type()
)
ccasGrpEMCfgLmrMCap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasGrpEMCfgLmrMCap.setStatus("current")


class _CcasGrpEMCfgLmrECap_Type(Integer32):
    """Custom type ccasGrpEMCfgLmrECap based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 6),
          ("seize", 4),
          ("voice", 5))
    )


_CcasGrpEMCfgLmrECap_Type.__name__ = "Integer32"
_CcasGrpEMCfgLmrECap_Object = MibTableColumn
ccasGrpEMCfgLmrECap = _CcasGrpEMCfgLmrECap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 2, 1, 1, 4),
    _CcasGrpEMCfgLmrECap_Type()
)
ccasGrpEMCfgLmrECap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasGrpEMCfgLmrECap.setStatus("current")


class _CcasGrpEMCfgAutoGainControl_Type(TruthValue):
    """Custom type ccasGrpEMCfgAutoGainControl based on TruthValue"""


_CcasGrpEMCfgAutoGainControl_Object = MibTableColumn
ccasGrpEMCfgAutoGainControl = _CcasGrpEMCfgAutoGainControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 2, 1, 1, 5),
    _CcasGrpEMCfgAutoGainControl_Type()
)
ccasGrpEMCfgAutoGainControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasGrpEMCfgAutoGainControl.setStatus("current")
_CcasGrpEMTmTable_Object = MibTable
ccasGrpEMTmTable = _CcasGrpEMTmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    ccasGrpEMTmTable.setStatus("current")
_CcasGrpEMTmEntry_Object = MibTableRow
ccasGrpEMTmEntry = _CcasGrpEMTmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ccasGrpEMTmEntry.setStatus("current")


class _CcasGrpEMTmClearWaitDuration_Type(Integer32):
    """Custom type ccasGrpEMTmClearWaitDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 2000),
    )


_CcasGrpEMTmClearWaitDuration_Type.__name__ = "Integer32"
_CcasGrpEMTmClearWaitDuration_Object = MibTableColumn
ccasGrpEMTmClearWaitDuration = _CcasGrpEMTmClearWaitDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 2, 2, 1, 1),
    _CcasGrpEMTmClearWaitDuration_Type()
)
ccasGrpEMTmClearWaitDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasGrpEMTmClearWaitDuration.setStatus("current")
if mibBuilder.loadTexts:
    ccasGrpEMTmClearWaitDuration.setUnits("milliseconds")


class _CcasGrpEMTmMaxWinkWaitDuration_Type(Integer32):
    """Custom type ccasGrpEMTmMaxWinkWaitDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 5000),
    )


_CcasGrpEMTmMaxWinkWaitDuration_Type.__name__ = "Integer32"
_CcasGrpEMTmMaxWinkWaitDuration_Object = MibTableColumn
ccasGrpEMTmMaxWinkWaitDuration = _CcasGrpEMTmMaxWinkWaitDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 2, 2, 1, 2),
    _CcasGrpEMTmMaxWinkWaitDuration_Type()
)
ccasGrpEMTmMaxWinkWaitDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasGrpEMTmMaxWinkWaitDuration.setStatus("current")
if mibBuilder.loadTexts:
    ccasGrpEMTmMaxWinkWaitDuration.setUnits("milliseconds")


class _CcasGrpEMTmMaxWinkDuration_Type(Integer32):
    """Custom type ccasGrpEMTmMaxWinkDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 3000),
    )


_CcasGrpEMTmMaxWinkDuration_Type.__name__ = "Integer32"
_CcasGrpEMTmMaxWinkDuration_Object = MibTableColumn
ccasGrpEMTmMaxWinkDuration = _CcasGrpEMTmMaxWinkDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 2, 2, 1, 3),
    _CcasGrpEMTmMaxWinkDuration_Type()
)
ccasGrpEMTmMaxWinkDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasGrpEMTmMaxWinkDuration.setStatus("current")
if mibBuilder.loadTexts:
    ccasGrpEMTmMaxWinkDuration.setUnits("milliseconds")


class _CcasGrpEMTmDelayStart_Type(Integer32):
    """Custom type ccasGrpEMTmDelayStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 2000),
    )


_CcasGrpEMTmDelayStart_Type.__name__ = "Integer32"
_CcasGrpEMTmDelayStart_Object = MibTableColumn
ccasGrpEMTmDelayStart = _CcasGrpEMTmDelayStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 2, 2, 1, 4),
    _CcasGrpEMTmDelayStart_Type()
)
ccasGrpEMTmDelayStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasGrpEMTmDelayStart.setStatus("current")
if mibBuilder.loadTexts:
    ccasGrpEMTmDelayStart.setUnits("milliseconds")


class _CcasGrpEMTmMaxDelayDuration_Type(Integer32):
    """Custom type ccasGrpEMTmMaxDelayDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 5000),
    )


_CcasGrpEMTmMaxDelayDuration_Type.__name__ = "Integer32"
_CcasGrpEMTmMaxDelayDuration_Object = MibTableColumn
ccasGrpEMTmMaxDelayDuration = _CcasGrpEMTmMaxDelayDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 2, 2, 1, 5),
    _CcasGrpEMTmMaxDelayDuration_Type()
)
ccasGrpEMTmMaxDelayDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasGrpEMTmMaxDelayDuration.setStatus("current")
if mibBuilder.loadTexts:
    ccasGrpEMTmMaxDelayDuration.setUnits("milliseconds")


class _CcasGrpEMTmMinDelayPulseWidth_Type(Integer32):
    """Custom type ccasGrpEMTmMinDelayPulseWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(140, 5000),
    )


_CcasGrpEMTmMinDelayPulseWidth_Type.__name__ = "Integer32"
_CcasGrpEMTmMinDelayPulseWidth_Object = MibTableColumn
ccasGrpEMTmMinDelayPulseWidth = _CcasGrpEMTmMinDelayPulseWidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 2, 2, 1, 6),
    _CcasGrpEMTmMinDelayPulseWidth_Type()
)
ccasGrpEMTmMinDelayPulseWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasGrpEMTmMinDelayPulseWidth.setStatus("current")
if mibBuilder.loadTexts:
    ccasGrpEMTmMinDelayPulseWidth.setUnits("milliseconds")


class _CcasGrpEMTmDigitDuration_Type(Integer32):
    """Custom type ccasGrpEMTmDigitDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 500),
    )


_CcasGrpEMTmDigitDuration_Type.__name__ = "Integer32"
_CcasGrpEMTmDigitDuration_Object = MibTableColumn
ccasGrpEMTmDigitDuration = _CcasGrpEMTmDigitDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 2, 2, 1, 7),
    _CcasGrpEMTmDigitDuration_Type()
)
ccasGrpEMTmDigitDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasGrpEMTmDigitDuration.setStatus("current")
if mibBuilder.loadTexts:
    ccasGrpEMTmDigitDuration.setUnits("milliseconds")


class _CcasGrpEMTmInterDigitDuration_Type(Integer32):
    """Custom type ccasGrpEMTmInterDigitDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 500),
    )


_CcasGrpEMTmInterDigitDuration_Type.__name__ = "Integer32"
_CcasGrpEMTmInterDigitDuration_Object = MibTableColumn
ccasGrpEMTmInterDigitDuration = _CcasGrpEMTmInterDigitDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 2, 2, 1, 8),
    _CcasGrpEMTmInterDigitDuration_Type()
)
ccasGrpEMTmInterDigitDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasGrpEMTmInterDigitDuration.setStatus("current")
if mibBuilder.loadTexts:
    ccasGrpEMTmInterDigitDuration.setUnits("milliseconds")


class _CcasGrpEMTmPulseRate_Type(Integer32):
    """Custom type ccasGrpEMTmPulseRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 20),
    )


_CcasGrpEMTmPulseRate_Type.__name__ = "Integer32"
_CcasGrpEMTmPulseRate_Object = MibTableColumn
ccasGrpEMTmPulseRate = _CcasGrpEMTmPulseRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 2, 2, 1, 9),
    _CcasGrpEMTmPulseRate_Type()
)
ccasGrpEMTmPulseRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasGrpEMTmPulseRate.setStatus("current")
if mibBuilder.loadTexts:
    ccasGrpEMTmPulseRate.setUnits("pulses per second")


class _CcasGrpEMTmPulseInterDigitDuration_Type(Integer32):
    """Custom type ccasGrpEMTmPulseInterDigitDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_CcasGrpEMTmPulseInterDigitDuration_Type.__name__ = "Integer32"
_CcasGrpEMTmPulseInterDigitDuration_Object = MibTableColumn
ccasGrpEMTmPulseInterDigitDuration = _CcasGrpEMTmPulseInterDigitDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 2, 2, 1, 10),
    _CcasGrpEMTmPulseInterDigitDuration_Type()
)
ccasGrpEMTmPulseInterDigitDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasGrpEMTmPulseInterDigitDuration.setStatus("current")
if mibBuilder.loadTexts:
    ccasGrpEMTmPulseInterDigitDuration.setUnits("milliseconds")


class _CcasGrpEMTmVoiceHangover_Type(Integer32):
    """Custom type ccasGrpEMTmVoiceHangover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_CcasGrpEMTmVoiceHangover_Type.__name__ = "Integer32"
_CcasGrpEMTmVoiceHangover_Object = MibTableColumn
ccasGrpEMTmVoiceHangover = _CcasGrpEMTmVoiceHangover_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 2, 2, 1, 11),
    _CcasGrpEMTmVoiceHangover_Type()
)
ccasGrpEMTmVoiceHangover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasGrpEMTmVoiceHangover.setStatus("current")
if mibBuilder.loadTexts:
    ccasGrpEMTmVoiceHangover.setUnits("milliseconds")


class _CcasGrpEMTmLmrTeardown_Type(Integer32):
    """Custom type ccasGrpEMTmLmrTeardown based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(5, 60000),
    )


_CcasGrpEMTmLmrTeardown_Type.__name__ = "Integer32"
_CcasGrpEMTmLmrTeardown_Object = MibTableColumn
ccasGrpEMTmLmrTeardown = _CcasGrpEMTmLmrTeardown_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 2, 2, 1, 12),
    _CcasGrpEMTmLmrTeardown_Type()
)
ccasGrpEMTmLmrTeardown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasGrpEMTmLmrTeardown.setStatus("current")
if mibBuilder.loadTexts:
    ccasGrpEMTmLmrTeardown.setUnits("seconds")


class _CcasGrpEMTmPttXmt_Type(Integer32):
    """Custom type ccasGrpEMTmPttXmt based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_CcasGrpEMTmPttXmt_Type.__name__ = "Integer32"
_CcasGrpEMTmPttXmt_Object = MibTableColumn
ccasGrpEMTmPttXmt = _CcasGrpEMTmPttXmt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 2, 2, 1, 13),
    _CcasGrpEMTmPttXmt_Type()
)
ccasGrpEMTmPttXmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasGrpEMTmPttXmt.setStatus("current")
if mibBuilder.loadTexts:
    ccasGrpEMTmPttXmt.setUnits("minutes")


class _CcasGrpEMTmPttRcv_Type(Integer32):
    """Custom type ccasGrpEMTmPttRcv based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_CcasGrpEMTmPttRcv_Type.__name__ = "Integer32"
_CcasGrpEMTmPttRcv_Object = MibTableColumn
ccasGrpEMTmPttRcv = _CcasGrpEMTmPttRcv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 2, 2, 1, 14),
    _CcasGrpEMTmPttRcv_Type()
)
ccasGrpEMTmPttRcv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasGrpEMTmPttRcv.setStatus("current")
if mibBuilder.loadTexts:
    ccasGrpEMTmPttRcv.setUnits("minutes")


class _CcasGrpEMTmDelayVoice_Type(Integer32):
    """Custom type ccasGrpEMTmDelayVoice based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_CcasGrpEMTmDelayVoice_Type.__name__ = "Integer32"
_CcasGrpEMTmDelayVoice_Object = MibTableColumn
ccasGrpEMTmDelayVoice = _CcasGrpEMTmDelayVoice_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 2, 2, 1, 15),
    _CcasGrpEMTmDelayVoice_Type()
)
ccasGrpEMTmDelayVoice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccasGrpEMTmDelayVoice.setStatus("current")
if mibBuilder.loadTexts:
    ccasGrpEMTmDelayVoice.setUnits("milliseconds")
_CcasGrpLineObjects_ObjectIdentity = ObjectIdentity
ccasGrpLineObjects = _CcasGrpLineObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 3)
)
_CcasGrpLineCfgTable_Object = MibTable
ccasGrpLineCfgTable = _CcasGrpLineCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ccasGrpLineCfgTable.setStatus("current")
_CcasGrpLineCfgEntry_Object = MibTableRow
ccasGrpLineCfgEntry = _CcasGrpLineCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 3, 1, 1)
)
ccasGrpLineCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CAS-IF-MIB", "ccasGrpCfgIndex"),
)
if mibBuilder.loadTexts:
    ccasGrpLineCfgEntry.setStatus("current")


class _CcasGrpLineCfgNumberRings_Type(Integer32):
    """Custom type ccasGrpLineCfgNumberRings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CcasGrpLineCfgNumberRings_Type.__name__ = "Integer32"
_CcasGrpLineCfgNumberRings_Object = MibTableColumn
ccasGrpLineCfgNumberRings = _CcasGrpLineCfgNumberRings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 3, 1, 1, 1),
    _CcasGrpLineCfgNumberRings_Type()
)
ccasGrpLineCfgNumberRings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasGrpLineCfgNumberRings.setStatus("current")
if mibBuilder.loadTexts:
    ccasGrpLineCfgNumberRings.setUnits("rings")
_CcasGrpLineCfgSupDisconnect_Type = TruthValue
_CcasGrpLineCfgSupDisconnect_Object = MibTableColumn
ccasGrpLineCfgSupDisconnect = _CcasGrpLineCfgSupDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 3, 1, 1, 2),
    _CcasGrpLineCfgSupDisconnect_Type()
)
ccasGrpLineCfgSupDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasGrpLineCfgSupDisconnect.setStatus("current")


class _CcasGrpLineCfgDialType_Type(Integer32):
    """Custom type ccasGrpLineCfgDialType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dtmf", 1),
          ("pulse", 2))
    )


_CcasGrpLineCfgDialType_Type.__name__ = "Integer32"
_CcasGrpLineCfgDialType_Object = MibTableColumn
ccasGrpLineCfgDialType = _CcasGrpLineCfgDialType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 3, 1, 1, 3),
    _CcasGrpLineCfgDialType_Type()
)
ccasGrpLineCfgDialType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasGrpLineCfgDialType.setStatus("current")
_CcasGrpLineTmTable_Object = MibTable
ccasGrpLineTmTable = _CcasGrpLineTmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    ccasGrpLineTmTable.setStatus("current")
_CcasGrpLineTmEntry_Object = MibTableRow
ccasGrpLineTmEntry = _CcasGrpLineTmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    ccasGrpLineTmEntry.setStatus("current")


class _CcasGrpLineTmDigitDuration_Type(Integer32):
    """Custom type ccasGrpLineTmDigitDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 500),
    )


_CcasGrpLineTmDigitDuration_Type.__name__ = "Integer32"
_CcasGrpLineTmDigitDuration_Object = MibTableColumn
ccasGrpLineTmDigitDuration = _CcasGrpLineTmDigitDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 3, 2, 1, 1),
    _CcasGrpLineTmDigitDuration_Type()
)
ccasGrpLineTmDigitDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasGrpLineTmDigitDuration.setStatus("current")
if mibBuilder.loadTexts:
    ccasGrpLineTmDigitDuration.setUnits("milliseconds")


class _CcasGrpLineTmInterDigitDuration_Type(Integer32):
    """Custom type ccasGrpLineTmInterDigitDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 500),
    )


_CcasGrpLineTmInterDigitDuration_Type.__name__ = "Integer32"
_CcasGrpLineTmInterDigitDuration_Object = MibTableColumn
ccasGrpLineTmInterDigitDuration = _CcasGrpLineTmInterDigitDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 3, 2, 1, 2),
    _CcasGrpLineTmInterDigitDuration_Type()
)
ccasGrpLineTmInterDigitDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasGrpLineTmInterDigitDuration.setStatus("current")
if mibBuilder.loadTexts:
    ccasGrpLineTmInterDigitDuration.setUnits("milliseconds")


class _CcasGrpLineTmPulseRate_Type(Integer32):
    """Custom type ccasGrpLineTmPulseRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 20),
    )


_CcasGrpLineTmPulseRate_Type.__name__ = "Integer32"
_CcasGrpLineTmPulseRate_Object = MibTableColumn
ccasGrpLineTmPulseRate = _CcasGrpLineTmPulseRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 3, 2, 1, 3),
    _CcasGrpLineTmPulseRate_Type()
)
ccasGrpLineTmPulseRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasGrpLineTmPulseRate.setStatus("current")
if mibBuilder.loadTexts:
    ccasGrpLineTmPulseRate.setUnits("pulses per second")


class _CcasGrpLineTmPulseInterDigitDuration_Type(Integer32):
    """Custom type ccasGrpLineTmPulseInterDigitDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_CcasGrpLineTmPulseInterDigitDuration_Type.__name__ = "Integer32"
_CcasGrpLineTmPulseInterDigitDuration_Object = MibTableColumn
ccasGrpLineTmPulseInterDigitDuration = _CcasGrpLineTmPulseInterDigitDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 3, 2, 1, 4),
    _CcasGrpLineTmPulseInterDigitDuration_Type()
)
ccasGrpLineTmPulseInterDigitDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasGrpLineTmPulseInterDigitDuration.setStatus("current")
if mibBuilder.loadTexts:
    ccasGrpLineTmPulseInterDigitDuration.setUnits("milliseconds")
_CcasGrpStaObjects_ObjectIdentity = ObjectIdentity
ccasGrpStaObjects = _CcasGrpStaObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 4)
)
_CcasGrpStaCfgTable_Object = MibTable
ccasGrpStaCfgTable = _CcasGrpStaCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    ccasGrpStaCfgTable.setStatus("current")
_CcasGrpStaCfgEntry_Object = MibTableRow
ccasGrpStaCfgEntry = _CcasGrpStaCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 4, 1, 1)
)
ccasGrpStaCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CAS-IF-MIB", "ccasGrpCfgIndex"),
)
if mibBuilder.loadTexts:
    ccasGrpStaCfgEntry.setStatus("current")


class _CcasGrpStaCfgNumberRings_Type(Integer32):
    """Custom type ccasGrpStaCfgNumberRings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CcasGrpStaCfgNumberRings_Type.__name__ = "Integer32"
_CcasGrpStaCfgNumberRings_Object = MibTableColumn
ccasGrpStaCfgNumberRings = _CcasGrpStaCfgNumberRings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 4, 1, 1, 1),
    _CcasGrpStaCfgNumberRings_Type()
)
ccasGrpStaCfgNumberRings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasGrpStaCfgNumberRings.setStatus("current")
if mibBuilder.loadTexts:
    ccasGrpStaCfgNumberRings.setUnits("rings")


class _CcasGrpStaCfgDialType_Type(Integer32):
    """Custom type ccasGrpStaCfgDialType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dtmf", 1),
          ("pulse", 2))
    )


_CcasGrpStaCfgDialType_Type.__name__ = "Integer32"
_CcasGrpStaCfgDialType_Object = MibTableColumn
ccasGrpStaCfgDialType = _CcasGrpStaCfgDialType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 4, 1, 1, 2),
    _CcasGrpStaCfgDialType_Type()
)
ccasGrpStaCfgDialType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasGrpStaCfgDialType.setStatus("current")
_CcasGrpStaTmTable_Object = MibTable
ccasGrpStaTmTable = _CcasGrpStaTmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    ccasGrpStaTmTable.setStatus("current")
_CcasGrpStaTmEntry_Object = MibTableRow
ccasGrpStaTmEntry = _CcasGrpStaTmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    ccasGrpStaTmEntry.setStatus("current")


class _CcasGrpStaTmDigitDuration_Type(Integer32):
    """Custom type ccasGrpStaTmDigitDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 500),
    )


_CcasGrpStaTmDigitDuration_Type.__name__ = "Integer32"
_CcasGrpStaTmDigitDuration_Object = MibTableColumn
ccasGrpStaTmDigitDuration = _CcasGrpStaTmDigitDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 4, 2, 1, 1),
    _CcasGrpStaTmDigitDuration_Type()
)
ccasGrpStaTmDigitDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasGrpStaTmDigitDuration.setStatus("current")
if mibBuilder.loadTexts:
    ccasGrpStaTmDigitDuration.setUnits("milliseconds")


class _CcasGrpStaTmInterDigitDuration_Type(Integer32):
    """Custom type ccasGrpStaTmInterDigitDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 500),
    )


_CcasGrpStaTmInterDigitDuration_Type.__name__ = "Integer32"
_CcasGrpStaTmInterDigitDuration_Object = MibTableColumn
ccasGrpStaTmInterDigitDuration = _CcasGrpStaTmInterDigitDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 4, 2, 1, 2),
    _CcasGrpStaTmInterDigitDuration_Type()
)
ccasGrpStaTmInterDigitDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasGrpStaTmInterDigitDuration.setStatus("current")
if mibBuilder.loadTexts:
    ccasGrpStaTmInterDigitDuration.setUnits("milliseconds")


class _CcasGrpStaTmPulseRate_Type(Integer32):
    """Custom type ccasGrpStaTmPulseRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 20),
    )


_CcasGrpStaTmPulseRate_Type.__name__ = "Integer32"
_CcasGrpStaTmPulseRate_Object = MibTableColumn
ccasGrpStaTmPulseRate = _CcasGrpStaTmPulseRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 4, 2, 1, 3),
    _CcasGrpStaTmPulseRate_Type()
)
ccasGrpStaTmPulseRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasGrpStaTmPulseRate.setStatus("current")
if mibBuilder.loadTexts:
    ccasGrpStaTmPulseRate.setUnits("pulses per second")


class _CcasGrpStaTmPulseInterDigitDuration_Type(Integer32):
    """Custom type ccasGrpStaTmPulseInterDigitDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_CcasGrpStaTmPulseInterDigitDuration_Type.__name__ = "Integer32"
_CcasGrpStaTmPulseInterDigitDuration_Object = MibTableColumn
ccasGrpStaTmPulseInterDigitDuration = _CcasGrpStaTmPulseInterDigitDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 4, 2, 1, 4),
    _CcasGrpStaTmPulseInterDigitDuration_Type()
)
ccasGrpStaTmPulseInterDigitDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasGrpStaTmPulseInterDigitDuration.setStatus("current")
if mibBuilder.loadTexts:
    ccasGrpStaTmPulseInterDigitDuration.setUnits("milliseconds")
_CcasGrpABCDObjects_ObjectIdentity = ObjectIdentity
ccasGrpABCDObjects = _CcasGrpABCDObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 5)
)
_CcasGrpABCDCfgTable_Object = MibTable
ccasGrpABCDCfgTable = _CcasGrpABCDCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    ccasGrpABCDCfgTable.setStatus("current")
_CcasGrpABCDCfgEntry_Object = MibTableRow
ccasGrpABCDCfgEntry = _CcasGrpABCDCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 5, 1, 1)
)
ccasGrpABCDCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CAS-IF-MIB", "ccasGrpCfgIndex"),
)
if mibBuilder.loadTexts:
    ccasGrpABCDCfgEntry.setStatus("current")


class _CcasGrpABCDCfgInvertBits_Type(Bits):
    """Custom type ccasGrpABCDCfgInvertBits based on Bits"""
    namedValues = NamedValues(
        *(("aBit", 3),
          ("bBit", 2),
          ("cBit", 1),
          ("dBit", 0))
    )

_CcasGrpABCDCfgInvertBits_Type.__name__ = "Bits"
_CcasGrpABCDCfgInvertBits_Object = MibTableColumn
ccasGrpABCDCfgInvertBits = _CcasGrpABCDCfgInvertBits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 5, 1, 1, 1),
    _CcasGrpABCDCfgInvertBits_Type()
)
ccasGrpABCDCfgInvertBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasGrpABCDCfgInvertBits.setStatus("current")


class _CcasGrpABCDCfgUnusedBits_Type(Bits):
    """Custom type ccasGrpABCDCfgUnusedBits based on Bits"""
    namedValues = NamedValues(
        *(("aBit", 3),
          ("bBit", 2),
          ("cBit", 1),
          ("dBit", 0))
    )

_CcasGrpABCDCfgUnusedBits_Type.__name__ = "Bits"
_CcasGrpABCDCfgUnusedBits_Object = MibTableColumn
ccasGrpABCDCfgUnusedBits = _CcasGrpABCDCfgUnusedBits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 2, 5, 1, 1, 2),
    _CcasGrpABCDCfgUnusedBits_Type()
)
ccasGrpABCDCfgUnusedBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasGrpABCDCfgUnusedBits.setStatus("current")
_CcasChannelObjects_ObjectIdentity = ObjectIdentity
ccasChannelObjects = _CcasChannelObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 3)
)
_CcasChannelCfgTable_Object = MibTable
ccasChannelCfgTable = _CcasChannelCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ccasChannelCfgTable.setStatus("current")
_CcasChannelCfgEntry_Object = MibTableRow
ccasChannelCfgEntry = _CcasChannelCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 3, 1, 1)
)
ccasChannelCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ccasChannelCfgEntry.setStatus("current")
_CcasChannelCfgDS1IfIndex_Type = InterfaceIndex
_CcasChannelCfgDS1IfIndex_Object = MibTableColumn
ccasChannelCfgDS1IfIndex = _CcasChannelCfgDS1IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 3, 1, 1, 1),
    _CcasChannelCfgDS1IfIndex_Type()
)
ccasChannelCfgDS1IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccasChannelCfgDS1IfIndex.setStatus("current")


class _CcasChannelCfgGroup_Type(Integer32):
    """Custom type ccasChannelCfgGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_CcasChannelCfgGroup_Type.__name__ = "Integer32"
_CcasChannelCfgGroup_Object = MibTableColumn
ccasChannelCfgGroup = _CcasChannelCfgGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 3, 1, 1, 2),
    _CcasChannelCfgGroup_Type()
)
ccasChannelCfgGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccasChannelCfgGroup.setStatus("current")


class _CcasChannelCfgTimeSlot_Type(Integer32):
    """Custom type ccasChannelCfgTimeSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_CcasChannelCfgTimeSlot_Type.__name__ = "Integer32"
_CcasChannelCfgTimeSlot_Object = MibTableColumn
ccasChannelCfgTimeSlot = _CcasChannelCfgTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 3, 1, 1, 3),
    _CcasChannelCfgTimeSlot_Type()
)
ccasChannelCfgTimeSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccasChannelCfgTimeSlot.setStatus("current")
_CcasChannelCfgBusyOut_Type = TruthValue
_CcasChannelCfgBusyOut_Object = MibTableColumn
ccasChannelCfgBusyOut = _CcasChannelCfgBusyOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 3, 1, 1, 4),
    _CcasChannelCfgBusyOut_Type()
)
ccasChannelCfgBusyOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasChannelCfgBusyOut.setStatus("current")
_CcasChannelStatusTable_Object = MibTable
ccasChannelStatusTable = _CcasChannelStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ccasChannelStatusTable.setStatus("current")
_CcasChannelStatusEntry_Object = MibTableRow
ccasChannelStatusEntry = _CcasChannelStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    ccasChannelStatusEntry.setStatus("current")


class _CcasChannelStatusRecvSignalBits_Type(Bits):
    """Custom type ccasChannelStatusRecvSignalBits based on Bits"""
    namedValues = NamedValues(
        *(("aBit", 3),
          ("bBit", 2),
          ("cBit", 1),
          ("dBit", 0))
    )

_CcasChannelStatusRecvSignalBits_Type.__name__ = "Bits"
_CcasChannelStatusRecvSignalBits_Object = MibTableColumn
ccasChannelStatusRecvSignalBits = _CcasChannelStatusRecvSignalBits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 3, 2, 1, 1),
    _CcasChannelStatusRecvSignalBits_Type()
)
ccasChannelStatusRecvSignalBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccasChannelStatusRecvSignalBits.setStatus("current")
_CcasChannelStatusBusyOut_Type = TruthValue
_CcasChannelStatusBusyOut_Object = MibTableColumn
ccasChannelStatusBusyOut = _CcasChannelStatusBusyOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 3, 2, 1, 2),
    _CcasChannelStatusBusyOut_Type()
)
ccasChannelStatusBusyOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccasChannelStatusBusyOut.setStatus("current")


class _CcasChannelStatusInfoType_Type(Integer32):
    """Custom type ccasChannelStatusInfoType based on Integer32"""
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
        *(("audio31", 4),
          ("audio7", 5),
          ("data56", 3),
          ("fax", 7),
          ("modem", 8),
          ("speech", 2),
          ("unknown", 1),
          ("video", 6))
    )


_CcasChannelStatusInfoType_Type.__name__ = "Integer32"
_CcasChannelStatusInfoType_Object = MibTableColumn
ccasChannelStatusInfoType = _CcasChannelStatusInfoType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 3, 2, 1, 3),
    _CcasChannelStatusInfoType_Type()
)
ccasChannelStatusInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccasChannelStatusInfoType.setStatus("current")


class _CcasChannelStatusXmitSignalBits_Type(Bits):
    """Custom type ccasChannelStatusXmitSignalBits based on Bits"""
    namedValues = NamedValues(
        *(("aBit", 3),
          ("bBit", 2),
          ("cBit", 1),
          ("dBit", 0))
    )

_CcasChannelStatusXmitSignalBits_Type.__name__ = "Bits"
_CcasChannelStatusXmitSignalBits_Object = MibTableColumn
ccasChannelStatusXmitSignalBits = _CcasChannelStatusXmitSignalBits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 3, 2, 1, 4),
    _CcasChannelStatusXmitSignalBits_Type()
)
ccasChannelStatusXmitSignalBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccasChannelStatusXmitSignalBits.setStatus("current")
_CcasVoiceCfgObjects_ObjectIdentity = ObjectIdentity
ccasVoiceCfgObjects = _CcasVoiceCfgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 4)
)
_CcasVoiceCfgTable_Object = MibTable
ccasVoiceCfgTable = _CcasVoiceCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ccasVoiceCfgTable.setStatus("current")
_CcasVoiceCfgEntry_Object = MibTableRow
ccasVoiceCfgEntry = _CcasVoiceCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 4, 1, 1)
)
ccasVoiceCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CAS-IF-MIB", "ccasGrpCfgIndex"),
)
if mibBuilder.loadTexts:
    ccasVoiceCfgEntry.setStatus("current")
_CcasVoiceCfgNoiseRegEnable_Type = TruthValue
_CcasVoiceCfgNoiseRegEnable_Object = MibTableColumn
ccasVoiceCfgNoiseRegEnable = _CcasVoiceCfgNoiseRegEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 4, 1, 1, 1),
    _CcasVoiceCfgNoiseRegEnable_Type()
)
ccasVoiceCfgNoiseRegEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasVoiceCfgNoiseRegEnable.setStatus("current")
_CcasVoiceCfgNonLinearProcEnable_Type = TruthValue
_CcasVoiceCfgNonLinearProcEnable_Object = MibTableColumn
ccasVoiceCfgNonLinearProcEnable = _CcasVoiceCfgNonLinearProcEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 4, 1, 1, 2),
    _CcasVoiceCfgNonLinearProcEnable_Type()
)
ccasVoiceCfgNonLinearProcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasVoiceCfgNonLinearProcEnable.setStatus("current")


class _CcasVoiceCfgMusicOnHoldThreshold_Type(Integer32):
    """Custom type ccasVoiceCfgMusicOnHoldThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-70, -30),
    )


_CcasVoiceCfgMusicOnHoldThreshold_Type.__name__ = "Integer32"
_CcasVoiceCfgMusicOnHoldThreshold_Object = MibTableColumn
ccasVoiceCfgMusicOnHoldThreshold = _CcasVoiceCfgMusicOnHoldThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 4, 1, 1, 3),
    _CcasVoiceCfgMusicOnHoldThreshold_Type()
)
ccasVoiceCfgMusicOnHoldThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasVoiceCfgMusicOnHoldThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ccasVoiceCfgMusicOnHoldThreshold.setUnits("dBm")


class _CcasVoiceCfgInGain_Type(Integer32):
    """Custom type ccasVoiceCfgInGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-6, 14),
    )


_CcasVoiceCfgInGain_Type.__name__ = "Integer32"
_CcasVoiceCfgInGain_Object = MibTableColumn
ccasVoiceCfgInGain = _CcasVoiceCfgInGain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 4, 1, 1, 4),
    _CcasVoiceCfgInGain_Type()
)
ccasVoiceCfgInGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasVoiceCfgInGain.setStatus("current")
if mibBuilder.loadTexts:
    ccasVoiceCfgInGain.setUnits("dB")


class _CcasVoiceCfgOutAttn_Type(Integer32):
    """Custom type ccasVoiceCfgOutAttn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_CcasVoiceCfgOutAttn_Type.__name__ = "Integer32"
_CcasVoiceCfgOutAttn_Object = MibTableColumn
ccasVoiceCfgOutAttn = _CcasVoiceCfgOutAttn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 4, 1, 1, 5),
    _CcasVoiceCfgOutAttn_Type()
)
ccasVoiceCfgOutAttn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasVoiceCfgOutAttn.setStatus("current")
if mibBuilder.loadTexts:
    ccasVoiceCfgOutAttn.setUnits("dB")
_CcasVoiceCfgEchoCancelEnable_Type = TruthValue
_CcasVoiceCfgEchoCancelEnable_Object = MibTableColumn
ccasVoiceCfgEchoCancelEnable = _CcasVoiceCfgEchoCancelEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 4, 1, 1, 6),
    _CcasVoiceCfgEchoCancelEnable_Type()
)
ccasVoiceCfgEchoCancelEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasVoiceCfgEchoCancelEnable.setStatus("current")


class _CcasVoiceCfgEchoCancelCoverage_Type(Integer32):
    """Custom type ccasVoiceCfgEchoCancelCoverage based on Integer32"""
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
        *(("echoCanceller128ms", 6),
          ("echoCanceller16ms", 2),
          ("echoCanceller24ms", 3),
          ("echoCanceller32ms", 4),
          ("echoCanceller64ms", 5),
          ("echoCanceller8ms", 1))
    )


_CcasVoiceCfgEchoCancelCoverage_Type.__name__ = "Integer32"
_CcasVoiceCfgEchoCancelCoverage_Object = MibTableColumn
ccasVoiceCfgEchoCancelCoverage = _CcasVoiceCfgEchoCancelCoverage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 4, 1, 1, 7),
    _CcasVoiceCfgEchoCancelCoverage_Type()
)
ccasVoiceCfgEchoCancelCoverage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasVoiceCfgEchoCancelCoverage.setStatus("current")


class _CcasVoiceCfgConnectionMode_Type(Integer32):
    """Custom type ccasVoiceCfgConnectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("plar", 3),
          ("trunk", 2))
    )


_CcasVoiceCfgConnectionMode_Type.__name__ = "Integer32"
_CcasVoiceCfgConnectionMode_Object = MibTableColumn
ccasVoiceCfgConnectionMode = _CcasVoiceCfgConnectionMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 4, 1, 1, 8),
    _CcasVoiceCfgConnectionMode_Type()
)
ccasVoiceCfgConnectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasVoiceCfgConnectionMode.setStatus("current")


class _CcasVoiceCfgConnectionNumber_Type(DisplayString):
    """Custom type ccasVoiceCfgConnectionNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CcasVoiceCfgConnectionNumber_Type.__name__ = "DisplayString"
_CcasVoiceCfgConnectionNumber_Object = MibTableColumn
ccasVoiceCfgConnectionNumber = _CcasVoiceCfgConnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 4, 1, 1, 9),
    _CcasVoiceCfgConnectionNumber_Type()
)
ccasVoiceCfgConnectionNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasVoiceCfgConnectionNumber.setStatus("current")


class _CcasVoiceCfgInitialDigitTimeOut_Type(Integer32):
    """Custom type ccasVoiceCfgInitialDigitTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_CcasVoiceCfgInitialDigitTimeOut_Type.__name__ = "Integer32"
_CcasVoiceCfgInitialDigitTimeOut_Object = MibTableColumn
ccasVoiceCfgInitialDigitTimeOut = _CcasVoiceCfgInitialDigitTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 4, 1, 1, 10),
    _CcasVoiceCfgInitialDigitTimeOut_Type()
)
ccasVoiceCfgInitialDigitTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasVoiceCfgInitialDigitTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    ccasVoiceCfgInitialDigitTimeOut.setUnits("seconds")


class _CcasVoiceCfgInterDigitTimeOut_Type(Integer32):
    """Custom type ccasVoiceCfgInterDigitTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_CcasVoiceCfgInterDigitTimeOut_Type.__name__ = "Integer32"
_CcasVoiceCfgInterDigitTimeOut_Object = MibTableColumn
ccasVoiceCfgInterDigitTimeOut = _CcasVoiceCfgInterDigitTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 4, 1, 1, 11),
    _CcasVoiceCfgInterDigitTimeOut_Type()
)
ccasVoiceCfgInterDigitTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasVoiceCfgInterDigitTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    ccasVoiceCfgInterDigitTimeOut.setUnits("seconds")
_CcasVoiceCfgRegionalTone_Type = CountryCode
_CcasVoiceCfgRegionalTone_Object = MibTableColumn
ccasVoiceCfgRegionalTone = _CcasVoiceCfgRegionalTone_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 4, 1, 1, 12),
    _CcasVoiceCfgRegionalTone_Type()
)
ccasVoiceCfgRegionalTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasVoiceCfgRegionalTone.setStatus("current")
_CcasXgcpCfgObjects_ObjectIdentity = ObjectIdentity
ccasXgcpCfgObjects = _CcasXgcpCfgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 5)
)
_CcasXgcpCfgTable_Object = MibTable
ccasXgcpCfgTable = _CcasXgcpCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ccasXgcpCfgTable.setStatus("current")
_CcasXgcpCfgEntry_Object = MibTableRow
ccasXgcpCfgEntry = _CcasXgcpCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 5, 1, 1)
)
ccasXgcpCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CAS-IF-MIB", "ccasGrpCfgIndex"),
)
if mibBuilder.loadTexts:
    ccasXgcpCfgEntry.setStatus("current")


class _CcasXgcpCfgCotToneCo1_Type(Integer32):
    """Custom type ccasXgcpCfgCotToneCo1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(280, 3800),
    )


_CcasXgcpCfgCotToneCo1_Type.__name__ = "Integer32"
_CcasXgcpCfgCotToneCo1_Object = MibTableColumn
ccasXgcpCfgCotToneCo1 = _CcasXgcpCfgCotToneCo1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 5, 1, 1, 1),
    _CcasXgcpCfgCotToneCo1_Type()
)
ccasXgcpCfgCotToneCo1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasXgcpCfgCotToneCo1.setStatus("current")
if mibBuilder.loadTexts:
    ccasXgcpCfgCotToneCo1.setUnits("hertz")


class _CcasXgcpCfgCotToneCo2_Type(Integer32):
    """Custom type ccasXgcpCfgCotToneCo2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(280, 3800),
    )


_CcasXgcpCfgCotToneCo2_Type.__name__ = "Integer32"
_CcasXgcpCfgCotToneCo2_Object = MibTableColumn
ccasXgcpCfgCotToneCo2 = _CcasXgcpCfgCotToneCo2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 1, 5, 1, 1, 2),
    _CcasXgcpCfgCotToneCo2_Type()
)
ccasXgcpCfgCotToneCo2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasXgcpCfgCotToneCo2.setStatus("current")
if mibBuilder.loadTexts:
    ccasXgcpCfgCotToneCo2.setUnits("hertz")
_CcasIfMIBConformance_ObjectIdentity = ObjectIdentity
ccasIfMIBConformance = _CcasIfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 3)
)
_CcasIfMIBCompliances_ObjectIdentity = ObjectIdentity
ccasIfMIBCompliances = _CcasIfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 3, 1)
)
_CcasIfMIBGroups_ObjectIdentity = ObjectIdentity
ccasIfMIBGroups = _CcasIfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 3, 2)
)
ccasGrpEMCfgEntry.registerAugmentions(
    ("CISCO-CAS-IF-MIB",
     "ccasGrpEMTmEntry")
)
ccasGrpEMTmEntry.setIndexNames(*ccasGrpEMCfgEntry.getIndexNames())
ccasGrpLineCfgEntry.registerAugmentions(
    ("CISCO-CAS-IF-MIB",
     "ccasGrpLineTmEntry")
)
ccasGrpLineTmEntry.setIndexNames(*ccasGrpLineCfgEntry.getIndexNames())
ccasGrpStaCfgEntry.registerAugmentions(
    ("CISCO-CAS-IF-MIB",
     "ccasGrpStaTmEntry")
)
ccasGrpStaTmEntry.setIndexNames(*ccasGrpStaCfgEntry.getIndexNames())
ccasChannelCfgEntry.registerAugmentions(
    ("CISCO-CAS-IF-MIB",
     "ccasChannelStatusEntry")
)
ccasChannelStatusEntry.setIndexNames(*ccasChannelCfgEntry.getIndexNames())

# Managed Objects groups

ccasIfDS1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 3, 2, 1)
)
ccasIfDS1Group.setObjects(
    ("CISCO-CAS-IF-MIB", "ccasDs1IfCfgDs0ChannelsConfigurable")
)
if mibBuilder.loadTexts:
    ccasIfDS1Group.setStatus("current")

ccasGeneralInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 3, 2, 2)
)
ccasGeneralInfoGroup.setObjects(
      *(("CISCO-CAS-IF-MIB", "ccasGrpCfgType"),
        ("CISCO-CAS-IF-MIB", "ccasGrpCfgDs0Channels"),
        ("CISCO-CAS-IF-MIB", "ccasGrpCfgRowStatus"),
        ("CISCO-CAS-IF-MIB", "ccasChannelCfgDS1IfIndex"),
        ("CISCO-CAS-IF-MIB", "ccasChannelCfgGroup"),
        ("CISCO-CAS-IF-MIB", "ccasChannelCfgTimeSlot"),
        ("CISCO-CAS-IF-MIB", "ccasChannelCfgBusyOut"),
        ("CISCO-CAS-IF-MIB", "ccasChannelStatusRecvSignalBits"),
        ("CISCO-CAS-IF-MIB", "ccasChannelStatusBusyOut"),
        ("CISCO-CAS-IF-MIB", "ccasChannelStatusInfoType"),
        ("CISCO-CAS-IF-MIB", "ccasChannelStatusXmitSignalBits"))
)
if mibBuilder.loadTexts:
    ccasGeneralInfoGroup.setStatus("obsolete")

ccasEMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 3, 2, 3)
)
ccasEMGroup.setObjects(
      *(("CISCO-CAS-IF-MIB", "ccasGrpEMCfgDialType"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMCfgDnisAni"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMTmClearWaitDuration"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMTmMaxWinkWaitDuration"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMTmMaxWinkDuration"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMTmDelayStart"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMTmMaxDelayDuration"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMTmMinDelayPulseWidth"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMTmDigitDuration"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMTmInterDigitDuration"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMTmPulseRate"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMTmPulseInterDigitDuration"))
)
if mibBuilder.loadTexts:
    ccasEMGroup.setStatus("deprecated")

ccasLineGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 3, 2, 4)
)
ccasLineGroup.setObjects(
      *(("CISCO-CAS-IF-MIB", "ccasGrpLineCfgNumberRings"),
        ("CISCO-CAS-IF-MIB", "ccasGrpLineCfgSupDisconnect"),
        ("CISCO-CAS-IF-MIB", "ccasGrpLineCfgDialType"),
        ("CISCO-CAS-IF-MIB", "ccasGrpLineTmDigitDuration"),
        ("CISCO-CAS-IF-MIB", "ccasGrpLineTmInterDigitDuration"),
        ("CISCO-CAS-IF-MIB", "ccasGrpLineTmPulseRate"),
        ("CISCO-CAS-IF-MIB", "ccasGrpLineTmPulseInterDigitDuration"))
)
if mibBuilder.loadTexts:
    ccasLineGroup.setStatus("current")

ccasStaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 3, 2, 5)
)
ccasStaGroup.setObjects(
      *(("CISCO-CAS-IF-MIB", "ccasGrpStaCfgNumberRings"),
        ("CISCO-CAS-IF-MIB", "ccasGrpStaCfgDialType"),
        ("CISCO-CAS-IF-MIB", "ccasGrpStaTmDigitDuration"),
        ("CISCO-CAS-IF-MIB", "ccasGrpStaTmInterDigitDuration"),
        ("CISCO-CAS-IF-MIB", "ccasGrpStaTmPulseRate"),
        ("CISCO-CAS-IF-MIB", "ccasGrpStaTmPulseInterDigitDuration"))
)
if mibBuilder.loadTexts:
    ccasStaGroup.setStatus("current")

ccasCustomABCDGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 3, 2, 6)
)
ccasCustomABCDGroup.setObjects(
      *(("CISCO-CAS-IF-MIB", "ccasGrpABCDCfgInvertBits"),
        ("CISCO-CAS-IF-MIB", "ccasGrpABCDCfgUnusedBits"))
)
if mibBuilder.loadTexts:
    ccasCustomABCDGroup.setStatus("current")

ccasVoiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 3, 2, 7)
)
ccasVoiceGroup.setObjects(
      *(("CISCO-CAS-IF-MIB", "ccasVoiceCfgNoiseRegEnable"),
        ("CISCO-CAS-IF-MIB", "ccasVoiceCfgNonLinearProcEnable"),
        ("CISCO-CAS-IF-MIB", "ccasVoiceCfgMusicOnHoldThreshold"),
        ("CISCO-CAS-IF-MIB", "ccasVoiceCfgInGain"),
        ("CISCO-CAS-IF-MIB", "ccasVoiceCfgOutAttn"),
        ("CISCO-CAS-IF-MIB", "ccasVoiceCfgEchoCancelEnable"),
        ("CISCO-CAS-IF-MIB", "ccasVoiceCfgEchoCancelCoverage"),
        ("CISCO-CAS-IF-MIB", "ccasVoiceCfgConnectionMode"),
        ("CISCO-CAS-IF-MIB", "ccasVoiceCfgConnectionNumber"),
        ("CISCO-CAS-IF-MIB", "ccasVoiceCfgInitialDigitTimeOut"),
        ("CISCO-CAS-IF-MIB", "ccasVoiceCfgInterDigitTimeOut"),
        ("CISCO-CAS-IF-MIB", "ccasVoiceCfgRegionalTone"))
)
if mibBuilder.loadTexts:
    ccasVoiceGroup.setStatus("current")

ccasGeneralInfoGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 3, 2, 8)
)
ccasGeneralInfoGroupRev1.setObjects(
      *(("CISCO-CAS-IF-MIB", "ccasGrpCfgType"),
        ("CISCO-CAS-IF-MIB", "ccasGrpCfgDs0Channels"),
        ("CISCO-CAS-IF-MIB", "ccasGrpCfgServiceType"),
        ("CISCO-CAS-IF-MIB", "ccasGrpCfgRowStatus"))
)
if mibBuilder.loadTexts:
    ccasGeneralInfoGroupRev1.setStatus("current")

ccasChannelInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 3, 2, 9)
)
ccasChannelInfoGroup.setObjects(
      *(("CISCO-CAS-IF-MIB", "ccasChannelCfgDS1IfIndex"),
        ("CISCO-CAS-IF-MIB", "ccasChannelCfgGroup"),
        ("CISCO-CAS-IF-MIB", "ccasChannelCfgTimeSlot"),
        ("CISCO-CAS-IF-MIB", "ccasChannelCfgBusyOut"),
        ("CISCO-CAS-IF-MIB", "ccasChannelStatusRecvSignalBits"),
        ("CISCO-CAS-IF-MIB", "ccasChannelStatusBusyOut"),
        ("CISCO-CAS-IF-MIB", "ccasChannelStatusInfoType"),
        ("CISCO-CAS-IF-MIB", "ccasChannelStatusXmitSignalBits"))
)
if mibBuilder.loadTexts:
    ccasChannelInfoGroup.setStatus("current")

ccasXgcpCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 3, 2, 10)
)
ccasXgcpCfgGroup.setObjects(
      *(("CISCO-CAS-IF-MIB", "ccasXgcpCfgCotToneCo1"),
        ("CISCO-CAS-IF-MIB", "ccasXgcpCfgCotToneCo2"))
)
if mibBuilder.loadTexts:
    ccasXgcpCfgGroup.setStatus("current")

ccasEMGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 3, 2, 11)
)
ccasEMGroupRev1.setObjects(
      *(("CISCO-CAS-IF-MIB", "ccasGrpEMCfgDialType"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMCfgDnisAni"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMTmClearWaitDuration"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMTmMaxWinkWaitDuration"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMTmMaxWinkDuration"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMTmDelayStart"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMTmMaxDelayDuration"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMTmMinDelayPulseWidth"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMTmDigitDuration"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMTmInterDigitDuration"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMTmPulseRate"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMTmPulseInterDigitDuration"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMCfgLmrMCap"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMCfgLmrECap"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMTmVoiceHangover"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMTmLmrTeardown"))
)
if mibBuilder.loadTexts:
    ccasEMGroupRev1.setStatus("deprecated")

ccasEMGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 3, 2, 12)
)
ccasEMGroupRev2.setObjects(
      *(("CISCO-CAS-IF-MIB", "ccasGrpEMCfgDialType"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMCfgDnisAni"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMTmClearWaitDuration"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMTmMaxWinkWaitDuration"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMTmMaxWinkDuration"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMTmDelayStart"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMTmMaxDelayDuration"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMTmMinDelayPulseWidth"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMTmDigitDuration"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMTmInterDigitDuration"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMTmPulseRate"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMTmPulseInterDigitDuration"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMCfgLmrMCap"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMCfgLmrECap"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMTmVoiceHangover"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMTmLmrTeardown"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMCfgAutoGainControl"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMTmPttXmt"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMTmPttRcv"),
        ("CISCO-CAS-IF-MIB", "ccasGrpEMTmDelayVoice"))
)
if mibBuilder.loadTexts:
    ccasEMGroupRev2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ccasIfMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ccasIfMIBCompliance.setStatus(
        "obsolete"
    )

ccasIfMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ccasIfMIBComplianceRev1.setStatus(
        "deprecated"
    )

ccasIfMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ccasIfMIBComplianceRev2.setStatus(
        "deprecated"
    )

ccasIfMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 85, 3, 1, 4)
)
if mibBuilder.loadTexts:
    ccasIfMIBComplianceRev3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CAS-IF-MIB",
    **{"ciscoCasIfMIB": ciscoCasIfMIB,
       "ccasIfObjects": ccasIfObjects,
       "ccasDS1Objects": ccasDS1Objects,
       "ccasDs1IfCfgTable": ccasDs1IfCfgTable,
       "ccasDs1IfCfgEntry": ccasDs1IfCfgEntry,
       "ccasDs1IfCfgDs0ChannelsConfigurable": ccasDs1IfCfgDs0ChannelsConfigurable,
       "ccasGrpObjects": ccasGrpObjects,
       "ccasGrpGeneralObjects": ccasGrpGeneralObjects,
       "ccasGrpCfgTable": ccasGrpCfgTable,
       "ccasGrpCfgEntry": ccasGrpCfgEntry,
       "ccasGrpCfgIndex": ccasGrpCfgIndex,
       "ccasGrpCfgType": ccasGrpCfgType,
       "ccasGrpCfgDs0Channels": ccasGrpCfgDs0Channels,
       "ccasGrpCfgRowStatus": ccasGrpCfgRowStatus,
       "ccasGrpCfgServiceType": ccasGrpCfgServiceType,
       "ccasGrpEMObjects": ccasGrpEMObjects,
       "ccasGrpEMCfgTable": ccasGrpEMCfgTable,
       "ccasGrpEMCfgEntry": ccasGrpEMCfgEntry,
       "ccasGrpEMCfgDialType": ccasGrpEMCfgDialType,
       "ccasGrpEMCfgDnisAni": ccasGrpEMCfgDnisAni,
       "ccasGrpEMCfgLmrMCap": ccasGrpEMCfgLmrMCap,
       "ccasGrpEMCfgLmrECap": ccasGrpEMCfgLmrECap,
       "ccasGrpEMCfgAutoGainControl": ccasGrpEMCfgAutoGainControl,
       "ccasGrpEMTmTable": ccasGrpEMTmTable,
       "ccasGrpEMTmEntry": ccasGrpEMTmEntry,
       "ccasGrpEMTmClearWaitDuration": ccasGrpEMTmClearWaitDuration,
       "ccasGrpEMTmMaxWinkWaitDuration": ccasGrpEMTmMaxWinkWaitDuration,
       "ccasGrpEMTmMaxWinkDuration": ccasGrpEMTmMaxWinkDuration,
       "ccasGrpEMTmDelayStart": ccasGrpEMTmDelayStart,
       "ccasGrpEMTmMaxDelayDuration": ccasGrpEMTmMaxDelayDuration,
       "ccasGrpEMTmMinDelayPulseWidth": ccasGrpEMTmMinDelayPulseWidth,
       "ccasGrpEMTmDigitDuration": ccasGrpEMTmDigitDuration,
       "ccasGrpEMTmInterDigitDuration": ccasGrpEMTmInterDigitDuration,
       "ccasGrpEMTmPulseRate": ccasGrpEMTmPulseRate,
       "ccasGrpEMTmPulseInterDigitDuration": ccasGrpEMTmPulseInterDigitDuration,
       "ccasGrpEMTmVoiceHangover": ccasGrpEMTmVoiceHangover,
       "ccasGrpEMTmLmrTeardown": ccasGrpEMTmLmrTeardown,
       "ccasGrpEMTmPttXmt": ccasGrpEMTmPttXmt,
       "ccasGrpEMTmPttRcv": ccasGrpEMTmPttRcv,
       "ccasGrpEMTmDelayVoice": ccasGrpEMTmDelayVoice,
       "ccasGrpLineObjects": ccasGrpLineObjects,
       "ccasGrpLineCfgTable": ccasGrpLineCfgTable,
       "ccasGrpLineCfgEntry": ccasGrpLineCfgEntry,
       "ccasGrpLineCfgNumberRings": ccasGrpLineCfgNumberRings,
       "ccasGrpLineCfgSupDisconnect": ccasGrpLineCfgSupDisconnect,
       "ccasGrpLineCfgDialType": ccasGrpLineCfgDialType,
       "ccasGrpLineTmTable": ccasGrpLineTmTable,
       "ccasGrpLineTmEntry": ccasGrpLineTmEntry,
       "ccasGrpLineTmDigitDuration": ccasGrpLineTmDigitDuration,
       "ccasGrpLineTmInterDigitDuration": ccasGrpLineTmInterDigitDuration,
       "ccasGrpLineTmPulseRate": ccasGrpLineTmPulseRate,
       "ccasGrpLineTmPulseInterDigitDuration": ccasGrpLineTmPulseInterDigitDuration,
       "ccasGrpStaObjects": ccasGrpStaObjects,
       "ccasGrpStaCfgTable": ccasGrpStaCfgTable,
       "ccasGrpStaCfgEntry": ccasGrpStaCfgEntry,
       "ccasGrpStaCfgNumberRings": ccasGrpStaCfgNumberRings,
       "ccasGrpStaCfgDialType": ccasGrpStaCfgDialType,
       "ccasGrpStaTmTable": ccasGrpStaTmTable,
       "ccasGrpStaTmEntry": ccasGrpStaTmEntry,
       "ccasGrpStaTmDigitDuration": ccasGrpStaTmDigitDuration,
       "ccasGrpStaTmInterDigitDuration": ccasGrpStaTmInterDigitDuration,
       "ccasGrpStaTmPulseRate": ccasGrpStaTmPulseRate,
       "ccasGrpStaTmPulseInterDigitDuration": ccasGrpStaTmPulseInterDigitDuration,
       "ccasGrpABCDObjects": ccasGrpABCDObjects,
       "ccasGrpABCDCfgTable": ccasGrpABCDCfgTable,
       "ccasGrpABCDCfgEntry": ccasGrpABCDCfgEntry,
       "ccasGrpABCDCfgInvertBits": ccasGrpABCDCfgInvertBits,
       "ccasGrpABCDCfgUnusedBits": ccasGrpABCDCfgUnusedBits,
       "ccasChannelObjects": ccasChannelObjects,
       "ccasChannelCfgTable": ccasChannelCfgTable,
       "ccasChannelCfgEntry": ccasChannelCfgEntry,
       "ccasChannelCfgDS1IfIndex": ccasChannelCfgDS1IfIndex,
       "ccasChannelCfgGroup": ccasChannelCfgGroup,
       "ccasChannelCfgTimeSlot": ccasChannelCfgTimeSlot,
       "ccasChannelCfgBusyOut": ccasChannelCfgBusyOut,
       "ccasChannelStatusTable": ccasChannelStatusTable,
       "ccasChannelStatusEntry": ccasChannelStatusEntry,
       "ccasChannelStatusRecvSignalBits": ccasChannelStatusRecvSignalBits,
       "ccasChannelStatusBusyOut": ccasChannelStatusBusyOut,
       "ccasChannelStatusInfoType": ccasChannelStatusInfoType,
       "ccasChannelStatusXmitSignalBits": ccasChannelStatusXmitSignalBits,
       "ccasVoiceCfgObjects": ccasVoiceCfgObjects,
       "ccasVoiceCfgTable": ccasVoiceCfgTable,
       "ccasVoiceCfgEntry": ccasVoiceCfgEntry,
       "ccasVoiceCfgNoiseRegEnable": ccasVoiceCfgNoiseRegEnable,
       "ccasVoiceCfgNonLinearProcEnable": ccasVoiceCfgNonLinearProcEnable,
       "ccasVoiceCfgMusicOnHoldThreshold": ccasVoiceCfgMusicOnHoldThreshold,
       "ccasVoiceCfgInGain": ccasVoiceCfgInGain,
       "ccasVoiceCfgOutAttn": ccasVoiceCfgOutAttn,
       "ccasVoiceCfgEchoCancelEnable": ccasVoiceCfgEchoCancelEnable,
       "ccasVoiceCfgEchoCancelCoverage": ccasVoiceCfgEchoCancelCoverage,
       "ccasVoiceCfgConnectionMode": ccasVoiceCfgConnectionMode,
       "ccasVoiceCfgConnectionNumber": ccasVoiceCfgConnectionNumber,
       "ccasVoiceCfgInitialDigitTimeOut": ccasVoiceCfgInitialDigitTimeOut,
       "ccasVoiceCfgInterDigitTimeOut": ccasVoiceCfgInterDigitTimeOut,
       "ccasVoiceCfgRegionalTone": ccasVoiceCfgRegionalTone,
       "ccasXgcpCfgObjects": ccasXgcpCfgObjects,
       "ccasXgcpCfgTable": ccasXgcpCfgTable,
       "ccasXgcpCfgEntry": ccasXgcpCfgEntry,
       "ccasXgcpCfgCotToneCo1": ccasXgcpCfgCotToneCo1,
       "ccasXgcpCfgCotToneCo2": ccasXgcpCfgCotToneCo2,
       "ccasIfMIBConformance": ccasIfMIBConformance,
       "ccasIfMIBCompliances": ccasIfMIBCompliances,
       "ccasIfMIBCompliance": ccasIfMIBCompliance,
       "ccasIfMIBComplianceRev1": ccasIfMIBComplianceRev1,
       "ccasIfMIBComplianceRev2": ccasIfMIBComplianceRev2,
       "ccasIfMIBComplianceRev3": ccasIfMIBComplianceRev3,
       "ccasIfMIBGroups": ccasIfMIBGroups,
       "ccasIfDS1Group": ccasIfDS1Group,
       "ccasGeneralInfoGroup": ccasGeneralInfoGroup,
       "ccasEMGroup": ccasEMGroup,
       "ccasLineGroup": ccasLineGroup,
       "ccasStaGroup": ccasStaGroup,
       "ccasCustomABCDGroup": ccasCustomABCDGroup,
       "ccasVoiceGroup": ccasVoiceGroup,
       "ccasGeneralInfoGroupRev1": ccasGeneralInfoGroupRev1,
       "ccasChannelInfoGroup": ccasChannelInfoGroup,
       "ccasXgcpCfgGroup": ccasXgcpCfgGroup,
       "ccasEMGroupRev1": ccasEMGroupRev1,
       "ccasEMGroupRev2": ccasEMGroupRev2}
)
