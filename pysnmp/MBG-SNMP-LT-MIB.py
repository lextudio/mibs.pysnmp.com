# SNMP MIB module (MBG-SNMP-LT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MBG-SNMP-LT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:20:35 2024
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

(mbgSnmpRoot,) = mibBuilder.importSymbols(
    "MBG-SNMP-ROOT-MIB",
    "mbgSnmpRoot")

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


# MODULE-IDENTITY

mbgLantime = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3)
)
mbgLantime.setRevisions(
        ("2012-01-25 07:45",
         "2011-03-30 00:00",
         "2011-03-29 00:00",
         "2010-01-19 00:00",
         "2009-12-03 00:00",
         "2008-09-10 00:00",
         "2008-07-15 00:00",
         "2008-06-15 00:00",
         "2006-08-23 00:00",
         "2006-03-20 00:00",
         "2005-07-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MbgLtInfo_ObjectIdentity = ObjectIdentity
mbgLtInfo = _MbgLtInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 0)
)
_MbgLtFirmwareVersion_Type = DisplayString
_MbgLtFirmwareVersion_Object = MibScalar
mbgLtFirmwareVersion = _MbgLtFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 0, 1),
    _MbgLtFirmwareVersion_Type()
)
mbgLtFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtFirmwareVersion.setStatus("current")


class _MbgLtFirmwareVersionVal_Type(Integer32):
    """Custom type mbgLtFirmwareVersionVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_MbgLtFirmwareVersionVal_Type.__name__ = "Integer32"
_MbgLtFirmwareVersionVal_Object = MibScalar
mbgLtFirmwareVersionVal = _MbgLtFirmwareVersionVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 0, 2),
    _MbgLtFirmwareVersionVal_Type()
)
mbgLtFirmwareVersionVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtFirmwareVersionVal.setStatus("current")
_MbgLtNtp_ObjectIdentity = ObjectIdentity
mbgLtNtp = _MbgLtNtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 1)
)
_MbgLtNtpCurrentState_Type = DisplayString
_MbgLtNtpCurrentState_Object = MibScalar
mbgLtNtpCurrentState = _MbgLtNtpCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 1, 1),
    _MbgLtNtpCurrentState_Type()
)
mbgLtNtpCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNtpCurrentState.setStatus("current")


class _MbgLtNtpCurrentStateVal_Type(Integer32):
    """Custom type mbgLtNtpCurrentStateVal based on Integer32"""
    defaultValue = 99

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              99)
        )
    )
    namedValues = NamedValues(
        *(("noGoodRefclock", 1),
          ("normalOperationPPS", 4),
          ("normalOperationRefclock", 5),
          ("notSynchronized", 0),
          ("syncToExtRefclock", 2),
          ("syncToSerialRefclock", 3),
          ("unknown", 99))
    )


_MbgLtNtpCurrentStateVal_Type.__name__ = "Integer32"
_MbgLtNtpCurrentStateVal_Object = MibScalar
mbgLtNtpCurrentStateVal = _MbgLtNtpCurrentStateVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 1, 2),
    _MbgLtNtpCurrentStateVal_Type()
)
mbgLtNtpCurrentStateVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNtpCurrentStateVal.setStatus("current")


class _MbgLtNtpStratum_Type(Integer32):
    """Custom type mbgLtNtpStratum based on Integer32"""
    defaultValue = 99

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_MbgLtNtpStratum_Type.__name__ = "Integer32"
_MbgLtNtpStratum_Object = MibScalar
mbgLtNtpStratum = _MbgLtNtpStratum_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 1, 3),
    _MbgLtNtpStratum_Type()
)
mbgLtNtpStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNtpStratum.setStatus("current")


class _MbgLtNtpActiveRefclockId_Type(Integer32):
    """Custom type mbgLtNtpActiveRefclockId based on Integer32"""
    defaultValue = 99

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("externalRefclock", 3),
          ("localClock", 0),
          ("notSync", 99),
          ("pps", 2),
          ("serialRefclock", 1))
    )


_MbgLtNtpActiveRefclockId_Type.__name__ = "Integer32"
_MbgLtNtpActiveRefclockId_Object = MibScalar
mbgLtNtpActiveRefclockId = _MbgLtNtpActiveRefclockId_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 1, 4),
    _MbgLtNtpActiveRefclockId_Type()
)
mbgLtNtpActiveRefclockId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNtpActiveRefclockId.setStatus("current")
_MbgLtNtpActiveRefclockName_Type = DisplayString
_MbgLtNtpActiveRefclockName_Object = MibScalar
mbgLtNtpActiveRefclockName = _MbgLtNtpActiveRefclockName_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 1, 5),
    _MbgLtNtpActiveRefclockName_Type()
)
mbgLtNtpActiveRefclockName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNtpActiveRefclockName.setStatus("current")
_MbgLtNtpActiveRefclockOffset_Type = DisplayString
_MbgLtNtpActiveRefclockOffset_Object = MibScalar
mbgLtNtpActiveRefclockOffset = _MbgLtNtpActiveRefclockOffset_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 1, 6),
    _MbgLtNtpActiveRefclockOffset_Type()
)
mbgLtNtpActiveRefclockOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNtpActiveRefclockOffset.setStatus("current")


class _MbgLtNtpActiveRefclockOffsetVal_Type(Integer32):
    """Custom type mbgLtNtpActiveRefclockOffsetVal based on Integer32"""
    defaultValue = 1024000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_MbgLtNtpActiveRefclockOffsetVal_Type.__name__ = "Integer32"
_MbgLtNtpActiveRefclockOffsetVal_Object = MibScalar
mbgLtNtpActiveRefclockOffsetVal = _MbgLtNtpActiveRefclockOffsetVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 1, 7),
    _MbgLtNtpActiveRefclockOffsetVal_Type()
)
mbgLtNtpActiveRefclockOffsetVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNtpActiveRefclockOffsetVal.setStatus("current")


class _MbgLtNtpNumberOfRefclocks_Type(Integer32):
    """Custom type mbgLtNtpNumberOfRefclocks based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_MbgLtNtpNumberOfRefclocks_Type.__name__ = "Integer32"
_MbgLtNtpNumberOfRefclocks_Object = MibScalar
mbgLtNtpNumberOfRefclocks = _MbgLtNtpNumberOfRefclocks_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 1, 8),
    _MbgLtNtpNumberOfRefclocks_Type()
)
mbgLtNtpNumberOfRefclocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNtpNumberOfRefclocks.setStatus("current")


class _MbgLtNtpAuthKeyId_Type(Integer32):
    """Custom type mbgLtNtpAuthKeyId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_MbgLtNtpAuthKeyId_Type.__name__ = "Integer32"
_MbgLtNtpAuthKeyId_Object = MibScalar
mbgLtNtpAuthKeyId = _MbgLtNtpAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 1, 9),
    _MbgLtNtpAuthKeyId_Type()
)
mbgLtNtpAuthKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNtpAuthKeyId.setStatus("current")
_MbgLtNtpVersion_Type = DisplayString
_MbgLtNtpVersion_Object = MibScalar
mbgLtNtpVersion = _MbgLtNtpVersion_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 1, 10),
    _MbgLtNtpVersion_Type()
)
mbgLtNtpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNtpVersion.setStatus("current")
_MbgLtRefclock_ObjectIdentity = ObjectIdentity
mbgLtRefclock = _MbgLtRefclock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2)
)
_MbgLtRefClockType_Type = DisplayString
_MbgLtRefClockType_Object = MibScalar
mbgLtRefClockType = _MbgLtRefClockType_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 1),
    _MbgLtRefClockType_Type()
)
mbgLtRefClockType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtRefClockType.setStatus("current")


class _MbgLtRefClockTypeVal_Type(Integer32):
    """Custom type mbgLtRefClockTypeVal based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("mbgAHS", 15),
          ("mbgDCT", 19),
          ("mbgDCTBGT", 20),
          ("mbgDHS", 16),
          ("mbgEDT", 13),
          ("mbgEDTBGTTGP", 14),
          ("mbgGPS167", 1),
          ("mbgGPS167BGTTGP", 2),
          ("mbgNDT167", 17),
          ("mbgNDT167BGT", 18),
          ("mbgPZF509", 3),
          ("mbgPZF509BGTTGP", 4),
          ("mbgRDT", 11),
          ("mbgRDTBGTTGP", 12),
          ("mbgSHS", 5),
          ("mbgSHSBGT", 6),
          ("mbgSHSFRC", 7),
          ("mbgSHSFRCBGT", 8),
          ("mbgSHSTCR", 21),
          ("mbgSHSTCRBGT", 22),
          ("mbgTCR509", 9),
          ("mbgTCR509BGTTGP", 10),
          ("notavailable", 0))
    )


_MbgLtRefClockTypeVal_Type.__name__ = "Integer32"
_MbgLtRefClockTypeVal_Object = MibScalar
mbgLtRefClockTypeVal = _MbgLtRefClockTypeVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 2),
    _MbgLtRefClockTypeVal_Type()
)
mbgLtRefClockTypeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtRefClockTypeVal.setStatus("current")
_MbgLtRefClockMode_Type = DisplayString
_MbgLtRefClockMode_Object = MibScalar
mbgLtRefClockMode = _MbgLtRefClockMode_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 3),
    _MbgLtRefClockMode_Type()
)
mbgLtRefClockMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtRefClockMode.setStatus("current")


class _MbgLtRefClockModeVal_Type(Integer32):
    """Custom type mbgLtRefClockModeVal based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("antennaFaulty", 3),
          ("antennaShortcircuit", 6),
          ("coldBoot", 5),
          ("normalOperation", 1),
          ("notavailable", 0),
          ("trackingSearching", 2),
          ("warmBoot", 4))
    )


_MbgLtRefClockModeVal_Type.__name__ = "Integer32"
_MbgLtRefClockModeVal_Object = MibScalar
mbgLtRefClockModeVal = _MbgLtRefClockModeVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 4),
    _MbgLtRefClockModeVal_Type()
)
mbgLtRefClockModeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtRefClockModeVal.setStatus("current")
_MbgLtRefGpsState_Type = DisplayString
_MbgLtRefGpsState_Object = MibScalar
mbgLtRefGpsState = _MbgLtRefGpsState_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 5),
    _MbgLtRefGpsState_Type()
)
mbgLtRefGpsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtRefGpsState.setStatus("current")


class _MbgLtRefGpsStateVal_Type(Integer32):
    """Custom type mbgLtRefGpsStateVal based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notavailable", 0),
          ("notsynchronized", 2),
          ("synchronized", 1))
    )


_MbgLtRefGpsStateVal_Type.__name__ = "Integer32"
_MbgLtRefGpsStateVal_Object = MibScalar
mbgLtRefGpsStateVal = _MbgLtRefGpsStateVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 6),
    _MbgLtRefGpsStateVal_Type()
)
mbgLtRefGpsStateVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtRefGpsStateVal.setStatus("current")
_MbgLtRefGpsPosition_Type = DisplayString
_MbgLtRefGpsPosition_Object = MibScalar
mbgLtRefGpsPosition = _MbgLtRefGpsPosition_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 7),
    _MbgLtRefGpsPosition_Type()
)
mbgLtRefGpsPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtRefGpsPosition.setStatus("current")
_MbgLtRefGpsSatellites_Type = DisplayString
_MbgLtRefGpsSatellites_Object = MibScalar
mbgLtRefGpsSatellites = _MbgLtRefGpsSatellites_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 8),
    _MbgLtRefGpsSatellites_Type()
)
mbgLtRefGpsSatellites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtRefGpsSatellites.setStatus("current")


class _MbgLtRefGpsSatellitesGood_Type(Integer32):
    """Custom type mbgLtRefGpsSatellitesGood based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_MbgLtRefGpsSatellitesGood_Type.__name__ = "Integer32"
_MbgLtRefGpsSatellitesGood_Object = MibScalar
mbgLtRefGpsSatellitesGood = _MbgLtRefGpsSatellitesGood_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 9),
    _MbgLtRefGpsSatellitesGood_Type()
)
mbgLtRefGpsSatellitesGood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtRefGpsSatellitesGood.setStatus("current")


class _MbgLtRefGpsSatellitesInView_Type(Integer32):
    """Custom type mbgLtRefGpsSatellitesInView based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_MbgLtRefGpsSatellitesInView_Type.__name__ = "Integer32"
_MbgLtRefGpsSatellitesInView_Object = MibScalar
mbgLtRefGpsSatellitesInView = _MbgLtRefGpsSatellitesInView_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 10),
    _MbgLtRefGpsSatellitesInView_Type()
)
mbgLtRefGpsSatellitesInView.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtRefGpsSatellitesInView.setStatus("current")
_MbgLtRefPzfState_Type = DisplayString
_MbgLtRefPzfState_Object = MibScalar
mbgLtRefPzfState = _MbgLtRefPzfState_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 11),
    _MbgLtRefPzfState_Type()
)
mbgLtRefPzfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtRefPzfState.setStatus("current")


class _MbgLtRefPzfStateVal_Type(Integer32):
    """Custom type mbgLtRefPzfStateVal based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("neversynced", 3),
          ("notavailable", 0),
          ("notsyncnow", 2),
          ("sync", 1))
    )


_MbgLtRefPzfStateVal_Type.__name__ = "Integer32"
_MbgLtRefPzfStateVal_Object = MibScalar
mbgLtRefPzfStateVal = _MbgLtRefPzfStateVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 12),
    _MbgLtRefPzfStateVal_Type()
)
mbgLtRefPzfStateVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtRefPzfStateVal.setStatus("current")


class _MbgLtRefPzfKorrelation_Type(Integer32):
    """Custom type mbgLtRefPzfKorrelation based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MbgLtRefPzfKorrelation_Type.__name__ = "Integer32"
_MbgLtRefPzfKorrelation_Object = MibScalar
mbgLtRefPzfKorrelation = _MbgLtRefPzfKorrelation_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 13),
    _MbgLtRefPzfKorrelation_Type()
)
mbgLtRefPzfKorrelation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtRefPzfKorrelation.setStatus("current")


class _MbgLtRefPzfField_Type(Integer32):
    """Custom type mbgLtRefPzfField based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_MbgLtRefPzfField_Type.__name__ = "Integer32"
_MbgLtRefPzfField_Object = MibScalar
mbgLtRefPzfField = _MbgLtRefPzfField_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 14),
    _MbgLtRefPzfField_Type()
)
mbgLtRefPzfField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtRefPzfField.setStatus("current")
_MbgLtRefGpsMode_Type = DisplayString
_MbgLtRefGpsMode_Object = MibScalar
mbgLtRefGpsMode = _MbgLtRefGpsMode_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 15),
    _MbgLtRefGpsMode_Type()
)
mbgLtRefGpsMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtRefGpsMode.setStatus("current")


class _MbgLtRefGpsModeVal_Type(Integer32):
    """Custom type mbgLtRefGpsModeVal based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("antennaFaulty", 3),
          ("antennaShortcircuit", 6),
          ("coldBoot", 5),
          ("normalOperation", 1),
          ("notavailable", 0),
          ("trackingSearching", 2),
          ("warmBoot", 4))
    )


_MbgLtRefGpsModeVal_Type.__name__ = "Integer32"
_MbgLtRefGpsModeVal_Object = MibScalar
mbgLtRefGpsModeVal = _MbgLtRefGpsModeVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 16),
    _MbgLtRefGpsModeVal_Type()
)
mbgLtRefGpsModeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtRefGpsModeVal.setStatus("current")
_MbgLtRefIrigMode_Type = DisplayString
_MbgLtRefIrigMode_Object = MibScalar
mbgLtRefIrigMode = _MbgLtRefIrigMode_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 17),
    _MbgLtRefIrigMode_Type()
)
mbgLtRefIrigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtRefIrigMode.setStatus("current")


class _MbgLtRefIrigModeVal_Type(Integer32):
    """Custom type mbgLtRefIrigModeVal based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("notavailable", 0),
          ("notlocked", 2),
          ("telegramError", 3))
    )


_MbgLtRefIrigModeVal_Type.__name__ = "Integer32"
_MbgLtRefIrigModeVal_Object = MibScalar
mbgLtRefIrigModeVal = _MbgLtRefIrigModeVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 18),
    _MbgLtRefIrigModeVal_Type()
)
mbgLtRefIrigModeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtRefIrigModeVal.setStatus("current")
_MbgLtRefPzfMode_Type = DisplayString
_MbgLtRefPzfMode_Object = MibScalar
mbgLtRefPzfMode = _MbgLtRefPzfMode_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 19),
    _MbgLtRefPzfMode_Type()
)
mbgLtRefPzfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtRefPzfMode.setStatus("current")


class _MbgLtRefPzfModeVal_Type(Integer32):
    """Custom type mbgLtRefPzfModeVal based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("antennaFaulty", 2),
          ("normalOperation", 1),
          ("notavailable", 0))
    )


_MbgLtRefPzfModeVal_Type.__name__ = "Integer32"
_MbgLtRefPzfModeVal_Object = MibScalar
mbgLtRefPzfModeVal = _MbgLtRefPzfModeVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 20),
    _MbgLtRefPzfModeVal_Type()
)
mbgLtRefPzfModeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtRefPzfModeVal.setStatus("current")
_MbgLtRefIrigState_Type = DisplayString
_MbgLtRefIrigState_Object = MibScalar
mbgLtRefIrigState = _MbgLtRefIrigState_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 21),
    _MbgLtRefIrigState_Type()
)
mbgLtRefIrigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtRefIrigState.setStatus("current")


class _MbgLtRefIrigStateVal_Type(Integer32):
    """Custom type mbgLtRefIrigStateVal based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_MbgLtRefIrigStateVal_Type.__name__ = "Integer32"
_MbgLtRefIrigStateVal_Object = MibScalar
mbgLtRefIrigStateVal = _MbgLtRefIrigStateVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 22),
    _MbgLtRefIrigStateVal_Type()
)
mbgLtRefIrigStateVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtRefIrigStateVal.setStatus("current")
_MbgLtRefSHSMode_Type = DisplayString
_MbgLtRefSHSMode_Object = MibScalar
mbgLtRefSHSMode = _MbgLtRefSHSMode_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 23),
    _MbgLtRefSHSMode_Type()
)
mbgLtRefSHSMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtRefSHSMode.setStatus("current")


class _MbgLtRefSHSModeVal_Type(Integer32):
    """Custom type mbgLtRefSHSModeVal based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalOperation", 1),
          ("notavailable", 0),
          ("stoppedTimeLimitError", 2))
    )


_MbgLtRefSHSModeVal_Type.__name__ = "Integer32"
_MbgLtRefSHSModeVal_Object = MibScalar
mbgLtRefSHSModeVal = _MbgLtRefSHSModeVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 24),
    _MbgLtRefSHSModeVal_Type()
)
mbgLtRefSHSModeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtRefSHSModeVal.setStatus("current")


class _MbgLtRefSHSTimeDiff_Type(Integer32):
    """Custom type mbgLtRefSHSTimeDiff based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_MbgLtRefSHSTimeDiff_Type.__name__ = "Integer32"
_MbgLtRefSHSTimeDiff_Object = MibScalar
mbgLtRefSHSTimeDiff = _MbgLtRefSHSTimeDiff_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 25),
    _MbgLtRefSHSTimeDiff_Type()
)
mbgLtRefSHSTimeDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtRefSHSTimeDiff.setStatus("current")
_MbgLtRefDctState_Type = DisplayString
_MbgLtRefDctState_Object = MibScalar
mbgLtRefDctState = _MbgLtRefDctState_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 26),
    _MbgLtRefDctState_Type()
)
mbgLtRefDctState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtRefDctState.setStatus("current")


class _MbgLtRefDctStateVal_Type(Integer32):
    """Custom type mbgLtRefDctStateVal based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("neversynced", 3),
          ("notavailable", 0),
          ("notsyncnow", 2),
          ("sync", 1))
    )


_MbgLtRefDctStateVal_Type.__name__ = "Integer32"
_MbgLtRefDctStateVal_Object = MibScalar
mbgLtRefDctStateVal = _MbgLtRefDctStateVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 27),
    _MbgLtRefDctStateVal_Type()
)
mbgLtRefDctStateVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtRefDctStateVal.setStatus("current")


class _MbgLtRefDctField_Type(DisplayString):
    """Custom type mbgLtRefDctField based on DisplayString"""
    defaultValue = OctetString("0")


_MbgLtRefDctField_Object = MibScalar
mbgLtRefDctField = _MbgLtRefDctField_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 28),
    _MbgLtRefDctField_Type()
)
mbgLtRefDctField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtRefDctField.setStatus("current")
_MbgLtRefDctMode_Type = DisplayString
_MbgLtRefDctMode_Object = MibScalar
mbgLtRefDctMode = _MbgLtRefDctMode_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 29),
    _MbgLtRefDctMode_Type()
)
mbgLtRefDctMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtRefDctMode.setStatus("current")


class _MbgLtRefDctModeVal_Type(Integer32):
    """Custom type mbgLtRefDctModeVal based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("antennaFaulty", 2),
          ("normalOperation", 1),
          ("notavailable", 0))
    )


_MbgLtRefDctModeVal_Type.__name__ = "Integer32"
_MbgLtRefDctModeVal_Object = MibScalar
mbgLtRefDctModeVal = _MbgLtRefDctModeVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 30),
    _MbgLtRefDctModeVal_Type()
)
mbgLtRefDctModeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtRefDctModeVal.setStatus("current")
_MbgLtRefGpsLeapSecond_Type = DisplayString
_MbgLtRefGpsLeapSecond_Object = MibScalar
mbgLtRefGpsLeapSecond = _MbgLtRefGpsLeapSecond_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 31),
    _MbgLtRefGpsLeapSecond_Type()
)
mbgLtRefGpsLeapSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtRefGpsLeapSecond.setStatus("current")


class _MbgLtRefGpsLeapCorrection_Type(Integer32):
    """Custom type mbgLtRefGpsLeapCorrection based on Integer32"""
    defaultValue = 0


_MbgLtRefGpsLeapCorrection_Object = MibScalar
mbgLtRefGpsLeapCorrection = _MbgLtRefGpsLeapCorrection_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 32),
    _MbgLtRefGpsLeapCorrection_Type()
)
mbgLtRefGpsLeapCorrection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtRefGpsLeapCorrection.setStatus("current")
_MbgLtMrs_ObjectIdentity = ObjectIdentity
mbgLtMrs = _MbgLtMrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50)
)
_MbgLtRefMrsRef_Type = DisplayString
_MbgLtRefMrsRef_Object = MibScalar
mbgLtRefMrsRef = _MbgLtRefMrsRef_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 1),
    _MbgLtRefMrsRef_Type()
)
mbgLtRefMrsRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtRefMrsRef.setStatus("current")


class _MbgLtRefMrsRefVal_Type(Integer32):
    """Custom type mbgLtRefMrsRefVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              99)
        )
    )
    namedValues = NamedValues(
        *(("notavailable", 0),
          ("refFreeRun", 99),
          ("refFreq", 4),
          ("refGps", 1),
          ("refIrig", 2),
          ("refNtp", 6),
          ("refPps", 3),
          ("refPtp", 5))
    )


_MbgLtRefMrsRefVal_Type.__name__ = "Integer32"
_MbgLtRefMrsRefVal_Object = MibScalar
mbgLtRefMrsRefVal = _MbgLtRefMrsRefVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 2),
    _MbgLtRefMrsRefVal_Type()
)
mbgLtRefMrsRefVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtRefMrsRefVal.setStatus("current")
_MbgLtRefMrsRefList_Type = DisplayString
_MbgLtRefMrsRefList_Object = MibScalar
mbgLtRefMrsRefList = _MbgLtRefMrsRefList_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 3),
    _MbgLtRefMrsRefList_Type()
)
mbgLtRefMrsRefList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtRefMrsRefList.setStatus("current")
_MbgLtRefMrsPrioList_Type = DisplayString
_MbgLtRefMrsPrioList_Object = MibScalar
mbgLtRefMrsPrioList = _MbgLtRefMrsPrioList_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 4),
    _MbgLtRefMrsPrioList_Type()
)
mbgLtRefMrsPrioList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtRefMrsPrioList.setStatus("current")
_MbgLtMrsRef_ObjectIdentity = ObjectIdentity
mbgLtMrsRef = _MbgLtMrsRef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10)
)
_MbgLtMrsRefGps_ObjectIdentity = ObjectIdentity
mbgLtMrsRefGps = _MbgLtMrsRefGps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 1)
)
_MbgLtMrsGpsOffs_Type = DisplayString
_MbgLtMrsGpsOffs_Object = MibScalar
mbgLtMrsGpsOffs = _MbgLtMrsGpsOffs_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 1, 1),
    _MbgLtMrsGpsOffs_Type()
)
mbgLtMrsGpsOffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtMrsGpsOffs.setStatus("current")
_MbgLtMrsGpsOffsVal_Type = Integer32
_MbgLtMrsGpsOffsVal_Object = MibScalar
mbgLtMrsGpsOffsVal = _MbgLtMrsGpsOffsVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 1, 2),
    _MbgLtMrsGpsOffsVal_Type()
)
mbgLtMrsGpsOffsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtMrsGpsOffsVal.setStatus("current")


class _MbgLtMrsGpsOffsBase_Type(Integer32):
    """Custom type mbgLtMrsGpsOffsBase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              6,
              9)
        )
    )
    namedValues = NamedValues(
        *(("baseMicroseconds", 6),
          ("baseMiliseconds", 3),
          ("baseNanoseconds", 9),
          ("baseSeconds", 0))
    )


_MbgLtMrsGpsOffsBase_Type.__name__ = "Integer32"
_MbgLtMrsGpsOffsBase_Object = MibScalar
mbgLtMrsGpsOffsBase = _MbgLtMrsGpsOffsBase_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 1, 3),
    _MbgLtMrsGpsOffsBase_Type()
)
mbgLtMrsGpsOffsBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtMrsGpsOffsBase.setStatus("current")
_MbgLtMrsGpsPrio_Type = Integer32
_MbgLtMrsGpsPrio_Object = MibScalar
mbgLtMrsGpsPrio = _MbgLtMrsGpsPrio_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 1, 4),
    _MbgLtMrsGpsPrio_Type()
)
mbgLtMrsGpsPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtMrsGpsPrio.setStatus("current")
_MbgLtMrsGpsState_Type = DisplayString
_MbgLtMrsGpsState_Object = MibScalar
mbgLtMrsGpsState = _MbgLtMrsGpsState_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 1, 5),
    _MbgLtMrsGpsState_Type()
)
mbgLtMrsGpsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtMrsGpsState.setStatus("current")


class _MbgLtMrsGpsStateVal_Type(Integer32):
    """Custom type mbgLtMrsGpsStateVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("hasLocked", 4),
          ("isAccurate", 6),
          ("isAvailable", 5),
          ("isMaster", 7),
          ("noSignal", 3),
          ("notAvailable", 0),
          ("notConnected", 2),
          ("notSupported", 1))
    )


_MbgLtMrsGpsStateVal_Type.__name__ = "Integer32"
_MbgLtMrsGpsStateVal_Object = MibScalar
mbgLtMrsGpsStateVal = _MbgLtMrsGpsStateVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 1, 6),
    _MbgLtMrsGpsStateVal_Type()
)
mbgLtMrsGpsStateVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtMrsGpsStateVal.setStatus("current")
_MbgLtMrsGpsPrecision_Type = Integer32
_MbgLtMrsGpsPrecision_Object = MibScalar
mbgLtMrsGpsPrecision = _MbgLtMrsGpsPrecision_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 1, 7),
    _MbgLtMrsGpsPrecision_Type()
)
mbgLtMrsGpsPrecision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtMrsGpsPrecision.setStatus("current")
_MbgLtMrsRefIrig_ObjectIdentity = ObjectIdentity
mbgLtMrsRefIrig = _MbgLtMrsRefIrig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 2)
)
_MbgLtMrsIrigOffs_Type = DisplayString
_MbgLtMrsIrigOffs_Object = MibScalar
mbgLtMrsIrigOffs = _MbgLtMrsIrigOffs_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 2, 1),
    _MbgLtMrsIrigOffs_Type()
)
mbgLtMrsIrigOffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtMrsIrigOffs.setStatus("current")
_MbgLtMrsIrigOffsVal_Type = Integer32
_MbgLtMrsIrigOffsVal_Object = MibScalar
mbgLtMrsIrigOffsVal = _MbgLtMrsIrigOffsVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 2, 2),
    _MbgLtMrsIrigOffsVal_Type()
)
mbgLtMrsIrigOffsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtMrsIrigOffsVal.setStatus("current")


class _MbgLtMrsIrigOffsBase_Type(Integer32):
    """Custom type mbgLtMrsIrigOffsBase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              6,
              9)
        )
    )
    namedValues = NamedValues(
        *(("baseMicroseconds", 6),
          ("baseMiliseconds", 3),
          ("baseNanoseconds", 9),
          ("baseSeconds", 0))
    )


_MbgLtMrsIrigOffsBase_Type.__name__ = "Integer32"
_MbgLtMrsIrigOffsBase_Object = MibScalar
mbgLtMrsIrigOffsBase = _MbgLtMrsIrigOffsBase_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 2, 3),
    _MbgLtMrsIrigOffsBase_Type()
)
mbgLtMrsIrigOffsBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtMrsIrigOffsBase.setStatus("current")
_MbgLtMrsIrigPrio_Type = Integer32
_MbgLtMrsIrigPrio_Object = MibScalar
mbgLtMrsIrigPrio = _MbgLtMrsIrigPrio_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 2, 4),
    _MbgLtMrsIrigPrio_Type()
)
mbgLtMrsIrigPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtMrsIrigPrio.setStatus("current")
_MbgLtMrsIrigState_Type = DisplayString
_MbgLtMrsIrigState_Object = MibScalar
mbgLtMrsIrigState = _MbgLtMrsIrigState_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 2, 5),
    _MbgLtMrsIrigState_Type()
)
mbgLtMrsIrigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtMrsIrigState.setStatus("current")


class _MbgLtMrsIrigStateVal_Type(Integer32):
    """Custom type mbgLtMrsIrigStateVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("hasLocked", 4),
          ("isAccurate", 6),
          ("isAvailable", 5),
          ("isMaster", 7),
          ("noSignal", 3),
          ("notAvailable", 0),
          ("notConnected", 2),
          ("notSupported", 1))
    )


_MbgLtMrsIrigStateVal_Type.__name__ = "Integer32"
_MbgLtMrsIrigStateVal_Object = MibScalar
mbgLtMrsIrigStateVal = _MbgLtMrsIrigStateVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 2, 6),
    _MbgLtMrsIrigStateVal_Type()
)
mbgLtMrsIrigStateVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtMrsIrigStateVal.setStatus("current")
_MbgLtMrsIrigCorr_Type = Integer32
_MbgLtMrsIrigCorr_Object = MibScalar
mbgLtMrsIrigCorr = _MbgLtMrsIrigCorr_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 2, 7),
    _MbgLtMrsIrigCorr_Type()
)
mbgLtMrsIrigCorr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtMrsIrigCorr.setStatus("current")
_MbgLtMrsIrigOffsLimit_Type = Integer32
_MbgLtMrsIrigOffsLimit_Object = MibScalar
mbgLtMrsIrigOffsLimit = _MbgLtMrsIrigOffsLimit_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 2, 8),
    _MbgLtMrsIrigOffsLimit_Type()
)
mbgLtMrsIrigOffsLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtMrsIrigOffsLimit.setStatus("current")
_MbgLtMrsIrigPrecision_Type = Integer32
_MbgLtMrsIrigPrecision_Object = MibScalar
mbgLtMrsIrigPrecision = _MbgLtMrsIrigPrecision_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 2, 9),
    _MbgLtMrsIrigPrecision_Type()
)
mbgLtMrsIrigPrecision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtMrsIrigPrecision.setStatus("current")
_MbgLtMrsRefPps_ObjectIdentity = ObjectIdentity
mbgLtMrsRefPps = _MbgLtMrsRefPps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 3)
)
_MbgLtMrsPpsOffs_Type = DisplayString
_MbgLtMrsPpsOffs_Object = MibScalar
mbgLtMrsPpsOffs = _MbgLtMrsPpsOffs_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 3, 1),
    _MbgLtMrsPpsOffs_Type()
)
mbgLtMrsPpsOffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtMrsPpsOffs.setStatus("current")
_MbgLtMrsPpsOffsVal_Type = Integer32
_MbgLtMrsPpsOffsVal_Object = MibScalar
mbgLtMrsPpsOffsVal = _MbgLtMrsPpsOffsVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 3, 2),
    _MbgLtMrsPpsOffsVal_Type()
)
mbgLtMrsPpsOffsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtMrsPpsOffsVal.setStatus("current")


class _MbgLtMrsPpsOffsBase_Type(Integer32):
    """Custom type mbgLtMrsPpsOffsBase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              6,
              9)
        )
    )
    namedValues = NamedValues(
        *(("baseMicroseconds", 6),
          ("baseMiliseconds", 3),
          ("baseNanoseconds", 9),
          ("baseSeconds", 0))
    )


_MbgLtMrsPpsOffsBase_Type.__name__ = "Integer32"
_MbgLtMrsPpsOffsBase_Object = MibScalar
mbgLtMrsPpsOffsBase = _MbgLtMrsPpsOffsBase_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 3, 3),
    _MbgLtMrsPpsOffsBase_Type()
)
mbgLtMrsPpsOffsBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtMrsPpsOffsBase.setStatus("current")
_MbgLtMrsPpsPrio_Type = Integer32
_MbgLtMrsPpsPrio_Object = MibScalar
mbgLtMrsPpsPrio = _MbgLtMrsPpsPrio_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 3, 4),
    _MbgLtMrsPpsPrio_Type()
)
mbgLtMrsPpsPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtMrsPpsPrio.setStatus("current")
_MbgLtMrsPpsState_Type = DisplayString
_MbgLtMrsPpsState_Object = MibScalar
mbgLtMrsPpsState = _MbgLtMrsPpsState_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 3, 5),
    _MbgLtMrsPpsState_Type()
)
mbgLtMrsPpsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtMrsPpsState.setStatus("current")


class _MbgLtMrsPpsStateVal_Type(Integer32):
    """Custom type mbgLtMrsPpsStateVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("hasLocked", 4),
          ("isAccurate", 6),
          ("isAvailable", 5),
          ("isMaster", 7),
          ("noSignal", 3),
          ("notAvailable", 0),
          ("notConnected", 2),
          ("notSupported", 1))
    )


_MbgLtMrsPpsStateVal_Type.__name__ = "Integer32"
_MbgLtMrsPpsStateVal_Object = MibScalar
mbgLtMrsPpsStateVal = _MbgLtMrsPpsStateVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 3, 6),
    _MbgLtMrsPpsStateVal_Type()
)
mbgLtMrsPpsStateVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtMrsPpsStateVal.setStatus("current")
_MbgLtMrsPpsCorr_Type = Integer32
_MbgLtMrsPpsCorr_Object = MibScalar
mbgLtMrsPpsCorr = _MbgLtMrsPpsCorr_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 3, 7),
    _MbgLtMrsPpsCorr_Type()
)
mbgLtMrsPpsCorr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtMrsPpsCorr.setStatus("current")
_MbgLtMrsPpsOffsLimit_Type = Integer32
_MbgLtMrsPpsOffsLimit_Object = MibScalar
mbgLtMrsPpsOffsLimit = _MbgLtMrsPpsOffsLimit_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 3, 8),
    _MbgLtMrsPpsOffsLimit_Type()
)
mbgLtMrsPpsOffsLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtMrsPpsOffsLimit.setStatus("current")
_MbgLtMrsPpsPrecision_Type = Integer32
_MbgLtMrsPpsPrecision_Object = MibScalar
mbgLtMrsPpsPrecision = _MbgLtMrsPpsPrecision_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 3, 9),
    _MbgLtMrsPpsPrecision_Type()
)
mbgLtMrsPpsPrecision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtMrsPpsPrecision.setStatus("current")
_MbgLtMrsRefFreq_ObjectIdentity = ObjectIdentity
mbgLtMrsRefFreq = _MbgLtMrsRefFreq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 4)
)
_MbgLtMrsFreqOffs_Type = DisplayString
_MbgLtMrsFreqOffs_Object = MibScalar
mbgLtMrsFreqOffs = _MbgLtMrsFreqOffs_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 4, 1),
    _MbgLtMrsFreqOffs_Type()
)
mbgLtMrsFreqOffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtMrsFreqOffs.setStatus("current")
_MbgLtMrsFreqOffsVal_Type = Integer32
_MbgLtMrsFreqOffsVal_Object = MibScalar
mbgLtMrsFreqOffsVal = _MbgLtMrsFreqOffsVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 4, 2),
    _MbgLtMrsFreqOffsVal_Type()
)
mbgLtMrsFreqOffsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtMrsFreqOffsVal.setStatus("current")


class _MbgLtMrsFreqOffsBase_Type(Integer32):
    """Custom type mbgLtMrsFreqOffsBase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              6,
              9)
        )
    )
    namedValues = NamedValues(
        *(("baseMicroseconds", 6),
          ("baseMiliseconds", 3),
          ("baseNanoseconds", 9),
          ("baseSeconds", 0))
    )


_MbgLtMrsFreqOffsBase_Type.__name__ = "Integer32"
_MbgLtMrsFreqOffsBase_Object = MibScalar
mbgLtMrsFreqOffsBase = _MbgLtMrsFreqOffsBase_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 4, 3),
    _MbgLtMrsFreqOffsBase_Type()
)
mbgLtMrsFreqOffsBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtMrsFreqOffsBase.setStatus("current")
_MbgLtMrsFreqPrio_Type = Integer32
_MbgLtMrsFreqPrio_Object = MibScalar
mbgLtMrsFreqPrio = _MbgLtMrsFreqPrio_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 4, 4),
    _MbgLtMrsFreqPrio_Type()
)
mbgLtMrsFreqPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtMrsFreqPrio.setStatus("current")
_MbgLtMrsFreqState_Type = DisplayString
_MbgLtMrsFreqState_Object = MibScalar
mbgLtMrsFreqState = _MbgLtMrsFreqState_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 4, 5),
    _MbgLtMrsFreqState_Type()
)
mbgLtMrsFreqState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtMrsFreqState.setStatus("current")


class _MbgLtMrsFreqStateVal_Type(Integer32):
    """Custom type mbgLtMrsFreqStateVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("hasLocked", 4),
          ("isAccurate", 6),
          ("isAvailable", 5),
          ("isMaster", 7),
          ("noSignal", 3),
          ("notAvailable", 0),
          ("notConnected", 2),
          ("notSupported", 1))
    )


_MbgLtMrsFreqStateVal_Type.__name__ = "Integer32"
_MbgLtMrsFreqStateVal_Object = MibScalar
mbgLtMrsFreqStateVal = _MbgLtMrsFreqStateVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 4, 6),
    _MbgLtMrsFreqStateVal_Type()
)
mbgLtMrsFreqStateVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtMrsFreqStateVal.setStatus("current")
_MbgLtMrsFreqCorr_Type = Integer32
_MbgLtMrsFreqCorr_Object = MibScalar
mbgLtMrsFreqCorr = _MbgLtMrsFreqCorr_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 4, 7),
    _MbgLtMrsFreqCorr_Type()
)
mbgLtMrsFreqCorr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtMrsFreqCorr.setStatus("current")
_MbgLtMrsFreqOffsLimit_Type = Integer32
_MbgLtMrsFreqOffsLimit_Object = MibScalar
mbgLtMrsFreqOffsLimit = _MbgLtMrsFreqOffsLimit_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 4, 8),
    _MbgLtMrsFreqOffsLimit_Type()
)
mbgLtMrsFreqOffsLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtMrsFreqOffsLimit.setStatus("current")
_MbgLtMrsFreqPrecision_Type = Integer32
_MbgLtMrsFreqPrecision_Object = MibScalar
mbgLtMrsFreqPrecision = _MbgLtMrsFreqPrecision_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 4, 9),
    _MbgLtMrsFreqPrecision_Type()
)
mbgLtMrsFreqPrecision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtMrsFreqPrecision.setStatus("current")
_MbgLtMrsRefPtp_ObjectIdentity = ObjectIdentity
mbgLtMrsRefPtp = _MbgLtMrsRefPtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 5)
)
_MbgLtMrsPtpOffs_Type = DisplayString
_MbgLtMrsPtpOffs_Object = MibScalar
mbgLtMrsPtpOffs = _MbgLtMrsPtpOffs_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 5, 1),
    _MbgLtMrsPtpOffs_Type()
)
mbgLtMrsPtpOffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtMrsPtpOffs.setStatus("current")
_MbgLtMrsPtpOffsVal_Type = Integer32
_MbgLtMrsPtpOffsVal_Object = MibScalar
mbgLtMrsPtpOffsVal = _MbgLtMrsPtpOffsVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 5, 2),
    _MbgLtMrsPtpOffsVal_Type()
)
mbgLtMrsPtpOffsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtMrsPtpOffsVal.setStatus("current")


class _MbgLtMrsPtpOffsBase_Type(Integer32):
    """Custom type mbgLtMrsPtpOffsBase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              6,
              9)
        )
    )
    namedValues = NamedValues(
        *(("baseMicroseconds", 6),
          ("baseMiliseconds", 3),
          ("baseNanoseconds", 9),
          ("baseSeconds", 0))
    )


_MbgLtMrsPtpOffsBase_Type.__name__ = "Integer32"
_MbgLtMrsPtpOffsBase_Object = MibScalar
mbgLtMrsPtpOffsBase = _MbgLtMrsPtpOffsBase_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 5, 3),
    _MbgLtMrsPtpOffsBase_Type()
)
mbgLtMrsPtpOffsBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtMrsPtpOffsBase.setStatus("current")
_MbgLtMrsPtpPrio_Type = Integer32
_MbgLtMrsPtpPrio_Object = MibScalar
mbgLtMrsPtpPrio = _MbgLtMrsPtpPrio_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 5, 4),
    _MbgLtMrsPtpPrio_Type()
)
mbgLtMrsPtpPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtMrsPtpPrio.setStatus("current")
_MbgLtMrsPtpState_Type = DisplayString
_MbgLtMrsPtpState_Object = MibScalar
mbgLtMrsPtpState = _MbgLtMrsPtpState_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 5, 5),
    _MbgLtMrsPtpState_Type()
)
mbgLtMrsPtpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtMrsPtpState.setStatus("current")


class _MbgLtMrsPtpStateVal_Type(Integer32):
    """Custom type mbgLtMrsPtpStateVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("hasLocked", 4),
          ("isAccurate", 6),
          ("isAvailable", 5),
          ("isMaster", 7),
          ("noSignal", 3),
          ("notAvailable", 0),
          ("notConnected", 2),
          ("notSupported", 1))
    )


_MbgLtMrsPtpStateVal_Type.__name__ = "Integer32"
_MbgLtMrsPtpStateVal_Object = MibScalar
mbgLtMrsPtpStateVal = _MbgLtMrsPtpStateVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 5, 6),
    _MbgLtMrsPtpStateVal_Type()
)
mbgLtMrsPtpStateVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtMrsPtpStateVal.setStatus("current")
_MbgLtMrsPtpCorr_Type = Integer32
_MbgLtMrsPtpCorr_Object = MibScalar
mbgLtMrsPtpCorr = _MbgLtMrsPtpCorr_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 5, 7),
    _MbgLtMrsPtpCorr_Type()
)
mbgLtMrsPtpCorr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtMrsPtpCorr.setStatus("current")
_MbgLtMrsPtpOffsLimit_Type = Integer32
_MbgLtMrsPtpOffsLimit_Object = MibScalar
mbgLtMrsPtpOffsLimit = _MbgLtMrsPtpOffsLimit_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 5, 8),
    _MbgLtMrsPtpOffsLimit_Type()
)
mbgLtMrsPtpOffsLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtMrsPtpOffsLimit.setStatus("current")
_MbgLtMrsPtpPrecision_Type = Integer32
_MbgLtMrsPtpPrecision_Object = MibScalar
mbgLtMrsPtpPrecision = _MbgLtMrsPtpPrecision_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 5, 9),
    _MbgLtMrsPtpPrecision_Type()
)
mbgLtMrsPtpPrecision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtMrsPtpPrecision.setStatus("current")
_MbgLtMrsRefNtp_ObjectIdentity = ObjectIdentity
mbgLtMrsRefNtp = _MbgLtMrsRefNtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 6)
)
_MbgLtMrsNtpOffs_Type = DisplayString
_MbgLtMrsNtpOffs_Object = MibScalar
mbgLtMrsNtpOffs = _MbgLtMrsNtpOffs_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 6, 1),
    _MbgLtMrsNtpOffs_Type()
)
mbgLtMrsNtpOffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtMrsNtpOffs.setStatus("current")
_MbgLtMrsNtpOffsVal_Type = Integer32
_MbgLtMrsNtpOffsVal_Object = MibScalar
mbgLtMrsNtpOffsVal = _MbgLtMrsNtpOffsVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 6, 2),
    _MbgLtMrsNtpOffsVal_Type()
)
mbgLtMrsNtpOffsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtMrsNtpOffsVal.setStatus("current")


class _MbgLtMrsNtpOffsBase_Type(Integer32):
    """Custom type mbgLtMrsNtpOffsBase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              6,
              9)
        )
    )
    namedValues = NamedValues(
        *(("baseMicroseconds", 6),
          ("baseMiliseconds", 3),
          ("baseNanoseconds", 9),
          ("baseSeconds", 0))
    )


_MbgLtMrsNtpOffsBase_Type.__name__ = "Integer32"
_MbgLtMrsNtpOffsBase_Object = MibScalar
mbgLtMrsNtpOffsBase = _MbgLtMrsNtpOffsBase_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 6, 3),
    _MbgLtMrsNtpOffsBase_Type()
)
mbgLtMrsNtpOffsBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtMrsNtpOffsBase.setStatus("current")
_MbgLtMrsNtpPrio_Type = Integer32
_MbgLtMrsNtpPrio_Object = MibScalar
mbgLtMrsNtpPrio = _MbgLtMrsNtpPrio_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 6, 4),
    _MbgLtMrsNtpPrio_Type()
)
mbgLtMrsNtpPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtMrsNtpPrio.setStatus("current")
_MbgLtMrsNtpState_Type = DisplayString
_MbgLtMrsNtpState_Object = MibScalar
mbgLtMrsNtpState = _MbgLtMrsNtpState_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 6, 5),
    _MbgLtMrsNtpState_Type()
)
mbgLtMrsNtpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtMrsNtpState.setStatus("current")


class _MbgLtMrsNtpStateVal_Type(Integer32):
    """Custom type mbgLtMrsNtpStateVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("hasLocked", 4),
          ("isAccurate", 6),
          ("isAvailable", 5),
          ("isMaster", 7),
          ("noSignal", 3),
          ("notAvailable", 0),
          ("notConnected", 2),
          ("notSupported", 1))
    )


_MbgLtMrsNtpStateVal_Type.__name__ = "Integer32"
_MbgLtMrsNtpStateVal_Object = MibScalar
mbgLtMrsNtpStateVal = _MbgLtMrsNtpStateVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 6, 6),
    _MbgLtMrsNtpStateVal_Type()
)
mbgLtMrsNtpStateVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtMrsNtpStateVal.setStatus("current")
_MbgLtMrsNtpCorr_Type = Integer32
_MbgLtMrsNtpCorr_Object = MibScalar
mbgLtMrsNtpCorr = _MbgLtMrsNtpCorr_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 6, 7),
    _MbgLtMrsNtpCorr_Type()
)
mbgLtMrsNtpCorr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtMrsNtpCorr.setStatus("current")
_MbgLtMrsNtpOffsLimit_Type = Integer32
_MbgLtMrsNtpOffsLimit_Object = MibScalar
mbgLtMrsNtpOffsLimit = _MbgLtMrsNtpOffsLimit_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 6, 8),
    _MbgLtMrsNtpOffsLimit_Type()
)
mbgLtMrsNtpOffsLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtMrsNtpOffsLimit.setStatus("current")
_MbgLtMrsNtpPrecision_Type = Integer32
_MbgLtMrsNtpPrecision_Object = MibScalar
mbgLtMrsNtpPrecision = _MbgLtMrsNtpPrecision_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 2, 50, 10, 6, 9),
    _MbgLtMrsNtpPrecision_Type()
)
mbgLtMrsNtpPrecision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtMrsNtpPrecision.setStatus("current")
_MbgLtNotifications_ObjectIdentity = ObjectIdentity
mbgLtNotifications = _MbgLtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 3)
)
_MbgLtTraps_ObjectIdentity = ObjectIdentity
mbgLtTraps = _MbgLtTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 3, 0)
)


class _MbgLtTrapMessage_Type(DisplayString):
    """Custom type mbgLtTrapMessage based on DisplayString"""
    defaultValue = OctetString("no event")


_MbgLtTrapMessage_Object = MibScalar
mbgLtTrapMessage = _MbgLtTrapMessage_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 3, 0, 100),
    _MbgLtTrapMessage_Type()
)
mbgLtTrapMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtTrapMessage.setStatus("current")
_MbgLtCfg_ObjectIdentity = ObjectIdentity
mbgLtCfg = _MbgLtCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4)
)
_MbgLtCfgNetwork_ObjectIdentity = ObjectIdentity
mbgLtCfgNetwork = _MbgLtCfgNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 1)
)
_MbgLtCfgHostname_Type = DisplayString
_MbgLtCfgHostname_Object = MibScalar
mbgLtCfgHostname = _MbgLtCfgHostname_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 1, 1),
    _MbgLtCfgHostname_Type()
)
mbgLtCfgHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgHostname.setStatus("current")
_MbgLtCfgDomainname_Type = DisplayString
_MbgLtCfgDomainname_Object = MibScalar
mbgLtCfgDomainname = _MbgLtCfgDomainname_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 1, 2),
    _MbgLtCfgDomainname_Type()
)
mbgLtCfgDomainname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgDomainname.setStatus("current")
_MbgLtCfgNameserver1_Type = DisplayString
_MbgLtCfgNameserver1_Object = MibScalar
mbgLtCfgNameserver1 = _MbgLtCfgNameserver1_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 1, 3),
    _MbgLtCfgNameserver1_Type()
)
mbgLtCfgNameserver1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNameserver1.setStatus("current")
_MbgLtCfgNameserver2_Type = DisplayString
_MbgLtCfgNameserver2_Object = MibScalar
mbgLtCfgNameserver2 = _MbgLtCfgNameserver2_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 1, 4),
    _MbgLtCfgNameserver2_Type()
)
mbgLtCfgNameserver2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNameserver2.setStatus("current")
_MbgLtCfgSyslogserver1_Type = DisplayString
_MbgLtCfgSyslogserver1_Object = MibScalar
mbgLtCfgSyslogserver1 = _MbgLtCfgSyslogserver1_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 1, 5),
    _MbgLtCfgSyslogserver1_Type()
)
mbgLtCfgSyslogserver1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgSyslogserver1.setStatus("current")
_MbgLtCfgSyslogserver2_Type = DisplayString
_MbgLtCfgSyslogserver2_Object = MibScalar
mbgLtCfgSyslogserver2 = _MbgLtCfgSyslogserver2_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 1, 6),
    _MbgLtCfgSyslogserver2_Type()
)
mbgLtCfgSyslogserver2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgSyslogserver2.setStatus("current")


class _MbgLtCfgTelnetAccess_Type(Integer32):
    """Custom type mbgLtCfgTelnetAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgTelnetAccess_Type.__name__ = "Integer32"
_MbgLtCfgTelnetAccess_Object = MibScalar
mbgLtCfgTelnetAccess = _MbgLtCfgTelnetAccess_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 1, 7),
    _MbgLtCfgTelnetAccess_Type()
)
mbgLtCfgTelnetAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgTelnetAccess.setStatus("current")


class _MbgLtCfgFTPAccess_Type(Integer32):
    """Custom type mbgLtCfgFTPAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgFTPAccess_Type.__name__ = "Integer32"
_MbgLtCfgFTPAccess_Object = MibScalar
mbgLtCfgFTPAccess = _MbgLtCfgFTPAccess_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 1, 8),
    _MbgLtCfgFTPAccess_Type()
)
mbgLtCfgFTPAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgFTPAccess.setStatus("current")


class _MbgLtCfgHTTPAccess_Type(Integer32):
    """Custom type mbgLtCfgHTTPAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgHTTPAccess_Type.__name__ = "Integer32"
_MbgLtCfgHTTPAccess_Object = MibScalar
mbgLtCfgHTTPAccess = _MbgLtCfgHTTPAccess_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 1, 9),
    _MbgLtCfgHTTPAccess_Type()
)
mbgLtCfgHTTPAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgHTTPAccess.setStatus("current")


class _MbgLtCfgHTTPSAccess_Type(Integer32):
    """Custom type mbgLtCfgHTTPSAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgHTTPSAccess_Type.__name__ = "Integer32"
_MbgLtCfgHTTPSAccess_Object = MibScalar
mbgLtCfgHTTPSAccess = _MbgLtCfgHTTPSAccess_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 1, 10),
    _MbgLtCfgHTTPSAccess_Type()
)
mbgLtCfgHTTPSAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgHTTPSAccess.setStatus("current")


class _MbgLtCfgSNMPAccess_Type(Integer32):
    """Custom type mbgLtCfgSNMPAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgSNMPAccess_Type.__name__ = "Integer32"
_MbgLtCfgSNMPAccess_Object = MibScalar
mbgLtCfgSNMPAccess = _MbgLtCfgSNMPAccess_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 1, 11),
    _MbgLtCfgSNMPAccess_Type()
)
mbgLtCfgSNMPAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgSNMPAccess.setStatus("current")


class _MbgLtCfgSambaAccess_Type(Integer32):
    """Custom type mbgLtCfgSambaAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgSambaAccess_Type.__name__ = "Integer32"
_MbgLtCfgSambaAccess_Object = MibScalar
mbgLtCfgSambaAccess = _MbgLtCfgSambaAccess_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 1, 12),
    _MbgLtCfgSambaAccess_Type()
)
mbgLtCfgSambaAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgSambaAccess.setStatus("current")


class _MbgLtCfgIPv6Access_Type(Integer32):
    """Custom type mbgLtCfgIPv6Access based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgIPv6Access_Type.__name__ = "Integer32"
_MbgLtCfgIPv6Access_Object = MibScalar
mbgLtCfgIPv6Access = _MbgLtCfgIPv6Access_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 1, 13),
    _MbgLtCfgIPv6Access_Type()
)
mbgLtCfgIPv6Access.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgIPv6Access.setStatus("current")


class _MbgLtCfgSSHAccess_Type(Integer32):
    """Custom type mbgLtCfgSSHAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgSSHAccess_Type.__name__ = "Integer32"
_MbgLtCfgSSHAccess_Object = MibScalar
mbgLtCfgSSHAccess = _MbgLtCfgSSHAccess_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 1, 14),
    _MbgLtCfgSSHAccess_Type()
)
mbgLtCfgSSHAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgSSHAccess.setStatus("current")
_MbgLtCfgNTP_ObjectIdentity = ObjectIdentity
mbgLtCfgNTP = _MbgLtCfgNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2)
)
_MbgLtCfgNTPServer1_ObjectIdentity = ObjectIdentity
mbgLtCfgNTPServer1 = _MbgLtCfgNTPServer1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 1)
)
_MbgLtCfgNTPServer1IP_Type = DisplayString
_MbgLtCfgNTPServer1IP_Object = MibScalar
mbgLtCfgNTPServer1IP = _MbgLtCfgNTPServer1IP_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 1, 1),
    _MbgLtCfgNTPServer1IP_Type()
)
mbgLtCfgNTPServer1IP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNTPServer1IP.setStatus("current")


class _MbgLtCfgNTPServer1Key_Type(Integer32):
    """Custom type mbgLtCfgNTPServer1Key based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_MbgLtCfgNTPServer1Key_Type.__name__ = "Integer32"
_MbgLtCfgNTPServer1Key_Object = MibScalar
mbgLtCfgNTPServer1Key = _MbgLtCfgNTPServer1Key_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 1, 2),
    _MbgLtCfgNTPServer1Key_Type()
)
mbgLtCfgNTPServer1Key.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNTPServer1Key.setStatus("current")


class _MbgLtCfgNTPServer1Autokey_Type(Integer32):
    """Custom type mbgLtCfgNTPServer1Autokey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgNTPServer1Autokey_Type.__name__ = "Integer32"
_MbgLtCfgNTPServer1Autokey_Object = MibScalar
mbgLtCfgNTPServer1Autokey = _MbgLtCfgNTPServer1Autokey_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 1, 3),
    _MbgLtCfgNTPServer1Autokey_Type()
)
mbgLtCfgNTPServer1Autokey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNTPServer1Autokey.setStatus("current")


class _MbgLtCfgNTPServer1Prefer_Type(Integer32):
    """Custom type mbgLtCfgNTPServer1Prefer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgNTPServer1Prefer_Type.__name__ = "Integer32"
_MbgLtCfgNTPServer1Prefer_Object = MibScalar
mbgLtCfgNTPServer1Prefer = _MbgLtCfgNTPServer1Prefer_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 1, 4),
    _MbgLtCfgNTPServer1Prefer_Type()
)
mbgLtCfgNTPServer1Prefer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNTPServer1Prefer.setStatus("current")
_MbgLtCfgNTPServer2_ObjectIdentity = ObjectIdentity
mbgLtCfgNTPServer2 = _MbgLtCfgNTPServer2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 2)
)
_MbgLtCfgNTPServer2IP_Type = DisplayString
_MbgLtCfgNTPServer2IP_Object = MibScalar
mbgLtCfgNTPServer2IP = _MbgLtCfgNTPServer2IP_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 2, 1),
    _MbgLtCfgNTPServer2IP_Type()
)
mbgLtCfgNTPServer2IP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNTPServer2IP.setStatus("current")


class _MbgLtCfgNTPServer2Key_Type(Integer32):
    """Custom type mbgLtCfgNTPServer2Key based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_MbgLtCfgNTPServer2Key_Type.__name__ = "Integer32"
_MbgLtCfgNTPServer2Key_Object = MibScalar
mbgLtCfgNTPServer2Key = _MbgLtCfgNTPServer2Key_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 2, 2),
    _MbgLtCfgNTPServer2Key_Type()
)
mbgLtCfgNTPServer2Key.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNTPServer2Key.setStatus("current")


class _MbgLtCfgNTPServer2Autokey_Type(Integer32):
    """Custom type mbgLtCfgNTPServer2Autokey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgNTPServer2Autokey_Type.__name__ = "Integer32"
_MbgLtCfgNTPServer2Autokey_Object = MibScalar
mbgLtCfgNTPServer2Autokey = _MbgLtCfgNTPServer2Autokey_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 2, 3),
    _MbgLtCfgNTPServer2Autokey_Type()
)
mbgLtCfgNTPServer2Autokey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNTPServer2Autokey.setStatus("current")


class _MbgLtCfgNTPServer2Prefer_Type(Integer32):
    """Custom type mbgLtCfgNTPServer2Prefer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgNTPServer2Prefer_Type.__name__ = "Integer32"
_MbgLtCfgNTPServer2Prefer_Object = MibScalar
mbgLtCfgNTPServer2Prefer = _MbgLtCfgNTPServer2Prefer_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 2, 4),
    _MbgLtCfgNTPServer2Prefer_Type()
)
mbgLtCfgNTPServer2Prefer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNTPServer2Prefer.setStatus("current")
_MbgLtCfgNTPServer3_ObjectIdentity = ObjectIdentity
mbgLtCfgNTPServer3 = _MbgLtCfgNTPServer3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 3)
)
_MbgLtCfgNTPServer3IP_Type = DisplayString
_MbgLtCfgNTPServer3IP_Object = MibScalar
mbgLtCfgNTPServer3IP = _MbgLtCfgNTPServer3IP_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 3, 1),
    _MbgLtCfgNTPServer3IP_Type()
)
mbgLtCfgNTPServer3IP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNTPServer3IP.setStatus("current")


class _MbgLtCfgNTPServer3Key_Type(Integer32):
    """Custom type mbgLtCfgNTPServer3Key based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_MbgLtCfgNTPServer3Key_Type.__name__ = "Integer32"
_MbgLtCfgNTPServer3Key_Object = MibScalar
mbgLtCfgNTPServer3Key = _MbgLtCfgNTPServer3Key_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 3, 2),
    _MbgLtCfgNTPServer3Key_Type()
)
mbgLtCfgNTPServer3Key.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNTPServer3Key.setStatus("current")


class _MbgLtCfgNTPServer3Autokey_Type(Integer32):
    """Custom type mbgLtCfgNTPServer3Autokey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgNTPServer3Autokey_Type.__name__ = "Integer32"
_MbgLtCfgNTPServer3Autokey_Object = MibScalar
mbgLtCfgNTPServer3Autokey = _MbgLtCfgNTPServer3Autokey_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 3, 3),
    _MbgLtCfgNTPServer3Autokey_Type()
)
mbgLtCfgNTPServer3Autokey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNTPServer3Autokey.setStatus("current")


class _MbgLtCfgNTPServer3Prefer_Type(Integer32):
    """Custom type mbgLtCfgNTPServer3Prefer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgNTPServer3Prefer_Type.__name__ = "Integer32"
_MbgLtCfgNTPServer3Prefer_Object = MibScalar
mbgLtCfgNTPServer3Prefer = _MbgLtCfgNTPServer3Prefer_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 3, 4),
    _MbgLtCfgNTPServer3Prefer_Type()
)
mbgLtCfgNTPServer3Prefer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNTPServer3Prefer.setStatus("current")
_MbgLtCfgNTPServer4_ObjectIdentity = ObjectIdentity
mbgLtCfgNTPServer4 = _MbgLtCfgNTPServer4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 4)
)
_MbgLtCfgNTPServer4IP_Type = DisplayString
_MbgLtCfgNTPServer4IP_Object = MibScalar
mbgLtCfgNTPServer4IP = _MbgLtCfgNTPServer4IP_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 4, 1),
    _MbgLtCfgNTPServer4IP_Type()
)
mbgLtCfgNTPServer4IP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNTPServer4IP.setStatus("current")


class _MbgLtCfgNTPServer4Key_Type(Integer32):
    """Custom type mbgLtCfgNTPServer4Key based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_MbgLtCfgNTPServer4Key_Type.__name__ = "Integer32"
_MbgLtCfgNTPServer4Key_Object = MibScalar
mbgLtCfgNTPServer4Key = _MbgLtCfgNTPServer4Key_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 4, 2),
    _MbgLtCfgNTPServer4Key_Type()
)
mbgLtCfgNTPServer4Key.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNTPServer4Key.setStatus("current")


class _MbgLtCfgNTPServer4Autokey_Type(Integer32):
    """Custom type mbgLtCfgNTPServer4Autokey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgNTPServer4Autokey_Type.__name__ = "Integer32"
_MbgLtCfgNTPServer4Autokey_Object = MibScalar
mbgLtCfgNTPServer4Autokey = _MbgLtCfgNTPServer4Autokey_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 4, 3),
    _MbgLtCfgNTPServer4Autokey_Type()
)
mbgLtCfgNTPServer4Autokey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNTPServer4Autokey.setStatus("current")


class _MbgLtCfgNTPServer4Prefer_Type(Integer32):
    """Custom type mbgLtCfgNTPServer4Prefer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgNTPServer4Prefer_Type.__name__ = "Integer32"
_MbgLtCfgNTPServer4Prefer_Object = MibScalar
mbgLtCfgNTPServer4Prefer = _MbgLtCfgNTPServer4Prefer_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 4, 4),
    _MbgLtCfgNTPServer4Prefer_Type()
)
mbgLtCfgNTPServer4Prefer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNTPServer4Prefer.setStatus("current")
_MbgLtCfgNTPServer5_ObjectIdentity = ObjectIdentity
mbgLtCfgNTPServer5 = _MbgLtCfgNTPServer5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 5)
)
_MbgLtCfgNTPServer5IP_Type = DisplayString
_MbgLtCfgNTPServer5IP_Object = MibScalar
mbgLtCfgNTPServer5IP = _MbgLtCfgNTPServer5IP_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 5, 1),
    _MbgLtCfgNTPServer5IP_Type()
)
mbgLtCfgNTPServer5IP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNTPServer5IP.setStatus("current")


class _MbgLtCfgNTPServer5Key_Type(Integer32):
    """Custom type mbgLtCfgNTPServer5Key based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_MbgLtCfgNTPServer5Key_Type.__name__ = "Integer32"
_MbgLtCfgNTPServer5Key_Object = MibScalar
mbgLtCfgNTPServer5Key = _MbgLtCfgNTPServer5Key_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 5, 2),
    _MbgLtCfgNTPServer5Key_Type()
)
mbgLtCfgNTPServer5Key.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNTPServer5Key.setStatus("current")


class _MbgLtCfgNTPServer5Autokey_Type(Integer32):
    """Custom type mbgLtCfgNTPServer5Autokey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgNTPServer5Autokey_Type.__name__ = "Integer32"
_MbgLtCfgNTPServer5Autokey_Object = MibScalar
mbgLtCfgNTPServer5Autokey = _MbgLtCfgNTPServer5Autokey_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 5, 3),
    _MbgLtCfgNTPServer5Autokey_Type()
)
mbgLtCfgNTPServer5Autokey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNTPServer5Autokey.setStatus("current")


class _MbgLtCfgNTPServer5Prefer_Type(Integer32):
    """Custom type mbgLtCfgNTPServer5Prefer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgNTPServer5Prefer_Type.__name__ = "Integer32"
_MbgLtCfgNTPServer5Prefer_Object = MibScalar
mbgLtCfgNTPServer5Prefer = _MbgLtCfgNTPServer5Prefer_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 5, 4),
    _MbgLtCfgNTPServer5Prefer_Type()
)
mbgLtCfgNTPServer5Prefer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNTPServer5Prefer.setStatus("current")
_MbgLtCfgNTPServer6_ObjectIdentity = ObjectIdentity
mbgLtCfgNTPServer6 = _MbgLtCfgNTPServer6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 6)
)
_MbgLtCfgNTPServer6IP_Type = DisplayString
_MbgLtCfgNTPServer6IP_Object = MibScalar
mbgLtCfgNTPServer6IP = _MbgLtCfgNTPServer6IP_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 6, 1),
    _MbgLtCfgNTPServer6IP_Type()
)
mbgLtCfgNTPServer6IP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNTPServer6IP.setStatus("current")


class _MbgLtCfgNTPServer6Key_Type(Integer32):
    """Custom type mbgLtCfgNTPServer6Key based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_MbgLtCfgNTPServer6Key_Type.__name__ = "Integer32"
_MbgLtCfgNTPServer6Key_Object = MibScalar
mbgLtCfgNTPServer6Key = _MbgLtCfgNTPServer6Key_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 6, 2),
    _MbgLtCfgNTPServer6Key_Type()
)
mbgLtCfgNTPServer6Key.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNTPServer6Key.setStatus("current")


class _MbgLtCfgNTPServer6Autokey_Type(Integer32):
    """Custom type mbgLtCfgNTPServer6Autokey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgNTPServer6Autokey_Type.__name__ = "Integer32"
_MbgLtCfgNTPServer6Autokey_Object = MibScalar
mbgLtCfgNTPServer6Autokey = _MbgLtCfgNTPServer6Autokey_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 6, 3),
    _MbgLtCfgNTPServer6Autokey_Type()
)
mbgLtCfgNTPServer6Autokey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNTPServer6Autokey.setStatus("current")


class _MbgLtCfgNTPServer6Prefer_Type(Integer32):
    """Custom type mbgLtCfgNTPServer6Prefer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgNTPServer6Prefer_Type.__name__ = "Integer32"
_MbgLtCfgNTPServer6Prefer_Object = MibScalar
mbgLtCfgNTPServer6Prefer = _MbgLtCfgNTPServer6Prefer_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 6, 4),
    _MbgLtCfgNTPServer6Prefer_Type()
)
mbgLtCfgNTPServer6Prefer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNTPServer6Prefer.setStatus("current")
_MbgLtCfgNTPServer7_ObjectIdentity = ObjectIdentity
mbgLtCfgNTPServer7 = _MbgLtCfgNTPServer7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 7)
)
_MbgLtCfgNTPServer7IP_Type = DisplayString
_MbgLtCfgNTPServer7IP_Object = MibScalar
mbgLtCfgNTPServer7IP = _MbgLtCfgNTPServer7IP_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 7, 1),
    _MbgLtCfgNTPServer7IP_Type()
)
mbgLtCfgNTPServer7IP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNTPServer7IP.setStatus("current")


class _MbgLtCfgNTPServer7Key_Type(Integer32):
    """Custom type mbgLtCfgNTPServer7Key based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_MbgLtCfgNTPServer7Key_Type.__name__ = "Integer32"
_MbgLtCfgNTPServer7Key_Object = MibScalar
mbgLtCfgNTPServer7Key = _MbgLtCfgNTPServer7Key_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 7, 2),
    _MbgLtCfgNTPServer7Key_Type()
)
mbgLtCfgNTPServer7Key.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNTPServer7Key.setStatus("current")


class _MbgLtCfgNTPServer7Autokey_Type(Integer32):
    """Custom type mbgLtCfgNTPServer7Autokey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgNTPServer7Autokey_Type.__name__ = "Integer32"
_MbgLtCfgNTPServer7Autokey_Object = MibScalar
mbgLtCfgNTPServer7Autokey = _MbgLtCfgNTPServer7Autokey_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 7, 3),
    _MbgLtCfgNTPServer7Autokey_Type()
)
mbgLtCfgNTPServer7Autokey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNTPServer7Autokey.setStatus("current")


class _MbgLtCfgNTPServer7Prefer_Type(Integer32):
    """Custom type mbgLtCfgNTPServer7Prefer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgNTPServer7Prefer_Type.__name__ = "Integer32"
_MbgLtCfgNTPServer7Prefer_Object = MibScalar
mbgLtCfgNTPServer7Prefer = _MbgLtCfgNTPServer7Prefer_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 7, 4),
    _MbgLtCfgNTPServer7Prefer_Type()
)
mbgLtCfgNTPServer7Prefer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNTPServer7Prefer.setStatus("current")


class _MbgLtCfgNTPStratumLocalClock_Type(Integer32):
    """Custom type mbgLtCfgNTPStratumLocalClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MbgLtCfgNTPStratumLocalClock_Type.__name__ = "Integer32"
_MbgLtCfgNTPStratumLocalClock_Object = MibScalar
mbgLtCfgNTPStratumLocalClock = _MbgLtCfgNTPStratumLocalClock_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 8),
    _MbgLtCfgNTPStratumLocalClock_Type()
)
mbgLtCfgNTPStratumLocalClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNTPStratumLocalClock.setStatus("current")


class _MbgLtCfgNTPTrustedKey_Type(Integer32):
    """Custom type mbgLtCfgNTPTrustedKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_MbgLtCfgNTPTrustedKey_Type.__name__ = "Integer32"
_MbgLtCfgNTPTrustedKey_Object = MibScalar
mbgLtCfgNTPTrustedKey = _MbgLtCfgNTPTrustedKey_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 9),
    _MbgLtCfgNTPTrustedKey_Type()
)
mbgLtCfgNTPTrustedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNTPTrustedKey.setStatus("current")
_MbgLtCfgNTPBroadcastIP_Type = DisplayString
_MbgLtCfgNTPBroadcastIP_Object = MibScalar
mbgLtCfgNTPBroadcastIP = _MbgLtCfgNTPBroadcastIP_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 10),
    _MbgLtCfgNTPBroadcastIP_Type()
)
mbgLtCfgNTPBroadcastIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNTPBroadcastIP.setStatus("current")


class _MbgLtCfgNTPBroadcastKey_Type(Integer32):
    """Custom type mbgLtCfgNTPBroadcastKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_MbgLtCfgNTPBroadcastKey_Type.__name__ = "Integer32"
_MbgLtCfgNTPBroadcastKey_Object = MibScalar
mbgLtCfgNTPBroadcastKey = _MbgLtCfgNTPBroadcastKey_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 11),
    _MbgLtCfgNTPBroadcastKey_Type()
)
mbgLtCfgNTPBroadcastKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNTPBroadcastKey.setStatus("current")


class _MbgLtCfgNTPBroadcastAutokey_Type(Integer32):
    """Custom type mbgLtCfgNTPBroadcastAutokey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgNTPBroadcastAutokey_Type.__name__ = "Integer32"
_MbgLtCfgNTPBroadcastAutokey_Object = MibScalar
mbgLtCfgNTPBroadcastAutokey = _MbgLtCfgNTPBroadcastAutokey_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 12),
    _MbgLtCfgNTPBroadcastAutokey_Type()
)
mbgLtCfgNTPBroadcastAutokey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNTPBroadcastAutokey.setStatus("current")


class _MbgLtCfgNTPAutokeyFeature_Type(Integer32):
    """Custom type mbgLtCfgNTPAutokeyFeature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgNTPAutokeyFeature_Type.__name__ = "Integer32"
_MbgLtCfgNTPAutokeyFeature_Object = MibScalar
mbgLtCfgNTPAutokeyFeature = _MbgLtCfgNTPAutokeyFeature_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 13),
    _MbgLtCfgNTPAutokeyFeature_Type()
)
mbgLtCfgNTPAutokeyFeature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNTPAutokeyFeature.setStatus("current")


class _MbgLtCfgNTPAtomPPS_Type(Integer32):
    """Custom type mbgLtCfgNTPAtomPPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgNTPAtomPPS_Type.__name__ = "Integer32"
_MbgLtCfgNTPAtomPPS_Object = MibScalar
mbgLtCfgNTPAtomPPS = _MbgLtCfgNTPAtomPPS_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 2, 14),
    _MbgLtCfgNTPAtomPPS_Type()
)
mbgLtCfgNTPAtomPPS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNTPAtomPPS.setStatus("current")
_MbgLtCfgEMail_ObjectIdentity = ObjectIdentity
mbgLtCfgEMail = _MbgLtCfgEMail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 3)
)
_MbgLtCfgEMailTo_Type = DisplayString
_MbgLtCfgEMailTo_Object = MibScalar
mbgLtCfgEMailTo = _MbgLtCfgEMailTo_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 3, 1),
    _MbgLtCfgEMailTo_Type()
)
mbgLtCfgEMailTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEMailTo.setStatus("current")
_MbgLtCfgEMailFrom_Type = DisplayString
_MbgLtCfgEMailFrom_Object = MibScalar
mbgLtCfgEMailFrom = _MbgLtCfgEMailFrom_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 3, 2),
    _MbgLtCfgEMailFrom_Type()
)
mbgLtCfgEMailFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEMailFrom.setStatus("current")
_MbgLtCfgEMailSmarthost_Type = DisplayString
_MbgLtCfgEMailSmarthost_Object = MibScalar
mbgLtCfgEMailSmarthost = _MbgLtCfgEMailSmarthost_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 3, 3),
    _MbgLtCfgEMailSmarthost_Type()
)
mbgLtCfgEMailSmarthost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEMailSmarthost.setStatus("current")
_MbgLtCfgSNMP_ObjectIdentity = ObjectIdentity
mbgLtCfgSNMP = _MbgLtCfgSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 4)
)
_MbgLtCfgSNMPTrapReceiver1_Type = DisplayString
_MbgLtCfgSNMPTrapReceiver1_Object = MibScalar
mbgLtCfgSNMPTrapReceiver1 = _MbgLtCfgSNMPTrapReceiver1_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 4, 1),
    _MbgLtCfgSNMPTrapReceiver1_Type()
)
mbgLtCfgSNMPTrapReceiver1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgSNMPTrapReceiver1.setStatus("current")
_MbgLtCfgSNMPTrapReceiver2_Type = DisplayString
_MbgLtCfgSNMPTrapReceiver2_Object = MibScalar
mbgLtCfgSNMPTrapReceiver2 = _MbgLtCfgSNMPTrapReceiver2_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 4, 2),
    _MbgLtCfgSNMPTrapReceiver2_Type()
)
mbgLtCfgSNMPTrapReceiver2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgSNMPTrapReceiver2.setStatus("current")
_MbgLtCfgSNMPTrapRec1Community_Type = DisplayString
_MbgLtCfgSNMPTrapRec1Community_Object = MibScalar
mbgLtCfgSNMPTrapRec1Community = _MbgLtCfgSNMPTrapRec1Community_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 4, 3),
    _MbgLtCfgSNMPTrapRec1Community_Type()
)
mbgLtCfgSNMPTrapRec1Community.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgSNMPTrapRec1Community.setStatus("current")
_MbgLtCfgSNMPTrapRec2Community_Type = DisplayString
_MbgLtCfgSNMPTrapRec2Community_Object = MibScalar
mbgLtCfgSNMPTrapRec2Community = _MbgLtCfgSNMPTrapRec2Community_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 4, 4),
    _MbgLtCfgSNMPTrapRec2Community_Type()
)
mbgLtCfgSNMPTrapRec2Community.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgSNMPTrapRec2Community.setStatus("current")
_MbgLtCfgSNMPReadOnlyCommunity_Type = DisplayString
_MbgLtCfgSNMPReadOnlyCommunity_Object = MibScalar
mbgLtCfgSNMPReadOnlyCommunity = _MbgLtCfgSNMPReadOnlyCommunity_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 4, 5),
    _MbgLtCfgSNMPReadOnlyCommunity_Type()
)
mbgLtCfgSNMPReadOnlyCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgSNMPReadOnlyCommunity.setStatus("current")
_MbgLtCfgSNMPReadWriteCommunity_Type = DisplayString
_MbgLtCfgSNMPReadWriteCommunity_Object = MibScalar
mbgLtCfgSNMPReadWriteCommunity = _MbgLtCfgSNMPReadWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 4, 6),
    _MbgLtCfgSNMPReadWriteCommunity_Type()
)
mbgLtCfgSNMPReadWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgSNMPReadWriteCommunity.setStatus("current")
_MbgLtCfgSNMPContact_Type = DisplayString
_MbgLtCfgSNMPContact_Object = MibScalar
mbgLtCfgSNMPContact = _MbgLtCfgSNMPContact_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 4, 7),
    _MbgLtCfgSNMPContact_Type()
)
mbgLtCfgSNMPContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgSNMPContact.setStatus("current")
_MbgLtCfgSNMPLocation_Type = DisplayString
_MbgLtCfgSNMPLocation_Object = MibScalar
mbgLtCfgSNMPLocation = _MbgLtCfgSNMPLocation_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 4, 8),
    _MbgLtCfgSNMPLocation_Type()
)
mbgLtCfgSNMPLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgSNMPLocation.setStatus("current")
_MbgLtCfgWinpopup_ObjectIdentity = ObjectIdentity
mbgLtCfgWinpopup = _MbgLtCfgWinpopup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 5)
)
_MbgLtCfgWMailAddress1_Type = DisplayString
_MbgLtCfgWMailAddress1_Object = MibScalar
mbgLtCfgWMailAddress1 = _MbgLtCfgWMailAddress1_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 5, 1),
    _MbgLtCfgWMailAddress1_Type()
)
mbgLtCfgWMailAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgWMailAddress1.setStatus("current")
_MbgLtCfgWMailAddress2_Type = DisplayString
_MbgLtCfgWMailAddress2_Object = MibScalar
mbgLtCfgWMailAddress2 = _MbgLtCfgWMailAddress2_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 5, 2),
    _MbgLtCfgWMailAddress2_Type()
)
mbgLtCfgWMailAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgWMailAddress2.setStatus("current")
_MbgLtCfgWalldisplay_ObjectIdentity = ObjectIdentity
mbgLtCfgWalldisplay = _MbgLtCfgWalldisplay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 6)
)
_MbgLtCfgVP100Display1IP_Type = DisplayString
_MbgLtCfgVP100Display1IP_Object = MibScalar
mbgLtCfgVP100Display1IP = _MbgLtCfgVP100Display1IP_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 6, 1),
    _MbgLtCfgVP100Display1IP_Type()
)
mbgLtCfgVP100Display1IP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgVP100Display1IP.setStatus("current")
_MbgLtCfgVP100Display1SN_Type = DisplayString
_MbgLtCfgVP100Display1SN_Object = MibScalar
mbgLtCfgVP100Display1SN = _MbgLtCfgVP100Display1SN_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 6, 2),
    _MbgLtCfgVP100Display1SN_Type()
)
mbgLtCfgVP100Display1SN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgVP100Display1SN.setStatus("current")
_MbgLtCfgVP100Display2IP_Type = DisplayString
_MbgLtCfgVP100Display2IP_Object = MibScalar
mbgLtCfgVP100Display2IP = _MbgLtCfgVP100Display2IP_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 6, 3),
    _MbgLtCfgVP100Display2IP_Type()
)
mbgLtCfgVP100Display2IP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgVP100Display2IP.setStatus("current")
_MbgLtCfgVP100Display2SN_Type = DisplayString
_MbgLtCfgVP100Display2SN_Object = MibScalar
mbgLtCfgVP100Display2SN = _MbgLtCfgVP100Display2SN_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 6, 4),
    _MbgLtCfgVP100Display2SN_Type()
)
mbgLtCfgVP100Display2SN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgVP100Display2SN.setStatus("current")
_MbgLtCfgNotify_ObjectIdentity = ObjectIdentity
mbgLtCfgNotify = _MbgLtCfgNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 7)
)
_MbgLtCfgNotifyNTPNotSync_Type = DisplayString
_MbgLtCfgNotifyNTPNotSync_Object = MibScalar
mbgLtCfgNotifyNTPNotSync = _MbgLtCfgNotifyNTPNotSync_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 7, 1),
    _MbgLtCfgNotifyNTPNotSync_Type()
)
mbgLtCfgNotifyNTPNotSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNotifyNTPNotSync.setStatus("current")
_MbgLtCfgNotifyNTPStopped_Type = DisplayString
_MbgLtCfgNotifyNTPStopped_Object = MibScalar
mbgLtCfgNotifyNTPStopped = _MbgLtCfgNotifyNTPStopped_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 7, 2),
    _MbgLtCfgNotifyNTPStopped_Type()
)
mbgLtCfgNotifyNTPStopped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNotifyNTPStopped.setStatus("current")
_MbgLtCfgNotifyServerBoot_Type = DisplayString
_MbgLtCfgNotifyServerBoot_Object = MibScalar
mbgLtCfgNotifyServerBoot = _MbgLtCfgNotifyServerBoot_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 7, 3),
    _MbgLtCfgNotifyServerBoot_Type()
)
mbgLtCfgNotifyServerBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNotifyServerBoot.setStatus("current")
_MbgLtCfgNotifyRefclkNoResponse_Type = DisplayString
_MbgLtCfgNotifyRefclkNoResponse_Object = MibScalar
mbgLtCfgNotifyRefclkNoResponse = _MbgLtCfgNotifyRefclkNoResponse_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 7, 4),
    _MbgLtCfgNotifyRefclkNoResponse_Type()
)
mbgLtCfgNotifyRefclkNoResponse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNotifyRefclkNoResponse.setStatus("current")
_MbgLtCfgNotifyRefclockNotSync_Type = DisplayString
_MbgLtCfgNotifyRefclockNotSync_Object = MibScalar
mbgLtCfgNotifyRefclockNotSync = _MbgLtCfgNotifyRefclockNotSync_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 7, 5),
    _MbgLtCfgNotifyRefclockNotSync_Type()
)
mbgLtCfgNotifyRefclockNotSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNotifyRefclockNotSync.setStatus("current")
_MbgLtCfgNotifyAntennaFaulty_Type = DisplayString
_MbgLtCfgNotifyAntennaFaulty_Object = MibScalar
mbgLtCfgNotifyAntennaFaulty = _MbgLtCfgNotifyAntennaFaulty_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 7, 6),
    _MbgLtCfgNotifyAntennaFaulty_Type()
)
mbgLtCfgNotifyAntennaFaulty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNotifyAntennaFaulty.setStatus("current")
_MbgLtCfgNotifyAntennaReconnect_Type = DisplayString
_MbgLtCfgNotifyAntennaReconnect_Object = MibScalar
mbgLtCfgNotifyAntennaReconnect = _MbgLtCfgNotifyAntennaReconnect_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 7, 7),
    _MbgLtCfgNotifyAntennaReconnect_Type()
)
mbgLtCfgNotifyAntennaReconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNotifyAntennaReconnect.setStatus("current")
_MbgLtCfgNotifyConfigChanged_Type = DisplayString
_MbgLtCfgNotifyConfigChanged_Object = MibScalar
mbgLtCfgNotifyConfigChanged = _MbgLtCfgNotifyConfigChanged_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 7, 8),
    _MbgLtCfgNotifyConfigChanged_Type()
)
mbgLtCfgNotifyConfigChanged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNotifyConfigChanged.setStatus("current")
_MbgLtCfgNotifySHSTimeLimitError_Type = DisplayString
_MbgLtCfgNotifySHSTimeLimitError_Object = MibScalar
mbgLtCfgNotifySHSTimeLimitError = _MbgLtCfgNotifySHSTimeLimitError_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 7, 9),
    _MbgLtCfgNotifySHSTimeLimitError_Type()
)
mbgLtCfgNotifySHSTimeLimitError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNotifySHSTimeLimitError.setStatus("current")
_MbgLtCfgNotifyLeapSecond_Type = DisplayString
_MbgLtCfgNotifyLeapSecond_Object = MibScalar
mbgLtCfgNotifyLeapSecond = _MbgLtCfgNotifyLeapSecond_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 7, 10),
    _MbgLtCfgNotifyLeapSecond_Type()
)
mbgLtCfgNotifyLeapSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgNotifyLeapSecond.setStatus("current")
_MbgLtCfgEthernet_ObjectIdentity = ObjectIdentity
mbgLtCfgEthernet = _MbgLtCfgEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8)
)
_MbgLtCfgEthernetIf0_ObjectIdentity = ObjectIdentity
mbgLtCfgEthernetIf0 = _MbgLtCfgEthernetIf0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 0)
)
_MbgLtCfgEthernetIf0IPv4IP_Type = DisplayString
_MbgLtCfgEthernetIf0IPv4IP_Object = MibScalar
mbgLtCfgEthernetIf0IPv4IP = _MbgLtCfgEthernetIf0IPv4IP_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 0, 1),
    _MbgLtCfgEthernetIf0IPv4IP_Type()
)
mbgLtCfgEthernetIf0IPv4IP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf0IPv4IP.setStatus("current")
_MbgLtCfgEthernetIf0IPv4Netmask_Type = DisplayString
_MbgLtCfgEthernetIf0IPv4Netmask_Object = MibScalar
mbgLtCfgEthernetIf0IPv4Netmask = _MbgLtCfgEthernetIf0IPv4Netmask_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 0, 2),
    _MbgLtCfgEthernetIf0IPv4Netmask_Type()
)
mbgLtCfgEthernetIf0IPv4Netmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf0IPv4Netmask.setStatus("current")
_MbgLtCfgEthernetIf0IPv4Gateway_Type = DisplayString
_MbgLtCfgEthernetIf0IPv4Gateway_Object = MibScalar
mbgLtCfgEthernetIf0IPv4Gateway = _MbgLtCfgEthernetIf0IPv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 0, 3),
    _MbgLtCfgEthernetIf0IPv4Gateway_Type()
)
mbgLtCfgEthernetIf0IPv4Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf0IPv4Gateway.setStatus("current")


class _MbgLtCfgEthernetIf0DHCPClient_Type(Integer32):
    """Custom type mbgLtCfgEthernetIf0DHCPClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgEthernetIf0DHCPClient_Type.__name__ = "Integer32"
_MbgLtCfgEthernetIf0DHCPClient_Object = MibScalar
mbgLtCfgEthernetIf0DHCPClient = _MbgLtCfgEthernetIf0DHCPClient_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 0, 4),
    _MbgLtCfgEthernetIf0DHCPClient_Type()
)
mbgLtCfgEthernetIf0DHCPClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf0DHCPClient.setStatus("current")
_MbgLtCfgEthernetIf0IPv6IP1_Type = DisplayString
_MbgLtCfgEthernetIf0IPv6IP1_Object = MibScalar
mbgLtCfgEthernetIf0IPv6IP1 = _MbgLtCfgEthernetIf0IPv6IP1_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 0, 5),
    _MbgLtCfgEthernetIf0IPv6IP1_Type()
)
mbgLtCfgEthernetIf0IPv6IP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf0IPv6IP1.setStatus("current")
_MbgLtCfgEthernetIf0IPv6IP2_Type = DisplayString
_MbgLtCfgEthernetIf0IPv6IP2_Object = MibScalar
mbgLtCfgEthernetIf0IPv6IP2 = _MbgLtCfgEthernetIf0IPv6IP2_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 0, 6),
    _MbgLtCfgEthernetIf0IPv6IP2_Type()
)
mbgLtCfgEthernetIf0IPv6IP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf0IPv6IP2.setStatus("current")
_MbgLtCfgEthernetIf0IPv6IP3_Type = DisplayString
_MbgLtCfgEthernetIf0IPv6IP3_Object = MibScalar
mbgLtCfgEthernetIf0IPv6IP3 = _MbgLtCfgEthernetIf0IPv6IP3_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 0, 7),
    _MbgLtCfgEthernetIf0IPv6IP3_Type()
)
mbgLtCfgEthernetIf0IPv6IP3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf0IPv6IP3.setStatus("current")


class _MbgLtCfgEthernetIf0IPv6Autoconf_Type(Integer32):
    """Custom type mbgLtCfgEthernetIf0IPv6Autoconf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgEthernetIf0IPv6Autoconf_Type.__name__ = "Integer32"
_MbgLtCfgEthernetIf0IPv6Autoconf_Object = MibScalar
mbgLtCfgEthernetIf0IPv6Autoconf = _MbgLtCfgEthernetIf0IPv6Autoconf_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 0, 8),
    _MbgLtCfgEthernetIf0IPv6Autoconf_Type()
)
mbgLtCfgEthernetIf0IPv6Autoconf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf0IPv6Autoconf.setStatus("current")


class _MbgLtCfgEthernetIf0NetLinkMode_Type(Integer32):
    """Custom type mbgLtCfgEthernetIf0NetLinkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("autosensing", 0),
          ("link100full", 4),
          ("link100half", 3),
          ("link10full", 2),
          ("link10half", 1))
    )


_MbgLtCfgEthernetIf0NetLinkMode_Type.__name__ = "Integer32"
_MbgLtCfgEthernetIf0NetLinkMode_Object = MibScalar
mbgLtCfgEthernetIf0NetLinkMode = _MbgLtCfgEthernetIf0NetLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 0, 9),
    _MbgLtCfgEthernetIf0NetLinkMode_Type()
)
mbgLtCfgEthernetIf0NetLinkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf0NetLinkMode.setStatus("current")
_MbgLtCfgEthernetIf1_ObjectIdentity = ObjectIdentity
mbgLtCfgEthernetIf1 = _MbgLtCfgEthernetIf1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 1)
)
_MbgLtCfgEthernetIf1IPv4IP_Type = DisplayString
_MbgLtCfgEthernetIf1IPv4IP_Object = MibScalar
mbgLtCfgEthernetIf1IPv4IP = _MbgLtCfgEthernetIf1IPv4IP_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 1, 1),
    _MbgLtCfgEthernetIf1IPv4IP_Type()
)
mbgLtCfgEthernetIf1IPv4IP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf1IPv4IP.setStatus("current")
_MbgLtCfgEthernetIf1IPv4Netmask_Type = DisplayString
_MbgLtCfgEthernetIf1IPv4Netmask_Object = MibScalar
mbgLtCfgEthernetIf1IPv4Netmask = _MbgLtCfgEthernetIf1IPv4Netmask_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 1, 2),
    _MbgLtCfgEthernetIf1IPv4Netmask_Type()
)
mbgLtCfgEthernetIf1IPv4Netmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf1IPv4Netmask.setStatus("current")
_MbgLtCfgEthernetIf1IPv4Gateway_Type = DisplayString
_MbgLtCfgEthernetIf1IPv4Gateway_Object = MibScalar
mbgLtCfgEthernetIf1IPv4Gateway = _MbgLtCfgEthernetIf1IPv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 1, 3),
    _MbgLtCfgEthernetIf1IPv4Gateway_Type()
)
mbgLtCfgEthernetIf1IPv4Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf1IPv4Gateway.setStatus("current")


class _MbgLtCfgEthernetIf1DHCPClient_Type(Integer32):
    """Custom type mbgLtCfgEthernetIf1DHCPClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgEthernetIf1DHCPClient_Type.__name__ = "Integer32"
_MbgLtCfgEthernetIf1DHCPClient_Object = MibScalar
mbgLtCfgEthernetIf1DHCPClient = _MbgLtCfgEthernetIf1DHCPClient_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 1, 4),
    _MbgLtCfgEthernetIf1DHCPClient_Type()
)
mbgLtCfgEthernetIf1DHCPClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf1DHCPClient.setStatus("current")
_MbgLtCfgEthernetIf1IPv6IP1_Type = DisplayString
_MbgLtCfgEthernetIf1IPv6IP1_Object = MibScalar
mbgLtCfgEthernetIf1IPv6IP1 = _MbgLtCfgEthernetIf1IPv6IP1_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 1, 5),
    _MbgLtCfgEthernetIf1IPv6IP1_Type()
)
mbgLtCfgEthernetIf1IPv6IP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf1IPv6IP1.setStatus("current")
_MbgLtCfgEthernetIf1IPv6IP2_Type = DisplayString
_MbgLtCfgEthernetIf1IPv6IP2_Object = MibScalar
mbgLtCfgEthernetIf1IPv6IP2 = _MbgLtCfgEthernetIf1IPv6IP2_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 1, 6),
    _MbgLtCfgEthernetIf1IPv6IP2_Type()
)
mbgLtCfgEthernetIf1IPv6IP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf1IPv6IP2.setStatus("current")
_MbgLtCfgEthernetIf1IPv6IP3_Type = DisplayString
_MbgLtCfgEthernetIf1IPv6IP3_Object = MibScalar
mbgLtCfgEthernetIf1IPv6IP3 = _MbgLtCfgEthernetIf1IPv6IP3_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 1, 7),
    _MbgLtCfgEthernetIf1IPv6IP3_Type()
)
mbgLtCfgEthernetIf1IPv6IP3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf1IPv6IP3.setStatus("current")


class _MbgLtCfgEthernetIf1IPv6Autoconf_Type(Integer32):
    """Custom type mbgLtCfgEthernetIf1IPv6Autoconf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgEthernetIf1IPv6Autoconf_Type.__name__ = "Integer32"
_MbgLtCfgEthernetIf1IPv6Autoconf_Object = MibScalar
mbgLtCfgEthernetIf1IPv6Autoconf = _MbgLtCfgEthernetIf1IPv6Autoconf_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 1, 8),
    _MbgLtCfgEthernetIf1IPv6Autoconf_Type()
)
mbgLtCfgEthernetIf1IPv6Autoconf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf1IPv6Autoconf.setStatus("current")


class _MbgLtCfgEthernetIf1NetLinkMode_Type(Integer32):
    """Custom type mbgLtCfgEthernetIf1NetLinkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("autosensing", 0),
          ("link100full", 4),
          ("link100half", 3),
          ("link10full", 2),
          ("link10half", 1))
    )


_MbgLtCfgEthernetIf1NetLinkMode_Type.__name__ = "Integer32"
_MbgLtCfgEthernetIf1NetLinkMode_Object = MibScalar
mbgLtCfgEthernetIf1NetLinkMode = _MbgLtCfgEthernetIf1NetLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 1, 9),
    _MbgLtCfgEthernetIf1NetLinkMode_Type()
)
mbgLtCfgEthernetIf1NetLinkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf1NetLinkMode.setStatus("current")
_MbgLtCfgEthernetIf2_ObjectIdentity = ObjectIdentity
mbgLtCfgEthernetIf2 = _MbgLtCfgEthernetIf2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 2)
)
_MbgLtCfgEthernetIf2IPv4IP_Type = DisplayString
_MbgLtCfgEthernetIf2IPv4IP_Object = MibScalar
mbgLtCfgEthernetIf2IPv4IP = _MbgLtCfgEthernetIf2IPv4IP_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 2, 1),
    _MbgLtCfgEthernetIf2IPv4IP_Type()
)
mbgLtCfgEthernetIf2IPv4IP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf2IPv4IP.setStatus("current")
_MbgLtCfgEthernetIf2IPv4Netmask_Type = DisplayString
_MbgLtCfgEthernetIf2IPv4Netmask_Object = MibScalar
mbgLtCfgEthernetIf2IPv4Netmask = _MbgLtCfgEthernetIf2IPv4Netmask_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 2, 2),
    _MbgLtCfgEthernetIf2IPv4Netmask_Type()
)
mbgLtCfgEthernetIf2IPv4Netmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf2IPv4Netmask.setStatus("current")
_MbgLtCfgEthernetIf2IPv4Gateway_Type = DisplayString
_MbgLtCfgEthernetIf2IPv4Gateway_Object = MibScalar
mbgLtCfgEthernetIf2IPv4Gateway = _MbgLtCfgEthernetIf2IPv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 2, 3),
    _MbgLtCfgEthernetIf2IPv4Gateway_Type()
)
mbgLtCfgEthernetIf2IPv4Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf2IPv4Gateway.setStatus("current")


class _MbgLtCfgEthernetIf2DHCPClient_Type(Integer32):
    """Custom type mbgLtCfgEthernetIf2DHCPClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgEthernetIf2DHCPClient_Type.__name__ = "Integer32"
_MbgLtCfgEthernetIf2DHCPClient_Object = MibScalar
mbgLtCfgEthernetIf2DHCPClient = _MbgLtCfgEthernetIf2DHCPClient_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 2, 4),
    _MbgLtCfgEthernetIf2DHCPClient_Type()
)
mbgLtCfgEthernetIf2DHCPClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf2DHCPClient.setStatus("current")
_MbgLtCfgEthernetIf2IPv6IP1_Type = DisplayString
_MbgLtCfgEthernetIf2IPv6IP1_Object = MibScalar
mbgLtCfgEthernetIf2IPv6IP1 = _MbgLtCfgEthernetIf2IPv6IP1_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 2, 5),
    _MbgLtCfgEthernetIf2IPv6IP1_Type()
)
mbgLtCfgEthernetIf2IPv6IP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf2IPv6IP1.setStatus("current")
_MbgLtCfgEthernetIf2IPv6IP2_Type = DisplayString
_MbgLtCfgEthernetIf2IPv6IP2_Object = MibScalar
mbgLtCfgEthernetIf2IPv6IP2 = _MbgLtCfgEthernetIf2IPv6IP2_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 2, 6),
    _MbgLtCfgEthernetIf2IPv6IP2_Type()
)
mbgLtCfgEthernetIf2IPv6IP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf2IPv6IP2.setStatus("current")
_MbgLtCfgEthernetIf2IPv6IP3_Type = DisplayString
_MbgLtCfgEthernetIf2IPv6IP3_Object = MibScalar
mbgLtCfgEthernetIf2IPv6IP3 = _MbgLtCfgEthernetIf2IPv6IP3_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 2, 7),
    _MbgLtCfgEthernetIf2IPv6IP3_Type()
)
mbgLtCfgEthernetIf2IPv6IP3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf2IPv6IP3.setStatus("current")


class _MbgLtCfgEthernetIf2IPv6Autoconf_Type(Integer32):
    """Custom type mbgLtCfgEthernetIf2IPv6Autoconf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgEthernetIf2IPv6Autoconf_Type.__name__ = "Integer32"
_MbgLtCfgEthernetIf2IPv6Autoconf_Object = MibScalar
mbgLtCfgEthernetIf2IPv6Autoconf = _MbgLtCfgEthernetIf2IPv6Autoconf_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 2, 8),
    _MbgLtCfgEthernetIf2IPv6Autoconf_Type()
)
mbgLtCfgEthernetIf2IPv6Autoconf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf2IPv6Autoconf.setStatus("current")


class _MbgLtCfgEthernetIf2NetLinkMode_Type(Integer32):
    """Custom type mbgLtCfgEthernetIf2NetLinkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("autosensing", 0),
          ("link100full", 4),
          ("link100half", 3),
          ("link10full", 2),
          ("link10half", 1))
    )


_MbgLtCfgEthernetIf2NetLinkMode_Type.__name__ = "Integer32"
_MbgLtCfgEthernetIf2NetLinkMode_Object = MibScalar
mbgLtCfgEthernetIf2NetLinkMode = _MbgLtCfgEthernetIf2NetLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 2, 9),
    _MbgLtCfgEthernetIf2NetLinkMode_Type()
)
mbgLtCfgEthernetIf2NetLinkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf2NetLinkMode.setStatus("current")
_MbgLtCfgEthernetIf3_ObjectIdentity = ObjectIdentity
mbgLtCfgEthernetIf3 = _MbgLtCfgEthernetIf3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 3)
)
_MbgLtCfgEthernetIf3IPv4IP_Type = DisplayString
_MbgLtCfgEthernetIf3IPv4IP_Object = MibScalar
mbgLtCfgEthernetIf3IPv4IP = _MbgLtCfgEthernetIf3IPv4IP_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 3, 1),
    _MbgLtCfgEthernetIf3IPv4IP_Type()
)
mbgLtCfgEthernetIf3IPv4IP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf3IPv4IP.setStatus("current")
_MbgLtCfgEthernetIf3IPv4Netmask_Type = DisplayString
_MbgLtCfgEthernetIf3IPv4Netmask_Object = MibScalar
mbgLtCfgEthernetIf3IPv4Netmask = _MbgLtCfgEthernetIf3IPv4Netmask_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 3, 2),
    _MbgLtCfgEthernetIf3IPv4Netmask_Type()
)
mbgLtCfgEthernetIf3IPv4Netmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf3IPv4Netmask.setStatus("current")
_MbgLtCfgEthernetIf3IPv4Gateway_Type = DisplayString
_MbgLtCfgEthernetIf3IPv4Gateway_Object = MibScalar
mbgLtCfgEthernetIf3IPv4Gateway = _MbgLtCfgEthernetIf3IPv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 3, 3),
    _MbgLtCfgEthernetIf3IPv4Gateway_Type()
)
mbgLtCfgEthernetIf3IPv4Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf3IPv4Gateway.setStatus("current")


class _MbgLtCfgEthernetIf3DHCPClient_Type(Integer32):
    """Custom type mbgLtCfgEthernetIf3DHCPClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgEthernetIf3DHCPClient_Type.__name__ = "Integer32"
_MbgLtCfgEthernetIf3DHCPClient_Object = MibScalar
mbgLtCfgEthernetIf3DHCPClient = _MbgLtCfgEthernetIf3DHCPClient_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 3, 4),
    _MbgLtCfgEthernetIf3DHCPClient_Type()
)
mbgLtCfgEthernetIf3DHCPClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf3DHCPClient.setStatus("current")
_MbgLtCfgEthernetIf3IPv6IP1_Type = DisplayString
_MbgLtCfgEthernetIf3IPv6IP1_Object = MibScalar
mbgLtCfgEthernetIf3IPv6IP1 = _MbgLtCfgEthernetIf3IPv6IP1_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 3, 5),
    _MbgLtCfgEthernetIf3IPv6IP1_Type()
)
mbgLtCfgEthernetIf3IPv6IP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf3IPv6IP1.setStatus("current")
_MbgLtCfgEthernetIf3IPv6IP2_Type = DisplayString
_MbgLtCfgEthernetIf3IPv6IP2_Object = MibScalar
mbgLtCfgEthernetIf3IPv6IP2 = _MbgLtCfgEthernetIf3IPv6IP2_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 3, 6),
    _MbgLtCfgEthernetIf3IPv6IP2_Type()
)
mbgLtCfgEthernetIf3IPv6IP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf3IPv6IP2.setStatus("current")
_MbgLtCfgEthernetIf3IPv6IP3_Type = DisplayString
_MbgLtCfgEthernetIf3IPv6IP3_Object = MibScalar
mbgLtCfgEthernetIf3IPv6IP3 = _MbgLtCfgEthernetIf3IPv6IP3_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 3, 7),
    _MbgLtCfgEthernetIf3IPv6IP3_Type()
)
mbgLtCfgEthernetIf3IPv6IP3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf3IPv6IP3.setStatus("current")


class _MbgLtCfgEthernetIf3IPv6Autoconf_Type(Integer32):
    """Custom type mbgLtCfgEthernetIf3IPv6Autoconf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgEthernetIf3IPv6Autoconf_Type.__name__ = "Integer32"
_MbgLtCfgEthernetIf3IPv6Autoconf_Object = MibScalar
mbgLtCfgEthernetIf3IPv6Autoconf = _MbgLtCfgEthernetIf3IPv6Autoconf_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 3, 8),
    _MbgLtCfgEthernetIf3IPv6Autoconf_Type()
)
mbgLtCfgEthernetIf3IPv6Autoconf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf3IPv6Autoconf.setStatus("current")


class _MbgLtCfgEthernetIf3NetLinkMode_Type(Integer32):
    """Custom type mbgLtCfgEthernetIf3NetLinkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("autosensing", 0),
          ("link100full", 4),
          ("link100half", 3),
          ("link10full", 2),
          ("link10half", 1))
    )


_MbgLtCfgEthernetIf3NetLinkMode_Type.__name__ = "Integer32"
_MbgLtCfgEthernetIf3NetLinkMode_Object = MibScalar
mbgLtCfgEthernetIf3NetLinkMode = _MbgLtCfgEthernetIf3NetLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 3, 9),
    _MbgLtCfgEthernetIf3NetLinkMode_Type()
)
mbgLtCfgEthernetIf3NetLinkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf3NetLinkMode.setStatus("current")
_MbgLtCfgEthernetIf4_ObjectIdentity = ObjectIdentity
mbgLtCfgEthernetIf4 = _MbgLtCfgEthernetIf4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 4)
)
_MbgLtCfgEthernetIf4IPv4IP_Type = DisplayString
_MbgLtCfgEthernetIf4IPv4IP_Object = MibScalar
mbgLtCfgEthernetIf4IPv4IP = _MbgLtCfgEthernetIf4IPv4IP_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 4, 1),
    _MbgLtCfgEthernetIf4IPv4IP_Type()
)
mbgLtCfgEthernetIf4IPv4IP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf4IPv4IP.setStatus("current")
_MbgLtCfgEthernetIf4IPv4Netmask_Type = DisplayString
_MbgLtCfgEthernetIf4IPv4Netmask_Object = MibScalar
mbgLtCfgEthernetIf4IPv4Netmask = _MbgLtCfgEthernetIf4IPv4Netmask_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 4, 2),
    _MbgLtCfgEthernetIf4IPv4Netmask_Type()
)
mbgLtCfgEthernetIf4IPv4Netmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf4IPv4Netmask.setStatus("current")
_MbgLtCfgEthernetIf4IPv4Gateway_Type = DisplayString
_MbgLtCfgEthernetIf4IPv4Gateway_Object = MibScalar
mbgLtCfgEthernetIf4IPv4Gateway = _MbgLtCfgEthernetIf4IPv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 4, 3),
    _MbgLtCfgEthernetIf4IPv4Gateway_Type()
)
mbgLtCfgEthernetIf4IPv4Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf4IPv4Gateway.setStatus("current")


class _MbgLtCfgEthernetIf4DHCPClient_Type(Integer32):
    """Custom type mbgLtCfgEthernetIf4DHCPClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgEthernetIf4DHCPClient_Type.__name__ = "Integer32"
_MbgLtCfgEthernetIf4DHCPClient_Object = MibScalar
mbgLtCfgEthernetIf4DHCPClient = _MbgLtCfgEthernetIf4DHCPClient_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 4, 4),
    _MbgLtCfgEthernetIf4DHCPClient_Type()
)
mbgLtCfgEthernetIf4DHCPClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf4DHCPClient.setStatus("current")
_MbgLtCfgEthernetIf4IPv6IP1_Type = DisplayString
_MbgLtCfgEthernetIf4IPv6IP1_Object = MibScalar
mbgLtCfgEthernetIf4IPv6IP1 = _MbgLtCfgEthernetIf4IPv6IP1_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 4, 5),
    _MbgLtCfgEthernetIf4IPv6IP1_Type()
)
mbgLtCfgEthernetIf4IPv6IP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf4IPv6IP1.setStatus("current")
_MbgLtCfgEthernetIf4IPv6IP2_Type = DisplayString
_MbgLtCfgEthernetIf4IPv6IP2_Object = MibScalar
mbgLtCfgEthernetIf4IPv6IP2 = _MbgLtCfgEthernetIf4IPv6IP2_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 4, 6),
    _MbgLtCfgEthernetIf4IPv6IP2_Type()
)
mbgLtCfgEthernetIf4IPv6IP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf4IPv6IP2.setStatus("current")
_MbgLtCfgEthernetIf4IPv6IP3_Type = DisplayString
_MbgLtCfgEthernetIf4IPv6IP3_Object = MibScalar
mbgLtCfgEthernetIf4IPv6IP3 = _MbgLtCfgEthernetIf4IPv6IP3_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 4, 7),
    _MbgLtCfgEthernetIf4IPv6IP3_Type()
)
mbgLtCfgEthernetIf4IPv6IP3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf4IPv6IP3.setStatus("current")


class _MbgLtCfgEthernetIf4IPv6Autoconf_Type(Integer32):
    """Custom type mbgLtCfgEthernetIf4IPv6Autoconf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgEthernetIf4IPv6Autoconf_Type.__name__ = "Integer32"
_MbgLtCfgEthernetIf4IPv6Autoconf_Object = MibScalar
mbgLtCfgEthernetIf4IPv6Autoconf = _MbgLtCfgEthernetIf4IPv6Autoconf_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 4, 8),
    _MbgLtCfgEthernetIf4IPv6Autoconf_Type()
)
mbgLtCfgEthernetIf4IPv6Autoconf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf4IPv6Autoconf.setStatus("current")


class _MbgLtCfgEthernetIf4NetLinkMode_Type(Integer32):
    """Custom type mbgLtCfgEthernetIf4NetLinkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("autosensing", 0),
          ("link100full", 4),
          ("link100half", 3),
          ("link10full", 2),
          ("link10half", 1))
    )


_MbgLtCfgEthernetIf4NetLinkMode_Type.__name__ = "Integer32"
_MbgLtCfgEthernetIf4NetLinkMode_Object = MibScalar
mbgLtCfgEthernetIf4NetLinkMode = _MbgLtCfgEthernetIf4NetLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 4, 9),
    _MbgLtCfgEthernetIf4NetLinkMode_Type()
)
mbgLtCfgEthernetIf4NetLinkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf4NetLinkMode.setStatus("current")
_MbgLtCfgEthernetIf5_ObjectIdentity = ObjectIdentity
mbgLtCfgEthernetIf5 = _MbgLtCfgEthernetIf5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 5)
)
_MbgLtCfgEthernetIf5IPv4IP_Type = DisplayString
_MbgLtCfgEthernetIf5IPv4IP_Object = MibScalar
mbgLtCfgEthernetIf5IPv4IP = _MbgLtCfgEthernetIf5IPv4IP_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 5, 1),
    _MbgLtCfgEthernetIf5IPv4IP_Type()
)
mbgLtCfgEthernetIf5IPv4IP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf5IPv4IP.setStatus("current")
_MbgLtCfgEthernetIf5IPv4Netmask_Type = DisplayString
_MbgLtCfgEthernetIf5IPv4Netmask_Object = MibScalar
mbgLtCfgEthernetIf5IPv4Netmask = _MbgLtCfgEthernetIf5IPv4Netmask_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 5, 2),
    _MbgLtCfgEthernetIf5IPv4Netmask_Type()
)
mbgLtCfgEthernetIf5IPv4Netmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf5IPv4Netmask.setStatus("current")
_MbgLtCfgEthernetIf5IPv4Gateway_Type = DisplayString
_MbgLtCfgEthernetIf5IPv4Gateway_Object = MibScalar
mbgLtCfgEthernetIf5IPv4Gateway = _MbgLtCfgEthernetIf5IPv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 5, 3),
    _MbgLtCfgEthernetIf5IPv4Gateway_Type()
)
mbgLtCfgEthernetIf5IPv4Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf5IPv4Gateway.setStatus("current")


class _MbgLtCfgEthernetIf5DHCPClient_Type(Integer32):
    """Custom type mbgLtCfgEthernetIf5DHCPClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgEthernetIf5DHCPClient_Type.__name__ = "Integer32"
_MbgLtCfgEthernetIf5DHCPClient_Object = MibScalar
mbgLtCfgEthernetIf5DHCPClient = _MbgLtCfgEthernetIf5DHCPClient_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 5, 4),
    _MbgLtCfgEthernetIf5DHCPClient_Type()
)
mbgLtCfgEthernetIf5DHCPClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf5DHCPClient.setStatus("current")
_MbgLtCfgEthernetIf5IPv6IP1_Type = DisplayString
_MbgLtCfgEthernetIf5IPv6IP1_Object = MibScalar
mbgLtCfgEthernetIf5IPv6IP1 = _MbgLtCfgEthernetIf5IPv6IP1_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 5, 5),
    _MbgLtCfgEthernetIf5IPv6IP1_Type()
)
mbgLtCfgEthernetIf5IPv6IP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf5IPv6IP1.setStatus("current")
_MbgLtCfgEthernetIf5IPv6IP2_Type = DisplayString
_MbgLtCfgEthernetIf5IPv6IP2_Object = MibScalar
mbgLtCfgEthernetIf5IPv6IP2 = _MbgLtCfgEthernetIf5IPv6IP2_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 5, 6),
    _MbgLtCfgEthernetIf5IPv6IP2_Type()
)
mbgLtCfgEthernetIf5IPv6IP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf5IPv6IP2.setStatus("current")
_MbgLtCfgEthernetIf5IPv6IP3_Type = DisplayString
_MbgLtCfgEthernetIf5IPv6IP3_Object = MibScalar
mbgLtCfgEthernetIf5IPv6IP3 = _MbgLtCfgEthernetIf5IPv6IP3_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 5, 7),
    _MbgLtCfgEthernetIf5IPv6IP3_Type()
)
mbgLtCfgEthernetIf5IPv6IP3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf5IPv6IP3.setStatus("current")


class _MbgLtCfgEthernetIf5IPv6Autoconf_Type(Integer32):
    """Custom type mbgLtCfgEthernetIf5IPv6Autoconf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgEthernetIf5IPv6Autoconf_Type.__name__ = "Integer32"
_MbgLtCfgEthernetIf5IPv6Autoconf_Object = MibScalar
mbgLtCfgEthernetIf5IPv6Autoconf = _MbgLtCfgEthernetIf5IPv6Autoconf_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 5, 8),
    _MbgLtCfgEthernetIf5IPv6Autoconf_Type()
)
mbgLtCfgEthernetIf5IPv6Autoconf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf5IPv6Autoconf.setStatus("current")


class _MbgLtCfgEthernetIf5NetLinkMode_Type(Integer32):
    """Custom type mbgLtCfgEthernetIf5NetLinkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("autosensing", 0),
          ("link100full", 4),
          ("link100half", 3),
          ("link10full", 2),
          ("link10half", 1))
    )


_MbgLtCfgEthernetIf5NetLinkMode_Type.__name__ = "Integer32"
_MbgLtCfgEthernetIf5NetLinkMode_Object = MibScalar
mbgLtCfgEthernetIf5NetLinkMode = _MbgLtCfgEthernetIf5NetLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 5, 9),
    _MbgLtCfgEthernetIf5NetLinkMode_Type()
)
mbgLtCfgEthernetIf5NetLinkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf5NetLinkMode.setStatus("current")
_MbgLtCfgEthernetIf6_ObjectIdentity = ObjectIdentity
mbgLtCfgEthernetIf6 = _MbgLtCfgEthernetIf6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 6)
)
_MbgLtCfgEthernetIf6IPv4IP_Type = DisplayString
_MbgLtCfgEthernetIf6IPv4IP_Object = MibScalar
mbgLtCfgEthernetIf6IPv4IP = _MbgLtCfgEthernetIf6IPv4IP_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 6, 1),
    _MbgLtCfgEthernetIf6IPv4IP_Type()
)
mbgLtCfgEthernetIf6IPv4IP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf6IPv4IP.setStatus("current")
_MbgLtCfgEthernetIf6IPv4Netmask_Type = DisplayString
_MbgLtCfgEthernetIf6IPv4Netmask_Object = MibScalar
mbgLtCfgEthernetIf6IPv4Netmask = _MbgLtCfgEthernetIf6IPv4Netmask_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 6, 2),
    _MbgLtCfgEthernetIf6IPv4Netmask_Type()
)
mbgLtCfgEthernetIf6IPv4Netmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf6IPv4Netmask.setStatus("current")
_MbgLtCfgEthernetIf6IPv4Gateway_Type = DisplayString
_MbgLtCfgEthernetIf6IPv4Gateway_Object = MibScalar
mbgLtCfgEthernetIf6IPv4Gateway = _MbgLtCfgEthernetIf6IPv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 6, 3),
    _MbgLtCfgEthernetIf6IPv4Gateway_Type()
)
mbgLtCfgEthernetIf6IPv4Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf6IPv4Gateway.setStatus("current")


class _MbgLtCfgEthernetIf6DHCPClient_Type(Integer32):
    """Custom type mbgLtCfgEthernetIf6DHCPClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgEthernetIf6DHCPClient_Type.__name__ = "Integer32"
_MbgLtCfgEthernetIf6DHCPClient_Object = MibScalar
mbgLtCfgEthernetIf6DHCPClient = _MbgLtCfgEthernetIf6DHCPClient_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 6, 4),
    _MbgLtCfgEthernetIf6DHCPClient_Type()
)
mbgLtCfgEthernetIf6DHCPClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf6DHCPClient.setStatus("current")
_MbgLtCfgEthernetIf6IPv6IP1_Type = DisplayString
_MbgLtCfgEthernetIf6IPv6IP1_Object = MibScalar
mbgLtCfgEthernetIf6IPv6IP1 = _MbgLtCfgEthernetIf6IPv6IP1_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 6, 5),
    _MbgLtCfgEthernetIf6IPv6IP1_Type()
)
mbgLtCfgEthernetIf6IPv6IP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf6IPv6IP1.setStatus("current")
_MbgLtCfgEthernetIf6IPv6IP2_Type = DisplayString
_MbgLtCfgEthernetIf6IPv6IP2_Object = MibScalar
mbgLtCfgEthernetIf6IPv6IP2 = _MbgLtCfgEthernetIf6IPv6IP2_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 6, 6),
    _MbgLtCfgEthernetIf6IPv6IP2_Type()
)
mbgLtCfgEthernetIf6IPv6IP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf6IPv6IP2.setStatus("current")
_MbgLtCfgEthernetIf6IPv6IP3_Type = DisplayString
_MbgLtCfgEthernetIf6IPv6IP3_Object = MibScalar
mbgLtCfgEthernetIf6IPv6IP3 = _MbgLtCfgEthernetIf6IPv6IP3_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 6, 7),
    _MbgLtCfgEthernetIf6IPv6IP3_Type()
)
mbgLtCfgEthernetIf6IPv6IP3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf6IPv6IP3.setStatus("current")


class _MbgLtCfgEthernetIf6IPv6Autoconf_Type(Integer32):
    """Custom type mbgLtCfgEthernetIf6IPv6Autoconf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgEthernetIf6IPv6Autoconf_Type.__name__ = "Integer32"
_MbgLtCfgEthernetIf6IPv6Autoconf_Object = MibScalar
mbgLtCfgEthernetIf6IPv6Autoconf = _MbgLtCfgEthernetIf6IPv6Autoconf_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 6, 8),
    _MbgLtCfgEthernetIf6IPv6Autoconf_Type()
)
mbgLtCfgEthernetIf6IPv6Autoconf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf6IPv6Autoconf.setStatus("current")


class _MbgLtCfgEthernetIf6NetLinkMode_Type(Integer32):
    """Custom type mbgLtCfgEthernetIf6NetLinkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("autosensing", 0),
          ("link100full", 4),
          ("link100half", 3),
          ("link10full", 2),
          ("link10half", 1))
    )


_MbgLtCfgEthernetIf6NetLinkMode_Type.__name__ = "Integer32"
_MbgLtCfgEthernetIf6NetLinkMode_Object = MibScalar
mbgLtCfgEthernetIf6NetLinkMode = _MbgLtCfgEthernetIf6NetLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 6, 9),
    _MbgLtCfgEthernetIf6NetLinkMode_Type()
)
mbgLtCfgEthernetIf6NetLinkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf6NetLinkMode.setStatus("current")
_MbgLtCfgEthernetIf7_ObjectIdentity = ObjectIdentity
mbgLtCfgEthernetIf7 = _MbgLtCfgEthernetIf7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 7)
)
_MbgLtCfgEthernetIf7IPv4IP_Type = DisplayString
_MbgLtCfgEthernetIf7IPv4IP_Object = MibScalar
mbgLtCfgEthernetIf7IPv4IP = _MbgLtCfgEthernetIf7IPv4IP_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 7, 1),
    _MbgLtCfgEthernetIf7IPv4IP_Type()
)
mbgLtCfgEthernetIf7IPv4IP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf7IPv4IP.setStatus("current")
_MbgLtCfgEthernetIf7IPv4Netmask_Type = DisplayString
_MbgLtCfgEthernetIf7IPv4Netmask_Object = MibScalar
mbgLtCfgEthernetIf7IPv4Netmask = _MbgLtCfgEthernetIf7IPv4Netmask_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 7, 2),
    _MbgLtCfgEthernetIf7IPv4Netmask_Type()
)
mbgLtCfgEthernetIf7IPv4Netmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf7IPv4Netmask.setStatus("current")
_MbgLtCfgEthernetIf7IPv4Gateway_Type = DisplayString
_MbgLtCfgEthernetIf7IPv4Gateway_Object = MibScalar
mbgLtCfgEthernetIf7IPv4Gateway = _MbgLtCfgEthernetIf7IPv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 7, 3),
    _MbgLtCfgEthernetIf7IPv4Gateway_Type()
)
mbgLtCfgEthernetIf7IPv4Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf7IPv4Gateway.setStatus("current")


class _MbgLtCfgEthernetIf7DHCPClient_Type(Integer32):
    """Custom type mbgLtCfgEthernetIf7DHCPClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgEthernetIf7DHCPClient_Type.__name__ = "Integer32"
_MbgLtCfgEthernetIf7DHCPClient_Object = MibScalar
mbgLtCfgEthernetIf7DHCPClient = _MbgLtCfgEthernetIf7DHCPClient_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 7, 4),
    _MbgLtCfgEthernetIf7DHCPClient_Type()
)
mbgLtCfgEthernetIf7DHCPClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf7DHCPClient.setStatus("current")
_MbgLtCfgEthernetIf7IPv6IP1_Type = DisplayString
_MbgLtCfgEthernetIf7IPv6IP1_Object = MibScalar
mbgLtCfgEthernetIf7IPv6IP1 = _MbgLtCfgEthernetIf7IPv6IP1_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 7, 5),
    _MbgLtCfgEthernetIf7IPv6IP1_Type()
)
mbgLtCfgEthernetIf7IPv6IP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf7IPv6IP1.setStatus("current")
_MbgLtCfgEthernetIf7IPv6IP2_Type = DisplayString
_MbgLtCfgEthernetIf7IPv6IP2_Object = MibScalar
mbgLtCfgEthernetIf7IPv6IP2 = _MbgLtCfgEthernetIf7IPv6IP2_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 7, 6),
    _MbgLtCfgEthernetIf7IPv6IP2_Type()
)
mbgLtCfgEthernetIf7IPv6IP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf7IPv6IP2.setStatus("current")
_MbgLtCfgEthernetIf7IPv6IP3_Type = DisplayString
_MbgLtCfgEthernetIf7IPv6IP3_Object = MibScalar
mbgLtCfgEthernetIf7IPv6IP3 = _MbgLtCfgEthernetIf7IPv6IP3_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 7, 7),
    _MbgLtCfgEthernetIf7IPv6IP3_Type()
)
mbgLtCfgEthernetIf7IPv6IP3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf7IPv6IP3.setStatus("current")


class _MbgLtCfgEthernetIf7IPv6Autoconf_Type(Integer32):
    """Custom type mbgLtCfgEthernetIf7IPv6Autoconf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgEthernetIf7IPv6Autoconf_Type.__name__ = "Integer32"
_MbgLtCfgEthernetIf7IPv6Autoconf_Object = MibScalar
mbgLtCfgEthernetIf7IPv6Autoconf = _MbgLtCfgEthernetIf7IPv6Autoconf_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 7, 8),
    _MbgLtCfgEthernetIf7IPv6Autoconf_Type()
)
mbgLtCfgEthernetIf7IPv6Autoconf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf7IPv6Autoconf.setStatus("current")


class _MbgLtCfgEthernetIf7NetLinkMode_Type(Integer32):
    """Custom type mbgLtCfgEthernetIf7NetLinkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("autosensing", 0),
          ("link100full", 4),
          ("link100half", 3),
          ("link10full", 2),
          ("link10half", 1))
    )


_MbgLtCfgEthernetIf7NetLinkMode_Type.__name__ = "Integer32"
_MbgLtCfgEthernetIf7NetLinkMode_Object = MibScalar
mbgLtCfgEthernetIf7NetLinkMode = _MbgLtCfgEthernetIf7NetLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 7, 9),
    _MbgLtCfgEthernetIf7NetLinkMode_Type()
)
mbgLtCfgEthernetIf7NetLinkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf7NetLinkMode.setStatus("current")
_MbgLtCfgEthernetIf8_ObjectIdentity = ObjectIdentity
mbgLtCfgEthernetIf8 = _MbgLtCfgEthernetIf8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 8)
)
_MbgLtCfgEthernetIf8IPv4IP_Type = DisplayString
_MbgLtCfgEthernetIf8IPv4IP_Object = MibScalar
mbgLtCfgEthernetIf8IPv4IP = _MbgLtCfgEthernetIf8IPv4IP_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 8, 1),
    _MbgLtCfgEthernetIf8IPv4IP_Type()
)
mbgLtCfgEthernetIf8IPv4IP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf8IPv4IP.setStatus("current")
_MbgLtCfgEthernetIf8IPv4Netmask_Type = DisplayString
_MbgLtCfgEthernetIf8IPv4Netmask_Object = MibScalar
mbgLtCfgEthernetIf8IPv4Netmask = _MbgLtCfgEthernetIf8IPv4Netmask_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 8, 2),
    _MbgLtCfgEthernetIf8IPv4Netmask_Type()
)
mbgLtCfgEthernetIf8IPv4Netmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf8IPv4Netmask.setStatus("current")
_MbgLtCfgEthernetIf8IPv4Gateway_Type = DisplayString
_MbgLtCfgEthernetIf8IPv4Gateway_Object = MibScalar
mbgLtCfgEthernetIf8IPv4Gateway = _MbgLtCfgEthernetIf8IPv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 8, 3),
    _MbgLtCfgEthernetIf8IPv4Gateway_Type()
)
mbgLtCfgEthernetIf8IPv4Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf8IPv4Gateway.setStatus("current")


class _MbgLtCfgEthernetIf8DHCPClient_Type(Integer32):
    """Custom type mbgLtCfgEthernetIf8DHCPClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgEthernetIf8DHCPClient_Type.__name__ = "Integer32"
_MbgLtCfgEthernetIf8DHCPClient_Object = MibScalar
mbgLtCfgEthernetIf8DHCPClient = _MbgLtCfgEthernetIf8DHCPClient_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 8, 4),
    _MbgLtCfgEthernetIf8DHCPClient_Type()
)
mbgLtCfgEthernetIf8DHCPClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf8DHCPClient.setStatus("current")
_MbgLtCfgEthernetIf8IPv6IP1_Type = DisplayString
_MbgLtCfgEthernetIf8IPv6IP1_Object = MibScalar
mbgLtCfgEthernetIf8IPv6IP1 = _MbgLtCfgEthernetIf8IPv6IP1_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 8, 5),
    _MbgLtCfgEthernetIf8IPv6IP1_Type()
)
mbgLtCfgEthernetIf8IPv6IP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf8IPv6IP1.setStatus("current")
_MbgLtCfgEthernetIf8IPv6IP2_Type = DisplayString
_MbgLtCfgEthernetIf8IPv6IP2_Object = MibScalar
mbgLtCfgEthernetIf8IPv6IP2 = _MbgLtCfgEthernetIf8IPv6IP2_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 8, 6),
    _MbgLtCfgEthernetIf8IPv6IP2_Type()
)
mbgLtCfgEthernetIf8IPv6IP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf8IPv6IP2.setStatus("current")
_MbgLtCfgEthernetIf8IPv6IP3_Type = DisplayString
_MbgLtCfgEthernetIf8IPv6IP3_Object = MibScalar
mbgLtCfgEthernetIf8IPv6IP3 = _MbgLtCfgEthernetIf8IPv6IP3_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 8, 7),
    _MbgLtCfgEthernetIf8IPv6IP3_Type()
)
mbgLtCfgEthernetIf8IPv6IP3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf8IPv6IP3.setStatus("current")


class _MbgLtCfgEthernetIf8IPv6Autoconf_Type(Integer32):
    """Custom type mbgLtCfgEthernetIf8IPv6Autoconf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgEthernetIf8IPv6Autoconf_Type.__name__ = "Integer32"
_MbgLtCfgEthernetIf8IPv6Autoconf_Object = MibScalar
mbgLtCfgEthernetIf8IPv6Autoconf = _MbgLtCfgEthernetIf8IPv6Autoconf_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 8, 8),
    _MbgLtCfgEthernetIf8IPv6Autoconf_Type()
)
mbgLtCfgEthernetIf8IPv6Autoconf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf8IPv6Autoconf.setStatus("current")


class _MbgLtCfgEthernetIf8NetLinkMode_Type(Integer32):
    """Custom type mbgLtCfgEthernetIf8NetLinkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("autosensing", 0),
          ("link100full", 4),
          ("link100half", 3),
          ("link10full", 2),
          ("link10half", 1))
    )


_MbgLtCfgEthernetIf8NetLinkMode_Type.__name__ = "Integer32"
_MbgLtCfgEthernetIf8NetLinkMode_Object = MibScalar
mbgLtCfgEthernetIf8NetLinkMode = _MbgLtCfgEthernetIf8NetLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 8, 9),
    _MbgLtCfgEthernetIf8NetLinkMode_Type()
)
mbgLtCfgEthernetIf8NetLinkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf8NetLinkMode.setStatus("current")
_MbgLtCfgEthernetIf9_ObjectIdentity = ObjectIdentity
mbgLtCfgEthernetIf9 = _MbgLtCfgEthernetIf9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 9)
)
_MbgLtCfgEthernetIf9IPv4IP_Type = DisplayString
_MbgLtCfgEthernetIf9IPv4IP_Object = MibScalar
mbgLtCfgEthernetIf9IPv4IP = _MbgLtCfgEthernetIf9IPv4IP_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 9, 1),
    _MbgLtCfgEthernetIf9IPv4IP_Type()
)
mbgLtCfgEthernetIf9IPv4IP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf9IPv4IP.setStatus("current")
_MbgLtCfgEthernetIf9IPv4Netmask_Type = DisplayString
_MbgLtCfgEthernetIf9IPv4Netmask_Object = MibScalar
mbgLtCfgEthernetIf9IPv4Netmask = _MbgLtCfgEthernetIf9IPv4Netmask_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 9, 2),
    _MbgLtCfgEthernetIf9IPv4Netmask_Type()
)
mbgLtCfgEthernetIf9IPv4Netmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf9IPv4Netmask.setStatus("current")
_MbgLtCfgEthernetIf9IPv4Gateway_Type = DisplayString
_MbgLtCfgEthernetIf9IPv4Gateway_Object = MibScalar
mbgLtCfgEthernetIf9IPv4Gateway = _MbgLtCfgEthernetIf9IPv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 9, 3),
    _MbgLtCfgEthernetIf9IPv4Gateway_Type()
)
mbgLtCfgEthernetIf9IPv4Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf9IPv4Gateway.setStatus("current")


class _MbgLtCfgEthernetIf9DHCPClient_Type(Integer32):
    """Custom type mbgLtCfgEthernetIf9DHCPClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgEthernetIf9DHCPClient_Type.__name__ = "Integer32"
_MbgLtCfgEthernetIf9DHCPClient_Object = MibScalar
mbgLtCfgEthernetIf9DHCPClient = _MbgLtCfgEthernetIf9DHCPClient_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 9, 4),
    _MbgLtCfgEthernetIf9DHCPClient_Type()
)
mbgLtCfgEthernetIf9DHCPClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf9DHCPClient.setStatus("current")
_MbgLtCfgEthernetIf9IPv6IP1_Type = DisplayString
_MbgLtCfgEthernetIf9IPv6IP1_Object = MibScalar
mbgLtCfgEthernetIf9IPv6IP1 = _MbgLtCfgEthernetIf9IPv6IP1_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 9, 5),
    _MbgLtCfgEthernetIf9IPv6IP1_Type()
)
mbgLtCfgEthernetIf9IPv6IP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf9IPv6IP1.setStatus("current")
_MbgLtCfgEthernetIf9IPv6IP2_Type = DisplayString
_MbgLtCfgEthernetIf9IPv6IP2_Object = MibScalar
mbgLtCfgEthernetIf9IPv6IP2 = _MbgLtCfgEthernetIf9IPv6IP2_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 9, 6),
    _MbgLtCfgEthernetIf9IPv6IP2_Type()
)
mbgLtCfgEthernetIf9IPv6IP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf9IPv6IP2.setStatus("current")
_MbgLtCfgEthernetIf9IPv6IP3_Type = DisplayString
_MbgLtCfgEthernetIf9IPv6IP3_Object = MibScalar
mbgLtCfgEthernetIf9IPv6IP3 = _MbgLtCfgEthernetIf9IPv6IP3_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 9, 7),
    _MbgLtCfgEthernetIf9IPv6IP3_Type()
)
mbgLtCfgEthernetIf9IPv6IP3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf9IPv6IP3.setStatus("current")


class _MbgLtCfgEthernetIf9IPv6Autoconf_Type(Integer32):
    """Custom type mbgLtCfgEthernetIf9IPv6Autoconf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MbgLtCfgEthernetIf9IPv6Autoconf_Type.__name__ = "Integer32"
_MbgLtCfgEthernetIf9IPv6Autoconf_Object = MibScalar
mbgLtCfgEthernetIf9IPv6Autoconf = _MbgLtCfgEthernetIf9IPv6Autoconf_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 9, 8),
    _MbgLtCfgEthernetIf9IPv6Autoconf_Type()
)
mbgLtCfgEthernetIf9IPv6Autoconf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf9IPv6Autoconf.setStatus("current")


class _MbgLtCfgEthernetIf9NetLinkMode_Type(Integer32):
    """Custom type mbgLtCfgEthernetIf9NetLinkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("autosensing", 0),
          ("link100full", 4),
          ("link100half", 3),
          ("link10full", 2),
          ("link10half", 1))
    )


_MbgLtCfgEthernetIf9NetLinkMode_Type.__name__ = "Integer32"
_MbgLtCfgEthernetIf9NetLinkMode_Object = MibScalar
mbgLtCfgEthernetIf9NetLinkMode = _MbgLtCfgEthernetIf9NetLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 8, 9, 9),
    _MbgLtCfgEthernetIf9NetLinkMode_Type()
)
mbgLtCfgEthernetIf9NetLinkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgEthernetIf9NetLinkMode.setStatus("current")
_MbgLtCfgSHS_ObjectIdentity = ObjectIdentity
mbgLtCfgSHS = _MbgLtCfgSHS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 9)
)


class _MbgLtCfgSHSCritLimit_Type(Integer32):
    """Custom type mbgLtCfgSHSCritLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_MbgLtCfgSHSCritLimit_Type.__name__ = "Integer32"
_MbgLtCfgSHSCritLimit_Object = MibScalar
mbgLtCfgSHSCritLimit = _MbgLtCfgSHSCritLimit_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 9, 1),
    _MbgLtCfgSHSCritLimit_Type()
)
mbgLtCfgSHSCritLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgSHSCritLimit.setStatus("current")


class _MbgLtCfgSHSWarnLimit_Type(Integer32):
    """Custom type mbgLtCfgSHSWarnLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_MbgLtCfgSHSWarnLimit_Type.__name__ = "Integer32"
_MbgLtCfgSHSWarnLimit_Object = MibScalar
mbgLtCfgSHSWarnLimit = _MbgLtCfgSHSWarnLimit_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 9, 2),
    _MbgLtCfgSHSWarnLimit_Type()
)
mbgLtCfgSHSWarnLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgSHSWarnLimit.setStatus("current")
_MbgLtCfgMRS_ObjectIdentity = ObjectIdentity
mbgLtCfgMRS = _MbgLtCfgMRS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 10)
)
_MbgLtCfgMRSRefPriority_Type = DisplayString
_MbgLtCfgMRSRefPriority_Object = MibScalar
mbgLtCfgMRSRefPriority = _MbgLtCfgMRSRefPriority_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 4, 10, 1),
    _MbgLtCfgMRSRefPriority_Type()
)
mbgLtCfgMRSRefPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCfgMRSRefPriority.setStatus("current")
_MbgLtCmd_ObjectIdentity = ObjectIdentity
mbgLtCmd = _MbgLtCmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 5)
)


class _MbgLtCmdExecute_Type(Integer32):
    """Custom type mbgLtCmdExecute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("doFirmwareUpdate", 2),
          ("doGenerateHTTPSKey", 5),
          ("doGenerateNewNTPAutokeyCert", 7),
          ("doGenerateSSHKey", 4),
          ("doReboot", 1),
          ("doReloadConfig", 3),
          ("doResetFactoryDefaults", 6),
          ("doResetSHSTimeLimitError", 9),
          ("doSendTestNotification", 8),
          ("ready", 0))
    )


_MbgLtCmdExecute_Type.__name__ = "Integer32"
_MbgLtCmdExecute_Object = MibScalar
mbgLtCmdExecute = _MbgLtCmdExecute_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 5, 1),
    _MbgLtCmdExecute_Type()
)
mbgLtCmdExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCmdExecute.setStatus("current")
_MbgLtCmdSetRefTime_Type = DisplayString
_MbgLtCmdSetRefTime_Object = MibScalar
mbgLtCmdSetRefTime = _MbgLtCmdSetRefTime_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 5, 2),
    _MbgLtCmdSetRefTime_Type()
)
mbgLtCmdSetRefTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtCmdSetRefTime.setStatus("current")
_MbgLtPtp_ObjectIdentity = ObjectIdentity
mbgLtPtp = _MbgLtPtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 10)
)
_MbgLtPtpMode_Type = DisplayString
_MbgLtPtpMode_Object = MibScalar
mbgLtPtpMode = _MbgLtPtpMode_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 10, 1),
    _MbgLtPtpMode_Type()
)
mbgLtPtpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtPtpMode.setStatus("current")


class _MbgLtPtpModeVal_Type(Integer32):
    """Custom type mbgLtPtpModeVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("ordinary", 3),
          ("slave", 2),
          ("stopped", 0))
    )


_MbgLtPtpModeVal_Type.__name__ = "Integer32"
_MbgLtPtpModeVal_Object = MibScalar
mbgLtPtpModeVal = _MbgLtPtpModeVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 10, 2),
    _MbgLtPtpModeVal_Type()
)
mbgLtPtpModeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtPtpModeVal.setStatus("current")
_MbgLtPtpPortState_Type = DisplayString
_MbgLtPtpPortState_Object = MibScalar
mbgLtPtpPortState = _MbgLtPtpPortState_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 10, 3),
    _MbgLtPtpPortState_Type()
)
mbgLtPtpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtPtpPortState.setStatus("current")


class _MbgLtPtpPortStateVal_Type(Integer32):
    """Custom type mbgLtPtpPortStateVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("initializing", 1),
          ("listening", 2),
          ("master", 3),
          ("slave", 4),
          ("uncalibrated", 0),
          ("unicastmaster", 5),
          ("unicastslave", 6))
    )


_MbgLtPtpPortStateVal_Type.__name__ = "Integer32"
_MbgLtPtpPortStateVal_Object = MibScalar
mbgLtPtpPortStateVal = _MbgLtPtpPortStateVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 10, 4),
    _MbgLtPtpPortStateVal_Type()
)
mbgLtPtpPortStateVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtPtpPortStateVal.setStatus("current")
_MbgLtPtpOffsetFromGM_Type = DisplayString
_MbgLtPtpOffsetFromGM_Object = MibScalar
mbgLtPtpOffsetFromGM = _MbgLtPtpOffsetFromGM_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 10, 5),
    _MbgLtPtpOffsetFromGM_Type()
)
mbgLtPtpOffsetFromGM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtPtpOffsetFromGM.setStatus("current")


class _MbgLtPtpOffsetFromGMVal_Type(Integer32):
    """Custom type mbgLtPtpOffsetFromGMVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_MbgLtPtpOffsetFromGMVal_Type.__name__ = "Integer32"
_MbgLtPtpOffsetFromGMVal_Object = MibScalar
mbgLtPtpOffsetFromGMVal = _MbgLtPtpOffsetFromGMVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 10, 6),
    _MbgLtPtpOffsetFromGMVal_Type()
)
mbgLtPtpOffsetFromGMVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtPtpOffsetFromGMVal.setStatus("current")
if mibBuilder.loadTexts:
    mbgLtPtpOffsetFromGMVal.setUnits("ns")
_MbgLtPtpDelay_Type = DisplayString
_MbgLtPtpDelay_Object = MibScalar
mbgLtPtpDelay = _MbgLtPtpDelay_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 10, 7),
    _MbgLtPtpDelay_Type()
)
mbgLtPtpDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtPtpDelay.setStatus("current")
if mibBuilder.loadTexts:
    mbgLtPtpDelay.setUnits("ns")


class _MbgLtPtpDelayVal_Type(Integer32):
    """Custom type mbgLtPtpDelayVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_MbgLtPtpDelayVal_Type.__name__ = "Integer32"
_MbgLtPtpDelayVal_Object = MibScalar
mbgLtPtpDelayVal = _MbgLtPtpDelayVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 10, 8),
    _MbgLtPtpDelayVal_Type()
)
mbgLtPtpDelayVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtPtpDelayVal.setStatus("current")
if mibBuilder.loadTexts:
    mbgLtPtpDelayVal.setUnits("ns")
_MbgLtFdm_ObjectIdentity = ObjectIdentity
mbgLtFdm = _MbgLtFdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 11)
)


class _MbgLtFdmPlFreq_Type(Integer32):
    """Custom type mbgLtFdmPlFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_MbgLtFdmPlFreq_Type.__name__ = "Integer32"
_MbgLtFdmPlFreq_Object = MibScalar
mbgLtFdmPlFreq = _MbgLtFdmPlFreq_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 11, 1),
    _MbgLtFdmPlFreq_Type()
)
mbgLtFdmPlFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtFdmPlFreq.setStatus("current")


class _MbgLtFdmFreqDev_Type(Integer32):
    """Custom type mbgLtFdmFreqDev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_MbgLtFdmFreqDev_Type.__name__ = "Integer32"
_MbgLtFdmFreqDev_Object = MibScalar
mbgLtFdmFreqDev = _MbgLtFdmFreqDev_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 11, 2),
    _MbgLtFdmFreqDev_Type()
)
mbgLtFdmFreqDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtFdmFreqDev.setStatus("current")


class _MbgLtFdmNomFreq_Type(Integer32):
    """Custom type mbgLtFdmNomFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_MbgLtFdmNomFreq_Type.__name__ = "Integer32"
_MbgLtFdmNomFreq_Object = MibScalar
mbgLtFdmNomFreq = _MbgLtFdmNomFreq_Object(
    (1, 3, 6, 1, 4, 1, 5597, 3, 11, 3),
    _MbgLtFdmNomFreq_Type()
)
mbgLtFdmNomFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtFdmNomFreq.setStatus("current")
_MbgLtConformance_ObjectIdentity = ObjectIdentity
mbgLtConformance = _MbgLtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 90)
)
_MbgLtCompliances_ObjectIdentity = ObjectIdentity
mbgLtCompliances = _MbgLtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 90, 1)
)
_MbgLtGroups_ObjectIdentity = ObjectIdentity
mbgLtGroups = _MbgLtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 3, 90, 2)
)

# Managed Objects groups

mbgLtObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5597, 3, 90, 2, 1)
)
mbgLtObjectsGroup.setObjects(
      *(("MBG-SNMP-LT-MIB", "mbgLtFirmwareVersion"),
        ("MBG-SNMP-LT-MIB", "mbgLtFirmwareVersionVal"),
        ("MBG-SNMP-LT-MIB", "mbgLtNtpCurrentState"),
        ("MBG-SNMP-LT-MIB", "mbgLtNtpCurrentStateVal"),
        ("MBG-SNMP-LT-MIB", "mbgLtNtpStratum"),
        ("MBG-SNMP-LT-MIB", "mbgLtNtpActiveRefclockId"),
        ("MBG-SNMP-LT-MIB", "mbgLtNtpActiveRefclockName"),
        ("MBG-SNMP-LT-MIB", "mbgLtNtpActiveRefclockOffset"),
        ("MBG-SNMP-LT-MIB", "mbgLtNtpActiveRefclockOffsetVal"),
        ("MBG-SNMP-LT-MIB", "mbgLtNtpNumberOfRefclocks"),
        ("MBG-SNMP-LT-MIB", "mbgLtNtpAuthKeyId"),
        ("MBG-SNMP-LT-MIB", "mbgLtNtpVersion"),
        ("MBG-SNMP-LT-MIB", "mbgLtRefClockType"),
        ("MBG-SNMP-LT-MIB", "mbgLtRefClockTypeVal"),
        ("MBG-SNMP-LT-MIB", "mbgLtRefClockMode"),
        ("MBG-SNMP-LT-MIB", "mbgLtRefClockModeVal"),
        ("MBG-SNMP-LT-MIB", "mbgLtRefGpsState"),
        ("MBG-SNMP-LT-MIB", "mbgLtRefGpsStateVal"),
        ("MBG-SNMP-LT-MIB", "mbgLtRefGpsPosition"),
        ("MBG-SNMP-LT-MIB", "mbgLtRefGpsSatellites"),
        ("MBG-SNMP-LT-MIB", "mbgLtRefGpsSatellitesGood"),
        ("MBG-SNMP-LT-MIB", "mbgLtRefGpsSatellitesInView"),
        ("MBG-SNMP-LT-MIB", "mbgLtRefPzfState"),
        ("MBG-SNMP-LT-MIB", "mbgLtRefPzfStateVal"),
        ("MBG-SNMP-LT-MIB", "mbgLtRefPzfKorrelation"),
        ("MBG-SNMP-LT-MIB", "mbgLtRefPzfField"),
        ("MBG-SNMP-LT-MIB", "mbgLtRefGpsMode"),
        ("MBG-SNMP-LT-MIB", "mbgLtRefGpsModeVal"),
        ("MBG-SNMP-LT-MIB", "mbgLtRefIrigMode"),
        ("MBG-SNMP-LT-MIB", "mbgLtRefIrigModeVal"),
        ("MBG-SNMP-LT-MIB", "mbgLtRefPzfMode"),
        ("MBG-SNMP-LT-MIB", "mbgLtRefPzfModeVal"),
        ("MBG-SNMP-LT-MIB", "mbgLtRefIrigState"),
        ("MBG-SNMP-LT-MIB", "mbgLtRefIrigStateVal"),
        ("MBG-SNMP-LT-MIB", "mbgLtRefSHSMode"),
        ("MBG-SNMP-LT-MIB", "mbgLtRefSHSModeVal"),
        ("MBG-SNMP-LT-MIB", "mbgLtRefSHSTimeDiff"),
        ("MBG-SNMP-LT-MIB", "mbgLtRefDctState"),
        ("MBG-SNMP-LT-MIB", "mbgLtRefDctStateVal"),
        ("MBG-SNMP-LT-MIB", "mbgLtRefDctField"),
        ("MBG-SNMP-LT-MIB", "mbgLtRefDctMode"),
        ("MBG-SNMP-LT-MIB", "mbgLtRefDctModeVal"),
        ("MBG-SNMP-LT-MIB", "mbgLtRefGpsLeapSecond"),
        ("MBG-SNMP-LT-MIB", "mbgLtRefGpsLeapCorrection"),
        ("MBG-SNMP-LT-MIB", "mbgLtRefMrsRef"),
        ("MBG-SNMP-LT-MIB", "mbgLtRefMrsRefVal"),
        ("MBG-SNMP-LT-MIB", "mbgLtRefMrsRefList"),
        ("MBG-SNMP-LT-MIB", "mbgLtRefMrsPrioList"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsGpsOffs"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsGpsOffsVal"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsGpsOffsBase"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsGpsPrio"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsGpsState"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsGpsStateVal"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsGpsPrecision"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsIrigOffs"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsIrigOffsVal"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsIrigOffsBase"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsIrigPrio"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsIrigState"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsIrigStateVal"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsIrigCorr"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsIrigOffsLimit"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsIrigPrecision"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsPpsOffs"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsPpsOffsVal"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsPpsOffsBase"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsPpsPrio"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsPpsState"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsPpsStateVal"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsPpsCorr"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsPpsOffsLimit"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsPpsPrecision"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsFreqOffs"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsFreqOffsVal"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsFreqOffsBase"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsFreqPrio"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsFreqState"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsFreqStateVal"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsFreqCorr"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsFreqOffsLimit"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsFreqPrecision"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsPtpOffs"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsPtpOffsVal"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsPtpOffsBase"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsPtpPrio"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsPtpState"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsPtpStateVal"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsPtpCorr"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsPtpOffsLimit"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsPtpPrecision"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsNtpOffs"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsNtpOffsVal"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsNtpOffsBase"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsNtpPrio"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsNtpState"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsNtpStateVal"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsNtpCorr"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsNtpOffsLimit"),
        ("MBG-SNMP-LT-MIB", "mbgLtMrsNtpPrecision"),
        ("MBG-SNMP-LT-MIB", "mbgLtTrapMessage"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgHostname"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgDomainname"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNameserver1"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNameserver2"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgSyslogserver1"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgSyslogserver2"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgTelnetAccess"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgFTPAccess"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgHTTPAccess"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgHTTPSAccess"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgSNMPAccess"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgSambaAccess"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgIPv6Access"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgSSHAccess"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNTPServer1IP"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNTPServer1Key"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNTPServer1Autokey"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNTPServer1Prefer"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNTPServer2IP"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNTPServer2Key"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNTPServer2Autokey"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNTPServer2Prefer"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNTPServer3IP"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNTPServer3Key"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNTPServer3Autokey"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNTPServer3Prefer"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNTPServer4IP"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNTPServer4Key"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNTPServer4Autokey"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNTPServer4Prefer"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNTPServer5IP"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNTPServer5Key"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNTPServer5Autokey"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNTPServer5Prefer"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNTPServer6IP"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNTPServer6Key"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNTPServer6Autokey"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNTPServer6Prefer"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNTPServer7IP"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNTPServer7Key"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNTPServer7Autokey"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNTPServer7Prefer"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNTPStratumLocalClock"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNTPTrustedKey"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNTPBroadcastIP"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNTPBroadcastKey"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNTPBroadcastAutokey"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNTPAutokeyFeature"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNTPAtomPPS"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEMailTo"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEMailFrom"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEMailSmarthost"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgSNMPTrapReceiver1"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgSNMPTrapReceiver2"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgSNMPTrapRec1Community"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgSNMPTrapRec2Community"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgSNMPReadOnlyCommunity"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgSNMPReadWriteCommunity"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgSNMPContact"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgSNMPLocation"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgWMailAddress1"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgWMailAddress2"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgVP100Display1IP"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgVP100Display1SN"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgVP100Display2IP"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgVP100Display2SN"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNotifyNTPNotSync"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNotifyNTPStopped"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNotifyServerBoot"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNotifyRefclkNoResponse"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNotifyRefclockNotSync"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNotifyAntennaFaulty"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNotifyAntennaReconnect"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNotifyConfigChanged"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNotifySHSTimeLimitError"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgNotifyLeapSecond"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf0IPv4IP"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf0IPv4Netmask"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf0IPv4Gateway"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf0DHCPClient"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf0IPv6IP1"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf0IPv6IP2"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf0IPv6IP3"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf0IPv6Autoconf"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf0NetLinkMode"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf1IPv4IP"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf1IPv4Netmask"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf1IPv4Gateway"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf1DHCPClient"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf1IPv6IP1"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf1IPv6IP2"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf1IPv6IP3"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf1IPv6Autoconf"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf1NetLinkMode"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf2IPv4IP"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf2IPv4Netmask"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf2IPv4Gateway"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf2DHCPClient"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf2IPv6IP1"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf2IPv6IP2"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf2IPv6IP3"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf2IPv6Autoconf"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf2NetLinkMode"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf3IPv4IP"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf3IPv4Netmask"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf3IPv4Gateway"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf3DHCPClient"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf3IPv6IP1"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf3IPv6IP2"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf3IPv6IP3"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf3IPv6Autoconf"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf3NetLinkMode"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf4IPv4IP"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf4IPv4Netmask"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf4IPv4Gateway"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf4DHCPClient"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf4IPv6IP1"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf4IPv6IP2"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf4IPv6IP3"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf4IPv6Autoconf"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf4NetLinkMode"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf5IPv4IP"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf5IPv4Netmask"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf5IPv4Gateway"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf5DHCPClient"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf5IPv6IP1"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf5IPv6IP2"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf5IPv6IP3"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf5IPv6Autoconf"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf5NetLinkMode"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf6IPv4IP"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf6IPv4Netmask"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf6IPv4Gateway"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf6DHCPClient"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf6IPv6IP1"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf6IPv6IP2"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf6IPv6IP3"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf6IPv6Autoconf"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf6NetLinkMode"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf7IPv4IP"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf7IPv4Netmask"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf7IPv4Gateway"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf7DHCPClient"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf7IPv6IP1"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf7IPv6IP2"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf7IPv6IP3"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf7IPv6Autoconf"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf7NetLinkMode"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf8IPv4IP"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf8IPv4Netmask"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf8IPv4Gateway"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf8DHCPClient"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf8IPv6IP1"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf8IPv6IP2"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf8IPv6IP3"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf8IPv6Autoconf"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf8NetLinkMode"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf9IPv4IP"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf9IPv4Netmask"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf9IPv4Gateway"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf9DHCPClient"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf9IPv6IP1"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf9IPv6IP2"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf9IPv6IP3"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf9IPv6Autoconf"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgEthernetIf9NetLinkMode"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgSHSCritLimit"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgSHSWarnLimit"),
        ("MBG-SNMP-LT-MIB", "mbgLtCfgMRSRefPriority"),
        ("MBG-SNMP-LT-MIB", "mbgLtCmdExecute"),
        ("MBG-SNMP-LT-MIB", "mbgLtCmdSetRefTime"),
        ("MBG-SNMP-LT-MIB", "mbgLtFdmPlFreq"),
        ("MBG-SNMP-LT-MIB", "mbgLtFdmFreqDev"),
        ("MBG-SNMP-LT-MIB", "mbgLtFdmNomFreq"),
        ("MBG-SNMP-LT-MIB", "mbgLtPtpMode"),
        ("MBG-SNMP-LT-MIB", "mbgLtPtpModeVal"),
        ("MBG-SNMP-LT-MIB", "mbgLtPtpPortState"),
        ("MBG-SNMP-LT-MIB", "mbgLtPtpPortStateVal"),
        ("MBG-SNMP-LT-MIB", "mbgLtPtpOffsetFromGM"),
        ("MBG-SNMP-LT-MIB", "mbgLtPtpOffsetFromGMVal"),
        ("MBG-SNMP-LT-MIB", "mbgLtPtpDelay"),
        ("MBG-SNMP-LT-MIB", "mbgLtPtpDelayVal"))
)
if mibBuilder.loadTexts:
    mbgLtObjectsGroup.setStatus("current")


# Notification objects

mbgLtTrapNTPNotSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 3, 3, 0, 1)
)
if mibBuilder.loadTexts:
    mbgLtTrapNTPNotSync.setStatus(
        "current"
    )

mbgLtTrapNTPStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 3, 3, 0, 2)
)
if mibBuilder.loadTexts:
    mbgLtTrapNTPStopped.setStatus(
        "current"
    )

mbgLtTrapServerBoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 3, 3, 0, 3)
)
if mibBuilder.loadTexts:
    mbgLtTrapServerBoot.setStatus(
        "current"
    )

mbgLtTrapReceiverNotResponding = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 3, 3, 0, 4)
)
if mibBuilder.loadTexts:
    mbgLtTrapReceiverNotResponding.setStatus(
        "current"
    )

mbgLtTrapReceiverNotSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 3, 3, 0, 5)
)
if mibBuilder.loadTexts:
    mbgLtTrapReceiverNotSync.setStatus(
        "current"
    )

mbgLtTrapAntennaFaulty = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 3, 3, 0, 6)
)
if mibBuilder.loadTexts:
    mbgLtTrapAntennaFaulty.setStatus(
        "current"
    )

mbgLtTrapAntennaReconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 3, 3, 0, 7)
)
if mibBuilder.loadTexts:
    mbgLtTrapAntennaReconnect.setStatus(
        "current"
    )

mbgLtTrapConfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 3, 3, 0, 8)
)
if mibBuilder.loadTexts:
    mbgLtTrapConfigChanged.setStatus(
        "current"
    )

mbgLtTrapLeapSecondAnnounced = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 3, 3, 0, 9)
)
if mibBuilder.loadTexts:
    mbgLtTrapLeapSecondAnnounced.setStatus(
        "current"
    )

mbgLtTrapSHSTimeLimitError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 3, 3, 0, 10)
)
if mibBuilder.loadTexts:
    mbgLtTrapSHSTimeLimitError.setStatus(
        "current"
    )

mbgLtTrapSecondaryRecNotSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 3, 3, 0, 11)
)
if mibBuilder.loadTexts:
    mbgLtTrapSecondaryRecNotSync.setStatus(
        "current"
    )

mbgLtTrapPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 3, 3, 0, 12)
)
if mibBuilder.loadTexts:
    mbgLtTrapPowerSupplyFailure.setStatus(
        "current"
    )

mbgLtTrapAntennaShortCircuit = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 3, 3, 0, 13)
)
if mibBuilder.loadTexts:
    mbgLtTrapAntennaShortCircuit.setStatus(
        "current"
    )

mbgLtTrapReceiverSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 3, 3, 0, 14)
)
if mibBuilder.loadTexts:
    mbgLtTrapReceiverSync.setStatus(
        "current"
    )

mbgLtTrapNTPClientAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 3, 3, 0, 15)
)
if mibBuilder.loadTexts:
    mbgLtTrapNTPClientAlarm.setStatus(
        "current"
    )

mbgLtTrapPowerSupplyUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 3, 3, 0, 16)
)
if mibBuilder.loadTexts:
    mbgLtTrapPowerSupplyUp.setStatus(
        "current"
    )

mbgLtTrapNetworkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 3, 3, 0, 17)
)
if mibBuilder.loadTexts:
    mbgLtTrapNetworkDown.setStatus(
        "current"
    )

mbgLtTrapNetworkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 3, 3, 0, 18)
)
if mibBuilder.loadTexts:
    mbgLtTrapNetworkUp.setStatus(
        "current"
    )

mbgLtTrapSecondaryRecNotResp = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 3, 3, 0, 19)
)
if mibBuilder.loadTexts:
    mbgLtTrapSecondaryRecNotResp.setStatus(
        "current"
    )

mbgLtTrapXmrLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 3, 3, 0, 30)
)
if mibBuilder.loadTexts:
    mbgLtTrapXmrLimitExceeded.setStatus(
        "current"
    )

mbgLtTrapXmrRefDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 3, 3, 0, 31)
)
if mibBuilder.loadTexts:
    mbgLtTrapXmrRefDisconnect.setStatus(
        "current"
    )

mbgLtTrapXmrRefReconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 3, 3, 0, 32)
)
if mibBuilder.loadTexts:
    mbgLtTrapXmrRefReconnect.setStatus(
        "current"
    )

mbgLtTrapFdmError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 3, 3, 0, 33)
)
if mibBuilder.loadTexts:
    mbgLtTrapFdmError.setStatus(
        "current"
    )

mbgLtTrapSHSTimeLimitWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 3, 3, 0, 34)
)
if mibBuilder.loadTexts:
    mbgLtTrapSHSTimeLimitWarning.setStatus(
        "current"
    )

mbgLtTrapSecondaryRecSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 3, 3, 0, 35)
)
if mibBuilder.loadTexts:
    mbgLtTrapSecondaryRecSync.setStatus(
        "current"
    )

mbgLtTrapNTPSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 3, 3, 0, 36)
)
if mibBuilder.loadTexts:
    mbgLtTrapNTPSync.setStatus(
        "current"
    )

mbgLtTrapPtpPortDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 3, 3, 0, 37)
)
if mibBuilder.loadTexts:
    mbgLtTrapPtpPortDisconnected.setStatus(
        "current"
    )

mbgLtTrapPtpPortConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 3, 3, 0, 38)
)
if mibBuilder.loadTexts:
    mbgLtTrapPtpPortConnected.setStatus(
        "current"
    )

mbgLtTrapPtpStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 3, 3, 0, 39)
)
if mibBuilder.loadTexts:
    mbgLtTrapPtpStateChanged.setStatus(
        "current"
    )

mbgLtTrapPtpError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 3, 3, 0, 40)
)
if mibBuilder.loadTexts:
    mbgLtTrapPtpError.setStatus(
        "current"
    )

mbgLtTrapNormalOperation = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 3, 3, 0, 77)
)
if mibBuilder.loadTexts:
    mbgLtTrapNormalOperation.setStatus(
        "current"
    )

mbgLtTrapHeartbeat = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 3, 3, 0, 88)
)
if mibBuilder.loadTexts:
    mbgLtTrapHeartbeat.setStatus(
        "current"
    )

mbgLtTrapTestNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 3, 3, 0, 99)
)
if mibBuilder.loadTexts:
    mbgLtTrapTestNotification.setStatus(
        "current"
    )


# Notifications groups

mbgLtTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5597, 3, 90, 2, 2)
)
mbgLtTrapsGroup.setObjects(
      *(("MBG-SNMP-LT-MIB", "mbgLtTrapNTPNotSync"),
        ("MBG-SNMP-LT-MIB", "mbgLtTrapNTPStopped"),
        ("MBG-SNMP-LT-MIB", "mbgLtTrapServerBoot"),
        ("MBG-SNMP-LT-MIB", "mbgLtTrapReceiverNotResponding"),
        ("MBG-SNMP-LT-MIB", "mbgLtTrapReceiverNotSync"),
        ("MBG-SNMP-LT-MIB", "mbgLtTrapAntennaFaulty"),
        ("MBG-SNMP-LT-MIB", "mbgLtTrapAntennaReconnect"),
        ("MBG-SNMP-LT-MIB", "mbgLtTrapConfigChanged"),
        ("MBG-SNMP-LT-MIB", "mbgLtTrapLeapSecondAnnounced"),
        ("MBG-SNMP-LT-MIB", "mbgLtTrapSHSTimeLimitError"),
        ("MBG-SNMP-LT-MIB", "mbgLtTrapSecondaryRecNotSync"),
        ("MBG-SNMP-LT-MIB", "mbgLtTrapPowerSupplyFailure"),
        ("MBG-SNMP-LT-MIB", "mbgLtTrapAntennaShortCircuit"),
        ("MBG-SNMP-LT-MIB", "mbgLtTrapReceiverSync"),
        ("MBG-SNMP-LT-MIB", "mbgLtTrapNTPClientAlarm"),
        ("MBG-SNMP-LT-MIB", "mbgLtTrapPowerSupplyUp"),
        ("MBG-SNMP-LT-MIB", "mbgLtTrapNetworkDown"),
        ("MBG-SNMP-LT-MIB", "mbgLtTrapNetworkUp"),
        ("MBG-SNMP-LT-MIB", "mbgLtTrapSecondaryRecNotResp"),
        ("MBG-SNMP-LT-MIB", "mbgLtTrapXmrLimitExceeded"),
        ("MBG-SNMP-LT-MIB", "mbgLtTrapXmrRefDisconnect"),
        ("MBG-SNMP-LT-MIB", "mbgLtTrapXmrRefReconnect"),
        ("MBG-SNMP-LT-MIB", "mbgLtTrapFdmError"),
        ("MBG-SNMP-LT-MIB", "mbgLtTrapSHSTimeLimitWarning"),
        ("MBG-SNMP-LT-MIB", "mbgLtTrapSecondaryRecSync"),
        ("MBG-SNMP-LT-MIB", "mbgLtTrapNTPSync"),
        ("MBG-SNMP-LT-MIB", "mbgLtTrapNormalOperation"),
        ("MBG-SNMP-LT-MIB", "mbgLtTrapHeartbeat"),
        ("MBG-SNMP-LT-MIB", "mbgLtTrapTestNotification"),
        ("MBG-SNMP-LT-MIB", "mbgLtTrapPtpPortDisconnected"),
        ("MBG-SNMP-LT-MIB", "mbgLtTrapPtpPortConnected"),
        ("MBG-SNMP-LT-MIB", "mbgLtTrapPtpStateChanged"),
        ("MBG-SNMP-LT-MIB", "mbgLtTrapPtpError"))
)
if mibBuilder.loadTexts:
    mbgLtTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mbgLtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5597, 3, 90, 1, 1)
)
if mibBuilder.loadTexts:
    mbgLtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MBG-SNMP-LT-MIB",
    **{"mbgLantime": mbgLantime,
       "mbgLtInfo": mbgLtInfo,
       "mbgLtFirmwareVersion": mbgLtFirmwareVersion,
       "mbgLtFirmwareVersionVal": mbgLtFirmwareVersionVal,
       "mbgLtNtp": mbgLtNtp,
       "mbgLtNtpCurrentState": mbgLtNtpCurrentState,
       "mbgLtNtpCurrentStateVal": mbgLtNtpCurrentStateVal,
       "mbgLtNtpStratum": mbgLtNtpStratum,
       "mbgLtNtpActiveRefclockId": mbgLtNtpActiveRefclockId,
       "mbgLtNtpActiveRefclockName": mbgLtNtpActiveRefclockName,
       "mbgLtNtpActiveRefclockOffset": mbgLtNtpActiveRefclockOffset,
       "mbgLtNtpActiveRefclockOffsetVal": mbgLtNtpActiveRefclockOffsetVal,
       "mbgLtNtpNumberOfRefclocks": mbgLtNtpNumberOfRefclocks,
       "mbgLtNtpAuthKeyId": mbgLtNtpAuthKeyId,
       "mbgLtNtpVersion": mbgLtNtpVersion,
       "mbgLtRefclock": mbgLtRefclock,
       "mbgLtRefClockType": mbgLtRefClockType,
       "mbgLtRefClockTypeVal": mbgLtRefClockTypeVal,
       "mbgLtRefClockMode": mbgLtRefClockMode,
       "mbgLtRefClockModeVal": mbgLtRefClockModeVal,
       "mbgLtRefGpsState": mbgLtRefGpsState,
       "mbgLtRefGpsStateVal": mbgLtRefGpsStateVal,
       "mbgLtRefGpsPosition": mbgLtRefGpsPosition,
       "mbgLtRefGpsSatellites": mbgLtRefGpsSatellites,
       "mbgLtRefGpsSatellitesGood": mbgLtRefGpsSatellitesGood,
       "mbgLtRefGpsSatellitesInView": mbgLtRefGpsSatellitesInView,
       "mbgLtRefPzfState": mbgLtRefPzfState,
       "mbgLtRefPzfStateVal": mbgLtRefPzfStateVal,
       "mbgLtRefPzfKorrelation": mbgLtRefPzfKorrelation,
       "mbgLtRefPzfField": mbgLtRefPzfField,
       "mbgLtRefGpsMode": mbgLtRefGpsMode,
       "mbgLtRefGpsModeVal": mbgLtRefGpsModeVal,
       "mbgLtRefIrigMode": mbgLtRefIrigMode,
       "mbgLtRefIrigModeVal": mbgLtRefIrigModeVal,
       "mbgLtRefPzfMode": mbgLtRefPzfMode,
       "mbgLtRefPzfModeVal": mbgLtRefPzfModeVal,
       "mbgLtRefIrigState": mbgLtRefIrigState,
       "mbgLtRefIrigStateVal": mbgLtRefIrigStateVal,
       "mbgLtRefSHSMode": mbgLtRefSHSMode,
       "mbgLtRefSHSModeVal": mbgLtRefSHSModeVal,
       "mbgLtRefSHSTimeDiff": mbgLtRefSHSTimeDiff,
       "mbgLtRefDctState": mbgLtRefDctState,
       "mbgLtRefDctStateVal": mbgLtRefDctStateVal,
       "mbgLtRefDctField": mbgLtRefDctField,
       "mbgLtRefDctMode": mbgLtRefDctMode,
       "mbgLtRefDctModeVal": mbgLtRefDctModeVal,
       "mbgLtRefGpsLeapSecond": mbgLtRefGpsLeapSecond,
       "mbgLtRefGpsLeapCorrection": mbgLtRefGpsLeapCorrection,
       "mbgLtMrs": mbgLtMrs,
       "mbgLtRefMrsRef": mbgLtRefMrsRef,
       "mbgLtRefMrsRefVal": mbgLtRefMrsRefVal,
       "mbgLtRefMrsRefList": mbgLtRefMrsRefList,
       "mbgLtRefMrsPrioList": mbgLtRefMrsPrioList,
       "mbgLtMrsRef": mbgLtMrsRef,
       "mbgLtMrsRefGps": mbgLtMrsRefGps,
       "mbgLtMrsGpsOffs": mbgLtMrsGpsOffs,
       "mbgLtMrsGpsOffsVal": mbgLtMrsGpsOffsVal,
       "mbgLtMrsGpsOffsBase": mbgLtMrsGpsOffsBase,
       "mbgLtMrsGpsPrio": mbgLtMrsGpsPrio,
       "mbgLtMrsGpsState": mbgLtMrsGpsState,
       "mbgLtMrsGpsStateVal": mbgLtMrsGpsStateVal,
       "mbgLtMrsGpsPrecision": mbgLtMrsGpsPrecision,
       "mbgLtMrsRefIrig": mbgLtMrsRefIrig,
       "mbgLtMrsIrigOffs": mbgLtMrsIrigOffs,
       "mbgLtMrsIrigOffsVal": mbgLtMrsIrigOffsVal,
       "mbgLtMrsIrigOffsBase": mbgLtMrsIrigOffsBase,
       "mbgLtMrsIrigPrio": mbgLtMrsIrigPrio,
       "mbgLtMrsIrigState": mbgLtMrsIrigState,
       "mbgLtMrsIrigStateVal": mbgLtMrsIrigStateVal,
       "mbgLtMrsIrigCorr": mbgLtMrsIrigCorr,
       "mbgLtMrsIrigOffsLimit": mbgLtMrsIrigOffsLimit,
       "mbgLtMrsIrigPrecision": mbgLtMrsIrigPrecision,
       "mbgLtMrsRefPps": mbgLtMrsRefPps,
       "mbgLtMrsPpsOffs": mbgLtMrsPpsOffs,
       "mbgLtMrsPpsOffsVal": mbgLtMrsPpsOffsVal,
       "mbgLtMrsPpsOffsBase": mbgLtMrsPpsOffsBase,
       "mbgLtMrsPpsPrio": mbgLtMrsPpsPrio,
       "mbgLtMrsPpsState": mbgLtMrsPpsState,
       "mbgLtMrsPpsStateVal": mbgLtMrsPpsStateVal,
       "mbgLtMrsPpsCorr": mbgLtMrsPpsCorr,
       "mbgLtMrsPpsOffsLimit": mbgLtMrsPpsOffsLimit,
       "mbgLtMrsPpsPrecision": mbgLtMrsPpsPrecision,
       "mbgLtMrsRefFreq": mbgLtMrsRefFreq,
       "mbgLtMrsFreqOffs": mbgLtMrsFreqOffs,
       "mbgLtMrsFreqOffsVal": mbgLtMrsFreqOffsVal,
       "mbgLtMrsFreqOffsBase": mbgLtMrsFreqOffsBase,
       "mbgLtMrsFreqPrio": mbgLtMrsFreqPrio,
       "mbgLtMrsFreqState": mbgLtMrsFreqState,
       "mbgLtMrsFreqStateVal": mbgLtMrsFreqStateVal,
       "mbgLtMrsFreqCorr": mbgLtMrsFreqCorr,
       "mbgLtMrsFreqOffsLimit": mbgLtMrsFreqOffsLimit,
       "mbgLtMrsFreqPrecision": mbgLtMrsFreqPrecision,
       "mbgLtMrsRefPtp": mbgLtMrsRefPtp,
       "mbgLtMrsPtpOffs": mbgLtMrsPtpOffs,
       "mbgLtMrsPtpOffsVal": mbgLtMrsPtpOffsVal,
       "mbgLtMrsPtpOffsBase": mbgLtMrsPtpOffsBase,
       "mbgLtMrsPtpPrio": mbgLtMrsPtpPrio,
       "mbgLtMrsPtpState": mbgLtMrsPtpState,
       "mbgLtMrsPtpStateVal": mbgLtMrsPtpStateVal,
       "mbgLtMrsPtpCorr": mbgLtMrsPtpCorr,
       "mbgLtMrsPtpOffsLimit": mbgLtMrsPtpOffsLimit,
       "mbgLtMrsPtpPrecision": mbgLtMrsPtpPrecision,
       "mbgLtMrsRefNtp": mbgLtMrsRefNtp,
       "mbgLtMrsNtpOffs": mbgLtMrsNtpOffs,
       "mbgLtMrsNtpOffsVal": mbgLtMrsNtpOffsVal,
       "mbgLtMrsNtpOffsBase": mbgLtMrsNtpOffsBase,
       "mbgLtMrsNtpPrio": mbgLtMrsNtpPrio,
       "mbgLtMrsNtpState": mbgLtMrsNtpState,
       "mbgLtMrsNtpStateVal": mbgLtMrsNtpStateVal,
       "mbgLtMrsNtpCorr": mbgLtMrsNtpCorr,
       "mbgLtMrsNtpOffsLimit": mbgLtMrsNtpOffsLimit,
       "mbgLtMrsNtpPrecision": mbgLtMrsNtpPrecision,
       "mbgLtNotifications": mbgLtNotifications,
       "mbgLtTraps": mbgLtTraps,
       "mbgLtTrapNTPNotSync": mbgLtTrapNTPNotSync,
       "mbgLtTrapNTPStopped": mbgLtTrapNTPStopped,
       "mbgLtTrapServerBoot": mbgLtTrapServerBoot,
       "mbgLtTrapReceiverNotResponding": mbgLtTrapReceiverNotResponding,
       "mbgLtTrapReceiverNotSync": mbgLtTrapReceiverNotSync,
       "mbgLtTrapAntennaFaulty": mbgLtTrapAntennaFaulty,
       "mbgLtTrapAntennaReconnect": mbgLtTrapAntennaReconnect,
       "mbgLtTrapConfigChanged": mbgLtTrapConfigChanged,
       "mbgLtTrapLeapSecondAnnounced": mbgLtTrapLeapSecondAnnounced,
       "mbgLtTrapSHSTimeLimitError": mbgLtTrapSHSTimeLimitError,
       "mbgLtTrapSecondaryRecNotSync": mbgLtTrapSecondaryRecNotSync,
       "mbgLtTrapPowerSupplyFailure": mbgLtTrapPowerSupplyFailure,
       "mbgLtTrapAntennaShortCircuit": mbgLtTrapAntennaShortCircuit,
       "mbgLtTrapReceiverSync": mbgLtTrapReceiverSync,
       "mbgLtTrapNTPClientAlarm": mbgLtTrapNTPClientAlarm,
       "mbgLtTrapPowerSupplyUp": mbgLtTrapPowerSupplyUp,
       "mbgLtTrapNetworkDown": mbgLtTrapNetworkDown,
       "mbgLtTrapNetworkUp": mbgLtTrapNetworkUp,
       "mbgLtTrapSecondaryRecNotResp": mbgLtTrapSecondaryRecNotResp,
       "mbgLtTrapXmrLimitExceeded": mbgLtTrapXmrLimitExceeded,
       "mbgLtTrapXmrRefDisconnect": mbgLtTrapXmrRefDisconnect,
       "mbgLtTrapXmrRefReconnect": mbgLtTrapXmrRefReconnect,
       "mbgLtTrapFdmError": mbgLtTrapFdmError,
       "mbgLtTrapSHSTimeLimitWarning": mbgLtTrapSHSTimeLimitWarning,
       "mbgLtTrapSecondaryRecSync": mbgLtTrapSecondaryRecSync,
       "mbgLtTrapNTPSync": mbgLtTrapNTPSync,
       "mbgLtTrapPtpPortDisconnected": mbgLtTrapPtpPortDisconnected,
       "mbgLtTrapPtpPortConnected": mbgLtTrapPtpPortConnected,
       "mbgLtTrapPtpStateChanged": mbgLtTrapPtpStateChanged,
       "mbgLtTrapPtpError": mbgLtTrapPtpError,
       "mbgLtTrapNormalOperation": mbgLtTrapNormalOperation,
       "mbgLtTrapHeartbeat": mbgLtTrapHeartbeat,
       "mbgLtTrapTestNotification": mbgLtTrapTestNotification,
       "mbgLtTrapMessage": mbgLtTrapMessage,
       "mbgLtCfg": mbgLtCfg,
       "mbgLtCfgNetwork": mbgLtCfgNetwork,
       "mbgLtCfgHostname": mbgLtCfgHostname,
       "mbgLtCfgDomainname": mbgLtCfgDomainname,
       "mbgLtCfgNameserver1": mbgLtCfgNameserver1,
       "mbgLtCfgNameserver2": mbgLtCfgNameserver2,
       "mbgLtCfgSyslogserver1": mbgLtCfgSyslogserver1,
       "mbgLtCfgSyslogserver2": mbgLtCfgSyslogserver2,
       "mbgLtCfgTelnetAccess": mbgLtCfgTelnetAccess,
       "mbgLtCfgFTPAccess": mbgLtCfgFTPAccess,
       "mbgLtCfgHTTPAccess": mbgLtCfgHTTPAccess,
       "mbgLtCfgHTTPSAccess": mbgLtCfgHTTPSAccess,
       "mbgLtCfgSNMPAccess": mbgLtCfgSNMPAccess,
       "mbgLtCfgSambaAccess": mbgLtCfgSambaAccess,
       "mbgLtCfgIPv6Access": mbgLtCfgIPv6Access,
       "mbgLtCfgSSHAccess": mbgLtCfgSSHAccess,
       "mbgLtCfgNTP": mbgLtCfgNTP,
       "mbgLtCfgNTPServer1": mbgLtCfgNTPServer1,
       "mbgLtCfgNTPServer1IP": mbgLtCfgNTPServer1IP,
       "mbgLtCfgNTPServer1Key": mbgLtCfgNTPServer1Key,
       "mbgLtCfgNTPServer1Autokey": mbgLtCfgNTPServer1Autokey,
       "mbgLtCfgNTPServer1Prefer": mbgLtCfgNTPServer1Prefer,
       "mbgLtCfgNTPServer2": mbgLtCfgNTPServer2,
       "mbgLtCfgNTPServer2IP": mbgLtCfgNTPServer2IP,
       "mbgLtCfgNTPServer2Key": mbgLtCfgNTPServer2Key,
       "mbgLtCfgNTPServer2Autokey": mbgLtCfgNTPServer2Autokey,
       "mbgLtCfgNTPServer2Prefer": mbgLtCfgNTPServer2Prefer,
       "mbgLtCfgNTPServer3": mbgLtCfgNTPServer3,
       "mbgLtCfgNTPServer3IP": mbgLtCfgNTPServer3IP,
       "mbgLtCfgNTPServer3Key": mbgLtCfgNTPServer3Key,
       "mbgLtCfgNTPServer3Autokey": mbgLtCfgNTPServer3Autokey,
       "mbgLtCfgNTPServer3Prefer": mbgLtCfgNTPServer3Prefer,
       "mbgLtCfgNTPServer4": mbgLtCfgNTPServer4,
       "mbgLtCfgNTPServer4IP": mbgLtCfgNTPServer4IP,
       "mbgLtCfgNTPServer4Key": mbgLtCfgNTPServer4Key,
       "mbgLtCfgNTPServer4Autokey": mbgLtCfgNTPServer4Autokey,
       "mbgLtCfgNTPServer4Prefer": mbgLtCfgNTPServer4Prefer,
       "mbgLtCfgNTPServer5": mbgLtCfgNTPServer5,
       "mbgLtCfgNTPServer5IP": mbgLtCfgNTPServer5IP,
       "mbgLtCfgNTPServer5Key": mbgLtCfgNTPServer5Key,
       "mbgLtCfgNTPServer5Autokey": mbgLtCfgNTPServer5Autokey,
       "mbgLtCfgNTPServer5Prefer": mbgLtCfgNTPServer5Prefer,
       "mbgLtCfgNTPServer6": mbgLtCfgNTPServer6,
       "mbgLtCfgNTPServer6IP": mbgLtCfgNTPServer6IP,
       "mbgLtCfgNTPServer6Key": mbgLtCfgNTPServer6Key,
       "mbgLtCfgNTPServer6Autokey": mbgLtCfgNTPServer6Autokey,
       "mbgLtCfgNTPServer6Prefer": mbgLtCfgNTPServer6Prefer,
       "mbgLtCfgNTPServer7": mbgLtCfgNTPServer7,
       "mbgLtCfgNTPServer7IP": mbgLtCfgNTPServer7IP,
       "mbgLtCfgNTPServer7Key": mbgLtCfgNTPServer7Key,
       "mbgLtCfgNTPServer7Autokey": mbgLtCfgNTPServer7Autokey,
       "mbgLtCfgNTPServer7Prefer": mbgLtCfgNTPServer7Prefer,
       "mbgLtCfgNTPStratumLocalClock": mbgLtCfgNTPStratumLocalClock,
       "mbgLtCfgNTPTrustedKey": mbgLtCfgNTPTrustedKey,
       "mbgLtCfgNTPBroadcastIP": mbgLtCfgNTPBroadcastIP,
       "mbgLtCfgNTPBroadcastKey": mbgLtCfgNTPBroadcastKey,
       "mbgLtCfgNTPBroadcastAutokey": mbgLtCfgNTPBroadcastAutokey,
       "mbgLtCfgNTPAutokeyFeature": mbgLtCfgNTPAutokeyFeature,
       "mbgLtCfgNTPAtomPPS": mbgLtCfgNTPAtomPPS,
       "mbgLtCfgEMail": mbgLtCfgEMail,
       "mbgLtCfgEMailTo": mbgLtCfgEMailTo,
       "mbgLtCfgEMailFrom": mbgLtCfgEMailFrom,
       "mbgLtCfgEMailSmarthost": mbgLtCfgEMailSmarthost,
       "mbgLtCfgSNMP": mbgLtCfgSNMP,
       "mbgLtCfgSNMPTrapReceiver1": mbgLtCfgSNMPTrapReceiver1,
       "mbgLtCfgSNMPTrapReceiver2": mbgLtCfgSNMPTrapReceiver2,
       "mbgLtCfgSNMPTrapRec1Community": mbgLtCfgSNMPTrapRec1Community,
       "mbgLtCfgSNMPTrapRec2Community": mbgLtCfgSNMPTrapRec2Community,
       "mbgLtCfgSNMPReadOnlyCommunity": mbgLtCfgSNMPReadOnlyCommunity,
       "mbgLtCfgSNMPReadWriteCommunity": mbgLtCfgSNMPReadWriteCommunity,
       "mbgLtCfgSNMPContact": mbgLtCfgSNMPContact,
       "mbgLtCfgSNMPLocation": mbgLtCfgSNMPLocation,
       "mbgLtCfgWinpopup": mbgLtCfgWinpopup,
       "mbgLtCfgWMailAddress1": mbgLtCfgWMailAddress1,
       "mbgLtCfgWMailAddress2": mbgLtCfgWMailAddress2,
       "mbgLtCfgWalldisplay": mbgLtCfgWalldisplay,
       "mbgLtCfgVP100Display1IP": mbgLtCfgVP100Display1IP,
       "mbgLtCfgVP100Display1SN": mbgLtCfgVP100Display1SN,
       "mbgLtCfgVP100Display2IP": mbgLtCfgVP100Display2IP,
       "mbgLtCfgVP100Display2SN": mbgLtCfgVP100Display2SN,
       "mbgLtCfgNotify": mbgLtCfgNotify,
       "mbgLtCfgNotifyNTPNotSync": mbgLtCfgNotifyNTPNotSync,
       "mbgLtCfgNotifyNTPStopped": mbgLtCfgNotifyNTPStopped,
       "mbgLtCfgNotifyServerBoot": mbgLtCfgNotifyServerBoot,
       "mbgLtCfgNotifyRefclkNoResponse": mbgLtCfgNotifyRefclkNoResponse,
       "mbgLtCfgNotifyRefclockNotSync": mbgLtCfgNotifyRefclockNotSync,
       "mbgLtCfgNotifyAntennaFaulty": mbgLtCfgNotifyAntennaFaulty,
       "mbgLtCfgNotifyAntennaReconnect": mbgLtCfgNotifyAntennaReconnect,
       "mbgLtCfgNotifyConfigChanged": mbgLtCfgNotifyConfigChanged,
       "mbgLtCfgNotifySHSTimeLimitError": mbgLtCfgNotifySHSTimeLimitError,
       "mbgLtCfgNotifyLeapSecond": mbgLtCfgNotifyLeapSecond,
       "mbgLtCfgEthernet": mbgLtCfgEthernet,
       "mbgLtCfgEthernetIf0": mbgLtCfgEthernetIf0,
       "mbgLtCfgEthernetIf0IPv4IP": mbgLtCfgEthernetIf0IPv4IP,
       "mbgLtCfgEthernetIf0IPv4Netmask": mbgLtCfgEthernetIf0IPv4Netmask,
       "mbgLtCfgEthernetIf0IPv4Gateway": mbgLtCfgEthernetIf0IPv4Gateway,
       "mbgLtCfgEthernetIf0DHCPClient": mbgLtCfgEthernetIf0DHCPClient,
       "mbgLtCfgEthernetIf0IPv6IP1": mbgLtCfgEthernetIf0IPv6IP1,
       "mbgLtCfgEthernetIf0IPv6IP2": mbgLtCfgEthernetIf0IPv6IP2,
       "mbgLtCfgEthernetIf0IPv6IP3": mbgLtCfgEthernetIf0IPv6IP3,
       "mbgLtCfgEthernetIf0IPv6Autoconf": mbgLtCfgEthernetIf0IPv6Autoconf,
       "mbgLtCfgEthernetIf0NetLinkMode": mbgLtCfgEthernetIf0NetLinkMode,
       "mbgLtCfgEthernetIf1": mbgLtCfgEthernetIf1,
       "mbgLtCfgEthernetIf1IPv4IP": mbgLtCfgEthernetIf1IPv4IP,
       "mbgLtCfgEthernetIf1IPv4Netmask": mbgLtCfgEthernetIf1IPv4Netmask,
       "mbgLtCfgEthernetIf1IPv4Gateway": mbgLtCfgEthernetIf1IPv4Gateway,
       "mbgLtCfgEthernetIf1DHCPClient": mbgLtCfgEthernetIf1DHCPClient,
       "mbgLtCfgEthernetIf1IPv6IP1": mbgLtCfgEthernetIf1IPv6IP1,
       "mbgLtCfgEthernetIf1IPv6IP2": mbgLtCfgEthernetIf1IPv6IP2,
       "mbgLtCfgEthernetIf1IPv6IP3": mbgLtCfgEthernetIf1IPv6IP3,
       "mbgLtCfgEthernetIf1IPv6Autoconf": mbgLtCfgEthernetIf1IPv6Autoconf,
       "mbgLtCfgEthernetIf1NetLinkMode": mbgLtCfgEthernetIf1NetLinkMode,
       "mbgLtCfgEthernetIf2": mbgLtCfgEthernetIf2,
       "mbgLtCfgEthernetIf2IPv4IP": mbgLtCfgEthernetIf2IPv4IP,
       "mbgLtCfgEthernetIf2IPv4Netmask": mbgLtCfgEthernetIf2IPv4Netmask,
       "mbgLtCfgEthernetIf2IPv4Gateway": mbgLtCfgEthernetIf2IPv4Gateway,
       "mbgLtCfgEthernetIf2DHCPClient": mbgLtCfgEthernetIf2DHCPClient,
       "mbgLtCfgEthernetIf2IPv6IP1": mbgLtCfgEthernetIf2IPv6IP1,
       "mbgLtCfgEthernetIf2IPv6IP2": mbgLtCfgEthernetIf2IPv6IP2,
       "mbgLtCfgEthernetIf2IPv6IP3": mbgLtCfgEthernetIf2IPv6IP3,
       "mbgLtCfgEthernetIf2IPv6Autoconf": mbgLtCfgEthernetIf2IPv6Autoconf,
       "mbgLtCfgEthernetIf2NetLinkMode": mbgLtCfgEthernetIf2NetLinkMode,
       "mbgLtCfgEthernetIf3": mbgLtCfgEthernetIf3,
       "mbgLtCfgEthernetIf3IPv4IP": mbgLtCfgEthernetIf3IPv4IP,
       "mbgLtCfgEthernetIf3IPv4Netmask": mbgLtCfgEthernetIf3IPv4Netmask,
       "mbgLtCfgEthernetIf3IPv4Gateway": mbgLtCfgEthernetIf3IPv4Gateway,
       "mbgLtCfgEthernetIf3DHCPClient": mbgLtCfgEthernetIf3DHCPClient,
       "mbgLtCfgEthernetIf3IPv6IP1": mbgLtCfgEthernetIf3IPv6IP1,
       "mbgLtCfgEthernetIf3IPv6IP2": mbgLtCfgEthernetIf3IPv6IP2,
       "mbgLtCfgEthernetIf3IPv6IP3": mbgLtCfgEthernetIf3IPv6IP3,
       "mbgLtCfgEthernetIf3IPv6Autoconf": mbgLtCfgEthernetIf3IPv6Autoconf,
       "mbgLtCfgEthernetIf3NetLinkMode": mbgLtCfgEthernetIf3NetLinkMode,
       "mbgLtCfgEthernetIf4": mbgLtCfgEthernetIf4,
       "mbgLtCfgEthernetIf4IPv4IP": mbgLtCfgEthernetIf4IPv4IP,
       "mbgLtCfgEthernetIf4IPv4Netmask": mbgLtCfgEthernetIf4IPv4Netmask,
       "mbgLtCfgEthernetIf4IPv4Gateway": mbgLtCfgEthernetIf4IPv4Gateway,
       "mbgLtCfgEthernetIf4DHCPClient": mbgLtCfgEthernetIf4DHCPClient,
       "mbgLtCfgEthernetIf4IPv6IP1": mbgLtCfgEthernetIf4IPv6IP1,
       "mbgLtCfgEthernetIf4IPv6IP2": mbgLtCfgEthernetIf4IPv6IP2,
       "mbgLtCfgEthernetIf4IPv6IP3": mbgLtCfgEthernetIf4IPv6IP3,
       "mbgLtCfgEthernetIf4IPv6Autoconf": mbgLtCfgEthernetIf4IPv6Autoconf,
       "mbgLtCfgEthernetIf4NetLinkMode": mbgLtCfgEthernetIf4NetLinkMode,
       "mbgLtCfgEthernetIf5": mbgLtCfgEthernetIf5,
       "mbgLtCfgEthernetIf5IPv4IP": mbgLtCfgEthernetIf5IPv4IP,
       "mbgLtCfgEthernetIf5IPv4Netmask": mbgLtCfgEthernetIf5IPv4Netmask,
       "mbgLtCfgEthernetIf5IPv4Gateway": mbgLtCfgEthernetIf5IPv4Gateway,
       "mbgLtCfgEthernetIf5DHCPClient": mbgLtCfgEthernetIf5DHCPClient,
       "mbgLtCfgEthernetIf5IPv6IP1": mbgLtCfgEthernetIf5IPv6IP1,
       "mbgLtCfgEthernetIf5IPv6IP2": mbgLtCfgEthernetIf5IPv6IP2,
       "mbgLtCfgEthernetIf5IPv6IP3": mbgLtCfgEthernetIf5IPv6IP3,
       "mbgLtCfgEthernetIf5IPv6Autoconf": mbgLtCfgEthernetIf5IPv6Autoconf,
       "mbgLtCfgEthernetIf5NetLinkMode": mbgLtCfgEthernetIf5NetLinkMode,
       "mbgLtCfgEthernetIf6": mbgLtCfgEthernetIf6,
       "mbgLtCfgEthernetIf6IPv4IP": mbgLtCfgEthernetIf6IPv4IP,
       "mbgLtCfgEthernetIf6IPv4Netmask": mbgLtCfgEthernetIf6IPv4Netmask,
       "mbgLtCfgEthernetIf6IPv4Gateway": mbgLtCfgEthernetIf6IPv4Gateway,
       "mbgLtCfgEthernetIf6DHCPClient": mbgLtCfgEthernetIf6DHCPClient,
       "mbgLtCfgEthernetIf6IPv6IP1": mbgLtCfgEthernetIf6IPv6IP1,
       "mbgLtCfgEthernetIf6IPv6IP2": mbgLtCfgEthernetIf6IPv6IP2,
       "mbgLtCfgEthernetIf6IPv6IP3": mbgLtCfgEthernetIf6IPv6IP3,
       "mbgLtCfgEthernetIf6IPv6Autoconf": mbgLtCfgEthernetIf6IPv6Autoconf,
       "mbgLtCfgEthernetIf6NetLinkMode": mbgLtCfgEthernetIf6NetLinkMode,
       "mbgLtCfgEthernetIf7": mbgLtCfgEthernetIf7,
       "mbgLtCfgEthernetIf7IPv4IP": mbgLtCfgEthernetIf7IPv4IP,
       "mbgLtCfgEthernetIf7IPv4Netmask": mbgLtCfgEthernetIf7IPv4Netmask,
       "mbgLtCfgEthernetIf7IPv4Gateway": mbgLtCfgEthernetIf7IPv4Gateway,
       "mbgLtCfgEthernetIf7DHCPClient": mbgLtCfgEthernetIf7DHCPClient,
       "mbgLtCfgEthernetIf7IPv6IP1": mbgLtCfgEthernetIf7IPv6IP1,
       "mbgLtCfgEthernetIf7IPv6IP2": mbgLtCfgEthernetIf7IPv6IP2,
       "mbgLtCfgEthernetIf7IPv6IP3": mbgLtCfgEthernetIf7IPv6IP3,
       "mbgLtCfgEthernetIf7IPv6Autoconf": mbgLtCfgEthernetIf7IPv6Autoconf,
       "mbgLtCfgEthernetIf7NetLinkMode": mbgLtCfgEthernetIf7NetLinkMode,
       "mbgLtCfgEthernetIf8": mbgLtCfgEthernetIf8,
       "mbgLtCfgEthernetIf8IPv4IP": mbgLtCfgEthernetIf8IPv4IP,
       "mbgLtCfgEthernetIf8IPv4Netmask": mbgLtCfgEthernetIf8IPv4Netmask,
       "mbgLtCfgEthernetIf8IPv4Gateway": mbgLtCfgEthernetIf8IPv4Gateway,
       "mbgLtCfgEthernetIf8DHCPClient": mbgLtCfgEthernetIf8DHCPClient,
       "mbgLtCfgEthernetIf8IPv6IP1": mbgLtCfgEthernetIf8IPv6IP1,
       "mbgLtCfgEthernetIf8IPv6IP2": mbgLtCfgEthernetIf8IPv6IP2,
       "mbgLtCfgEthernetIf8IPv6IP3": mbgLtCfgEthernetIf8IPv6IP3,
       "mbgLtCfgEthernetIf8IPv6Autoconf": mbgLtCfgEthernetIf8IPv6Autoconf,
       "mbgLtCfgEthernetIf8NetLinkMode": mbgLtCfgEthernetIf8NetLinkMode,
       "mbgLtCfgEthernetIf9": mbgLtCfgEthernetIf9,
       "mbgLtCfgEthernetIf9IPv4IP": mbgLtCfgEthernetIf9IPv4IP,
       "mbgLtCfgEthernetIf9IPv4Netmask": mbgLtCfgEthernetIf9IPv4Netmask,
       "mbgLtCfgEthernetIf9IPv4Gateway": mbgLtCfgEthernetIf9IPv4Gateway,
       "mbgLtCfgEthernetIf9DHCPClient": mbgLtCfgEthernetIf9DHCPClient,
       "mbgLtCfgEthernetIf9IPv6IP1": mbgLtCfgEthernetIf9IPv6IP1,
       "mbgLtCfgEthernetIf9IPv6IP2": mbgLtCfgEthernetIf9IPv6IP2,
       "mbgLtCfgEthernetIf9IPv6IP3": mbgLtCfgEthernetIf9IPv6IP3,
       "mbgLtCfgEthernetIf9IPv6Autoconf": mbgLtCfgEthernetIf9IPv6Autoconf,
       "mbgLtCfgEthernetIf9NetLinkMode": mbgLtCfgEthernetIf9NetLinkMode,
       "mbgLtCfgSHS": mbgLtCfgSHS,
       "mbgLtCfgSHSCritLimit": mbgLtCfgSHSCritLimit,
       "mbgLtCfgSHSWarnLimit": mbgLtCfgSHSWarnLimit,
       "mbgLtCfgMRS": mbgLtCfgMRS,
       "mbgLtCfgMRSRefPriority": mbgLtCfgMRSRefPriority,
       "mbgLtCmd": mbgLtCmd,
       "mbgLtCmdExecute": mbgLtCmdExecute,
       "mbgLtCmdSetRefTime": mbgLtCmdSetRefTime,
       "mbgLtPtp": mbgLtPtp,
       "mbgLtPtpMode": mbgLtPtpMode,
       "mbgLtPtpModeVal": mbgLtPtpModeVal,
       "mbgLtPtpPortState": mbgLtPtpPortState,
       "mbgLtPtpPortStateVal": mbgLtPtpPortStateVal,
       "mbgLtPtpOffsetFromGM": mbgLtPtpOffsetFromGM,
       "mbgLtPtpOffsetFromGMVal": mbgLtPtpOffsetFromGMVal,
       "mbgLtPtpDelay": mbgLtPtpDelay,
       "mbgLtPtpDelayVal": mbgLtPtpDelayVal,
       "mbgLtFdm": mbgLtFdm,
       "mbgLtFdmPlFreq": mbgLtFdmPlFreq,
       "mbgLtFdmFreqDev": mbgLtFdmFreqDev,
       "mbgLtFdmNomFreq": mbgLtFdmNomFreq,
       "mbgLtConformance": mbgLtConformance,
       "mbgLtCompliances": mbgLtCompliances,
       "mbgLtCompliance": mbgLtCompliance,
       "mbgLtGroups": mbgLtGroups,
       "mbgLtObjectsGroup": mbgLtObjectsGroup,
       "mbgLtTrapsGroup": mbgLtTrapsGroup}
)
