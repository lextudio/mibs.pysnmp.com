# SNMP MIB module (TRANZEO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TRANZEO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:23 2024
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



class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Tranzeo_ObjectIdentity = ObjectIdentity
tranzeo = _Tranzeo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24575)
)
_Signal_ObjectIdentity = ObjectIdentity
signal = _Signal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24575, 1)
)
_Rssi_ObjectIdentity = ObjectIdentity
rssi = _Rssi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24575, 1, 1)
)


class _Signallow_Type(Integer32):
    """Custom type signallow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-110, 0),
    )


_Signallow_Type.__name__ = "Integer32"
_Signallow_Object = MibScalar
signallow = _Signallow_Object(
    (1, 3, 6, 1, 4, 1, 24575, 1, 1, 1),
    _Signallow_Type()
)
signallow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signallow.setStatus("mandatory")


class _Signalaverage_Type(Integer32):
    """Custom type signalaverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-110, 0),
    )


_Signalaverage_Type.__name__ = "Integer32"
_Signalaverage_Object = MibScalar
signalaverage = _Signalaverage_Object(
    (1, 3, 6, 1, 4, 1, 24575, 1, 1, 2),
    _Signalaverage_Type()
)
signalaverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalaverage.setStatus("mandatory")


class _Signalhigh_Type(Integer32):
    """Custom type signalhigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-110, 0),
    )


_Signalhigh_Type.__name__ = "Integer32"
_Signalhigh_Object = MibScalar
signalhigh = _Signalhigh_Object(
    (1, 3, 6, 1, 4, 1, 24575, 1, 1, 3),
    _Signalhigh_Type()
)
signalhigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalhigh.setStatus("mandatory")
_Noise_ObjectIdentity = ObjectIdentity
noise = _Noise_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24575, 1, 2)
)


class _Noiselow_Type(Integer32):
    """Custom type noiselow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-110, 0),
    )


_Noiselow_Type.__name__ = "Integer32"
_Noiselow_Object = MibScalar
noiselow = _Noiselow_Object(
    (1, 3, 6, 1, 4, 1, 24575, 1, 2, 1),
    _Noiselow_Type()
)
noiselow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiselow.setStatus("mandatory")


class _Noiseaverage_Type(Integer32):
    """Custom type noiseaverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-110, 0),
    )


_Noiseaverage_Type.__name__ = "Integer32"
_Noiseaverage_Object = MibScalar
noiseaverage = _Noiseaverage_Object(
    (1, 3, 6, 1, 4, 1, 24575, 1, 2, 2),
    _Noiseaverage_Type()
)
noiseaverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiseaverage.setStatus("mandatory")


class _Noisehigh_Type(Integer32):
    """Custom type noisehigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-110, 0),
    )


_Noisehigh_Type.__name__ = "Integer32"
_Noisehigh_Object = MibScalar
noisehigh = _Noisehigh_Object(
    (1, 3, 6, 1, 4, 1, 24575, 1, 2, 3),
    _Noisehigh_Type()
)
noisehigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noisehigh.setStatus("mandatory")
_ProbeConfig_ObjectIdentity = ObjectIdentity
probeConfig = _ProbeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24575, 2)
)


class _ProbeResetControl_Type(Integer32):
    """Custom type probeResetControl based on Integer32"""
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
        *(("autoconfig", 4),
          ("coldBoot", 3),
          ("running", 1),
          ("warmBoot", 2))
    )


_ProbeResetControl_Type.__name__ = "Integer32"
_ProbeResetControl_Object = MibScalar
probeResetControl = _ProbeResetControl_Object(
    (1, 3, 6, 1, 4, 1, 24575, 2, 1),
    _ProbeResetControl_Type()
)
probeResetControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probeResetControl.setStatus("mandatory")
_StationStat_ObjectIdentity = ObjectIdentity
stationStat = _StationStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24575, 3)
)


class _StnNumber_Type(Integer32):
    """Custom type stnNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_StnNumber_Type.__name__ = "Integer32"
_StnNumber_Object = MibScalar
stnNumber = _StnNumber_Object(
    (1, 3, 6, 1, 4, 1, 24575, 3, 1),
    _StnNumber_Type()
)
stnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNumber.setStatus("mandatory")
_AssocStation_ObjectIdentity = ObjectIdentity
assocStation = _AssocStation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24575, 4)
)
_StnIpAddr_Type = IpAddress
_StnIpAddr_Object = MibScalar
stnIpAddr = _StnIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 24575, 4, 1),
    _StnIpAddr_Type()
)
stnIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIpAddr.setStatus("mandatory")
_StnMacAddr_Type = PhysAddress
_StnMacAddr_Object = MibScalar
stnMacAddr = _StnMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 24575, 4, 2),
    _StnMacAddr_Type()
)
stnMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnMacAddr.setStatus("deprecated")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRANZEO-MIB",
    **{"PhysAddress": PhysAddress,
       "tranzeo": tranzeo,
       "signal": signal,
       "rssi": rssi,
       "signallow": signallow,
       "signalaverage": signalaverage,
       "signalhigh": signalhigh,
       "noise": noise,
       "noiselow": noiselow,
       "noiseaverage": noiseaverage,
       "noisehigh": noisehigh,
       "probeConfig": probeConfig,
       "probeResetControl": probeResetControl,
       "stationStat": stationStat,
       "stnNumber": stnNumber,
       "assocStation": assocStation,
       "stnIpAddr": stnIpAddr,
       "stnMacAddr": stnMacAddr}
)
