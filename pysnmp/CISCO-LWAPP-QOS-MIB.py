# SNMP MIB module (CISCO-LWAPP-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:53 2024
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

(cLApDot11IfEntry,
 cLApDot11IfSlotId,
 cLApDot11IfType,
 cLApName,
 cLApSysMacAddress) = mibBuilder.importSymbols(
    "CISCO-LWAPP-AP-MIB",
    "cLApDot11IfEntry",
    "cLApDot11IfSlotId",
    "cLApDot11IfType",
    "cLApName",
    "cLApSysMacAddress")

(cldcClientMacAddress,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-DOT11-CLIENT-MIB",
    "cldcClientMacAddress")

(cLWlanConfigEntry,
 cLWlanIndex) = mibBuilder.importSymbols(
    "CISCO-LWAPP-WLAN-MIB",
    "cLWlanConfigEntry",
    "cLWlanIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(TimeIntervalSec,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "TimeIntervalSec")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappQosMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524)
)
ciscoLwappQosMIB.setRevisions(
        ("2010-07-21 00:00",
         "2007-01-07 00:00",
         "2006-04-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappQosMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappQosMIBNotifs = _CiscoLwappQosMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 0)
)
_CiscoLwappQosMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappQosMIBObjects = _CiscoLwappQosMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1)
)
_CLQd11aCACConfig_ObjectIdentity = ObjectIdentity
cLQd11aCACConfig = _CLQd11aCACConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1)
)


class _CLQd11aVoiceAdmCtrlSupport_Type(TruthValue):
    """Custom type cLQd11aVoiceAdmCtrlSupport based on TruthValue"""


_CLQd11aVoiceAdmCtrlSupport_Object = MibScalar
cLQd11aVoiceAdmCtrlSupport = _CLQd11aVoiceAdmCtrlSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 1),
    _CLQd11aVoiceAdmCtrlSupport_Type()
)
cLQd11aVoiceAdmCtrlSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11aVoiceAdmCtrlSupport.setStatus("current")


class _CLQd11aVoiceMaxAdmBandwidth_Type(Unsigned32):
    """Custom type cLQd11aVoiceMaxAdmBandwidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CLQd11aVoiceMaxAdmBandwidth_Type.__name__ = "Unsigned32"
_CLQd11aVoiceMaxAdmBandwidth_Object = MibScalar
cLQd11aVoiceMaxAdmBandwidth = _CLQd11aVoiceMaxAdmBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 2),
    _CLQd11aVoiceMaxAdmBandwidth_Type()
)
cLQd11aVoiceMaxAdmBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11aVoiceMaxAdmBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11aVoiceMaxAdmBandwidth.setUnits("Percent")


class _CLQd11aVoiceMaxRoamBandwidth_Type(Unsigned32):
    """Custom type cLQd11aVoiceMaxRoamBandwidth based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CLQd11aVoiceMaxRoamBandwidth_Type.__name__ = "Unsigned32"
_CLQd11aVoiceMaxRoamBandwidth_Object = MibScalar
cLQd11aVoiceMaxRoamBandwidth = _CLQd11aVoiceMaxRoamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 3),
    _CLQd11aVoiceMaxRoamBandwidth_Type()
)
cLQd11aVoiceMaxRoamBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11aVoiceMaxRoamBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11aVoiceMaxRoamBandwidth.setUnits("Percent")


class _CLQd11aVideoAdmCtrlSupport_Type(TruthValue):
    """Custom type cLQd11aVideoAdmCtrlSupport based on TruthValue"""


_CLQd11aVideoAdmCtrlSupport_Object = MibScalar
cLQd11aVideoAdmCtrlSupport = _CLQd11aVideoAdmCtrlSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 4),
    _CLQd11aVideoAdmCtrlSupport_Type()
)
cLQd11aVideoAdmCtrlSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11aVideoAdmCtrlSupport.setStatus("current")


class _CLQd11aVideoMaxAdmBandwidth_Type(Unsigned32):
    """Custom type cLQd11aVideoMaxAdmBandwidth based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CLQd11aVideoMaxAdmBandwidth_Type.__name__ = "Unsigned32"
_CLQd11aVideoMaxAdmBandwidth_Object = MibScalar
cLQd11aVideoMaxAdmBandwidth = _CLQd11aVideoMaxAdmBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 5),
    _CLQd11aVideoMaxAdmBandwidth_Type()
)
cLQd11aVideoMaxAdmBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11aVideoMaxAdmBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11aVideoMaxAdmBandwidth.setUnits("Percent")


class _CLQd11aVideoMaxRoamBandwidth_Type(Unsigned32):
    """Custom type cLQd11aVideoMaxRoamBandwidth based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CLQd11aVideoMaxRoamBandwidth_Type.__name__ = "Unsigned32"
_CLQd11aVideoMaxRoamBandwidth_Object = MibScalar
cLQd11aVideoMaxRoamBandwidth = _CLQd11aVideoMaxRoamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 6),
    _CLQd11aVideoMaxRoamBandwidth_Type()
)
cLQd11aVideoMaxRoamBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11aVideoMaxRoamBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11aVideoMaxRoamBandwidth.setUnits("Percent")


class _CLQd11aGprProbeInterval_Type(Unsigned32):
    """Custom type cLQd11aGprProbeInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_CLQd11aGprProbeInterval_Type.__name__ = "Unsigned32"
_CLQd11aGprProbeInterval_Object = MibScalar
cLQd11aGprProbeInterval = _CLQd11aGprProbeInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 7),
    _CLQd11aGprProbeInterval_Type()
)
cLQd11aGprProbeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11aGprProbeInterval.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11aGprProbeInterval.setUnits("TU")


class _CLQd11aVoiceCtrl_Type(Integer32):
    """Custom type cLQd11aVoiceCtrl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loadBased", 1),
          ("static", 2))
    )


_CLQd11aVoiceCtrl_Type.__name__ = "Integer32"
_CLQd11aVoiceCtrl_Object = MibScalar
cLQd11aVoiceCtrl = _CLQd11aVoiceCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 8),
    _CLQd11aVoiceCtrl_Type()
)
cLQd11aVoiceCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11aVoiceCtrl.setStatus("current")
_CLQd11aExpeditedBw_Type = TruthValue
_CLQd11aExpeditedBw_Object = MibScalar
cLQd11aExpeditedBw = _CLQd11aExpeditedBw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 9),
    _CLQd11aExpeditedBw_Type()
)
cLQd11aExpeditedBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11aExpeditedBw.setStatus("current")


class _CLQd11aEdcaProfile_Type(Integer32):
    """Custom type cLQd11aEdcaProfile based on Integer32"""
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
        *(("optimizedVideoVoice", 4),
          ("optimizedVoice", 3),
          ("svpVoice", 2),
          ("wmmDefault", 1))
    )


_CLQd11aEdcaProfile_Type.__name__ = "Integer32"
_CLQd11aEdcaProfile_Object = MibScalar
cLQd11aEdcaProfile = _CLQd11aEdcaProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 10),
    _CLQd11aEdcaProfile_Type()
)
cLQd11aEdcaProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11aEdcaProfile.setStatus("current")
_CLQd11aMacOptimization_Type = TruthValue
_CLQd11aMacOptimization_Object = MibScalar
cLQd11aMacOptimization = _CLQd11aMacOptimization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 11),
    _CLQd11aMacOptimization_Type()
)
cLQd11aMacOptimization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11aMacOptimization.setStatus("current")
_CLQd11aMaxCallLimit_Type = Unsigned32
_CLQd11aMaxCallLimit_Object = MibScalar
cLQd11aMaxCallLimit = _CLQd11aMaxCallLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 12),
    _CLQd11aMaxCallLimit_Type()
)
cLQd11aMaxCallLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11aMaxCallLimit.setStatus("current")
_CLQd11bCACConfig_ObjectIdentity = ObjectIdentity
cLQd11bCACConfig = _CLQd11bCACConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2)
)


class _CLQd11bVoiceAdmCtrlSupport_Type(TruthValue):
    """Custom type cLQd11bVoiceAdmCtrlSupport based on TruthValue"""


_CLQd11bVoiceAdmCtrlSupport_Object = MibScalar
cLQd11bVoiceAdmCtrlSupport = _CLQd11bVoiceAdmCtrlSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 1),
    _CLQd11bVoiceAdmCtrlSupport_Type()
)
cLQd11bVoiceAdmCtrlSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11bVoiceAdmCtrlSupport.setStatus("current")


class _CLQd11bVoiceMaxAdmBandwidth_Type(Unsigned32):
    """Custom type cLQd11bVoiceMaxAdmBandwidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CLQd11bVoiceMaxAdmBandwidth_Type.__name__ = "Unsigned32"
_CLQd11bVoiceMaxAdmBandwidth_Object = MibScalar
cLQd11bVoiceMaxAdmBandwidth = _CLQd11bVoiceMaxAdmBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 2),
    _CLQd11bVoiceMaxAdmBandwidth_Type()
)
cLQd11bVoiceMaxAdmBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11bVoiceMaxAdmBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11bVoiceMaxAdmBandwidth.setUnits("Percent")


class _CLQd11bVoiceMaxRoamBandwidth_Type(Unsigned32):
    """Custom type cLQd11bVoiceMaxRoamBandwidth based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CLQd11bVoiceMaxRoamBandwidth_Type.__name__ = "Unsigned32"
_CLQd11bVoiceMaxRoamBandwidth_Object = MibScalar
cLQd11bVoiceMaxRoamBandwidth = _CLQd11bVoiceMaxRoamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 3),
    _CLQd11bVoiceMaxRoamBandwidth_Type()
)
cLQd11bVoiceMaxRoamBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11bVoiceMaxRoamBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11bVoiceMaxRoamBandwidth.setUnits("Percent")


class _CLQd11bVideoAdmCtrlSupport_Type(TruthValue):
    """Custom type cLQd11bVideoAdmCtrlSupport based on TruthValue"""


_CLQd11bVideoAdmCtrlSupport_Object = MibScalar
cLQd11bVideoAdmCtrlSupport = _CLQd11bVideoAdmCtrlSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 4),
    _CLQd11bVideoAdmCtrlSupport_Type()
)
cLQd11bVideoAdmCtrlSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11bVideoAdmCtrlSupport.setStatus("current")


class _CLQd11bVideoMaxAdmBandwidth_Type(Unsigned32):
    """Custom type cLQd11bVideoMaxAdmBandwidth based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CLQd11bVideoMaxAdmBandwidth_Type.__name__ = "Unsigned32"
_CLQd11bVideoMaxAdmBandwidth_Object = MibScalar
cLQd11bVideoMaxAdmBandwidth = _CLQd11bVideoMaxAdmBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 5),
    _CLQd11bVideoMaxAdmBandwidth_Type()
)
cLQd11bVideoMaxAdmBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11bVideoMaxAdmBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11bVideoMaxAdmBandwidth.setUnits("Percent")


class _CLQd11bVideoMaxRoamBandwidth_Type(Unsigned32):
    """Custom type cLQd11bVideoMaxRoamBandwidth based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CLQd11bVideoMaxRoamBandwidth_Type.__name__ = "Unsigned32"
_CLQd11bVideoMaxRoamBandwidth_Object = MibScalar
cLQd11bVideoMaxRoamBandwidth = _CLQd11bVideoMaxRoamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 6),
    _CLQd11bVideoMaxRoamBandwidth_Type()
)
cLQd11bVideoMaxRoamBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11bVideoMaxRoamBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11bVideoMaxRoamBandwidth.setUnits("Percent")


class _CLQd11bGprProbeInterval_Type(Unsigned32):
    """Custom type cLQd11bGprProbeInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_CLQd11bGprProbeInterval_Type.__name__ = "Unsigned32"
_CLQd11bGprProbeInterval_Object = MibScalar
cLQd11bGprProbeInterval = _CLQd11bGprProbeInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 7),
    _CLQd11bGprProbeInterval_Type()
)
cLQd11bGprProbeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11bGprProbeInterval.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11bGprProbeInterval.setUnits("TU")


class _CLQd11bVoiceCtrl_Type(Integer32):
    """Custom type cLQd11bVoiceCtrl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loadBased", 1),
          ("static", 2))
    )


_CLQd11bVoiceCtrl_Type.__name__ = "Integer32"
_CLQd11bVoiceCtrl_Object = MibScalar
cLQd11bVoiceCtrl = _CLQd11bVoiceCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 8),
    _CLQd11bVoiceCtrl_Type()
)
cLQd11bVoiceCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11bVoiceCtrl.setStatus("current")
_CLQd11bExpeditedBw_Type = TruthValue
_CLQd11bExpeditedBw_Object = MibScalar
cLQd11bExpeditedBw = _CLQd11bExpeditedBw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 9),
    _CLQd11bExpeditedBw_Type()
)
cLQd11bExpeditedBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11bExpeditedBw.setStatus("current")


class _CLQd11bEdcaProfile_Type(Integer32):
    """Custom type cLQd11bEdcaProfile based on Integer32"""
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
        *(("optimizedVideoVoice", 4),
          ("optimizedVoice", 3),
          ("svpVoice", 2),
          ("wmmDefault", 1))
    )


_CLQd11bEdcaProfile_Type.__name__ = "Integer32"
_CLQd11bEdcaProfile_Object = MibScalar
cLQd11bEdcaProfile = _CLQd11bEdcaProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 10),
    _CLQd11bEdcaProfile_Type()
)
cLQd11bEdcaProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11bEdcaProfile.setStatus("current")
_CLQd11bMacOptimization_Type = TruthValue
_CLQd11bMacOptimization_Object = MibScalar
cLQd11bMacOptimization = _CLQd11bMacOptimization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 11),
    _CLQd11bMacOptimization_Type()
)
cLQd11bMacOptimization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11bMacOptimization.setStatus("current")
_CLQd11bMaxCallLimit_Type = Unsigned32
_CLQd11bMaxCallLimit_Object = MibScalar
cLQd11bMaxCallLimit = _CLQd11bMaxCallLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 12),
    _CLQd11bMaxCallLimit_Type()
)
cLQd11bMaxCallLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11bMaxCallLimit.setStatus("current")
_CLQd11GprConfig_ObjectIdentity = ObjectIdentity
cLQd11GprConfig = _CLQd11GprConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 3)
)
_CLQd11GprTable_Object = MibTable
cLQd11GprTable = _CLQd11GprTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cLQd11GprTable.setStatus("current")
_CLQd11GprEntry_Object = MibTableRow
cLQd11GprEntry = _CLQd11GprEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cLQd11GprEntry.setStatus("current")


class _CLQd11GprSupport_Type(TruthValue):
    """Custom type cLQd11GprSupport based on TruthValue"""


_CLQd11GprSupport_Object = MibTableColumn
cLQd11GprSupport = _CLQd11GprSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 3, 1, 1, 1),
    _CLQd11GprSupport_Type()
)
cLQd11GprSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11GprSupport.setStatus("current")
_CLQd11CACStats_ObjectIdentity = ObjectIdentity
cLQd11CACStats = _CLQd11CACStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4)
)
_CLQd11CACStatsTable_Object = MibTable
cLQd11CACStatsTable = _CLQd11CACStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cLQd11CACStatsTable.setStatus("current")
_CLQd11CACStatsEntry_Object = MibTableRow
cLQd11CACStatsEntry = _CLQd11CACStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    cLQd11CACStatsEntry.setStatus("current")


class _CLQd11CacVoiceBwInUse_Type(Gauge32):
    """Custom type cLQd11CacVoiceBwInUse based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CLQd11CacVoiceBwInUse_Type.__name__ = "Gauge32"
_CLQd11CacVoiceBwInUse_Object = MibTableColumn
cLQd11CacVoiceBwInUse = _CLQd11CacVoiceBwInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 1),
    _CLQd11CacVoiceBwInUse_Type()
)
cLQd11CacVoiceBwInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11CacVoiceBwInUse.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11CacVoiceBwInUse.setUnits("Percent")


class _CLQd11CacVideoBwInUse_Type(Gauge32):
    """Custom type cLQd11CacVideoBwInUse based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CLQd11CacVideoBwInUse_Type.__name__ = "Gauge32"
_CLQd11CacVideoBwInUse_Object = MibTableColumn
cLQd11CacVideoBwInUse = _CLQd11CacVideoBwInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 2),
    _CLQd11CacVideoBwInUse_Type()
)
cLQd11CacVideoBwInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11CacVideoBwInUse.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11CacVideoBwInUse.setUnits("Percent")
_CLQd11CacVoiceCallsInProgress_Type = Gauge32
_CLQd11CacVoiceCallsInProgress_Object = MibTableColumn
cLQd11CacVoiceCallsInProgress = _CLQd11CacVoiceCallsInProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 3),
    _CLQd11CacVoiceCallsInProgress_Type()
)
cLQd11CacVoiceCallsInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11CacVoiceCallsInProgress.setStatus("current")
_CLQd11CacRoamVoiceCallsInProg_Type = Gauge32
_CLQd11CacRoamVoiceCallsInProg_Object = MibTableColumn
cLQd11CacRoamVoiceCallsInProg = _CLQd11CacRoamVoiceCallsInProg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 4),
    _CLQd11CacRoamVoiceCallsInProg_Type()
)
cLQd11CacRoamVoiceCallsInProg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11CacRoamVoiceCallsInProg.setStatus("current")
_CLQd11CacTotalVoiceCallsAP_Type = Counter32
_CLQd11CacTotalVoiceCallsAP_Object = MibTableColumn
cLQd11CacTotalVoiceCallsAP = _CLQd11CacTotalVoiceCallsAP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 5),
    _CLQd11CacTotalVoiceCallsAP_Type()
)
cLQd11CacTotalVoiceCallsAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11CacTotalVoiceCallsAP.setStatus("current")
_CLQd11CacTotalRoamCallsAP_Type = Counter32
_CLQd11CacTotalRoamCallsAP_Object = MibTableColumn
cLQd11CacTotalRoamCallsAP = _CLQd11CacTotalRoamCallsAP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 6),
    _CLQd11CacTotalRoamCallsAP_Type()
)
cLQd11CacTotalRoamCallsAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11CacTotalRoamCallsAP.setStatus("current")
_CLQd11CacVoiceCallsRejectedAP_Type = Counter32
_CLQd11CacVoiceCallsRejectedAP_Object = MibTableColumn
cLQd11CacVoiceCallsRejectedAP = _CLQd11CacVoiceCallsRejectedAP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 7),
    _CLQd11CacVoiceCallsRejectedAP_Type()
)
cLQd11CacVoiceCallsRejectedAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11CacVoiceCallsRejectedAP.setStatus("current")
_CLQd11CacRoamCallsRejectedAP_Type = Counter32
_CLQd11CacRoamCallsRejectedAP_Object = MibTableColumn
cLQd11CacRoamCallsRejectedAP = _CLQd11CacRoamCallsRejectedAP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 8),
    _CLQd11CacRoamCallsRejectedAP_Type()
)
cLQd11CacRoamCallsRejectedAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11CacRoamCallsRejectedAP.setStatus("current")
_CLQd11CacRejCallsInsufBw_Type = Counter32
_CLQd11CacRejCallsInsufBw_Object = MibTableColumn
cLQd11CacRejCallsInsufBw = _CLQd11CacRejCallsInsufBw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 9),
    _CLQd11CacRejCallsInsufBw_Type()
)
cLQd11CacRejCallsInsufBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11CacRejCallsInsufBw.setStatus("current")
_CLQd11CacRejCallsBadParams_Type = Counter32
_CLQd11CacRejCallsBadParams_Object = MibTableColumn
cLQd11CacRejCallsBadParams = _CLQd11CacRejCallsBadParams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 10),
    _CLQd11CacRejCallsBadParams_Type()
)
cLQd11CacRejCallsBadParams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11CacRejCallsBadParams.setStatus("current")
_CLQd11CacRejCallsPhyRate_Type = Counter32
_CLQd11CacRejCallsPhyRate_Object = MibTableColumn
cLQd11CacRejCallsPhyRate = _CLQd11CacRejCallsPhyRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 11),
    _CLQd11CacRejCallsPhyRate_Type()
)
cLQd11CacRejCallsPhyRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11CacRejCallsPhyRate.setStatus("current")
_CLQd11CacRejCallsQosPolicy_Type = Counter32
_CLQd11CacRejCallsQosPolicy_Object = MibTableColumn
cLQd11CacRejCallsQosPolicy = _CLQd11CacRejCallsQosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 12),
    _CLQd11CacRejCallsQosPolicy_Type()
)
cLQd11CacRejCallsQosPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11CacRejCallsQosPolicy.setStatus("current")
_CLQd11SipCacNonRoamCallsInProgress_Type = Gauge32
_CLQd11SipCacNonRoamCallsInProgress_Object = MibTableColumn
cLQd11SipCacNonRoamCallsInProgress = _CLQd11SipCacNonRoamCallsInProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 13),
    _CLQd11SipCacNonRoamCallsInProgress_Type()
)
cLQd11SipCacNonRoamCallsInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11SipCacNonRoamCallsInProgress.setStatus("current")
_CLQd11SipCacRoamCallsInProg_Type = Gauge32
_CLQd11SipCacRoamCallsInProg_Object = MibTableColumn
cLQd11SipCacRoamCallsInProg = _CLQd11SipCacRoamCallsInProg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 14),
    _CLQd11SipCacRoamCallsInProg_Type()
)
cLQd11SipCacRoamCallsInProg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11SipCacRoamCallsInProg.setStatus("current")
_CLQd11SipCacTotalNonRoamCallsAP_Type = Counter32
_CLQd11SipCacTotalNonRoamCallsAP_Object = MibTableColumn
cLQd11SipCacTotalNonRoamCallsAP = _CLQd11SipCacTotalNonRoamCallsAP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 15),
    _CLQd11SipCacTotalNonRoamCallsAP_Type()
)
cLQd11SipCacTotalNonRoamCallsAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11SipCacTotalNonRoamCallsAP.setStatus("current")
_CLQd11SipCacTotalRoamCallsAP_Type = Counter32
_CLQd11SipCacTotalRoamCallsAP_Object = MibTableColumn
cLQd11SipCacTotalRoamCallsAP = _CLQd11SipCacTotalRoamCallsAP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 16),
    _CLQd11SipCacTotalRoamCallsAP_Type()
)
cLQd11SipCacTotalRoamCallsAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11SipCacTotalRoamCallsAP.setStatus("current")
_CLQd11SipCacNonRoamCallsRejectedInSuffBw_Type = Counter32
_CLQd11SipCacNonRoamCallsRejectedInSuffBw_Object = MibTableColumn
cLQd11SipCacNonRoamCallsRejectedInSuffBw = _CLQd11SipCacNonRoamCallsRejectedInSuffBw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 17),
    _CLQd11SipCacNonRoamCallsRejectedInSuffBw_Type()
)
cLQd11SipCacNonRoamCallsRejectedInSuffBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11SipCacNonRoamCallsRejectedInSuffBw.setStatus("current")
_CLQd11SipCacRoamCallsRejectedInSuffBw_Type = Counter32
_CLQd11SipCacRoamCallsRejectedInSuffBw_Object = MibTableColumn
cLQd11SipCacRoamCallsRejectedInSuffBw = _CLQd11SipCacRoamCallsRejectedInSuffBw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 18),
    _CLQd11SipCacRoamCallsRejectedInSuffBw_Type()
)
cLQd11SipCacRoamCallsRejectedInSuffBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11SipCacRoamCallsRejectedInSuffBw.setStatus("current")
_CLQd11SipCacNonRoamCallsRejectedMaxLimit_Type = Counter32
_CLQd11SipCacNonRoamCallsRejectedMaxLimit_Object = MibTableColumn
cLQd11SipCacNonRoamCallsRejectedMaxLimit = _CLQd11SipCacNonRoamCallsRejectedMaxLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 19),
    _CLQd11SipCacNonRoamCallsRejectedMaxLimit_Type()
)
cLQd11SipCacNonRoamCallsRejectedMaxLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11SipCacNonRoamCallsRejectedMaxLimit.setStatus("current")
_CLQd11SipCacRoamCallsRejectedMaxLimit_Type = Counter32
_CLQd11SipCacRoamCallsRejectedMaxLimit_Object = MibTableColumn
cLQd11SipCacRoamCallsRejectedMaxLimit = _CLQd11SipCacRoamCallsRejectedMaxLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 20),
    _CLQd11SipCacRoamCallsRejectedMaxLimit_Type()
)
cLQd11SipCacRoamCallsRejectedMaxLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11SipCacRoamCallsRejectedMaxLimit.setStatus("current")
_CLQd11SipCacRejCallsQosPolicy_Type = Counter32
_CLQd11SipCacRejCallsQosPolicy_Object = MibTableColumn
cLQd11SipCacRejCallsQosPolicy = _CLQd11SipCacRejCallsQosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 21),
    _CLQd11SipCacRejCallsQosPolicy_Type()
)
cLQd11SipCacRejCallsQosPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11SipCacRejCallsQosPolicy.setStatus("current")
_CLQEntConfConfig_ObjectIdentity = ObjectIdentity
cLQEntConfConfig = _CLQEntConfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 5)
)
_CLQd11VoiceStats_ObjectIdentity = ObjectIdentity
cLQd11VoiceStats = _CLQd11VoiceStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 6)
)
_CLQd11VoiceStatsTable_Object = MibTable
cLQd11VoiceStatsTable = _CLQd11VoiceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cLQd11VoiceStatsTable.setStatus("current")
_CLQd11VoiceStatsEntry_Object = MibTableRow
cLQd11VoiceStatsEntry = _CLQd11VoiceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 6, 1, 1)
)
cLQd11VoiceStatsEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
)
if mibBuilder.loadTexts:
    cLQd11VoiceStatsEntry.setStatus("current")
_CLQd11VoiceCallCounts_Type = Counter32
_CLQd11VoiceCallCounts_Object = MibTableColumn
cLQd11VoiceCallCounts = _CLQd11VoiceCallCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 6, 1, 1, 1),
    _CLQd11VoiceCallCounts_Type()
)
cLQd11VoiceCallCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11VoiceCallCounts.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11VoiceCallCounts.setUnits("calls")
_CLQd11CacVoiceCallTimePeriod_Type = TimeIntervalSec
_CLQd11CacVoiceCallTimePeriod_Object = MibTableColumn
cLQd11CacVoiceCallTimePeriod = _CLQd11CacVoiceCallTimePeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 6, 1, 1, 2),
    _CLQd11CacVoiceCallTimePeriod_Type()
)
cLQd11CacVoiceCallTimePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQd11CacVoiceCallTimePeriod.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11CacVoiceCallTimePeriod.setUnits("seconds")
_CLQVoiceWlanConfig_ObjectIdentity = ObjectIdentity
cLQVoiceWlanConfig = _CLQVoiceWlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 7)
)
_CLQVoiceWlanConfigTable_Object = MibTable
cLQVoiceWlanConfigTable = _CLQVoiceWlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 7, 1)
)
if mibBuilder.loadTexts:
    cLQVoiceWlanConfigTable.setStatus("current")
_CLQVoiceWlanConfigEntry_Object = MibTableRow
cLQVoiceWlanConfigEntry = _CLQVoiceWlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 7, 1, 1)
)
cLQVoiceWlanConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLQVoiceWlanConfigEntry.setStatus("current")


class _CLQVoiceWlanConfigDetectVoipCallFailure_Type(TruthValue):
    """Custom type cLQVoiceWlanConfigDetectVoipCallFailure based on TruthValue"""


_CLQVoiceWlanConfigDetectVoipCallFailure_Object = MibTableColumn
cLQVoiceWlanConfigDetectVoipCallFailure = _CLQVoiceWlanConfigDetectVoipCallFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 7, 1, 1, 1),
    _CLQVoiceWlanConfigDetectVoipCallFailure_Type()
)
cLQVoiceWlanConfigDetectVoipCallFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQVoiceWlanConfigDetectVoipCallFailure.setStatus("current")
_CLQVoiceClient_ObjectIdentity = ObjectIdentity
cLQVoiceClient = _CLQVoiceClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 8)
)
_CLQVoiceClientTable_Object = MibTable
cLQVoiceClientTable = _CLQVoiceClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 8, 1)
)
if mibBuilder.loadTexts:
    cLQVoiceClientTable.setStatus("current")
_CLQVoiceClientEntry_Object = MibTableRow
cLQVoiceClientEntry = _CLQVoiceClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 8, 1, 1)
)
cLQVoiceClientEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cLQVoiceClientEntry.setStatus("current")
_CLQVoiceClientCallingNumber_Type = SnmpAdminString
_CLQVoiceClientCallingNumber_Object = MibTableColumn
cLQVoiceClientCallingNumber = _CLQVoiceClientCallingNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 8, 1, 1, 1),
    _CLQVoiceClientCallingNumber_Type()
)
cLQVoiceClientCallingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVoiceClientCallingNumber.setStatus("current")
_CLQVoiceClientLastCalledNumber_Type = SnmpAdminString
_CLQVoiceClientLastCalledNumber_Object = MibTableColumn
cLQVoiceClientLastCalledNumber = _CLQVoiceClientLastCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 8, 1, 1, 2),
    _CLQVoiceClientLastCalledNumber_Type()
)
cLQVoiceClientLastCalledNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVoiceClientLastCalledNumber.setStatus("current")


class _CLQVoiceClientLastCallFailureReasonCode_Type(Integer32):
    """Custom type cLQVoiceClientLastCallFailureReasonCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              400,
              401,
              402,
              403,
              404,
              405,
              406,
              407,
              408,
              409,
              410,
              411,
              413,
              414,
              415,
              420,
              480,
              481,
              482,
              483,
              484,
              485,
              486,
              500,
              501,
              502,
              503,
              504,
              505,
              600,
              603,
              604,
              606)
        )
    )
    namedValues = NamedValues(
        *(("addressIncomplete", 484),
          ("ambiguous", 485),
          ("badExtension", 420),
          ("badGateway", 502),
          ("badRequest", 400),
          ("busy", 486),
          ("busyEverywhere", 600),
          ("callLegDoesNotExist", 481),
          ("conflict", 409),
          ("decline", 603),
          ("doesNotExistAnywhere", 604),
          ("forbidden", 403),
          ("gone", 410),
          ("internalServerError", 500),
          ("lengthRequired", 411),
          ("loopDetected", 482),
          ("maxLimitExceeded", 4),
          ("methodNotallowed", 405),
          ("normalFailure", 2),
          ("notAcceptable", 406),
          ("notFound", 404),
          ("notImplemented", 501),
          ("paymentRequired", 402),
          ("proxyAuthenticationRequired", 407),
          ("requestEntityTooLarge", 413),
          ("requestTimeout", 408),
          ("requestURITooLarge", 414),
          ("roamFailure", 3),
          ("serverTimeout", 504),
          ("serviceUnavailable", 503),
          ("sessionNotAcceptable", 606),
          ("temporarilyNotAvailable", 480),
          ("tooManyHops", 483),
          ("unathorized", 401),
          ("unknown", 1),
          ("unsupportedMdediaType", 415),
          ("versionNotSupported", 505))
    )


_CLQVoiceClientLastCallFailureReasonCode_Type.__name__ = "Integer32"
_CLQVoiceClientLastCallFailureReasonCode_Object = MibTableColumn
cLQVoiceClientLastCallFailureReasonCode = _CLQVoiceClientLastCallFailureReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 8, 1, 1, 3),
    _CLQVoiceClientLastCallFailureReasonCode_Type()
)
cLQVoiceClientLastCallFailureReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLQVoiceClientLastCallFailureReasonCode.setStatus("current")
_CLQd11SipCacConfig_ObjectIdentity = ObjectIdentity
cLQd11SipCacConfig = _CLQd11SipCacConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 9)
)
_CLQd11SipCacConfigTable_Object = MibTable
cLQd11SipCacConfigTable = _CLQd11SipCacConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 9, 1)
)
if mibBuilder.loadTexts:
    cLQd11SipCacConfigTable.setStatus("current")
_CLQd11SipCacConfigEntry_Object = MibTableRow
cLQd11SipCacConfigEntry = _CLQd11SipCacConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 9, 1, 1)
)
cLQd11SipCacConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfType"),
)
if mibBuilder.loadTexts:
    cLQd11SipCacConfigEntry.setStatus("current")


class _CLQd11SipCacConfigCodecType_Type(Integer32):
    """Custom type cLQd11SipCacConfigCodecType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("g711", 2),
          ("g729", 3),
          ("userDefined", 1))
    )


_CLQd11SipCacConfigCodecType_Type.__name__ = "Integer32"
_CLQd11SipCacConfigCodecType_Object = MibTableColumn
cLQd11SipCacConfigCodecType = _CLQd11SipCacConfigCodecType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 9, 1, 1, 1),
    _CLQd11SipCacConfigCodecType_Type()
)
cLQd11SipCacConfigCodecType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11SipCacConfigCodecType.setStatus("current")
_CLQd11SipCacConfigBw_Type = Unsigned32
_CLQd11SipCacConfigBw_Object = MibTableColumn
cLQd11SipCacConfigBw = _CLQd11SipCacConfigBw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 9, 1, 1, 2),
    _CLQd11SipCacConfigBw_Type()
)
cLQd11SipCacConfigBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11SipCacConfigBw.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11SipCacConfigBw.setUnits("kbps")
_CLQd11SipCacConfigVoiceSampleSize_Type = Unsigned32
_CLQd11SipCacConfigVoiceSampleSize_Object = MibTableColumn
cLQd11SipCacConfigVoiceSampleSize = _CLQd11SipCacConfigVoiceSampleSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 9, 1, 1, 3),
    _CLQd11SipCacConfigVoiceSampleSize_Type()
)
cLQd11SipCacConfigVoiceSampleSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLQd11SipCacConfigVoiceSampleSize.setStatus("current")
if mibBuilder.loadTexts:
    cLQd11SipCacConfigVoiceSampleSize.setUnits("milliseconds")
_CLQConfigObjects_ObjectIdentity = ObjectIdentity
cLQConfigObjects = _CLQConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 10)
)
_CiscoLwappVoipCallFailureNotifEnabled_Type = TruthValue
_CiscoLwappVoipCallFailureNotifEnabled_Object = MibScalar
ciscoLwappVoipCallFailureNotifEnabled = _CiscoLwappVoipCallFailureNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 10, 1),
    _CiscoLwappVoipCallFailureNotifEnabled_Type()
)
ciscoLwappVoipCallFailureNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoLwappVoipCallFailureNotifEnabled.setStatus("current")
_CiscoLwappQosMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappQosMIBConform = _CiscoLwappQosMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2)
)
_CiscoLwappQosMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappQosMIBCompliances = _CiscoLwappQosMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 1)
)
_CiscoLwappQosMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappQosMIBGroups = _CiscoLwappQosMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2)
)
cLWlanConfigEntry.registerAugmentions(
    ("CISCO-LWAPP-QOS-MIB",
     "cLQd11GprEntry")
)
cLQd11GprEntry.setIndexNames(*cLWlanConfigEntry.getIndexNames())
cLApDot11IfEntry.registerAugmentions(
    ("CISCO-LWAPP-QOS-MIB",
     "cLQd11CACStatsEntry")
)
cLQd11CACStatsEntry.setIndexNames(*cLApDot11IfEntry.getIndexNames())

# Managed Objects groups

ciscoLwappQosDot11aConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 1)
)
ciscoLwappQosDot11aConfigGroup.setObjects(
      *(("CISCO-LWAPP-QOS-MIB", "cLQd11aVoiceAdmCtrlSupport"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11aVoiceMaxAdmBandwidth"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11aVoiceMaxRoamBandwidth"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11aVideoAdmCtrlSupport"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11aVideoMaxAdmBandwidth"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11aVideoMaxRoamBandwidth"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11aGprProbeInterval"))
)
if mibBuilder.loadTexts:
    ciscoLwappQosDot11aConfigGroup.setStatus("current")

ciscoLwappQosDot11bConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 2)
)
ciscoLwappQosDot11bConfigGroup.setObjects(
      *(("CISCO-LWAPP-QOS-MIB", "cLQd11bVoiceAdmCtrlSupport"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11bVoiceMaxAdmBandwidth"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11bVoiceMaxRoamBandwidth"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11bVideoAdmCtrlSupport"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11bVideoMaxAdmBandwidth"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11bVideoMaxRoamBandwidth"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11bGprProbeInterval"))
)
if mibBuilder.loadTexts:
    ciscoLwappQosDot11bConfigGroup.setStatus("current")

ciscoLwappQosDot11WlanConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 3)
)
ciscoLwappQosDot11WlanConfigGroup.setObjects(
    ("CISCO-LWAPP-QOS-MIB", "cLQd11GprSupport")
)
if mibBuilder.loadTexts:
    ciscoLwappQosDot11WlanConfigGroup.setStatus("current")

ciscoLwappQosDot11CacStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 4)
)
ciscoLwappQosDot11CacStatsGroup.setObjects(
      *(("CISCO-LWAPP-QOS-MIB", "cLQd11CacVoiceBwInUse"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11CacVideoBwInUse"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11CacVoiceCallsInProgress"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11CacRoamVoiceCallsInProg"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11CacTotalVoiceCallsAP"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11CacTotalRoamCallsAP"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11CacVoiceCallsRejectedAP"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11CacRoamCallsRejectedAP"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11CacRejCallsInsufBw"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11CacRejCallsBadParams"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11CacRejCallsPhyRate"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11CacRejCallsQosPolicy"))
)
if mibBuilder.loadTexts:
    ciscoLwappQosDot11CacStatsGroup.setStatus("current")

ciscoLwappQosDot11aConfigGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 5)
)
ciscoLwappQosDot11aConfigGroupSup1.setObjects(
      *(("CISCO-LWAPP-QOS-MIB", "cLQd11aVoiceCtrl"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11aExpeditedBw"))
)
if mibBuilder.loadTexts:
    ciscoLwappQosDot11aConfigGroupSup1.setStatus("current")

ciscoLwappQosDot11bConfigGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 6)
)
ciscoLwappQosDot11bConfigGroupSup1.setObjects(
      *(("CISCO-LWAPP-QOS-MIB", "cLQd11bVoiceCtrl"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11bExpeditedBw"))
)
if mibBuilder.loadTexts:
    ciscoLwappQosDot11bConfigGroupSup1.setStatus("current")

ciscoLwappQosDot11aConfigGroupSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 7)
)
ciscoLwappQosDot11aConfigGroupSup2.setObjects(
      *(("CISCO-LWAPP-QOS-MIB", "cLQd11aEdcaProfile"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11aMacOptimization"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11aMaxCallLimit"))
)
if mibBuilder.loadTexts:
    ciscoLwappQosDot11aConfigGroupSup2.setStatus("current")

ciscoLwappQosDot11bConfigGroupSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 8)
)
ciscoLwappQosDot11bConfigGroupSup2.setObjects(
      *(("CISCO-LWAPP-QOS-MIB", "cLQd11bEdcaProfile"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11bMacOptimization"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11bMaxCallLimit"))
)
if mibBuilder.loadTexts:
    ciscoLwappQosDot11bConfigGroupSup2.setStatus("current")

ciscoLwappQosDot11SipCacStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 9)
)
ciscoLwappQosDot11SipCacStatsGroup.setObjects(
      *(("CISCO-LWAPP-QOS-MIB", "cLQd11SipCacNonRoamCallsInProgress"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11SipCacRoamCallsInProg"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11SipCacTotalNonRoamCallsAP"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11SipCacTotalRoamCallsAP"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11SipCacNonRoamCallsRejectedInSuffBw"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11SipCacRoamCallsRejectedInSuffBw"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11SipCacNonRoamCallsRejectedMaxLimit"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11SipCacRoamCallsRejectedMaxLimit"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11SipCacRejCallsQosPolicy"))
)
if mibBuilder.loadTexts:
    ciscoLwappQosDot11SipCacStatsGroup.setStatus("current")

ciscoLwappQosDot11SipConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 10)
)
ciscoLwappQosDot11SipConfigGroup.setObjects(
      *(("CISCO-LWAPP-QOS-MIB", "cLQd11SipCacConfigCodecType"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11SipCacConfigBw"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11SipCacConfigVoiceSampleSize"))
)
if mibBuilder.loadTexts:
    ciscoLwappQosDot11SipConfigGroup.setStatus("current")

ciscoLwappQosDot11VoiceStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 11)
)
ciscoLwappQosDot11VoiceStatsGroup.setObjects(
      *(("CISCO-LWAPP-QOS-MIB", "cLQd11VoiceCallCounts"),
        ("CISCO-LWAPP-QOS-MIB", "cLQd11CacVoiceCallTimePeriod"))
)
if mibBuilder.loadTexts:
    ciscoLwappQosDot11VoiceStatsGroup.setStatus("current")

ciscoLwappQosDot11VoiceConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 12)
)
ciscoLwappQosDot11VoiceConfigGroup.setObjects(
      *(("CISCO-LWAPP-QOS-MIB", "cLQVoiceWlanConfigDetectVoipCallFailure"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVoiceClientCallingNumber"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVoiceClientLastCalledNumber"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVoiceClientLastCallFailureReasonCode"))
)
if mibBuilder.loadTexts:
    ciscoLwappQosDot11VoiceConfigGroup.setStatus("current")

ciscoLwappQosConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 14)
)
ciscoLwappQosConfigGroup.setObjects(
    ("CISCO-LWAPP-QOS-MIB", "ciscoLwappVoipCallFailureNotifEnabled")
)
if mibBuilder.loadTexts:
    ciscoLwappQosConfigGroup.setStatus("current")


# Notification objects

ciscoLwappVoipCallFailureNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 0, 1)
)
ciscoLwappVoipCallFailureNotif.setObjects(
      *(("CISCO-LWAPP-QOS-MIB", "cLQVoiceClientLastCallFailureReasonCode"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVoiceClientCallingNumber"),
        ("CISCO-LWAPP-QOS-MIB", "cLQVoiceClientLastCalledNumber"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfType"))
)
if mibBuilder.loadTexts:
    ciscoLwappVoipCallFailureNotif.setStatus(
        "current"
    )


# Notifications groups

ciscoLwappQosDot11VoiceNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 13)
)
ciscoLwappQosDot11VoiceNotifGroup.setObjects(
    ("CISCO-LWAPP-QOS-MIB", "ciscoLwappVoipCallFailureNotif")
)
if mibBuilder.loadTexts:
    ciscoLwappQosDot11VoiceNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLwappQosMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLwappQosMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappQosMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoLwappQosMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoLwappQosMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoLwappQosMIBComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-QOS-MIB",
    **{"ciscoLwappQosMIB": ciscoLwappQosMIB,
       "ciscoLwappQosMIBNotifs": ciscoLwappQosMIBNotifs,
       "ciscoLwappVoipCallFailureNotif": ciscoLwappVoipCallFailureNotif,
       "ciscoLwappQosMIBObjects": ciscoLwappQosMIBObjects,
       "cLQd11aCACConfig": cLQd11aCACConfig,
       "cLQd11aVoiceAdmCtrlSupport": cLQd11aVoiceAdmCtrlSupport,
       "cLQd11aVoiceMaxAdmBandwidth": cLQd11aVoiceMaxAdmBandwidth,
       "cLQd11aVoiceMaxRoamBandwidth": cLQd11aVoiceMaxRoamBandwidth,
       "cLQd11aVideoAdmCtrlSupport": cLQd11aVideoAdmCtrlSupport,
       "cLQd11aVideoMaxAdmBandwidth": cLQd11aVideoMaxAdmBandwidth,
       "cLQd11aVideoMaxRoamBandwidth": cLQd11aVideoMaxRoamBandwidth,
       "cLQd11aGprProbeInterval": cLQd11aGprProbeInterval,
       "cLQd11aVoiceCtrl": cLQd11aVoiceCtrl,
       "cLQd11aExpeditedBw": cLQd11aExpeditedBw,
       "cLQd11aEdcaProfile": cLQd11aEdcaProfile,
       "cLQd11aMacOptimization": cLQd11aMacOptimization,
       "cLQd11aMaxCallLimit": cLQd11aMaxCallLimit,
       "cLQd11bCACConfig": cLQd11bCACConfig,
       "cLQd11bVoiceAdmCtrlSupport": cLQd11bVoiceAdmCtrlSupport,
       "cLQd11bVoiceMaxAdmBandwidth": cLQd11bVoiceMaxAdmBandwidth,
       "cLQd11bVoiceMaxRoamBandwidth": cLQd11bVoiceMaxRoamBandwidth,
       "cLQd11bVideoAdmCtrlSupport": cLQd11bVideoAdmCtrlSupport,
       "cLQd11bVideoMaxAdmBandwidth": cLQd11bVideoMaxAdmBandwidth,
       "cLQd11bVideoMaxRoamBandwidth": cLQd11bVideoMaxRoamBandwidth,
       "cLQd11bGprProbeInterval": cLQd11bGprProbeInterval,
       "cLQd11bVoiceCtrl": cLQd11bVoiceCtrl,
       "cLQd11bExpeditedBw": cLQd11bExpeditedBw,
       "cLQd11bEdcaProfile": cLQd11bEdcaProfile,
       "cLQd11bMacOptimization": cLQd11bMacOptimization,
       "cLQd11bMaxCallLimit": cLQd11bMaxCallLimit,
       "cLQd11GprConfig": cLQd11GprConfig,
       "cLQd11GprTable": cLQd11GprTable,
       "cLQd11GprEntry": cLQd11GprEntry,
       "cLQd11GprSupport": cLQd11GprSupport,
       "cLQd11CACStats": cLQd11CACStats,
       "cLQd11CACStatsTable": cLQd11CACStatsTable,
       "cLQd11CACStatsEntry": cLQd11CACStatsEntry,
       "cLQd11CacVoiceBwInUse": cLQd11CacVoiceBwInUse,
       "cLQd11CacVideoBwInUse": cLQd11CacVideoBwInUse,
       "cLQd11CacVoiceCallsInProgress": cLQd11CacVoiceCallsInProgress,
       "cLQd11CacRoamVoiceCallsInProg": cLQd11CacRoamVoiceCallsInProg,
       "cLQd11CacTotalVoiceCallsAP": cLQd11CacTotalVoiceCallsAP,
       "cLQd11CacTotalRoamCallsAP": cLQd11CacTotalRoamCallsAP,
       "cLQd11CacVoiceCallsRejectedAP": cLQd11CacVoiceCallsRejectedAP,
       "cLQd11CacRoamCallsRejectedAP": cLQd11CacRoamCallsRejectedAP,
       "cLQd11CacRejCallsInsufBw": cLQd11CacRejCallsInsufBw,
       "cLQd11CacRejCallsBadParams": cLQd11CacRejCallsBadParams,
       "cLQd11CacRejCallsPhyRate": cLQd11CacRejCallsPhyRate,
       "cLQd11CacRejCallsQosPolicy": cLQd11CacRejCallsQosPolicy,
       "cLQd11SipCacNonRoamCallsInProgress": cLQd11SipCacNonRoamCallsInProgress,
       "cLQd11SipCacRoamCallsInProg": cLQd11SipCacRoamCallsInProg,
       "cLQd11SipCacTotalNonRoamCallsAP": cLQd11SipCacTotalNonRoamCallsAP,
       "cLQd11SipCacTotalRoamCallsAP": cLQd11SipCacTotalRoamCallsAP,
       "cLQd11SipCacNonRoamCallsRejectedInSuffBw": cLQd11SipCacNonRoamCallsRejectedInSuffBw,
       "cLQd11SipCacRoamCallsRejectedInSuffBw": cLQd11SipCacRoamCallsRejectedInSuffBw,
       "cLQd11SipCacNonRoamCallsRejectedMaxLimit": cLQd11SipCacNonRoamCallsRejectedMaxLimit,
       "cLQd11SipCacRoamCallsRejectedMaxLimit": cLQd11SipCacRoamCallsRejectedMaxLimit,
       "cLQd11SipCacRejCallsQosPolicy": cLQd11SipCacRejCallsQosPolicy,
       "cLQEntConfConfig": cLQEntConfConfig,
       "cLQd11VoiceStats": cLQd11VoiceStats,
       "cLQd11VoiceStatsTable": cLQd11VoiceStatsTable,
       "cLQd11VoiceStatsEntry": cLQd11VoiceStatsEntry,
       "cLQd11VoiceCallCounts": cLQd11VoiceCallCounts,
       "cLQd11CacVoiceCallTimePeriod": cLQd11CacVoiceCallTimePeriod,
       "cLQVoiceWlanConfig": cLQVoiceWlanConfig,
       "cLQVoiceWlanConfigTable": cLQVoiceWlanConfigTable,
       "cLQVoiceWlanConfigEntry": cLQVoiceWlanConfigEntry,
       "cLQVoiceWlanConfigDetectVoipCallFailure": cLQVoiceWlanConfigDetectVoipCallFailure,
       "cLQVoiceClient": cLQVoiceClient,
       "cLQVoiceClientTable": cLQVoiceClientTable,
       "cLQVoiceClientEntry": cLQVoiceClientEntry,
       "cLQVoiceClientCallingNumber": cLQVoiceClientCallingNumber,
       "cLQVoiceClientLastCalledNumber": cLQVoiceClientLastCalledNumber,
       "cLQVoiceClientLastCallFailureReasonCode": cLQVoiceClientLastCallFailureReasonCode,
       "cLQd11SipCacConfig": cLQd11SipCacConfig,
       "cLQd11SipCacConfigTable": cLQd11SipCacConfigTable,
       "cLQd11SipCacConfigEntry": cLQd11SipCacConfigEntry,
       "cLQd11SipCacConfigCodecType": cLQd11SipCacConfigCodecType,
       "cLQd11SipCacConfigBw": cLQd11SipCacConfigBw,
       "cLQd11SipCacConfigVoiceSampleSize": cLQd11SipCacConfigVoiceSampleSize,
       "cLQConfigObjects": cLQConfigObjects,
       "ciscoLwappVoipCallFailureNotifEnabled": ciscoLwappVoipCallFailureNotifEnabled,
       "ciscoLwappQosMIBConform": ciscoLwappQosMIBConform,
       "ciscoLwappQosMIBCompliances": ciscoLwappQosMIBCompliances,
       "ciscoLwappQosMIBCompliance": ciscoLwappQosMIBCompliance,
       "ciscoLwappQosMIBComplianceRev1": ciscoLwappQosMIBComplianceRev1,
       "ciscoLwappQosMIBComplianceRev2": ciscoLwappQosMIBComplianceRev2,
       "ciscoLwappQosMIBGroups": ciscoLwappQosMIBGroups,
       "ciscoLwappQosDot11aConfigGroup": ciscoLwappQosDot11aConfigGroup,
       "ciscoLwappQosDot11bConfigGroup": ciscoLwappQosDot11bConfigGroup,
       "ciscoLwappQosDot11WlanConfigGroup": ciscoLwappQosDot11WlanConfigGroup,
       "ciscoLwappQosDot11CacStatsGroup": ciscoLwappQosDot11CacStatsGroup,
       "ciscoLwappQosDot11aConfigGroupSup1": ciscoLwappQosDot11aConfigGroupSup1,
       "ciscoLwappQosDot11bConfigGroupSup1": ciscoLwappQosDot11bConfigGroupSup1,
       "ciscoLwappQosDot11aConfigGroupSup2": ciscoLwappQosDot11aConfigGroupSup2,
       "ciscoLwappQosDot11bConfigGroupSup2": ciscoLwappQosDot11bConfigGroupSup2,
       "ciscoLwappQosDot11SipCacStatsGroup": ciscoLwappQosDot11SipCacStatsGroup,
       "ciscoLwappQosDot11SipConfigGroup": ciscoLwappQosDot11SipConfigGroup,
       "ciscoLwappQosDot11VoiceStatsGroup": ciscoLwappQosDot11VoiceStatsGroup,
       "ciscoLwappQosDot11VoiceConfigGroup": ciscoLwappQosDot11VoiceConfigGroup,
       "ciscoLwappQosDot11VoiceNotifGroup": ciscoLwappQosDot11VoiceNotifGroup,
       "ciscoLwappQosConfigGroup": ciscoLwappQosConfigGroup}
)
