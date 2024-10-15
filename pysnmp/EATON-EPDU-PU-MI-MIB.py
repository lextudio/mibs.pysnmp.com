# SNMP MIB module (EATON-EPDU-PU-MI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EATON-EPDU-PU-MI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:20 2024
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

pulizzi = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20677)
)
pulizzi.setRevisions(
        ("2010-02-03 12:00",
         "2009-01-08 12:00",
         "2008-12-19 12:00",
         "2008-11-06 12:00",
         "2008-08-25 12:00",
         "2008-07-09 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Monitoredepdu_ObjectIdentity = ObjectIdentity
monitoredepdu = _Monitoredepdu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 3)
)
_Epdum1_ObjectIdentity = ObjectIdentity
epdum1 = _Epdum1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1)
)
_Epdum11_ObjectIdentity = ObjectIdentity
epdum11 = _Epdum11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1)
)
_UnitConfig_ObjectIdentity = ObjectIdentity
unitConfig = _UnitConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 1)
)
_Uptime_Type = TimeTicks
_Uptime_Object = MibScalar
uptime = _Uptime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 1, 1),
    _Uptime_Type()
)
uptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uptime.setStatus("current")


class _UnitName_Type(OctetString):
    """Custom type unitName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_UnitName_Type.__name__ = "OctetString"
_UnitName_Object = MibScalar
unitName = _UnitName_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 1, 2),
    _UnitName_Type()
)
unitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitName.setStatus("current")
_LowCurrentThreshold1old_Type = Integer32
_LowCurrentThreshold1old_Object = MibScalar
lowCurrentThreshold1old = _LowCurrentThreshold1old_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 1, 3),
    _LowCurrentThreshold1old_Type()
)
lowCurrentThreshold1old.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold1old.setStatus("deprecated")
if mibBuilder.loadTexts:
    lowCurrentThreshold1old.setUnits("Amps")
_LowCurrentThreshold2old_Type = Integer32
_LowCurrentThreshold2old_Object = MibScalar
lowCurrentThreshold2old = _LowCurrentThreshold2old_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 1, 4),
    _LowCurrentThreshold2old_Type()
)
lowCurrentThreshold2old.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold2old.setStatus("deprecated")
if mibBuilder.loadTexts:
    lowCurrentThreshold2old.setUnits("Amps")
_LowCurrentThreshold3old_Type = Integer32
_LowCurrentThreshold3old_Object = MibScalar
lowCurrentThreshold3old = _LowCurrentThreshold3old_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 1, 5),
    _LowCurrentThreshold3old_Type()
)
lowCurrentThreshold3old.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold3old.setStatus("deprecated")
if mibBuilder.loadTexts:
    lowCurrentThreshold3old.setUnits("Amps")
_LowCurrentThreshold4old_Type = Integer32
_LowCurrentThreshold4old_Object = MibScalar
lowCurrentThreshold4old = _LowCurrentThreshold4old_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 1, 6),
    _LowCurrentThreshold4old_Type()
)
lowCurrentThreshold4old.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold4old.setStatus("deprecated")
if mibBuilder.loadTexts:
    lowCurrentThreshold4old.setUnits("Amps")
_LowCurrentThreshold5old_Type = Integer32
_LowCurrentThreshold5old_Object = MibScalar
lowCurrentThreshold5old = _LowCurrentThreshold5old_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 1, 7),
    _LowCurrentThreshold5old_Type()
)
lowCurrentThreshold5old.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold5old.setStatus("deprecated")
if mibBuilder.loadTexts:
    lowCurrentThreshold5old.setUnits("Amps")
_LowCurrentThreshold6old_Type = Integer32
_LowCurrentThreshold6old_Object = MibScalar
lowCurrentThreshold6old = _LowCurrentThreshold6old_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 1, 8),
    _LowCurrentThreshold6old_Type()
)
lowCurrentThreshold6old.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold6old.setStatus("deprecated")
if mibBuilder.loadTexts:
    lowCurrentThreshold6old.setUnits("Amps")
_LowCurrentThreshold7old_Type = Integer32
_LowCurrentThreshold7old_Object = MibScalar
lowCurrentThreshold7old = _LowCurrentThreshold7old_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 1, 9),
    _LowCurrentThreshold7old_Type()
)
lowCurrentThreshold7old.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold7old.setStatus("deprecated")
if mibBuilder.loadTexts:
    lowCurrentThreshold7old.setUnits("Amps or Degrees Farenheit")
_LowCurrentThreshold8old_Type = Integer32
_LowCurrentThreshold8old_Object = MibScalar
lowCurrentThreshold8old = _LowCurrentThreshold8old_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 1, 10),
    _LowCurrentThreshold8old_Type()
)
lowCurrentThreshold8old.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold8old.setStatus("deprecated")
if mibBuilder.loadTexts:
    lowCurrentThreshold8old.setUnits("Amps or Degrees Farenheit")
_HighCurrentThreshold1old_Type = Integer32
_HighCurrentThreshold1old_Object = MibScalar
highCurrentThreshold1old = _HighCurrentThreshold1old_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 1, 11),
    _HighCurrentThreshold1old_Type()
)
highCurrentThreshold1old.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold1old.setStatus("deprecated")
if mibBuilder.loadTexts:
    highCurrentThreshold1old.setUnits("Amps")
_HighCurrentThreshold2old_Type = Integer32
_HighCurrentThreshold2old_Object = MibScalar
highCurrentThreshold2old = _HighCurrentThreshold2old_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 1, 12),
    _HighCurrentThreshold2old_Type()
)
highCurrentThreshold2old.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold2old.setStatus("deprecated")
if mibBuilder.loadTexts:
    highCurrentThreshold2old.setUnits("Amps")
_HighCurrentThreshold3old_Type = Integer32
_HighCurrentThreshold3old_Object = MibScalar
highCurrentThreshold3old = _HighCurrentThreshold3old_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 1, 13),
    _HighCurrentThreshold3old_Type()
)
highCurrentThreshold3old.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold3old.setStatus("deprecated")
if mibBuilder.loadTexts:
    highCurrentThreshold3old.setUnits("Amps")
_HighCurrentThreshold4old_Type = Integer32
_HighCurrentThreshold4old_Object = MibScalar
highCurrentThreshold4old = _HighCurrentThreshold4old_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 1, 14),
    _HighCurrentThreshold4old_Type()
)
highCurrentThreshold4old.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold4old.setStatus("deprecated")
if mibBuilder.loadTexts:
    highCurrentThreshold4old.setUnits("Amps")
_HighCurrentThreshold5old_Type = Integer32
_HighCurrentThreshold5old_Object = MibScalar
highCurrentThreshold5old = _HighCurrentThreshold5old_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 1, 15),
    _HighCurrentThreshold5old_Type()
)
highCurrentThreshold5old.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold5old.setStatus("deprecated")
if mibBuilder.loadTexts:
    highCurrentThreshold5old.setUnits("Amps")
_HighCurrentThreshold6old_Type = Integer32
_HighCurrentThreshold6old_Object = MibScalar
highCurrentThreshold6old = _HighCurrentThreshold6old_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 1, 16),
    _HighCurrentThreshold6old_Type()
)
highCurrentThreshold6old.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold6old.setStatus("deprecated")
if mibBuilder.loadTexts:
    highCurrentThreshold6old.setUnits("Amps")
_HighCurrentThreshold7old_Type = Integer32
_HighCurrentThreshold7old_Object = MibScalar
highCurrentThreshold7old = _HighCurrentThreshold7old_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 1, 17),
    _HighCurrentThreshold7old_Type()
)
highCurrentThreshold7old.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold7old.setStatus("deprecated")
if mibBuilder.loadTexts:
    highCurrentThreshold7old.setUnits("Amps or Degrees Farenheit")
_HighCurrentThreshold8old_Type = Integer32
_HighCurrentThreshold8old_Object = MibScalar
highCurrentThreshold8old = _HighCurrentThreshold8old_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 1, 18),
    _HighCurrentThreshold8old_Type()
)
highCurrentThreshold8old.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold8old.setStatus("deprecated")
if mibBuilder.loadTexts:
    highCurrentThreshold8old.setUnits("Amps or Degrees Farenheit")


class _Temperature1Enable_Type(Integer32):
    """Custom type temperature1Enable based on Integer32"""
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


_Temperature1Enable_Type.__name__ = "Integer32"
_Temperature1Enable_Object = MibScalar
temperature1Enable = _Temperature1Enable_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 1, 19),
    _Temperature1Enable_Type()
)
temperature1Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperature1Enable.setStatus("current")


class _Temperature2Enable_Type(Integer32):
    """Custom type temperature2Enable based on Integer32"""
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


_Temperature2Enable_Type.__name__ = "Integer32"
_Temperature2Enable_Object = MibScalar
temperature2Enable = _Temperature2Enable_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 1, 20),
    _Temperature2Enable_Type()
)
temperature2Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperature2Enable.setStatus("current")
_FirmwareRevision_Type = OctetString
_FirmwareRevision_Object = MibScalar
firmwareRevision = _FirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 1, 21),
    _FirmwareRevision_Type()
)
firmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareRevision.setStatus("current")


class _AssetID_Type(OctetString):
    """Custom type assetID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_AssetID_Type.__name__ = "OctetString"
_AssetID_Object = MibScalar
assetID = _AssetID_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 1, 22),
    _AssetID_Type()
)
assetID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    assetID.setStatus("current")
_NumCurrentChannels_Type = Integer32
_NumCurrentChannels_Object = MibScalar
numCurrentChannels = _NumCurrentChannels_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 1, 23),
    _NumCurrentChannels_Type()
)
numCurrentChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numCurrentChannels.setStatus("current")


class _CurrentMonitorType_Type(Integer32):
    """Custom type currentMonitorType based on Integer32"""
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
        *(("branchCurrent", 2),
          ("outletCurrent", 3),
          ("singlePhaseWithBranch", 6),
          ("splitPhaseCurrent", 5),
          ("splitPhaseWithBranch", 8),
          ("threePhaseCurrent", 4),
          ("threePhaseWithBranch", 7),
          ("totalUnitCurrent", 1))
    )


_CurrentMonitorType_Type.__name__ = "Integer32"
_CurrentMonitorType_Object = MibScalar
currentMonitorType = _CurrentMonitorType_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 1, 24),
    _CurrentMonitorType_Type()
)
currentMonitorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMonitorType.setStatus("current")
_NetworkSettings_ObjectIdentity = ObjectIdentity
networkSettings = _NetworkSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 2)
)
_UnitIPAddress_Type = IpAddress
_UnitIPAddress_Object = MibScalar
unitIPAddress = _UnitIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 2, 1),
    _UnitIPAddress_Type()
)
unitIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitIPAddress.setStatus("current")
_UnitSubnetMask_Type = IpAddress
_UnitSubnetMask_Object = MibScalar
unitSubnetMask = _UnitSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 2, 2),
    _UnitSubnetMask_Type()
)
unitSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitSubnetMask.setStatus("current")
_UnitGateway_Type = IpAddress
_UnitGateway_Object = MibScalar
unitGateway = _UnitGateway_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 2, 3),
    _UnitGateway_Type()
)
unitGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitGateway.setStatus("current")
_UnitMACAddress_Type = OctetString
_UnitMACAddress_Object = MibScalar
unitMACAddress = _UnitMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 2, 4),
    _UnitMACAddress_Type()
)
unitMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitMACAddress.setStatus("current")
_TrapDestIP_Type = IpAddress
_TrapDestIP_Object = MibScalar
trapDestIP = _TrapDestIP_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 2, 5),
    _TrapDestIP_Type()
)
trapDestIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDestIP.setStatus("current")
_MailServerIP_Type = IpAddress
_MailServerIP_Object = MibScalar
mailServerIP = _MailServerIP_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 2, 6),
    _MailServerIP_Type()
)
mailServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailServerIP.setStatus("current")


class _AlertEmailAddress_Type(OctetString):
    """Custom type alertEmailAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 49),
    )


_AlertEmailAddress_Type.__name__ = "OctetString"
_AlertEmailAddress_Object = MibScalar
alertEmailAddress = _AlertEmailAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 2, 7),
    _AlertEmailAddress_Type()
)
alertEmailAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertEmailAddress.setStatus("current")
_Measurements_ObjectIdentity = ObjectIdentity
measurements = _Measurements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 3)
)
_Chan1_Type = Integer32
_Chan1_Object = MibScalar
chan1 = _Chan1_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 3, 1),
    _Chan1_Type()
)
chan1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan1.setStatus("current")
if mibBuilder.loadTexts:
    chan1.setUnits("0.1 Amps RMS")
_Chan2_Type = Integer32
_Chan2_Object = MibScalar
chan2 = _Chan2_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 3, 2),
    _Chan2_Type()
)
chan2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan2.setStatus("current")
if mibBuilder.loadTexts:
    chan2.setUnits("0.1 Amps RMS")
_Chan3_Type = Integer32
_Chan3_Object = MibScalar
chan3 = _Chan3_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 3, 3),
    _Chan3_Type()
)
chan3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan3.setStatus("current")
if mibBuilder.loadTexts:
    chan3.setUnits("0.1 Amps RMS")
_Chan4_Type = Integer32
_Chan4_Object = MibScalar
chan4 = _Chan4_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 3, 4),
    _Chan4_Type()
)
chan4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan4.setStatus("current")
if mibBuilder.loadTexts:
    chan4.setUnits("0.1 Amps RMS")
_Chan5_Type = Integer32
_Chan5_Object = MibScalar
chan5 = _Chan5_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 3, 5),
    _Chan5_Type()
)
chan5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan5.setStatus("current")
if mibBuilder.loadTexts:
    chan5.setUnits("0.1 Amps RMS")
_Chan6_Type = Integer32
_Chan6_Object = MibScalar
chan6 = _Chan6_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 3, 6),
    _Chan6_Type()
)
chan6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan6.setStatus("current")
if mibBuilder.loadTexts:
    chan6.setUnits("0.1 Amps RMS")
_Chan7_Type = Integer32
_Chan7_Object = MibScalar
chan7 = _Chan7_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 3, 7),
    _Chan7_Type()
)
chan7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan7.setStatus("current")
if mibBuilder.loadTexts:
    chan7.setUnits("0.1 Amps RMS")
_Chan8_Type = Integer32
_Chan8_Object = MibScalar
chan8 = _Chan8_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 3, 8),
    _Chan8_Type()
)
chan8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan8.setStatus("current")
if mibBuilder.loadTexts:
    chan8.setUnits("0.1 Amps RMS")
_Chan9_Type = Integer32
_Chan9_Object = MibScalar
chan9 = _Chan9_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 3, 9),
    _Chan9_Type()
)
chan9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan9.setStatus("current")
if mibBuilder.loadTexts:
    chan9.setUnits("0.1 Amps RMS")
_Chan10_Type = Integer32
_Chan10_Object = MibScalar
chan10 = _Chan10_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 3, 10),
    _Chan10_Type()
)
chan10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan10.setStatus("current")
if mibBuilder.loadTexts:
    chan10.setUnits("0.1 Amps RMS")
_Chan11_Type = Integer32
_Chan11_Object = MibScalar
chan11 = _Chan11_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 3, 11),
    _Chan11_Type()
)
chan11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan11.setStatus("current")
if mibBuilder.loadTexts:
    chan11.setUnits("0.1 Amps RMS")
_Chan12_Type = Integer32
_Chan12_Object = MibScalar
chan12 = _Chan12_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 3, 12),
    _Chan12_Type()
)
chan12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan12.setStatus("current")
if mibBuilder.loadTexts:
    chan12.setUnits("0.1 Amps RMS")
_Chan13_Type = Integer32
_Chan13_Object = MibScalar
chan13 = _Chan13_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 3, 13),
    _Chan13_Type()
)
chan13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan13.setStatus("current")
if mibBuilder.loadTexts:
    chan13.setUnits("0.1 Amps RMS")
_Chan14_Type = Integer32
_Chan14_Object = MibScalar
chan14 = _Chan14_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 3, 14),
    _Chan14_Type()
)
chan14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan14.setStatus("current")
if mibBuilder.loadTexts:
    chan14.setUnits("0.1 Amps RMS")
_Chan15_Type = Integer32
_Chan15_Object = MibScalar
chan15 = _Chan15_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 3, 15),
    _Chan15_Type()
)
chan15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan15.setStatus("current")
if mibBuilder.loadTexts:
    chan15.setUnits("0.1 Amps RMS")
_Chan16_Type = Integer32
_Chan16_Object = MibScalar
chan16 = _Chan16_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 3, 16),
    _Chan16_Type()
)
chan16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan16.setStatus("current")
if mibBuilder.loadTexts:
    chan16.setUnits("0.1 Amps RMS")
_Chan17_Type = Integer32
_Chan17_Object = MibScalar
chan17 = _Chan17_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 3, 17),
    _Chan17_Type()
)
chan17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan17.setStatus("current")
if mibBuilder.loadTexts:
    chan17.setUnits("0.1 Amps RMS")
_Chan18_Type = Integer32
_Chan18_Object = MibScalar
chan18 = _Chan18_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 3, 18),
    _Chan18_Type()
)
chan18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan18.setStatus("current")
if mibBuilder.loadTexts:
    chan18.setUnits("0.1 Amps RMS")
_Chan19_Type = Integer32
_Chan19_Object = MibScalar
chan19 = _Chan19_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 3, 19),
    _Chan19_Type()
)
chan19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan19.setStatus("current")
if mibBuilder.loadTexts:
    chan19.setUnits("0.1 Amps RMS")
_Chan20_Type = Integer32
_Chan20_Object = MibScalar
chan20 = _Chan20_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 3, 20),
    _Chan20_Type()
)
chan20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan20.setStatus("current")
if mibBuilder.loadTexts:
    chan20.setUnits("0.1 Amps RMS")
_Chan21_Type = Integer32
_Chan21_Object = MibScalar
chan21 = _Chan21_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 3, 21),
    _Chan21_Type()
)
chan21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan21.setStatus("current")
if mibBuilder.loadTexts:
    chan21.setUnits("0.1 Amps RMS")
_Chan22_Type = Integer32
_Chan22_Object = MibScalar
chan22 = _Chan22_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 3, 22),
    _Chan22_Type()
)
chan22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan22.setStatus("current")
if mibBuilder.loadTexts:
    chan22.setUnits("0.1 Amps RMS")
_Chan23_Type = Integer32
_Chan23_Object = MibScalar
chan23 = _Chan23_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 3, 23),
    _Chan23_Type()
)
chan23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan23.setStatus("current")
if mibBuilder.loadTexts:
    chan23.setUnits("0.1 Amps RMS")
_Chan24_Type = Integer32
_Chan24_Object = MibScalar
chan24 = _Chan24_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 3, 24),
    _Chan24_Type()
)
chan24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan24.setStatus("current")
if mibBuilder.loadTexts:
    chan24.setUnits("0.1 Amps RMS")
_Chan25_Type = Integer32
_Chan25_Object = MibScalar
chan25 = _Chan25_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 3, 25),
    _Chan25_Type()
)
chan25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan25.setStatus("current")
if mibBuilder.loadTexts:
    chan25.setUnits("0.1 Amps RMS")
_Chan26_Type = Integer32
_Chan26_Object = MibScalar
chan26 = _Chan26_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 3, 26),
    _Chan26_Type()
)
chan26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan26.setStatus("current")
if mibBuilder.loadTexts:
    chan26.setUnits("0.1 Amps RMS")
_Chan27_Type = Integer32
_Chan27_Object = MibScalar
chan27 = _Chan27_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 3, 27),
    _Chan27_Type()
)
chan27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan27.setStatus("current")
if mibBuilder.loadTexts:
    chan27.setUnits("0.1 Amps RMS")
_Chan28_Type = Integer32
_Chan28_Object = MibScalar
chan28 = _Chan28_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 3, 28),
    _Chan28_Type()
)
chan28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan28.setStatus("current")
if mibBuilder.loadTexts:
    chan28.setUnits("0.1 Amps RMS")
_Chan29_Type = Integer32
_Chan29_Object = MibScalar
chan29 = _Chan29_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 3, 29),
    _Chan29_Type()
)
chan29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan29.setStatus("current")
if mibBuilder.loadTexts:
    chan29.setUnits("0.1 Amps RMS")
_Chan30_Type = Integer32
_Chan30_Object = MibScalar
chan30 = _Chan30_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 3, 30),
    _Chan30_Type()
)
chan30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan30.setStatus("current")
if mibBuilder.loadTexts:
    chan30.setUnits("0.1 Amps RMS")
_Chan31_Type = Integer32
_Chan31_Object = MibScalar
chan31 = _Chan31_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 3, 31),
    _Chan31_Type()
)
chan31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan31.setStatus("current")
if mibBuilder.loadTexts:
    chan31.setUnits("0.1 Amps RMS")
_Chan32_Type = Integer32
_Chan32_Object = MibScalar
chan32 = _Chan32_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 3, 32),
    _Chan32_Type()
)
chan32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan32.setStatus("current")
if mibBuilder.loadTexts:
    chan32.setUnits("0.1 Amps RMS")
_TempChan1_Type = Integer32
_TempChan1_Object = MibScalar
tempChan1 = _TempChan1_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 3, 248),
    _TempChan1_Type()
)
tempChan1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempChan1.setStatus("current")
if mibBuilder.loadTexts:
    tempChan1.setUnits("Degrees Fahrenheit")
_TempChan2_Type = Integer32
_TempChan2_Object = MibScalar
tempChan2 = _TempChan2_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 3, 249),
    _TempChan2_Type()
)
tempChan2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempChan2.setStatus("current")
if mibBuilder.loadTexts:
    tempChan2.setUnits("Degrees Fahrenheit")
_ChanNames_ObjectIdentity = ObjectIdentity
chanNames = _ChanNames_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 4)
)


class _Chan1Name_Type(OctetString):
    """Custom type chan1Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Chan1Name_Type.__name__ = "OctetString"
_Chan1Name_Object = MibScalar
chan1Name = _Chan1Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 4, 1),
    _Chan1Name_Type()
)
chan1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chan1Name.setStatus("current")


class _Chan2Name_Type(OctetString):
    """Custom type chan2Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Chan2Name_Type.__name__ = "OctetString"
_Chan2Name_Object = MibScalar
chan2Name = _Chan2Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 4, 2),
    _Chan2Name_Type()
)
chan2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chan2Name.setStatus("current")


class _Chan3Name_Type(OctetString):
    """Custom type chan3Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Chan3Name_Type.__name__ = "OctetString"
_Chan3Name_Object = MibScalar
chan3Name = _Chan3Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 4, 3),
    _Chan3Name_Type()
)
chan3Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chan3Name.setStatus("current")


class _Chan4Name_Type(OctetString):
    """Custom type chan4Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Chan4Name_Type.__name__ = "OctetString"
_Chan4Name_Object = MibScalar
chan4Name = _Chan4Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 4, 4),
    _Chan4Name_Type()
)
chan4Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chan4Name.setStatus("current")


class _Chan5Name_Type(OctetString):
    """Custom type chan5Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Chan5Name_Type.__name__ = "OctetString"
_Chan5Name_Object = MibScalar
chan5Name = _Chan5Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 4, 5),
    _Chan5Name_Type()
)
chan5Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chan5Name.setStatus("current")


class _Chan6Name_Type(OctetString):
    """Custom type chan6Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Chan6Name_Type.__name__ = "OctetString"
_Chan6Name_Object = MibScalar
chan6Name = _Chan6Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 4, 6),
    _Chan6Name_Type()
)
chan6Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chan6Name.setStatus("current")


class _Chan7Name_Type(OctetString):
    """Custom type chan7Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Chan7Name_Type.__name__ = "OctetString"
_Chan7Name_Object = MibScalar
chan7Name = _Chan7Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 4, 7),
    _Chan7Name_Type()
)
chan7Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chan7Name.setStatus("current")


class _Chan8Name_Type(OctetString):
    """Custom type chan8Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Chan8Name_Type.__name__ = "OctetString"
_Chan8Name_Object = MibScalar
chan8Name = _Chan8Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 4, 8),
    _Chan8Name_Type()
)
chan8Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chan8Name.setStatus("current")


class _Chan9Name_Type(OctetString):
    """Custom type chan9Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Chan9Name_Type.__name__ = "OctetString"
_Chan9Name_Object = MibScalar
chan9Name = _Chan9Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 4, 9),
    _Chan9Name_Type()
)
chan9Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chan9Name.setStatus("current")


class _Chan10Name_Type(OctetString):
    """Custom type chan10Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Chan10Name_Type.__name__ = "OctetString"
_Chan10Name_Object = MibScalar
chan10Name = _Chan10Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 4, 10),
    _Chan10Name_Type()
)
chan10Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chan10Name.setStatus("current")


class _Chan11Name_Type(OctetString):
    """Custom type chan11Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Chan11Name_Type.__name__ = "OctetString"
_Chan11Name_Object = MibScalar
chan11Name = _Chan11Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 4, 11),
    _Chan11Name_Type()
)
chan11Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chan11Name.setStatus("current")


class _Chan12Name_Type(OctetString):
    """Custom type chan12Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Chan12Name_Type.__name__ = "OctetString"
_Chan12Name_Object = MibScalar
chan12Name = _Chan12Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 4, 12),
    _Chan12Name_Type()
)
chan12Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chan12Name.setStatus("current")


class _Chan13Name_Type(OctetString):
    """Custom type chan13Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Chan13Name_Type.__name__ = "OctetString"
_Chan13Name_Object = MibScalar
chan13Name = _Chan13Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 4, 13),
    _Chan13Name_Type()
)
chan13Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chan13Name.setStatus("current")


class _Chan14Name_Type(OctetString):
    """Custom type chan14Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Chan14Name_Type.__name__ = "OctetString"
_Chan14Name_Object = MibScalar
chan14Name = _Chan14Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 4, 14),
    _Chan14Name_Type()
)
chan14Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chan14Name.setStatus("current")


class _Chan15Name_Type(OctetString):
    """Custom type chan15Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Chan15Name_Type.__name__ = "OctetString"
_Chan15Name_Object = MibScalar
chan15Name = _Chan15Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 4, 15),
    _Chan15Name_Type()
)
chan15Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chan15Name.setStatus("current")


class _Chan16Name_Type(OctetString):
    """Custom type chan16Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Chan16Name_Type.__name__ = "OctetString"
_Chan16Name_Object = MibScalar
chan16Name = _Chan16Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 4, 16),
    _Chan16Name_Type()
)
chan16Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chan16Name.setStatus("current")


class _Chan17Name_Type(OctetString):
    """Custom type chan17Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Chan17Name_Type.__name__ = "OctetString"
_Chan17Name_Object = MibScalar
chan17Name = _Chan17Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 4, 17),
    _Chan17Name_Type()
)
chan17Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chan17Name.setStatus("current")


class _Chan18Name_Type(OctetString):
    """Custom type chan18Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Chan18Name_Type.__name__ = "OctetString"
_Chan18Name_Object = MibScalar
chan18Name = _Chan18Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 4, 18),
    _Chan18Name_Type()
)
chan18Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chan18Name.setStatus("current")


class _Chan19Name_Type(OctetString):
    """Custom type chan19Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Chan19Name_Type.__name__ = "OctetString"
_Chan19Name_Object = MibScalar
chan19Name = _Chan19Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 4, 19),
    _Chan19Name_Type()
)
chan19Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chan19Name.setStatus("current")


class _Chan20Name_Type(OctetString):
    """Custom type chan20Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Chan20Name_Type.__name__ = "OctetString"
_Chan20Name_Object = MibScalar
chan20Name = _Chan20Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 4, 20),
    _Chan20Name_Type()
)
chan20Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chan20Name.setStatus("current")


class _Chan21Name_Type(OctetString):
    """Custom type chan21Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Chan21Name_Type.__name__ = "OctetString"
_Chan21Name_Object = MibScalar
chan21Name = _Chan21Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 4, 21),
    _Chan21Name_Type()
)
chan21Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chan21Name.setStatus("current")


class _Chan22Name_Type(OctetString):
    """Custom type chan22Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Chan22Name_Type.__name__ = "OctetString"
_Chan22Name_Object = MibScalar
chan22Name = _Chan22Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 4, 22),
    _Chan22Name_Type()
)
chan22Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chan22Name.setStatus("current")


class _Chan23Name_Type(OctetString):
    """Custom type chan23Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Chan23Name_Type.__name__ = "OctetString"
_Chan23Name_Object = MibScalar
chan23Name = _Chan23Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 4, 23),
    _Chan23Name_Type()
)
chan23Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chan23Name.setStatus("current")


class _Chan24Name_Type(OctetString):
    """Custom type chan24Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Chan24Name_Type.__name__ = "OctetString"
_Chan24Name_Object = MibScalar
chan24Name = _Chan24Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 4, 24),
    _Chan24Name_Type()
)
chan24Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chan24Name.setStatus("current")


class _Chan25Name_Type(OctetString):
    """Custom type chan25Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Chan25Name_Type.__name__ = "OctetString"
_Chan25Name_Object = MibScalar
chan25Name = _Chan25Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 4, 25),
    _Chan25Name_Type()
)
chan25Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chan25Name.setStatus("current")


class _Chan26Name_Type(OctetString):
    """Custom type chan26Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Chan26Name_Type.__name__ = "OctetString"
_Chan26Name_Object = MibScalar
chan26Name = _Chan26Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 4, 26),
    _Chan26Name_Type()
)
chan26Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chan26Name.setStatus("current")


class _Chan27Name_Type(OctetString):
    """Custom type chan27Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Chan27Name_Type.__name__ = "OctetString"
_Chan27Name_Object = MibScalar
chan27Name = _Chan27Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 4, 27),
    _Chan27Name_Type()
)
chan27Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chan27Name.setStatus("current")


class _Chan28Name_Type(OctetString):
    """Custom type chan28Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Chan28Name_Type.__name__ = "OctetString"
_Chan28Name_Object = MibScalar
chan28Name = _Chan28Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 4, 28),
    _Chan28Name_Type()
)
chan28Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chan28Name.setStatus("current")


class _Chan29Name_Type(OctetString):
    """Custom type chan29Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Chan29Name_Type.__name__ = "OctetString"
_Chan29Name_Object = MibScalar
chan29Name = _Chan29Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 4, 29),
    _Chan29Name_Type()
)
chan29Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chan29Name.setStatus("current")


class _Chan30Name_Type(OctetString):
    """Custom type chan30Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Chan30Name_Type.__name__ = "OctetString"
_Chan30Name_Object = MibScalar
chan30Name = _Chan30Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 4, 30),
    _Chan30Name_Type()
)
chan30Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chan30Name.setStatus("current")


class _Chan31Name_Type(OctetString):
    """Custom type chan31Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Chan31Name_Type.__name__ = "OctetString"
_Chan31Name_Object = MibScalar
chan31Name = _Chan31Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 4, 31),
    _Chan31Name_Type()
)
chan31Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chan31Name.setStatus("current")


class _Chan32Name_Type(OctetString):
    """Custom type chan32Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Chan32Name_Type.__name__ = "OctetString"
_Chan32Name_Object = MibScalar
chan32Name = _Chan32Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 4, 32),
    _Chan32Name_Type()
)
chan32Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chan32Name.setStatus("current")


class _Temp1Name_Type(OctetString):
    """Custom type temp1Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Temp1Name_Type.__name__ = "OctetString"
_Temp1Name_Object = MibScalar
temp1Name = _Temp1Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 4, 248),
    _Temp1Name_Type()
)
temp1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temp1Name.setStatus("current")


class _Temp2Name_Type(OctetString):
    """Custom type temp2Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Temp2Name_Type.__name__ = "OctetString"
_Temp2Name_Object = MibScalar
temp2Name = _Temp2Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 4, 249),
    _Temp2Name_Type()
)
temp2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temp2Name.setStatus("current")
_LowCurrentThresh_ObjectIdentity = ObjectIdentity
lowCurrentThresh = _LowCurrentThresh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 5)
)


class _LowCurrentThreshold1_Type(Integer32):
    """Custom type lowCurrentThreshold1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LowCurrentThreshold1_Type.__name__ = "Integer32"
_LowCurrentThreshold1_Object = MibScalar
lowCurrentThreshold1 = _LowCurrentThreshold1_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 5, 1),
    _LowCurrentThreshold1_Type()
)
lowCurrentThreshold1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold1.setStatus("current")
if mibBuilder.loadTexts:
    lowCurrentThreshold1.setUnits("Amps")


class _LowCurrentThreshold2_Type(Integer32):
    """Custom type lowCurrentThreshold2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LowCurrentThreshold2_Type.__name__ = "Integer32"
_LowCurrentThreshold2_Object = MibScalar
lowCurrentThreshold2 = _LowCurrentThreshold2_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 5, 2),
    _LowCurrentThreshold2_Type()
)
lowCurrentThreshold2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold2.setStatus("current")
if mibBuilder.loadTexts:
    lowCurrentThreshold2.setUnits("Amps")


class _LowCurrentThreshold3_Type(Integer32):
    """Custom type lowCurrentThreshold3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LowCurrentThreshold3_Type.__name__ = "Integer32"
_LowCurrentThreshold3_Object = MibScalar
lowCurrentThreshold3 = _LowCurrentThreshold3_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 5, 3),
    _LowCurrentThreshold3_Type()
)
lowCurrentThreshold3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold3.setStatus("current")
if mibBuilder.loadTexts:
    lowCurrentThreshold3.setUnits("Amps")


class _LowCurrentThreshold4_Type(Integer32):
    """Custom type lowCurrentThreshold4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LowCurrentThreshold4_Type.__name__ = "Integer32"
_LowCurrentThreshold4_Object = MibScalar
lowCurrentThreshold4 = _LowCurrentThreshold4_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 5, 4),
    _LowCurrentThreshold4_Type()
)
lowCurrentThreshold4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold4.setStatus("current")
if mibBuilder.loadTexts:
    lowCurrentThreshold4.setUnits("Amps")


class _LowCurrentThreshold5_Type(Integer32):
    """Custom type lowCurrentThreshold5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LowCurrentThreshold5_Type.__name__ = "Integer32"
_LowCurrentThreshold5_Object = MibScalar
lowCurrentThreshold5 = _LowCurrentThreshold5_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 5, 5),
    _LowCurrentThreshold5_Type()
)
lowCurrentThreshold5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold5.setStatus("current")
if mibBuilder.loadTexts:
    lowCurrentThreshold5.setUnits("Amps")


class _LowCurrentThreshold6_Type(Integer32):
    """Custom type lowCurrentThreshold6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LowCurrentThreshold6_Type.__name__ = "Integer32"
_LowCurrentThreshold6_Object = MibScalar
lowCurrentThreshold6 = _LowCurrentThreshold6_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 5, 6),
    _LowCurrentThreshold6_Type()
)
lowCurrentThreshold6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold6.setStatus("current")
if mibBuilder.loadTexts:
    lowCurrentThreshold6.setUnits("Amps")


class _LowCurrentThreshold7_Type(Integer32):
    """Custom type lowCurrentThreshold7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LowCurrentThreshold7_Type.__name__ = "Integer32"
_LowCurrentThreshold7_Object = MibScalar
lowCurrentThreshold7 = _LowCurrentThreshold7_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 5, 7),
    _LowCurrentThreshold7_Type()
)
lowCurrentThreshold7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold7.setStatus("current")
if mibBuilder.loadTexts:
    lowCurrentThreshold7.setUnits("Amps")


class _LowCurrentThreshold8_Type(Integer32):
    """Custom type lowCurrentThreshold8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LowCurrentThreshold8_Type.__name__ = "Integer32"
_LowCurrentThreshold8_Object = MibScalar
lowCurrentThreshold8 = _LowCurrentThreshold8_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 5, 8),
    _LowCurrentThreshold8_Type()
)
lowCurrentThreshold8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold8.setStatus("current")
if mibBuilder.loadTexts:
    lowCurrentThreshold8.setUnits("Amps")


class _LowCurrentThreshold9_Type(Integer32):
    """Custom type lowCurrentThreshold9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LowCurrentThreshold9_Type.__name__ = "Integer32"
_LowCurrentThreshold9_Object = MibScalar
lowCurrentThreshold9 = _LowCurrentThreshold9_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 5, 9),
    _LowCurrentThreshold9_Type()
)
lowCurrentThreshold9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold9.setStatus("current")
if mibBuilder.loadTexts:
    lowCurrentThreshold9.setUnits("Amps")


class _LowCurrentThreshold10_Type(Integer32):
    """Custom type lowCurrentThreshold10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LowCurrentThreshold10_Type.__name__ = "Integer32"
_LowCurrentThreshold10_Object = MibScalar
lowCurrentThreshold10 = _LowCurrentThreshold10_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 5, 10),
    _LowCurrentThreshold10_Type()
)
lowCurrentThreshold10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold10.setStatus("current")
if mibBuilder.loadTexts:
    lowCurrentThreshold10.setUnits("Amps")


class _LowCurrentThreshold11_Type(Integer32):
    """Custom type lowCurrentThreshold11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LowCurrentThreshold11_Type.__name__ = "Integer32"
_LowCurrentThreshold11_Object = MibScalar
lowCurrentThreshold11 = _LowCurrentThreshold11_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 5, 11),
    _LowCurrentThreshold11_Type()
)
lowCurrentThreshold11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold11.setStatus("current")
if mibBuilder.loadTexts:
    lowCurrentThreshold11.setUnits("Amps")


class _LowCurrentThreshold12_Type(Integer32):
    """Custom type lowCurrentThreshold12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LowCurrentThreshold12_Type.__name__ = "Integer32"
_LowCurrentThreshold12_Object = MibScalar
lowCurrentThreshold12 = _LowCurrentThreshold12_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 5, 12),
    _LowCurrentThreshold12_Type()
)
lowCurrentThreshold12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold12.setStatus("current")
if mibBuilder.loadTexts:
    lowCurrentThreshold12.setUnits("Amps")


class _LowCurrentThreshold13_Type(Integer32):
    """Custom type lowCurrentThreshold13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LowCurrentThreshold13_Type.__name__ = "Integer32"
_LowCurrentThreshold13_Object = MibScalar
lowCurrentThreshold13 = _LowCurrentThreshold13_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 5, 13),
    _LowCurrentThreshold13_Type()
)
lowCurrentThreshold13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold13.setStatus("current")
if mibBuilder.loadTexts:
    lowCurrentThreshold13.setUnits("Amps")


class _LowCurrentThreshold14_Type(Integer32):
    """Custom type lowCurrentThreshold14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LowCurrentThreshold14_Type.__name__ = "Integer32"
_LowCurrentThreshold14_Object = MibScalar
lowCurrentThreshold14 = _LowCurrentThreshold14_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 5, 14),
    _LowCurrentThreshold14_Type()
)
lowCurrentThreshold14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold14.setStatus("current")
if mibBuilder.loadTexts:
    lowCurrentThreshold14.setUnits("Amps")


class _LowCurrentThreshold15_Type(Integer32):
    """Custom type lowCurrentThreshold15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LowCurrentThreshold15_Type.__name__ = "Integer32"
_LowCurrentThreshold15_Object = MibScalar
lowCurrentThreshold15 = _LowCurrentThreshold15_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 5, 15),
    _LowCurrentThreshold15_Type()
)
lowCurrentThreshold15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold15.setStatus("current")
if mibBuilder.loadTexts:
    lowCurrentThreshold15.setUnits("Amps")


class _LowCurrentThreshold16_Type(Integer32):
    """Custom type lowCurrentThreshold16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LowCurrentThreshold16_Type.__name__ = "Integer32"
_LowCurrentThreshold16_Object = MibScalar
lowCurrentThreshold16 = _LowCurrentThreshold16_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 5, 16),
    _LowCurrentThreshold16_Type()
)
lowCurrentThreshold16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold16.setStatus("current")
if mibBuilder.loadTexts:
    lowCurrentThreshold16.setUnits("Amps")


class _LowCurrentThreshold17_Type(Integer32):
    """Custom type lowCurrentThreshold17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LowCurrentThreshold17_Type.__name__ = "Integer32"
_LowCurrentThreshold17_Object = MibScalar
lowCurrentThreshold17 = _LowCurrentThreshold17_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 5, 17),
    _LowCurrentThreshold17_Type()
)
lowCurrentThreshold17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold17.setStatus("current")
if mibBuilder.loadTexts:
    lowCurrentThreshold17.setUnits("Amps")


class _LowCurrentThreshold18_Type(Integer32):
    """Custom type lowCurrentThreshold18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LowCurrentThreshold18_Type.__name__ = "Integer32"
_LowCurrentThreshold18_Object = MibScalar
lowCurrentThreshold18 = _LowCurrentThreshold18_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 5, 18),
    _LowCurrentThreshold18_Type()
)
lowCurrentThreshold18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold18.setStatus("current")
if mibBuilder.loadTexts:
    lowCurrentThreshold18.setUnits("Amps")


class _LowCurrentThreshold19_Type(Integer32):
    """Custom type lowCurrentThreshold19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LowCurrentThreshold19_Type.__name__ = "Integer32"
_LowCurrentThreshold19_Object = MibScalar
lowCurrentThreshold19 = _LowCurrentThreshold19_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 5, 19),
    _LowCurrentThreshold19_Type()
)
lowCurrentThreshold19.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold19.setStatus("current")
if mibBuilder.loadTexts:
    lowCurrentThreshold19.setUnits("Amps")


class _LowCurrentThreshold20_Type(Integer32):
    """Custom type lowCurrentThreshold20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LowCurrentThreshold20_Type.__name__ = "Integer32"
_LowCurrentThreshold20_Object = MibScalar
lowCurrentThreshold20 = _LowCurrentThreshold20_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 5, 20),
    _LowCurrentThreshold20_Type()
)
lowCurrentThreshold20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold20.setStatus("current")
if mibBuilder.loadTexts:
    lowCurrentThreshold20.setUnits("Amps")


class _LowCurrentThreshold21_Type(Integer32):
    """Custom type lowCurrentThreshold21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LowCurrentThreshold21_Type.__name__ = "Integer32"
_LowCurrentThreshold21_Object = MibScalar
lowCurrentThreshold21 = _LowCurrentThreshold21_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 5, 21),
    _LowCurrentThreshold21_Type()
)
lowCurrentThreshold21.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold21.setStatus("current")
if mibBuilder.loadTexts:
    lowCurrentThreshold21.setUnits("Amps")


class _LowCurrentThreshold22_Type(Integer32):
    """Custom type lowCurrentThreshold22 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LowCurrentThreshold22_Type.__name__ = "Integer32"
_LowCurrentThreshold22_Object = MibScalar
lowCurrentThreshold22 = _LowCurrentThreshold22_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 5, 22),
    _LowCurrentThreshold22_Type()
)
lowCurrentThreshold22.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold22.setStatus("current")
if mibBuilder.loadTexts:
    lowCurrentThreshold22.setUnits("Amps")


class _LowCurrentThreshold23_Type(Integer32):
    """Custom type lowCurrentThreshold23 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LowCurrentThreshold23_Type.__name__ = "Integer32"
_LowCurrentThreshold23_Object = MibScalar
lowCurrentThreshold23 = _LowCurrentThreshold23_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 5, 23),
    _LowCurrentThreshold23_Type()
)
lowCurrentThreshold23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold23.setStatus("current")
if mibBuilder.loadTexts:
    lowCurrentThreshold23.setUnits("Amps")


class _LowCurrentThreshold24_Type(Integer32):
    """Custom type lowCurrentThreshold24 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LowCurrentThreshold24_Type.__name__ = "Integer32"
_LowCurrentThreshold24_Object = MibScalar
lowCurrentThreshold24 = _LowCurrentThreshold24_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 5, 24),
    _LowCurrentThreshold24_Type()
)
lowCurrentThreshold24.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold24.setStatus("current")
if mibBuilder.loadTexts:
    lowCurrentThreshold24.setUnits("Amps")


class _LowCurrentThreshold25_Type(Integer32):
    """Custom type lowCurrentThreshold25 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LowCurrentThreshold25_Type.__name__ = "Integer32"
_LowCurrentThreshold25_Object = MibScalar
lowCurrentThreshold25 = _LowCurrentThreshold25_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 5, 25),
    _LowCurrentThreshold25_Type()
)
lowCurrentThreshold25.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold25.setStatus("current")
if mibBuilder.loadTexts:
    lowCurrentThreshold25.setUnits("Amps")


class _LowCurrentThreshold26_Type(Integer32):
    """Custom type lowCurrentThreshold26 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LowCurrentThreshold26_Type.__name__ = "Integer32"
_LowCurrentThreshold26_Object = MibScalar
lowCurrentThreshold26 = _LowCurrentThreshold26_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 5, 26),
    _LowCurrentThreshold26_Type()
)
lowCurrentThreshold26.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold26.setStatus("current")
if mibBuilder.loadTexts:
    lowCurrentThreshold26.setUnits("Amps")


class _LowCurrentThreshold27_Type(Integer32):
    """Custom type lowCurrentThreshold27 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LowCurrentThreshold27_Type.__name__ = "Integer32"
_LowCurrentThreshold27_Object = MibScalar
lowCurrentThreshold27 = _LowCurrentThreshold27_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 5, 27),
    _LowCurrentThreshold27_Type()
)
lowCurrentThreshold27.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold27.setStatus("current")
if mibBuilder.loadTexts:
    lowCurrentThreshold27.setUnits("Amps")


class _LowCurrentThreshold28_Type(Integer32):
    """Custom type lowCurrentThreshold28 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LowCurrentThreshold28_Type.__name__ = "Integer32"
_LowCurrentThreshold28_Object = MibScalar
lowCurrentThreshold28 = _LowCurrentThreshold28_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 5, 28),
    _LowCurrentThreshold28_Type()
)
lowCurrentThreshold28.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold28.setStatus("current")
if mibBuilder.loadTexts:
    lowCurrentThreshold28.setUnits("Amps")


class _LowCurrentThreshold29_Type(Integer32):
    """Custom type lowCurrentThreshold29 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LowCurrentThreshold29_Type.__name__ = "Integer32"
_LowCurrentThreshold29_Object = MibScalar
lowCurrentThreshold29 = _LowCurrentThreshold29_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 5, 29),
    _LowCurrentThreshold29_Type()
)
lowCurrentThreshold29.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold29.setStatus("current")
if mibBuilder.loadTexts:
    lowCurrentThreshold29.setUnits("Amps")


class _LowCurrentThreshold30_Type(Integer32):
    """Custom type lowCurrentThreshold30 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LowCurrentThreshold30_Type.__name__ = "Integer32"
_LowCurrentThreshold30_Object = MibScalar
lowCurrentThreshold30 = _LowCurrentThreshold30_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 5, 30),
    _LowCurrentThreshold30_Type()
)
lowCurrentThreshold30.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold30.setStatus("current")
if mibBuilder.loadTexts:
    lowCurrentThreshold30.setUnits("Amps")


class _LowCurrentThreshold31_Type(Integer32):
    """Custom type lowCurrentThreshold31 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LowCurrentThreshold31_Type.__name__ = "Integer32"
_LowCurrentThreshold31_Object = MibScalar
lowCurrentThreshold31 = _LowCurrentThreshold31_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 5, 31),
    _LowCurrentThreshold31_Type()
)
lowCurrentThreshold31.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold31.setStatus("current")
if mibBuilder.loadTexts:
    lowCurrentThreshold31.setUnits("Amps")


class _LowCurrentThreshold32_Type(Integer32):
    """Custom type lowCurrentThreshold32 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LowCurrentThreshold32_Type.__name__ = "Integer32"
_LowCurrentThreshold32_Object = MibScalar
lowCurrentThreshold32 = _LowCurrentThreshold32_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 5, 32),
    _LowCurrentThreshold32_Type()
)
lowCurrentThreshold32.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowCurrentThreshold32.setStatus("current")
if mibBuilder.loadTexts:
    lowCurrentThreshold32.setUnits("Amps")
_HighCurrentThresh_ObjectIdentity = ObjectIdentity
highCurrentThresh = _HighCurrentThresh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 6)
)


class _HighCurrentThreshold1_Type(Integer32):
    """Custom type highCurrentThreshold1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HighCurrentThreshold1_Type.__name__ = "Integer32"
_HighCurrentThreshold1_Object = MibScalar
highCurrentThreshold1 = _HighCurrentThreshold1_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 6, 1),
    _HighCurrentThreshold1_Type()
)
highCurrentThreshold1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold1.setStatus("current")
if mibBuilder.loadTexts:
    highCurrentThreshold1.setUnits("Amps")


class _HighCurrentThreshold2_Type(Integer32):
    """Custom type highCurrentThreshold2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HighCurrentThreshold2_Type.__name__ = "Integer32"
_HighCurrentThreshold2_Object = MibScalar
highCurrentThreshold2 = _HighCurrentThreshold2_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 6, 2),
    _HighCurrentThreshold2_Type()
)
highCurrentThreshold2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold2.setStatus("current")
if mibBuilder.loadTexts:
    highCurrentThreshold2.setUnits("Amps")


class _HighCurrentThreshold3_Type(Integer32):
    """Custom type highCurrentThreshold3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HighCurrentThreshold3_Type.__name__ = "Integer32"
_HighCurrentThreshold3_Object = MibScalar
highCurrentThreshold3 = _HighCurrentThreshold3_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 6, 3),
    _HighCurrentThreshold3_Type()
)
highCurrentThreshold3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold3.setStatus("current")
if mibBuilder.loadTexts:
    highCurrentThreshold3.setUnits("Amps")


class _HighCurrentThreshold4_Type(Integer32):
    """Custom type highCurrentThreshold4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HighCurrentThreshold4_Type.__name__ = "Integer32"
_HighCurrentThreshold4_Object = MibScalar
highCurrentThreshold4 = _HighCurrentThreshold4_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 6, 4),
    _HighCurrentThreshold4_Type()
)
highCurrentThreshold4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold4.setStatus("current")
if mibBuilder.loadTexts:
    highCurrentThreshold4.setUnits("Amps")


class _HighCurrentThreshold5_Type(Integer32):
    """Custom type highCurrentThreshold5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HighCurrentThreshold5_Type.__name__ = "Integer32"
_HighCurrentThreshold5_Object = MibScalar
highCurrentThreshold5 = _HighCurrentThreshold5_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 6, 5),
    _HighCurrentThreshold5_Type()
)
highCurrentThreshold5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold5.setStatus("current")
if mibBuilder.loadTexts:
    highCurrentThreshold5.setUnits("Amps")


class _HighCurrentThreshold6_Type(Integer32):
    """Custom type highCurrentThreshold6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HighCurrentThreshold6_Type.__name__ = "Integer32"
_HighCurrentThreshold6_Object = MibScalar
highCurrentThreshold6 = _HighCurrentThreshold6_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 6, 6),
    _HighCurrentThreshold6_Type()
)
highCurrentThreshold6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold6.setStatus("current")
if mibBuilder.loadTexts:
    highCurrentThreshold6.setUnits("Amps")


class _HighCurrentThreshold7_Type(Integer32):
    """Custom type highCurrentThreshold7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HighCurrentThreshold7_Type.__name__ = "Integer32"
_HighCurrentThreshold7_Object = MibScalar
highCurrentThreshold7 = _HighCurrentThreshold7_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 6, 7),
    _HighCurrentThreshold7_Type()
)
highCurrentThreshold7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold7.setStatus("current")
if mibBuilder.loadTexts:
    highCurrentThreshold7.setUnits("Amps")


class _HighCurrentThreshold8_Type(Integer32):
    """Custom type highCurrentThreshold8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HighCurrentThreshold8_Type.__name__ = "Integer32"
_HighCurrentThreshold8_Object = MibScalar
highCurrentThreshold8 = _HighCurrentThreshold8_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 6, 8),
    _HighCurrentThreshold8_Type()
)
highCurrentThreshold8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold8.setStatus("current")
if mibBuilder.loadTexts:
    highCurrentThreshold8.setUnits("Amps")


class _HighCurrentThreshold9_Type(Integer32):
    """Custom type highCurrentThreshold9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HighCurrentThreshold9_Type.__name__ = "Integer32"
_HighCurrentThreshold9_Object = MibScalar
highCurrentThreshold9 = _HighCurrentThreshold9_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 6, 9),
    _HighCurrentThreshold9_Type()
)
highCurrentThreshold9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold9.setStatus("current")
if mibBuilder.loadTexts:
    highCurrentThreshold9.setUnits("Amps")


class _HighCurrentThreshold10_Type(Integer32):
    """Custom type highCurrentThreshold10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HighCurrentThreshold10_Type.__name__ = "Integer32"
_HighCurrentThreshold10_Object = MibScalar
highCurrentThreshold10 = _HighCurrentThreshold10_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 6, 10),
    _HighCurrentThreshold10_Type()
)
highCurrentThreshold10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold10.setStatus("current")
if mibBuilder.loadTexts:
    highCurrentThreshold10.setUnits("Amps")


class _HighCurrentThreshold11_Type(Integer32):
    """Custom type highCurrentThreshold11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HighCurrentThreshold11_Type.__name__ = "Integer32"
_HighCurrentThreshold11_Object = MibScalar
highCurrentThreshold11 = _HighCurrentThreshold11_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 6, 11),
    _HighCurrentThreshold11_Type()
)
highCurrentThreshold11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold11.setStatus("current")
if mibBuilder.loadTexts:
    highCurrentThreshold11.setUnits("Amps")


class _HighCurrentThreshold12_Type(Integer32):
    """Custom type highCurrentThreshold12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HighCurrentThreshold12_Type.__name__ = "Integer32"
_HighCurrentThreshold12_Object = MibScalar
highCurrentThreshold12 = _HighCurrentThreshold12_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 6, 12),
    _HighCurrentThreshold12_Type()
)
highCurrentThreshold12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold12.setStatus("current")
if mibBuilder.loadTexts:
    highCurrentThreshold12.setUnits("Amps")


class _HighCurrentThreshold13_Type(Integer32):
    """Custom type highCurrentThreshold13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HighCurrentThreshold13_Type.__name__ = "Integer32"
_HighCurrentThreshold13_Object = MibScalar
highCurrentThreshold13 = _HighCurrentThreshold13_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 6, 13),
    _HighCurrentThreshold13_Type()
)
highCurrentThreshold13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold13.setStatus("current")
if mibBuilder.loadTexts:
    highCurrentThreshold13.setUnits("Amps")


class _HighCurrentThreshold14_Type(Integer32):
    """Custom type highCurrentThreshold14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HighCurrentThreshold14_Type.__name__ = "Integer32"
_HighCurrentThreshold14_Object = MibScalar
highCurrentThreshold14 = _HighCurrentThreshold14_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 6, 14),
    _HighCurrentThreshold14_Type()
)
highCurrentThreshold14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold14.setStatus("current")
if mibBuilder.loadTexts:
    highCurrentThreshold14.setUnits("Amps")


class _HighCurrentThreshold15_Type(Integer32):
    """Custom type highCurrentThreshold15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HighCurrentThreshold15_Type.__name__ = "Integer32"
_HighCurrentThreshold15_Object = MibScalar
highCurrentThreshold15 = _HighCurrentThreshold15_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 6, 15),
    _HighCurrentThreshold15_Type()
)
highCurrentThreshold15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold15.setStatus("current")
if mibBuilder.loadTexts:
    highCurrentThreshold15.setUnits("Amps")


class _HighCurrentThreshold16_Type(Integer32):
    """Custom type highCurrentThreshold16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HighCurrentThreshold16_Type.__name__ = "Integer32"
_HighCurrentThreshold16_Object = MibScalar
highCurrentThreshold16 = _HighCurrentThreshold16_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 6, 16),
    _HighCurrentThreshold16_Type()
)
highCurrentThreshold16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold16.setStatus("current")
if mibBuilder.loadTexts:
    highCurrentThreshold16.setUnits("Amps")


class _HighCurrentThreshold17_Type(Integer32):
    """Custom type highCurrentThreshold17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HighCurrentThreshold17_Type.__name__ = "Integer32"
_HighCurrentThreshold17_Object = MibScalar
highCurrentThreshold17 = _HighCurrentThreshold17_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 6, 17),
    _HighCurrentThreshold17_Type()
)
highCurrentThreshold17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold17.setStatus("current")
if mibBuilder.loadTexts:
    highCurrentThreshold17.setUnits("Amps")


class _HighCurrentThreshold18_Type(Integer32):
    """Custom type highCurrentThreshold18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HighCurrentThreshold18_Type.__name__ = "Integer32"
_HighCurrentThreshold18_Object = MibScalar
highCurrentThreshold18 = _HighCurrentThreshold18_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 6, 18),
    _HighCurrentThreshold18_Type()
)
highCurrentThreshold18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold18.setStatus("current")
if mibBuilder.loadTexts:
    highCurrentThreshold18.setUnits("Amps")


class _HighCurrentThreshold19_Type(Integer32):
    """Custom type highCurrentThreshold19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HighCurrentThreshold19_Type.__name__ = "Integer32"
_HighCurrentThreshold19_Object = MibScalar
highCurrentThreshold19 = _HighCurrentThreshold19_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 6, 19),
    _HighCurrentThreshold19_Type()
)
highCurrentThreshold19.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold19.setStatus("current")
if mibBuilder.loadTexts:
    highCurrentThreshold19.setUnits("Amps")


class _HighCurrentThreshold20_Type(Integer32):
    """Custom type highCurrentThreshold20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HighCurrentThreshold20_Type.__name__ = "Integer32"
_HighCurrentThreshold20_Object = MibScalar
highCurrentThreshold20 = _HighCurrentThreshold20_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 6, 20),
    _HighCurrentThreshold20_Type()
)
highCurrentThreshold20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold20.setStatus("current")
if mibBuilder.loadTexts:
    highCurrentThreshold20.setUnits("Amps")


class _HighCurrentThreshold21_Type(Integer32):
    """Custom type highCurrentThreshold21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HighCurrentThreshold21_Type.__name__ = "Integer32"
_HighCurrentThreshold21_Object = MibScalar
highCurrentThreshold21 = _HighCurrentThreshold21_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 6, 21),
    _HighCurrentThreshold21_Type()
)
highCurrentThreshold21.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold21.setStatus("current")
if mibBuilder.loadTexts:
    highCurrentThreshold21.setUnits("Amps")


class _HighCurrentThreshold22_Type(Integer32):
    """Custom type highCurrentThreshold22 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HighCurrentThreshold22_Type.__name__ = "Integer32"
_HighCurrentThreshold22_Object = MibScalar
highCurrentThreshold22 = _HighCurrentThreshold22_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 6, 22),
    _HighCurrentThreshold22_Type()
)
highCurrentThreshold22.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold22.setStatus("current")
if mibBuilder.loadTexts:
    highCurrentThreshold22.setUnits("Amps")


class _HighCurrentThreshold23_Type(Integer32):
    """Custom type highCurrentThreshold23 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HighCurrentThreshold23_Type.__name__ = "Integer32"
_HighCurrentThreshold23_Object = MibScalar
highCurrentThreshold23 = _HighCurrentThreshold23_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 6, 23),
    _HighCurrentThreshold23_Type()
)
highCurrentThreshold23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold23.setStatus("current")
if mibBuilder.loadTexts:
    highCurrentThreshold23.setUnits("Amps")


class _HighCurrentThreshold24_Type(Integer32):
    """Custom type highCurrentThreshold24 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HighCurrentThreshold24_Type.__name__ = "Integer32"
_HighCurrentThreshold24_Object = MibScalar
highCurrentThreshold24 = _HighCurrentThreshold24_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 6, 24),
    _HighCurrentThreshold24_Type()
)
highCurrentThreshold24.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold24.setStatus("current")
if mibBuilder.loadTexts:
    highCurrentThreshold24.setUnits("Amps")


class _HighCurrentThreshold25_Type(Integer32):
    """Custom type highCurrentThreshold25 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HighCurrentThreshold25_Type.__name__ = "Integer32"
_HighCurrentThreshold25_Object = MibScalar
highCurrentThreshold25 = _HighCurrentThreshold25_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 6, 25),
    _HighCurrentThreshold25_Type()
)
highCurrentThreshold25.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold25.setStatus("current")
if mibBuilder.loadTexts:
    highCurrentThreshold25.setUnits("Amps")


class _HighCurrentThreshold26_Type(Integer32):
    """Custom type highCurrentThreshold26 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HighCurrentThreshold26_Type.__name__ = "Integer32"
_HighCurrentThreshold26_Object = MibScalar
highCurrentThreshold26 = _HighCurrentThreshold26_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 6, 26),
    _HighCurrentThreshold26_Type()
)
highCurrentThreshold26.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold26.setStatus("current")
if mibBuilder.loadTexts:
    highCurrentThreshold26.setUnits("Amps")


class _HighCurrentThreshold27_Type(Integer32):
    """Custom type highCurrentThreshold27 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HighCurrentThreshold27_Type.__name__ = "Integer32"
_HighCurrentThreshold27_Object = MibScalar
highCurrentThreshold27 = _HighCurrentThreshold27_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 6, 27),
    _HighCurrentThreshold27_Type()
)
highCurrentThreshold27.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold27.setStatus("current")
if mibBuilder.loadTexts:
    highCurrentThreshold27.setUnits("Amps")


class _HighCurrentThreshold28_Type(Integer32):
    """Custom type highCurrentThreshold28 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HighCurrentThreshold28_Type.__name__ = "Integer32"
_HighCurrentThreshold28_Object = MibScalar
highCurrentThreshold28 = _HighCurrentThreshold28_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 6, 28),
    _HighCurrentThreshold28_Type()
)
highCurrentThreshold28.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold28.setStatus("current")
if mibBuilder.loadTexts:
    highCurrentThreshold28.setUnits("Amps")


class _HighCurrentThreshold29_Type(Integer32):
    """Custom type highCurrentThreshold29 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HighCurrentThreshold29_Type.__name__ = "Integer32"
_HighCurrentThreshold29_Object = MibScalar
highCurrentThreshold29 = _HighCurrentThreshold29_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 6, 29),
    _HighCurrentThreshold29_Type()
)
highCurrentThreshold29.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold29.setStatus("current")
if mibBuilder.loadTexts:
    highCurrentThreshold29.setUnits("Amps")


class _HighCurrentThreshold30_Type(Integer32):
    """Custom type highCurrentThreshold30 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HighCurrentThreshold30_Type.__name__ = "Integer32"
_HighCurrentThreshold30_Object = MibScalar
highCurrentThreshold30 = _HighCurrentThreshold30_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 6, 30),
    _HighCurrentThreshold30_Type()
)
highCurrentThreshold30.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold30.setStatus("current")
if mibBuilder.loadTexts:
    highCurrentThreshold30.setUnits("Amps")


class _HighCurrentThreshold31_Type(Integer32):
    """Custom type highCurrentThreshold31 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HighCurrentThreshold31_Type.__name__ = "Integer32"
_HighCurrentThreshold31_Object = MibScalar
highCurrentThreshold31 = _HighCurrentThreshold31_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 6, 31),
    _HighCurrentThreshold31_Type()
)
highCurrentThreshold31.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold31.setStatus("current")
if mibBuilder.loadTexts:
    highCurrentThreshold31.setUnits("Amps")


class _HighCurrentThreshold32_Type(Integer32):
    """Custom type highCurrentThreshold32 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HighCurrentThreshold32_Type.__name__ = "Integer32"
_HighCurrentThreshold32_Object = MibScalar
highCurrentThreshold32 = _HighCurrentThreshold32_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 6, 32),
    _HighCurrentThreshold32_Type()
)
highCurrentThreshold32.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highCurrentThreshold32.setStatus("current")
if mibBuilder.loadTexts:
    highCurrentThreshold32.setUnits("Amps")
_LowTempThresh_ObjectIdentity = ObjectIdentity
lowTempThresh = _LowTempThresh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 7)
)


class _LowTempThreshold1_Type(Integer32):
    """Custom type lowTempThreshold1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_LowTempThreshold1_Type.__name__ = "Integer32"
_LowTempThreshold1_Object = MibScalar
lowTempThreshold1 = _LowTempThreshold1_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 7, 1),
    _LowTempThreshold1_Type()
)
lowTempThreshold1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowTempThreshold1.setStatus("current")
if mibBuilder.loadTexts:
    lowTempThreshold1.setUnits("Degrees")


class _LowTempThreshold2_Type(Integer32):
    """Custom type lowTempThreshold2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_LowTempThreshold2_Type.__name__ = "Integer32"
_LowTempThreshold2_Object = MibScalar
lowTempThreshold2 = _LowTempThreshold2_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 7, 2),
    _LowTempThreshold2_Type()
)
lowTempThreshold2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowTempThreshold2.setStatus("current")
if mibBuilder.loadTexts:
    lowTempThreshold2.setUnits("Degrees")
_HighTempThresh_ObjectIdentity = ObjectIdentity
highTempThresh = _HighTempThresh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 8)
)


class _HighTempThreshold1_Type(Integer32):
    """Custom type highTempThreshold1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_HighTempThreshold1_Type.__name__ = "Integer32"
_HighTempThreshold1_Object = MibScalar
highTempThreshold1 = _HighTempThreshold1_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 8, 1),
    _HighTempThreshold1_Type()
)
highTempThreshold1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highTempThreshold1.setStatus("current")
if mibBuilder.loadTexts:
    highTempThreshold1.setUnits("Degrees")


class _HighTempThreshold2_Type(Integer32):
    """Custom type highTempThreshold2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_HighTempThreshold2_Type.__name__ = "Integer32"
_HighTempThreshold2_Object = MibScalar
highTempThreshold2 = _HighTempThreshold2_Object(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 8, 2),
    _HighTempThreshold2_Type()
)
highTempThreshold2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highTempThreshold2.setStatus("current")
if mibBuilder.loadTexts:
    highTempThreshold2.setUnits("Degrees")
_Conformance_ObjectIdentity = ObjectIdentity
conformance = _Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 25)
)
_Groups_ObjectIdentity = ObjectIdentity
groups = _Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 25, 5)
)

# Managed Objects groups

unitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 25, 5, 1)
)
unitGroup.setObjects(
      *(("EATON-EPDU-PU-MI-MIB", "mailServerIP"),
        ("EATON-EPDU-PU-MI-MIB", "alertEmailAddress"),
        ("EATON-EPDU-PU-MI-MIB", "assetID"),
        ("EATON-EPDU-PU-MI-MIB", "chan10Name"),
        ("EATON-EPDU-PU-MI-MIB", "chan11Name"),
        ("EATON-EPDU-PU-MI-MIB", "chan12Name"),
        ("EATON-EPDU-PU-MI-MIB", "chan13Name"),
        ("EATON-EPDU-PU-MI-MIB", "chan14Name"),
        ("EATON-EPDU-PU-MI-MIB", "chan15Name"),
        ("EATON-EPDU-PU-MI-MIB", "chan16Name"),
        ("EATON-EPDU-PU-MI-MIB", "chan17Name"),
        ("EATON-EPDU-PU-MI-MIB", "chan18Name"),
        ("EATON-EPDU-PU-MI-MIB", "chan19Name"),
        ("EATON-EPDU-PU-MI-MIB", "chan1Name"),
        ("EATON-EPDU-PU-MI-MIB", "chan20Name"),
        ("EATON-EPDU-PU-MI-MIB", "chan21Name"),
        ("EATON-EPDU-PU-MI-MIB", "chan22Name"),
        ("EATON-EPDU-PU-MI-MIB", "chan23Name"),
        ("EATON-EPDU-PU-MI-MIB", "chan24Name"),
        ("EATON-EPDU-PU-MI-MIB", "chan25Name"),
        ("EATON-EPDU-PU-MI-MIB", "chan26Name"),
        ("EATON-EPDU-PU-MI-MIB", "chan27Name"),
        ("EATON-EPDU-PU-MI-MIB", "chan28Name"),
        ("EATON-EPDU-PU-MI-MIB", "chan29Name"),
        ("EATON-EPDU-PU-MI-MIB", "chan2Name"),
        ("EATON-EPDU-PU-MI-MIB", "chan30Name"),
        ("EATON-EPDU-PU-MI-MIB", "chan31Name"),
        ("EATON-EPDU-PU-MI-MIB", "chan32Name"),
        ("EATON-EPDU-PU-MI-MIB", "chan3Name"),
        ("EATON-EPDU-PU-MI-MIB", "chan4Name"),
        ("EATON-EPDU-PU-MI-MIB", "chan5Name"),
        ("EATON-EPDU-PU-MI-MIB", "chan6Name"),
        ("EATON-EPDU-PU-MI-MIB", "chan7Name"),
        ("EATON-EPDU-PU-MI-MIB", "chan8Name"),
        ("EATON-EPDU-PU-MI-MIB", "chan9Name"),
        ("EATON-EPDU-PU-MI-MIB", "currentMonitorType"),
        ("EATON-EPDU-PU-MI-MIB", "firmwareRevision"),
        ("EATON-EPDU-PU-MI-MIB", "numCurrentChannels"),
        ("EATON-EPDU-PU-MI-MIB", "temp1Name"),
        ("EATON-EPDU-PU-MI-MIB", "temp2Name"),
        ("EATON-EPDU-PU-MI-MIB", "temperature1Enable"),
        ("EATON-EPDU-PU-MI-MIB", "temperature2Enable"),
        ("EATON-EPDU-PU-MI-MIB", "trapDestIP"),
        ("EATON-EPDU-PU-MI-MIB", "unitGateway"),
        ("EATON-EPDU-PU-MI-MIB", "unitIPAddress"),
        ("EATON-EPDU-PU-MI-MIB", "unitMACAddress"),
        ("EATON-EPDU-PU-MI-MIB", "unitName"),
        ("EATON-EPDU-PU-MI-MIB", "unitSubnetMask"),
        ("EATON-EPDU-PU-MI-MIB", "uptime"))
)
if mibBuilder.loadTexts:
    unitGroup.setStatus("current")

measurementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 25, 5, 2)
)
measurementGroup.setObjects(
      *(("EATON-EPDU-PU-MI-MIB", "chan1"),
        ("EATON-EPDU-PU-MI-MIB", "chan10"),
        ("EATON-EPDU-PU-MI-MIB", "chan11"),
        ("EATON-EPDU-PU-MI-MIB", "chan12"),
        ("EATON-EPDU-PU-MI-MIB", "chan13"),
        ("EATON-EPDU-PU-MI-MIB", "chan14"),
        ("EATON-EPDU-PU-MI-MIB", "chan15"),
        ("EATON-EPDU-PU-MI-MIB", "chan16"),
        ("EATON-EPDU-PU-MI-MIB", "chan17"),
        ("EATON-EPDU-PU-MI-MIB", "chan18"),
        ("EATON-EPDU-PU-MI-MIB", "chan19"),
        ("EATON-EPDU-PU-MI-MIB", "chan2"),
        ("EATON-EPDU-PU-MI-MIB", "chan20"),
        ("EATON-EPDU-PU-MI-MIB", "chan21"),
        ("EATON-EPDU-PU-MI-MIB", "chan22"),
        ("EATON-EPDU-PU-MI-MIB", "chan23"),
        ("EATON-EPDU-PU-MI-MIB", "chan24"),
        ("EATON-EPDU-PU-MI-MIB", "chan25"),
        ("EATON-EPDU-PU-MI-MIB", "chan26"),
        ("EATON-EPDU-PU-MI-MIB", "chan27"),
        ("EATON-EPDU-PU-MI-MIB", "chan28"),
        ("EATON-EPDU-PU-MI-MIB", "chan29"),
        ("EATON-EPDU-PU-MI-MIB", "chan3"),
        ("EATON-EPDU-PU-MI-MIB", "chan30"),
        ("EATON-EPDU-PU-MI-MIB", "chan31"),
        ("EATON-EPDU-PU-MI-MIB", "chan32"),
        ("EATON-EPDU-PU-MI-MIB", "chan4"),
        ("EATON-EPDU-PU-MI-MIB", "chan5"),
        ("EATON-EPDU-PU-MI-MIB", "chan6"),
        ("EATON-EPDU-PU-MI-MIB", "chan7"),
        ("EATON-EPDU-PU-MI-MIB", "chan8"),
        ("EATON-EPDU-PU-MI-MIB", "chan9"),
        ("EATON-EPDU-PU-MI-MIB", "tempChan1"),
        ("EATON-EPDU-PU-MI-MIB", "tempChan2"))
)
if mibBuilder.loadTexts:
    measurementGroup.setStatus("current")

thresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 25, 5, 3)
)
thresholdGroup.setObjects(
      *(("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold1"),
        ("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold10"),
        ("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold11"),
        ("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold12"),
        ("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold13"),
        ("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold14"),
        ("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold15"),
        ("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold16"),
        ("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold17"),
        ("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold18"),
        ("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold19"),
        ("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold2"),
        ("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold20"),
        ("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold21"),
        ("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold22"),
        ("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold23"),
        ("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold24"),
        ("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold25"),
        ("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold26"),
        ("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold27"),
        ("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold28"),
        ("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold29"),
        ("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold3"),
        ("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold30"),
        ("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold31"),
        ("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold32"),
        ("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold4"),
        ("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold5"),
        ("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold6"),
        ("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold7"),
        ("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold8"),
        ("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold9"),
        ("EATON-EPDU-PU-MI-MIB", "highTempThreshold1"),
        ("EATON-EPDU-PU-MI-MIB", "highTempThreshold2"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold1"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold10"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold11"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold12"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold13"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold14"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold15"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold16"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold17"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold18"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold19"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold2"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold20"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold21"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold22"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold23"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold24"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold25"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold26"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold27"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold28"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold29"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold3"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold30"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold31"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold32"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold4"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold5"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold6"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold7"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold8"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold9"),
        ("EATON-EPDU-PU-MI-MIB", "lowTempThreshold1"),
        ("EATON-EPDU-PU-MI-MIB", "lowTempThreshold2"))
)
if mibBuilder.loadTexts:
    thresholdGroup.setStatus("current")

thresholdGroupOld = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 25, 5, 4)
)
thresholdGroupOld.setObjects(
      *(("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold1old"),
        ("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold2old"),
        ("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold3old"),
        ("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold4old"),
        ("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold5old"),
        ("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold6old"),
        ("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold7old"),
        ("EATON-EPDU-PU-MI-MIB", "highCurrentThreshold8old"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold1old"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold2old"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold3old"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold4old"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold5old"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold6old"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold7old"),
        ("EATON-EPDU-PU-MI-MIB", "lowCurrentThreshold8old"))
)
if mibBuilder.loadTexts:
    thresholdGroupOld.setStatus("deprecated")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

compliances = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 25, 1)
)
if mibBuilder.loadTexts:
    compliances.setStatus(
        "current"
    )

oldCompliances = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 20677, 3, 1, 1, 25, 2)
)
if mibBuilder.loadTexts:
    oldCompliances.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EATON-EPDU-PU-MI-MIB",
    **{"pulizzi": pulizzi,
       "monitoredepdu": monitoredepdu,
       "epdum1": epdum1,
       "epdum11": epdum11,
       "unitConfig": unitConfig,
       "uptime": uptime,
       "unitName": unitName,
       "lowCurrentThreshold1old": lowCurrentThreshold1old,
       "lowCurrentThreshold2old": lowCurrentThreshold2old,
       "lowCurrentThreshold3old": lowCurrentThreshold3old,
       "lowCurrentThreshold4old": lowCurrentThreshold4old,
       "lowCurrentThreshold5old": lowCurrentThreshold5old,
       "lowCurrentThreshold6old": lowCurrentThreshold6old,
       "lowCurrentThreshold7old": lowCurrentThreshold7old,
       "lowCurrentThreshold8old": lowCurrentThreshold8old,
       "highCurrentThreshold1old": highCurrentThreshold1old,
       "highCurrentThreshold2old": highCurrentThreshold2old,
       "highCurrentThreshold3old": highCurrentThreshold3old,
       "highCurrentThreshold4old": highCurrentThreshold4old,
       "highCurrentThreshold5old": highCurrentThreshold5old,
       "highCurrentThreshold6old": highCurrentThreshold6old,
       "highCurrentThreshold7old": highCurrentThreshold7old,
       "highCurrentThreshold8old": highCurrentThreshold8old,
       "temperature1Enable": temperature1Enable,
       "temperature2Enable": temperature2Enable,
       "firmwareRevision": firmwareRevision,
       "assetID": assetID,
       "numCurrentChannels": numCurrentChannels,
       "currentMonitorType": currentMonitorType,
       "networkSettings": networkSettings,
       "unitIPAddress": unitIPAddress,
       "unitSubnetMask": unitSubnetMask,
       "unitGateway": unitGateway,
       "unitMACAddress": unitMACAddress,
       "trapDestIP": trapDestIP,
       "mailServerIP": mailServerIP,
       "alertEmailAddress": alertEmailAddress,
       "measurements": measurements,
       "chan1": chan1,
       "chan2": chan2,
       "chan3": chan3,
       "chan4": chan4,
       "chan5": chan5,
       "chan6": chan6,
       "chan7": chan7,
       "chan8": chan8,
       "chan9": chan9,
       "chan10": chan10,
       "chan11": chan11,
       "chan12": chan12,
       "chan13": chan13,
       "chan14": chan14,
       "chan15": chan15,
       "chan16": chan16,
       "chan17": chan17,
       "chan18": chan18,
       "chan19": chan19,
       "chan20": chan20,
       "chan21": chan21,
       "chan22": chan22,
       "chan23": chan23,
       "chan24": chan24,
       "chan25": chan25,
       "chan26": chan26,
       "chan27": chan27,
       "chan28": chan28,
       "chan29": chan29,
       "chan30": chan30,
       "chan31": chan31,
       "chan32": chan32,
       "tempChan1": tempChan1,
       "tempChan2": tempChan2,
       "chanNames": chanNames,
       "chan1Name": chan1Name,
       "chan2Name": chan2Name,
       "chan3Name": chan3Name,
       "chan4Name": chan4Name,
       "chan5Name": chan5Name,
       "chan6Name": chan6Name,
       "chan7Name": chan7Name,
       "chan8Name": chan8Name,
       "chan9Name": chan9Name,
       "chan10Name": chan10Name,
       "chan11Name": chan11Name,
       "chan12Name": chan12Name,
       "chan13Name": chan13Name,
       "chan14Name": chan14Name,
       "chan15Name": chan15Name,
       "chan16Name": chan16Name,
       "chan17Name": chan17Name,
       "chan18Name": chan18Name,
       "chan19Name": chan19Name,
       "chan20Name": chan20Name,
       "chan21Name": chan21Name,
       "chan22Name": chan22Name,
       "chan23Name": chan23Name,
       "chan24Name": chan24Name,
       "chan25Name": chan25Name,
       "chan26Name": chan26Name,
       "chan27Name": chan27Name,
       "chan28Name": chan28Name,
       "chan29Name": chan29Name,
       "chan30Name": chan30Name,
       "chan31Name": chan31Name,
       "chan32Name": chan32Name,
       "temp1Name": temp1Name,
       "temp2Name": temp2Name,
       "lowCurrentThresh": lowCurrentThresh,
       "lowCurrentThreshold1": lowCurrentThreshold1,
       "lowCurrentThreshold2": lowCurrentThreshold2,
       "lowCurrentThreshold3": lowCurrentThreshold3,
       "lowCurrentThreshold4": lowCurrentThreshold4,
       "lowCurrentThreshold5": lowCurrentThreshold5,
       "lowCurrentThreshold6": lowCurrentThreshold6,
       "lowCurrentThreshold7": lowCurrentThreshold7,
       "lowCurrentThreshold8": lowCurrentThreshold8,
       "lowCurrentThreshold9": lowCurrentThreshold9,
       "lowCurrentThreshold10": lowCurrentThreshold10,
       "lowCurrentThreshold11": lowCurrentThreshold11,
       "lowCurrentThreshold12": lowCurrentThreshold12,
       "lowCurrentThreshold13": lowCurrentThreshold13,
       "lowCurrentThreshold14": lowCurrentThreshold14,
       "lowCurrentThreshold15": lowCurrentThreshold15,
       "lowCurrentThreshold16": lowCurrentThreshold16,
       "lowCurrentThreshold17": lowCurrentThreshold17,
       "lowCurrentThreshold18": lowCurrentThreshold18,
       "lowCurrentThreshold19": lowCurrentThreshold19,
       "lowCurrentThreshold20": lowCurrentThreshold20,
       "lowCurrentThreshold21": lowCurrentThreshold21,
       "lowCurrentThreshold22": lowCurrentThreshold22,
       "lowCurrentThreshold23": lowCurrentThreshold23,
       "lowCurrentThreshold24": lowCurrentThreshold24,
       "lowCurrentThreshold25": lowCurrentThreshold25,
       "lowCurrentThreshold26": lowCurrentThreshold26,
       "lowCurrentThreshold27": lowCurrentThreshold27,
       "lowCurrentThreshold28": lowCurrentThreshold28,
       "lowCurrentThreshold29": lowCurrentThreshold29,
       "lowCurrentThreshold30": lowCurrentThreshold30,
       "lowCurrentThreshold31": lowCurrentThreshold31,
       "lowCurrentThreshold32": lowCurrentThreshold32,
       "highCurrentThresh": highCurrentThresh,
       "highCurrentThreshold1": highCurrentThreshold1,
       "highCurrentThreshold2": highCurrentThreshold2,
       "highCurrentThreshold3": highCurrentThreshold3,
       "highCurrentThreshold4": highCurrentThreshold4,
       "highCurrentThreshold5": highCurrentThreshold5,
       "highCurrentThreshold6": highCurrentThreshold6,
       "highCurrentThreshold7": highCurrentThreshold7,
       "highCurrentThreshold8": highCurrentThreshold8,
       "highCurrentThreshold9": highCurrentThreshold9,
       "highCurrentThreshold10": highCurrentThreshold10,
       "highCurrentThreshold11": highCurrentThreshold11,
       "highCurrentThreshold12": highCurrentThreshold12,
       "highCurrentThreshold13": highCurrentThreshold13,
       "highCurrentThreshold14": highCurrentThreshold14,
       "highCurrentThreshold15": highCurrentThreshold15,
       "highCurrentThreshold16": highCurrentThreshold16,
       "highCurrentThreshold17": highCurrentThreshold17,
       "highCurrentThreshold18": highCurrentThreshold18,
       "highCurrentThreshold19": highCurrentThreshold19,
       "highCurrentThreshold20": highCurrentThreshold20,
       "highCurrentThreshold21": highCurrentThreshold21,
       "highCurrentThreshold22": highCurrentThreshold22,
       "highCurrentThreshold23": highCurrentThreshold23,
       "highCurrentThreshold24": highCurrentThreshold24,
       "highCurrentThreshold25": highCurrentThreshold25,
       "highCurrentThreshold26": highCurrentThreshold26,
       "highCurrentThreshold27": highCurrentThreshold27,
       "highCurrentThreshold28": highCurrentThreshold28,
       "highCurrentThreshold29": highCurrentThreshold29,
       "highCurrentThreshold30": highCurrentThreshold30,
       "highCurrentThreshold31": highCurrentThreshold31,
       "highCurrentThreshold32": highCurrentThreshold32,
       "lowTempThresh": lowTempThresh,
       "lowTempThreshold1": lowTempThreshold1,
       "lowTempThreshold2": lowTempThreshold2,
       "highTempThresh": highTempThresh,
       "highTempThreshold1": highTempThreshold1,
       "highTempThreshold2": highTempThreshold2,
       "conformance": conformance,
       "compliances": compliances,
       "oldCompliances": oldCompliances,
       "groups": groups,
       "unitGroup": unitGroup,
       "measurementGroup": measurementGroup,
       "thresholdGroup": thresholdGroup,
       "thresholdGroupOld": thresholdGroupOld}
)
