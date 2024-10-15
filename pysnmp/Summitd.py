# SNMP MIB module (Summitd) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Summitd
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:24 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Summit_development_ObjectIdentity = ObjectIdentity
summit_development = _Summit_development_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23688)
)
_Summit_Products_ObjectIdentity = ObjectIdentity
summit_Products = _Summit_Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23688, 1)
)
_Uni_a_ObjectIdentity = ObjectIdentity
uni_a = _Uni_a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23688, 1, 1)
)


class _Name_Type(DisplayString):
    """Custom type name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Name_Type.__name__ = "DisplayString"
_Name_Object = MibScalar
name = _Name_Object(
    (1, 3, 6, 1, 4, 1, 23688, 1, 1, 1),
    _Name_Type()
)
name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    name.setStatus("mandatory")


class _Condition_Type(Integer32):
    """Custom type condition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("ok", 1),
          ("warning", 3))
    )


_Condition_Type.__name__ = "Integer32"
_Condition_Object = MibScalar
condition = _Condition_Object(
    (1, 3, 6, 1, 4, 1, 23688, 1, 1, 2),
    _Condition_Type()
)
condition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    condition.setStatus("mandatory")
_Mannum_Type = Integer32
_Mannum_Object = MibScalar
mannum = _Mannum_Object(
    (1, 3, 6, 1, 4, 1, 23688, 1, 1, 3),
    _Mannum_Type()
)
mannum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mannum.setStatus("mandatory")


class _Status_Type(DisplayString):
    """Custom type status based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Status_Type.__name__ = "DisplayString"
_Status_Object = MibScalar
status = _Status_Object(
    (1, 3, 6, 1, 4, 1, 23688, 1, 1, 4),
    _Status_Type()
)
status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status.setStatus("mandatory")
_Rssi_Type = Gauge32
_Rssi_Object = MibScalar
rssi = _Rssi_Object(
    (1, 3, 6, 1, 4, 1, 23688, 1, 1, 5),
    _Rssi_Type()
)
rssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rssi.setStatus("mandatory")
_Ebno_Type = Gauge32
_Ebno_Object = MibScalar
ebno = _Ebno_Object(
    (1, 3, 6, 1, 4, 1, 23688, 1, 1, 6),
    _Ebno_Type()
)
ebno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebno.setStatus("mandatory")
_Berr_Type = Gauge32
_Berr_Object = MibScalar
berr = _Berr_Object(
    (1, 3, 6, 1, 4, 1, 23688, 1, 1, 7),
    _Berr_Type()
)
berr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berr.setStatus("mandatory")
_Temperature_Type = Integer32
_Temperature_Object = MibScalar
temperature = _Temperature_Object(
    (1, 3, 6, 1, 4, 1, 23688, 1, 1, 8),
    _Temperature_Type()
)
temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature.setStatus("mandatory")
_MaxENspeed_Type = Integer32
_MaxENspeed_Object = MibScalar
maxENspeed = _MaxENspeed_Object(
    (1, 3, 6, 1, 4, 1, 23688, 1, 1, 9),
    _MaxENspeed_Type()
)
maxENspeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxENspeed.setStatus("mandatory")
_CurrentRadioSpeed_Type = Integer32
_CurrentRadioSpeed_Object = MibScalar
currentRadioSpeed = _CurrentRadioSpeed_Object(
    (1, 3, 6, 1, 4, 1, 23688, 1, 1, 10),
    _CurrentRadioSpeed_Type()
)
currentRadioSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentRadioSpeed.setStatus("mandatory")
_Type_Type = DisplayString
_Type_Object = MibScalar
type = _Type_Object(
    (1, 3, 6, 1, 4, 1, 23688, 1, 1, 11),
    _Type_Type()
)
type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    type.setStatus("mandatory")
_TxFreq_Type = DisplayString
_TxFreq_Object = MibScalar
txFreq = _TxFreq_Object(
    (1, 3, 6, 1, 4, 1, 23688, 1, 1, 12),
    _TxFreq_Type()
)
txFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txFreq.setStatus("mandatory")
_RxFreq_Type = DisplayString
_RxFreq_Object = MibScalar
rxFreq = _RxFreq_Object(
    (1, 3, 6, 1, 4, 1, 23688, 1, 1, 13),
    _RxFreq_Type()
)
rxFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxFreq.setStatus("mandatory")
_TxDataSpeed_Type = Gauge32
_TxDataSpeed_Object = MibScalar
txDataSpeed = _TxDataSpeed_Object(
    (1, 3, 6, 1, 4, 1, 23688, 1, 1, 14),
    _TxDataSpeed_Type()
)
txDataSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txDataSpeed.setStatus("mandatory")
_RxDataSpeed_Type = Gauge32
_RxDataSpeed_Object = MibScalar
rxDataSpeed = _RxDataSpeed_Object(
    (1, 3, 6, 1, 4, 1, 23688, 1, 1, 15),
    _RxDataSpeed_Type()
)
rxDataSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxDataSpeed.setStatus("mandatory")
_RemoteName_Type = DisplayString
_RemoteName_Object = MibScalar
remoteName = _RemoteName_Object(
    (1, 3, 6, 1, 4, 1, 23688, 1, 1, 16),
    _RemoteName_Type()
)
remoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteName.setStatus("mandatory")
_RemoteIPaddress_Type = IpAddress
_RemoteIPaddress_Object = MibScalar
remoteIPaddress = _RemoteIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 23688, 1, 1, 17),
    _RemoteIPaddress_Type()
)
remoteIPaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIPaddress.setStatus("mandatory")


class _Atpc_Type(Integer32):
    """Custom type atpc based on Integer32"""
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


_Atpc_Type.__name__ = "Integer32"
_Atpc_Object = MibScalar
atpc = _Atpc_Object(
    (1, 3, 6, 1, 4, 1, 23688, 1, 1, 18),
    _Atpc_Type()
)
atpc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atpc.setStatus("mandatory")
_TxPower_Type = Gauge32
_TxPower_Object = MibScalar
txPower = _TxPower_Object(
    (1, 3, 6, 1, 4, 1, 23688, 1, 1, 19),
    _TxPower_Type()
)
txPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txPower.setStatus("mandatory")


class _Acm_Type(Integer32):
    """Custom type acm based on Integer32"""
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


_Acm_Type.__name__ = "Integer32"
_Acm_Object = MibScalar
acm = _Acm_Object(
    (1, 3, 6, 1, 4, 1, 23688, 1, 1, 20),
    _Acm_Type()
)
acm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acm.setStatus("mandatory")


class _TxModulation_Type(Integer32):
    """Custom type txModulation based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("qam-1024", 10),
          ("qam-128", 7),
          ("qam-16", 4),
          ("qam-2", 1),
          ("qam-256", 8),
          ("qam-32", 5),
          ("qam-4", 2),
          ("qam-512", 9),
          ("qam-64", 6),
          ("qam-8", 3))
    )


_TxModulation_Type.__name__ = "Integer32"
_TxModulation_Object = MibScalar
txModulation = _TxModulation_Object(
    (1, 3, 6, 1, 4, 1, 23688, 1, 1, 21),
    _TxModulation_Type()
)
txModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txModulation.setStatus("mandatory")


class _RxModulation_Type(Integer32):
    """Custom type rxModulation based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("qam-1024", 10),
          ("qam-128", 7),
          ("qam-16", 4),
          ("qam-2", 1),
          ("qam-256", 8),
          ("qam-32", 5),
          ("qam-4", 2),
          ("qam-512", 9),
          ("qam-64", 6),
          ("qam-8", 3))
    )


_RxModulation_Type.__name__ = "Integer32"
_RxModulation_Object = MibScalar
rxModulation = _RxModulation_Object(
    (1, 3, 6, 1, 4, 1, 23688, 1, 1, 22),
    _RxModulation_Type()
)
rxModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxModulation.setStatus("mandatory")
_TxBandwidth_Type = Gauge32
_TxBandwidth_Object = MibScalar
txBandwidth = _TxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 23688, 1, 1, 23),
    _TxBandwidth_Type()
)
txBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txBandwidth.setStatus("mandatory")
_RxBandwidth_Type = Gauge32
_RxBandwidth_Object = MibScalar
rxBandwidth = _RxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 23688, 1, 1, 24),
    _RxBandwidth_Type()
)
rxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxBandwidth.setStatus("mandatory")
_LicenseExpire_Type = Gauge32
_LicenseExpire_Object = MibScalar
licenseExpire = _LicenseExpire_Object(
    (1, 3, 6, 1, 4, 1, 23688, 1, 1, 25),
    _LicenseExpire_Type()
)
licenseExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseExpire.setStatus("mandatory")
_Summitd_Common_ObjectIdentity = ObjectIdentity
summitd_Common = _Summitd_Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23688, 2)
)
_Summitd_Experimental_ObjectIdentity = ObjectIdentity
summitd_Experimental = _Summitd_Experimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23688, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Summitd",
    **{"summit-development": summit_development,
       "summit-Products": summit_Products,
       "uni-a": uni_a,
       "name": name,
       "condition": condition,
       "mannum": mannum,
       "status": status,
       "rssi": rssi,
       "ebno": ebno,
       "berr": berr,
       "temperature": temperature,
       "maxENspeed": maxENspeed,
       "currentRadioSpeed": currentRadioSpeed,
       "type": type,
       "txFreq": txFreq,
       "rxFreq": rxFreq,
       "txDataSpeed": txDataSpeed,
       "rxDataSpeed": rxDataSpeed,
       "remoteName": remoteName,
       "remoteIPaddress": remoteIPaddress,
       "atpc": atpc,
       "txPower": txPower,
       "acm": acm,
       "txModulation": txModulation,
       "rxModulation": rxModulation,
       "txBandwidth": txBandwidth,
       "rxBandwidth": rxBandwidth,
       "licenseExpire": licenseExpire,
       "summitd-Common": summitd_Common,
       "summitd-Experimental": summitd_Experimental}
)
