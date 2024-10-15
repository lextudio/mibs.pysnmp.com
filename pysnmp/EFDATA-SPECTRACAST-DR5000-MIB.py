# SNMP MIB module (EFDATA-SPECTRACAST-DR5000-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EFDATA-SPECTRACAST-DR5000-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:38 2024
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


# Types definitions



class MPEG_PID_mode(Integer32):
    """Custom type MPEG_PID_mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 2),
          ("manual", 1))
    )





class FLAG(Integer32):
    """Custom type FLAG based on Integer32"""
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




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Efdata_ObjectIdentity = ObjectIdentity
efdata = _Efdata_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247)
)
_Spectracast_ObjectIdentity = ObjectIdentity
spectracast = _Spectracast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3)
)
_Dr5000_ObjectIdentity = ObjectIdentity
dr5000 = _Dr5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2)
)
_General_ObjectIdentity = ObjectIdentity
general = _General_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 1)
)
_SoftwareVersion_Type = DisplayString
_SoftwareVersion_Object = MibScalar
softwareVersion = _SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 1, 1),
    _SoftwareVersion_Type()
)
softwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareVersion.setStatus("mandatory")
_HardwareVersion_Type = DisplayString
_HardwareVersion_Object = MibScalar
hardwareVersion = _HardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 1, 2),
    _HardwareVersion_Type()
)
hardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareVersion.setStatus("mandatory")
_MacAddress_Type = DisplayString
_MacAddress_Object = MibScalar
macAddress = _MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 1, 3),
    _MacAddress_Type()
)
macAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddress.setStatus("mandatory")
_MulticastRoutingStatus_Type = DisplayString
_MulticastRoutingStatus_Object = MibScalar
multicastRoutingStatus = _MulticastRoutingStatus_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 1, 4),
    _MulticastRoutingStatus_Type()
)
multicastRoutingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastRoutingStatus.setStatus("mandatory")
_Rfparameters_ObjectIdentity = ObjectIdentity
rfparameters = _Rfparameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 2)
)
_Rf_Input_Type = DisplayString
_Rf_Input_Object = MibScalar
rf_Input = _Rf_Input_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 2, 1),
    _Rf_Input_Type()
)
rf_Input.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rf_Input.setStatus("mandatory")
_Lnb_Frequency_Type = DisplayString
_Lnb_Frequency_Object = MibScalar
lnb_Frequency = _Lnb_Frequency_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 2, 2),
    _Lnb_Frequency_Type()
)
lnb_Frequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lnb_Frequency.setStatus("mandatory")
_SymbolRate_Type = DisplayString
_SymbolRate_Object = MibScalar
symbolRate = _SymbolRate_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 2, 3),
    _SymbolRate_Type()
)
symbolRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    symbolRate.setStatus("mandatory")


class _Polarity_Type(Integer32):
    """Custom type polarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              14,
              18)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("horizontal", 18),
          ("vertical", 14))
    )


_Polarity_Type.__name__ = "Integer32"
_Polarity_Object = MibScalar
polarity = _Polarity_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 2, 4),
    _Polarity_Type()
)
polarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    polarity.setStatus("mandatory")


class _FrequencyRange_Type(Integer32):
    """Custom type frequencyRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_FrequencyRange_Type.__name__ = "Integer32"
_FrequencyRange_Object = MibScalar
frequencyRange = _FrequencyRange_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 2, 5),
    _FrequencyRange_Type()
)
frequencyRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frequencyRange.setStatus("mandatory")
_Dvbparameters_ObjectIdentity = ObjectIdentity
dvbparameters = _Dvbparameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 3)
)
_Pids_number_Type = Integer32
_Pids_number_Object = MibScalar
pids_number = _Pids_number_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 3, 1),
    _Pids_number_Type()
)
pids_number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pids_number.setStatus("mandatory")
_PidTable_Object = MibTable
pidTable = _PidTable_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 3, 2)
)
if mibBuilder.loadTexts:
    pidTable.setStatus("mandatory")
_PidEntry_Object = MibTableRow
pidEntry = _PidEntry_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 3, 2, 1)
)
pidEntry.setIndexNames(
    (0, "EFDATA-SPECTRACAST-DR5000-MIB", "pidindex"),
)
if mibBuilder.loadTexts:
    pidEntry.setStatus("mandatory")
_Pidindex_Type = Integer32
_Pidindex_Object = MibTableColumn
pidindex = _Pidindex_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 3, 2, 1, 1),
    _Pidindex_Type()
)
pidindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pidindex.setStatus("mandatory")
_Pidvalue_Type = Integer32
_Pidvalue_Object = MibTableColumn
pidvalue = _Pidvalue_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 3, 2, 1, 2),
    _Pidvalue_Type()
)
pidvalue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pidvalue.setStatus("mandatory")
_Ccuparameters_ObjectIdentity = ObjectIdentity
ccuparameters = _Ccuparameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 4)
)


class _CcuConnectionMode_Type(Integer32):
    """Custom type ccuConnectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("duplex", 1),
          ("manual", 0),
          ("simplex", 2))
    )


_CcuConnectionMode_Type.__name__ = "Integer32"
_CcuConnectionMode_Object = MibScalar
ccuConnectionMode = _CcuConnectionMode_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 4, 1),
    _CcuConnectionMode_Type()
)
ccuConnectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccuConnectionMode.setStatus("mandatory")
_CcuIpAddress_Type = IpAddress
_CcuIpAddress_Object = MibScalar
ccuIpAddress = _CcuIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 4, 2),
    _CcuIpAddress_Type()
)
ccuIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccuIpAddress.setStatus("mandatory")
_CcuUserName_Type = DisplayString
_CcuUserName_Object = MibScalar
ccuUserName = _CcuUserName_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 4, 3),
    _CcuUserName_Type()
)
ccuUserName.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ccuUserName.setStatus("mandatory")
_CcuPassword_Type = DisplayString
_CcuPassword_Object = MibScalar
ccuPassword = _CcuPassword_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 4, 4),
    _CcuPassword_Type()
)
ccuPassword.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ccuPassword.setStatus("mandatory")


class _EncryptedMulticast_Type(Integer32):
    """Custom type encryptedMulticast based on Integer32"""
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


_EncryptedMulticast_Type.__name__ = "Integer32"
_EncryptedMulticast_Object = MibScalar
encryptedMulticast = _EncryptedMulticast_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 4, 5),
    _EncryptedMulticast_Type()
)
encryptedMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    encryptedMulticast.setStatus("mandatory")
_Dialupparameters_ObjectIdentity = ObjectIdentity
dialupparameters = _Dialupparameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 5)
)


class _ConnectionMode_Type(Integer32):
    """Custom type connectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 0))
    )


_ConnectionMode_Type.__name__ = "Integer32"
_ConnectionMode_Object = MibScalar
connectionMode = _ConnectionMode_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 5, 1),
    _ConnectionMode_Type()
)
connectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectionMode.setStatus("mandatory")
_PhoneNumber_Type = Integer32
_PhoneNumber_Object = MibScalar
phoneNumber = _PhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 5, 2),
    _PhoneNumber_Type()
)
phoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phoneNumber.setStatus("mandatory")
_UserName_Type = DisplayString
_UserName_Object = MibScalar
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 5, 3),
    _UserName_Type()
)
userName.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    userName.setStatus("mandatory")
_Password_Type = DisplayString
_Password_Object = MibScalar
password = _Password_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 5, 4),
    _Password_Type()
)
password.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    password.setStatus("mandatory")


class _DialTone_Type(Integer32):
    """Custom type dialTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pulse", 1),
          ("tone", 0))
    )


_DialTone_Type.__name__ = "Integer32"
_DialTone_Object = MibScalar
dialTone = _DialTone_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 5, 5),
    _DialTone_Type()
)
dialTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialTone.setStatus("mandatory")
_Speed_Type = Integer32
_Speed_Object = MibScalar
speed = _Speed_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 5, 7),
    _Speed_Type()
)
speed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speed.setStatus("mandatory")
_IdleTimeOut_Type = Integer32
_IdleTimeOut_Object = MibScalar
idleTimeOut = _IdleTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 5, 8),
    _IdleTimeOut_Type()
)
idleTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idleTimeOut.setStatus("mandatory")


class _Authentication_Type(Integer32):
    """Custom type authentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("chap", 1),
          ("pap", 0))
    )


_Authentication_Type.__name__ = "Integer32"
_Authentication_Object = MibScalar
authentication = _Authentication_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 5, 9),
    _Authentication_Type()
)
authentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authentication.setStatus("mandatory")
_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 6)
)
_InitializationStatus_Type = DisplayString
_InitializationStatus_Object = MibScalar
initializationStatus = _InitializationStatus_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 6, 1),
    _InitializationStatus_Type()
)
initializationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    initializationStatus.setStatus("mandatory")
_DemodulatorStatus_Type = DisplayString
_DemodulatorStatus_Object = MibScalar
demodulatorStatus = _DemodulatorStatus_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 6, 2),
    _DemodulatorStatus_Type()
)
demodulatorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    demodulatorStatus.setStatus("mandatory")
_SpectralInversion_Type = DisplayString
_SpectralInversion_Object = MibScalar
spectralInversion = _SpectralInversion_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 6, 3),
    _SpectralInversion_Type()
)
spectralInversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spectralInversion.setStatus("mandatory")
_Ber_before_Err_Correction_Type = DisplayString
_Ber_before_Err_Correction_Object = MibScalar
ber_before_Err_Correction = _Ber_before_Err_Correction_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 6, 4),
    _Ber_before_Err_Correction_Type()
)
ber_before_Err_Correction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ber_before_Err_Correction.setStatus("mandatory")
_Fec_Type = DisplayString
_Fec_Object = MibScalar
fec = _Fec_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 6, 5),
    _Fec_Type()
)
fec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fec.setStatus("mandatory")
_Agc_Type = DisplayString
_Agc_Object = MibScalar
agc = _Agc_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 6, 6),
    _Agc_Type()
)
agc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agc.setStatus("mandatory")
_FrequencyOffset_Type = DisplayString
_FrequencyOffset_Object = MibScalar
frequencyOffset = _FrequencyOffset_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 6, 7),
    _FrequencyOffset_Type()
)
frequencyOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frequencyOffset.setStatus("mandatory")
_Eb_N0_Type = DisplayString
_Eb_N0_Object = MibScalar
eb_N0 = _Eb_N0_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 6, 8),
    _Eb_N0_Type()
)
eb_N0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eb_N0.setStatus("mandatory")


class _Ccu_connection_status_Type(Integer32):
    """Custom type ccu_connection_status based on Integer32"""
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
        *(("connected", 1),
          ("disconnected", 0),
          ("tryingtoconnect", 2),
          ("waitingfordialup", 3),
          ("waitingforrflock", 4))
    )


_Ccu_connection_status_Type.__name__ = "Integer32"
_Ccu_connection_status_Object = MibScalar
ccu_connection_status = _Ccu_connection_status_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 6, 9),
    _Ccu_connection_status_Type()
)
ccu_connection_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccu_connection_status.setStatus("mandatory")


class _Dialup_connection_status_Type(Integer32):
    """Custom type dialup_connection_status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              10)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disconnected", 0),
          ("idle", 10),
          ("tryingtoconnect", 2))
    )


_Dialup_connection_status_Type.__name__ = "Integer32"
_Dialup_connection_status_Object = MibScalar
dialup_connection_status = _Dialup_connection_status_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 6, 10),
    _Dialup_connection_status_Type()
)
dialup_connection_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialup_connection_status.setStatus("mandatory")
_FlowStatistics_ObjectIdentity = ObjectIdentity
flowStatistics = _FlowStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 7)
)
_TotalThroughput_Type = DisplayString
_TotalThroughput_Object = MibScalar
totalThroughput = _TotalThroughput_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 7, 1),
    _TotalThroughput_Type()
)
totalThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalThroughput.setStatus("mandatory")
_UnicastThroughput_Type = DisplayString
_UnicastThroughput_Object = MibScalar
unicastThroughput = _UnicastThroughput_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 7, 2),
    _UnicastThroughput_Type()
)
unicastThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unicastThroughput.setStatus("mandatory")
_MulticastThroughput_Type = DisplayString
_MulticastThroughput_Object = MibScalar
multicastThroughput = _MulticastThroughput_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 7, 3),
    _MulticastThroughput_Type()
)
multicastThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastThroughput.setStatus("mandatory")
_TotalPackets_Type = DisplayString
_TotalPackets_Object = MibScalar
totalPackets = _TotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 7, 4),
    _TotalPackets_Type()
)
totalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalPackets.setStatus("mandatory")
_BadPackets_Type = DisplayString
_BadPackets_Object = MibScalar
badPackets = _BadPackets_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 7, 5),
    _BadPackets_Type()
)
badPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    badPackets.setStatus("mandatory")
_CorrectedPackets_Type = DisplayString
_CorrectedPackets_Object = MibScalar
correctedPackets = _CorrectedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 7, 6),
    _CorrectedPackets_Type()
)
correctedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    correctedPackets.setStatus("mandatory")


class _ResetFlowStatistics_Type(Integer32):
    """Custom type resetFlowStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_ResetFlowStatistics_Type.__name__ = "Integer32"
_ResetFlowStatistics_Object = MibScalar
resetFlowStatistics = _ResetFlowStatistics_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 7, 7),
    _ResetFlowStatistics_Type()
)
resetFlowStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetFlowStatistics.setStatus("mandatory")
_Maintenance_ObjectIdentity = ObjectIdentity
maintenance = _Maintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 8)
)


class _DriverRestart_Type(Integer32):
    """Custom type driverRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_DriverRestart_Type.__name__ = "Integer32"
_DriverRestart_Object = MibScalar
driverRestart = _DriverRestart_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 8, 1),
    _DriverRestart_Type()
)
driverRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    driverRestart.setStatus("mandatory")


class _DialupConnect_Type(Integer32):
    """Custom type dialupConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_DialupConnect_Type.__name__ = "Integer32"
_DialupConnect_Object = MibScalar
dialupConnect = _DialupConnect_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 8, 2),
    _DialupConnect_Type()
)
dialupConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialupConnect.setStatus("mandatory")


class _DialupDisconnect_Type(Integer32):
    """Custom type dialupDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_DialupDisconnect_Type.__name__ = "Integer32"
_DialupDisconnect_Object = MibScalar
dialupDisconnect = _DialupDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 8, 3),
    _DialupDisconnect_Type()
)
dialupDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialupDisconnect.setStatus("mandatory")


class _Ccuconnect_Type(Integer32):
    """Custom type ccuconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Ccuconnect_Type.__name__ = "Integer32"
_Ccuconnect_Object = MibScalar
ccuconnect = _Ccuconnect_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 8, 4),
    _Ccuconnect_Type()
)
ccuconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccuconnect.setStatus("mandatory")


class _Ccudisconnect_Type(Integer32):
    """Custom type ccudisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Ccudisconnect_Type.__name__ = "Integer32"
_Ccudisconnect_Object = MibScalar
ccudisconnect = _Ccudisconnect_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 8, 5),
    _Ccudisconnect_Type()
)
ccudisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccudisconnect.setStatus("mandatory")
_Upgrade_Type = DisplayString
_Upgrade_Object = MibScalar
upgrade = _Upgrade_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 8, 6),
    _Upgrade_Type()
)
upgrade.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    upgrade.setStatus("mandatory")
_SnmpVariables_ObjectIdentity = ObjectIdentity
snmpVariables = _SnmpVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 9)
)


class _EnableTraps_Type(Integer32):
    """Custom type enableTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EnableTraps_Type.__name__ = "Integer32"
_EnableTraps_Object = MibScalar
enableTraps = _EnableTraps_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 1),
    _EnableTraps_Type()
)
enableTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableTraps.setStatus("mandatory")
_SnmpManagerIP_Type = IpAddress
_SnmpManagerIP_Object = MibScalar
snmpManagerIP = _SnmpManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 2),
    _SnmpManagerIP_Type()
)
snmpManagerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpManagerIP.setStatus("mandatory")
_TrapPeriod_Type = Integer32
_TrapPeriod_Object = MibScalar
trapPeriod = _TrapPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 3),
    _TrapPeriod_Type()
)
trapPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapPeriod.setStatus("mandatory")
_TrapList_ObjectIdentity = ObjectIdentity
trapList = _TrapList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 4)
)
_MulticastDaemon_ObjectIdentity = ObjectIdentity
multicastDaemon = _MulticastDaemon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 4, 1)
)


class _MulticastTrapEnable_Type(Integer32):
    """Custom type multicastTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MulticastTrapEnable_Type.__name__ = "Integer32"
_MulticastTrapEnable_Object = MibScalar
multicastTrapEnable = _MulticastTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 4, 1, 1),
    _MulticastTrapEnable_Type()
)
multicastTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastTrapEnable.setStatus("mandatory")
_Demodulator_ObjectIdentity = ObjectIdentity
demodulator = _Demodulator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 4, 2)
)


class _DemodulatorTrapEnable_Type(Integer32):
    """Custom type demodulatorTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DemodulatorTrapEnable_Type.__name__ = "Integer32"
_DemodulatorTrapEnable_Object = MibScalar
demodulatorTrapEnable = _DemodulatorTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 4, 2, 1),
    _DemodulatorTrapEnable_Type()
)
demodulatorTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    demodulatorTrapEnable.setStatus("mandatory")
_CcuConnection_ObjectIdentity = ObjectIdentity
ccuConnection = _CcuConnection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 4, 3)
)


class _CcuTrapEnable_Type(Integer32):
    """Custom type ccuTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_CcuTrapEnable_Type.__name__ = "Integer32"
_CcuTrapEnable_Object = MibScalar
ccuTrapEnable = _CcuTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 4, 3, 1),
    _CcuTrapEnable_Type()
)
ccuTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccuTrapEnable.setStatus("mandatory")
_Dialup_ObjectIdentity = ObjectIdentity
dialup = _Dialup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 4, 4)
)


class _DialupTrapEnable_Type(Integer32):
    """Custom type dialupTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DialupTrapEnable_Type.__name__ = "Integer32"
_DialupTrapEnable_Object = MibScalar
dialupTrapEnable = _DialupTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 4, 4, 1),
    _DialupTrapEnable_Type()
)
dialupTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialupTrapEnable.setStatus("mandatory")
_BerLevel_ObjectIdentity = ObjectIdentity
berLevel = _BerLevel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 4, 5)
)


class _BerTrapEnable_Type(Integer32):
    """Custom type berTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BerTrapEnable_Type.__name__ = "Integer32"
_BerTrapEnable_Object = MibScalar
berTrapEnable = _BerTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 4, 5, 1),
    _BerTrapEnable_Type()
)
berTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    berTrapEnable.setStatus("mandatory")
_BerThreshold_Type = OctetString
_BerThreshold_Object = MibScalar
berThreshold = _BerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 4, 5, 2),
    _BerThreshold_Type()
)
berThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    berThreshold.setStatus("mandatory")
_FreqOffset_ObjectIdentity = ObjectIdentity
freqOffset = _FreqOffset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 4, 6)
)


class _FreqOffsetTrapEnable_Type(Integer32):
    """Custom type freqOffsetTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FreqOffsetTrapEnable_Type.__name__ = "Integer32"
_FreqOffsetTrapEnable_Object = MibScalar
freqOffsetTrapEnable = _FreqOffsetTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 4, 6, 1),
    _FreqOffsetTrapEnable_Type()
)
freqOffsetTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    freqOffsetTrapEnable.setStatus("mandatory")
_FreqOffsetThreshold_Type = OctetString
_FreqOffsetThreshold_Object = MibScalar
freqOffsetThreshold = _FreqOffsetThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 4, 6, 2),
    _FreqOffsetThreshold_Type()
)
freqOffsetThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    freqOffsetThreshold.setStatus("mandatory")
_AgcLevel_ObjectIdentity = ObjectIdentity
agcLevel = _AgcLevel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 4, 7)
)


class _AgcTrapEnable_Type(Integer32):
    """Custom type agcTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AgcTrapEnable_Type.__name__ = "Integer32"
_AgcTrapEnable_Object = MibScalar
agcTrapEnable = _AgcTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 4, 7, 1),
    _AgcTrapEnable_Type()
)
agcTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agcTrapEnable.setStatus("mandatory")
_AgcThreshold_Type = OctetString
_AgcThreshold_Object = MibScalar
agcThreshold = _AgcThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 4, 7, 2),
    _AgcThreshold_Type()
)
agcThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agcThreshold.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EFDATA-SPECTRACAST-DR5000-MIB",
    **{"MPEG-PID-mode": MPEG_PID_mode,
       "FLAG": FLAG,
       "efdata": efdata,
       "spectracast": spectracast,
       "dr5000": dr5000,
       "general": general,
       "softwareVersion": softwareVersion,
       "hardwareVersion": hardwareVersion,
       "macAddress": macAddress,
       "multicastRoutingStatus": multicastRoutingStatus,
       "rfparameters": rfparameters,
       "rf-Input": rf_Input,
       "lnb-Frequency": lnb_Frequency,
       "symbolRate": symbolRate,
       "polarity": polarity,
       "frequencyRange": frequencyRange,
       "dvbparameters": dvbparameters,
       "pids-number": pids_number,
       "pidTable": pidTable,
       "pidEntry": pidEntry,
       "pidindex": pidindex,
       "pidvalue": pidvalue,
       "ccuparameters": ccuparameters,
       "ccuConnectionMode": ccuConnectionMode,
       "ccuIpAddress": ccuIpAddress,
       "ccuUserName": ccuUserName,
       "ccuPassword": ccuPassword,
       "encryptedMulticast": encryptedMulticast,
       "dialupparameters": dialupparameters,
       "connectionMode": connectionMode,
       "phoneNumber": phoneNumber,
       "userName": userName,
       "password": password,
       "dialTone": dialTone,
       "speed": speed,
       "idleTimeOut": idleTimeOut,
       "authentication": authentication,
       "status": status,
       "initializationStatus": initializationStatus,
       "demodulatorStatus": demodulatorStatus,
       "spectralInversion": spectralInversion,
       "ber-before-Err-Correction": ber_before_Err_Correction,
       "fec": fec,
       "agc": agc,
       "frequencyOffset": frequencyOffset,
       "eb-N0": eb_N0,
       "ccu-connection-status": ccu_connection_status,
       "dialup-connection-status": dialup_connection_status,
       "flowStatistics": flowStatistics,
       "totalThroughput": totalThroughput,
       "unicastThroughput": unicastThroughput,
       "multicastThroughput": multicastThroughput,
       "totalPackets": totalPackets,
       "badPackets": badPackets,
       "correctedPackets": correctedPackets,
       "resetFlowStatistics": resetFlowStatistics,
       "maintenance": maintenance,
       "driverRestart": driverRestart,
       "dialupConnect": dialupConnect,
       "dialupDisconnect": dialupDisconnect,
       "ccuconnect": ccuconnect,
       "ccudisconnect": ccudisconnect,
       "upgrade": upgrade,
       "snmpVariables": snmpVariables,
       "enableTraps": enableTraps,
       "snmpManagerIP": snmpManagerIP,
       "trapPeriod": trapPeriod,
       "trapList": trapList,
       "multicastDaemon": multicastDaemon,
       "multicastTrapEnable": multicastTrapEnable,
       "demodulator": demodulator,
       "demodulatorTrapEnable": demodulatorTrapEnable,
       "ccuConnection": ccuConnection,
       "ccuTrapEnable": ccuTrapEnable,
       "dialup": dialup,
       "dialupTrapEnable": dialupTrapEnable,
       "berLevel": berLevel,
       "berTrapEnable": berTrapEnable,
       "berThreshold": berThreshold,
       "freqOffset": freqOffset,
       "freqOffsetTrapEnable": freqOffsetTrapEnable,
       "freqOffsetThreshold": freqOffsetThreshold,
       "agcLevel": agcLevel,
       "agcTrapEnable": agcTrapEnable,
       "agcThreshold": agcThreshold}
)
