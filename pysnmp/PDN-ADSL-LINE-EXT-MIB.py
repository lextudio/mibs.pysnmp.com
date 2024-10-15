# SNMP MIB module (PDN-ADSL-LINE-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-ADSL-LINE-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:13 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(pdn_interfaces,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-interfaces")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

pdnAdslLineExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24)
)
pdnAdslLineExtMIB.setRevisions(
        ("2005-03-29 00:00",
         "2005-01-06 00:00",
         "2004-10-15 00:00",
         "2004-09-10 00:00",
         "2004-04-21 00:00",
         "2004-04-20 00:00",
         "2004-03-01 00:00",
         "2003-12-08 00:00",
         "2003-12-03 00:00",
         "2003-11-19 15:00",
         "2003-11-11 15:00",
         "2003-11-06 15:00",
         "2003-10-31 15:00",
         "2003-10-23 15:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PdnAdslTransmissionModeType(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_PdnAdslLineExtNotifications_ObjectIdentity = ObjectIdentity
pdnAdslLineExtNotifications = _PdnAdslLineExtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 0)
)
_PdnAdslLineExtObjects_ObjectIdentity = ObjectIdentity
pdnAdslLineExtObjects = _PdnAdslLineExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1)
)
_PdnAdslLineExtTable_Object = MibTable
pdnAdslLineExtTable = _PdnAdslLineExtTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 1)
)
if mibBuilder.loadTexts:
    pdnAdslLineExtTable.setStatus("current")
_PdnAdslLineExtEntry_Object = MibTableRow
pdnAdslLineExtEntry = _PdnAdslLineExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 1, 1)
)
pdnAdslLineExtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pdnAdslLineExtEntry.setStatus("current")
_PdnAdslLineTransAtucCap_Type = PdnAdslTransmissionModeType
_PdnAdslLineTransAtucCap_Object = MibTableColumn
pdnAdslLineTransAtucCap = _PdnAdslLineTransAtucCap_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 1, 1, 1),
    _PdnAdslLineTransAtucCap_Type()
)
pdnAdslLineTransAtucCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAdslLineTransAtucCap.setStatus("current")
_PdnAdslLineTransAtucConfig_Type = PdnAdslTransmissionModeType
_PdnAdslLineTransAtucConfig_Object = MibTableColumn
pdnAdslLineTransAtucConfig = _PdnAdslLineTransAtucConfig_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 1, 1, 2),
    _PdnAdslLineTransAtucConfig_Type()
)
pdnAdslLineTransAtucConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnAdslLineTransAtucConfig.setStatus("current")
_PdnAdslLineTransAtucActual_Type = PdnAdslTransmissionModeType
_PdnAdslLineTransAtucActual_Object = MibTableColumn
pdnAdslLineTransAtucActual = _PdnAdslLineTransAtucActual_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 1, 1, 3),
    _PdnAdslLineTransAtucActual_Type()
)
pdnAdslLineTransAtucActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAdslLineTransAtucActual.setStatus("current")


class _PdnAdslLinePowerManagementConfig_Type(Integer32):
    """Custom type pdnAdslLinePowerManagementConfig based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_PdnAdslLinePowerManagementConfig_Type.__name__ = "Integer32"
_PdnAdslLinePowerManagementConfig_Object = MibTableColumn
pdnAdslLinePowerManagementConfig = _PdnAdslLinePowerManagementConfig_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 1, 1, 4),
    _PdnAdslLinePowerManagementConfig_Type()
)
pdnAdslLinePowerManagementConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnAdslLinePowerManagementConfig.setStatus("current")


class _PdnAdslLineSpectrumProfile_Type(SnmpAdminString):
    """Custom type pdnAdslLineSpectrumProfile based on SnmpAdminString"""
    defaultValue = OctetString("DEFVAL")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 32),
    )


_PdnAdslLineSpectrumProfile_Type.__name__ = "SnmpAdminString"
_PdnAdslLineSpectrumProfile_Object = MibTableColumn
pdnAdslLineSpectrumProfile = _PdnAdslLineSpectrumProfile_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 1, 1, 5),
    _PdnAdslLineSpectrumProfile_Type()
)
pdnAdslLineSpectrumProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnAdslLineSpectrumProfile.setStatus("current")


class _PdnAdslLinePmMode_Type(Bits):
    """Custom type pdnAdslLinePmMode based on Bits"""
    namedValues = NamedValues(
        *(("idleStateL3", 0),
          ("lowPwrStateL1L2", 1))
    )

_PdnAdslLinePmMode_Type.__name__ = "Bits"
_PdnAdslLinePmMode_Object = MibTableColumn
pdnAdslLinePmMode = _PdnAdslLinePmMode_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 1, 1, 6),
    _PdnAdslLinePmMode_Type()
)
pdnAdslLinePmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnAdslLinePmMode.setStatus("current")


class _PdnAdslLineL0Time_Type(Unsigned32):
    """Custom type pdnAdslLineL0Time based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PdnAdslLineL0Time_Type.__name__ = "Unsigned32"
_PdnAdslLineL0Time_Object = MibTableColumn
pdnAdslLineL0Time = _PdnAdslLineL0Time_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 1, 1, 7),
    _PdnAdslLineL0Time_Type()
)
pdnAdslLineL0Time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnAdslLineL0Time.setStatus("current")
if mibBuilder.loadTexts:
    pdnAdslLineL0Time.setUnits("seconds")


class _PdnAdslLineL2Time_Type(Unsigned32):
    """Custom type pdnAdslLineL2Time based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PdnAdslLineL2Time_Type.__name__ = "Unsigned32"
_PdnAdslLineL2Time_Object = MibTableColumn
pdnAdslLineL2Time = _PdnAdslLineL2Time_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 1, 1, 8),
    _PdnAdslLineL2Time_Type()
)
pdnAdslLineL2Time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnAdslLineL2Time.setStatus("current")
if mibBuilder.loadTexts:
    pdnAdslLineL2Time.setUnits("seconds")


class _PdnAdslLineL2Atpr_Type(Unsigned32):
    """Custom type pdnAdslLineL2Atpr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_PdnAdslLineL2Atpr_Type.__name__ = "Unsigned32"
_PdnAdslLineL2Atpr_Object = MibTableColumn
pdnAdslLineL2Atpr = _PdnAdslLineL2Atpr_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 1, 1, 9),
    _PdnAdslLineL2Atpr_Type()
)
pdnAdslLineL2Atpr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnAdslLineL2Atpr.setStatus("current")
if mibBuilder.loadTexts:
    pdnAdslLineL2Atpr.setUnits("dB")


class _PdnAdslLineLdsf_Type(Integer32):
    """Custom type pdnAdslLineLdsf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ldsfMode0", 1),
          ("ldsfMode1", 2))
    )


_PdnAdslLineLdsf_Type.__name__ = "Integer32"
_PdnAdslLineLdsf_Object = MibTableColumn
pdnAdslLineLdsf = _PdnAdslLineLdsf_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 1, 1, 10),
    _PdnAdslLineLdsf_Type()
)
pdnAdslLineLdsf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnAdslLineLdsf.setStatus("current")


class _PdnAdslLineL2Atprt_Type(Unsigned32):
    """Custom type pdnAdslLineL2Atprt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_PdnAdslLineL2Atprt_Type.__name__ = "Unsigned32"
_PdnAdslLineL2Atprt_Object = MibTableColumn
pdnAdslLineL2Atprt = _PdnAdslLineL2Atprt_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 1, 1, 11),
    _PdnAdslLineL2Atprt_Type()
)
pdnAdslLineL2Atprt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnAdslLineL2Atprt.setStatus("current")
if mibBuilder.loadTexts:
    pdnAdslLineL2Atprt.setUnits("dB")
_PdnAdslLineSpectrumProfileTable_Object = MibTable
pdnAdslLineSpectrumProfileTable = _PdnAdslLineSpectrumProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 2)
)
if mibBuilder.loadTexts:
    pdnAdslLineSpectrumProfileTable.setStatus("current")
_PdnAdslLineSpectrumProfileEntry_Object = MibTableRow
pdnAdslLineSpectrumProfileEntry = _PdnAdslLineSpectrumProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 2, 1)
)
pdnAdslLineSpectrumProfileEntry.setIndexNames(
    (1, "PDN-ADSL-LINE-EXT-MIB", "pdnAdslLineSpectrumProfileName"),
)
if mibBuilder.loadTexts:
    pdnAdslLineSpectrumProfileEntry.setStatus("current")


class _PdnAdslLineSpectrumProfileName_Type(SnmpAdminString):
    """Custom type pdnAdslLineSpectrumProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PdnAdslLineSpectrumProfileName_Type.__name__ = "SnmpAdminString"
_PdnAdslLineSpectrumProfileName_Object = MibTableColumn
pdnAdslLineSpectrumProfileName = _PdnAdslLineSpectrumProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 2, 1, 1),
    _PdnAdslLineSpectrumProfileName_Type()
)
pdnAdslLineSpectrumProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnAdslLineSpectrumProfileName.setStatus("current")
_PdnAdslLineSpectrumProfileRowStatus_Type = RowStatus
_PdnAdslLineSpectrumProfileRowStatus_Object = MibTableColumn
pdnAdslLineSpectrumProfileRowStatus = _PdnAdslLineSpectrumProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 2, 1, 2),
    _PdnAdslLineSpectrumProfileRowStatus_Type()
)
pdnAdslLineSpectrumProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnAdslLineSpectrumProfileRowStatus.setStatus("current")


class _PdnAdslLineSpectrumModeSpecificPsdProfile_Type(SnmpAdminString):
    """Custom type pdnAdslLineSpectrumModeSpecificPsdProfile based on SnmpAdminString"""
    defaultValue = OctetString("DEFVAL")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PdnAdslLineSpectrumModeSpecificPsdProfile_Type.__name__ = "SnmpAdminString"
_PdnAdslLineSpectrumModeSpecificPsdProfile_Object = MibTableColumn
pdnAdslLineSpectrumModeSpecificPsdProfile = _PdnAdslLineSpectrumModeSpecificPsdProfile_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 2, 1, 3),
    _PdnAdslLineSpectrumModeSpecificPsdProfile_Type()
)
pdnAdslLineSpectrumModeSpecificPsdProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnAdslLineSpectrumModeSpecificPsdProfile.setStatus("current")


class _PdnAdslLineSpectrumAtucCarMaskProfile_Type(SnmpAdminString):
    """Custom type pdnAdslLineSpectrumAtucCarMaskProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PdnAdslLineSpectrumAtucCarMaskProfile_Type.__name__ = "SnmpAdminString"
_PdnAdslLineSpectrumAtucCarMaskProfile_Object = MibTableColumn
pdnAdslLineSpectrumAtucCarMaskProfile = _PdnAdslLineSpectrumAtucCarMaskProfile_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 2, 1, 4),
    _PdnAdslLineSpectrumAtucCarMaskProfile_Type()
)
pdnAdslLineSpectrumAtucCarMaskProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnAdslLineSpectrumAtucCarMaskProfile.setStatus("current")


class _PdnAdslLineSpectrumAturCarMaskProfile_Type(SnmpAdminString):
    """Custom type pdnAdslLineSpectrumAturCarMaskProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PdnAdslLineSpectrumAturCarMaskProfile_Type.__name__ = "SnmpAdminString"
_PdnAdslLineSpectrumAturCarMaskProfile_Object = MibTableColumn
pdnAdslLineSpectrumAturCarMaskProfile = _PdnAdslLineSpectrumAturCarMaskProfile_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 2, 1, 5),
    _PdnAdslLineSpectrumAturCarMaskProfile_Type()
)
pdnAdslLineSpectrumAturCarMaskProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnAdslLineSpectrumAturCarMaskProfile.setStatus("current")
_PdnAdslModeSpecificPsdConfTable_Object = MibTable
pdnAdslModeSpecificPsdConfTable = _PdnAdslModeSpecificPsdConfTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 3)
)
if mibBuilder.loadTexts:
    pdnAdslModeSpecificPsdConfTable.setStatus("current")
_PdnAdslModeSpecificPsdConfEntry_Object = MibTableRow
pdnAdslModeSpecificPsdConfEntry = _PdnAdslModeSpecificPsdConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 3, 1)
)
pdnAdslModeSpecificPsdConfEntry.setIndexNames(
    (0, "PDN-ADSL-LINE-EXT-MIB", "pdnAdslModeSpecificPsdConfProfileName"),
    (0, "PDN-ADSL-LINE-EXT-MIB", "pdnAdslModeSpecificPsdConfAdslMode"),
)
if mibBuilder.loadTexts:
    pdnAdslModeSpecificPsdConfEntry.setStatus("current")


class _PdnAdslModeSpecificPsdConfProfileName_Type(SnmpAdminString):
    """Custom type pdnAdslModeSpecificPsdConfProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PdnAdslModeSpecificPsdConfProfileName_Type.__name__ = "SnmpAdminString"
_PdnAdslModeSpecificPsdConfProfileName_Object = MibTableColumn
pdnAdslModeSpecificPsdConfProfileName = _PdnAdslModeSpecificPsdConfProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 3, 1, 1),
    _PdnAdslModeSpecificPsdConfProfileName_Type()
)
pdnAdslModeSpecificPsdConfProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnAdslModeSpecificPsdConfProfileName.setStatus("current")


class _PdnAdslModeSpecificPsdConfAdslMode_Type(Integer32):
    """Custom type pdnAdslModeSpecificPsdConfAdslMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adsl2", 1),
          ("adsl2NoSplitter", 2),
          ("adsl2plus", 3))
    )


_PdnAdslModeSpecificPsdConfAdslMode_Type.__name__ = "Integer32"
_PdnAdslModeSpecificPsdConfAdslMode_Object = MibTableColumn
pdnAdslModeSpecificPsdConfAdslMode = _PdnAdslModeSpecificPsdConfAdslMode_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 3, 1, 2),
    _PdnAdslModeSpecificPsdConfAdslMode_Type()
)
pdnAdslModeSpecificPsdConfAdslMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnAdslModeSpecificPsdConfAdslMode.setStatus("current")
_PdnAdslModeSpecificPsdConfRowStatus_Type = RowStatus
_PdnAdslModeSpecificPsdConfRowStatus_Object = MibTableColumn
pdnAdslModeSpecificPsdConfRowStatus = _PdnAdslModeSpecificPsdConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 3, 1, 3),
    _PdnAdslModeSpecificPsdConfRowStatus_Type()
)
pdnAdslModeSpecificPsdConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnAdslModeSpecificPsdConfRowStatus.setStatus("current")


class _PdnAdslModeSpecificPsdConfAdslPsdConfProfile_Type(SnmpAdminString):
    """Custom type pdnAdslModeSpecificPsdConfAdslPsdConfProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PdnAdslModeSpecificPsdConfAdslPsdConfProfile_Type.__name__ = "SnmpAdminString"
_PdnAdslModeSpecificPsdConfAdslPsdConfProfile_Object = MibTableColumn
pdnAdslModeSpecificPsdConfAdslPsdConfProfile = _PdnAdslModeSpecificPsdConfAdslPsdConfProfile_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 3, 1, 4),
    _PdnAdslModeSpecificPsdConfAdslPsdConfProfile_Type()
)
pdnAdslModeSpecificPsdConfAdslPsdConfProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnAdslModeSpecificPsdConfAdslPsdConfProfile.setStatus("current")
_PdnAdslPsdConfTable_Object = MibTable
pdnAdslPsdConfTable = _PdnAdslPsdConfTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 4)
)
if mibBuilder.loadTexts:
    pdnAdslPsdConfTable.setStatus("current")
_PdnAdslPsdConfEntry_Object = MibTableRow
pdnAdslPsdConfEntry = _PdnAdslPsdConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 4, 1)
)
pdnAdslPsdConfEntry.setIndexNames(
    (1, "PDN-ADSL-LINE-EXT-MIB", "pdnAdslPsdConfProfileName"),
)
if mibBuilder.loadTexts:
    pdnAdslPsdConfEntry.setStatus("current")


class _PdnAdslPsdConfProfileName_Type(SnmpAdminString):
    """Custom type pdnAdslPsdConfProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PdnAdslPsdConfProfileName_Type.__name__ = "SnmpAdminString"
_PdnAdslPsdConfProfileName_Object = MibTableColumn
pdnAdslPsdConfProfileName = _PdnAdslPsdConfProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 4, 1, 1),
    _PdnAdslPsdConfProfileName_Type()
)
pdnAdslPsdConfProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnAdslPsdConfProfileName.setStatus("current")
_PdnAdslPsdConfRowStatus_Type = RowStatus
_PdnAdslPsdConfRowStatus_Object = MibTableColumn
pdnAdslPsdConfRowStatus = _PdnAdslPsdConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 4, 1, 2),
    _PdnAdslPsdConfRowStatus_Type()
)
pdnAdslPsdConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnAdslPsdConfRowStatus.setStatus("current")


class _PdnAdslPsdConfAtucMaxNomPsd_Type(Integer32):
    """Custom type pdnAdslPsdConfAtucMaxNomPsd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-800, -400),
    )


_PdnAdslPsdConfAtucMaxNomPsd_Type.__name__ = "Integer32"
_PdnAdslPsdConfAtucMaxNomPsd_Object = MibTableColumn
pdnAdslPsdConfAtucMaxNomPsd = _PdnAdslPsdConfAtucMaxNomPsd_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 4, 1, 3),
    _PdnAdslPsdConfAtucMaxNomPsd_Type()
)
pdnAdslPsdConfAtucMaxNomPsd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnAdslPsdConfAtucMaxNomPsd.setStatus("current")
if mibBuilder.loadTexts:
    pdnAdslPsdConfAtucMaxNomPsd.setUnits("tenth dBm/Hz")


class _PdnAdslPsdConfAturMaxNomPsd_Type(Integer32):
    """Custom type pdnAdslPsdConfAturMaxNomPsd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-650, -380),
    )


_PdnAdslPsdConfAturMaxNomPsd_Type.__name__ = "Integer32"
_PdnAdslPsdConfAturMaxNomPsd_Object = MibTableColumn
pdnAdslPsdConfAturMaxNomPsd = _PdnAdslPsdConfAturMaxNomPsd_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 4, 1, 4),
    _PdnAdslPsdConfAturMaxNomPsd_Type()
)
pdnAdslPsdConfAturMaxNomPsd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnAdslPsdConfAturMaxNomPsd.setStatus("current")
if mibBuilder.loadTexts:
    pdnAdslPsdConfAturMaxNomPsd.setUnits("tenth dBm/Hz")


class _PdnAdslPsdConfAtucMaxNomAtp_Type(Unsigned32):
    """Custom type pdnAdslPsdConfAtucMaxNomAtp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PdnAdslPsdConfAtucMaxNomAtp_Type.__name__ = "Unsigned32"
_PdnAdslPsdConfAtucMaxNomAtp_Object = MibTableColumn
pdnAdslPsdConfAtucMaxNomAtp = _PdnAdslPsdConfAtucMaxNomAtp_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 4, 1, 5),
    _PdnAdslPsdConfAtucMaxNomAtp_Type()
)
pdnAdslPsdConfAtucMaxNomAtp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnAdslPsdConfAtucMaxNomAtp.setStatus("current")
if mibBuilder.loadTexts:
    pdnAdslPsdConfAtucMaxNomAtp.setUnits("tenth dBm")


class _PdnAdslPsdConfAturMaxNomAtp_Type(Unsigned32):
    """Custom type pdnAdslPsdConfAturMaxNomAtp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PdnAdslPsdConfAturMaxNomAtp_Type.__name__ = "Unsigned32"
_PdnAdslPsdConfAturMaxNomAtp_Object = MibTableColumn
pdnAdslPsdConfAturMaxNomAtp = _PdnAdslPsdConfAturMaxNomAtp_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 4, 1, 6),
    _PdnAdslPsdConfAturMaxNomAtp_Type()
)
pdnAdslPsdConfAturMaxNomAtp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnAdslPsdConfAturMaxNomAtp.setStatus("current")
if mibBuilder.loadTexts:
    pdnAdslPsdConfAturMaxNomAtp.setUnits("tenth dBm")


class _PdnAdslPsdConfAtucMaxRxPwr_Type(Integer32):
    """Custom type pdnAdslPsdConfAtucMaxRxPwr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, 255),
        ValueRangeConstraint(2048, 2048),
    )


_PdnAdslPsdConfAtucMaxRxPwr_Type.__name__ = "Integer32"
_PdnAdslPsdConfAtucMaxRxPwr_Object = MibTableColumn
pdnAdslPsdConfAtucMaxRxPwr = _PdnAdslPsdConfAtucMaxRxPwr_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 4, 1, 7),
    _PdnAdslPsdConfAtucMaxRxPwr_Type()
)
pdnAdslPsdConfAtucMaxRxPwr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnAdslPsdConfAtucMaxRxPwr.setStatus("current")
if mibBuilder.loadTexts:
    pdnAdslPsdConfAtucMaxRxPwr.setUnits("tenth dBm")
_PdnAdslCarMaskTable_Object = MibTable
pdnAdslCarMaskTable = _PdnAdslCarMaskTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 5)
)
if mibBuilder.loadTexts:
    pdnAdslCarMaskTable.setStatus("current")
_PdnAdslCarMaskEntry_Object = MibTableRow
pdnAdslCarMaskEntry = _PdnAdslCarMaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 5, 1)
)
pdnAdslCarMaskEntry.setIndexNames(
    (0, "PDN-ADSL-LINE-EXT-MIB", "pdnAdslCarMaskProfileName"),
    (0, "PDN-ADSL-LINE-EXT-MIB", "pdnAdslCarMaskSubCarrierIndex"),
)
if mibBuilder.loadTexts:
    pdnAdslCarMaskEntry.setStatus("current")


class _PdnAdslCarMaskProfileName_Type(SnmpAdminString):
    """Custom type pdnAdslCarMaskProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PdnAdslCarMaskProfileName_Type.__name__ = "SnmpAdminString"
_PdnAdslCarMaskProfileName_Object = MibTableColumn
pdnAdslCarMaskProfileName = _PdnAdslCarMaskProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 5, 1, 1),
    _PdnAdslCarMaskProfileName_Type()
)
pdnAdslCarMaskProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnAdslCarMaskProfileName.setStatus("current")
_PdnAdslCarMaskSubCarrierIndex_Type = Unsigned32
_PdnAdslCarMaskSubCarrierIndex_Object = MibTableColumn
pdnAdslCarMaskSubCarrierIndex = _PdnAdslCarMaskSubCarrierIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 5, 1, 2),
    _PdnAdslCarMaskSubCarrierIndex_Type()
)
pdnAdslCarMaskSubCarrierIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnAdslCarMaskSubCarrierIndex.setStatus("current")
_PdnAdslCarMaskRowStatus_Type = RowStatus
_PdnAdslCarMaskRowStatus_Object = MibTableColumn
pdnAdslCarMaskRowStatus = _PdnAdslCarMaskRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 5, 1, 3),
    _PdnAdslCarMaskRowStatus_Type()
)
pdnAdslCarMaskRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnAdslCarMaskRowStatus.setStatus("current")


class _PdnAdslCarMaskSubCarrierStatus_Type(Integer32):
    """Custom type pdnAdslCarMaskSubCarrierStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("masked", 1)
    )


_PdnAdslCarMaskSubCarrierStatus_Type.__name__ = "Integer32"
_PdnAdslCarMaskSubCarrierStatus_Object = MibTableColumn
pdnAdslCarMaskSubCarrierStatus = _PdnAdslCarMaskSubCarrierStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 5, 1, 4),
    _PdnAdslCarMaskSubCarrierStatus_Type()
)
pdnAdslCarMaskSubCarrierStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAdslCarMaskSubCarrierStatus.setStatus("current")
_PdnAdslLineStatusTable_Object = MibTable
pdnAdslLineStatusTable = _PdnAdslLineStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 6)
)
if mibBuilder.loadTexts:
    pdnAdslLineStatusTable.setStatus("current")
_PdnAdslLineStatusEntry_Object = MibTableRow
pdnAdslLineStatusEntry = _PdnAdslLineStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 6, 1)
)
pdnAdslLineStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pdnAdslLineStatusEntry.setStatus("current")


class _PdnAdslLineStatusAtucLineAtn_Type(Unsigned32):
    """Custom type pdnAdslLineStatusAtucLineAtn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1270),
        ValueRangeConstraint(2048, 2048),
    )


_PdnAdslLineStatusAtucLineAtn_Type.__name__ = "Unsigned32"
_PdnAdslLineStatusAtucLineAtn_Object = MibTableColumn
pdnAdslLineStatusAtucLineAtn = _PdnAdslLineStatusAtucLineAtn_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 6, 1, 1),
    _PdnAdslLineStatusAtucLineAtn_Type()
)
pdnAdslLineStatusAtucLineAtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAdslLineStatusAtucLineAtn.setStatus("current")
if mibBuilder.loadTexts:
    pdnAdslLineStatusAtucLineAtn.setUnits("tenth dB")


class _PdnAdslLineStatusAturLineAtn_Type(Unsigned32):
    """Custom type pdnAdslLineStatusAturLineAtn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1270),
        ValueRangeConstraint(2048, 2048),
    )


_PdnAdslLineStatusAturLineAtn_Type.__name__ = "Unsigned32"
_PdnAdslLineStatusAturLineAtn_Object = MibTableColumn
pdnAdslLineStatusAturLineAtn = _PdnAdslLineStatusAturLineAtn_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 6, 1, 2),
    _PdnAdslLineStatusAturLineAtn_Type()
)
pdnAdslLineStatusAturLineAtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAdslLineStatusAturLineAtn.setStatus("current")
if mibBuilder.loadTexts:
    pdnAdslLineStatusAturLineAtn.setUnits("tenth dB")


class _PdnAdslLineStatusAtucSignalAtn_Type(Unsigned32):
    """Custom type pdnAdslLineStatusAtucSignalAtn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1270),
        ValueRangeConstraint(2048, 2048),
    )


_PdnAdslLineStatusAtucSignalAtn_Type.__name__ = "Unsigned32"
_PdnAdslLineStatusAtucSignalAtn_Object = MibTableColumn
pdnAdslLineStatusAtucSignalAtn = _PdnAdslLineStatusAtucSignalAtn_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 6, 1, 3),
    _PdnAdslLineStatusAtucSignalAtn_Type()
)
pdnAdslLineStatusAtucSignalAtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAdslLineStatusAtucSignalAtn.setStatus("current")
if mibBuilder.loadTexts:
    pdnAdslLineStatusAtucSignalAtn.setUnits("tenth dB")


class _PdnAdslLineStatusAturSignalAtn_Type(Unsigned32):
    """Custom type pdnAdslLineStatusAturSignalAtn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1270),
        ValueRangeConstraint(2048, 2048),
    )


_PdnAdslLineStatusAturSignalAtn_Type.__name__ = "Unsigned32"
_PdnAdslLineStatusAturSignalAtn_Object = MibTableColumn
pdnAdslLineStatusAturSignalAtn = _PdnAdslLineStatusAturSignalAtn_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 6, 1, 4),
    _PdnAdslLineStatusAturSignalAtn_Type()
)
pdnAdslLineStatusAturSignalAtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAdslLineStatusAturSignalAtn.setStatus("current")
if mibBuilder.loadTexts:
    pdnAdslLineStatusAturSignalAtn.setUnits("tenth dB")


class _PdnAdslLineStatusAtucSnrMgn_Type(Integer32):
    """Custom type pdnAdslLineStatusAtucSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-640, 630),
        ValueRangeConstraint(2048, 2048),
    )


_PdnAdslLineStatusAtucSnrMgn_Type.__name__ = "Integer32"
_PdnAdslLineStatusAtucSnrMgn_Object = MibTableColumn
pdnAdslLineStatusAtucSnrMgn = _PdnAdslLineStatusAtucSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 6, 1, 5),
    _PdnAdslLineStatusAtucSnrMgn_Type()
)
pdnAdslLineStatusAtucSnrMgn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAdslLineStatusAtucSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    pdnAdslLineStatusAtucSnrMgn.setUnits("tenth dB")


class _PdnAdslLineStatusAturSnrMgn_Type(Integer32):
    """Custom type pdnAdslLineStatusAturSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-640, 630),
        ValueRangeConstraint(2048, 2048),
    )


_PdnAdslLineStatusAturSnrMgn_Type.__name__ = "Integer32"
_PdnAdslLineStatusAturSnrMgn_Object = MibTableColumn
pdnAdslLineStatusAturSnrMgn = _PdnAdslLineStatusAturSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 6, 1, 6),
    _PdnAdslLineStatusAturSnrMgn_Type()
)
pdnAdslLineStatusAturSnrMgn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAdslLineStatusAturSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    pdnAdslLineStatusAturSnrMgn.setUnits("tenth dB")
_PdnAdslLineStatusAtucMaxAttainableLineRate_Type = Gauge32
_PdnAdslLineStatusAtucMaxAttainableLineRate_Object = MibTableColumn
pdnAdslLineStatusAtucMaxAttainableLineRate = _PdnAdslLineStatusAtucMaxAttainableLineRate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 6, 1, 7),
    _PdnAdslLineStatusAtucMaxAttainableLineRate_Type()
)
pdnAdslLineStatusAtucMaxAttainableLineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAdslLineStatusAtucMaxAttainableLineRate.setStatus("current")
if mibBuilder.loadTexts:
    pdnAdslLineStatusAtucMaxAttainableLineRate.setUnits("bps")
_PdnAdslLineStatusAturMaxAttainableLineRate_Type = Gauge32
_PdnAdslLineStatusAturMaxAttainableLineRate_Object = MibTableColumn
pdnAdslLineStatusAturMaxAttainableLineRate = _PdnAdslLineStatusAturMaxAttainableLineRate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 6, 1, 8),
    _PdnAdslLineStatusAturMaxAttainableLineRate_Type()
)
pdnAdslLineStatusAturMaxAttainableLineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAdslLineStatusAturMaxAttainableLineRate.setStatus("current")
if mibBuilder.loadTexts:
    pdnAdslLineStatusAturMaxAttainableLineRate.setUnits("bps")


class _PdnAdslLineStatusAtucActAtp_Type(Integer32):
    """Custom type pdnAdslLineStatusAtucActAtp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-310, 310),
        ValueRangeConstraint(2048, 2048),
    )


_PdnAdslLineStatusAtucActAtp_Type.__name__ = "Integer32"
_PdnAdslLineStatusAtucActAtp_Object = MibTableColumn
pdnAdslLineStatusAtucActAtp = _PdnAdslLineStatusAtucActAtp_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 6, 1, 9),
    _PdnAdslLineStatusAtucActAtp_Type()
)
pdnAdslLineStatusAtucActAtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAdslLineStatusAtucActAtp.setStatus("current")
if mibBuilder.loadTexts:
    pdnAdslLineStatusAtucActAtp.setUnits("tenth dBm")


class _PdnAdslLineStatusAturActAtp_Type(Integer32):
    """Custom type pdnAdslLineStatusAturActAtp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-310, 310),
        ValueRangeConstraint(2048, 2048),
    )


_PdnAdslLineStatusAturActAtp_Type.__name__ = "Integer32"
_PdnAdslLineStatusAturActAtp_Object = MibTableColumn
pdnAdslLineStatusAturActAtp = _PdnAdslLineStatusAturActAtp_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 6, 1, 10),
    _PdnAdslLineStatusAturActAtp_Type()
)
pdnAdslLineStatusAturActAtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAdslLineStatusAturActAtp.setStatus("current")
if mibBuilder.loadTexts:
    pdnAdslLineStatusAturActAtp.setUnits("tenth dBm")
_PdnAdslLineSubCarStatusTable_Object = MibTable
pdnAdslLineSubCarStatusTable = _PdnAdslLineSubCarStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 7)
)
if mibBuilder.loadTexts:
    pdnAdslLineSubCarStatusTable.setStatus("current")
_PdnAdslLineSubCarStatusEntry_Object = MibTableRow
pdnAdslLineSubCarStatusEntry = _PdnAdslLineSubCarStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 7, 1)
)
pdnAdslLineSubCarStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "PDN-ADSL-LINE-EXT-MIB", "pdnAdslLineCarrierIndex"),
)
if mibBuilder.loadTexts:
    pdnAdslLineSubCarStatusEntry.setStatus("current")
_PdnAdslLineCarrierIndex_Type = Unsigned32
_PdnAdslLineCarrierIndex_Object = MibTableColumn
pdnAdslLineCarrierIndex = _PdnAdslLineCarrierIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 7, 1, 1),
    _PdnAdslLineCarrierIndex_Type()
)
pdnAdslLineCarrierIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnAdslLineCarrierIndex.setStatus("current")


class _PdnAdslLineSubCarAtucHlinPs_Type(Integer32):
    """Custom type pdnAdslLineSubCarAtucHlinPs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, -32768),
        ValueRangeConstraint(-32767, 32767),
    )


_PdnAdslLineSubCarAtucHlinPs_Type.__name__ = "Integer32"
_PdnAdslLineSubCarAtucHlinPs_Object = MibTableColumn
pdnAdslLineSubCarAtucHlinPs = _PdnAdslLineSubCarAtucHlinPs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 7, 1, 2),
    _PdnAdslLineSubCarAtucHlinPs_Type()
)
pdnAdslLineSubCarAtucHlinPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAdslLineSubCarAtucHlinPs.setStatus("current")


class _PdnAdslLineSubCarAturHlinPs_Type(Integer32):
    """Custom type pdnAdslLineSubCarAturHlinPs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, -32768),
        ValueRangeConstraint(-32767, 32767),
    )


_PdnAdslLineSubCarAturHlinPs_Type.__name__ = "Integer32"
_PdnAdslLineSubCarAturHlinPs_Object = MibTableColumn
pdnAdslLineSubCarAturHlinPs = _PdnAdslLineSubCarAturHlinPs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 7, 1, 3),
    _PdnAdslLineSubCarAturHlinPs_Type()
)
pdnAdslLineSubCarAturHlinPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAdslLineSubCarAturHlinPs.setStatus("current")


class _PdnAdslLineSubCarAtucHlogMt_Type(Unsigned32):
    """Custom type pdnAdslLineSubCarAtucHlogMt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PdnAdslLineSubCarAtucHlogMt_Type.__name__ = "Unsigned32"
_PdnAdslLineSubCarAtucHlogMt_Object = MibTableColumn
pdnAdslLineSubCarAtucHlogMt = _PdnAdslLineSubCarAtucHlogMt_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 7, 1, 4),
    _PdnAdslLineSubCarAtucHlogMt_Type()
)
pdnAdslLineSubCarAtucHlogMt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAdslLineSubCarAtucHlogMt.setStatus("current")


class _PdnAdslLineSubCarAturHlogMt_Type(Unsigned32):
    """Custom type pdnAdslLineSubCarAturHlogMt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PdnAdslLineSubCarAturHlogMt_Type.__name__ = "Unsigned32"
_PdnAdslLineSubCarAturHlogMt_Object = MibTableColumn
pdnAdslLineSubCarAturHlogMt = _PdnAdslLineSubCarAturHlogMt_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 7, 1, 5),
    _PdnAdslLineSubCarAturHlogMt_Type()
)
pdnAdslLineSubCarAturHlogMt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAdslLineSubCarAturHlogMt.setStatus("current")


class _PdnAdslLineSubCarAtucQlnPs_Type(Unsigned32):
    """Custom type pdnAdslLineSubCarAtucQlnPs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
        ValueRangeConstraint(255, 255),
    )


_PdnAdslLineSubCarAtucQlnPs_Type.__name__ = "Unsigned32"
_PdnAdslLineSubCarAtucQlnPs_Object = MibTableColumn
pdnAdslLineSubCarAtucQlnPs = _PdnAdslLineSubCarAtucQlnPs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 7, 1, 6),
    _PdnAdslLineSubCarAtucQlnPs_Type()
)
pdnAdslLineSubCarAtucQlnPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAdslLineSubCarAtucQlnPs.setStatus("current")
if mibBuilder.loadTexts:
    pdnAdslLineSubCarAtucQlnPs.setUnits("dB")


class _PdnAdslLineSubCarAturQlnPs_Type(Unsigned32):
    """Custom type pdnAdslLineSubCarAturQlnPs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
        ValueRangeConstraint(255, 255),
    )


_PdnAdslLineSubCarAturQlnPs_Type.__name__ = "Unsigned32"
_PdnAdslLineSubCarAturQlnPs_Object = MibTableColumn
pdnAdslLineSubCarAturQlnPs = _PdnAdslLineSubCarAturQlnPs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 7, 1, 7),
    _PdnAdslLineSubCarAturQlnPs_Type()
)
pdnAdslLineSubCarAturQlnPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAdslLineSubCarAturQlnPs.setStatus("current")
if mibBuilder.loadTexts:
    pdnAdslLineSubCarAturQlnPs.setUnits("dB")


class _PdnAdslLineSubCarAtucSnrPs_Type(Unsigned32):
    """Custom type pdnAdslLineSubCarAtucSnrPs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
        ValueRangeConstraint(255, 255),
    )


_PdnAdslLineSubCarAtucSnrPs_Type.__name__ = "Unsigned32"
_PdnAdslLineSubCarAtucSnrPs_Object = MibTableColumn
pdnAdslLineSubCarAtucSnrPs = _PdnAdslLineSubCarAtucSnrPs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 7, 1, 8),
    _PdnAdslLineSubCarAtucSnrPs_Type()
)
pdnAdslLineSubCarAtucSnrPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAdslLineSubCarAtucSnrPs.setStatus("current")
if mibBuilder.loadTexts:
    pdnAdslLineSubCarAtucSnrPs.setUnits("dB")


class _PdnAdslLineSubCarAturSnrPs_Type(Unsigned32):
    """Custom type pdnAdslLineSubCarAturSnrPs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
        ValueRangeConstraint(255, 255),
    )


_PdnAdslLineSubCarAturSnrPs_Type.__name__ = "Unsigned32"
_PdnAdslLineSubCarAturSnrPs_Object = MibTableColumn
pdnAdslLineSubCarAturSnrPs = _PdnAdslLineSubCarAturSnrPs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 7, 1, 9),
    _PdnAdslLineSubCarAturSnrPs_Type()
)
pdnAdslLineSubCarAturSnrPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAdslLineSubCarAturSnrPs.setStatus("current")
if mibBuilder.loadTexts:
    pdnAdslLineSubCarAturSnrPs.setUnits("dB")


class _PdnAdslLineSubCarAtucBitsPs_Type(Unsigned32):
    """Custom type pdnAdslLineSubCarAtucBitsPs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_PdnAdslLineSubCarAtucBitsPs_Type.__name__ = "Unsigned32"
_PdnAdslLineSubCarAtucBitsPs_Object = MibTableColumn
pdnAdslLineSubCarAtucBitsPs = _PdnAdslLineSubCarAtucBitsPs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 7, 1, 10),
    _PdnAdslLineSubCarAtucBitsPs_Type()
)
pdnAdslLineSubCarAtucBitsPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAdslLineSubCarAtucBitsPs.setStatus("current")
if mibBuilder.loadTexts:
    pdnAdslLineSubCarAtucBitsPs.setUnits("Bits")


class _PdnAdslLineSubCarAturBitsPs_Type(Unsigned32):
    """Custom type pdnAdslLineSubCarAturBitsPs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_PdnAdslLineSubCarAturBitsPs_Type.__name__ = "Unsigned32"
_PdnAdslLineSubCarAturBitsPs_Object = MibTableColumn
pdnAdslLineSubCarAturBitsPs = _PdnAdslLineSubCarAturBitsPs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 7, 1, 11),
    _PdnAdslLineSubCarAturBitsPs_Type()
)
pdnAdslLineSubCarAturBitsPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAdslLineSubCarAturBitsPs.setStatus("current")
if mibBuilder.loadTexts:
    pdnAdslLineSubCarAturBitsPs.setUnits("Bits")


class _PdnAdslLineSubCarAtucHlogPs_Type(Unsigned32):
    """Custom type pdnAdslLineSubCarAtucHlogPs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1022),
        ValueRangeConstraint(1023, 1023),
    )


_PdnAdslLineSubCarAtucHlogPs_Type.__name__ = "Unsigned32"
_PdnAdslLineSubCarAtucHlogPs_Object = MibTableColumn
pdnAdslLineSubCarAtucHlogPs = _PdnAdslLineSubCarAtucHlogPs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 7, 1, 12),
    _PdnAdslLineSubCarAtucHlogPs_Type()
)
pdnAdslLineSubCarAtucHlogPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAdslLineSubCarAtucHlogPs.setStatus("current")
if mibBuilder.loadTexts:
    pdnAdslLineSubCarAtucHlogPs.setUnits("dB")


class _PdnAdslLineSubCarAturHlogPs_Type(Unsigned32):
    """Custom type pdnAdslLineSubCarAturHlogPs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1022),
        ValueRangeConstraint(1023, 1023),
    )


_PdnAdslLineSubCarAturHlogPs_Type.__name__ = "Unsigned32"
_PdnAdslLineSubCarAturHlogPs_Object = MibTableColumn
pdnAdslLineSubCarAturHlogPs = _PdnAdslLineSubCarAturHlogPs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 1, 7, 1, 13),
    _PdnAdslLineSubCarAturHlogPs_Type()
)
pdnAdslLineSubCarAturHlogPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAdslLineSubCarAturHlogPs.setStatus("current")
if mibBuilder.loadTexts:
    pdnAdslLineSubCarAturHlogPs.setUnits("dB")
_PdnAdslLineExtAFNs_ObjectIdentity = ObjectIdentity
pdnAdslLineExtAFNs = _PdnAdslLineExtAFNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 2)
)
_PdnAdslLineExtConformance_ObjectIdentity = ObjectIdentity
pdnAdslLineExtConformance = _PdnAdslLineExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 3)
)
_PdnAdslLineExtCompliances_ObjectIdentity = ObjectIdentity
pdnAdslLineExtCompliances = _PdnAdslLineExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 3, 1)
)
_PdnAdslLineExtGroups_ObjectIdentity = ObjectIdentity
pdnAdslLineExtGroups = _PdnAdslLineExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 3, 2)
)
_PdnAdslLineExtObjGroups_ObjectIdentity = ObjectIdentity
pdnAdslLineExtObjGroups = _PdnAdslLineExtObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 3, 2, 1)
)
_PdnAdslLineExtAfnGroups_ObjectIdentity = ObjectIdentity
pdnAdslLineExtAfnGroups = _PdnAdslLineExtAfnGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 3, 2, 2)
)
_PdnAdslLineExtNtfyGroups_ObjectIdentity = ObjectIdentity
pdnAdslLineExtNtfyGroups = _PdnAdslLineExtNtfyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 3, 2, 3)
)

# Managed Objects groups

pdnAdslLineExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 3, 2, 1, 1)
)
pdnAdslLineExtGroup.setObjects(
      *(("PDN-ADSL-LINE-EXT-MIB", "pdnAdslLineTransAtucCap"),
        ("PDN-ADSL-LINE-EXT-MIB", "pdnAdslLineTransAtucConfig"),
        ("PDN-ADSL-LINE-EXT-MIB", "pdnAdslLineTransAtucActual"),
        ("PDN-ADSL-LINE-EXT-MIB", "pdnAdslLinePowerManagementConfig"),
        ("PDN-ADSL-LINE-EXT-MIB", "pdnAdslLineSpectrumProfile"),
        ("PDN-ADSL-LINE-EXT-MIB", "pdnAdslLinePmMode"),
        ("PDN-ADSL-LINE-EXT-MIB", "pdnAdslLineL0Time"),
        ("PDN-ADSL-LINE-EXT-MIB", "pdnAdslLineL2Time"),
        ("PDN-ADSL-LINE-EXT-MIB", "pdnAdslLineL2Atpr"),
        ("PDN-ADSL-LINE-EXT-MIB", "pdnAdslLineLdsf"))
)
if mibBuilder.loadTexts:
    pdnAdslLineExtGroup.setStatus("current")

pdnAdslLineSpectrumGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 3, 2, 1, 2)
)
pdnAdslLineSpectrumGroup.setObjects(
      *(("PDN-ADSL-LINE-EXT-MIB", "pdnAdslLineSpectrumProfileRowStatus"),
        ("PDN-ADSL-LINE-EXT-MIB", "pdnAdslLineSpectrumModeSpecificPsdProfile"),
        ("PDN-ADSL-LINE-EXT-MIB", "pdnAdslLineSpectrumAtucCarMaskProfile"),
        ("PDN-ADSL-LINE-EXT-MIB", "pdnAdslLineSpectrumAturCarMaskProfile"))
)
if mibBuilder.loadTexts:
    pdnAdslLineSpectrumGroup.setStatus("current")

pdnAdslModeSpecificPsdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 3, 2, 1, 3)
)
pdnAdslModeSpecificPsdGroup.setObjects(
      *(("PDN-ADSL-LINE-EXT-MIB", "pdnAdslModeSpecificPsdConfAdslPsdConfProfile"),
        ("PDN-ADSL-LINE-EXT-MIB", "pdnAdslModeSpecificPsdConfRowStatus"))
)
if mibBuilder.loadTexts:
    pdnAdslModeSpecificPsdGroup.setStatus("current")

pdnAdslPsdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 3, 2, 1, 4)
)
pdnAdslPsdGroup.setObjects(
      *(("PDN-ADSL-LINE-EXT-MIB", "pdnAdslPsdConfRowStatus"),
        ("PDN-ADSL-LINE-EXT-MIB", "pdnAdslPsdConfAtucMaxNomPsd"),
        ("PDN-ADSL-LINE-EXT-MIB", "pdnAdslPsdConfAturMaxNomPsd"),
        ("PDN-ADSL-LINE-EXT-MIB", "pdnAdslPsdConfAtucMaxNomAtp"),
        ("PDN-ADSL-LINE-EXT-MIB", "pdnAdslPsdConfAturMaxNomAtp"),
        ("PDN-ADSL-LINE-EXT-MIB", "pdnAdslPsdConfAtucMaxRxPwr"))
)
if mibBuilder.loadTexts:
    pdnAdslPsdGroup.setStatus("current")

pdnAdslCarMaskGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 3, 2, 1, 5)
)
pdnAdslCarMaskGroup.setObjects(
      *(("PDN-ADSL-LINE-EXT-MIB", "pdnAdslCarMaskRowStatus"),
        ("PDN-ADSL-LINE-EXT-MIB", "pdnAdslCarMaskSubCarrierStatus"))
)
if mibBuilder.loadTexts:
    pdnAdslCarMaskGroup.setStatus("current")

pdnAdslLineL2AtprtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 3, 2, 1, 6)
)
pdnAdslLineL2AtprtGroup.setObjects(
    ("PDN-ADSL-LINE-EXT-MIB", "pdnAdslLineL2Atprt")
)
if mibBuilder.loadTexts:
    pdnAdslLineL2AtprtGroup.setStatus("current")

pdnAdslLineStatusLineAtnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 3, 2, 1, 7)
)
pdnAdslLineStatusLineAtnGroup.setObjects(
      *(("PDN-ADSL-LINE-EXT-MIB", "pdnAdslLineStatusAtucLineAtn"),
        ("PDN-ADSL-LINE-EXT-MIB", "pdnAdslLineStatusAturLineAtn"))
)
if mibBuilder.loadTexts:
    pdnAdslLineStatusLineAtnGroup.setStatus("current")

pdnAdslLineStatusSignalAtnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 3, 2, 1, 8)
)
pdnAdslLineStatusSignalAtnGroup.setObjects(
      *(("PDN-ADSL-LINE-EXT-MIB", "pdnAdslLineStatusAtucSignalAtn"),
        ("PDN-ADSL-LINE-EXT-MIB", "pdnAdslLineStatusAturSignalAtn"))
)
if mibBuilder.loadTexts:
    pdnAdslLineStatusSignalAtnGroup.setStatus("current")

pdnAdslLineStatusSnrMgnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 3, 2, 1, 9)
)
pdnAdslLineStatusSnrMgnGroup.setObjects(
      *(("PDN-ADSL-LINE-EXT-MIB", "pdnAdslLineStatusAtucSnrMgn"),
        ("PDN-ADSL-LINE-EXT-MIB", "pdnAdslLineStatusAturSnrMgn"))
)
if mibBuilder.loadTexts:
    pdnAdslLineStatusSnrMgnGroup.setStatus("current")

pdnAdslLineStatusMaxattainableLineRateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 3, 2, 1, 10)
)
pdnAdslLineStatusMaxattainableLineRateGroup.setObjects(
      *(("PDN-ADSL-LINE-EXT-MIB", "pdnAdslLineStatusAtucMaxAttainableLineRate"),
        ("PDN-ADSL-LINE-EXT-MIB", "pdnAdslLineStatusAturMaxAttainableLineRate"))
)
if mibBuilder.loadTexts:
    pdnAdslLineStatusMaxattainableLineRateGroup.setStatus("current")

pdnAdslLineStatusActAtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 3, 2, 1, 11)
)
pdnAdslLineStatusActAtpGroup.setObjects(
      *(("PDN-ADSL-LINE-EXT-MIB", "pdnAdslLineStatusAtucActAtp"),
        ("PDN-ADSL-LINE-EXT-MIB", "pdnAdslLineStatusAturActAtp"))
)
if mibBuilder.loadTexts:
    pdnAdslLineStatusActAtpGroup.setStatus("current")

pdnAdslLineSubCarStatusHlinGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 3, 2, 1, 12)
)
pdnAdslLineSubCarStatusHlinGroup.setObjects(
      *(("PDN-ADSL-LINE-EXT-MIB", "pdnAdslLineSubCarAtucHlinPs"),
        ("PDN-ADSL-LINE-EXT-MIB", "pdnAdslLineSubCarAturHlinPs"))
)
if mibBuilder.loadTexts:
    pdnAdslLineSubCarStatusHlinGroup.setStatus("current")

pdnAdslLineSubCarStatusHlogMtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 3, 2, 1, 13)
)
pdnAdslLineSubCarStatusHlogMtGroup.setObjects(
      *(("PDN-ADSL-LINE-EXT-MIB", "pdnAdslLineSubCarAtucHlogMt"),
        ("PDN-ADSL-LINE-EXT-MIB", "pdnAdslLineSubCarAturHlogMt"))
)
if mibBuilder.loadTexts:
    pdnAdslLineSubCarStatusHlogMtGroup.setStatus("current")

pdnAdslLineSubCarStatusQlnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 3, 2, 1, 14)
)
pdnAdslLineSubCarStatusQlnGroup.setObjects(
      *(("PDN-ADSL-LINE-EXT-MIB", "pdnAdslLineSubCarAtucQlnPs"),
        ("PDN-ADSL-LINE-EXT-MIB", "pdnAdslLineSubCarAturQlnPs"))
)
if mibBuilder.loadTexts:
    pdnAdslLineSubCarStatusQlnGroup.setStatus("current")

pdnAdslLineSubCarStatusSnrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 3, 2, 1, 15)
)
pdnAdslLineSubCarStatusSnrGroup.setObjects(
      *(("PDN-ADSL-LINE-EXT-MIB", "pdnAdslLineSubCarAtucSnrPs"),
        ("PDN-ADSL-LINE-EXT-MIB", "pdnAdslLineSubCarAturSnrPs"))
)
if mibBuilder.loadTexts:
    pdnAdslLineSubCarStatusSnrGroup.setStatus("current")

pdnAdslLineSubCarStatusBitsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 3, 2, 1, 16)
)
pdnAdslLineSubCarStatusBitsGroup.setObjects(
      *(("PDN-ADSL-LINE-EXT-MIB", "pdnAdslLineSubCarAtucBitsPs"),
        ("PDN-ADSL-LINE-EXT-MIB", "pdnAdslLineSubCarAturBitsPs"))
)
if mibBuilder.loadTexts:
    pdnAdslLineSubCarStatusBitsGroup.setStatus("current")

pdnAdslLineSubCarStatusHlogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 3, 2, 1, 17)
)
pdnAdslLineSubCarStatusHlogGroup.setObjects(
      *(("PDN-ADSL-LINE-EXT-MIB", "pdnAdslLineSubCarAtucHlogPs"),
        ("PDN-ADSL-LINE-EXT-MIB", "pdnAdslLineSubCarAturHlogPs"))
)
if mibBuilder.loadTexts:
    pdnAdslLineSubCarStatusHlogGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pdnAdslLineExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 24, 3, 1, 1)
)
if mibBuilder.loadTexts:
    pdnAdslLineExtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-ADSL-LINE-EXT-MIB",
    **{"PdnAdslTransmissionModeType": PdnAdslTransmissionModeType,
       "pdnAdslLineExtMIB": pdnAdslLineExtMIB,
       "pdnAdslLineExtNotifications": pdnAdslLineExtNotifications,
       "pdnAdslLineExtObjects": pdnAdslLineExtObjects,
       "pdnAdslLineExtTable": pdnAdslLineExtTable,
       "pdnAdslLineExtEntry": pdnAdslLineExtEntry,
       "pdnAdslLineTransAtucCap": pdnAdslLineTransAtucCap,
       "pdnAdslLineTransAtucConfig": pdnAdslLineTransAtucConfig,
       "pdnAdslLineTransAtucActual": pdnAdslLineTransAtucActual,
       "pdnAdslLinePowerManagementConfig": pdnAdslLinePowerManagementConfig,
       "pdnAdslLineSpectrumProfile": pdnAdslLineSpectrumProfile,
       "pdnAdslLinePmMode": pdnAdslLinePmMode,
       "pdnAdslLineL0Time": pdnAdslLineL0Time,
       "pdnAdslLineL2Time": pdnAdslLineL2Time,
       "pdnAdslLineL2Atpr": pdnAdslLineL2Atpr,
       "pdnAdslLineLdsf": pdnAdslLineLdsf,
       "pdnAdslLineL2Atprt": pdnAdslLineL2Atprt,
       "pdnAdslLineSpectrumProfileTable": pdnAdslLineSpectrumProfileTable,
       "pdnAdslLineSpectrumProfileEntry": pdnAdslLineSpectrumProfileEntry,
       "pdnAdslLineSpectrumProfileName": pdnAdslLineSpectrumProfileName,
       "pdnAdslLineSpectrumProfileRowStatus": pdnAdslLineSpectrumProfileRowStatus,
       "pdnAdslLineSpectrumModeSpecificPsdProfile": pdnAdslLineSpectrumModeSpecificPsdProfile,
       "pdnAdslLineSpectrumAtucCarMaskProfile": pdnAdslLineSpectrumAtucCarMaskProfile,
       "pdnAdslLineSpectrumAturCarMaskProfile": pdnAdslLineSpectrumAturCarMaskProfile,
       "pdnAdslModeSpecificPsdConfTable": pdnAdslModeSpecificPsdConfTable,
       "pdnAdslModeSpecificPsdConfEntry": pdnAdslModeSpecificPsdConfEntry,
       "pdnAdslModeSpecificPsdConfProfileName": pdnAdslModeSpecificPsdConfProfileName,
       "pdnAdslModeSpecificPsdConfAdslMode": pdnAdslModeSpecificPsdConfAdslMode,
       "pdnAdslModeSpecificPsdConfRowStatus": pdnAdslModeSpecificPsdConfRowStatus,
       "pdnAdslModeSpecificPsdConfAdslPsdConfProfile": pdnAdslModeSpecificPsdConfAdslPsdConfProfile,
       "pdnAdslPsdConfTable": pdnAdslPsdConfTable,
       "pdnAdslPsdConfEntry": pdnAdslPsdConfEntry,
       "pdnAdslPsdConfProfileName": pdnAdslPsdConfProfileName,
       "pdnAdslPsdConfRowStatus": pdnAdslPsdConfRowStatus,
       "pdnAdslPsdConfAtucMaxNomPsd": pdnAdslPsdConfAtucMaxNomPsd,
       "pdnAdslPsdConfAturMaxNomPsd": pdnAdslPsdConfAturMaxNomPsd,
       "pdnAdslPsdConfAtucMaxNomAtp": pdnAdslPsdConfAtucMaxNomAtp,
       "pdnAdslPsdConfAturMaxNomAtp": pdnAdslPsdConfAturMaxNomAtp,
       "pdnAdslPsdConfAtucMaxRxPwr": pdnAdslPsdConfAtucMaxRxPwr,
       "pdnAdslCarMaskTable": pdnAdslCarMaskTable,
       "pdnAdslCarMaskEntry": pdnAdslCarMaskEntry,
       "pdnAdslCarMaskProfileName": pdnAdslCarMaskProfileName,
       "pdnAdslCarMaskSubCarrierIndex": pdnAdslCarMaskSubCarrierIndex,
       "pdnAdslCarMaskRowStatus": pdnAdslCarMaskRowStatus,
       "pdnAdslCarMaskSubCarrierStatus": pdnAdslCarMaskSubCarrierStatus,
       "pdnAdslLineStatusTable": pdnAdslLineStatusTable,
       "pdnAdslLineStatusEntry": pdnAdslLineStatusEntry,
       "pdnAdslLineStatusAtucLineAtn": pdnAdslLineStatusAtucLineAtn,
       "pdnAdslLineStatusAturLineAtn": pdnAdslLineStatusAturLineAtn,
       "pdnAdslLineStatusAtucSignalAtn": pdnAdslLineStatusAtucSignalAtn,
       "pdnAdslLineStatusAturSignalAtn": pdnAdslLineStatusAturSignalAtn,
       "pdnAdslLineStatusAtucSnrMgn": pdnAdslLineStatusAtucSnrMgn,
       "pdnAdslLineStatusAturSnrMgn": pdnAdslLineStatusAturSnrMgn,
       "pdnAdslLineStatusAtucMaxAttainableLineRate": pdnAdslLineStatusAtucMaxAttainableLineRate,
       "pdnAdslLineStatusAturMaxAttainableLineRate": pdnAdslLineStatusAturMaxAttainableLineRate,
       "pdnAdslLineStatusAtucActAtp": pdnAdslLineStatusAtucActAtp,
       "pdnAdslLineStatusAturActAtp": pdnAdslLineStatusAturActAtp,
       "pdnAdslLineSubCarStatusTable": pdnAdslLineSubCarStatusTable,
       "pdnAdslLineSubCarStatusEntry": pdnAdslLineSubCarStatusEntry,
       "pdnAdslLineCarrierIndex": pdnAdslLineCarrierIndex,
       "pdnAdslLineSubCarAtucHlinPs": pdnAdslLineSubCarAtucHlinPs,
       "pdnAdslLineSubCarAturHlinPs": pdnAdslLineSubCarAturHlinPs,
       "pdnAdslLineSubCarAtucHlogMt": pdnAdslLineSubCarAtucHlogMt,
       "pdnAdslLineSubCarAturHlogMt": pdnAdslLineSubCarAturHlogMt,
       "pdnAdslLineSubCarAtucQlnPs": pdnAdslLineSubCarAtucQlnPs,
       "pdnAdslLineSubCarAturQlnPs": pdnAdslLineSubCarAturQlnPs,
       "pdnAdslLineSubCarAtucSnrPs": pdnAdslLineSubCarAtucSnrPs,
       "pdnAdslLineSubCarAturSnrPs": pdnAdslLineSubCarAturSnrPs,
       "pdnAdslLineSubCarAtucBitsPs": pdnAdslLineSubCarAtucBitsPs,
       "pdnAdslLineSubCarAturBitsPs": pdnAdslLineSubCarAturBitsPs,
       "pdnAdslLineSubCarAtucHlogPs": pdnAdslLineSubCarAtucHlogPs,
       "pdnAdslLineSubCarAturHlogPs": pdnAdslLineSubCarAturHlogPs,
       "pdnAdslLineExtAFNs": pdnAdslLineExtAFNs,
       "pdnAdslLineExtConformance": pdnAdslLineExtConformance,
       "pdnAdslLineExtCompliances": pdnAdslLineExtCompliances,
       "pdnAdslLineExtMIBCompliance": pdnAdslLineExtMIBCompliance,
       "pdnAdslLineExtGroups": pdnAdslLineExtGroups,
       "pdnAdslLineExtObjGroups": pdnAdslLineExtObjGroups,
       "pdnAdslLineExtGroup": pdnAdslLineExtGroup,
       "pdnAdslLineSpectrumGroup": pdnAdslLineSpectrumGroup,
       "pdnAdslModeSpecificPsdGroup": pdnAdslModeSpecificPsdGroup,
       "pdnAdslPsdGroup": pdnAdslPsdGroup,
       "pdnAdslCarMaskGroup": pdnAdslCarMaskGroup,
       "pdnAdslLineL2AtprtGroup": pdnAdslLineL2AtprtGroup,
       "pdnAdslLineStatusLineAtnGroup": pdnAdslLineStatusLineAtnGroup,
       "pdnAdslLineStatusSignalAtnGroup": pdnAdslLineStatusSignalAtnGroup,
       "pdnAdslLineStatusSnrMgnGroup": pdnAdslLineStatusSnrMgnGroup,
       "pdnAdslLineStatusMaxattainableLineRateGroup": pdnAdslLineStatusMaxattainableLineRateGroup,
       "pdnAdslLineStatusActAtpGroup": pdnAdslLineStatusActAtpGroup,
       "pdnAdslLineSubCarStatusHlinGroup": pdnAdslLineSubCarStatusHlinGroup,
       "pdnAdslLineSubCarStatusHlogMtGroup": pdnAdslLineSubCarStatusHlogMtGroup,
       "pdnAdslLineSubCarStatusQlnGroup": pdnAdslLineSubCarStatusQlnGroup,
       "pdnAdslLineSubCarStatusSnrGroup": pdnAdslLineSubCarStatusSnrGroup,
       "pdnAdslLineSubCarStatusBitsGroup": pdnAdslLineSubCarStatusBitsGroup,
       "pdnAdslLineSubCarStatusHlogGroup": pdnAdslLineSubCarStatusHlogGroup,
       "pdnAdslLineExtAfnGroups": pdnAdslLineExtAfnGroups,
       "pdnAdslLineExtNtfyGroups": pdnAdslLineExtNtfyGroups}
)
