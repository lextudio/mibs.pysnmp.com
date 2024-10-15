# SNMP MIB module (ELTEX-TAU8) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-TAU8
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:17 2024
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

(elHardware,) = mibBuilder.importSymbols(
    "ELTEX-SMI-ACTUAL",
    "elHardware")

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
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

tau8 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55)
)
tau8.setRevisions(
        ("2013-08-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CallerIdType(Integer32, TextualConvention):
    status = "current"
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
        *(("bell", 0),
          ("dtmf", 2),
          ("off", 3),
          ("v23", 1))
    )



class CallTransferType(Integer32, TextualConvention):
    status = "current"
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
        *(("attendedCT", 1),
          ("localCT", 3),
          ("transmitFlash", 0),
          ("unattendedCT", 2))
    )



class RsrvModeType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("homing", 1),
          ("off", 0),
          ("parking", 2))
    )



class RsrvCheckMethodType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invite", 0),
          ("options", 2),
          ("register", 1))
    )



class OutboundType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("outbound", 1),
          ("outboundWithBusy", 2))
    )



class EarlyMediaType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("progress183EarlyMedia", 1),
          ("ringing180", 0))
    )



class Option100relType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("required", 1),
          ("supported", 0))
    )



class KeepAliveModeType(Integer32, TextualConvention):
    status = "current"
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
        *(("clrf", 3),
          ("notify", 2),
          ("off", 0),
          ("options", 1))
    )



class DtmfTransferType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inband", 0),
          ("info", 2),
          ("rfc2833", 1))
    )



class FaxDirectionType(Integer32, TextualConvention):
    status = "current"
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
        *(("callee", 2),
          ("caller", 1),
          ("callerAndCallee", 0),
          ("noDetectFax", 3))
    )



class FaxtransferType(Integer32, TextualConvention):
    status = "current"
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
        *(("g711a", 0),
          ("g711u", 1),
          ("none", 3),
          ("t38", 2))
    )



class FlashtransferType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("info", 2),
          ("off", 0),
          ("rfc2833", 1))
    )



class FlashMimeType(Integer32, TextualConvention):
    status = "current"
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
        *(("broadsoft", 2),
          ("dtmfRelay", 1),
          ("hookflash", 0),
          ("sscc", 3))
    )



class ModemType(Integer32, TextualConvention):
    status = "current"
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
        *(("g711a", 0),
          ("g711aNse", 2),
          ("g711u", 1),
          ("g711uNse", 3),
          ("off", 4))
    )



class GroupType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cyclic", 2),
          ("group", 0),
          ("serial", 1))
    )



class TraceOutputType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("console", 0),
          ("disable", 2),
          ("syslogd", 1))
    )



class ConferenceMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("remote", 1))
    )



# MIB Managed Objects in the order of their OIDs

_PbxConfig_ObjectIdentity = ObjectIdentity
pbxConfig = _PbxConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1)
)
_FxsPorts_ObjectIdentity = ObjectIdentity
fxsPorts = _FxsPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1)
)
_FxsPortsUseFxsProfile_Type = TruthValue
_FxsPortsUseFxsProfile_Object = MibScalar
fxsPortsUseFxsProfile = _FxsPortsUseFxsProfile_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 1),
    _FxsPortsUseFxsProfile_Type()
)
fxsPortsUseFxsProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortsUseFxsProfile.setStatus("current")
_FxsPortTable_Object = MibTable
fxsPortTable = _FxsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2)
)
if mibBuilder.loadTexts:
    fxsPortTable.setStatus("current")
_FxsPortEntry_Object = MibTableRow
fxsPortEntry = _FxsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1)
)
fxsPortEntry.setIndexNames(
    (0, "ELTEX-TAU8", "fxsPortIndex"),
)
if mibBuilder.loadTexts:
    fxsPortEntry.setStatus("current")
_FxsPortIndex_Type = Integer32
_FxsPortIndex_Object = MibTableColumn
fxsPortIndex = _FxsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 1),
    _FxsPortIndex_Type()
)
fxsPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fxsPortIndex.setStatus("current")
_FxsPortEnabled_Type = TruthValue
_FxsPortEnabled_Object = MibTableColumn
fxsPortEnabled = _FxsPortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 2),
    _FxsPortEnabled_Type()
)
fxsPortEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortEnabled.setStatus("current")
_FxsPortSipProfileId_Type = Integer32
_FxsPortSipProfileId_Object = MibTableColumn
fxsPortSipProfileId = _FxsPortSipProfileId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 3),
    _FxsPortSipProfileId_Type()
)
fxsPortSipProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortSipProfileId.setStatus("current")
_FxsPortProfile_Type = Integer32
_FxsPortProfile_Object = MibTableColumn
fxsPortProfile = _FxsPortProfile_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 4),
    _FxsPortProfile_Type()
)
fxsPortProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortProfile.setStatus("current")
_FxsPortPhone_Type = DisplayString
_FxsPortPhone_Object = MibTableColumn
fxsPortPhone = _FxsPortPhone_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 5),
    _FxsPortPhone_Type()
)
fxsPortPhone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortPhone.setStatus("current")
_FxsPortUsername_Type = DisplayString
_FxsPortUsername_Object = MibTableColumn
fxsPortUsername = _FxsPortUsername_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 6),
    _FxsPortUsername_Type()
)
fxsPortUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortUsername.setStatus("current")
_FxsPortAuthName_Type = DisplayString
_FxsPortAuthName_Object = MibTableColumn
fxsPortAuthName = _FxsPortAuthName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 7),
    _FxsPortAuthName_Type()
)
fxsPortAuthName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortAuthName.setStatus("current")
_FxsPortAuthPass_Type = DisplayString
_FxsPortAuthPass_Object = MibTableColumn
fxsPortAuthPass = _FxsPortAuthPass_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 8),
    _FxsPortAuthPass_Type()
)
fxsPortAuthPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortAuthPass.setStatus("current")
_FxsPortSipPort_Type = Integer32
_FxsPortSipPort_Object = MibTableColumn
fxsPortSipPort = _FxsPortSipPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 9),
    _FxsPortSipPort_Type()
)
fxsPortSipPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortSipPort.setStatus("current")
_FxsPortUseAltNumber_Type = TruthValue
_FxsPortUseAltNumber_Object = MibTableColumn
fxsPortUseAltNumber = _FxsPortUseAltNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 10),
    _FxsPortUseAltNumber_Type()
)
fxsPortUseAltNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortUseAltNumber.setStatus("current")
_FxsPortAltNumber_Type = DisplayString
_FxsPortAltNumber_Object = MibTableColumn
fxsPortAltNumber = _FxsPortAltNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 11),
    _FxsPortAltNumber_Type()
)
fxsPortAltNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortAltNumber.setStatus("current")
_FxsPortCpcRus_Type = Integer32
_FxsPortCpcRus_Object = MibTableColumn
fxsPortCpcRus = _FxsPortCpcRus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 12),
    _FxsPortCpcRus_Type()
)
fxsPortCpcRus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortCpcRus.setStatus("current")
_FxsPortMinOnhookTime_Type = Integer32
_FxsPortMinOnhookTime_Object = MibTableColumn
fxsPortMinOnhookTime = _FxsPortMinOnhookTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 13),
    _FxsPortMinOnhookTime_Type()
)
fxsPortMinOnhookTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortMinOnhookTime.setStatus("current")
_FxsPortMinFlash_Type = Integer32
_FxsPortMinFlash_Object = MibTableColumn
fxsPortMinFlash = _FxsPortMinFlash_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 14),
    _FxsPortMinFlash_Type()
)
fxsPortMinFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortMinFlash.setStatus("current")
_FxsPortGainR_Type = Integer32
_FxsPortGainR_Object = MibTableColumn
fxsPortGainR = _FxsPortGainR_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 15),
    _FxsPortGainR_Type()
)
fxsPortGainR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortGainR.setStatus("current")
_FxsPortGainT_Type = Integer32
_FxsPortGainT_Object = MibTableColumn
fxsPortGainT = _FxsPortGainT_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 16),
    _FxsPortGainT_Type()
)
fxsPortGainT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortGainT.setStatus("current")
_FxsPortMinPulse_Type = Integer32
_FxsPortMinPulse_Object = MibTableColumn
fxsPortMinPulse = _FxsPortMinPulse_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 17),
    _FxsPortMinPulse_Type()
)
fxsPortMinPulse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortMinPulse.setStatus("current")
_FxsPortInterdigit_Type = Integer32
_FxsPortInterdigit_Object = MibTableColumn
fxsPortInterdigit = _FxsPortInterdigit_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 18),
    _FxsPortInterdigit_Type()
)
fxsPortInterdigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortInterdigit.setStatus("current")
_FxsPortCallerId_Type = CallerIdType
_FxsPortCallerId_Object = MibTableColumn
fxsPortCallerId = _FxsPortCallerId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 19),
    _FxsPortCallerId_Type()
)
fxsPortCallerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortCallerId.setStatus("current")
_FxsPortHangupTimeout_Type = Integer32
_FxsPortHangupTimeout_Object = MibTableColumn
fxsPortHangupTimeout = _FxsPortHangupTimeout_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 20),
    _FxsPortHangupTimeout_Type()
)
fxsPortHangupTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortHangupTimeout.setStatus("current")
_FxsPortRbTimeout_Type = Integer32
_FxsPortRbTimeout_Object = MibTableColumn
fxsPortRbTimeout = _FxsPortRbTimeout_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 21),
    _FxsPortRbTimeout_Type()
)
fxsPortRbTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortRbTimeout.setStatus("current")
_FxsPortBusyTimeout_Type = Integer32
_FxsPortBusyTimeout_Object = MibTableColumn
fxsPortBusyTimeout = _FxsPortBusyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 22),
    _FxsPortBusyTimeout_Type()
)
fxsPortBusyTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortBusyTimeout.setStatus("current")
_FxsPortPolarityReverse_Type = TruthValue
_FxsPortPolarityReverse_Object = MibTableColumn
fxsPortPolarityReverse = _FxsPortPolarityReverse_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 23),
    _FxsPortPolarityReverse_Type()
)
fxsPortPolarityReverse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortPolarityReverse.setStatus("current")
_FxsPortCallTransfer_Type = CallTransferType
_FxsPortCallTransfer_Object = MibTableColumn
fxsPortCallTransfer = _FxsPortCallTransfer_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 24),
    _FxsPortCallTransfer_Type()
)
fxsPortCallTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortCallTransfer.setStatus("current")
_FxsPortCallWaiting_Type = TruthValue
_FxsPortCallWaiting_Object = MibTableColumn
fxsPortCallWaiting = _FxsPortCallWaiting_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 25),
    _FxsPortCallWaiting_Type()
)
fxsPortCallWaiting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortCallWaiting.setStatus("current")
_FxsPortDirectnumber_Type = DisplayString
_FxsPortDirectnumber_Object = MibTableColumn
fxsPortDirectnumber = _FxsPortDirectnumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 26),
    _FxsPortDirectnumber_Type()
)
fxsPortDirectnumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortDirectnumber.setStatus("current")
_FxsPortStopDial_Type = TruthValue
_FxsPortStopDial_Object = MibTableColumn
fxsPortStopDial = _FxsPortStopDial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 27),
    _FxsPortStopDial_Type()
)
fxsPortStopDial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortStopDial.setStatus("current")
_FxsPortHotLine_Type = TruthValue
_FxsPortHotLine_Object = MibTableColumn
fxsPortHotLine = _FxsPortHotLine_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 28),
    _FxsPortHotLine_Type()
)
fxsPortHotLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortHotLine.setStatus("current")
_FxsPortHotNumber_Type = DisplayString
_FxsPortHotNumber_Object = MibTableColumn
fxsPortHotNumber = _FxsPortHotNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 29),
    _FxsPortHotNumber_Type()
)
fxsPortHotNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortHotNumber.setStatus("current")
_FxsPortHotTimeout_Type = Integer32
_FxsPortHotTimeout_Object = MibTableColumn
fxsPortHotTimeout = _FxsPortHotTimeout_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 30),
    _FxsPortHotTimeout_Type()
)
fxsPortHotTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortHotTimeout.setStatus("current")
_FxsPortCtUnconditional_Type = TruthValue
_FxsPortCtUnconditional_Object = MibTableColumn
fxsPortCtUnconditional = _FxsPortCtUnconditional_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 31),
    _FxsPortCtUnconditional_Type()
)
fxsPortCtUnconditional.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortCtUnconditional.setStatus("current")
_FxsPortCfuNumber_Type = DisplayString
_FxsPortCfuNumber_Object = MibTableColumn
fxsPortCfuNumber = _FxsPortCfuNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 32),
    _FxsPortCfuNumber_Type()
)
fxsPortCfuNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortCfuNumber.setStatus("current")
_FxsPortCtBusy_Type = TruthValue
_FxsPortCtBusy_Object = MibTableColumn
fxsPortCtBusy = _FxsPortCtBusy_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 33),
    _FxsPortCtBusy_Type()
)
fxsPortCtBusy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortCtBusy.setStatus("current")
_FxsPortCfbNumber_Type = DisplayString
_FxsPortCfbNumber_Object = MibTableColumn
fxsPortCfbNumber = _FxsPortCfbNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 34),
    _FxsPortCfbNumber_Type()
)
fxsPortCfbNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortCfbNumber.setStatus("current")
_FxsPortCtNoanswer_Type = TruthValue
_FxsPortCtNoanswer_Object = MibTableColumn
fxsPortCtNoanswer = _FxsPortCtNoanswer_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 35),
    _FxsPortCtNoanswer_Type()
)
fxsPortCtNoanswer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortCtNoanswer.setStatus("current")
_FxsPortCfnaNumber_Type = DisplayString
_FxsPortCfnaNumber_Object = MibTableColumn
fxsPortCfnaNumber = _FxsPortCfnaNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 36),
    _FxsPortCfnaNumber_Type()
)
fxsPortCfnaNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortCfnaNumber.setStatus("current")
_FxsPortCtTimeout_Type = Integer32
_FxsPortCtTimeout_Object = MibTableColumn
fxsPortCtTimeout = _FxsPortCtTimeout_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 37),
    _FxsPortCtTimeout_Type()
)
fxsPortCtTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortCtTimeout.setStatus("current")
_FxsPortDndEnable_Type = TruthValue
_FxsPortDndEnable_Object = MibTableColumn
fxsPortDndEnable = _FxsPortDndEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 38),
    _FxsPortDndEnable_Type()
)
fxsPortDndEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortDndEnable.setStatus("current")
_FxsPortRowStatus_Type = RowStatus
_FxsPortRowStatus_Object = MibTableColumn
fxsPortRowStatus = _FxsPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 2, 1, 39),
    _FxsPortRowStatus_Type()
)
fxsPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fxsPortRowStatus.setStatus("current")
_FxsPortsMIBBoundary_Type = Integer32
_FxsPortsMIBBoundary_Object = MibScalar
fxsPortsMIBBoundary = _FxsPortsMIBBoundary_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 1, 3),
    _FxsPortsMIBBoundary_Type()
)
fxsPortsMIBBoundary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPortsMIBBoundary.setStatus("current")
_FxsProfiles_ObjectIdentity = ObjectIdentity
fxsProfiles = _FxsProfiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 2)
)
_FxsProfileTable_Object = MibTable
fxsProfileTable = _FxsProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fxsProfileTable.setStatus("current")
_FxsProfileEntry_Object = MibTableRow
fxsProfileEntry = _FxsProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 2, 1, 1)
)
fxsProfileEntry.setIndexNames(
    (0, "ELTEX-TAU8", "fxsProfileIndex"),
)
if mibBuilder.loadTexts:
    fxsProfileEntry.setStatus("current")
_FxsProfileIndex_Type = Integer32
_FxsProfileIndex_Object = MibTableColumn
fxsProfileIndex = _FxsProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 2, 1, 1, 1),
    _FxsProfileIndex_Type()
)
fxsProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fxsProfileIndex.setStatus("current")
_FxsProfileName_Type = DisplayString
_FxsProfileName_Object = MibTableColumn
fxsProfileName = _FxsProfileName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 2, 1, 1, 2),
    _FxsProfileName_Type()
)
fxsProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsProfileName.setStatus("current")
_FxsProfileMinOnhookTime_Type = Integer32
_FxsProfileMinOnhookTime_Object = MibTableColumn
fxsProfileMinOnhookTime = _FxsProfileMinOnhookTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 2, 1, 1, 3),
    _FxsProfileMinOnhookTime_Type()
)
fxsProfileMinOnhookTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsProfileMinOnhookTime.setStatus("current")
_FxsProfileMinFlash_Type = Integer32
_FxsProfileMinFlash_Object = MibTableColumn
fxsProfileMinFlash = _FxsProfileMinFlash_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 2, 1, 1, 4),
    _FxsProfileMinFlash_Type()
)
fxsProfileMinFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsProfileMinFlash.setStatus("current")
_FxsProfileGainR_Type = Integer32
_FxsProfileGainR_Object = MibTableColumn
fxsProfileGainR = _FxsProfileGainR_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 2, 1, 1, 5),
    _FxsProfileGainR_Type()
)
fxsProfileGainR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsProfileGainR.setStatus("current")
_FxsProfileGainT_Type = Integer32
_FxsProfileGainT_Object = MibTableColumn
fxsProfileGainT = _FxsProfileGainT_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 2, 1, 1, 6),
    _FxsProfileGainT_Type()
)
fxsProfileGainT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsProfileGainT.setStatus("current")
_FxsProfileMinPulse_Type = Integer32
_FxsProfileMinPulse_Object = MibTableColumn
fxsProfileMinPulse = _FxsProfileMinPulse_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 2, 1, 1, 7),
    _FxsProfileMinPulse_Type()
)
fxsProfileMinPulse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsProfileMinPulse.setStatus("current")
_FxsProfileInterdigit_Type = Integer32
_FxsProfileInterdigit_Object = MibTableColumn
fxsProfileInterdigit = _FxsProfileInterdigit_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 2, 1, 1, 8),
    _FxsProfileInterdigit_Type()
)
fxsProfileInterdigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsProfileInterdigit.setStatus("current")
_FxsProfileCallerId_Type = CallerIdType
_FxsProfileCallerId_Object = MibTableColumn
fxsProfileCallerId = _FxsProfileCallerId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 2, 1, 1, 9),
    _FxsProfileCallerId_Type()
)
fxsProfileCallerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsProfileCallerId.setStatus("current")
_FxsProfileHangupTimeout_Type = Integer32
_FxsProfileHangupTimeout_Object = MibTableColumn
fxsProfileHangupTimeout = _FxsProfileHangupTimeout_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 2, 1, 1, 10),
    _FxsProfileHangupTimeout_Type()
)
fxsProfileHangupTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsProfileHangupTimeout.setStatus("current")
_FxsProfileRbTimeout_Type = Integer32
_FxsProfileRbTimeout_Object = MibTableColumn
fxsProfileRbTimeout = _FxsProfileRbTimeout_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 2, 1, 1, 11),
    _FxsProfileRbTimeout_Type()
)
fxsProfileRbTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsProfileRbTimeout.setStatus("current")
_FxsProfileBusyTimeout_Type = Integer32
_FxsProfileBusyTimeout_Object = MibTableColumn
fxsProfileBusyTimeout = _FxsProfileBusyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 2, 1, 1, 12),
    _FxsProfileBusyTimeout_Type()
)
fxsProfileBusyTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsProfileBusyTimeout.setStatus("current")
_FxsProfilePolarityReverse_Type = TruthValue
_FxsProfilePolarityReverse_Object = MibTableColumn
fxsProfilePolarityReverse = _FxsProfilePolarityReverse_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 2, 1, 1, 13),
    _FxsProfilePolarityReverse_Type()
)
fxsProfilePolarityReverse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsProfilePolarityReverse.setStatus("current")
_FxsProfileRowStatus_Type = RowStatus
_FxsProfileRowStatus_Object = MibTableColumn
fxsProfileRowStatus = _FxsProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 2, 1, 1, 14),
    _FxsProfileRowStatus_Type()
)
fxsProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fxsProfileRowStatus.setStatus("current")
_FxsProfilesMIBBoundary_Type = Integer32
_FxsProfilesMIBBoundary_Object = MibScalar
fxsProfilesMIBBoundary = _FxsProfilesMIBBoundary_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 2, 2),
    _FxsProfilesMIBBoundary_Type()
)
fxsProfilesMIBBoundary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsProfilesMIBBoundary.setStatus("current")
_SipConfig_ObjectIdentity = ObjectIdentity
sipConfig = _SipConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3)
)
_SipCommon_ObjectIdentity = ObjectIdentity
sipCommon = _SipCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 1)
)
_SipCommonStunEnable_Type = TruthValue
_SipCommonStunEnable_Object = MibScalar
sipCommonStunEnable = _SipCommonStunEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 1, 1),
    _SipCommonStunEnable_Type()
)
sipCommonStunEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipCommonStunEnable.setStatus("current")
_SipCommonStunServer_Type = DisplayString
_SipCommonStunServer_Object = MibScalar
sipCommonStunServer = _SipCommonStunServer_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 1, 2),
    _SipCommonStunServer_Type()
)
sipCommonStunServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipCommonStunServer.setStatus("current")
_SipCommonStunInterval_Type = Integer32
_SipCommonStunInterval_Object = MibScalar
sipCommonStunInterval = _SipCommonStunInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 1, 3),
    _SipCommonStunInterval_Type()
)
sipCommonStunInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipCommonStunInterval.setStatus("current")
_SipCommonPublicIp_Type = DisplayString
_SipCommonPublicIp_Object = MibScalar
sipCommonPublicIp = _SipCommonPublicIp_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 1, 4),
    _SipCommonPublicIp_Type()
)
sipCommonPublicIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipCommonPublicIp.setStatus("current")
_SipCommonNotUseNAPTR_Type = TruthValue
_SipCommonNotUseNAPTR_Object = MibScalar
sipCommonNotUseNAPTR = _SipCommonNotUseNAPTR_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 1, 5),
    _SipCommonNotUseNAPTR_Type()
)
sipCommonNotUseNAPTR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipCommonNotUseNAPTR.setStatus("current")
_SipCommonNotUseSRV_Type = TruthValue
_SipCommonNotUseSRV_Object = MibScalar
sipCommonNotUseSRV = _SipCommonNotUseSRV_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 1, 6),
    _SipCommonNotUseSRV_Type()
)
sipCommonNotUseSRV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipCommonNotUseSRV.setStatus("current")
_SipProfileTable_Object = MibTable
sipProfileTable = _SipProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2)
)
if mibBuilder.loadTexts:
    sipProfileTable.setStatus("current")
_SipProfileEntry_Object = MibTableRow
sipProfileEntry = _SipProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1)
)
sipProfileEntry.setIndexNames(
    (0, "ELTEX-TAU8", "sipProfileIndex"),
)
if mibBuilder.loadTexts:
    sipProfileEntry.setStatus("current")
_SipProfileIndex_Type = Integer32
_SipProfileIndex_Object = MibTableColumn
sipProfileIndex = _SipProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 1),
    _SipProfileIndex_Type()
)
sipProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sipProfileIndex.setStatus("current")
_SipProfileName_Type = DisplayString
_SipProfileName_Object = MibTableColumn
sipProfileName = _SipProfileName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 2),
    _SipProfileName_Type()
)
sipProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileName.setStatus("current")
_SipProEnablesip_Type = TruthValue
_SipProEnablesip_Object = MibTableColumn
sipProEnablesip = _SipProEnablesip_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 3),
    _SipProEnablesip_Type()
)
sipProEnablesip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProEnablesip.setStatus("current")
_SipProRsrvMode_Type = RsrvModeType
_SipProRsrvMode_Object = MibTableColumn
sipProRsrvMode = _SipProRsrvMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 4),
    _SipProRsrvMode_Type()
)
sipProRsrvMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProRsrvMode.setStatus("current")
_SipProProxyip_Type = DisplayString
_SipProProxyip_Object = MibTableColumn
sipProProxyip = _SipProProxyip_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 5),
    _SipProProxyip_Type()
)
sipProProxyip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProProxyip.setStatus("current")
_SipProRegistration_Type = TruthValue
_SipProRegistration_Object = MibTableColumn
sipProRegistration = _SipProRegistration_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 6),
    _SipProRegistration_Type()
)
sipProRegistration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProRegistration.setStatus("current")
_SipProRegistrarip_Type = DisplayString
_SipProRegistrarip_Object = MibTableColumn
sipProRegistrarip = _SipProRegistrarip_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 7),
    _SipProRegistrarip_Type()
)
sipProRegistrarip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProRegistrarip.setStatus("current")
_SipProProxyipRsrv1_Type = DisplayString
_SipProProxyipRsrv1_Object = MibTableColumn
sipProProxyipRsrv1 = _SipProProxyipRsrv1_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 8),
    _SipProProxyipRsrv1_Type()
)
sipProProxyipRsrv1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProProxyipRsrv1.setStatus("current")
_SipProRegistrationRsrv1_Type = TruthValue
_SipProRegistrationRsrv1_Object = MibTableColumn
sipProRegistrationRsrv1 = _SipProRegistrationRsrv1_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 9),
    _SipProRegistrationRsrv1_Type()
)
sipProRegistrationRsrv1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProRegistrationRsrv1.setStatus("current")
_SipProRegistraripRsrv1_Type = DisplayString
_SipProRegistraripRsrv1_Object = MibTableColumn
sipProRegistraripRsrv1 = _SipProRegistraripRsrv1_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 10),
    _SipProRegistraripRsrv1_Type()
)
sipProRegistraripRsrv1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProRegistraripRsrv1.setStatus("current")
_SipProProxyipRsrv2_Type = DisplayString
_SipProProxyipRsrv2_Object = MibTableColumn
sipProProxyipRsrv2 = _SipProProxyipRsrv2_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 11),
    _SipProProxyipRsrv2_Type()
)
sipProProxyipRsrv2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProProxyipRsrv2.setStatus("current")
_SipProRegistrationRsrv2_Type = TruthValue
_SipProRegistrationRsrv2_Object = MibTableColumn
sipProRegistrationRsrv2 = _SipProRegistrationRsrv2_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 12),
    _SipProRegistrationRsrv2_Type()
)
sipProRegistrationRsrv2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProRegistrationRsrv2.setStatus("current")
_SipProRegistraripRsrv2_Type = DisplayString
_SipProRegistraripRsrv2_Object = MibTableColumn
sipProRegistraripRsrv2 = _SipProRegistraripRsrv2_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 13),
    _SipProRegistraripRsrv2_Type()
)
sipProRegistraripRsrv2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProRegistraripRsrv2.setStatus("current")
_SipProProxyipRsrv3_Type = DisplayString
_SipProProxyipRsrv3_Object = MibTableColumn
sipProProxyipRsrv3 = _SipProProxyipRsrv3_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 14),
    _SipProProxyipRsrv3_Type()
)
sipProProxyipRsrv3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProProxyipRsrv3.setStatus("current")
_SipProRegistrationRsrv3_Type = TruthValue
_SipProRegistrationRsrv3_Object = MibTableColumn
sipProRegistrationRsrv3 = _SipProRegistrationRsrv3_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 15),
    _SipProRegistrationRsrv3_Type()
)
sipProRegistrationRsrv3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProRegistrationRsrv3.setStatus("current")
_SipProRegistraripRsrv3_Type = DisplayString
_SipProRegistraripRsrv3_Object = MibTableColumn
sipProRegistraripRsrv3 = _SipProRegistraripRsrv3_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 16),
    _SipProRegistraripRsrv3_Type()
)
sipProRegistraripRsrv3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProRegistraripRsrv3.setStatus("current")
_SipProProxyipRsrv4_Type = DisplayString
_SipProProxyipRsrv4_Object = MibTableColumn
sipProProxyipRsrv4 = _SipProProxyipRsrv4_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 17),
    _SipProProxyipRsrv4_Type()
)
sipProProxyipRsrv4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProProxyipRsrv4.setStatus("current")
_SipProRegistrationRsrv4_Type = TruthValue
_SipProRegistrationRsrv4_Object = MibTableColumn
sipProRegistrationRsrv4 = _SipProRegistrationRsrv4_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 18),
    _SipProRegistrationRsrv4_Type()
)
sipProRegistrationRsrv4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProRegistrationRsrv4.setStatus("current")
_SipProRegistraripRsrv4_Type = DisplayString
_SipProRegistraripRsrv4_Object = MibTableColumn
sipProRegistraripRsrv4 = _SipProRegistraripRsrv4_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 19),
    _SipProRegistraripRsrv4_Type()
)
sipProRegistraripRsrv4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProRegistraripRsrv4.setStatus("current")
_SipProRsrvCheckMethod_Type = RsrvCheckMethodType
_SipProRsrvCheckMethod_Object = MibTableColumn
sipProRsrvCheckMethod = _SipProRsrvCheckMethod_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 20),
    _SipProRsrvCheckMethod_Type()
)
sipProRsrvCheckMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProRsrvCheckMethod.setStatus("current")
_SipProRsrvKeepaliveTime_Type = Integer32
_SipProRsrvKeepaliveTime_Object = MibTableColumn
sipProRsrvKeepaliveTime = _SipProRsrvKeepaliveTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 21),
    _SipProRsrvKeepaliveTime_Type()
)
sipProRsrvKeepaliveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProRsrvKeepaliveTime.setStatus("current")
_SipProDomain_Type = DisplayString
_SipProDomain_Object = MibTableColumn
sipProDomain = _SipProDomain_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 22),
    _SipProDomain_Type()
)
sipProDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProDomain.setStatus("current")
_SipProOutbound_Type = OutboundType
_SipProOutbound_Object = MibTableColumn
sipProOutbound = _SipProOutbound_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 23),
    _SipProOutbound_Type()
)
sipProOutbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProOutbound.setStatus("current")
_SipProExpires_Type = Integer32
_SipProExpires_Object = MibTableColumn
sipProExpires = _SipProExpires_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 24),
    _SipProExpires_Type()
)
sipProExpires.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProExpires.setStatus("current")
_SipProRri_Type = Integer32
_SipProRri_Object = MibTableColumn
sipProRri = _SipProRri_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 25),
    _SipProRri_Type()
)
sipProRri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProRri.setStatus("current")
_SipProDomainToReg_Type = TruthValue
_SipProDomainToReg_Object = MibTableColumn
sipProDomainToReg = _SipProDomainToReg_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 26),
    _SipProDomainToReg_Type()
)
sipProDomainToReg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProDomainToReg.setStatus("current")
_SipProEarlyMedia_Type = EarlyMediaType
_SipProEarlyMedia_Object = MibTableColumn
sipProEarlyMedia = _SipProEarlyMedia_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 27),
    _SipProEarlyMedia_Type()
)
sipProEarlyMedia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProEarlyMedia.setStatus("current")
_SipProDisplayToReg_Type = TruthValue
_SipProDisplayToReg_Object = MibTableColumn
sipProDisplayToReg = _SipProDisplayToReg_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 28),
    _SipProDisplayToReg_Type()
)
sipProDisplayToReg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProDisplayToReg.setStatus("current")
_SipProRingback_Type = TruthValue
_SipProRingback_Object = MibTableColumn
sipProRingback = _SipProRingback_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 29),
    _SipProRingback_Type()
)
sipProRingback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProRingback.setStatus("current")
_SipProReduceSdpMediaCount_Type = TruthValue
_SipProReduceSdpMediaCount_Object = MibTableColumn
sipProReduceSdpMediaCount = _SipProReduceSdpMediaCount_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 30),
    _SipProReduceSdpMediaCount_Type()
)
sipProReduceSdpMediaCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProReduceSdpMediaCount.setStatus("current")
_SipProOption100rel_Type = Option100relType
_SipProOption100rel_Object = MibTableColumn
sipProOption100rel = _SipProOption100rel_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 31),
    _SipProOption100rel_Type()
)
sipProOption100rel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProOption100rel.setStatus("current")
_SipProCodecOrder_Type = DisplayString
_SipProCodecOrder_Object = MibTableColumn
sipProCodecOrder = _SipProCodecOrder_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 32),
    _SipProCodecOrder_Type()
)
sipProCodecOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProCodecOrder.setStatus("current")
_SipProG711pte_Type = Integer32
_SipProG711pte_Object = MibTableColumn
sipProG711pte = _SipProG711pte_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 33),
    _SipProG711pte_Type()
)
sipProG711pte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProG711pte.setStatus("current")
_SipProDtmfTransfer_Type = DtmfTransferType
_SipProDtmfTransfer_Object = MibTableColumn
sipProDtmfTransfer = _SipProDtmfTransfer_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 34),
    _SipProDtmfTransfer_Type()
)
sipProDtmfTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProDtmfTransfer.setStatus("current")
_SipProFaxDirection_Type = FaxDirectionType
_SipProFaxDirection_Object = MibTableColumn
sipProFaxDirection = _SipProFaxDirection_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 35),
    _SipProFaxDirection_Type()
)
sipProFaxDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProFaxDirection.setStatus("current")
_SipProFaxTransfer1_Type = FaxtransferType
_SipProFaxTransfer1_Object = MibTableColumn
sipProFaxTransfer1 = _SipProFaxTransfer1_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 36),
    _SipProFaxTransfer1_Type()
)
sipProFaxTransfer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProFaxTransfer1.setStatus("current")
_SipProFaxTransfer2_Type = FaxtransferType
_SipProFaxTransfer2_Object = MibTableColumn
sipProFaxTransfer2 = _SipProFaxTransfer2_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 37),
    _SipProFaxTransfer2_Type()
)
sipProFaxTransfer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProFaxTransfer2.setStatus("current")
_SipProFaxTransfer3_Type = FaxtransferType
_SipProFaxTransfer3_Object = MibTableColumn
sipProFaxTransfer3 = _SipProFaxTransfer3_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 38),
    _SipProFaxTransfer3_Type()
)
sipProFaxTransfer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProFaxTransfer3.setStatus("current")
_SipProEnableInT38_Type = TruthValue
_SipProEnableInT38_Object = MibTableColumn
sipProEnableInT38 = _SipProEnableInT38_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 39),
    _SipProEnableInT38_Type()
)
sipProEnableInT38.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProEnableInT38.setStatus("current")
_SipProFlashTransfer_Type = FlashtransferType
_SipProFlashTransfer_Object = MibTableColumn
sipProFlashTransfer = _SipProFlashTransfer_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 40),
    _SipProFlashTransfer_Type()
)
sipProFlashTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProFlashTransfer.setStatus("current")
_SipProFlashMime_Type = FlashMimeType
_SipProFlashMime_Object = MibTableColumn
sipProFlashMime = _SipProFlashMime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 41),
    _SipProFlashMime_Type()
)
sipProFlashMime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProFlashMime.setStatus("current")
_SipProModem_Type = ModemType
_SipProModem_Object = MibTableColumn
sipProModem = _SipProModem_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 42),
    _SipProModem_Type()
)
sipProModem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProModem.setStatus("current")
_SipProPayload_Type = Integer32
_SipProPayload_Object = MibTableColumn
sipProPayload = _SipProPayload_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 43),
    _SipProPayload_Type()
)
sipProPayload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProPayload.setStatus("current")
_SipProSilenceDetector_Type = TruthValue
_SipProSilenceDetector_Object = MibTableColumn
sipProSilenceDetector = _SipProSilenceDetector_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 44),
    _SipProSilenceDetector_Type()
)
sipProSilenceDetector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProSilenceDetector.setStatus("current")
_SipProEchoCanceler_Type = TruthValue
_SipProEchoCanceler_Object = MibTableColumn
sipProEchoCanceler = _SipProEchoCanceler_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 45),
    _SipProEchoCanceler_Type()
)
sipProEchoCanceler.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProEchoCanceler.setStatus("current")
_SipProRtcp_Type = TruthValue
_SipProRtcp_Object = MibTableColumn
sipProRtcp = _SipProRtcp_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 46),
    _SipProRtcp_Type()
)
sipProRtcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProRtcp.setStatus("current")
_SipProRtcpTimer_Type = Integer32
_SipProRtcpTimer_Object = MibTableColumn
sipProRtcpTimer = _SipProRtcpTimer_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 47),
    _SipProRtcpTimer_Type()
)
sipProRtcpTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProRtcpTimer.setStatus("current")
_SipProRtcpCount_Type = Integer32
_SipProRtcpCount_Object = MibTableColumn
sipProRtcpCount = _SipProRtcpCount_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 48),
    _SipProRtcpCount_Type()
)
sipProRtcpCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProRtcpCount.setStatus("current")
_SipProDialplanRegexp_Type = DisplayString
_SipProDialplanRegexp_Object = MibTableColumn
sipProDialplanRegexp = _SipProDialplanRegexp_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 49),
    _SipProDialplanRegexp_Type()
)
sipProDialplanRegexp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProDialplanRegexp.setStatus("current")
_SipProRowStatus_Type = RowStatus
_SipProRowStatus_Object = MibTableColumn
sipProRowStatus = _SipProRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 50),
    _SipProRowStatus_Type()
)
sipProRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProRowStatus.setStatus("current")
_SipProKeepAliveMode_Type = KeepAliveModeType
_SipProKeepAliveMode_Object = MibTableColumn
sipProKeepAliveMode = _SipProKeepAliveMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 51),
    _SipProKeepAliveMode_Type()
)
sipProKeepAliveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProKeepAliveMode.setStatus("current")
_SipProKeepAliveInterval_Type = Integer32
_SipProKeepAliveInterval_Object = MibTableColumn
sipProKeepAliveInterval = _SipProKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 52),
    _SipProKeepAliveInterval_Type()
)
sipProKeepAliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProKeepAliveInterval.setStatus("current")
_SipProConferenceMode_Type = ConferenceMode
_SipProConferenceMode_Object = MibTableColumn
sipProConferenceMode = _SipProConferenceMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 53),
    _SipProConferenceMode_Type()
)
sipProConferenceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProConferenceMode.setStatus("current")
_SipProConferenceServer_Type = DisplayString
_SipProConferenceServer_Object = MibTableColumn
sipProConferenceServer = _SipProConferenceServer_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 54),
    _SipProConferenceServer_Type()
)
sipProConferenceServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProConferenceServer.setStatus("current")
_SipProImsEnable_Type = TruthValue
_SipProImsEnable_Object = MibTableColumn
sipProImsEnable = _SipProImsEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 55),
    _SipProImsEnable_Type()
)
sipProImsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProImsEnable.setStatus("current")
_SipProXcapCallholdName_Type = DisplayString
_SipProXcapCallholdName_Object = MibTableColumn
sipProXcapCallholdName = _SipProXcapCallholdName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 56),
    _SipProXcapCallholdName_Type()
)
sipProXcapCallholdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProXcapCallholdName.setStatus("current")
_SipProXcapCwName_Type = DisplayString
_SipProXcapCwName_Object = MibTableColumn
sipProXcapCwName = _SipProXcapCwName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 57),
    _SipProXcapCwName_Type()
)
sipProXcapCwName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProXcapCwName.setStatus("current")
_SipProXcapConferenceName_Type = DisplayString
_SipProXcapConferenceName_Object = MibTableColumn
sipProXcapConferenceName = _SipProXcapConferenceName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 58),
    _SipProXcapConferenceName_Type()
)
sipProXcapConferenceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProXcapConferenceName.setStatus("current")
_SipProXcapHotlineName_Type = DisplayString
_SipProXcapHotlineName_Object = MibTableColumn
sipProXcapHotlineName = _SipProXcapHotlineName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 2, 1, 59),
    _SipProXcapHotlineName_Type()
)
sipProXcapHotlineName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProXcapHotlineName.setStatus("current")
_SipProfilesMIBBoundary_Type = Integer32
_SipProfilesMIBBoundary_Object = MibScalar
sipProfilesMIBBoundary = _SipProfilesMIBBoundary_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 3, 3),
    _SipProfilesMIBBoundary_Type()
)
sipProfilesMIBBoundary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipProfilesMIBBoundary.setStatus("current")
_GroupsConfig_ObjectIdentity = ObjectIdentity
groupsConfig = _GroupsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 4)
)
_HuntGroupTable_Object = MibTable
huntGroupTable = _HuntGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 4, 1)
)
if mibBuilder.loadTexts:
    huntGroupTable.setStatus("current")
_HuntGroupEntry_Object = MibTableRow
huntGroupEntry = _HuntGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 4, 1, 1)
)
huntGroupEntry.setIndexNames(
    (0, "ELTEX-TAU8", "huntGrIndex"),
)
if mibBuilder.loadTexts:
    huntGroupEntry.setStatus("current")
_HuntGrIndex_Type = Integer32
_HuntGrIndex_Object = MibTableColumn
huntGrIndex = _HuntGrIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 4, 1, 1, 1),
    _HuntGrIndex_Type()
)
huntGrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    huntGrIndex.setStatus("current")
_HuntGrEnable_Type = TruthValue
_HuntGrEnable_Object = MibTableColumn
huntGrEnable = _HuntGrEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 4, 1, 1, 2),
    _HuntGrEnable_Type()
)
huntGrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    huntGrEnable.setStatus("current")
_HuntGroupName_Type = DisplayString
_HuntGroupName_Object = MibTableColumn
huntGroupName = _HuntGroupName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 4, 1, 1, 3),
    _HuntGroupName_Type()
)
huntGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    huntGroupName.setStatus("current")
_HuntGrSipProfileId_Type = Integer32
_HuntGrSipProfileId_Object = MibTableColumn
huntGrSipProfileId = _HuntGrSipProfileId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 4, 1, 1, 4),
    _HuntGrSipProfileId_Type()
)
huntGrSipProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    huntGrSipProfileId.setStatus("current")
_HuntGrPhone_Type = DisplayString
_HuntGrPhone_Object = MibTableColumn
huntGrPhone = _HuntGrPhone_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 4, 1, 1, 5),
    _HuntGrPhone_Type()
)
huntGrPhone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    huntGrPhone.setStatus("current")
_HuntGrRegistration_Type = TruthValue
_HuntGrRegistration_Object = MibTableColumn
huntGrRegistration = _HuntGrRegistration_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 4, 1, 1, 6),
    _HuntGrRegistration_Type()
)
huntGrRegistration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    huntGrRegistration.setStatus("current")
_HuntGrUserName_Type = DisplayString
_HuntGrUserName_Object = MibTableColumn
huntGrUserName = _HuntGrUserName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 4, 1, 1, 7),
    _HuntGrUserName_Type()
)
huntGrUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    huntGrUserName.setStatus("current")
_HuntGrPassword_Type = DisplayString
_HuntGrPassword_Object = MibTableColumn
huntGrPassword = _HuntGrPassword_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 4, 1, 1, 8),
    _HuntGrPassword_Type()
)
huntGrPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    huntGrPassword.setStatus("current")
_HuntGrType_Type = GroupType
_HuntGrType_Object = MibTableColumn
huntGrType = _HuntGrType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 4, 1, 1, 9),
    _HuntGrType_Type()
)
huntGrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    huntGrType.setStatus("current")
_HuntGrCallQueueSize_Type = Integer32
_HuntGrCallQueueSize_Object = MibTableColumn
huntGrCallQueueSize = _HuntGrCallQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 4, 1, 1, 10),
    _HuntGrCallQueueSize_Type()
)
huntGrCallQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    huntGrCallQueueSize.setStatus("current")
_HuntGrWaitingTime_Type = Integer32
_HuntGrWaitingTime_Object = MibTableColumn
huntGrWaitingTime = _HuntGrWaitingTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 4, 1, 1, 11),
    _HuntGrWaitingTime_Type()
)
huntGrWaitingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    huntGrWaitingTime.setStatus("current")
_HuntGrSipPort_Type = Integer32
_HuntGrSipPort_Object = MibTableColumn
huntGrSipPort = _HuntGrSipPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 4, 1, 1, 12),
    _HuntGrSipPort_Type()
)
huntGrSipPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    huntGrSipPort.setStatus("current")
_HuntGrPickupEnable_Type = TruthValue
_HuntGrPickupEnable_Object = MibTableColumn
huntGrPickupEnable = _HuntGrPickupEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 4, 1, 1, 13),
    _HuntGrPickupEnable_Type()
)
huntGrPickupEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    huntGrPickupEnable.setStatus("current")
_HuntGrPorts_Type = DisplayString
_HuntGrPorts_Object = MibTableColumn
huntGrPorts = _HuntGrPorts_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 4, 1, 1, 14),
    _HuntGrPorts_Type()
)
huntGrPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    huntGrPorts.setStatus("current")
_HuntGrRowStatus_Type = RowStatus
_HuntGrRowStatus_Object = MibTableColumn
huntGrRowStatus = _HuntGrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 4, 1, 1, 15),
    _HuntGrRowStatus_Type()
)
huntGrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    huntGrRowStatus.setStatus("current")
_HuntGroupsMIBBoundary_Type = Integer32
_HuntGroupsMIBBoundary_Object = MibScalar
huntGroupsMIBBoundary = _HuntGroupsMIBBoundary_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 4, 2),
    _HuntGroupsMIBBoundary_Type()
)
huntGroupsMIBBoundary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    huntGroupsMIBBoundary.setStatus("current")
_SuppServices_ObjectIdentity = ObjectIdentity
suppServices = _SuppServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 5)
)
_DvoCfuPrefix_Type = DisplayString
_DvoCfuPrefix_Object = MibScalar
dvoCfuPrefix = _DvoCfuPrefix_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 5, 1),
    _DvoCfuPrefix_Type()
)
dvoCfuPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvoCfuPrefix.setStatus("current")
_DvoCfbPrefix_Type = DisplayString
_DvoCfbPrefix_Object = MibScalar
dvoCfbPrefix = _DvoCfbPrefix_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 5, 2),
    _DvoCfbPrefix_Type()
)
dvoCfbPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvoCfbPrefix.setStatus("current")
_DvoCfnaPrefix_Type = DisplayString
_DvoCfnaPrefix_Object = MibScalar
dvoCfnaPrefix = _DvoCfnaPrefix_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 5, 3),
    _DvoCfnaPrefix_Type()
)
dvoCfnaPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvoCfnaPrefix.setStatus("current")
_DvoCallPickupPrefix_Type = DisplayString
_DvoCallPickupPrefix_Object = MibScalar
dvoCallPickupPrefix = _DvoCallPickupPrefix_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 5, 4),
    _DvoCallPickupPrefix_Type()
)
dvoCallPickupPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvoCallPickupPrefix.setStatus("current")
_DvoHotNumberPrefix_Type = DisplayString
_DvoHotNumberPrefix_Object = MibScalar
dvoHotNumberPrefix = _DvoHotNumberPrefix_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 5, 5),
    _DvoHotNumberPrefix_Type()
)
dvoHotNumberPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvoHotNumberPrefix.setStatus("current")
_DvoCallwaitingPrefix_Type = DisplayString
_DvoCallwaitingPrefix_Object = MibScalar
dvoCallwaitingPrefix = _DvoCallwaitingPrefix_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 5, 6),
    _DvoCallwaitingPrefix_Type()
)
dvoCallwaitingPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvoCallwaitingPrefix.setStatus("current")
_DvoDndPrefix_Type = DisplayString
_DvoDndPrefix_Object = MibScalar
dvoDndPrefix = _DvoDndPrefix_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 1, 5, 7),
    _DvoDndPrefix_Type()
)
dvoDndPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvoDndPrefix.setStatus("current")
_NetworkConfig_ObjectIdentity = ObjectIdentity
networkConfig = _NetworkConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 2)
)
_SnmpConfig_ObjectIdentity = ObjectIdentity
snmpConfig = _SnmpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 2, 1)
)
_SnmpRoCommunity_Type = DisplayString
_SnmpRoCommunity_Object = MibScalar
snmpRoCommunity = _SnmpRoCommunity_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 2, 1, 1),
    _SnmpRoCommunity_Type()
)
snmpRoCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpRoCommunity.setStatus("current")
_SnmpRwCommunity_Type = DisplayString
_SnmpRwCommunity_Object = MibScalar
snmpRwCommunity = _SnmpRwCommunity_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 2, 1, 2),
    _SnmpRwCommunity_Type()
)
snmpRwCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpRwCommunity.setStatus("current")
_SnmpTrapsink_Type = DisplayString
_SnmpTrapsink_Object = MibScalar
snmpTrapsink = _SnmpTrapsink_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 2, 1, 3),
    _SnmpTrapsink_Type()
)
snmpTrapsink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapsink.setStatus("current")
_SnmpTrap2sink_Type = DisplayString
_SnmpTrap2sink_Object = MibScalar
snmpTrap2sink = _SnmpTrap2sink_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 2, 1, 4),
    _SnmpTrap2sink_Type()
)
snmpTrap2sink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrap2sink.setStatus("current")
_SnmpInformsink_Type = DisplayString
_SnmpInformsink_Object = MibScalar
snmpInformsink = _SnmpInformsink_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 2, 1, 5),
    _SnmpInformsink_Type()
)
snmpInformsink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpInformsink.setStatus("current")
_SnmpSysname_Type = DisplayString
_SnmpSysname_Object = MibScalar
snmpSysname = _SnmpSysname_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 2, 1, 6),
    _SnmpSysname_Type()
)
snmpSysname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSysname.setStatus("current")
_SnmpSyscontact_Type = DisplayString
_SnmpSyscontact_Object = MibScalar
snmpSyscontact = _SnmpSyscontact_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 2, 1, 7),
    _SnmpSyscontact_Type()
)
snmpSyscontact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSyscontact.setStatus("current")
_SnmpSyslocation_Type = DisplayString
_SnmpSyslocation_Object = MibScalar
snmpSyslocation = _SnmpSyslocation_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 2, 1, 8),
    _SnmpSyslocation_Type()
)
snmpSyslocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSyslocation.setStatus("current")
_SnmpTrapCommunity_Type = DisplayString
_SnmpTrapCommunity_Object = MibScalar
snmpTrapCommunity = _SnmpTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 2, 1, 9),
    _SnmpTrapCommunity_Type()
)
snmpTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapCommunity.setStatus("current")
_SystemConfig_ObjectIdentity = ObjectIdentity
systemConfig = _SystemConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 3)
)
_TraceConfig_ObjectIdentity = ObjectIdentity
traceConfig = _TraceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 3, 1)
)
_TraceOutput_Type = TraceOutputType
_TraceOutput_Object = MibScalar
traceOutput = _TraceOutput_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 3, 1, 1),
    _TraceOutput_Type()
)
traceOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceOutput.setStatus("current")
_SyslogdIpaddr_Type = DisplayString
_SyslogdIpaddr_Object = MibScalar
syslogdIpaddr = _SyslogdIpaddr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 3, 1, 2),
    _SyslogdIpaddr_Type()
)
syslogdIpaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogdIpaddr.setStatus("current")
_SyslogdPort_Type = Integer32
_SyslogdPort_Object = MibScalar
syslogdPort = _SyslogdPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 3, 1, 3),
    _SyslogdPort_Type()
)
syslogdPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogdPort.setStatus("current")
_LogLocalFile_Type = DisplayString
_LogLocalFile_Object = MibScalar
logLocalFile = _LogLocalFile_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 3, 1, 4),
    _LogLocalFile_Type()
)
logLocalFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logLocalFile.setStatus("current")
_LogLocalSize_Type = Integer32
_LogLocalSize_Object = MibScalar
logLocalSize = _LogLocalSize_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 3, 1, 5),
    _LogLocalSize_Type()
)
logLocalSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logLocalSize.setStatus("current")
_LogVoipPbxEnable_Type = TruthValue
_LogVoipPbxEnable_Object = MibScalar
logVoipPbxEnable = _LogVoipPbxEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 3, 1, 6),
    _LogVoipPbxEnable_Type()
)
logVoipPbxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logVoipPbxEnable.setStatus("current")
_LogVoipError_Type = TruthValue
_LogVoipError_Object = MibScalar
logVoipError = _LogVoipError_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 3, 1, 7),
    _LogVoipError_Type()
)
logVoipError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logVoipError.setStatus("current")
_LogVoipWarning_Type = TruthValue
_LogVoipWarning_Object = MibScalar
logVoipWarning = _LogVoipWarning_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 3, 1, 8),
    _LogVoipWarning_Type()
)
logVoipWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logVoipWarning.setStatus("current")
_LogVoipDebug_Type = TruthValue
_LogVoipDebug_Object = MibScalar
logVoipDebug = _LogVoipDebug_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 3, 1, 9),
    _LogVoipDebug_Type()
)
logVoipDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logVoipDebug.setStatus("current")
_LogVoipInfo_Type = TruthValue
_LogVoipInfo_Object = MibScalar
logVoipInfo = _LogVoipInfo_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 3, 1, 10),
    _LogVoipInfo_Type()
)
logVoipInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logVoipInfo.setStatus("current")


class _LogVoipSipLevel_Type(Integer32):
    """Custom type logVoipSipLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_LogVoipSipLevel_Type.__name__ = "Integer32"
_LogVoipSipLevel_Object = MibScalar
logVoipSipLevel = _LogVoipSipLevel_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 3, 1, 11),
    _LogVoipSipLevel_Type()
)
logVoipSipLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logVoipSipLevel.setStatus("current")
_LogIgmpEnable_Type = TruthValue
_LogIgmpEnable_Object = MibScalar
logIgmpEnable = _LogIgmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 3, 1, 12),
    _LogIgmpEnable_Type()
)
logIgmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logIgmpEnable.setStatus("current")
_ActionCommands_ObjectIdentity = ObjectIdentity
actionCommands = _ActionCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 10)
)
_ActionSave_Type = TruthValue
_ActionSave_Object = MibScalar
actionSave = _ActionSave_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 10, 1),
    _ActionSave_Type()
)
actionSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actionSave.setStatus("current")
_ActionReboot_Type = TruthValue
_ActionReboot_Object = MibScalar
actionReboot = _ActionReboot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 10, 2),
    _ActionReboot_Type()
)
actionReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actionReboot.setStatus("current")

# Managed Objects groups

tau8Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35265, 1, 55, 200)
)
tau8Group.setObjects(
      *(("ELTEX-TAU8", "fxsPortsUseFxsProfile"),
        ("ELTEX-TAU8", "fxsPortEnabled"),
        ("ELTEX-TAU8", "fxsPortSipProfileId"),
        ("ELTEX-TAU8", "fxsPortProfile"),
        ("ELTEX-TAU8", "fxsPortPhone"),
        ("ELTEX-TAU8", "fxsPortUsername"),
        ("ELTEX-TAU8", "fxsPortAuthName"),
        ("ELTEX-TAU8", "fxsPortAuthPass"),
        ("ELTEX-TAU8", "fxsPortSipPort"),
        ("ELTEX-TAU8", "fxsPortUseAltNumber"),
        ("ELTEX-TAU8", "fxsPortAltNumber"),
        ("ELTEX-TAU8", "fxsPortCpcRus"),
        ("ELTEX-TAU8", "fxsPortMinOnhookTime"),
        ("ELTEX-TAU8", "fxsPortMinFlash"),
        ("ELTEX-TAU8", "fxsPortGainR"),
        ("ELTEX-TAU8", "fxsPortGainT"),
        ("ELTEX-TAU8", "fxsPortMinPulse"),
        ("ELTEX-TAU8", "fxsPortInterdigit"),
        ("ELTEX-TAU8", "fxsPortCallerId"),
        ("ELTEX-TAU8", "fxsPortHangupTimeout"),
        ("ELTEX-TAU8", "fxsPortRbTimeout"),
        ("ELTEX-TAU8", "fxsPortBusyTimeout"),
        ("ELTEX-TAU8", "fxsPortPolarityReverse"),
        ("ELTEX-TAU8", "fxsPortCallTransfer"),
        ("ELTEX-TAU8", "fxsPortCallWaiting"),
        ("ELTEX-TAU8", "fxsPortDirectnumber"),
        ("ELTEX-TAU8", "fxsPortStopDial"),
        ("ELTEX-TAU8", "fxsPortHotLine"),
        ("ELTEX-TAU8", "fxsPortHotNumber"),
        ("ELTEX-TAU8", "fxsPortHotTimeout"),
        ("ELTEX-TAU8", "fxsPortCtUnconditional"),
        ("ELTEX-TAU8", "fxsPortCfuNumber"),
        ("ELTEX-TAU8", "fxsPortCtBusy"),
        ("ELTEX-TAU8", "fxsPortCfbNumber"),
        ("ELTEX-TAU8", "fxsPortCtNoanswer"),
        ("ELTEX-TAU8", "fxsPortCfnaNumber"),
        ("ELTEX-TAU8", "fxsPortCtTimeout"),
        ("ELTEX-TAU8", "fxsPortDndEnable"),
        ("ELTEX-TAU8", "fxsPortRowStatus"),
        ("ELTEX-TAU8", "fxsPortsMIBBoundary"),
        ("ELTEX-TAU8", "fxsProfileName"),
        ("ELTEX-TAU8", "fxsProfileMinOnhookTime"),
        ("ELTEX-TAU8", "fxsProfileMinFlash"),
        ("ELTEX-TAU8", "fxsProfileGainR"),
        ("ELTEX-TAU8", "fxsProfileGainT"),
        ("ELTEX-TAU8", "fxsProfileMinPulse"),
        ("ELTEX-TAU8", "fxsProfileInterdigit"),
        ("ELTEX-TAU8", "fxsProfileCallerId"),
        ("ELTEX-TAU8", "fxsProfileHangupTimeout"),
        ("ELTEX-TAU8", "fxsProfileRbTimeout"),
        ("ELTEX-TAU8", "fxsProfileBusyTimeout"),
        ("ELTEX-TAU8", "fxsProfilePolarityReverse"),
        ("ELTEX-TAU8", "fxsProfileRowStatus"),
        ("ELTEX-TAU8", "fxsProfilesMIBBoundary"),
        ("ELTEX-TAU8", "sipCommonStunEnable"),
        ("ELTEX-TAU8", "sipCommonStunServer"),
        ("ELTEX-TAU8", "sipCommonStunInterval"),
        ("ELTEX-TAU8", "sipCommonPublicIp"),
        ("ELTEX-TAU8", "sipCommonNotUseNAPTR"),
        ("ELTEX-TAU8", "sipCommonNotUseSRV"),
        ("ELTEX-TAU8", "sipProfileName"),
        ("ELTEX-TAU8", "sipProEnablesip"),
        ("ELTEX-TAU8", "sipProRsrvMode"),
        ("ELTEX-TAU8", "sipProProxyip"),
        ("ELTEX-TAU8", "sipProRegistration"),
        ("ELTEX-TAU8", "sipProRegistrarip"),
        ("ELTEX-TAU8", "sipProProxyipRsrv1"),
        ("ELTEX-TAU8", "sipProRegistrationRsrv1"),
        ("ELTEX-TAU8", "sipProRegistraripRsrv1"),
        ("ELTEX-TAU8", "sipProProxyipRsrv2"),
        ("ELTEX-TAU8", "sipProRegistrationRsrv2"),
        ("ELTEX-TAU8", "sipProRegistraripRsrv2"),
        ("ELTEX-TAU8", "sipProProxyipRsrv3"),
        ("ELTEX-TAU8", "sipProRegistrationRsrv3"),
        ("ELTEX-TAU8", "sipProRegistraripRsrv3"),
        ("ELTEX-TAU8", "sipProProxyipRsrv4"),
        ("ELTEX-TAU8", "sipProRegistrationRsrv4"),
        ("ELTEX-TAU8", "sipProRegistraripRsrv4"),
        ("ELTEX-TAU8", "sipProRsrvCheckMethod"),
        ("ELTEX-TAU8", "sipProRsrvKeepaliveTime"),
        ("ELTEX-TAU8", "sipProDomain"),
        ("ELTEX-TAU8", "sipProOutbound"),
        ("ELTEX-TAU8", "sipProExpires"),
        ("ELTEX-TAU8", "sipProRri"),
        ("ELTEX-TAU8", "sipProDomainToReg"),
        ("ELTEX-TAU8", "sipProEarlyMedia"),
        ("ELTEX-TAU8", "sipProDisplayToReg"),
        ("ELTEX-TAU8", "sipProRingback"),
        ("ELTEX-TAU8", "sipProReduceSdpMediaCount"),
        ("ELTEX-TAU8", "sipProOption100rel"),
        ("ELTEX-TAU8", "sipProCodecOrder"),
        ("ELTEX-TAU8", "sipProG711pte"),
        ("ELTEX-TAU8", "sipProDtmfTransfer"),
        ("ELTEX-TAU8", "sipProFaxDirection"),
        ("ELTEX-TAU8", "sipProFaxTransfer1"),
        ("ELTEX-TAU8", "sipProFaxTransfer2"),
        ("ELTEX-TAU8", "sipProFaxTransfer3"),
        ("ELTEX-TAU8", "sipProEnableInT38"),
        ("ELTEX-TAU8", "sipProFlashTransfer"),
        ("ELTEX-TAU8", "sipProFlashMime"),
        ("ELTEX-TAU8", "sipProModem"),
        ("ELTEX-TAU8", "sipProPayload"),
        ("ELTEX-TAU8", "sipProSilenceDetector"),
        ("ELTEX-TAU8", "sipProEchoCanceler"),
        ("ELTEX-TAU8", "sipProRtcp"),
        ("ELTEX-TAU8", "sipProRtcpTimer"),
        ("ELTEX-TAU8", "sipProRtcpCount"),
        ("ELTEX-TAU8", "sipProDialplanRegexp"),
        ("ELTEX-TAU8", "sipProRowStatus"),
        ("ELTEX-TAU8", "sipProKeepAliveMode"),
        ("ELTEX-TAU8", "sipProKeepAliveInterval"),
        ("ELTEX-TAU8", "sipProConferenceMode"),
        ("ELTEX-TAU8", "sipProConferenceServer"),
        ("ELTEX-TAU8", "sipProImsEnable"),
        ("ELTEX-TAU8", "sipProXcapCallholdName"),
        ("ELTEX-TAU8", "sipProXcapCwName"),
        ("ELTEX-TAU8", "sipProXcapConferenceName"),
        ("ELTEX-TAU8", "sipProXcapHotlineName"),
        ("ELTEX-TAU8", "sipProfilesMIBBoundary"),
        ("ELTEX-TAU8", "huntGrEnable"),
        ("ELTEX-TAU8", "huntGroupName"),
        ("ELTEX-TAU8", "huntGrSipProfileId"),
        ("ELTEX-TAU8", "huntGrPhone"),
        ("ELTEX-TAU8", "huntGrRegistration"),
        ("ELTEX-TAU8", "huntGrUserName"),
        ("ELTEX-TAU8", "huntGrPassword"),
        ("ELTEX-TAU8", "huntGrType"),
        ("ELTEX-TAU8", "huntGrCallQueueSize"),
        ("ELTEX-TAU8", "huntGrWaitingTime"),
        ("ELTEX-TAU8", "huntGrSipPort"),
        ("ELTEX-TAU8", "huntGrPickupEnable"),
        ("ELTEX-TAU8", "huntGrPorts"),
        ("ELTEX-TAU8", "huntGrRowStatus"),
        ("ELTEX-TAU8", "huntGroupsMIBBoundary"),
        ("ELTEX-TAU8", "dvoCfuPrefix"),
        ("ELTEX-TAU8", "dvoCfbPrefix"),
        ("ELTEX-TAU8", "dvoCfnaPrefix"),
        ("ELTEX-TAU8", "dvoCallPickupPrefix"),
        ("ELTEX-TAU8", "dvoHotNumberPrefix"),
        ("ELTEX-TAU8", "dvoCallwaitingPrefix"),
        ("ELTEX-TAU8", "dvoDndPrefix"),
        ("ELTEX-TAU8", "snmpRoCommunity"),
        ("ELTEX-TAU8", "snmpRwCommunity"),
        ("ELTEX-TAU8", "snmpTrapsink"),
        ("ELTEX-TAU8", "snmpTrap2sink"),
        ("ELTEX-TAU8", "snmpInformsink"),
        ("ELTEX-TAU8", "snmpSysname"),
        ("ELTEX-TAU8", "snmpSyscontact"),
        ("ELTEX-TAU8", "snmpSyslocation"),
        ("ELTEX-TAU8", "snmpTrapCommunity"),
        ("ELTEX-TAU8", "traceOutput"),
        ("ELTEX-TAU8", "syslogdIpaddr"),
        ("ELTEX-TAU8", "syslogdPort"),
        ("ELTEX-TAU8", "logLocalFile"),
        ("ELTEX-TAU8", "logLocalSize"),
        ("ELTEX-TAU8", "logVoipPbxEnable"),
        ("ELTEX-TAU8", "logVoipError"),
        ("ELTEX-TAU8", "logVoipWarning"),
        ("ELTEX-TAU8", "logVoipDebug"),
        ("ELTEX-TAU8", "logVoipInfo"),
        ("ELTEX-TAU8", "logVoipSipLevel"),
        ("ELTEX-TAU8", "logIgmpEnable"),
        ("ELTEX-TAU8", "actionReboot"),
        ("ELTEX-TAU8", "actionSave"))
)
if mibBuilder.loadTexts:
    tau8Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-TAU8",
    **{"CallerIdType": CallerIdType,
       "CallTransferType": CallTransferType,
       "RsrvModeType": RsrvModeType,
       "RsrvCheckMethodType": RsrvCheckMethodType,
       "OutboundType": OutboundType,
       "EarlyMediaType": EarlyMediaType,
       "Option100relType": Option100relType,
       "KeepAliveModeType": KeepAliveModeType,
       "DtmfTransferType": DtmfTransferType,
       "FaxDirectionType": FaxDirectionType,
       "FaxtransferType": FaxtransferType,
       "FlashtransferType": FlashtransferType,
       "FlashMimeType": FlashMimeType,
       "ModemType": ModemType,
       "GroupType": GroupType,
       "TraceOutputType": TraceOutputType,
       "ConferenceMode": ConferenceMode,
       "tau8": tau8,
       "pbxConfig": pbxConfig,
       "fxsPorts": fxsPorts,
       "fxsPortsUseFxsProfile": fxsPortsUseFxsProfile,
       "fxsPortTable": fxsPortTable,
       "fxsPortEntry": fxsPortEntry,
       "fxsPortIndex": fxsPortIndex,
       "fxsPortEnabled": fxsPortEnabled,
       "fxsPortSipProfileId": fxsPortSipProfileId,
       "fxsPortProfile": fxsPortProfile,
       "fxsPortPhone": fxsPortPhone,
       "fxsPortUsername": fxsPortUsername,
       "fxsPortAuthName": fxsPortAuthName,
       "fxsPortAuthPass": fxsPortAuthPass,
       "fxsPortSipPort": fxsPortSipPort,
       "fxsPortUseAltNumber": fxsPortUseAltNumber,
       "fxsPortAltNumber": fxsPortAltNumber,
       "fxsPortCpcRus": fxsPortCpcRus,
       "fxsPortMinOnhookTime": fxsPortMinOnhookTime,
       "fxsPortMinFlash": fxsPortMinFlash,
       "fxsPortGainR": fxsPortGainR,
       "fxsPortGainT": fxsPortGainT,
       "fxsPortMinPulse": fxsPortMinPulse,
       "fxsPortInterdigit": fxsPortInterdigit,
       "fxsPortCallerId": fxsPortCallerId,
       "fxsPortHangupTimeout": fxsPortHangupTimeout,
       "fxsPortRbTimeout": fxsPortRbTimeout,
       "fxsPortBusyTimeout": fxsPortBusyTimeout,
       "fxsPortPolarityReverse": fxsPortPolarityReverse,
       "fxsPortCallTransfer": fxsPortCallTransfer,
       "fxsPortCallWaiting": fxsPortCallWaiting,
       "fxsPortDirectnumber": fxsPortDirectnumber,
       "fxsPortStopDial": fxsPortStopDial,
       "fxsPortHotLine": fxsPortHotLine,
       "fxsPortHotNumber": fxsPortHotNumber,
       "fxsPortHotTimeout": fxsPortHotTimeout,
       "fxsPortCtUnconditional": fxsPortCtUnconditional,
       "fxsPortCfuNumber": fxsPortCfuNumber,
       "fxsPortCtBusy": fxsPortCtBusy,
       "fxsPortCfbNumber": fxsPortCfbNumber,
       "fxsPortCtNoanswer": fxsPortCtNoanswer,
       "fxsPortCfnaNumber": fxsPortCfnaNumber,
       "fxsPortCtTimeout": fxsPortCtTimeout,
       "fxsPortDndEnable": fxsPortDndEnable,
       "fxsPortRowStatus": fxsPortRowStatus,
       "fxsPortsMIBBoundary": fxsPortsMIBBoundary,
       "fxsProfiles": fxsProfiles,
       "fxsProfileTable": fxsProfileTable,
       "fxsProfileEntry": fxsProfileEntry,
       "fxsProfileIndex": fxsProfileIndex,
       "fxsProfileName": fxsProfileName,
       "fxsProfileMinOnhookTime": fxsProfileMinOnhookTime,
       "fxsProfileMinFlash": fxsProfileMinFlash,
       "fxsProfileGainR": fxsProfileGainR,
       "fxsProfileGainT": fxsProfileGainT,
       "fxsProfileMinPulse": fxsProfileMinPulse,
       "fxsProfileInterdigit": fxsProfileInterdigit,
       "fxsProfileCallerId": fxsProfileCallerId,
       "fxsProfileHangupTimeout": fxsProfileHangupTimeout,
       "fxsProfileRbTimeout": fxsProfileRbTimeout,
       "fxsProfileBusyTimeout": fxsProfileBusyTimeout,
       "fxsProfilePolarityReverse": fxsProfilePolarityReverse,
       "fxsProfileRowStatus": fxsProfileRowStatus,
       "fxsProfilesMIBBoundary": fxsProfilesMIBBoundary,
       "sipConfig": sipConfig,
       "sipCommon": sipCommon,
       "sipCommonStunEnable": sipCommonStunEnable,
       "sipCommonStunServer": sipCommonStunServer,
       "sipCommonStunInterval": sipCommonStunInterval,
       "sipCommonPublicIp": sipCommonPublicIp,
       "sipCommonNotUseNAPTR": sipCommonNotUseNAPTR,
       "sipCommonNotUseSRV": sipCommonNotUseSRV,
       "sipProfileTable": sipProfileTable,
       "sipProfileEntry": sipProfileEntry,
       "sipProfileIndex": sipProfileIndex,
       "sipProfileName": sipProfileName,
       "sipProEnablesip": sipProEnablesip,
       "sipProRsrvMode": sipProRsrvMode,
       "sipProProxyip": sipProProxyip,
       "sipProRegistration": sipProRegistration,
       "sipProRegistrarip": sipProRegistrarip,
       "sipProProxyipRsrv1": sipProProxyipRsrv1,
       "sipProRegistrationRsrv1": sipProRegistrationRsrv1,
       "sipProRegistraripRsrv1": sipProRegistraripRsrv1,
       "sipProProxyipRsrv2": sipProProxyipRsrv2,
       "sipProRegistrationRsrv2": sipProRegistrationRsrv2,
       "sipProRegistraripRsrv2": sipProRegistraripRsrv2,
       "sipProProxyipRsrv3": sipProProxyipRsrv3,
       "sipProRegistrationRsrv3": sipProRegistrationRsrv3,
       "sipProRegistraripRsrv3": sipProRegistraripRsrv3,
       "sipProProxyipRsrv4": sipProProxyipRsrv4,
       "sipProRegistrationRsrv4": sipProRegistrationRsrv4,
       "sipProRegistraripRsrv4": sipProRegistraripRsrv4,
       "sipProRsrvCheckMethod": sipProRsrvCheckMethod,
       "sipProRsrvKeepaliveTime": sipProRsrvKeepaliveTime,
       "sipProDomain": sipProDomain,
       "sipProOutbound": sipProOutbound,
       "sipProExpires": sipProExpires,
       "sipProRri": sipProRri,
       "sipProDomainToReg": sipProDomainToReg,
       "sipProEarlyMedia": sipProEarlyMedia,
       "sipProDisplayToReg": sipProDisplayToReg,
       "sipProRingback": sipProRingback,
       "sipProReduceSdpMediaCount": sipProReduceSdpMediaCount,
       "sipProOption100rel": sipProOption100rel,
       "sipProCodecOrder": sipProCodecOrder,
       "sipProG711pte": sipProG711pte,
       "sipProDtmfTransfer": sipProDtmfTransfer,
       "sipProFaxDirection": sipProFaxDirection,
       "sipProFaxTransfer1": sipProFaxTransfer1,
       "sipProFaxTransfer2": sipProFaxTransfer2,
       "sipProFaxTransfer3": sipProFaxTransfer3,
       "sipProEnableInT38": sipProEnableInT38,
       "sipProFlashTransfer": sipProFlashTransfer,
       "sipProFlashMime": sipProFlashMime,
       "sipProModem": sipProModem,
       "sipProPayload": sipProPayload,
       "sipProSilenceDetector": sipProSilenceDetector,
       "sipProEchoCanceler": sipProEchoCanceler,
       "sipProRtcp": sipProRtcp,
       "sipProRtcpTimer": sipProRtcpTimer,
       "sipProRtcpCount": sipProRtcpCount,
       "sipProDialplanRegexp": sipProDialplanRegexp,
       "sipProRowStatus": sipProRowStatus,
       "sipProKeepAliveMode": sipProKeepAliveMode,
       "sipProKeepAliveInterval": sipProKeepAliveInterval,
       "sipProConferenceMode": sipProConferenceMode,
       "sipProConferenceServer": sipProConferenceServer,
       "sipProImsEnable": sipProImsEnable,
       "sipProXcapCallholdName": sipProXcapCallholdName,
       "sipProXcapCwName": sipProXcapCwName,
       "sipProXcapConferenceName": sipProXcapConferenceName,
       "sipProXcapHotlineName": sipProXcapHotlineName,
       "sipProfilesMIBBoundary": sipProfilesMIBBoundary,
       "groupsConfig": groupsConfig,
       "huntGroupTable": huntGroupTable,
       "huntGroupEntry": huntGroupEntry,
       "huntGrIndex": huntGrIndex,
       "huntGrEnable": huntGrEnable,
       "huntGroupName": huntGroupName,
       "huntGrSipProfileId": huntGrSipProfileId,
       "huntGrPhone": huntGrPhone,
       "huntGrRegistration": huntGrRegistration,
       "huntGrUserName": huntGrUserName,
       "huntGrPassword": huntGrPassword,
       "huntGrType": huntGrType,
       "huntGrCallQueueSize": huntGrCallQueueSize,
       "huntGrWaitingTime": huntGrWaitingTime,
       "huntGrSipPort": huntGrSipPort,
       "huntGrPickupEnable": huntGrPickupEnable,
       "huntGrPorts": huntGrPorts,
       "huntGrRowStatus": huntGrRowStatus,
       "huntGroupsMIBBoundary": huntGroupsMIBBoundary,
       "suppServices": suppServices,
       "dvoCfuPrefix": dvoCfuPrefix,
       "dvoCfbPrefix": dvoCfbPrefix,
       "dvoCfnaPrefix": dvoCfnaPrefix,
       "dvoCallPickupPrefix": dvoCallPickupPrefix,
       "dvoHotNumberPrefix": dvoHotNumberPrefix,
       "dvoCallwaitingPrefix": dvoCallwaitingPrefix,
       "dvoDndPrefix": dvoDndPrefix,
       "networkConfig": networkConfig,
       "snmpConfig": snmpConfig,
       "snmpRoCommunity": snmpRoCommunity,
       "snmpRwCommunity": snmpRwCommunity,
       "snmpTrapsink": snmpTrapsink,
       "snmpTrap2sink": snmpTrap2sink,
       "snmpInformsink": snmpInformsink,
       "snmpSysname": snmpSysname,
       "snmpSyscontact": snmpSyscontact,
       "snmpSyslocation": snmpSyslocation,
       "snmpTrapCommunity": snmpTrapCommunity,
       "systemConfig": systemConfig,
       "traceConfig": traceConfig,
       "traceOutput": traceOutput,
       "syslogdIpaddr": syslogdIpaddr,
       "syslogdPort": syslogdPort,
       "logLocalFile": logLocalFile,
       "logLocalSize": logLocalSize,
       "logVoipPbxEnable": logVoipPbxEnable,
       "logVoipError": logVoipError,
       "logVoipWarning": logVoipWarning,
       "logVoipDebug": logVoipDebug,
       "logVoipInfo": logVoipInfo,
       "logVoipSipLevel": logVoipSipLevel,
       "logIgmpEnable": logIgmpEnable,
       "actionCommands": actionCommands,
       "actionSave": actionSave,
       "actionReboot": actionReboot,
       "tau8Group": tau8Group}
)
