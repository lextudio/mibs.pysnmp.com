# SNMP MIB module (BROTHER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BROTHER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:36 2024
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Brother_ObjectIdentity = ObjectIdentity
brother = _Brother_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3)
)
_Net_peripheral_ObjectIdentity = ObjectIdentity
net_peripheral = _Net_peripheral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9)
)
_Net_printer_ObjectIdentity = ObjectIdentity
net_printer = _Net_printer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 1)
)
_GeneralDeviceStatus_ObjectIdentity = ObjectIdentity
generalDeviceStatus = _GeneralDeviceStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 1, 1)
)
_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 1, 1, 2)
)


class _BrJamPlace_Type(Integer32):
    """Custom type brJamPlace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_BrJamPlace_Type.__name__ = "Integer32"
_BrJamPlace_Object = MibScalar
brJamPlace = _BrJamPlace_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 1, 1, 2, 9),
    _BrJamPlace_Type()
)
brJamPlace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brJamPlace.setStatus("mandatory")
_Tonerlow_ObjectIdentity = ObjectIdentity
tonerlow = _Tonerlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 1, 1, 2, 10)
)


class _BrToner1Low_Type(Integer32):
    """Custom type brToner1Low based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_BrToner1Low_Type.__name__ = "Integer32"
_BrToner1Low_Object = MibScalar
brToner1Low = _BrToner1Low_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 1, 1, 2, 10, 1),
    _BrToner1Low_Type()
)
brToner1Low.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brToner1Low.setStatus("mandatory")


class _BrToner2Low_Type(Integer32):
    """Custom type brToner2Low based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_BrToner2Low_Type.__name__ = "Integer32"
_BrToner2Low_Object = MibScalar
brToner2Low = _BrToner2Low_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 1, 1, 2, 10, 2),
    _BrToner2Low_Type()
)
brToner2Low.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brToner2Low.setStatus("mandatory")


class _BrToner3Low_Type(Integer32):
    """Custom type brToner3Low based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_BrToner3Low_Type.__name__ = "Integer32"
_BrToner3Low_Object = MibScalar
brToner3Low = _BrToner3Low_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 1, 1, 2, 10, 3),
    _BrToner3Low_Type()
)
brToner3Low.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brToner3Low.setStatus("mandatory")


class _BrToner4Low_Type(Integer32):
    """Custom type brToner4Low based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_BrToner4Low_Type.__name__ = "Integer32"
_BrToner4Low_Object = MibScalar
brToner4Low = _BrToner4Low_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 1, 1, 2, 10, 4),
    _BrToner4Low_Type()
)
brToner4Low.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brToner4Low.setStatus("mandatory")
_Brieee1284id_Type = OctetString
_Brieee1284id_Object = MibScalar
brieee1284id = _Brieee1284id_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 1, 1, 7),
    _Brieee1284id_Type()
)
brieee1284id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brieee1284id.setStatus("mandatory")


class _Brttt1_Type(Integer32):
    """Custom type brttt1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Brttt1_Type.__name__ = "Integer32"
_Brttt1_Object = MibScalar
brttt1 = _Brttt1_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 1, 1, 10),
    _Brttt1_Type()
)
brttt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brttt1.setStatus("mandatory")
_Net_MFP_ObjectIdentity = ObjectIdentity
net_MFP = _Net_MFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2)
)
_Fax_setup_ObjectIdentity = ObjectIdentity
fax_setup = _Fax_setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 1)
)
_Autodial_ObjectIdentity = ObjectIdentity
autodial = _Autodial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 1, 1)
)
_OnetouchDial_ObjectIdentity = ObjectIdentity
onetouchDial = _OnetouchDial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 1, 1, 1)
)


class _BrOneTouchDialCount_Type(Integer32):
    """Custom type brOneTouchDialCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BrOneTouchDialCount_Type.__name__ = "Integer32"
_BrOneTouchDialCount_Object = MibScalar
brOneTouchDialCount = _BrOneTouchDialCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 1, 1, 1, 1),
    _BrOneTouchDialCount_Type()
)
brOneTouchDialCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brOneTouchDialCount.setStatus("mandatory")
_BrOneTouchDialTable_Object = MibTable
brOneTouchDialTable = _BrOneTouchDialTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    brOneTouchDialTable.setStatus("mandatory")
_BrOneTouchDialEntry_Object = MibTableRow
brOneTouchDialEntry = _BrOneTouchDialEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 1, 1, 1, 2, 1)
)
brOneTouchDialEntry.setIndexNames(
    (0, "BROTHER-MIB", "brOneTouchDialIndex"),
)
if mibBuilder.loadTexts:
    brOneTouchDialEntry.setStatus("mandatory")


class _BrOneTouchDialIndex_Type(Integer32):
    """Custom type brOneTouchDialIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BrOneTouchDialIndex_Type.__name__ = "Integer32"
_BrOneTouchDialIndex_Object = MibTableColumn
brOneTouchDialIndex = _BrOneTouchDialIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 1, 1, 1, 2, 1, 1),
    _BrOneTouchDialIndex_Type()
)
brOneTouchDialIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brOneTouchDialIndex.setStatus("mandatory")
_BrOneTouchDialData_Type = OctetString
_BrOneTouchDialData_Object = MibTableColumn
brOneTouchDialData = _BrOneTouchDialData_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 1, 1, 1, 2, 1, 2),
    _BrOneTouchDialData_Type()
)
brOneTouchDialData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brOneTouchDialData.setStatus("mandatory")
_SpeedDial_ObjectIdentity = ObjectIdentity
speedDial = _SpeedDial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 1, 1, 2)
)


class _BrSpeedDialCount_Type(Integer32):
    """Custom type brSpeedDialCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BrSpeedDialCount_Type.__name__ = "Integer32"
_BrSpeedDialCount_Object = MibScalar
brSpeedDialCount = _BrSpeedDialCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 1, 1, 2, 1),
    _BrSpeedDialCount_Type()
)
brSpeedDialCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brSpeedDialCount.setStatus("mandatory")
_BrSpeedDialTable_Object = MibTable
brSpeedDialTable = _BrSpeedDialTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    brSpeedDialTable.setStatus("mandatory")
_BrSpeedDialEntry_Object = MibTableRow
brSpeedDialEntry = _BrSpeedDialEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 1, 1, 2, 2, 1)
)
brSpeedDialEntry.setIndexNames(
    (0, "BROTHER-MIB", "brSpeedDialIndex"),
)
if mibBuilder.loadTexts:
    brSpeedDialEntry.setStatus("mandatory")


class _BrSpeedDialIndex_Type(Integer32):
    """Custom type brSpeedDialIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BrSpeedDialIndex_Type.__name__ = "Integer32"
_BrSpeedDialIndex_Object = MibTableColumn
brSpeedDialIndex = _BrSpeedDialIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 1, 1, 2, 2, 1, 1),
    _BrSpeedDialIndex_Type()
)
brSpeedDialIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brSpeedDialIndex.setStatus("mandatory")
_BrSpeedDialData_Type = OctetString
_BrSpeedDialData_Object = MibTableColumn
brSpeedDialData = _BrSpeedDialData_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 1, 1, 2, 2, 1, 2),
    _BrSpeedDialData_Type()
)
brSpeedDialData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brSpeedDialData.setStatus("mandatory")


class _BrDialDataAllClear_Type(Integer32):
    """Custom type brDialDataAllClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BrDialDataAllClear_Type.__name__ = "Integer32"
_BrDialDataAllClear_Object = MibScalar
brDialDataAllClear = _BrDialDataAllClear_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 1, 1, 3),
    _BrDialDataAllClear_Type()
)
brDialDataAllClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brDialDataAllClear.setStatus("mandatory")
_Fax_general_ObjectIdentity = ObjectIdentity
fax_general = _Fax_general_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 1, 2)
)
_BrFaxReceiveMode_Type = Integer32
_BrFaxReceiveMode_Object = MibScalar
brFaxReceiveMode = _BrFaxReceiveMode_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 1, 2, 1),
    _BrFaxReceiveMode_Type()
)
brFaxReceiveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brFaxReceiveMode.setStatus("mandatory")


class _BrRingDelayCount_Type(Integer32):
    """Custom type brRingDelayCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_BrRingDelayCount_Type.__name__ = "Integer32"
_BrRingDelayCount_Object = MibScalar
brRingDelayCount = _BrRingDelayCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 1, 2, 2),
    _BrRingDelayCount_Type()
)
brRingDelayCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brRingDelayCount.setStatus("mandatory")
_BrOwnFaxNumber_Type = OctetString
_BrOwnFaxNumber_Object = MibScalar
brOwnFaxNumber = _BrOwnFaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 1, 2, 3),
    _BrOwnFaxNumber_Type()
)
brOwnFaxNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brOwnFaxNumber.setStatus("mandatory")
_Scanner_setup_ObjectIdentity = ObjectIdentity
scanner_setup = _Scanner_setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 11)
)
_ScanToInfo_ObjectIdentity = ObjectIdentity
scanToInfo = _ScanToInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 11, 1)
)
_BrRegisterKeyInfo_Type = OctetString
_BrRegisterKeyInfo_Object = MibScalar
brRegisterKeyInfo = _BrRegisterKeyInfo_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 11, 1, 1),
    _BrRegisterKeyInfo_Type()
)
brRegisterKeyInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brRegisterKeyInfo.setStatus("mandatory")
_BrUnRegisterKeyInfo_Type = OctetString
_BrUnRegisterKeyInfo_Object = MibScalar
brUnRegisterKeyInfo = _BrUnRegisterKeyInfo_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 11, 1, 2),
    _BrUnRegisterKeyInfo_Type()
)
brUnRegisterKeyInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brUnRegisterKeyInfo.setStatus("mandatory")


class _BrNetSKeyReceiverAddress_Type(OctetString):
    """Custom type brNetSKeyReceiverAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_BrNetSKeyReceiverAddress_Type.__name__ = "OctetString"
_BrNetSKeyReceiverAddress_Object = MibScalar
brNetSKeyReceiverAddress = _BrNetSKeyReceiverAddress_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 11, 1, 5),
    _BrNetSKeyReceiverAddress_Type()
)
brNetSKeyReceiverAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brNetSKeyReceiverAddress.setStatus("mandatory")
_MfpCapability_ObjectIdentity = ObjectIdentity
mfpCapability = _MfpCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 101)
)
_McGeneral_ObjectIdentity = ObjectIdentity
mcGeneral = _McGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 101, 1)
)
_McgRemoteSetup_ObjectIdentity = ObjectIdentity
mcgRemoteSetup = _McgRemoteSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 101, 1, 11)
)


class _BrNetRemoteSetUpSupported_Type(Integer32):
    """Custom type brNetRemoteSetUpSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrNetRemoteSetUpSupported_Type.__name__ = "Integer32"
_BrNetRemoteSetUpSupported_Object = MibScalar
brNetRemoteSetUpSupported = _BrNetRemoteSetUpSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 101, 1, 11, 1),
    _BrNetRemoteSetUpSupported_Type()
)
brNetRemoteSetUpSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brNetRemoteSetUpSupported.setStatus("mandatory")


class _BrNetRemoteSetUpEnable_Type(Integer32):
    """Custom type brNetRemoteSetUpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrNetRemoteSetUpEnable_Type.__name__ = "Integer32"
_BrNetRemoteSetUpEnable_Object = MibScalar
brNetRemoteSetUpEnable = _BrNetRemoteSetUpEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 101, 1, 11, 2),
    _BrNetRemoteSetUpEnable_Type()
)
brNetRemoteSetUpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brNetRemoteSetUpEnable.setStatus("mandatory")


class _BrNetRemoteSetUpFileFormat_Type(Integer32):
    """Custom type brNetRemoteSetUpFileFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rmd", 2),
          ("rms", 1),
          ("rmsrmd", 3))
    )


_BrNetRemoteSetUpFileFormat_Type.__name__ = "Integer32"
_BrNetRemoteSetUpFileFormat_Object = MibScalar
brNetRemoteSetUpFileFormat = _BrNetRemoteSetUpFileFormat_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 101, 1, 11, 3),
    _BrNetRemoteSetUpFileFormat_Type()
)
brNetRemoteSetUpFileFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brNetRemoteSetUpFileFormat.setStatus("mandatory")
_McFax_ObjectIdentity = ObjectIdentity
mcFax = _McFax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 101, 2)
)
_McfGeneral_ObjectIdentity = ObjectIdentity
mcfGeneral = _McfGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 101, 2, 1)
)


class _BrFaxSupported_Type(Integer32):
    """Custom type brFaxSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrFaxSupported_Type.__name__ = "Integer32"
_BrFaxSupported_Object = MibScalar
brFaxSupported = _BrFaxSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 101, 2, 1, 1),
    _BrFaxSupported_Type()
)
brFaxSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFaxSupported.setStatus("mandatory")


class _BrIFaxSupported_Type(Integer32):
    """Custom type brIFaxSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrIFaxSupported_Type.__name__ = "Integer32"
_BrIFaxSupported_Object = MibScalar
brIFaxSupported = _BrIFaxSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 101, 2, 1, 3),
    _BrIFaxSupported_Type()
)
brIFaxSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIFaxSupported.setStatus("mandatory")
_McfNetFaxShare_ObjectIdentity = ObjectIdentity
mcfNetFaxShare = _McfNetFaxShare_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 101, 2, 11)
)


class _BrNetFaxShareSupported_Type(Integer32):
    """Custom type brNetFaxShareSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrNetFaxShareSupported_Type.__name__ = "Integer32"
_BrNetFaxShareSupported_Object = MibScalar
brNetFaxShareSupported = _BrNetFaxShareSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 101, 2, 11, 1),
    _BrNetFaxShareSupported_Type()
)
brNetFaxShareSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brNetFaxShareSupported.setStatus("mandatory")


class _BrNetFaxShareEnable_Type(Integer32):
    """Custom type brNetFaxShareEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrNetFaxShareEnable_Type.__name__ = "Integer32"
_BrNetFaxShareEnable_Object = MibScalar
brNetFaxShareEnable = _BrNetFaxShareEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 101, 2, 11, 2),
    _BrNetFaxShareEnable_Type()
)
brNetFaxShareEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brNetFaxShareEnable.setStatus("mandatory")
_McfNetPcFaxRx_ObjectIdentity = ObjectIdentity
mcfNetPcFaxRx = _McfNetPcFaxRx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 101, 2, 12)
)


class _BrNetPcFaxRxSupported_Type(Integer32):
    """Custom type brNetPcFaxRxSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrNetPcFaxRxSupported_Type.__name__ = "Integer32"
_BrNetPcFaxRxSupported_Object = MibScalar
brNetPcFaxRxSupported = _BrNetPcFaxRxSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 101, 2, 12, 1),
    _BrNetPcFaxRxSupported_Type()
)
brNetPcFaxRxSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brNetPcFaxRxSupported.setStatus("mandatory")


class _BrNetPcFaxRxEnable_Type(Integer32):
    """Custom type brNetPcFaxRxEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrNetPcFaxRxEnable_Type.__name__ = "Integer32"
_BrNetPcFaxRxEnable_Object = MibScalar
brNetPcFaxRxEnable = _BrNetPcFaxRxEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 101, 2, 12, 2),
    _BrNetPcFaxRxEnable_Type()
)
brNetPcFaxRxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brNetPcFaxRxEnable.setStatus("mandatory")
_BrNetRegisterPcFaxInfo_Type = OctetString
_BrNetRegisterPcFaxInfo_Object = MibScalar
brNetRegisterPcFaxInfo = _BrNetRegisterPcFaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 101, 2, 12, 3),
    _BrNetRegisterPcFaxInfo_Type()
)
brNetRegisterPcFaxInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brNetRegisterPcFaxInfo.setStatus("mandatory")
_McfFaxInfomation_ObjectIdentity = ObjectIdentity
mcfFaxInfomation = _McfFaxInfomation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 101, 2, 101)
)


class _BrPhoneNumberLastFax_Type(OctetString):
    """Custom type brPhoneNumberLastFax based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_BrPhoneNumberLastFax_Type.__name__ = "OctetString"
_BrPhoneNumberLastFax_Object = MibScalar
brPhoneNumberLastFax = _BrPhoneNumberLastFax_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 101, 2, 101, 1),
    _BrPhoneNumberLastFax_Type()
)
brPhoneNumberLastFax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPhoneNumberLastFax.setStatus("mandatory")
_BrPagesSentLastFax_Type = Counter32
_BrPagesSentLastFax_Object = MibScalar
brPagesSentLastFax = _BrPagesSentLastFax_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 101, 2, 101, 2),
    _BrPagesSentLastFax_Type()
)
brPagesSentLastFax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPagesSentLastFax.setStatus("mandatory")
_BrTimestampLastFax_Type = DateAndTime
_BrTimestampLastFax_Object = MibScalar
brTimestampLastFax = _BrTimestampLastFax_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 101, 2, 101, 3),
    _BrTimestampLastFax_Type()
)
brTimestampLastFax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brTimestampLastFax.setStatus("mandatory")


class _BrFaxHeaderInfo_Type(DisplayString):
    """Custom type brFaxHeaderInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_BrFaxHeaderInfo_Type.__name__ = "DisplayString"
_BrFaxHeaderInfo_Object = MibScalar
brFaxHeaderInfo = _BrFaxHeaderInfo_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 101, 2, 101, 4),
    _BrFaxHeaderInfo_Type()
)
brFaxHeaderInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brFaxHeaderInfo.setStatus("mandatory")
_McScanner_ObjectIdentity = ObjectIdentity
mcScanner = _McScanner_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 101, 3)
)
_McsNetScanner_ObjectIdentity = ObjectIdentity
mcsNetScanner = _McsNetScanner_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 101, 3, 11)
)


class _BrNetScannerSupported_Type(Integer32):
    """Custom type brNetScannerSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrNetScannerSupported_Type.__name__ = "Integer32"
_BrNetScannerSupported_Object = MibScalar
brNetScannerSupported = _BrNetScannerSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 101, 3, 11, 1),
    _BrNetScannerSupported_Type()
)
brNetScannerSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brNetScannerSupported.setStatus("mandatory")


class _BrNetScannerEnable_Type(Integer32):
    """Custom type brNetScannerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrNetScannerEnable_Type.__name__ = "Integer32"
_BrNetScannerEnable_Object = MibScalar
brNetScannerEnable = _BrNetScannerEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 101, 3, 11, 2),
    _BrNetScannerEnable_Type()
)
brNetScannerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brNetScannerEnable.setStatus("mandatory")
_McsNetSKy_ObjectIdentity = ObjectIdentity
mcsNetSKy = _McsNetSKy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 101, 3, 12)
)


class _BrNetSKeySupported_Type(Integer32):
    """Custom type brNetSKeySupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrNetSKeySupported_Type.__name__ = "Integer32"
_BrNetSKeySupported_Object = MibScalar
brNetSKeySupported = _BrNetSKeySupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 101, 3, 12, 1),
    _BrNetSKeySupported_Type()
)
brNetSKeySupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brNetSKeySupported.setStatus("mandatory")


class _BrNetSKeyEnable_Type(Integer32):
    """Custom type brNetSKeyEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrNetSKeyEnable_Type.__name__ = "Integer32"
_BrNetSKeyEnable_Object = MibScalar
brNetSKeyEnable = _BrNetSKeyEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 101, 3, 12, 2),
    _BrNetSKeyEnable_Type()
)
brNetSKeyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brNetSKeyEnable.setStatus("mandatory")
_Mfpgeneral_setup_ObjectIdentity = ObjectIdentity
mfpgeneral_setup = _Mfpgeneral_setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 111)
)
_BrServiceMode_Type = OctetString
_BrServiceMode_Object = MibScalar
brServiceMode = _BrServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 111, 1),
    _BrServiceMode_Type()
)
brServiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brServiceMode.setStatus("mandatory")


class _BrLockMode_Type(Integer32):
    """Custom type brLockMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BrLockMode_Type.__name__ = "Integer32"
_BrLockMode_Object = MibScalar
brLockMode = _BrLockMode_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 111, 2),
    _BrLockMode_Type()
)
brLockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLockMode.setStatus("mandatory")
_BrActivityReportSetting_Type = Integer32
_BrActivityReportSetting_Object = MibScalar
brActivityReportSetting = _BrActivityReportSetting_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 2, 111, 3),
    _BrActivityReportSetting_Type()
)
brActivityReportSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brActivityReportSetting.setStatus("mandatory")
_NetPML_ObjectIdentity = ObjectIdentity
netPML = _NetPML_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4)
)
_NetPMLmgmt_ObjectIdentity = ObjectIdentity
netPMLmgmt = _NetPMLmgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2)
)
_Device_ObjectIdentity = ObjectIdentity
device = _Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1)
)
_Destination_subsystem1_ObjectIdentity = ObjectIdentity
destination_subsystem1 = _Destination_subsystem1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 1)
)
_Sleep_ObjectIdentity = ObjectIdentity
sleep = _Sleep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 1, 1)
)


class _Brpowerstime_Type(Integer32):
    """Custom type brpowerstime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Brpowerstime_Type.__name__ = "Integer32"
_Brpowerstime_Object = MibScalar
brpowerstime = _Brpowerstime_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 1, 1, 1),
    _Brpowerstime_Type()
)
brpowerstime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpowerstime.setStatus("mandatory")
_Autoc_ObjectIdentity = ObjectIdentity
autoc = _Autoc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 1, 2)
)


class _Brautocont_Type(Integer32):
    """Custom type brautocont based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Brautocont_Type.__name__ = "Integer32"
_Brautocont_Object = MibScalar
brautocont = _Brautocont_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 1, 2, 7),
    _Brautocont_Type()
)
brautocont.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brautocont.setStatus("mandatory")
_Simm_ObjectIdentity = ObjectIdentity
simm = _Simm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 1, 4)
)
_Specification_ObjectIdentity = ObjectIdentity
specification = _Specification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 1, 4, 1)
)
_Simmkind0_ObjectIdentity = ObjectIdentity
simmkind0 = _Simmkind0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 1, 4, 1, 1)
)
_Brsimmtype0_Type = Integer32
_Brsimmtype0_Object = MibScalar
brsimmtype0 = _Brsimmtype0_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 1, 4, 1, 1, 4),
    _Brsimmtype0_Type()
)
brsimmtype0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brsimmtype0.setStatus("mandatory")
_Brsimmsize0_Type = Integer32
_Brsimmsize0_Object = MibScalar
brsimmsize0 = _Brsimmsize0_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 1, 4, 1, 1, 5),
    _Brsimmsize0_Type()
)
brsimmsize0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brsimmsize0.setStatus("mandatory")
_Simmkind1_ObjectIdentity = ObjectIdentity
simmkind1 = _Simmkind1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 1, 4, 1, 2)
)
_Brsimmtype1_Type = Integer32
_Brsimmtype1_Object = MibScalar
brsimmtype1 = _Brsimmtype1_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 1, 4, 1, 2, 4),
    _Brsimmtype1_Type()
)
brsimmtype1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brsimmtype1.setStatus("mandatory")
_Brsimmsize1_Type = Integer32
_Brsimmsize1_Object = MibScalar
brsimmsize1 = _Brsimmsize1_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 1, 4, 1, 2, 5),
    _Brsimmsize1_Type()
)
brsimmsize1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brsimmsize1.setStatus("mandatory")
_Simmkind2_ObjectIdentity = ObjectIdentity
simmkind2 = _Simmkind2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 1, 4, 1, 3)
)
_Brsimmtype2_Type = Integer32
_Brsimmtype2_Object = MibScalar
brsimmtype2 = _Brsimmtype2_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 1, 4, 1, 3, 4),
    _Brsimmtype2_Type()
)
brsimmtype2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brsimmtype2.setStatus("mandatory")
_Brsimmsize2_Type = Integer32
_Brsimmsize2_Object = MibScalar
brsimmsize2 = _Brsimmsize2_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 1, 4, 1, 3, 5),
    _Brsimmsize2_Type()
)
brsimmsize2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brsimmsize2.setStatus("mandatory")
_Simmkind3_ObjectIdentity = ObjectIdentity
simmkind3 = _Simmkind3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 1, 4, 1, 4)
)
_Brsimmtype3_Type = Integer32
_Brsimmtype3_Object = MibScalar
brsimmtype3 = _Brsimmtype3_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 1, 4, 1, 4, 4),
    _Brsimmtype3_Type()
)
brsimmtype3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brsimmtype3.setStatus("mandatory")
_Brsimmsize3_Type = Integer32
_Brsimmsize3_Object = MibScalar
brsimmsize3 = _Brsimmsize3_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 1, 4, 1, 4, 5),
    _Brsimmsize3_Type()
)
brsimmsize3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brsimmsize3.setStatus("mandatory")
_Bio1_explanation_ObjectIdentity = ObjectIdentity
bio1_explanation = _Bio1_explanation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 1, 4, 3)
)
_Determined_ObjectIdentity = ObjectIdentity
determined = _Determined_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 1, 4, 3, 1)
)


class _BrTBD1_Type(Integer32):
    """Custom type brTBD1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_BrTBD1_Type.__name__ = "Integer32"
_BrTBD1_Object = MibScalar
brTBD1 = _BrTBD1_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 1, 4, 3, 1, 4),
    _BrTBD1_Type()
)
brTBD1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brTBD1.setStatus("mandatory")
_Destination_subsystem2_ObjectIdentity = ObjectIdentity
destination_subsystem2 = _Destination_subsystem2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 2)
)
_Printerjob_ObjectIdentity = ObjectIdentity
printerjob = _Printerjob_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 2, 1)
)
_Jobend_ObjectIdentity = ObjectIdentity
jobend = _Jobend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 2, 1, 1)
)


class _Brtimeout_Type(Integer32):
    """Custom type brtimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Brtimeout_Type.__name__ = "Integer32"
_Brtimeout_Object = MibScalar
brtimeout = _Brtimeout_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 2, 1, 1, 1),
    _Brtimeout_Type()
)
brtimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brtimeout.setStatus("mandatory")


class _BrTBD2_Type(Integer32):
    """Custom type brTBD2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_BrTBD2_Type.__name__ = "Integer32"
_BrTBD2_Object = MibScalar
brTBD2 = _BrTBD2_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 2, 1, 1, 5),
    _BrTBD2_Type()
)
brTBD2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brTBD2.setStatus("mandatory")
_Destination_subsystem3_ObjectIdentity = ObjectIdentity
destination_subsystem3 = _Destination_subsystem3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 3)
)
_Prt_setup_ObjectIdentity = ObjectIdentity
prt_setup = _Prt_setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 3, 3)
)
_Prt_condition_ObjectIdentity = ObjectIdentity
prt_condition = _Prt_condition_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 3, 3, 1)
)


class _Brpersonality_Type(Integer32):
    """Custom type brpersonality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("auto", 5),
          ("epson", 7),
          ("hbp", 8),
          ("hpgl", 2),
          ("ibm", 6),
          ("pcl", 1),
          ("ps", 4))
    )


_Brpersonality_Type.__name__ = "Integer32"
_Brpersonality_Object = MibScalar
brpersonality = _Brpersonality_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 3, 3, 1, 1),
    _Brpersonality_Type()
)
brpersonality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpersonality.setStatus("mandatory")


class _Brorientation_Type(Integer32):
    """Custom type brorientation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Brorientation_Type.__name__ = "Integer32"
_Brorientation_Object = MibScalar
brorientation = _Brorientation_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 3, 3, 1, 2),
    _Brorientation_Type()
)
brorientation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brorientation.setStatus("mandatory")


class _Brcopies_Type(Integer32):
    """Custom type brcopies based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_Brcopies_Type.__name__ = "Integer32"
_Brcopies_Object = MibScalar
brcopies = _Brcopies_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 3, 3, 1, 4),
    _Brcopies_Type()
)
brcopies.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcopies.setStatus("mandatory")


class _BrTBD3_Type(Integer32):
    """Custom type brTBD3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_BrTBD3_Type.__name__ = "Integer32"
_BrTBD3_Object = MibScalar
brTBD3 = _BrTBD3_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 3, 3, 1, 6),
    _BrTBD3_Type()
)
brTBD3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brTBD3.setStatus("mandatory")


class _Brresolution_Type(Integer32):
    """Custom type brresolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1200),
    )


_Brresolution_Type.__name__ = "Integer32"
_Brresolution_Object = MibScalar
brresolution = _Brresolution_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 3, 3, 1, 8),
    _Brresolution_Type()
)
brresolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brresolution.setStatus("mandatory")


class _Brpageprotect_Type(Integer32):
    """Custom type brpageprotect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_Brpageprotect_Type.__name__ = "Integer32"
_Brpageprotect_Object = MibScalar
brpageprotect = _Brpageprotect_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 3, 3, 1, 10),
    _Brpageprotect_Type()
)
brpageprotect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpageprotect.setStatus("mandatory")


class _Brlines_Type(Integer32):
    """Custom type brlines based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 128),
    )


_Brlines_Type.__name__ = "Integer32"
_Brlines_Object = MibScalar
brlines = _Brlines_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 3, 3, 1, 11),
    _Brlines_Type()
)
brlines.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brlines.setStatus("mandatory")


class _Brpaper_Type(Integer32):
    """Custom type brpaper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              24,
              25,
              26,
              27,
              45,
              46,
              80,
              81,
              90,
              91,
              99,
              100,
              890,
              891,
              892,
              893,
              894,
              895,
              896,
              897,
              898,
              899,
              900,
              901,
              902,
              903,
              904,
              905,
              906,
              907,
              908,
              911,
              920,
              921,
              922,
              923,
              924,
              925,
              926,
              927,
              1001)
        )
    )
    namedValues = NamedValues(
        *(("a3ISO", 27),
          ("a3PLUS", 891),
          ("a4", 26),
          ("a4LONG", 894),
          ("a4Letter", 898),
          ("a4ShortEdge", 893),
          ("a5", 25),
          ("a5l", 923),
          ("a6", 24),
          ("auto", 1001),
          ("b4JIS", 46),
          ("b5", 100),
          ("b5Executive", 899),
          ("b5ISOShortEdge", 896),
          ("b5JIS", 45),
          ("b6", 99),
          ("b6JIS", 924),
          ("c5", 91),
          ("com10", 81),
          ("custom", 897),
          ("detectsensor", 911),
          ("dl", 90),
          ("dll", 901),
          ("envelopes", 900),
          ("envelopesY4", 921),
          ("executive", 1),
          ("executiveShortEdge", 895),
          ("folio", 903),
          ("hagaki", 902),
          ("inches3x5", 920),
          ("largestEnvelopesTheWest", 922),
          ("ledger", 890),
          ("legal", 3),
          ("letter", 2),
          ("letterShortEdge", 892),
          ("monarch", 80),
          ("organaizerJ", 904),
          ("organaizerK", 905),
          ("organaizerL", 906),
          ("organaizerM", 907),
          ("prc16k184x260", 926),
          ("prc16k195x270", 925),
          ("prc16k197x273", 927),
          ("userdefined", 908))
    )


_Brpaper_Type.__name__ = "Integer32"
_Brpaper_Object = MibScalar
brpaper = _Brpaper_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 3, 3, 1, 13),
    _Brpaper_Type()
)
brpaper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpaper.setStatus("mandatory")
_Brpapertype_Type = Integer32
_Brpapertype_Object = MibScalar
brpapertype = _Brpapertype_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 3, 3, 1, 22),
    _Brpapertype_Type()
)
brpapertype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpapertype.setStatus("mandatory")
_Brpapertype2_Type = Integer32
_Brpapertype2_Object = MibScalar
brpapertype2 = _Brpapertype2_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 3, 3, 1, 23),
    _Brpapertype2_Type()
)
brpapertype2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpapertype2.setStatus("mandatory")
_BrpapertypeMP_Type = Integer32
_BrpapertypeMP_Object = MibScalar
brpapertypeMP = _BrpapertypeMP_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 3, 3, 1, 26),
    _BrpapertypeMP_Type()
)
brpapertypeMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpapertypeMP.setStatus("mandatory")
_Destination_subsystem4_ObjectIdentity = ObjectIdentity
destination_subsystem4 = _Destination_subsystem4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 4)
)
_Print_engine_ObjectIdentity = ObjectIdentity
print_engine = _Print_engine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 4, 1)
)
_Prt_density_ObjectIdentity = ObjectIdentity
prt_density = _Prt_density_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 4, 1, 1)
)


class _Brdensity_Type(Integer32):
    """Custom type brdensity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-15, 15),
    )


_Brdensity_Type.__name__ = "Integer32"
_Brdensity_Object = MibScalar
brdensity = _Brdensity_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 4, 1, 1, 5),
    _Brdensity_Type()
)
brdensity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brdensity.setStatus("mandatory")
_Status_prt_eng_ObjectIdentity = ObjectIdentity
status_prt_eng = _Status_prt_eng_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 4, 1, 2)
)
_Tray_ObjectIdentity = ObjectIdentity
tray = _Tray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 4, 1, 3)
)
_Manual_ObjectIdentity = ObjectIdentity
manual = _Manual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 4, 1, 3, 1)
)


class _Brmanualfeed_Type(Integer32):
    """Custom type brmanualfeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Brmanualfeed_Type.__name__ = "Integer32"
_Brmanualfeed_Object = MibScalar
brmanualfeed = _Brmanualfeed_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 4, 1, 3, 1, 4),
    _Brmanualfeed_Type()
)
brmanualfeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brmanualfeed.setStatus("mandatory")
_Traysize_ObjectIdentity = ObjectIdentity
traysize = _Traysize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3)
)
_Mp_ObjectIdentity = ObjectIdentity
mp = _Mp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 1)
)


class _Brmpsize_Type(Integer32):
    """Custom type brmpsize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              24,
              25,
              26,
              27,
              45,
              46,
              80,
              81,
              90,
              91,
              99,
              100,
              890,
              891,
              892,
              893,
              894,
              895,
              896,
              897,
              898,
              899,
              900,
              901,
              902,
              903,
              904,
              905,
              906,
              907,
              908,
              911,
              920,
              921,
              922)
        )
    )
    namedValues = NamedValues(
        *(("a3ISO", 27),
          ("a3PLUS", 891),
          ("a4", 26),
          ("a4LONG", 894),
          ("a4Letter", 898),
          ("a4ShortEdge", 893),
          ("a5", 25),
          ("a6", 24),
          ("b4JIS", 46),
          ("b5", 100),
          ("b5Executive", 899),
          ("b5ISOShortEdge", 896),
          ("b5JIS", 45),
          ("b6", 99),
          ("c5", 91),
          ("com10", 81),
          ("custom", 897),
          ("detectsensor", 911),
          ("dl", 90),
          ("dll", 901),
          ("envelopes", 900),
          ("envelopesY4", 921),
          ("executive", 1),
          ("executiveShortEdge", 895),
          ("folio", 903),
          ("hagaki", 902),
          ("inches3x5", 920),
          ("largestEnvelopesTheWest", 922),
          ("ledger", 890),
          ("legal", 3),
          ("letter", 2),
          ("letterShortEdge", 892),
          ("monarch", 80),
          ("organaizerJ", 904),
          ("organaizerK", 905),
          ("organaizerL", 906),
          ("organaizerM", 907),
          ("userdefined", 908))
    )


_Brmpsize_Type.__name__ = "Integer32"
_Brmpsize_Object = MibScalar
brmpsize = _Brmpsize_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 1, 1),
    _Brmpsize_Type()
)
brmpsize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brmpsize.setStatus("mandatory")
_Cassette_ObjectIdentity = ObjectIdentity
cassette = _Cassette_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 2)
)


class _Brtray1size_Type(Integer32):
    """Custom type brtray1size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              24,
              25,
              26,
              27,
              45,
              46,
              80,
              81,
              90,
              91,
              99,
              100,
              890,
              891,
              892,
              893,
              894,
              895,
              896,
              897,
              898,
              899,
              900,
              901,
              902,
              903,
              904,
              905,
              906,
              907,
              908,
              911,
              920,
              921,
              922)
        )
    )
    namedValues = NamedValues(
        *(("a3ISO", 27),
          ("a3PLUS", 891),
          ("a4", 26),
          ("a4LONG", 894),
          ("a4Letter", 898),
          ("a4ShortEdge", 893),
          ("a5", 25),
          ("a6", 24),
          ("b4JIS", 46),
          ("b5", 100),
          ("b5Executive", 899),
          ("b5ISOShortEdge", 896),
          ("b5JIS", 45),
          ("b6", 99),
          ("c5", 91),
          ("com10", 81),
          ("custom", 897),
          ("detectsensor", 911),
          ("dl", 90),
          ("dll", 901),
          ("envelopes", 900),
          ("envelopesY4", 921),
          ("executive", 1),
          ("executiveShortEdge", 895),
          ("folio", 903),
          ("hagaki", 902),
          ("inches3x5", 920),
          ("largestEnvelopesTheWest", 922),
          ("ledger", 890),
          ("legal", 3),
          ("letter", 2),
          ("letterShortEdge", 892),
          ("monarch", 80),
          ("organaizerJ", 904),
          ("organaizerK", 905),
          ("organaizerL", 906),
          ("organaizerM", 907),
          ("userdefined", 908))
    )


_Brtray1size_Type.__name__ = "Integer32"
_Brtray1size_Object = MibScalar
brtray1size = _Brtray1size_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 2, 1),
    _Brtray1size_Type()
)
brtray1size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brtray1size.setStatus("mandatory")
_Cassette2_ObjectIdentity = ObjectIdentity
cassette2 = _Cassette2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 3)
)


class _Brtray2size_Type(Integer32):
    """Custom type brtray2size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              24,
              25,
              26,
              27,
              45,
              46,
              80,
              81,
              90,
              91,
              99,
              100,
              890,
              891,
              892,
              893,
              894,
              895,
              896,
              897,
              898,
              899,
              900,
              901,
              902,
              903,
              904,
              905,
              906,
              907,
              908,
              911,
              920,
              921,
              922)
        )
    )
    namedValues = NamedValues(
        *(("a3ISO", 27),
          ("a3PLUS", 891),
          ("a4", 26),
          ("a4LONG", 894),
          ("a4Letter", 898),
          ("a4ShortEdge", 893),
          ("a5", 25),
          ("a6", 24),
          ("b4JIS", 46),
          ("b5", 100),
          ("b5Executive", 899),
          ("b5ISOShortEdge", 896),
          ("b5JIS", 45),
          ("b6", 99),
          ("c5", 91),
          ("com10", 81),
          ("custom", 897),
          ("detectsensor", 911),
          ("dl", 90),
          ("dll", 901),
          ("envelopes", 900),
          ("envelopesY4", 921),
          ("executive", 1),
          ("executiveShortEdge", 895),
          ("folio", 903),
          ("hagaki", 902),
          ("inches3x5", 920),
          ("largestEnvelopesTheWest", 922),
          ("ledger", 890),
          ("legal", 3),
          ("letter", 2),
          ("letterShortEdge", 892),
          ("monarch", 80),
          ("organaizerJ", 904),
          ("organaizerK", 905),
          ("organaizerL", 906),
          ("organaizerM", 907),
          ("userdefined", 908))
    )


_Brtray2size_Type.__name__ = "Integer32"
_Brtray2size_Object = MibScalar
brtray2size = _Brtray2size_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 3, 1),
    _Brtray2size_Type()
)
brtray2size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brtray2size.setStatus("mandatory")
_Cassette3_ObjectIdentity = ObjectIdentity
cassette3 = _Cassette3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 4)
)


class _Brtray3size_Type(Integer32):
    """Custom type brtray3size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              24,
              25,
              26,
              27,
              45,
              46,
              80,
              81,
              90,
              91,
              99,
              100,
              890,
              891,
              892,
              893,
              894,
              895,
              896,
              897,
              898,
              899,
              900,
              901,
              902,
              903,
              904,
              905,
              906,
              907,
              908,
              911,
              920,
              921,
              922)
        )
    )
    namedValues = NamedValues(
        *(("a3ISO", 27),
          ("a3PLUS", 891),
          ("a4", 26),
          ("a4LONG", 894),
          ("a4Letter", 898),
          ("a4ShortEdge", 893),
          ("a5", 25),
          ("a6", 24),
          ("b4JIS", 46),
          ("b5", 100),
          ("b5Executive", 899),
          ("b5ISOShortEdge", 896),
          ("b5JIS", 45),
          ("b6", 99),
          ("c5", 91),
          ("com10", 81),
          ("custom", 897),
          ("detectsensor", 911),
          ("dl", 90),
          ("dll", 901),
          ("envelopes", 900),
          ("envelopesY4", 921),
          ("executive", 1),
          ("executiveShortEdge", 895),
          ("folio", 903),
          ("hagaki", 902),
          ("inches3x5", 920),
          ("largestEnvelopesTheWest", 922),
          ("ledger", 890),
          ("legal", 3),
          ("letter", 2),
          ("letterShortEdge", 892),
          ("monarch", 80),
          ("organaizerJ", 904),
          ("organaizerK", 905),
          ("organaizerL", 906),
          ("organaizerM", 907),
          ("userdefined", 908))
    )


_Brtray3size_Type.__name__ = "Integer32"
_Brtray3size_Object = MibScalar
brtray3size = _Brtray3size_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 4, 1),
    _Brtray3size_Type()
)
brtray3size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brtray3size.setStatus("mandatory")
_Cassette4_ObjectIdentity = ObjectIdentity
cassette4 = _Cassette4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 5)
)


class _Brtray4size_Type(Integer32):
    """Custom type brtray4size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              24,
              25,
              26,
              27,
              45,
              46,
              80,
              81,
              90,
              91,
              99,
              100,
              890,
              891,
              892,
              893,
              894,
              895,
              896,
              897,
              898,
              899,
              900,
              901,
              902,
              903,
              904,
              905,
              906,
              907,
              908,
              911,
              920,
              921,
              922)
        )
    )
    namedValues = NamedValues(
        *(("a3ISO", 27),
          ("a3PLUS", 891),
          ("a4", 26),
          ("a4LONG", 894),
          ("a4Letter", 898),
          ("a4ShortEdge", 893),
          ("a5", 25),
          ("a6", 24),
          ("b4JIS", 46),
          ("b5", 100),
          ("b5Executive", 899),
          ("b5ISOShortEdge", 896),
          ("b5JIS", 45),
          ("b6", 99),
          ("c5", 91),
          ("com10", 81),
          ("custom", 897),
          ("detectsensor", 911),
          ("dl", 90),
          ("dll", 901),
          ("envelopes", 900),
          ("envelopesY4", 921),
          ("executive", 1),
          ("executiveShortEdge", 895),
          ("folio", 903),
          ("hagaki", 902),
          ("inches3x5", 920),
          ("largestEnvelopesTheWest", 922),
          ("ledger", 890),
          ("legal", 3),
          ("letter", 2),
          ("letterShortEdge", 892),
          ("monarch", 80),
          ("organaizerJ", 904),
          ("organaizerK", 905),
          ("organaizerL", 906),
          ("organaizerM", 907),
          ("userdefined", 908))
    )


_Brtray4size_Type.__name__ = "Integer32"
_Brtray4size_Object = MibScalar
brtray4size = _Brtray4size_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 5, 1),
    _Brtray4size_Type()
)
brtray4size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brtray4size.setStatus("mandatory")
_Economy_ObjectIdentity = ObjectIdentity
economy = _Economy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 4, 1, 6)
)


class _Brret_Type(Integer32):
    """Custom type brret based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Brret_Type.__name__ = "Integer32"
_Brret_Object = MibScalar
brret = _Brret_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 4, 1, 6, 5),
    _Brret_Type()
)
brret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brret.setStatus("mandatory")


class _Breconomode_Type(Integer32):
    """Custom type breconomode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Breconomode_Type.__name__ = "Integer32"
_Breconomode_Object = MibScalar
breconomode = _Breconomode_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 4, 1, 6, 7),
    _Breconomode_Type()
)
breconomode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    breconomode.setStatus("mandatory")
_Brorg_ObjectIdentity = ObjectIdentity
brorg = _Brorg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5)
)
_Printersetup_ObjectIdentity = ObjectIdentity
printersetup = _Printersetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1)
)
_General_ObjectIdentity = ObjectIdentity
general = _General_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 1)
)


class _BrPrtGeneralEmulationTimeout_Type(Integer32):
    """Custom type brPrtGeneralEmulationTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_BrPrtGeneralEmulationTimeout_Type.__name__ = "Integer32"
_BrPrtGeneralEmulationTimeout_Object = MibScalar
brPrtGeneralEmulationTimeout = _BrPrtGeneralEmulationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 1, 1),
    _BrPrtGeneralEmulationTimeout_Type()
)
brPrtGeneralEmulationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtGeneralEmulationTimeout.setStatus("mandatory")


class _BrPrtGeneralFeeder_Type(Integer32):
    """Custom type brPrtGeneralFeeder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_BrPrtGeneralFeeder_Type.__name__ = "Integer32"
_BrPrtGeneralFeeder_Object = MibScalar
brPrtGeneralFeeder = _BrPrtGeneralFeeder_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 1, 2),
    _BrPrtGeneralFeeder_Type()
)
brPrtGeneralFeeder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtGeneralFeeder.setStatus("mandatory")


class _BrPrtGeneralPowerSave_Type(Integer32):
    """Custom type brPrtGeneralPowerSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BrPrtGeneralPowerSave_Type.__name__ = "Integer32"
_BrPrtGeneralPowerSave_Object = MibScalar
brPrtGeneralPowerSave = _BrPrtGeneralPowerSave_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 1, 3),
    _BrPrtGeneralPowerSave_Type()
)
brPrtGeneralPowerSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtGeneralPowerSave.setStatus("mandatory")


class _BrPrtGeneralBuzzer_Type(Integer32):
    """Custom type brPrtGeneralBuzzer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BrPrtGeneralBuzzer_Type.__name__ = "Integer32"
_BrPrtGeneralBuzzer_Object = MibScalar
brPrtGeneralBuzzer = _BrPrtGeneralBuzzer_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 1, 4),
    _BrPrtGeneralBuzzer_Type()
)
brPrtGeneralBuzzer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtGeneralBuzzer.setStatus("mandatory")


class _BrPrtGeneralColor_Type(Integer32):
    """Custom type brPrtGeneralColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_BrPrtGeneralColor_Type.__name__ = "Integer32"
_BrPrtGeneralColor_Object = MibScalar
brPrtGeneralColor = _BrPrtGeneralColor_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 1, 5),
    _BrPrtGeneralColor_Type()
)
brPrtGeneralColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtGeneralColor.setStatus("mandatory")


class _BrPrtGeneralDuplex_Type(Integer32):
    """Custom type brPrtGeneralDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BrPrtGeneralDuplex_Type.__name__ = "Integer32"
_BrPrtGeneralDuplex_Object = MibScalar
brPrtGeneralDuplex = _BrPrtGeneralDuplex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 1, 6),
    _BrPrtGeneralDuplex_Type()
)
brPrtGeneralDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtGeneralDuplex.setStatus("mandatory")


class _BrPrtGeneralBinding_Type(Integer32):
    """Custom type brPrtGeneralBinding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_BrPrtGeneralBinding_Type.__name__ = "Integer32"
_BrPrtGeneralBinding_Object = MibScalar
brPrtGeneralBinding = _BrPrtGeneralBinding_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 1, 7),
    _BrPrtGeneralBinding_Type()
)
brPrtGeneralBinding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtGeneralBinding.setStatus("mandatory")
_Advanced_ObjectIdentity = ObjectIdentity
advanced = _Advanced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2)
)


class _BrPrtAdvancedPriority_Type(Integer32):
    """Custom type brPrtAdvancedPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BrPrtAdvancedPriority_Type.__name__ = "Integer32"
_BrPrtAdvancedPriority_Object = MibScalar
brPrtAdvancedPriority = _BrPrtAdvancedPriority_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 1),
    _BrPrtAdvancedPriority_Type()
)
brPrtAdvancedPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtAdvancedPriority.setStatus("mandatory")


class _BrPrtAdvancedUseMPTrayFirst_Type(Integer32):
    """Custom type brPrtAdvancedUseMPTrayFirst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BrPrtAdvancedUseMPTrayFirst_Type.__name__ = "Integer32"
_BrPrtAdvancedUseMPTrayFirst_Object = MibScalar
brPrtAdvancedUseMPTrayFirst = _BrPrtAdvancedUseMPTrayFirst_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 2),
    _BrPrtAdvancedUseMPTrayFirst_Type()
)
brPrtAdvancedUseMPTrayFirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtAdvancedUseMPTrayFirst.setStatus("mandatory")


class _BrPrtAdvancedMPTrayFeed_Type(Integer32):
    """Custom type brPrtAdvancedMPTrayFeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BrPrtAdvancedMPTrayFeed_Type.__name__ = "Integer32"
_BrPrtAdvancedMPTrayFeed_Object = MibScalar
brPrtAdvancedMPTrayFeed = _BrPrtAdvancedMPTrayFeed_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 3),
    _BrPrtAdvancedMPTrayFeed_Type()
)
brPrtAdvancedMPTrayFeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtAdvancedMPTrayFeed.setStatus("mandatory")


class _BrPrtAdvancedXOffset_Type(Integer32):
    """Custom type brPrtAdvancedXOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 500),
    )


_BrPrtAdvancedXOffset_Type.__name__ = "Integer32"
_BrPrtAdvancedXOffset_Object = MibScalar
brPrtAdvancedXOffset = _BrPrtAdvancedXOffset_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 4),
    _BrPrtAdvancedXOffset_Type()
)
brPrtAdvancedXOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtAdvancedXOffset.setStatus("mandatory")


class _BrPrtAdvancedYOffset_Type(Integer32):
    """Custom type brPrtAdvancedYOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 500),
    )


_BrPrtAdvancedYOffset_Type.__name__ = "Integer32"
_BrPrtAdvancedYOffset_Object = MibScalar
brPrtAdvancedYOffset = _BrPrtAdvancedYOffset_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 5),
    _BrPrtAdvancedYOffset_Type()
)
brPrtAdvancedYOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtAdvancedYOffset.setStatus("mandatory")


class _BrPrtAdvancedImageCompression_Type(Integer32):
    """Custom type brPrtAdvancedImageCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BrPrtAdvancedImageCompression_Type.__name__ = "Integer32"
_BrPrtAdvancedImageCompression_Object = MibScalar
brPrtAdvancedImageCompression = _BrPrtAdvancedImageCompression_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 6),
    _BrPrtAdvancedImageCompression_Type()
)
brPrtAdvancedImageCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtAdvancedImageCompression.setStatus("mandatory")
_Autoff_ObjectIdentity = ObjectIdentity
autoff = _Autoff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 7)
)


class _BrPrtAdvancedAutoFormFeed_Type(Integer32):
    """Custom type brPrtAdvancedAutoFormFeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BrPrtAdvancedAutoFormFeed_Type.__name__ = "Integer32"
_BrPrtAdvancedAutoFormFeed_Object = MibScalar
brPrtAdvancedAutoFormFeed = _BrPrtAdvancedAutoFormFeed_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 7, 1),
    _BrPrtAdvancedAutoFormFeed_Type()
)
brPrtAdvancedAutoFormFeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtAdvancedAutoFormFeed.setStatus("mandatory")


class _BrPrtAdvancedAutoTimeout_Type(Integer32):
    """Custom type brPrtAdvancedAutoTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_BrPrtAdvancedAutoTimeout_Type.__name__ = "Integer32"
_BrPrtAdvancedAutoTimeout_Object = MibScalar
brPrtAdvancedAutoTimeout = _BrPrtAdvancedAutoTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 7, 2),
    _BrPrtAdvancedAutoTimeout_Type()
)
brPrtAdvancedAutoTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtAdvancedAutoTimeout.setStatus("mandatory")


class _BrPrtAdvancedFFSuppress_Type(Integer32):
    """Custom type brPrtAdvancedFFSuppress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BrPrtAdvancedFFSuppress_Type.__name__ = "Integer32"
_BrPrtAdvancedFFSuppress_Object = MibScalar
brPrtAdvancedFFSuppress = _BrPrtAdvancedFFSuppress_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 8),
    _BrPrtAdvancedFFSuppress_Type()
)
brPrtAdvancedFFSuppress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtAdvancedFFSuppress.setStatus("mandatory")


class _BrPrtAdvancedTonerLowPrint_Type(Integer32):
    """Custom type brPrtAdvancedTonerLowPrint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BrPrtAdvancedTonerLowPrint_Type.__name__ = "Integer32"
_BrPrtAdvancedTonerLowPrint_Object = MibScalar
brPrtAdvancedTonerLowPrint = _BrPrtAdvancedTonerLowPrint_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 9),
    _BrPrtAdvancedTonerLowPrint_Type()
)
brPrtAdvancedTonerLowPrint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtAdvancedTonerLowPrint.setStatus("mandatory")


class _BrPrtAdvancedPrintDensity_Type(Integer32):
    """Custom type brPrtAdvancedPrintDensity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_BrPrtAdvancedPrintDensity_Type.__name__ = "Integer32"
_BrPrtAdvancedPrintDensity_Object = MibScalar
brPrtAdvancedPrintDensity = _BrPrtAdvancedPrintDensity_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 10),
    _BrPrtAdvancedPrintDensity_Type()
)
brPrtAdvancedPrintDensity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtAdvancedPrintDensity.setStatus("mandatory")


class _BrPrtAdvancedInputBuffer_Type(Integer32):
    """Custom type brPrtAdvancedInputBuffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_BrPrtAdvancedInputBuffer_Type.__name__ = "Integer32"
_BrPrtAdvancedInputBuffer_Object = MibScalar
brPrtAdvancedInputBuffer = _BrPrtAdvancedInputBuffer_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 11),
    _BrPrtAdvancedInputBuffer_Type()
)
brPrtAdvancedInputBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtAdvancedInputBuffer.setStatus("mandatory")


class _BrPrtAdvancedLanguage_Type(Integer32):
    """Custom type brPrtAdvancedLanguage based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("brazil", 22),
          ("bulgarian", 19),
          ("chinese", 21),
          ("czech", 16),
          ("danish", 2),
          ("dutch", 3),
          ("english", 1),
          ("finish", 4),
          ("french", 5),
          ("german", 6),
          ("hungarian", 17),
          ("italian", 7),
          ("japanese", 14),
          ("norwegian", 8),
          ("polish", 13),
          ("portuguse", 9),
          ("romanian", 18),
          ("russian", 15),
          ("slovakian", 20),
          ("spanish", 11),
          ("swedish", 10),
          ("turkish", 12))
    )


_BrPrtAdvancedLanguage_Type.__name__ = "Integer32"
_BrPrtAdvancedLanguage_Object = MibScalar
brPrtAdvancedLanguage = _BrPrtAdvancedLanguage_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 12),
    _BrPrtAdvancedLanguage_Type()
)
brPrtAdvancedLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtAdvancedLanguage.setStatus("mandatory")


class _BrSecurePrintRAMSizeMax_Type(Integer32):
    """Custom type brSecurePrintRAMSizeMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BrSecurePrintRAMSizeMax_Type.__name__ = "Integer32"
_BrSecurePrintRAMSizeMax_Object = MibScalar
brSecurePrintRAMSizeMax = _BrSecurePrintRAMSizeMax_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 13),
    _BrSecurePrintRAMSizeMax_Type()
)
brSecurePrintRAMSizeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brSecurePrintRAMSizeMax.setStatus("mandatory")


class _BrSecurePrintRAMSize_Type(Integer32):
    """Custom type brSecurePrintRAMSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BrSecurePrintRAMSize_Type.__name__ = "Integer32"
_BrSecurePrintRAMSize_Object = MibScalar
brSecurePrintRAMSize = _BrSecurePrintRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 14),
    _BrSecurePrintRAMSize_Type()
)
brSecurePrintRAMSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brSecurePrintRAMSize.setStatus("mandatory")


class _BrPrtAdvancedJamRecovery_Type(Integer32):
    """Custom type brPrtAdvancedJamRecovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_BrPrtAdvancedJamRecovery_Type.__name__ = "Integer32"
_BrPrtAdvancedJamRecovery_Object = MibScalar
brPrtAdvancedJamRecovery = _BrPrtAdvancedJamRecovery_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 15),
    _BrPrtAdvancedJamRecovery_Type()
)
brPrtAdvancedJamRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtAdvancedJamRecovery.setStatus("mandatory")


class _BrPrtAdvancedSleepIndication_Type(Integer32):
    """Custom type brPrtAdvancedSleepIndication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dimmed", 2),
          ("off", 1))
    )


_BrPrtAdvancedSleepIndication_Type.__name__ = "Integer32"
_BrPrtAdvancedSleepIndication_Object = MibScalar
brPrtAdvancedSleepIndication = _BrPrtAdvancedSleepIndication_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 16),
    _BrPrtAdvancedSleepIndication_Type()
)
brPrtAdvancedSleepIndication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtAdvancedSleepIndication.setStatus("mandatory")


class _BrPrtAdvancedDestination_Type(Integer32):
    """Custom type brPrtAdvancedDestination based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oct", 2),
          ("octStack", 3),
          ("standardOutputTray", 1))
    )


_BrPrtAdvancedDestination_Type.__name__ = "Integer32"
_BrPrtAdvancedDestination_Object = MibScalar
brPrtAdvancedDestination = _BrPrtAdvancedDestination_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 17),
    _BrPrtAdvancedDestination_Type()
)
brPrtAdvancedDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtAdvancedDestination.setStatus("mandatory")


class _BrPrtAdvancedLowerLCD_Type(Integer32):
    """Custom type brPrtAdvancedLowerLCD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("counter", 2),
          ("jobName", 3),
          ("nonePage", 1))
    )


_BrPrtAdvancedLowerLCD_Type.__name__ = "Integer32"
_BrPrtAdvancedLowerLCD_Object = MibScalar
brPrtAdvancedLowerLCD = _BrPrtAdvancedLowerLCD_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 18),
    _BrPrtAdvancedLowerLCD_Type()
)
brPrtAdvancedLowerLCD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtAdvancedLowerLCD.setStatus("mandatory")


class _BrPrtAdvancedAutoOnline_Type(Integer32):
    """Custom type brPrtAdvancedAutoOnline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_BrPrtAdvancedAutoOnline_Type.__name__ = "Integer32"
_BrPrtAdvancedAutoOnline_Object = MibScalar
brPrtAdvancedAutoOnline = _BrPrtAdvancedAutoOnline_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 19),
    _BrPrtAdvancedAutoOnline_Type()
)
brPrtAdvancedAutoOnline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtAdvancedAutoOnline.setStatus("mandatory")


class _BrPrtAdvancedButtonRepeat_Type(Integer32):
    """Custom type brPrtAdvancedButtonRepeat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_BrPrtAdvancedButtonRepeat_Type.__name__ = "Integer32"
_BrPrtAdvancedButtonRepeat_Object = MibScalar
brPrtAdvancedButtonRepeat = _BrPrtAdvancedButtonRepeat_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 20),
    _BrPrtAdvancedButtonRepeat_Type()
)
brPrtAdvancedButtonRepeat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtAdvancedButtonRepeat.setStatus("mandatory")


class _BrPrtAdvancedMessageScroll_Type(Integer32):
    """Custom type brPrtAdvancedMessageScroll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_BrPrtAdvancedMessageScroll_Type.__name__ = "Integer32"
_BrPrtAdvancedMessageScroll_Object = MibScalar
brPrtAdvancedMessageScroll = _BrPrtAdvancedMessageScroll_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 21),
    _BrPrtAdvancedMessageScroll_Type()
)
brPrtAdvancedMessageScroll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtAdvancedMessageScroll.setStatus("mandatory")
_Buzzer_ObjectIdentity = ObjectIdentity
buzzer = _Buzzer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 22)
)


class _BrPrtAdvancedErrorBuzzer_Type(Integer32):
    """Custom type brPrtAdvancedErrorBuzzer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 2),
          ("off", 1),
          ("special", 3))
    )


_BrPrtAdvancedErrorBuzzer_Type.__name__ = "Integer32"
_BrPrtAdvancedErrorBuzzer_Object = MibScalar
brPrtAdvancedErrorBuzzer = _BrPrtAdvancedErrorBuzzer_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 22, 1),
    _BrPrtAdvancedErrorBuzzer_Type()
)
brPrtAdvancedErrorBuzzer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtAdvancedErrorBuzzer.setStatus("mandatory")


class _BrPrtAdvancedPanelBuzzer_Type(Integer32):
    """Custom type brPrtAdvancedPanelBuzzer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_BrPrtAdvancedPanelBuzzer_Type.__name__ = "Integer32"
_BrPrtAdvancedPanelBuzzer_Object = MibScalar
brPrtAdvancedPanelBuzzer = _BrPrtAdvancedPanelBuzzer_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 22, 2),
    _BrPrtAdvancedPanelBuzzer_Type()
)
brPrtAdvancedPanelBuzzer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtAdvancedPanelBuzzer.setStatus("mandatory")


class _BrPrtAdvancedBuzzerVolume_Type(Integer32):
    """Custom type brPrtAdvancedBuzzerVolume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 2))
    )


_BrPrtAdvancedBuzzerVolume_Type.__name__ = "Integer32"
_BrPrtAdvancedBuzzerVolume_Object = MibScalar
brPrtAdvancedBuzzerVolume = _BrPrtAdvancedBuzzerVolume_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 22, 3),
    _BrPrtAdvancedBuzzerVolume_Type()
)
brPrtAdvancedBuzzerVolume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtAdvancedBuzzerVolume.setStatus("mandatory")
_BrPrtAdvancedLCDDensity_Type = Integer32
_BrPrtAdvancedLCDDensity_Object = MibScalar
brPrtAdvancedLCDDensity = _BrPrtAdvancedLCDDensity_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 23),
    _BrPrtAdvancedLCDDensity_Type()
)
brPrtAdvancedLCDDensity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtAdvancedLCDDensity.setStatus("mandatory")
_SmallPaperSize_ObjectIdentity = ObjectIdentity
smallPaperSize = _SmallPaperSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 51)
)


class _BrSmallPaperSizeMP_Type(Integer32):
    """Custom type brSmallPaperSizeMP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              24,
              25,
              26,
              27,
              45,
              46,
              80,
              81,
              90,
              91,
              99,
              100,
              890,
              891,
              892,
              893,
              894,
              895,
              896,
              897,
              898,
              899,
              900,
              901,
              902,
              903,
              904,
              905,
              906,
              907,
              908,
              911,
              920,
              921,
              922,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("a3ISO", 27),
          ("a3PLUS", 891),
          ("a4", 26),
          ("a4LONG", 894),
          ("a4Letter", 898),
          ("a4ShortEdge", 893),
          ("a5", 25),
          ("a6", 24),
          ("b4JIS", 46),
          ("b5", 100),
          ("b5Executive", 899),
          ("b5ISOShortEdge", 896),
          ("b5JIS", 45),
          ("b6", 99),
          ("c5", 91),
          ("com10", 81),
          ("custom", 897),
          ("detectsensor", 911),
          ("dl", 90),
          ("dll", 901),
          ("envelopes", 900),
          ("envelopesY4", 921),
          ("executive", 1),
          ("executiveShortEdge", 895),
          ("folio", 903),
          ("hagaki", 902),
          ("inches3x5", 920),
          ("largestEnvelopesTheWest", 922),
          ("ledger", 890),
          ("legal", 3),
          ("letter", 2),
          ("letterShortEdge", 892),
          ("monarch", 80),
          ("noCasette", 1000),
          ("organaizerJ", 904),
          ("organaizerK", 905),
          ("organaizerL", 906),
          ("organaizerM", 907),
          ("userdefined", 908))
    )


_BrSmallPaperSizeMP_Type.__name__ = "Integer32"
_BrSmallPaperSizeMP_Object = MibScalar
brSmallPaperSizeMP = _BrSmallPaperSizeMP_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 51, 1),
    _BrSmallPaperSizeMP_Type()
)
brSmallPaperSizeMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brSmallPaperSizeMP.setStatus("mandatory")


class _BrSmallPaperSize1_Type(Integer32):
    """Custom type brSmallPaperSize1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              24,
              25,
              26,
              27,
              45,
              46,
              80,
              81,
              90,
              91,
              99,
              100,
              890,
              891,
              892,
              893,
              894,
              895,
              896,
              897,
              898,
              899,
              900,
              901,
              902,
              903,
              904,
              905,
              906,
              907,
              908,
              911,
              920,
              921,
              922,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("a3ISO", 27),
          ("a3PLUS", 891),
          ("a4", 26),
          ("a4LONG", 894),
          ("a4Letter", 898),
          ("a4ShortEdge", 893),
          ("a5", 25),
          ("a6", 24),
          ("b4JIS", 46),
          ("b5", 100),
          ("b5Executive", 899),
          ("b5ISOShortEdge", 896),
          ("b5JIS", 45),
          ("b6", 99),
          ("c5", 91),
          ("com10", 81),
          ("custom", 897),
          ("detectsensor", 911),
          ("dl", 90),
          ("dll", 901),
          ("envelopes", 900),
          ("envelopesY4", 921),
          ("executive", 1),
          ("executiveShortEdge", 895),
          ("folio", 903),
          ("hagaki", 902),
          ("inches3x5", 920),
          ("largestEnvelopesTheWest", 922),
          ("ledger", 890),
          ("legal", 3),
          ("letter", 2),
          ("letterShortEdge", 892),
          ("monarch", 80),
          ("noCasette", 1000),
          ("organaizerJ", 904),
          ("organaizerK", 905),
          ("organaizerL", 906),
          ("organaizerM", 907),
          ("userdefined", 908))
    )


_BrSmallPaperSize1_Type.__name__ = "Integer32"
_BrSmallPaperSize1_Object = MibScalar
brSmallPaperSize1 = _BrSmallPaperSize1_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 51, 2),
    _BrSmallPaperSize1_Type()
)
brSmallPaperSize1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brSmallPaperSize1.setStatus("mandatory")


class _BrSmallPaperSize2_Type(Integer32):
    """Custom type brSmallPaperSize2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              24,
              25,
              26,
              27,
              45,
              46,
              80,
              81,
              90,
              91,
              99,
              100,
              890,
              891,
              892,
              893,
              894,
              895,
              896,
              897,
              898,
              899,
              900,
              901,
              902,
              903,
              904,
              905,
              906,
              907,
              908,
              911,
              920,
              921,
              922,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("a3ISO", 27),
          ("a3PLUS", 891),
          ("a4", 26),
          ("a4LONG", 894),
          ("a4Letter", 898),
          ("a4ShortEdge", 893),
          ("a5", 25),
          ("a6", 24),
          ("b4JIS", 46),
          ("b5", 100),
          ("b5Executive", 899),
          ("b5ISOShortEdge", 896),
          ("b5JIS", 45),
          ("b6", 99),
          ("c5", 91),
          ("com10", 81),
          ("custom", 897),
          ("detectsensor", 911),
          ("dl", 90),
          ("dll", 901),
          ("envelopes", 900),
          ("envelopesY4", 921),
          ("executive", 1),
          ("executiveShortEdge", 895),
          ("folio", 903),
          ("hagaki", 902),
          ("inches3x5", 920),
          ("largestEnvelopesTheWest", 922),
          ("ledger", 890),
          ("legal", 3),
          ("letter", 2),
          ("letterShortEdge", 892),
          ("monarch", 80),
          ("noCasette", 1000),
          ("organaizerJ", 904),
          ("organaizerK", 905),
          ("organaizerL", 906),
          ("organaizerM", 907),
          ("userdefined", 908))
    )


_BrSmallPaperSize2_Type.__name__ = "Integer32"
_BrSmallPaperSize2_Object = MibScalar
brSmallPaperSize2 = _BrSmallPaperSize2_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 51, 3),
    _BrSmallPaperSize2_Type()
)
brSmallPaperSize2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brSmallPaperSize2.setStatus("mandatory")


class _BrSmallPaperSize3_Type(Integer32):
    """Custom type brSmallPaperSize3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              24,
              25,
              26,
              27,
              45,
              46,
              80,
              81,
              90,
              91,
              99,
              100,
              890,
              891,
              892,
              893,
              894,
              895,
              896,
              897,
              898,
              899,
              900,
              901,
              902,
              903,
              904,
              905,
              906,
              907,
              908,
              911,
              920,
              921,
              922,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("a3ISO", 27),
          ("a3PLUS", 891),
          ("a4", 26),
          ("a4LONG", 894),
          ("a4Letter", 898),
          ("a4ShortEdge", 893),
          ("a5", 25),
          ("a6", 24),
          ("b4JIS", 46),
          ("b5", 100),
          ("b5Executive", 899),
          ("b5ISOShortEdge", 896),
          ("b5JIS", 45),
          ("b6", 99),
          ("c5", 91),
          ("com10", 81),
          ("custom", 897),
          ("detectsensor", 911),
          ("dl", 90),
          ("dll", 901),
          ("envelopes", 900),
          ("envelopesY4", 921),
          ("executive", 1),
          ("executiveShortEdge", 895),
          ("folio", 903),
          ("hagaki", 902),
          ("inches3x5", 920),
          ("largestEnvelopesTheWest", 922),
          ("ledger", 890),
          ("legal", 3),
          ("letter", 2),
          ("letterShortEdge", 892),
          ("monarch", 80),
          ("noCasette", 1000),
          ("organaizerJ", 904),
          ("organaizerK", 905),
          ("organaizerL", 906),
          ("organaizerM", 907),
          ("userdefined", 908))
    )


_BrSmallPaperSize3_Type.__name__ = "Integer32"
_BrSmallPaperSize3_Object = MibScalar
brSmallPaperSize3 = _BrSmallPaperSize3_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 51, 4),
    _BrSmallPaperSize3_Type()
)
brSmallPaperSize3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brSmallPaperSize3.setStatus("mandatory")


class _BrSmallPaperSize4_Type(Integer32):
    """Custom type brSmallPaperSize4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              24,
              25,
              26,
              27,
              45,
              46,
              80,
              81,
              90,
              91,
              99,
              100,
              890,
              891,
              892,
              893,
              894,
              895,
              896,
              897,
              898,
              899,
              900,
              901,
              902,
              903,
              904,
              905,
              906,
              907,
              908,
              911,
              920,
              921,
              922,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("a3ISO", 27),
          ("a3PLUS", 891),
          ("a4", 26),
          ("a4LONG", 894),
          ("a4Letter", 898),
          ("a4ShortEdge", 893),
          ("a5", 25),
          ("a6", 24),
          ("b4JIS", 46),
          ("b5", 100),
          ("b5Executive", 899),
          ("b5ISOShortEdge", 896),
          ("b5JIS", 45),
          ("b6", 99),
          ("c5", 91),
          ("com10", 81),
          ("custom", 897),
          ("detectsensor", 911),
          ("dl", 90),
          ("dll", 901),
          ("envelopes", 900),
          ("envelopesY4", 921),
          ("executive", 1),
          ("executiveShortEdge", 895),
          ("folio", 903),
          ("hagaki", 902),
          ("inches3x5", 920),
          ("largestEnvelopesTheWest", 922),
          ("ledger", 890),
          ("legal", 3),
          ("letter", 2),
          ("letterShortEdge", 892),
          ("monarch", 80),
          ("noCasette", 1000),
          ("organaizerJ", 904),
          ("organaizerK", 905),
          ("organaizerL", 906),
          ("organaizerM", 907),
          ("userdefined", 908))
    )


_BrSmallPaperSize4_Type.__name__ = "Integer32"
_BrSmallPaperSize4_Object = MibScalar
brSmallPaperSize4 = _BrSmallPaperSize4_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 51, 5),
    _BrSmallPaperSize4_Type()
)
brSmallPaperSize4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brSmallPaperSize4.setStatus("mandatory")
_TrayPriority_ObjectIdentity = ObjectIdentity
trayPriority = _TrayPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 52)
)
_BrPrtAdvancedTrayPriority_Type = Integer32
_BrPrtAdvancedTrayPriority_Object = MibScalar
brPrtAdvancedTrayPriority = _BrPrtAdvancedTrayPriority_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 52, 1),
    _BrPrtAdvancedTrayPriority_Type()
)
brPrtAdvancedTrayPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtAdvancedTrayPriority.setStatus("mandatory")
_BrTrayPriorityCount_Type = Integer32
_BrTrayPriorityCount_Object = MibScalar
brTrayPriorityCount = _BrTrayPriorityCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 52, 2),
    _BrTrayPriorityCount_Type()
)
brTrayPriorityCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brTrayPriorityCount.setStatus("mandatory")
_BrTrayPriorityTable_Object = MibTable
brTrayPriorityTable = _BrTrayPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 52, 3)
)
if mibBuilder.loadTexts:
    brTrayPriorityTable.setStatus("mandatory")
_BrTrayPriorityEntry_Object = MibTableRow
brTrayPriorityEntry = _BrTrayPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 52, 3, 1)
)
brTrayPriorityEntry.setIndexNames(
    (0, "BROTHER-MIB", "brTrayPriorityIndex"),
)
if mibBuilder.loadTexts:
    brTrayPriorityEntry.setStatus("mandatory")


class _BrTrayPriorityIndex_Type(Integer32):
    """Custom type brTrayPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BrTrayPriorityIndex_Type.__name__ = "Integer32"
_BrTrayPriorityIndex_Object = MibTableColumn
brTrayPriorityIndex = _BrTrayPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 52, 3, 1, 1),
    _BrTrayPriorityIndex_Type()
)
brTrayPriorityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brTrayPriorityIndex.setStatus("mandatory")
_BrTrayPriorityMember_Type = OctetString
_BrTrayPriorityMember_Object = MibTableColumn
brTrayPriorityMember = _BrTrayPriorityMember_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 52, 3, 1, 2),
    _BrTrayPriorityMember_Type()
)
brTrayPriorityMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brTrayPriorityMember.setStatus("mandatory")
_CarbonCopy_ObjectIdentity = ObjectIdentity
carbonCopy = _CarbonCopy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 53)
)


class _BrCarbonCopyMode_Type(Integer32):
    """Custom type brCarbonCopyMode based on Integer32"""
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
        *(("auto", 3),
          ("off", 1),
          ("on", 2),
          ("parallel", 4))
    )


_BrCarbonCopyMode_Type.__name__ = "Integer32"
_BrCarbonCopyMode_Object = MibScalar
brCarbonCopyMode = _BrCarbonCopyMode_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 53, 1),
    _BrCarbonCopyMode_Type()
)
brCarbonCopyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brCarbonCopyMode.setStatus("mandatory")
_BrCarbonCopies_Type = Integer32
_BrCarbonCopies_Object = MibScalar
brCarbonCopies = _BrCarbonCopies_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 53, 2),
    _BrCarbonCopies_Type()
)
brCarbonCopies.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brCarbonCopies.setStatus("mandatory")
_BrCarbonCopyTable_Object = MibTable
brCarbonCopyTable = _BrCarbonCopyTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 53, 10)
)
if mibBuilder.loadTexts:
    brCarbonCopyTable.setStatus("mandatory")
_BrCarbonCopyEntry_Object = MibTableRow
brCarbonCopyEntry = _BrCarbonCopyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 53, 10, 1)
)
brCarbonCopyEntry.setIndexNames(
    (0, "BROTHER-MIB", "brCarbonCopyIndex"),
)
if mibBuilder.loadTexts:
    brCarbonCopyEntry.setStatus("mandatory")


class _BrCarbonCopyIndex_Type(Integer32):
    """Custom type brCarbonCopyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BrCarbonCopyIndex_Type.__name__ = "Integer32"
_BrCarbonCopyIndex_Object = MibTableColumn
brCarbonCopyIndex = _BrCarbonCopyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 53, 10, 1, 1),
    _BrCarbonCopyIndex_Type()
)
brCarbonCopyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brCarbonCopyIndex.setStatus("mandatory")


class _BrCarbonCopyTray_Type(Integer32):
    """Custom type brCarbonCopyTray based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("auto", 11),
          ("mpTray", 10),
          ("tray1", 1),
          ("tray2", 2),
          ("tray3", 3),
          ("tray4", 4))
    )


_BrCarbonCopyTray_Type.__name__ = "Integer32"
_BrCarbonCopyTray_Object = MibTableColumn
brCarbonCopyTray = _BrCarbonCopyTray_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 53, 10, 1, 2),
    _BrCarbonCopyTray_Type()
)
brCarbonCopyTray.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brCarbonCopyTray.setStatus("mandatory")


class _BrCarbonCopyMacro_Type(Integer32):
    """Custom type brCarbonCopyMacro based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_BrCarbonCopyMacro_Type.__name__ = "Integer32"
_BrCarbonCopyMacro_Object = MibTableColumn
brCarbonCopyMacro = _BrCarbonCopyMacro_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 53, 10, 1, 3),
    _BrCarbonCopyMacro_Type()
)
brCarbonCopyMacro.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brCarbonCopyMacro.setStatus("mandatory")
_BrCarbonCopyMacroID_Type = Integer32
_BrCarbonCopyMacroID_Object = MibTableColumn
brCarbonCopyMacroID = _BrCarbonCopyMacroID_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 53, 10, 1, 4),
    _BrCarbonCopyMacroID_Type()
)
brCarbonCopyMacroID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brCarbonCopyMacroID.setStatus("mandatory")
_MediaFix_ObjectIdentity = ObjectIdentity
mediaFix = _MediaFix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 54)
)


class _BrMediaFixTray1_Type(Integer32):
    """Custom type brMediaFixTray1 based on Integer32"""
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
        *(("bond", 7),
          ("envThick", 9),
          ("envThin", 10),
          ("envelopes", 8),
          ("off", 1),
          ("recycled", 11),
          ("regular", 2),
          ("thick", 3),
          ("thicker", 4),
          ("thin", 6),
          ("transparency", 5))
    )


_BrMediaFixTray1_Type.__name__ = "Integer32"
_BrMediaFixTray1_Object = MibScalar
brMediaFixTray1 = _BrMediaFixTray1_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 54, 1),
    _BrMediaFixTray1_Type()
)
brMediaFixTray1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMediaFixTray1.setStatus("mandatory")


class _BrMediaFixTray2_Type(Integer32):
    """Custom type brMediaFixTray2 based on Integer32"""
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
        *(("bond", 7),
          ("envThick", 9),
          ("envThin", 10),
          ("envelopes", 8),
          ("off", 1),
          ("recycled", 11),
          ("regular", 2),
          ("thick", 3),
          ("thicker", 4),
          ("thin", 6),
          ("transparency", 5))
    )


_BrMediaFixTray2_Type.__name__ = "Integer32"
_BrMediaFixTray2_Object = MibScalar
brMediaFixTray2 = _BrMediaFixTray2_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 54, 2),
    _BrMediaFixTray2_Type()
)
brMediaFixTray2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMediaFixTray2.setStatus("mandatory")


class _BrMediaFixTray3_Type(Integer32):
    """Custom type brMediaFixTray3 based on Integer32"""
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
        *(("bond", 7),
          ("envThick", 9),
          ("envThin", 10),
          ("envelopes", 8),
          ("off", 1),
          ("recycled", 11),
          ("regular", 2),
          ("thick", 3),
          ("thicker", 4),
          ("thin", 6),
          ("transparency", 5))
    )


_BrMediaFixTray3_Type.__name__ = "Integer32"
_BrMediaFixTray3_Object = MibScalar
brMediaFixTray3 = _BrMediaFixTray3_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 54, 3),
    _BrMediaFixTray3_Type()
)
brMediaFixTray3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMediaFixTray3.setStatus("mandatory")


class _BrMediaFixTray4_Type(Integer32):
    """Custom type brMediaFixTray4 based on Integer32"""
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
        *(("bond", 7),
          ("envThick", 9),
          ("envThin", 10),
          ("envelopes", 8),
          ("off", 1),
          ("recycled", 11),
          ("regular", 2),
          ("thick", 3),
          ("thicker", 4),
          ("thin", 6),
          ("transparency", 5))
    )


_BrMediaFixTray4_Type.__name__ = "Integer32"
_BrMediaFixTray4_Object = MibScalar
brMediaFixTray4 = _BrMediaFixTray4_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 54, 4),
    _BrMediaFixTray4_Type()
)
brMediaFixTray4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMediaFixTray4.setStatus("mandatory")


class _BrMediaFixMP_Type(Integer32):
    """Custom type brMediaFixMP based on Integer32"""
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
        *(("bond", 7),
          ("envThick", 9),
          ("envThin", 10),
          ("envelopes", 8),
          ("off", 1),
          ("recycled", 11),
          ("regular", 2),
          ("thick", 3),
          ("thicker", 4),
          ("thin", 6),
          ("transparency", 5))
    )


_BrMediaFixMP_Type.__name__ = "Integer32"
_BrMediaFixMP_Object = MibScalar
brMediaFixMP = _BrMediaFixMP_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 54, 10),
    _BrMediaFixMP_Type()
)
brMediaFixMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMediaFixMP.setStatus("mandatory")
_Directprint_ObjectIdentity = ObjectIdentity
directprint = _Directprint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 60)
)


class _BrDirectPrintPaperSize_Type(Integer32):
    """Custom type brDirectPrintPaperSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              24,
              25,
              26,
              27,
              45,
              46,
              80,
              81,
              90,
              91,
              99,
              100,
              890,
              891,
              892,
              893,
              894,
              895,
              896,
              897,
              898,
              899,
              900,
              901,
              902,
              903,
              904,
              905,
              906,
              907,
              908,
              911,
              920,
              921,
              922,
              923,
              924,
              925,
              926,
              927)
        )
    )
    namedValues = NamedValues(
        *(("a3ISO", 27),
          ("a3PLUS", 891),
          ("a4", 26),
          ("a4LONG", 894),
          ("a4Letter", 898),
          ("a4ShortEdge", 893),
          ("a5", 25),
          ("a5l", 923),
          ("a6", 24),
          ("b4JIS", 46),
          ("b5", 100),
          ("b5Executive", 899),
          ("b5ISOShortEdge", 896),
          ("b5JIS", 45),
          ("b6", 99),
          ("b6jis", 924),
          ("c5", 91),
          ("com10", 81),
          ("custom", 897),
          ("detectsensor", 911),
          ("dl", 90),
          ("dll", 901),
          ("envelopes", 900),
          ("envelopesY4", 921),
          ("executive", 1),
          ("executiveShortEdge", 895),
          ("folio", 903),
          ("hagaki", 902),
          ("inches3x5", 920),
          ("largestEnvelopesTheWest", 922),
          ("ledger", 890),
          ("legal", 3),
          ("letter", 2),
          ("letterShortEdge", 892),
          ("monarch", 80),
          ("organaizerJ", 904),
          ("organaizerK", 905),
          ("organaizerL", 906),
          ("organaizerM", 907),
          ("prc16k184x260", 926),
          ("prc16k195x270", 925),
          ("prc16k197x273", 927),
          ("userdefined", 908))
    )


_BrDirectPrintPaperSize_Type.__name__ = "Integer32"
_BrDirectPrintPaperSize_Object = MibScalar
brDirectPrintPaperSize = _BrDirectPrintPaperSize_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 60, 1),
    _BrDirectPrintPaperSize_Type()
)
brDirectPrintPaperSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brDirectPrintPaperSize.setStatus("mandatory")
_BrDirectPrintMediaType_Type = Integer32
_BrDirectPrintMediaType_Object = MibScalar
brDirectPrintMediaType = _BrDirectPrintMediaType_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 60, 2),
    _BrDirectPrintMediaType_Type()
)
brDirectPrintMediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brDirectPrintMediaType.setStatus("mandatory")
_BrDirectPrintMultipulPage_Type = Integer32
_BrDirectPrintMultipulPage_Object = MibScalar
brDirectPrintMultipulPage = _BrDirectPrintMultipulPage_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 60, 3),
    _BrDirectPrintMultipulPage_Type()
)
brDirectPrintMultipulPage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brDirectPrintMultipulPage.setStatus("mandatory")
_BrDirectPrintOrientation_Type = Integer32
_BrDirectPrintOrientation_Object = MibScalar
brDirectPrintOrientation = _BrDirectPrintOrientation_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 60, 4),
    _BrDirectPrintOrientation_Type()
)
brDirectPrintOrientation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brDirectPrintOrientation.setStatus("mandatory")
_BrDirectPrintCollate_Type = Integer32
_BrDirectPrintCollate_Object = MibScalar
brDirectPrintCollate = _BrDirectPrintCollate_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 60, 5),
    _BrDirectPrintCollate_Type()
)
brDirectPrintCollate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brDirectPrintCollate.setStatus("mandatory")
_BrDirectPrintOutputColor_Type = Integer32
_BrDirectPrintOutputColor_Object = MibScalar
brDirectPrintOutputColor = _BrDirectPrintOutputColor_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 60, 6),
    _BrDirectPrintOutputColor_Type()
)
brDirectPrintOutputColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brDirectPrintOutputColor.setStatus("mandatory")
_BrDirectPrintPrintQuality_Type = Integer32
_BrDirectPrintPrintQuality_Object = MibScalar
brDirectPrintPrintQuality = _BrDirectPrintPrintQuality_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 60, 7),
    _BrDirectPrintPrintQuality_Type()
)
brDirectPrintPrintQuality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brDirectPrintPrintQuality.setStatus("mandatory")
_BrDirectPrintPdfOption_Type = Integer32
_BrDirectPrintPdfOption_Object = MibScalar
brDirectPrintPdfOption = _BrDirectPrintPdfOption_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 60, 8),
    _BrDirectPrintPdfOption_Type()
)
brDirectPrintPdfOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brDirectPrintPdfOption.setStatus("mandatory")
_BrDirectPrintSetting_Type = Integer32
_BrDirectPrintSetting_Object = MibScalar
brDirectPrintSetting = _BrDirectPrintSetting_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 60, 9),
    _BrDirectPrintSetting_Type()
)
brDirectPrintSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brDirectPrintSetting.setStatus("mandatory")


class _BrDirectPrintPdfThumbnailType_Type(Integer32):
    """Custom type brDirectPrintPdfThumbnailType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alternativeImage", 1),
          ("reductionImage", 2))
    )


_BrDirectPrintPdfThumbnailType_Type.__name__ = "Integer32"
_BrDirectPrintPdfThumbnailType_Object = MibScalar
brDirectPrintPdfThumbnailType = _BrDirectPrintPdfThumbnailType_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 60, 10),
    _BrDirectPrintPdfThumbnailType_Type()
)
brDirectPrintPdfThumbnailType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brDirectPrintPdfThumbnailType.setStatus("mandatory")
_Pictbridge_ObjectIdentity = ObjectIdentity
pictbridge = _Pictbridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 61)
)


class _BrPictBridgePaperSize_Type(Integer32):
    """Custom type brPictBridgePaperSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              24,
              25,
              26,
              27,
              45,
              46,
              80,
              81,
              90,
              91,
              99,
              100,
              890,
              891,
              892,
              893,
              894,
              895,
              896,
              897,
              898,
              899,
              900,
              901,
              902,
              903,
              904,
              905,
              906,
              907,
              908,
              911,
              920,
              921,
              922)
        )
    )
    namedValues = NamedValues(
        *(("a3ISO", 27),
          ("a3PLUS", 891),
          ("a4", 26),
          ("a4LONG", 894),
          ("a4Letter", 898),
          ("a4ShortEdge", 893),
          ("a5", 25),
          ("a6", 24),
          ("b4JIS", 46),
          ("b5", 100),
          ("b5Executive", 899),
          ("b5ISOShortEdge", 896),
          ("b5JIS", 45),
          ("b6", 99),
          ("c5", 91),
          ("com10", 81),
          ("custom", 897),
          ("detectsensor", 911),
          ("dl", 90),
          ("dll", 901),
          ("envelopes", 900),
          ("envelopesY4", 921),
          ("executive", 1),
          ("executiveShortEdge", 895),
          ("folio", 903),
          ("hagaki", 902),
          ("inches3x5", 920),
          ("largestEnvelopesTheWest", 922),
          ("ledger", 890),
          ("legal", 3),
          ("letter", 2),
          ("letterShortEdge", 892),
          ("monarch", 80),
          ("organaizerJ", 904),
          ("organaizerK", 905),
          ("organaizerL", 906),
          ("organaizerM", 907),
          ("userdefined", 908))
    )


_BrPictBridgePaperSize_Type.__name__ = "Integer32"
_BrPictBridgePaperSize_Object = MibScalar
brPictBridgePaperSize = _BrPictBridgePaperSize_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 61, 1),
    _BrPictBridgePaperSize_Type()
)
brPictBridgePaperSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPictBridgePaperSize.setStatus("mandatory")
_BrPictBridgeOrientation_Type = Integer32
_BrPictBridgeOrientation_Object = MibScalar
brPictBridgeOrientation = _BrPictBridgeOrientation_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 61, 2),
    _BrPictBridgeOrientation_Type()
)
brPictBridgeOrientation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPictBridgeOrientation.setStatus("mandatory")
_BrPictBridgeDateTime_Type = Integer32
_BrPictBridgeDateTime_Object = MibScalar
brPictBridgeDateTime = _BrPictBridgeDateTime_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 61, 3),
    _BrPictBridgeDateTime_Type()
)
brPictBridgeDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPictBridgeDateTime.setStatus("mandatory")
_BrPictBridgeFileName_Type = Integer32
_BrPictBridgeFileName_Object = MibScalar
brPictBridgeFileName = _BrPictBridgeFileName_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 61, 4),
    _BrPictBridgeFileName_Type()
)
brPictBridgeFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPictBridgeFileName.setStatus("mandatory")
_BrPictBridgePrintQuality_Type = Integer32
_BrPictBridgePrintQuality_Object = MibScalar
brPictBridgePrintQuality = _BrPictBridgePrintQuality_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 61, 5),
    _BrPictBridgePrintQuality_Type()
)
brPictBridgePrintQuality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPictBridgePrintQuality.setStatus("mandatory")
_BrPictBridgePrintSetting_Type = Integer32
_BrPictBridgePrintSetting_Object = MibScalar
brPictBridgePrintSetting = _BrPictBridgePrintSetting_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 61, 6),
    _BrPictBridgePrintSetting_Type()
)
brPictBridgePrintSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPictBridgePrintSetting.setStatus("mandatory")
_Colorcorrection_ObjectIdentity = ObjectIdentity
colorcorrection = _Colorcorrection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 62)
)
_BrColorCalibration_Type = Integer32
_BrColorCalibration_Object = MibScalar
brColorCalibration = _BrColorCalibration_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 62, 1),
    _BrColorCalibration_Type()
)
brColorCalibration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brColorCalibration.setStatus("mandatory")
_BrColorCalibrationReset_Type = Integer32
_BrColorCalibrationReset_Object = MibScalar
brColorCalibrationReset = _BrColorCalibrationReset_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 62, 2),
    _BrColorCalibrationReset_Type()
)
brColorCalibrationReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brColorCalibrationReset.setStatus("mandatory")
_BrAutoRegistRegistrate_Type = Integer32
_BrAutoRegistRegistrate_Object = MibScalar
brAutoRegistRegistrate = _BrAutoRegistRegistrate_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 62, 3),
    _BrAutoRegistRegistrate_Type()
)
brAutoRegistRegistrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brAutoRegistRegistrate.setStatus("mandatory")
_BrAutoRegistSetInterval_Type = Integer32
_BrAutoRegistSetInterval_Object = MibScalar
brAutoRegistSetInterval = _BrAutoRegistSetInterval_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 62, 4),
    _BrAutoRegistSetInterval_Type()
)
brAutoRegistSetInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brAutoRegistSetInterval.setStatus("mandatory")
_BrRegistrationPrintChart_Type = Integer32
_BrRegistrationPrintChart_Object = MibScalar
brRegistrationPrintChart = _BrRegistrationPrintChart_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 62, 5),
    _BrRegistrationPrintChart_Type()
)
brRegistrationPrintChart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brRegistrationPrintChart.setStatus("mandatory")
_BrRegistrationXMagentaLeft_Type = Integer32
_BrRegistrationXMagentaLeft_Object = MibScalar
brRegistrationXMagentaLeft = _BrRegistrationXMagentaLeft_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 62, 6),
    _BrRegistrationXMagentaLeft_Type()
)
brRegistrationXMagentaLeft.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brRegistrationXMagentaLeft.setStatus("mandatory")
_BrRegistrationXMagentaRight_Type = Integer32
_BrRegistrationXMagentaRight_Object = MibScalar
brRegistrationXMagentaRight = _BrRegistrationXMagentaRight_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 62, 7),
    _BrRegistrationXMagentaRight_Type()
)
brRegistrationXMagentaRight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brRegistrationXMagentaRight.setStatus("mandatory")
_BrRegistrationXCyanLeft_Type = Integer32
_BrRegistrationXCyanLeft_Object = MibScalar
brRegistrationXCyanLeft = _BrRegistrationXCyanLeft_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 62, 8),
    _BrRegistrationXCyanLeft_Type()
)
brRegistrationXCyanLeft.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brRegistrationXCyanLeft.setStatus("mandatory")
_BrRegistrationXCyanRight_Type = Integer32
_BrRegistrationXCyanRight_Object = MibScalar
brRegistrationXCyanRight = _BrRegistrationXCyanRight_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 62, 9),
    _BrRegistrationXCyanRight_Type()
)
brRegistrationXCyanRight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brRegistrationXCyanRight.setStatus("mandatory")
_BrRegistrationXYellowLeft_Type = Integer32
_BrRegistrationXYellowLeft_Object = MibScalar
brRegistrationXYellowLeft = _BrRegistrationXYellowLeft_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 62, 10),
    _BrRegistrationXYellowLeft_Type()
)
brRegistrationXYellowLeft.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brRegistrationXYellowLeft.setStatus("mandatory")
_BrRegistrationXYellowRight_Type = Integer32
_BrRegistrationXYellowRight_Object = MibScalar
brRegistrationXYellowRight = _BrRegistrationXYellowRight_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 62, 11),
    _BrRegistrationXYellowRight_Type()
)
brRegistrationXYellowRight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brRegistrationXYellowRight.setStatus("mandatory")
_BrRegistrationYMagenta_Type = Integer32
_BrRegistrationYMagenta_Object = MibScalar
brRegistrationYMagenta = _BrRegistrationYMagenta_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 62, 12),
    _BrRegistrationYMagenta_Type()
)
brRegistrationYMagenta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brRegistrationYMagenta.setStatus("mandatory")
_BrRegistrationYCyan_Type = Integer32
_BrRegistrationYCyan_Object = MibScalar
brRegistrationYCyan = _BrRegistrationYCyan_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 62, 13),
    _BrRegistrationYCyan_Type()
)
brRegistrationYCyan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brRegistrationYCyan.setStatus("mandatory")
_BrRegistrationYYellow_Type = Integer32
_BrRegistrationYYellow_Object = MibScalar
brRegistrationYYellow = _BrRegistrationYYellow_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 62, 14),
    _BrRegistrationYYellow_Type()
)
brRegistrationYYellow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brRegistrationYYellow.setStatus("mandatory")
_Funclock_ObjectIdentity = ObjectIdentity
funclock = _Funclock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63)
)
_BrFuncLockSettingInit_Type = Integer32
_BrFuncLockSettingInit_Object = MibScalar
brFuncLockSettingInit = _BrFuncLockSettingInit_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 1),
    _BrFuncLockSettingInit_Type()
)
brFuncLockSettingInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brFuncLockSettingInit.setStatus("mandatory")
_BrFuncLockAdminPassword_Type = DisplayString
_BrFuncLockAdminPassword_Object = MibScalar
brFuncLockAdminPassword = _BrFuncLockAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 2),
    _BrFuncLockAdminPassword_Type()
)
brFuncLockAdminPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brFuncLockAdminPassword.setStatus("mandatory")


class _BrFuncLock_Type(Integer32):
    """Custom type brFuncLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_BrFuncLock_Type.__name__ = "Integer32"
_BrFuncLock_Object = MibScalar
brFuncLock = _BrFuncLock_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 3),
    _BrFuncLock_Type()
)
brFuncLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brFuncLock.setStatus("mandatory")


class _BrFuncLockPublicFuncCount_Type(Integer32):
    """Custom type brFuncLockPublicFuncCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BrFuncLockPublicFuncCount_Type.__name__ = "Integer32"
_BrFuncLockPublicFuncCount_Object = MibScalar
brFuncLockPublicFuncCount = _BrFuncLockPublicFuncCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 4),
    _BrFuncLockPublicFuncCount_Type()
)
brFuncLockPublicFuncCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFuncLockPublicFuncCount.setStatus("mandatory")
_BrFuncLockPublicTable_Object = MibTable
brFuncLockPublicTable = _BrFuncLockPublicTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 5)
)
if mibBuilder.loadTexts:
    brFuncLockPublicTable.setStatus("mandatory")
_BrFuncLockPublicEntry_Object = MibTableRow
brFuncLockPublicEntry = _BrFuncLockPublicEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 5, 1)
)
brFuncLockPublicEntry.setIndexNames(
    (0, "BROTHER-MIB", "brFuncLockPublicFuncIndex"),
)
if mibBuilder.loadTexts:
    brFuncLockPublicEntry.setStatus("mandatory")


class _BrFuncLockPublicFuncIndex_Type(Integer32):
    """Custom type brFuncLockPublicFuncIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BrFuncLockPublicFuncIndex_Type.__name__ = "Integer32"
_BrFuncLockPublicFuncIndex_Object = MibTableColumn
brFuncLockPublicFuncIndex = _BrFuncLockPublicFuncIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 5, 1, 1),
    _BrFuncLockPublicFuncIndex_Type()
)
brFuncLockPublicFuncIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFuncLockPublicFuncIndex.setStatus("mandatory")


class _BrFuncLockPublicFuncMember_Type(Integer32):
    """Custom type brFuncLockPublicFuncMember based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("copybr", 2),
          ("copycolor", 1),
          ("faxrx", 4),
          ("faxtx", 3),
          ("pcc", 7),
          ("print", 6),
          ("scan", 5))
    )


_BrFuncLockPublicFuncMember_Type.__name__ = "Integer32"
_BrFuncLockPublicFuncMember_Object = MibTableColumn
brFuncLockPublicFuncMember = _BrFuncLockPublicFuncMember_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 5, 1, 2),
    _BrFuncLockPublicFuncMember_Type()
)
brFuncLockPublicFuncMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFuncLockPublicFuncMember.setStatus("mandatory")


class _BrFuncLockPublicFuncSupported_Type(Integer32):
    """Custom type brFuncLockPublicFuncSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrFuncLockPublicFuncSupported_Type.__name__ = "Integer32"
_BrFuncLockPublicFuncSupported_Object = MibTableColumn
brFuncLockPublicFuncSupported = _BrFuncLockPublicFuncSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 5, 1, 3),
    _BrFuncLockPublicFuncSupported_Type()
)
brFuncLockPublicFuncSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFuncLockPublicFuncSupported.setStatus("mandatory")


class _BrFuncLockPublicFuncEnable_Type(Integer32):
    """Custom type brFuncLockPublicFuncEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrFuncLockPublicFuncEnable_Type.__name__ = "Integer32"
_BrFuncLockPublicFuncEnable_Object = MibTableColumn
brFuncLockPublicFuncEnable = _BrFuncLockPublicFuncEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 5, 1, 4),
    _BrFuncLockPublicFuncEnable_Type()
)
brFuncLockPublicFuncEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brFuncLockPublicFuncEnable.setStatus("mandatory")


class _BrFuncLockUserCount_Type(Integer32):
    """Custom type brFuncLockUserCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BrFuncLockUserCount_Type.__name__ = "Integer32"
_BrFuncLockUserCount_Object = MibScalar
brFuncLockUserCount = _BrFuncLockUserCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 6),
    _BrFuncLockUserCount_Type()
)
brFuncLockUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFuncLockUserCount.setStatus("mandatory")
_BrFuncLockUserTable_Object = MibTable
brFuncLockUserTable = _BrFuncLockUserTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 7)
)
if mibBuilder.loadTexts:
    brFuncLockUserTable.setStatus("mandatory")
_BrFuncLockUserEntry_Object = MibTableRow
brFuncLockUserEntry = _BrFuncLockUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 7, 1)
)
brFuncLockUserEntry.setIndexNames(
    (0, "BROTHER-MIB", "brFuncLockUserIndex"),
)
if mibBuilder.loadTexts:
    brFuncLockUserEntry.setStatus("mandatory")


class _BrFuncLockUserIndex_Type(Integer32):
    """Custom type brFuncLockUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BrFuncLockUserIndex_Type.__name__ = "Integer32"
_BrFuncLockUserIndex_Object = MibTableColumn
brFuncLockUserIndex = _BrFuncLockUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 7, 1, 1),
    _BrFuncLockUserIndex_Type()
)
brFuncLockUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFuncLockUserIndex.setStatus("mandatory")
_BrFuncLockUserName_Type = DisplayString
_BrFuncLockUserName_Object = MibTableColumn
brFuncLockUserName = _BrFuncLockUserName_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 7, 1, 2),
    _BrFuncLockUserName_Type()
)
brFuncLockUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brFuncLockUserName.setStatus("mandatory")
_BrFuncLockUserPassword_Type = DisplayString
_BrFuncLockUserPassword_Object = MibTableColumn
brFuncLockUserPassword = _BrFuncLockUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 7, 1, 3),
    _BrFuncLockUserPassword_Type()
)
brFuncLockUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brFuncLockUserPassword.setStatus("mandatory")


class _BrFuncLockUserFuncCount_Type(Integer32):
    """Custom type brFuncLockUserFuncCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BrFuncLockUserFuncCount_Type.__name__ = "Integer32"
_BrFuncLockUserFuncCount_Object = MibScalar
brFuncLockUserFuncCount = _BrFuncLockUserFuncCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 8),
    _BrFuncLockUserFuncCount_Type()
)
brFuncLockUserFuncCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFuncLockUserFuncCount.setStatus("mandatory")
_BrFuncLockUserFuncTable_Object = MibTable
brFuncLockUserFuncTable = _BrFuncLockUserFuncTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 9)
)
if mibBuilder.loadTexts:
    brFuncLockUserFuncTable.setStatus("mandatory")
_BrFuncLockUserFuncEntry_Object = MibTableRow
brFuncLockUserFuncEntry = _BrFuncLockUserFuncEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 9, 1)
)
brFuncLockUserFuncEntry.setIndexNames(
    (0, "BROTHER-MIB", "brFuncLockUserIndex"),
    (0, "BROTHER-MIB", "brFuncLockUserFuncIndex"),
)
if mibBuilder.loadTexts:
    brFuncLockUserFuncEntry.setStatus("mandatory")


class _BrFuncLockUserFuncIndex_Type(Integer32):
    """Custom type brFuncLockUserFuncIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BrFuncLockUserFuncIndex_Type.__name__ = "Integer32"
_BrFuncLockUserFuncIndex_Object = MibTableColumn
brFuncLockUserFuncIndex = _BrFuncLockUserFuncIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 9, 1, 1),
    _BrFuncLockUserFuncIndex_Type()
)
brFuncLockUserFuncIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFuncLockUserFuncIndex.setStatus("mandatory")


class _BrFuncLockUserFuncMember_Type(Integer32):
    """Custom type brFuncLockUserFuncMember based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("copybr", 2),
          ("copycolor", 1),
          ("faxrx", 4),
          ("faxtx", 3),
          ("pcc", 7),
          ("print", 6),
          ("scan", 5))
    )


_BrFuncLockUserFuncMember_Type.__name__ = "Integer32"
_BrFuncLockUserFuncMember_Object = MibTableColumn
brFuncLockUserFuncMember = _BrFuncLockUserFuncMember_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 9, 1, 2),
    _BrFuncLockUserFuncMember_Type()
)
brFuncLockUserFuncMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFuncLockUserFuncMember.setStatus("mandatory")


class _BrFuncLockUserFuncSupported_Type(Integer32):
    """Custom type brFuncLockUserFuncSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrFuncLockUserFuncSupported_Type.__name__ = "Integer32"
_BrFuncLockUserFuncSupported_Object = MibTableColumn
brFuncLockUserFuncSupported = _BrFuncLockUserFuncSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 9, 1, 3),
    _BrFuncLockUserFuncSupported_Type()
)
brFuncLockUserFuncSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFuncLockUserFuncSupported.setStatus("mandatory")


class _BrFuncLockUserFuncEnable_Type(Integer32):
    """Custom type brFuncLockUserFuncEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrFuncLockUserFuncEnable_Type.__name__ = "Integer32"
_BrFuncLockUserFuncEnable_Object = MibTableColumn
brFuncLockUserFuncEnable = _BrFuncLockUserFuncEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 9, 1, 4),
    _BrFuncLockUserFuncEnable_Type()
)
brFuncLockUserFuncEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brFuncLockUserFuncEnable.setStatus("mandatory")
_BrFuncLockSetting_Type = Integer32
_BrFuncLockSetting_Object = MibScalar
brFuncLockSetting = _BrFuncLockSetting_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 10),
    _BrFuncLockSetting_Type()
)
brFuncLockSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brFuncLockSetting.setStatus("mandatory")


class _BrFuncLockUserPrintPageCounterReset_Type(Integer32):
    """Custom type brFuncLockUserPrintPageCounterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_BrFuncLockUserPrintPageCounterReset_Type.__name__ = "Integer32"
_BrFuncLockUserPrintPageCounterReset_Object = MibScalar
brFuncLockUserPrintPageCounterReset = _BrFuncLockUserPrintPageCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 20),
    _BrFuncLockUserPrintPageCounterReset_Type()
)
brFuncLockUserPrintPageCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brFuncLockUserPrintPageCounterReset.setStatus("mandatory")


class _BrFuncLockPublicPrintLimitEnable_Type(Integer32):
    """Custom type brFuncLockPublicPrintLimitEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrFuncLockPublicPrintLimitEnable_Type.__name__ = "Integer32"
_BrFuncLockPublicPrintLimitEnable_Object = MibScalar
brFuncLockPublicPrintLimitEnable = _BrFuncLockPublicPrintLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 21),
    _BrFuncLockPublicPrintLimitEnable_Type()
)
brFuncLockPublicPrintLimitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brFuncLockPublicPrintLimitEnable.setStatus("mandatory")


class _BrFuncLockPublicPrintPageMax_Type(Integer32):
    """Custom type brFuncLockPublicPrintPageMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999999),
    )


_BrFuncLockPublicPrintPageMax_Type.__name__ = "Integer32"
_BrFuncLockPublicPrintPageMax_Object = MibScalar
brFuncLockPublicPrintPageMax = _BrFuncLockPublicPrintPageMax_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 22),
    _BrFuncLockPublicPrintPageMax_Type()
)
brFuncLockPublicPrintPageMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brFuncLockPublicPrintPageMax.setStatus("mandatory")


class _BrFuncLockPublicPrintPageCountMono_Type(Integer32):
    """Custom type brFuncLockPublicPrintPageCountMono based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_BrFuncLockPublicPrintPageCountMono_Type.__name__ = "Integer32"
_BrFuncLockPublicPrintPageCountMono_Object = MibScalar
brFuncLockPublicPrintPageCountMono = _BrFuncLockPublicPrintPageCountMono_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 23),
    _BrFuncLockPublicPrintPageCountMono_Type()
)
brFuncLockPublicPrintPageCountMono.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFuncLockPublicPrintPageCountMono.setStatus("mandatory")


class _BrFuncLockPublicPrintPageCountColor_Type(Integer32):
    """Custom type brFuncLockPublicPrintPageCountColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_BrFuncLockPublicPrintPageCountColor_Type.__name__ = "Integer32"
_BrFuncLockPublicPrintPageCountColor_Object = MibScalar
brFuncLockPublicPrintPageCountColor = _BrFuncLockPublicPrintPageCountColor_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 24),
    _BrFuncLockPublicPrintPageCountColor_Type()
)
brFuncLockPublicPrintPageCountColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFuncLockPublicPrintPageCountColor.setStatus("mandatory")
_BrFuncLockUserPrintPageTable_Object = MibTable
brFuncLockUserPrintPageTable = _BrFuncLockUserPrintPageTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 25)
)
if mibBuilder.loadTexts:
    brFuncLockUserPrintPageTable.setStatus("mandatory")
_BrFuncLockUserPrintPageEntry_Object = MibTableRow
brFuncLockUserPrintPageEntry = _BrFuncLockUserPrintPageEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 25, 1)
)
brFuncLockUserPrintPageEntry.setIndexNames(
    (0, "BROTHER-MIB", "brFuncLockUserPrintPageIndex"),
)
if mibBuilder.loadTexts:
    brFuncLockUserPrintPageEntry.setStatus("mandatory")


class _BrFuncLockUserPrintPageIndex_Type(Integer32):
    """Custom type brFuncLockUserPrintPageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BrFuncLockUserPrintPageIndex_Type.__name__ = "Integer32"
_BrFuncLockUserPrintPageIndex_Object = MibTableColumn
brFuncLockUserPrintPageIndex = _BrFuncLockUserPrintPageIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 25, 1, 1),
    _BrFuncLockUserPrintPageIndex_Type()
)
brFuncLockUserPrintPageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFuncLockUserPrintPageIndex.setStatus("mandatory")


class _BrFuncLockUserPrintPageLimitEnable_Type(Integer32):
    """Custom type brFuncLockUserPrintPageLimitEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrFuncLockUserPrintPageLimitEnable_Type.__name__ = "Integer32"
_BrFuncLockUserPrintPageLimitEnable_Object = MibTableColumn
brFuncLockUserPrintPageLimitEnable = _BrFuncLockUserPrintPageLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 25, 1, 2),
    _BrFuncLockUserPrintPageLimitEnable_Type()
)
brFuncLockUserPrintPageLimitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brFuncLockUserPrintPageLimitEnable.setStatus("mandatory")


class _BrFuncLockUserPrintPageCountMono_Type(Integer32):
    """Custom type brFuncLockUserPrintPageCountMono based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_BrFuncLockUserPrintPageCountMono_Type.__name__ = "Integer32"
_BrFuncLockUserPrintPageCountMono_Object = MibTableColumn
brFuncLockUserPrintPageCountMono = _BrFuncLockUserPrintPageCountMono_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 25, 1, 3),
    _BrFuncLockUserPrintPageCountMono_Type()
)
brFuncLockUserPrintPageCountMono.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFuncLockUserPrintPageCountMono.setStatus("mandatory")


class _BrFuncLockUserPrintPageCountColor_Type(Integer32):
    """Custom type brFuncLockUserPrintPageCountColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_BrFuncLockUserPrintPageCountColor_Type.__name__ = "Integer32"
_BrFuncLockUserPrintPageCountColor_Object = MibTableColumn
brFuncLockUserPrintPageCountColor = _BrFuncLockUserPrintPageCountColor_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 25, 1, 4),
    _BrFuncLockUserPrintPageCountColor_Type()
)
brFuncLockUserPrintPageCountColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFuncLockUserPrintPageCountColor.setStatus("mandatory")


class _BrFuncLockUserPrintPageMax_Type(Integer32):
    """Custom type brFuncLockUserPrintPageMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999999),
    )


_BrFuncLockUserPrintPageMax_Type.__name__ = "Integer32"
_BrFuncLockUserPrintPageMax_Object = MibTableColumn
brFuncLockUserPrintPageMax = _BrFuncLockUserPrintPageMax_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 25, 1, 5),
    _BrFuncLockUserPrintPageMax_Type()
)
brFuncLockUserPrintPageMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brFuncLockUserPrintPageMax.setStatus("mandatory")


class _BrFuncLockUserPrintPageCountMonoLast_Type(Integer32):
    """Custom type brFuncLockUserPrintPageCountMonoLast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_BrFuncLockUserPrintPageCountMonoLast_Type.__name__ = "Integer32"
_BrFuncLockUserPrintPageCountMonoLast_Object = MibTableColumn
brFuncLockUserPrintPageCountMonoLast = _BrFuncLockUserPrintPageCountMonoLast_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 25, 1, 6),
    _BrFuncLockUserPrintPageCountMonoLast_Type()
)
brFuncLockUserPrintPageCountMonoLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFuncLockUserPrintPageCountMonoLast.setStatus("mandatory")


class _BrFuncLockUserPrintPageCountColorLast_Type(Integer32):
    """Custom type brFuncLockUserPrintPageCountColorLast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_BrFuncLockUserPrintPageCountColorLast_Type.__name__ = "Integer32"
_BrFuncLockUserPrintPageCountColorLast_Object = MibTableColumn
brFuncLockUserPrintPageCountColorLast = _BrFuncLockUserPrintPageCountColorLast_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 25, 1, 7),
    _BrFuncLockUserPrintPageCountColorLast_Type()
)
brFuncLockUserPrintPageCountColorLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFuncLockUserPrintPageCountColorLast.setStatus("mandatory")


class _BrFuncLockPcLoginNameAuthEnable_Type(Integer32):
    """Custom type brFuncLockPcLoginNameAuthEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrFuncLockPcLoginNameAuthEnable_Type.__name__ = "Integer32"
_BrFuncLockPcLoginNameAuthEnable_Object = MibScalar
brFuncLockPcLoginNameAuthEnable = _BrFuncLockPcLoginNameAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 26),
    _BrFuncLockPcLoginNameAuthEnable_Type()
)
brFuncLockPcLoginNameAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brFuncLockPcLoginNameAuthEnable.setStatus("mandatory")
_BrFuncLockPcLoginNameAuthCount_Type = Integer32
_BrFuncLockPcLoginNameAuthCount_Object = MibScalar
brFuncLockPcLoginNameAuthCount = _BrFuncLockPcLoginNameAuthCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 27),
    _BrFuncLockPcLoginNameAuthCount_Type()
)
brFuncLockPcLoginNameAuthCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFuncLockPcLoginNameAuthCount.setStatus("mandatory")
_BrFuncLockPcLoginNameTable_Object = MibTable
brFuncLockPcLoginNameTable = _BrFuncLockPcLoginNameTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 28)
)
if mibBuilder.loadTexts:
    brFuncLockPcLoginNameTable.setStatus("mandatory")
_BrFuncLockPcLoginNameEntry_Object = MibTableRow
brFuncLockPcLoginNameEntry = _BrFuncLockPcLoginNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 28, 1)
)
brFuncLockPcLoginNameEntry.setIndexNames(
    (0, "BROTHER-MIB", "brFuncLockPcLoginNameAuthIndex"),
)
if mibBuilder.loadTexts:
    brFuncLockPcLoginNameEntry.setStatus("mandatory")


class _BrFuncLockPcLoginNameAuthIndex_Type(Integer32):
    """Custom type brFuncLockPcLoginNameAuthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_BrFuncLockPcLoginNameAuthIndex_Type.__name__ = "Integer32"
_BrFuncLockPcLoginNameAuthIndex_Object = MibTableColumn
brFuncLockPcLoginNameAuthIndex = _BrFuncLockPcLoginNameAuthIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 28, 1, 1),
    _BrFuncLockPcLoginNameAuthIndex_Type()
)
brFuncLockPcLoginNameAuthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFuncLockPcLoginNameAuthIndex.setStatus("mandatory")
_BrFuncLockPcLoginName_Type = OctetString
_BrFuncLockPcLoginName_Object = MibTableColumn
brFuncLockPcLoginName = _BrFuncLockPcLoginName_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 28, 1, 2),
    _BrFuncLockPcLoginName_Type()
)
brFuncLockPcLoginName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brFuncLockPcLoginName.setStatus("mandatory")


class _BrFuncLockPcLoginNameAuthID_Type(Integer32):
    """Custom type brFuncLockPcLoginNameAuthID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_BrFuncLockPcLoginNameAuthID_Type.__name__ = "Integer32"
_BrFuncLockPcLoginNameAuthID_Object = MibTableColumn
brFuncLockPcLoginNameAuthID = _BrFuncLockPcLoginNameAuthID_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 28, 1, 3),
    _BrFuncLockPcLoginNameAuthID_Type()
)
brFuncLockPcLoginNameAuthID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brFuncLockPcLoginNameAuthID.setStatus("mandatory")


class _BrFuncLockPublicPrintPageCountMonoLast_Type(Integer32):
    """Custom type brFuncLockPublicPrintPageCountMonoLast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_BrFuncLockPublicPrintPageCountMonoLast_Type.__name__ = "Integer32"
_BrFuncLockPublicPrintPageCountMonoLast_Object = MibScalar
brFuncLockPublicPrintPageCountMonoLast = _BrFuncLockPublicPrintPageCountMonoLast_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 29),
    _BrFuncLockPublicPrintPageCountMonoLast_Type()
)
brFuncLockPublicPrintPageCountMonoLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFuncLockPublicPrintPageCountMonoLast.setStatus("mandatory")


class _BrFuncLockPublicPrintPageCountColorLast_Type(Integer32):
    """Custom type brFuncLockPublicPrintPageCountColorLast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_BrFuncLockPublicPrintPageCountColorLast_Type.__name__ = "Integer32"
_BrFuncLockPublicPrintPageCountColorLast_Object = MibScalar
brFuncLockPublicPrintPageCountColorLast = _BrFuncLockPublicPrintPageCountColorLast_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 30),
    _BrFuncLockPublicPrintPageCountColorLast_Type()
)
brFuncLockPublicPrintPageCountColorLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFuncLockPublicPrintPageCountColorLast.setStatus("mandatory")
_Autocountreset_ObjectIdentity = ObjectIdentity
autocountreset = _Autocountreset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 31)
)


class _BrFuncLockAutoCountResetFrequency_Type(Integer32):
    """Custom type brFuncLockAutoCountResetFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BrFuncLockAutoCountResetFrequency_Type.__name__ = "Integer32"
_BrFuncLockAutoCountResetFrequency_Object = MibScalar
brFuncLockAutoCountResetFrequency = _BrFuncLockAutoCountResetFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 31, 1),
    _BrFuncLockAutoCountResetFrequency_Type()
)
brFuncLockAutoCountResetFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brFuncLockAutoCountResetFrequency.setStatus("mandatory")


class _BrFuncLockAutoCountResetTime_Type(OctetString):
    """Custom type brFuncLockAutoCountResetTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_BrFuncLockAutoCountResetTime_Type.__name__ = "OctetString"
_BrFuncLockAutoCountResetTime_Object = MibScalar
brFuncLockAutoCountResetTime = _BrFuncLockAutoCountResetTime_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 31, 2),
    _BrFuncLockAutoCountResetTime_Type()
)
brFuncLockAutoCountResetTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brFuncLockAutoCountResetTime.setStatus("mandatory")


class _BrFuncLockAutoCountResetWeek_Type(Integer32):
    """Custom type brFuncLockAutoCountResetWeek based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_BrFuncLockAutoCountResetWeek_Type.__name__ = "Integer32"
_BrFuncLockAutoCountResetWeek_Object = MibScalar
brFuncLockAutoCountResetWeek = _BrFuncLockAutoCountResetWeek_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 31, 3),
    _BrFuncLockAutoCountResetWeek_Type()
)
brFuncLockAutoCountResetWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brFuncLockAutoCountResetWeek.setStatus("mandatory")


class _BrFuncLockAutoCountResetDate_Type(Integer32):
    """Custom type brFuncLockAutoCountResetDate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_BrFuncLockAutoCountResetDate_Type.__name__ = "Integer32"
_BrFuncLockAutoCountResetDate_Object = MibScalar
brFuncLockAutoCountResetDate = _BrFuncLockAutoCountResetDate_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 2, 63, 31, 4),
    _BrFuncLockAutoCountResetDate_Type()
)
brFuncLockAutoCountResetDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brFuncLockAutoCountResetDate.setStatus("mandatory")
_Mail_ObjectIdentity = ObjectIdentity
mail = _Mail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 3)
)


class _BrPrtMailbox_Type(Integer32):
    """Custom type brPrtMailbox based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BrPrtMailbox_Type.__name__ = "Integer32"
_BrPrtMailbox_Object = MibScalar
brPrtMailbox = _BrPrtMailbox_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 3, 1),
    _BrPrtMailbox_Type()
)
brPrtMailbox.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtMailbox.setStatus("mandatory")
_BrPrtMailboxProtectTable_Object = MibTable
brPrtMailboxProtectTable = _BrPrtMailboxProtectTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 3, 2)
)
if mibBuilder.loadTexts:
    brPrtMailboxProtectTable.setStatus("mandatory")
_BrPrtMailboxProtectEntry_Object = MibTableRow
brPrtMailboxProtectEntry = _BrPrtMailboxProtectEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 3, 2, 1)
)
brPrtMailboxProtectEntry.setIndexNames(
    (0, "BROTHER-MIB", "brPrtMailboxProtectIndex"),
)
if mibBuilder.loadTexts:
    brPrtMailboxProtectEntry.setStatus("mandatory")


class _BrPrtMailboxProtectIndex_Type(Integer32):
    """Custom type brPrtMailboxProtectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BrPrtMailboxProtectIndex_Type.__name__ = "Integer32"
_BrPrtMailboxProtectIndex_Object = MibTableColumn
brPrtMailboxProtectIndex = _BrPrtMailboxProtectIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 3, 2, 1, 1),
    _BrPrtMailboxProtectIndex_Type()
)
brPrtMailboxProtectIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtMailboxProtectIndex.setStatus("mandatory")


class _BrPrtMailboxProtect_Type(Integer32):
    """Custom type brPrtMailboxProtect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BrPrtMailboxProtect_Type.__name__ = "Integer32"
_BrPrtMailboxProtect_Object = MibTableColumn
brPrtMailboxProtect = _BrPrtMailboxProtect_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 3, 2, 1, 2),
    _BrPrtMailboxProtect_Type()
)
brPrtMailboxProtect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtMailboxProtect.setStatus("mandatory")
_BrPrtAvoidMailboxFullTable_Object = MibTable
brPrtAvoidMailboxFullTable = _BrPrtAvoidMailboxFullTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 3, 3)
)
if mibBuilder.loadTexts:
    brPrtAvoidMailboxFullTable.setStatus("mandatory")
_BrPrtAvoidMailboxFullEntry_Object = MibTableRow
brPrtAvoidMailboxFullEntry = _BrPrtAvoidMailboxFullEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 3, 3, 1)
)
brPrtAvoidMailboxFullEntry.setIndexNames(
    (0, "BROTHER-MIB", "brPrtAvoidMailboxFullIndex"),
)
if mibBuilder.loadTexts:
    brPrtAvoidMailboxFullEntry.setStatus("mandatory")


class _BrPrtAvoidMailboxFullIndex_Type(Integer32):
    """Custom type brPrtAvoidMailboxFullIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BrPrtAvoidMailboxFullIndex_Type.__name__ = "Integer32"
_BrPrtAvoidMailboxFullIndex_Object = MibTableColumn
brPrtAvoidMailboxFullIndex = _BrPrtAvoidMailboxFullIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 3, 3, 1, 1),
    _BrPrtAvoidMailboxFullIndex_Type()
)
brPrtAvoidMailboxFullIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtAvoidMailboxFullIndex.setStatus("mandatory")


class _BrPrtAvoidMailboxFull_Type(Integer32):
    """Custom type brPrtAvoidMailboxFull based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BrPrtAvoidMailboxFull_Type.__name__ = "Integer32"
_BrPrtAvoidMailboxFull_Object = MibTableColumn
brPrtAvoidMailboxFull = _BrPrtAvoidMailboxFull_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 3, 3, 1, 2),
    _BrPrtAvoidMailboxFull_Type()
)
brPrtAvoidMailboxFull.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtAvoidMailboxFull.setStatus("mandatory")


class _BrPrtMailboxOutbin_Type(Integer32):
    """Custom type brPrtMailboxOutbin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 110),
    )


_BrPrtMailboxOutbin_Type.__name__ = "Integer32"
_BrPrtMailboxOutbin_Object = MibScalar
brPrtMailboxOutbin = _BrPrtMailboxOutbin_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 3, 4),
    _BrPrtMailboxOutbin_Type()
)
brPrtMailboxOutbin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtMailboxOutbin.setStatus("mandatory")


class _BrPrtMailboxProtectGroup_Type(Integer32):
    """Custom type brPrtMailboxProtectGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_BrPrtMailboxProtectGroup_Type.__name__ = "Integer32"
_BrPrtMailboxProtectGroup_Object = MibScalar
brPrtMailboxProtectGroup = _BrPrtMailboxProtectGroup_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 3, 5),
    _BrPrtMailboxProtectGroup_Type()
)
brPrtMailboxProtectGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtMailboxProtectGroup.setStatus("mandatory")


class _BrPrtAvoidMailboxFullGroup_Type(Integer32):
    """Custom type brPrtAvoidMailboxFullGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrPrtAvoidMailboxFullGroup_Type.__name__ = "Integer32"
_BrPrtAvoidMailboxFullGroup_Object = MibScalar
brPrtAvoidMailboxFullGroup = _BrPrtAvoidMailboxFullGroup_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 3, 6),
    _BrPrtAvoidMailboxFullGroup_Type()
)
brPrtAvoidMailboxFullGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrtAvoidMailboxFullGroup.setStatus("mandatory")
_Finisher_ObjectIdentity = ObjectIdentity
finisher = _Finisher_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 4)
)


class _BrPrtFinisher_Type(Integer32):
    """Custom type brPrtFinisher based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrPrtFinisher_Type.__name__ = "Integer32"
_BrPrtFinisher_Object = MibScalar
brPrtFinisher = _BrPrtFinisher_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 4, 1),
    _BrPrtFinisher_Type()
)
brPrtFinisher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPrtFinisher.setStatus("mandatory")
_Catch_tray_ObjectIdentity = ObjectIdentity
catch_tray = _Catch_tray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 5)
)


class _BrPrtCatchTray_Type(Integer32):
    """Custom type brPrtCatchTray based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BrPrtCatchTray_Type.__name__ = "Integer32"
_BrPrtCatchTray_Object = MibScalar
brPrtCatchTray = _BrPrtCatchTray_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 1, 5, 1),
    _BrPrtCatchTray_Type()
)
brPrtCatchTray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPrtCatchTray.setStatus("mandatory")
_Pagesetup_ObjectIdentity = ObjectIdentity
pagesetup = _Pagesetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2)
)
_Pcl_ObjectIdentity = ObjectIdentity
pcl = _Pcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 1)
)
_Margin_p_ObjectIdentity = ObjectIdentity
margin_p = _Margin_p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 1, 1)
)


class _BrPagePCLLeftMargin_Type(Integer32):
    """Custom type brPagePCLLeftMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrPagePCLLeftMargin_Type.__name__ = "Integer32"
_BrPagePCLLeftMargin_Object = MibScalar
brPagePCLLeftMargin = _BrPagePCLLeftMargin_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 1, 1, 1),
    _BrPagePCLLeftMargin_Type()
)
brPagePCLLeftMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPagePCLLeftMargin.setStatus("mandatory")


class _BrPagePCLRightMargin_Type(Integer32):
    """Custom type brPagePCLRightMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrPagePCLRightMargin_Type.__name__ = "Integer32"
_BrPagePCLRightMargin_Object = MibScalar
brPagePCLRightMargin = _BrPagePCLRightMargin_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 1, 1, 2),
    _BrPagePCLRightMargin_Type()
)
brPagePCLRightMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPagePCLRightMargin.setStatus("mandatory")


class _BrPagePCLTopMargin_Type(Integer32):
    """Custom type brPagePCLTopMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_BrPagePCLTopMargin_Type.__name__ = "Integer32"
_BrPagePCLTopMargin_Object = MibScalar
brPagePCLTopMargin = _BrPagePCLTopMargin_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 1, 1, 3),
    _BrPagePCLTopMargin_Type()
)
brPagePCLTopMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPagePCLTopMargin.setStatus("mandatory")


class _BrPagePCLBottomMargin_Type(Integer32):
    """Custom type brPagePCLBottomMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_BrPagePCLBottomMargin_Type.__name__ = "Integer32"
_BrPagePCLBottomMargin_Object = MibScalar
brPagePCLBottomMargin = _BrPagePCLBottomMargin_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 1, 1, 4),
    _BrPagePCLBottomMargin_Type()
)
brPagePCLBottomMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPagePCLBottomMargin.setStatus("mandatory")


class _BrPagePCLLines_Type(Integer32):
    """Custom type brPagePCLLines based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 128),
    )


_BrPagePCLLines_Type.__name__ = "Integer32"
_BrPagePCLLines_Object = MibScalar
brPagePCLLines = _BrPagePCLLines_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 1, 1, 5),
    _BrPagePCLLines_Type()
)
brPagePCLLines.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPagePCLLines.setStatus("mandatory")
_Auto_p_ObjectIdentity = ObjectIdentity
auto_p = _Auto_p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 1, 2)
)


class _BrPagePCLAutoLF_Type(Integer32):
    """Custom type brPagePCLAutoLF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BrPagePCLAutoLF_Type.__name__ = "Integer32"
_BrPagePCLAutoLF_Object = MibScalar
brPagePCLAutoLF = _BrPagePCLAutoLF_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 1, 2, 1),
    _BrPagePCLAutoLF_Type()
)
brPagePCLAutoLF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPagePCLAutoLF.setStatus("mandatory")


class _BrPagePCLAutoCR_Type(Integer32):
    """Custom type brPagePCLAutoCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BrPagePCLAutoCR_Type.__name__ = "Integer32"
_BrPagePCLAutoCR_Object = MibScalar
brPagePCLAutoCR = _BrPagePCLAutoCR_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 1, 2, 2),
    _BrPagePCLAutoCR_Type()
)
brPagePCLAutoCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPagePCLAutoCR.setStatus("mandatory")


class _BrPagePCLAutoWrap_Type(Integer32):
    """Custom type brPagePCLAutoWrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BrPagePCLAutoWrap_Type.__name__ = "Integer32"
_BrPagePCLAutoWrap_Object = MibScalar
brPagePCLAutoWrap = _BrPagePCLAutoWrap_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 1, 2, 3),
    _BrPagePCLAutoWrap_Type()
)
brPagePCLAutoWrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPagePCLAutoWrap.setStatus("mandatory")


class _BrPagePCLAutoSkip_Type(Integer32):
    """Custom type brPagePCLAutoSkip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BrPagePCLAutoSkip_Type.__name__ = "Integer32"
_BrPagePCLAutoSkip_Object = MibScalar
brPagePCLAutoSkip = _BrPagePCLAutoSkip_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 1, 2, 4),
    _BrPagePCLAutoSkip_Type()
)
brPagePCLAutoSkip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPagePCLAutoSkip.setStatus("mandatory")
_Ps_ObjectIdentity = ObjectIdentity
ps = _Ps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 2)
)


class _BrPagePSPrintPSError_Type(Integer32):
    """Custom type brPagePSPrintPSError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_BrPagePSPrintPSError_Type.__name__ = "Integer32"
_BrPagePSPrintPSError_Object = MibScalar
brPagePSPrintPSError = _BrPagePSPrintPSError_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 2, 1),
    _BrPagePSPrintPSError_Type()
)
brPagePSPrintPSError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPagePSPrintPSError.setStatus("mandatory")


class _BrPagePSKeepPCLFonts_Type(Integer32):
    """Custom type brPagePSKeepPCLFonts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_BrPagePSKeepPCLFonts_Type.__name__ = "Integer32"
_BrPagePSKeepPCLFonts_Object = MibScalar
brPagePSKeepPCLFonts = _BrPagePSKeepPCLFonts_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 2, 2),
    _BrPagePSKeepPCLFonts_Type()
)
brPagePSKeepPCLFonts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPagePSKeepPCLFonts.setStatus("mandatory")


class _BrPagePSCAPTsetting_Type(Integer32):
    """Custom type brPagePSCAPTsetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_BrPagePSCAPTsetting_Type.__name__ = "Integer32"
_BrPagePSCAPTsetting_Object = MibScalar
brPagePSCAPTsetting = _BrPagePSCAPTsetting_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 2, 3),
    _BrPagePSCAPTsetting_Type()
)
brPagePSCAPTsetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPagePSCAPTsetting.setStatus("mandatory")
_Gl_ObjectIdentity = ObjectIdentity
gl = _Gl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 3)
)
_Pen1_ObjectIdentity = ObjectIdentity
pen1 = _Pen1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 3, 1)
)


class _BrPageGLPen1Size_Type(Integer32):
    """Custom type brPageGLPen1Size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_BrPageGLPen1Size_Type.__name__ = "Integer32"
_BrPageGLPen1Size_Object = MibScalar
brPageGLPen1Size = _BrPageGLPen1Size_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 3, 1, 1),
    _BrPageGLPen1Size_Type()
)
brPageGLPen1Size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPageGLPen1Size.setStatus("mandatory")


class _BrPageGLPen1GrayLevel_Type(Integer32):
    """Custom type brPageGLPen1GrayLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_BrPageGLPen1GrayLevel_Type.__name__ = "Integer32"
_BrPageGLPen1GrayLevel_Object = MibScalar
brPageGLPen1GrayLevel = _BrPageGLPen1GrayLevel_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 3, 1, 2),
    _BrPageGLPen1GrayLevel_Type()
)
brPageGLPen1GrayLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPageGLPen1GrayLevel.setStatus("mandatory")
_Pen2_ObjectIdentity = ObjectIdentity
pen2 = _Pen2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 3, 2)
)


class _BrPageGLPen2Size_Type(Integer32):
    """Custom type brPageGLPen2Size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_BrPageGLPen2Size_Type.__name__ = "Integer32"
_BrPageGLPen2Size_Object = MibScalar
brPageGLPen2Size = _BrPageGLPen2Size_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 3, 2, 1),
    _BrPageGLPen2Size_Type()
)
brPageGLPen2Size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPageGLPen2Size.setStatus("mandatory")


class _BrPageGLPen2GrayLevel_Type(Integer32):
    """Custom type brPageGLPen2GrayLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_BrPageGLPen2GrayLevel_Type.__name__ = "Integer32"
_BrPageGLPen2GrayLevel_Object = MibScalar
brPageGLPen2GrayLevel = _BrPageGLPen2GrayLevel_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 3, 2, 2),
    _BrPageGLPen2GrayLevel_Type()
)
brPageGLPen2GrayLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPageGLPen2GrayLevel.setStatus("mandatory")
_Pen3_ObjectIdentity = ObjectIdentity
pen3 = _Pen3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 3, 3)
)


class _BrPageGLPen3Size_Type(Integer32):
    """Custom type brPageGLPen3Size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_BrPageGLPen3Size_Type.__name__ = "Integer32"
_BrPageGLPen3Size_Object = MibScalar
brPageGLPen3Size = _BrPageGLPen3Size_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 3, 3, 1),
    _BrPageGLPen3Size_Type()
)
brPageGLPen3Size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPageGLPen3Size.setStatus("mandatory")


class _BrPageGLPen3GrayLevel_Type(Integer32):
    """Custom type brPageGLPen3GrayLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_BrPageGLPen3GrayLevel_Type.__name__ = "Integer32"
_BrPageGLPen3GrayLevel_Object = MibScalar
brPageGLPen3GrayLevel = _BrPageGLPen3GrayLevel_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 3, 3, 2),
    _BrPageGLPen3GrayLevel_Type()
)
brPageGLPen3GrayLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPageGLPen3GrayLevel.setStatus("mandatory")
_Pen4_ObjectIdentity = ObjectIdentity
pen4 = _Pen4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 3, 4)
)


class _BrPageGLPen4Size_Type(Integer32):
    """Custom type brPageGLPen4Size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_BrPageGLPen4Size_Type.__name__ = "Integer32"
_BrPageGLPen4Size_Object = MibScalar
brPageGLPen4Size = _BrPageGLPen4Size_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 3, 4, 1),
    _BrPageGLPen4Size_Type()
)
brPageGLPen4Size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPageGLPen4Size.setStatus("mandatory")


class _BrPageGLPen4GrayLevel_Type(Integer32):
    """Custom type brPageGLPen4GrayLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_BrPageGLPen4GrayLevel_Type.__name__ = "Integer32"
_BrPageGLPen4GrayLevel_Object = MibScalar
brPageGLPen4GrayLevel = _BrPageGLPen4GrayLevel_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 3, 4, 2),
    _BrPageGLPen4GrayLevel_Type()
)
brPageGLPen4GrayLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPageGLPen4GrayLevel.setStatus("mandatory")
_Pen5_ObjectIdentity = ObjectIdentity
pen5 = _Pen5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 3, 5)
)


class _BrPageGLPen5Size_Type(Integer32):
    """Custom type brPageGLPen5Size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_BrPageGLPen5Size_Type.__name__ = "Integer32"
_BrPageGLPen5Size_Object = MibScalar
brPageGLPen5Size = _BrPageGLPen5Size_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 3, 5, 1),
    _BrPageGLPen5Size_Type()
)
brPageGLPen5Size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPageGLPen5Size.setStatus("mandatory")


class _BrPageGLPen5GrayLevel_Type(Integer32):
    """Custom type brPageGLPen5GrayLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_BrPageGLPen5GrayLevel_Type.__name__ = "Integer32"
_BrPageGLPen5GrayLevel_Object = MibScalar
brPageGLPen5GrayLevel = _BrPageGLPen5GrayLevel_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 3, 5, 2),
    _BrPageGLPen5GrayLevel_Type()
)
brPageGLPen5GrayLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPageGLPen5GrayLevel.setStatus("mandatory")
_Pen6_ObjectIdentity = ObjectIdentity
pen6 = _Pen6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 3, 6)
)


class _BrPageGLPen6Size_Type(Integer32):
    """Custom type brPageGLPen6Size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_BrPageGLPen6Size_Type.__name__ = "Integer32"
_BrPageGLPen6Size_Object = MibScalar
brPageGLPen6Size = _BrPageGLPen6Size_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 3, 6, 1),
    _BrPageGLPen6Size_Type()
)
brPageGLPen6Size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPageGLPen6Size.setStatus("mandatory")


class _BrPageGLPen6GrayLevel_Type(Integer32):
    """Custom type brPageGLPen6GrayLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_BrPageGLPen6GrayLevel_Type.__name__ = "Integer32"
_BrPageGLPen6GrayLevel_Object = MibScalar
brPageGLPen6GrayLevel = _BrPageGLPen6GrayLevel_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 3, 6, 2),
    _BrPageGLPen6GrayLevel_Type()
)
brPageGLPen6GrayLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPageGLPen6GrayLevel.setStatus("mandatory")
_Epson_ObjectIdentity = ObjectIdentity
epson = _Epson_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 4)
)
_Margin_e_ObjectIdentity = ObjectIdentity
margin_e = _Margin_e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 4, 1)
)


class _BrPageEPSONLeftMargin_Type(Integer32):
    """Custom type brPageEPSONLeftMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrPageEPSONLeftMargin_Type.__name__ = "Integer32"
_BrPageEPSONLeftMargin_Object = MibScalar
brPageEPSONLeftMargin = _BrPageEPSONLeftMargin_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 4, 1, 1),
    _BrPageEPSONLeftMargin_Type()
)
brPageEPSONLeftMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPageEPSONLeftMargin.setStatus("mandatory")


class _BrPageEPSONRightMargin_Type(Integer32):
    """Custom type brPageEPSONRightMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrPageEPSONRightMargin_Type.__name__ = "Integer32"
_BrPageEPSONRightMargin_Object = MibScalar
brPageEPSONRightMargin = _BrPageEPSONRightMargin_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 4, 1, 2),
    _BrPageEPSONRightMargin_Type()
)
brPageEPSONRightMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPageEPSONRightMargin.setStatus("mandatory")


class _BrPageEPSONTopMargin_Type(Integer32):
    """Custom type brPageEPSONTopMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_BrPageEPSONTopMargin_Type.__name__ = "Integer32"
_BrPageEPSONTopMargin_Object = MibScalar
brPageEPSONTopMargin = _BrPageEPSONTopMargin_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 4, 1, 3),
    _BrPageEPSONTopMargin_Type()
)
brPageEPSONTopMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPageEPSONTopMargin.setStatus("mandatory")


class _BrPageEPSONBottomMargin_Type(Integer32):
    """Custom type brPageEPSONBottomMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_BrPageEPSONBottomMargin_Type.__name__ = "Integer32"
_BrPageEPSONBottomMargin_Object = MibScalar
brPageEPSONBottomMargin = _BrPageEPSONBottomMargin_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 4, 1, 4),
    _BrPageEPSONBottomMargin_Type()
)
brPageEPSONBottomMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPageEPSONBottomMargin.setStatus("mandatory")


class _BrPageEPSONLines_Type(Integer32):
    """Custom type brPageEPSONLines based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 128),
    )


_BrPageEPSONLines_Type.__name__ = "Integer32"
_BrPageEPSONLines_Object = MibScalar
brPageEPSONLines = _BrPageEPSONLines_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 4, 1, 5),
    _BrPageEPSONLines_Type()
)
brPageEPSONLines.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPageEPSONLines.setStatus("mandatory")
_Auto_e_ObjectIdentity = ObjectIdentity
auto_e = _Auto_e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 4, 2)
)


class _BrPageEPSONAutoLF_Type(Integer32):
    """Custom type brPageEPSONAutoLF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BrPageEPSONAutoLF_Type.__name__ = "Integer32"
_BrPageEPSONAutoLF_Object = MibScalar
brPageEPSONAutoLF = _BrPageEPSONAutoLF_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 4, 2, 1),
    _BrPageEPSONAutoLF_Type()
)
brPageEPSONAutoLF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPageEPSONAutoLF.setStatus("mandatory")


class _BrPageEPSONAutoMask_Type(Integer32):
    """Custom type brPageEPSONAutoMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BrPageEPSONAutoMask_Type.__name__ = "Integer32"
_BrPageEPSONAutoMask_Object = MibScalar
brPageEPSONAutoMask = _BrPageEPSONAutoMask_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 4, 2, 5),
    _BrPageEPSONAutoMask_Type()
)
brPageEPSONAutoMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPageEPSONAutoMask.setStatus("mandatory")
_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 5)
)
_Margin_i_ObjectIdentity = ObjectIdentity
margin_i = _Margin_i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 5, 1)
)


class _BrPageIBMLeftMargin_Type(Integer32):
    """Custom type brPageIBMLeftMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrPageIBMLeftMargin_Type.__name__ = "Integer32"
_BrPageIBMLeftMargin_Object = MibScalar
brPageIBMLeftMargin = _BrPageIBMLeftMargin_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 5, 1, 1),
    _BrPageIBMLeftMargin_Type()
)
brPageIBMLeftMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPageIBMLeftMargin.setStatus("mandatory")


class _BrPageIBMRightMargin_Type(Integer32):
    """Custom type brPageIBMRightMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrPageIBMRightMargin_Type.__name__ = "Integer32"
_BrPageIBMRightMargin_Object = MibScalar
brPageIBMRightMargin = _BrPageIBMRightMargin_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 5, 1, 2),
    _BrPageIBMRightMargin_Type()
)
brPageIBMRightMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPageIBMRightMargin.setStatus("mandatory")


class _BrPageIBMTopMargin_Type(Integer32):
    """Custom type brPageIBMTopMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_BrPageIBMTopMargin_Type.__name__ = "Integer32"
_BrPageIBMTopMargin_Object = MibScalar
brPageIBMTopMargin = _BrPageIBMTopMargin_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 5, 1, 3),
    _BrPageIBMTopMargin_Type()
)
brPageIBMTopMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPageIBMTopMargin.setStatus("mandatory")


class _BrPageIBMBottomMargin_Type(Integer32):
    """Custom type brPageIBMBottomMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_BrPageIBMBottomMargin_Type.__name__ = "Integer32"
_BrPageIBMBottomMargin_Object = MibScalar
brPageIBMBottomMargin = _BrPageIBMBottomMargin_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 5, 1, 4),
    _BrPageIBMBottomMargin_Type()
)
brPageIBMBottomMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPageIBMBottomMargin.setStatus("mandatory")


class _BrPageIBMLines_Type(Integer32):
    """Custom type brPageIBMLines based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 128),
    )


_BrPageIBMLines_Type.__name__ = "Integer32"
_BrPageIBMLines_Object = MibScalar
brPageIBMLines = _BrPageIBMLines_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 5, 1, 5),
    _BrPageIBMLines_Type()
)
brPageIBMLines.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPageIBMLines.setStatus("mandatory")
_Auto_i_ObjectIdentity = ObjectIdentity
auto_i = _Auto_i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 5, 2)
)


class _BrPageIBMAutoLF_Type(Integer32):
    """Custom type brPageIBMAutoLF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BrPageIBMAutoLF_Type.__name__ = "Integer32"
_BrPageIBMAutoLF_Object = MibScalar
brPageIBMAutoLF = _BrPageIBMAutoLF_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 5, 2, 1),
    _BrPageIBMAutoLF_Type()
)
brPageIBMAutoLF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPageIBMAutoLF.setStatus("mandatory")


class _BrPageIBMAutoCR_Type(Integer32):
    """Custom type brPageIBMAutoCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BrPageIBMAutoCR_Type.__name__ = "Integer32"
_BrPageIBMAutoCR_Object = MibScalar
brPageIBMAutoCR = _BrPageIBMAutoCR_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 5, 2, 2),
    _BrPageIBMAutoCR_Type()
)
brPageIBMAutoCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPageIBMAutoCR.setStatus("mandatory")


class _BrPageIBMAutoMask_Type(Integer32):
    """Custom type brPageIBMAutoMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BrPageIBMAutoMask_Type.__name__ = "Integer32"
_BrPageIBMAutoMask_Object = MibScalar
brPageIBMAutoMask = _BrPageIBMAutoMask_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 2, 5, 2, 5),
    _BrPageIBMAutoMask_Type()
)
brPageIBMAutoMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPageIBMAutoMask.setStatus("mandatory")
_Fontsetup_ObjectIdentity = ObjectIdentity
fontsetup = _Fontsetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 3)
)


class _BrFontName_Type(Integer32):
    """Custom type brFontName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_BrFontName_Type.__name__ = "Integer32"
_BrFontName_Object = MibScalar
brFontName = _BrFontName_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 3, 1),
    _BrFontName_Type()
)
brFontName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brFontName.setStatus("mandatory")


class _BrFontPointSize_Type(Integer32):
    """Custom type brFontPointSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 99999),
    )


_BrFontPointSize_Type.__name__ = "Integer32"
_BrFontPointSize_Object = MibScalar
brFontPointSize = _BrFontPointSize_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 3, 2),
    _BrFontPointSize_Type()
)
brFontPointSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brFontPointSize.setStatus("mandatory")


class _BrFontPitch_Type(Integer32):
    """Custom type brFontPitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_BrFontPitch_Type.__name__ = "Integer32"
_BrFontPitch_Object = MibScalar
brFontPitch = _BrFontPitch_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 3, 3),
    _BrFontPitch_Type()
)
brFontPitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brFontPitch.setStatus("mandatory")


class _BrFontSymbolSet_Type(Integer32):
    """Custom type brFontSymbolSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_BrFontSymbolSet_Type.__name__ = "Integer32"
_BrFontSymbolSet_Object = MibScalar
brFontSymbolSet = _BrFontSymbolSet_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 3, 4),
    _BrFontSymbolSet_Type()
)
brFontSymbolSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brFontSymbolSet.setStatus("mandatory")
_Controlpanel_ObjectIdentity = ObjectIdentity
controlpanel = _Controlpanel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 4)
)
_Reset_ObjectIdentity = ObjectIdentity
reset = _Reset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 4, 1)
)


class _BrPanelResetUser_Type(Integer32):
    """Custom type brPanelResetUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BrPanelResetUser_Type.__name__ = "Integer32"
_BrPanelResetUser_Object = MibScalar
brPanelResetUser = _BrPanelResetUser_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 4, 1, 1),
    _BrPanelResetUser_Type()
)
brPanelResetUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPanelResetUser.setStatus("mandatory")


class _BrPanelResetFactory_Type(Integer32):
    """Custom type brPanelResetFactory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BrPanelResetFactory_Type.__name__ = "Integer32"
_BrPanelResetFactory_Object = MibScalar
brPanelResetFactory = _BrPanelResetFactory_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 4, 1, 2),
    _BrPanelResetFactory_Type()
)
brPanelResetFactory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPanelResetFactory.setStatus("mandatory")
_Test_ObjectIdentity = ObjectIdentity
test = _Test_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 4, 2)
)


class _BrPanelTestConfiguration_Type(Integer32):
    """Custom type brPanelTestConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BrPanelTestConfiguration_Type.__name__ = "Integer32"
_BrPanelTestConfiguration_Object = MibScalar
brPanelTestConfiguration = _BrPanelTestConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 4, 2, 1),
    _BrPanelTestConfiguration_Type()
)
brPanelTestConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPanelTestConfiguration.setStatus("mandatory")


class _BrPanelTestFontList_Type(Integer32):
    """Custom type brPanelTestFontList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BrPanelTestFontList_Type.__name__ = "Integer32"
_BrPanelTestFontList_Object = MibScalar
brPanelTestFontList = _BrPanelTestFontList_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 4, 2, 2),
    _BrPanelTestFontList_Type()
)
brPanelTestFontList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPanelTestFontList.setStatus("mandatory")


class _BrPanelTestTestPage_Type(Integer32):
    """Custom type brPanelTestTestPage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BrPanelTestTestPage_Type.__name__ = "Integer32"
_BrPanelTestTestPage_Object = MibScalar
brPanelTestTestPage = _BrPanelTestTestPage_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 4, 2, 3),
    _BrPanelTestTestPage_Type()
)
brPanelTestTestPage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPanelTestTestPage.setStatus("mandatory")


class _BrPanelTestDemoPage_Type(Integer32):
    """Custom type brPanelTestDemoPage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BrPanelTestDemoPage_Type.__name__ = "Integer32"
_BrPanelTestDemoPage_Object = MibScalar
brPanelTestDemoPage = _BrPanelTestDemoPage_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 4, 2, 4),
    _BrPanelTestDemoPage_Type()
)
brPanelTestDemoPage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPanelTestDemoPage.setStatus("mandatory")
_Panellock_ObjectIdentity = ObjectIdentity
panellock = _Panellock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 4, 3)
)


class _BrPanelLockPasswd_Type(Integer32):
    """Custom type brPanelLockPasswd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BrPanelLockPasswd_Type.__name__ = "Integer32"
_BrPanelLockPasswd_Object = MibScalar
brPanelLockPasswd = _BrPanelLockPasswd_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 4, 3, 1),
    _BrPanelLockPasswd_Type()
)
brPanelLockPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPanelLockPasswd.setStatus("mandatory")


class _BrPanelLock_Type(Integer32):
    """Custom type brPanelLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_BrPanelLock_Type.__name__ = "Integer32"
_BrPanelLock_Object = MibScalar
brPanelLock = _BrPanelLock_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 4, 3, 2),
    _BrPanelLock_Type()
)
brPanelLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPanelLock.setStatus("mandatory")
_BrPanelLockOn_Type = OctetString
_BrPanelLockOn_Object = MibScalar
brPanelLockOn = _BrPanelLockOn_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 4, 3, 3),
    _BrPanelLockOn_Type()
)
brPanelLockOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPanelLockOn.setStatus("mandatory")
_BrPanelLockOff_Type = OctetString
_BrPanelLockOff_Object = MibScalar
brPanelLockOff = _BrPanelLockOff_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 4, 3, 4),
    _BrPanelLockOff_Type()
)
brPanelLockOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPanelLockOff.setStatus("mandatory")
_Key_ObjectIdentity = ObjectIdentity
key = _Key_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 4, 4)
)


class _BrPanelKeyOnline_Type(Integer32):
    """Custom type brPanelKeyOnline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrPanelKeyOnline_Type.__name__ = "Integer32"
_BrPanelKeyOnline_Object = MibScalar
brPanelKeyOnline = _BrPanelKeyOnline_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 4, 4, 1),
    _BrPanelKeyOnline_Type()
)
brPanelKeyOnline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPanelKeyOnline.setStatus("mandatory")


class _BrPanelKeyFormFeed_Type(Integer32):
    """Custom type brPanelKeyFormFeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrPanelKeyFormFeed_Type.__name__ = "Integer32"
_BrPanelKeyFormFeed_Object = MibScalar
brPanelKeyFormFeed = _BrPanelKeyFormFeed_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 4, 4, 2),
    _BrPanelKeyFormFeed_Type()
)
brPanelKeyFormFeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPanelKeyFormFeed.setStatus("mandatory")


class _BrPanelKeyContinue_Type(Integer32):
    """Custom type brPanelKeyContinue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrPanelKeyContinue_Type.__name__ = "Integer32"
_BrPanelKeyContinue_Object = MibScalar
brPanelKeyContinue = _BrPanelKeyContinue_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 4, 4, 3),
    _BrPanelKeyContinue_Type()
)
brPanelKeyContinue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPanelKeyContinue.setStatus("mandatory")


class _BrPanelKeyMode_Type(Integer32):
    """Custom type brPanelKeyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrPanelKeyMode_Type.__name__ = "Integer32"
_BrPanelKeyMode_Object = MibScalar
brPanelKeyMode = _BrPanelKeyMode_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 4, 4, 4),
    _BrPanelKeyMode_Type()
)
brPanelKeyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPanelKeyMode.setStatus("mandatory")


class _BrPanelKeyGo_Type(Integer32):
    """Custom type brPanelKeyGo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrPanelKeyGo_Type.__name__ = "Integer32"
_BrPanelKeyGo_Object = MibScalar
brPanelKeyGo = _BrPanelKeyGo_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 4, 4, 5),
    _BrPanelKeyGo_Type()
)
brPanelKeyGo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPanelKeyGo.setStatus("mandatory")


class _BrPanelKeyJobCancel_Type(Integer32):
    """Custom type brPanelKeyJobCancel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrPanelKeyJobCancel_Type.__name__ = "Integer32"
_BrPanelKeyJobCancel_Object = MibScalar
brPanelKeyJobCancel = _BrPanelKeyJobCancel_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 4, 4, 6),
    _BrPanelKeyJobCancel_Type()
)
brPanelKeyJobCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPanelKeyJobCancel.setStatus("mandatory")


class _BrPanelKeyReprint_Type(Integer32):
    """Custom type brPanelKeyReprint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrPanelKeyReprint_Type.__name__ = "Integer32"
_BrPanelKeyReprint_Object = MibScalar
brPanelKeyReprint = _BrPanelKeyReprint_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 4, 4, 7),
    _BrPanelKeyReprint_Type()
)
brPanelKeyReprint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPanelKeyReprint.setStatus("mandatory")


class _BrPanelKeySecure_Type(Integer32):
    """Custom type brPanelKeySecure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrPanelKeySecure_Type.__name__ = "Integer32"
_BrPanelKeySecure_Object = MibScalar
brPanelKeySecure = _BrPanelKeySecure_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 4, 4, 8),
    _BrPanelKeySecure_Type()
)
brPanelKeySecure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPanelKeySecure.setStatus("mandatory")
_Panelinfo_ObjectIdentity = ObjectIdentity
panelinfo = _Panelinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 4, 5)
)


class _BrLCDMode1_Type(Integer32):
    """Custom type brLCDMode1 based on Integer32"""
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
        *(("blink", 2),
          ("blinkScroll", 4),
          ("fix", 1),
          ("scroll", 3))
    )


_BrLCDMode1_Type.__name__ = "Integer32"
_BrLCDMode1_Object = MibScalar
brLCDMode1 = _BrLCDMode1_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 4, 5, 1),
    _BrLCDMode1_Type()
)
brLCDMode1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLCDMode1.setStatus("mandatory")
_BrLCDString1_Type = OctetString
_BrLCDString1_Object = MibScalar
brLCDString1 = _BrLCDString1_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 4, 5, 2),
    _BrLCDString1_Type()
)
brLCDString1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLCDString1.setStatus("mandatory")


class _BrLCDMode2_Type(Integer32):
    """Custom type brLCDMode2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blink", 2),
          ("fix", 1),
          ("scroll", 3))
    )


_BrLCDMode2_Type.__name__ = "Integer32"
_BrLCDMode2_Object = MibScalar
brLCDMode2 = _BrLCDMode2_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 4, 5, 3),
    _BrLCDMode2_Type()
)
brLCDMode2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLCDMode2.setStatus("mandatory")
_BrLCDString2_Type = OctetString
_BrLCDString2_Object = MibScalar
brLCDString2 = _BrLCDString2_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 4, 5, 4),
    _BrLCDString2_Type()
)
brLCDString2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLCDString2.setStatus("mandatory")
_BrLCDString16fix_Type = DisplayString
_BrLCDString16fix_Object = MibScalar
brLCDString16fix = _BrLCDString16fix_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 4, 5, 5),
    _BrLCDString16fix_Type()
)
brLCDString16fix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLCDString16fix.setStatus("mandatory")


class _BrBackLightColor_Type(Integer32):
    """Custom type brBackLightColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("notsupport", 255),
          ("orange", 2),
          ("red", 3))
    )


_BrBackLightColor_Type.__name__ = "Integer32"
_BrBackLightColor_Object = MibScalar
brBackLightColor = _BrBackLightColor_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 4, 5, 6),
    _BrBackLightColor_Type()
)
brBackLightColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brBackLightColor.setStatus("mandatory")


class _BrLCDMode3_Type(Integer32):
    """Custom type brLCDMode3 based on Integer32"""
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
        *(("blink", 2),
          ("blinkScroll", 4),
          ("fix", 1),
          ("scroll", 3))
    )


_BrLCDMode3_Type.__name__ = "Integer32"
_BrLCDMode3_Object = MibScalar
brLCDMode3 = _BrLCDMode3_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 4, 5, 7),
    _BrLCDMode3_Type()
)
brLCDMode3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLCDMode3.setStatus("mandatory")
_BrLCDString3_Type = OctetString
_BrLCDString3_Object = MibScalar
brLCDString3 = _BrLCDString3_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 4, 5, 8),
    _BrLCDString3_Type()
)
brLCDString3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLCDString3.setStatus("mandatory")


class _BrLCDMode4_Type(Integer32):
    """Custom type brLCDMode4 based on Integer32"""
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
        *(("blink", 2),
          ("blinkScroll", 4),
          ("fix", 1),
          ("scroll", 3))
    )


_BrLCDMode4_Type.__name__ = "Integer32"
_BrLCDMode4_Object = MibScalar
brLCDMode4 = _BrLCDMode4_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 4, 5, 9),
    _BrLCDMode4_Type()
)
brLCDMode4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLCDMode4.setStatus("mandatory")
_BrLCDString4_Type = OctetString
_BrLCDString4_Object = MibScalar
brLCDString4 = _BrLCDString4_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 4, 5, 10),
    _BrLCDString4_Type()
)
brLCDString4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLCDString4.setStatus("mandatory")


class _BrLCDMode5_Type(Integer32):
    """Custom type brLCDMode5 based on Integer32"""
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
        *(("blink", 2),
          ("blinkScroll", 4),
          ("fix", 1),
          ("scroll", 3))
    )


_BrLCDMode5_Type.__name__ = "Integer32"
_BrLCDMode5_Object = MibScalar
brLCDMode5 = _BrLCDMode5_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 4, 5, 11),
    _BrLCDMode5_Type()
)
brLCDMode5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLCDMode5.setStatus("mandatory")
_BrLCDString5_Type = OctetString
_BrLCDString5_Object = MibScalar
brLCDString5 = _BrLCDString5_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 4, 5, 12),
    _BrLCDString5_Type()
)
brLCDString5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLCDString5.setStatus("mandatory")
_BrLCDContrast_Type = Integer32
_BrLCDContrast_Object = MibScalar
brLCDContrast = _BrLCDContrast_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 4, 5, 13),
    _BrLCDContrast_Type()
)
brLCDContrast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLCDContrast.setStatus("mandatory")
_Printerinfomation_ObjectIdentity = ObjectIdentity
printerinfomation = _Printerinfomation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5)
)
_BrInfoSerialNumber_Type = OctetString
_BrInfoSerialNumber_Object = MibScalar
brInfoSerialNumber = _BrInfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 1),
    _BrInfoSerialNumber_Type()
)
brInfoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brInfoSerialNumber.setStatus("mandatory")


class _BrInfoType_Type(Integer32):
    """Custom type brInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrInfoType_Type.__name__ = "Integer32"
_BrInfoType_Object = MibScalar
brInfoType = _BrInfoType_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 2),
    _BrInfoType_Type()
)
brInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brInfoType.setStatus("mandatory")
_Version_ObjectIdentity = ObjectIdentity
version = _Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 3)
)


class _BrInfoUpperMIBVer_Type(Integer32):
    """Custom type brInfoUpperMIBVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrInfoUpperMIBVer_Type.__name__ = "Integer32"
_BrInfoUpperMIBVer_Object = MibScalar
brInfoUpperMIBVer = _BrInfoUpperMIBVer_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 3, 1),
    _BrInfoUpperMIBVer_Type()
)
brInfoUpperMIBVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brInfoUpperMIBVer.setStatus("mandatory")


class _BrInfoLowerMIBVer_Type(Integer32):
    """Custom type brInfoLowerMIBVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrInfoLowerMIBVer_Type.__name__ = "Integer32"
_BrInfoLowerMIBVer_Object = MibScalar
brInfoLowerMIBVer = _BrInfoLowerMIBVer_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 3, 2),
    _BrInfoLowerMIBVer_Type()
)
brInfoLowerMIBVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brInfoLowerMIBVer.setStatus("mandatory")


class _BrInfoStatus_Type(Integer32):
    """Custom type brInfoStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrInfoStatus_Type.__name__ = "Integer32"
_BrInfoStatus_Object = MibScalar
brInfoStatus = _BrInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 4),
    _BrInfoStatus_Type()
)
brInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brInfoStatus.setStatus("mandatory")


class _BrInfoNetVerUpStatus_Type(Integer32):
    """Custom type brInfoNetVerUpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrInfoNetVerUpStatus_Type.__name__ = "Integer32"
_BrInfoNetVerUpStatus_Object = MibScalar
brInfoNetVerUpStatus = _BrInfoNetVerUpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 5),
    _BrInfoNetVerUpStatus_Type()
)
brInfoNetVerUpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brInfoNetVerUpStatus.setStatus("mandatory")
_BrInfoPrinterUStatus_Type = Integer32
_BrInfoPrinterUStatus_Object = MibScalar
brInfoPrinterUStatus = _BrInfoPrinterUStatus_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 6),
    _BrInfoPrinterUStatus_Type()
)
brInfoPrinterUStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brInfoPrinterUStatus.setStatus("mandatory")
_BrInfoPConSupported_Type = Integer32
_BrInfoPConSupported_Object = MibScalar
brInfoPConSupported = _BrInfoPConSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 7),
    _BrInfoPConSupported_Type()
)
brInfoPConSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brInfoPConSupported.setStatus("mandatory")
_BrInfoMaintenance_Type = OctetString
_BrInfoMaintenance_Object = MibScalar
brInfoMaintenance = _BrInfoMaintenance_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 8),
    _BrInfoMaintenance_Type()
)
brInfoMaintenance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brInfoMaintenance.setStatus("mandatory")


class _BrInfoModelNumber_Type(Integer32):
    """Custom type brInfoModelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6,
              8,
              9,
              11,
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
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148)
        )
    )
    namedValues = NamedValues(
        *(("acfbCCD", 136),
          ("acfbCIS", 135),
          ("alLcdModel", 21),
          ("alLedModel", 20),
          ("alfb", 120),
          ("all", 19),
          ("all2", 25),
          ("allchn", 23),
          ("allfb", 116),
          ("allmfc", 115),
          ("am", 13),
          ("aml", 17),
          ("bh", 103),
          ("bh3fb", 113),
          ("bh3mfc", 114),
          ("bhfb", 104),
          ("bhhs", 106),
          ("bhl2fb", 109),
          ("bhl2mfc", 108),
          ("dcp540", 121),
          ("dcp585", 144),
          ("dcp6150", 129),
          ("dcp6260", 130),
          ("dcp6460", 131),
          ("dcp6690", 142),
          ("dcp6860", 132),
          ("dcp750", 122),
          ("dcp770", 133),
          ("hl2400ce", 4),
          ("hl2460", 8),
          ("hl2600cn", 9),
          ("hl3260", 6),
          ("hl3400CN", 5),
          ("hl3450cn", 11),
          ("hl4040", 22),
          ("hl4050hl4070", 24),
          ("jigen", 16),
          ("l4c", 18),
          ("mfc440", 123),
          ("mfc480", 134),
          ("mfc490", 145),
          ("mfc5460", 127),
          ("mfc5490", 139),
          ("mfc5860", 128),
          ("mfc5890", 140),
          ("mfc6490", 141),
          ("mfc665", 124),
          ("mfc6890", 143),
          ("mfc7440", 137),
          ("mfc7840", 138),
          ("mfc790", 146),
          ("mfc850", 125),
          ("mfc860", 126),
          ("mfc930", 148),
          ("mfc990", 147),
          ("mini2", 111),
          ("mini2adf", 112),
          ("mini2eColorLCD", 118),
          ("mini2eColorLCDADF", 119),
          ("slow4c", 117),
          ("zl", 102),
          ("zl2", 15),
          ("zl2fb", 107),
          ("zl2mfc", 110),
          ("zlfb", 101),
          ("zlhe", 14),
          ("zlhs", 105))
    )


_BrInfoModelNumber_Type.__name__ = "Integer32"
_BrInfoModelNumber_Object = MibScalar
brInfoModelNumber = _BrInfoModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 9),
    _BrInfoModelNumber_Type()
)
brInfoModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brInfoModelNumber.setStatus("mandatory")
_BrInfoCounter_Type = OctetString
_BrInfoCounter_Object = MibScalar
brInfoCounter = _BrInfoCounter_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 10),
    _BrInfoCounter_Type()
)
brInfoCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brInfoCounter.setStatus("mandatory")
_BrInfoNextCare_Type = OctetString
_BrInfoNextCare_Object = MibScalar
brInfoNextCare = _BrInfoNextCare_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 11),
    _BrInfoNextCare_Type()
)
brInfoNextCare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brInfoNextCare.setStatus("mandatory")


class _BrInfoHDDSlot1_Type(Integer32):
    """Custom type brInfoHDDSlot1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_BrInfoHDDSlot1_Type.__name__ = "Integer32"
_BrInfoHDDSlot1_Object = MibScalar
brInfoHDDSlot1 = _BrInfoHDDSlot1_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 12),
    _BrInfoHDDSlot1_Type()
)
brInfoHDDSlot1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brInfoHDDSlot1.setStatus("mandatory")


class _BrInfoHDDSlot2_Type(Integer32):
    """Custom type brInfoHDDSlot2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_BrInfoHDDSlot2_Type.__name__ = "Integer32"
_BrInfoHDDSlot2_Object = MibScalar
brInfoHDDSlot2 = _BrInfoHDDSlot2_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 13),
    _BrInfoHDDSlot2_Type()
)
brInfoHDDSlot2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brInfoHDDSlot2.setStatus("mandatory")


class _BrInfoHDDInternal_Type(Integer32):
    """Custom type brInfoHDDInternal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_BrInfoHDDInternal_Type.__name__ = "Integer32"
_BrInfoHDDInternal_Object = MibScalar
brInfoHDDInternal = _BrInfoHDDInternal_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 14),
    _BrInfoHDDInternal_Type()
)
brInfoHDDInternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brInfoHDDInternal.setStatus("mandatory")
_BrInfoHDDSize_Type = OctetString
_BrInfoHDDSize_Object = MibScalar
brInfoHDDSize = _BrInfoHDDSize_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 15),
    _BrInfoHDDSize_Type()
)
brInfoHDDSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brInfoHDDSize.setStatus("mandatory")
_BrInfoSolutionsCenterURL_Type = DisplayString
_BrInfoSolutionsCenterURL_Object = MibScalar
brInfoSolutionsCenterURL = _BrInfoSolutionsCenterURL_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 16),
    _BrInfoSolutionsCenterURL_Type()
)
brInfoSolutionsCenterURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brInfoSolutionsCenterURL.setStatus("mandatory")
_BrInfoDeviceRomVersion_Type = DisplayString
_BrInfoDeviceRomVersion_Object = MibScalar
brInfoDeviceRomVersion = _BrInfoDeviceRomVersion_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 17),
    _BrInfoDeviceRomVersion_Type()
)
brInfoDeviceRomVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brInfoDeviceRomVersion.setStatus("mandatory")
_BrInfoCoverage_Type = OctetString
_BrInfoCoverage_Object = MibScalar
brInfoCoverage = _BrInfoCoverage_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 18),
    _BrInfoCoverage_Type()
)
brInfoCoverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brInfoCoverage.setStatus("mandatory")
_BrInfoEstimatedPagesRemaining_Type = Counter32
_BrInfoEstimatedPagesRemaining_Object = MibScalar
brInfoEstimatedPagesRemaining = _BrInfoEstimatedPagesRemaining_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 19),
    _BrInfoEstimatedPagesRemaining_Type()
)
brInfoEstimatedPagesRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brInfoEstimatedPagesRemaining.setStatus("mandatory")
_BrInfoReplaceCount_Type = OctetString
_BrInfoReplaceCount_Object = MibScalar
brInfoReplaceCount = _BrInfoReplaceCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 20),
    _BrInfoReplaceCount_Type()
)
brInfoReplaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brInfoReplaceCount.setStatus("mandatory")
_BrInfoJamCount_Type = OctetString
_BrInfoJamCount_Object = MibScalar
brInfoJamCount = _BrInfoJamCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 21),
    _BrInfoJamCount_Type()
)
brInfoJamCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brInfoJamCount.setStatus("mandatory")
_BrInfoJamCountClear_Type = Integer32
_BrInfoJamCountClear_Object = MibScalar
brInfoJamCountClear = _BrInfoJamCountClear_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 22),
    _BrInfoJamCountClear_Type()
)
brInfoJamCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brInfoJamCountClear.setStatus("mandatory")
_BrInfoReplaceTime_Type = OctetString
_BrInfoReplaceTime_Object = MibScalar
brInfoReplaceTime = _BrInfoReplaceTime_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 23),
    _BrInfoReplaceTime_Type()
)
brInfoReplaceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brInfoReplaceTime.setStatus("mandatory")
_BrInfoDeviceSubRomVersion_Type = OctetString
_BrInfoDeviceSubRomVersion_Object = MibScalar
brInfoDeviceSubRomVersion = _BrInfoDeviceSubRomVersion_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 24),
    _BrInfoDeviceSubRomVersion_Type()
)
brInfoDeviceSubRomVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brInfoDeviceSubRomVersion.setStatus("mandatory")
_BrInfoAlertVersion_Type = Integer32
_BrInfoAlertVersion_Object = MibScalar
brInfoAlertVersion = _BrInfoAlertVersion_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 25),
    _BrInfoAlertVersion_Type()
)
brInfoAlertVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brInfoAlertVersion.setStatus("mandatory")


class _BrInfoBlackPrint_Type(Integer32):
    """Custom type brInfoBlackPrint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrInfoBlackPrint_Type.__name__ = "Integer32"
_BrInfoBlackPrint_Object = MibScalar
brInfoBlackPrint = _BrInfoBlackPrint_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 26),
    _BrInfoBlackPrint_Type()
)
brInfoBlackPrint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brInfoBlackPrint.setStatus("mandatory")
_ErrorHistory_ObjectIdentity = ObjectIdentity
errorHistory = _ErrorHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 51)
)
_BrErrorHistoryCount_Type = Integer32
_BrErrorHistoryCount_Object = MibScalar
brErrorHistoryCount = _BrErrorHistoryCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 51, 1),
    _BrErrorHistoryCount_Type()
)
brErrorHistoryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brErrorHistoryCount.setStatus("mandatory")
_BrErrorHistoryTable_Object = MibTable
brErrorHistoryTable = _BrErrorHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 51, 2)
)
if mibBuilder.loadTexts:
    brErrorHistoryTable.setStatus("mandatory")
_BrErrorHistoryEntry_Object = MibTableRow
brErrorHistoryEntry = _BrErrorHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 51, 2, 1)
)
brErrorHistoryEntry.setIndexNames(
    (0, "BROTHER-MIB", "brErrorHistoryIndex"),
)
if mibBuilder.loadTexts:
    brErrorHistoryEntry.setStatus("mandatory")


class _BrErrorHistoryIndex_Type(Integer32):
    """Custom type brErrorHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BrErrorHistoryIndex_Type.__name__ = "Integer32"
_BrErrorHistoryIndex_Object = MibTableColumn
brErrorHistoryIndex = _BrErrorHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 51, 2, 1, 1),
    _BrErrorHistoryIndex_Type()
)
brErrorHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brErrorHistoryIndex.setStatus("mandatory")
_BrErrorHistoryDescription_Type = OctetString
_BrErrorHistoryDescription_Object = MibTableColumn
brErrorHistoryDescription = _BrErrorHistoryDescription_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 51, 2, 1, 2),
    _BrErrorHistoryDescription_Type()
)
brErrorHistoryDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brErrorHistoryDescription.setStatus("mandatory")
_BrErrorHistoryAllClear_Type = Integer32
_BrErrorHistoryAllClear_Object = MibScalar
brErrorHistoryAllClear = _BrErrorHistoryAllClear_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 51, 3),
    _BrErrorHistoryAllClear_Type()
)
brErrorHistoryAllClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brErrorHistoryAllClear.setStatus("mandatory")
_BrCommunicationErrorHistoryCount_Type = Integer32
_BrCommunicationErrorHistoryCount_Object = MibScalar
brCommunicationErrorHistoryCount = _BrCommunicationErrorHistoryCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 51, 11),
    _BrCommunicationErrorHistoryCount_Type()
)
brCommunicationErrorHistoryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brCommunicationErrorHistoryCount.setStatus("mandatory")
_BrCommunicationErrorHistoryTable_Object = MibTable
brCommunicationErrorHistoryTable = _BrCommunicationErrorHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 51, 12)
)
if mibBuilder.loadTexts:
    brCommunicationErrorHistoryTable.setStatus("mandatory")
_BrCommunicationErrorHistoryEntry_Object = MibTableRow
brCommunicationErrorHistoryEntry = _BrCommunicationErrorHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 51, 12, 1)
)
brCommunicationErrorHistoryEntry.setIndexNames(
    (0, "BROTHER-MIB", "brCommunicationErrorHistoryIndex"),
)
if mibBuilder.loadTexts:
    brCommunicationErrorHistoryEntry.setStatus("mandatory")


class _BrCommunicationErrorHistoryIndex_Type(Integer32):
    """Custom type brCommunicationErrorHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BrCommunicationErrorHistoryIndex_Type.__name__ = "Integer32"
_BrCommunicationErrorHistoryIndex_Object = MibTableColumn
brCommunicationErrorHistoryIndex = _BrCommunicationErrorHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 51, 12, 1, 1),
    _BrCommunicationErrorHistoryIndex_Type()
)
brCommunicationErrorHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brCommunicationErrorHistoryIndex.setStatus("mandatory")
_BrCommunicationErrorHistoryDescription_Type = OctetString
_BrCommunicationErrorHistoryDescription_Object = MibTableColumn
brCommunicationErrorHistoryDescription = _BrCommunicationErrorHistoryDescription_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 51, 12, 1, 2),
    _BrCommunicationErrorHistoryDescription_Type()
)
brCommunicationErrorHistoryDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brCommunicationErrorHistoryDescription.setStatus("mandatory")
_PrintPages_ObjectIdentity = ObjectIdentity
printPages = _PrintPages_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 52)
)
_BrPrintPagesTable_Object = MibTable
brPrintPagesTable = _BrPrintPagesTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 52, 1)
)
if mibBuilder.loadTexts:
    brPrintPagesTable.setStatus("mandatory")
_BrPrintPagesEntry_Object = MibTableRow
brPrintPagesEntry = _BrPrintPagesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 52, 1, 1)
)
brPrintPagesEntry.setIndexNames(
    (0, "BROTHER-MIB", "brPrintPagesIndex"),
)
if mibBuilder.loadTexts:
    brPrintPagesEntry.setStatus("mandatory")


class _BrPrintPagesIndex_Type(Integer32):
    """Custom type brPrintPagesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BrPrintPagesIndex_Type.__name__ = "Integer32"
_BrPrintPagesIndex_Object = MibTableColumn
brPrintPagesIndex = _BrPrintPagesIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 52, 1, 1, 1),
    _BrPrintPagesIndex_Type()
)
brPrintPagesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPrintPagesIndex.setStatus("mandatory")


class _BrPrintPagesPaperSize_Type(Integer32):
    """Custom type brPrintPagesPaperSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              24,
              25,
              26,
              27,
              45,
              46,
              80,
              81,
              90,
              91,
              99,
              100,
              890,
              891,
              892,
              893,
              894,
              895,
              896,
              897,
              898,
              899,
              900,
              901,
              902,
              903,
              904,
              905,
              906,
              907,
              908,
              909,
              910,
              911,
              920,
              921,
              922,
              924,
              999)
        )
    )
    namedValues = NamedValues(
        *(("a3ISO", 27),
          ("a3PLUS", 891),
          ("a4", 26),
          ("a4LONG", 894),
          ("a4Letter", 898),
          ("a4ShortEdge", 893),
          ("a5", 25),
          ("a6", 24),
          ("b4JIS", 46),
          ("b5", 100),
          ("b5Executive", 899),
          ("b5ISOShortEdge", 896),
          ("b5JIS", 45),
          ("b6", 99),
          ("b6A5A6", 910),
          ("b6JIS", 924),
          ("c5", 91),
          ("com10", 81),
          ("custom", 897),
          ("detectsensor", 911),
          ("dl", 90),
          ("dll", 901),
          ("envelopes", 900),
          ("envelopesY4", 921),
          ("executive", 1),
          ("executiveShortEdge", 895),
          ("folio", 903),
          ("hagaki", 902),
          ("inches3x5", 920),
          ("largestEnvelopesTheWest", 922),
          ("ledger", 890),
          ("legal", 3),
          ("legalA4Long", 909),
          ("letter", 2),
          ("letterShortEdge", 892),
          ("monarch", 80),
          ("organaizerJ", 904),
          ("organaizerK", 905),
          ("organaizerL", 906),
          ("organaizerM", 907),
          ("otherPage", 999),
          ("userdefined", 908))
    )


_BrPrintPagesPaperSize_Type.__name__ = "Integer32"
_BrPrintPagesPaperSize_Object = MibTableColumn
brPrintPagesPaperSize = _BrPrintPagesPaperSize_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 52, 1, 1, 2),
    _BrPrintPagesPaperSize_Type()
)
brPrintPagesPaperSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPrintPagesPaperSize.setStatus("mandatory")
_BrPrintPages_Type = Counter32
_BrPrintPages_Object = MibTableColumn
brPrintPages = _BrPrintPages_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 52, 1, 1, 3),
    _BrPrintPages_Type()
)
brPrintPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPrintPages.setStatus("mandatory")
_BrPrintPagesMediaPlaceTable_Object = MibTable
brPrintPagesMediaPlaceTable = _BrPrintPagesMediaPlaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 52, 11)
)
if mibBuilder.loadTexts:
    brPrintPagesMediaPlaceTable.setStatus("mandatory")
_BrPrintPagesMediaPlaceEntry_Object = MibTableRow
brPrintPagesMediaPlaceEntry = _BrPrintPagesMediaPlaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 52, 11, 1)
)
brPrintPagesMediaPlaceEntry.setIndexNames(
    (0, "BROTHER-MIB", "brPrintPagesMediaPlaceIndex"),
)
if mibBuilder.loadTexts:
    brPrintPagesMediaPlaceEntry.setStatus("mandatory")


class _BrPrintPagesMediaPlaceIndex_Type(Integer32):
    """Custom type brPrintPagesMediaPlaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BrPrintPagesMediaPlaceIndex_Type.__name__ = "Integer32"
_BrPrintPagesMediaPlaceIndex_Object = MibTableColumn
brPrintPagesMediaPlaceIndex = _BrPrintPagesMediaPlaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 52, 11, 1, 1),
    _BrPrintPagesMediaPlaceIndex_Type()
)
brPrintPagesMediaPlaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPrintPagesMediaPlaceIndex.setStatus("mandatory")


class _BrPrintPagesMediaPlaceType_Type(Integer32):
    """Custom type brPrintPagesMediaPlaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("back", 2),
          ("face", 1))
    )


_BrPrintPagesMediaPlaceType_Type.__name__ = "Integer32"
_BrPrintPagesMediaPlaceType_Object = MibTableColumn
brPrintPagesMediaPlaceType = _BrPrintPagesMediaPlaceType_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 52, 11, 1, 2),
    _BrPrintPagesMediaPlaceType_Type()
)
brPrintPagesMediaPlaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPrintPagesMediaPlaceType.setStatus("mandatory")
_BrPrintPagesMediaPlaceCounter_Type = Counter32
_BrPrintPagesMediaPlaceCounter_Object = MibTableColumn
brPrintPagesMediaPlaceCounter = _BrPrintPagesMediaPlaceCounter_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 52, 11, 1, 3),
    _BrPrintPagesMediaPlaceCounter_Type()
)
brPrintPagesMediaPlaceCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPrintPagesMediaPlaceCounter.setStatus("mandatory")
_BrPrintPagesFuncTable_Object = MibTable
brPrintPagesFuncTable = _BrPrintPagesFuncTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 52, 21)
)
if mibBuilder.loadTexts:
    brPrintPagesFuncTable.setStatus("mandatory")
_BrPrintPagesFuncEntry_Object = MibTableRow
brPrintPagesFuncEntry = _BrPrintPagesFuncEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 52, 21, 1)
)
brPrintPagesFuncEntry.setIndexNames(
    (0, "BROTHER-MIB", "brPrintPagesFuncIndex"),
)
if mibBuilder.loadTexts:
    brPrintPagesFuncEntry.setStatus("mandatory")


class _BrPrintPagesFuncIndex_Type(Integer32):
    """Custom type brPrintPagesFuncIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BrPrintPagesFuncIndex_Type.__name__ = "Integer32"
_BrPrintPagesFuncIndex_Object = MibTableColumn
brPrintPagesFuncIndex = _BrPrintPagesFuncIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 52, 21, 1, 1),
    _BrPrintPagesFuncIndex_Type()
)
brPrintPagesFuncIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPrintPagesFuncIndex.setStatus("mandatory")


class _BrPrintPagesFuncType_Type(Integer32):
    """Custom type brPrintPagesFuncType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("copycolor", 4),
          ("copymono", 9),
          ("copytotal", 3),
          ("faxcolor", 6),
          ("faxmono", 8),
          ("faxtotal", 2),
          ("pcPrintcolor", 5),
          ("pcPrintmono", 7),
          ("pcPrinttotal", 1))
    )


_BrPrintPagesFuncType_Type.__name__ = "Integer32"
_BrPrintPagesFuncType_Object = MibTableColumn
brPrintPagesFuncType = _BrPrintPagesFuncType_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 52, 21, 1, 2),
    _BrPrintPagesFuncType_Type()
)
brPrintPagesFuncType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPrintPagesFuncType.setStatus("mandatory")
_BrPrintPagesFuncCounter_Type = Counter32
_BrPrintPagesFuncCounter_Object = MibTableColumn
brPrintPagesFuncCounter = _BrPrintPagesFuncCounter_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 52, 21, 1, 3),
    _BrPrintPagesFuncCounter_Type()
)
brPrintPagesFuncCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPrintPagesFuncCounter.setStatus("mandatory")
_BrPrintPagesPaperTypeTable_Object = MibTable
brPrintPagesPaperTypeTable = _BrPrintPagesPaperTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 52, 31)
)
if mibBuilder.loadTexts:
    brPrintPagesPaperTypeTable.setStatus("mandatory")
_BrPrintPagesPaperTypeEntry_Object = MibTableRow
brPrintPagesPaperTypeEntry = _BrPrintPagesPaperTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 52, 31, 1)
)
brPrintPagesPaperTypeEntry.setIndexNames(
    (0, "BROTHER-MIB", "brPrintPagesPaperTypeIndex"),
)
if mibBuilder.loadTexts:
    brPrintPagesPaperTypeEntry.setStatus("mandatory")


class _BrPrintPagesPaperTypeIndex_Type(Integer32):
    """Custom type brPrintPagesPaperTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_BrPrintPagesPaperTypeIndex_Type.__name__ = "Integer32"
_BrPrintPagesPaperTypeIndex_Object = MibTableColumn
brPrintPagesPaperTypeIndex = _BrPrintPagesPaperTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 52, 31, 1, 1),
    _BrPrintPagesPaperTypeIndex_Type()
)
brPrintPagesPaperTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPrintPagesPaperTypeIndex.setStatus("mandatory")


class _BrPrintPagesPaperTypeType_Type(Integer32):
    """Custom type brPrintPagesPaperTypeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("envelopesenvthickenvthin", 14),
          ("regularthinrecycled", 12),
          ("thickthickerbond", 13),
          ("transparency", 3))
    )


_BrPrintPagesPaperTypeType_Type.__name__ = "Integer32"
_BrPrintPagesPaperTypeType_Object = MibTableColumn
brPrintPagesPaperTypeType = _BrPrintPagesPaperTypeType_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 52, 31, 1, 2),
    _BrPrintPagesPaperTypeType_Type()
)
brPrintPagesPaperTypeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPrintPagesPaperTypeType.setStatus("mandatory")
_BrPrintPagesPaperTypeCounter_Type = Counter32
_BrPrintPagesPaperTypeCounter_Object = MibTableColumn
brPrintPagesPaperTypeCounter = _BrPrintPagesPaperTypeCounter_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 52, 31, 1, 3),
    _BrPrintPagesPaperTypeCounter_Type()
)
brPrintPagesPaperTypeCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPrintPagesPaperTypeCounter.setStatus("mandatory")
_Capability_ObjectIdentity = ObjectIdentity
capability = _Capability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 53)
)
_Copies_ObjectIdentity = ObjectIdentity
copies = _Copies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 53, 1)
)
_BrCapabilityCopiesMax_Type = Integer32
_BrCapabilityCopiesMax_Object = MibScalar
brCapabilityCopiesMax = _BrCapabilityCopiesMax_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 53, 1, 1),
    _BrCapabilityCopiesMax_Type()
)
brCapabilityCopiesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brCapabilityCopiesMax.setStatus("mandatory")
_BrCapabilityCopiesMin_Type = Integer32
_BrCapabilityCopiesMin_Object = MibScalar
brCapabilityCopiesMin = _BrCapabilityCopiesMin_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 53, 1, 2),
    _BrCapabilityCopiesMin_Type()
)
brCapabilityCopiesMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brCapabilityCopiesMin.setStatus("mandatory")
_Orientation_ObjectIdentity = ObjectIdentity
orientation = _Orientation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 53, 2)
)
_BrCapabilityOrientationCount_Type = Integer32
_BrCapabilityOrientationCount_Object = MibScalar
brCapabilityOrientationCount = _BrCapabilityOrientationCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 53, 2, 1),
    _BrCapabilityOrientationCount_Type()
)
brCapabilityOrientationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brCapabilityOrientationCount.setStatus("mandatory")
_BrCapabilityOrientationTable_Object = MibTable
brCapabilityOrientationTable = _BrCapabilityOrientationTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 53, 2, 2)
)
if mibBuilder.loadTexts:
    brCapabilityOrientationTable.setStatus("mandatory")
_BrCapabilityOrientationEntry_Object = MibTableRow
brCapabilityOrientationEntry = _BrCapabilityOrientationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 53, 2, 2, 1)
)
brCapabilityOrientationEntry.setIndexNames(
    (0, "BROTHER-MIB", "brCapabilityOrientationIndex"),
)
if mibBuilder.loadTexts:
    brCapabilityOrientationEntry.setStatus("mandatory")


class _BrCapabilityOrientationIndex_Type(Integer32):
    """Custom type brCapabilityOrientationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BrCapabilityOrientationIndex_Type.__name__ = "Integer32"
_BrCapabilityOrientationIndex_Object = MibTableColumn
brCapabilityOrientationIndex = _BrCapabilityOrientationIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 53, 2, 2, 1, 1),
    _BrCapabilityOrientationIndex_Type()
)
brCapabilityOrientationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brCapabilityOrientationIndex.setStatus("mandatory")
_BrCapabilityOrientationName_Type = DisplayString
_BrCapabilityOrientationName_Object = MibTableColumn
brCapabilityOrientationName = _BrCapabilityOrientationName_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 53, 2, 2, 1, 2),
    _BrCapabilityOrientationName_Type()
)
brCapabilityOrientationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brCapabilityOrientationName.setStatus("mandatory")
_Paper_ObjectIdentity = ObjectIdentity
paper = _Paper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 53, 3)
)
_BrCapabilityPaperCount_Type = Integer32
_BrCapabilityPaperCount_Object = MibScalar
brCapabilityPaperCount = _BrCapabilityPaperCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 53, 3, 1),
    _BrCapabilityPaperCount_Type()
)
brCapabilityPaperCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brCapabilityPaperCount.setStatus("mandatory")
_BrCapabilityPaperTable_Object = MibTable
brCapabilityPaperTable = _BrCapabilityPaperTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 53, 3, 2)
)
if mibBuilder.loadTexts:
    brCapabilityPaperTable.setStatus("mandatory")
_BrCapabilityPaperEntry_Object = MibTableRow
brCapabilityPaperEntry = _BrCapabilityPaperEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 53, 3, 2, 1)
)
brCapabilityPaperEntry.setIndexNames(
    (0, "BROTHER-MIB", "brCapabilityPaperIndex"),
)
if mibBuilder.loadTexts:
    brCapabilityPaperEntry.setStatus("mandatory")


class _BrCapabilityPaperIndex_Type(Integer32):
    """Custom type brCapabilityPaperIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BrCapabilityPaperIndex_Type.__name__ = "Integer32"
_BrCapabilityPaperIndex_Object = MibTableColumn
brCapabilityPaperIndex = _BrCapabilityPaperIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 53, 3, 2, 1, 1),
    _BrCapabilityPaperIndex_Type()
)
brCapabilityPaperIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brCapabilityPaperIndex.setStatus("mandatory")
_BrCapabilityPaperName_Type = DisplayString
_BrCapabilityPaperName_Object = MibTableColumn
brCapabilityPaperName = _BrCapabilityPaperName_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 53, 3, 2, 1, 2),
    _BrCapabilityPaperName_Type()
)
brCapabilityPaperName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brCapabilityPaperName.setStatus("mandatory")
_Mediatype_ObjectIdentity = ObjectIdentity
mediatype = _Mediatype_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 53, 4)
)
_BrCapabilityMediatypeCount_Type = Integer32
_BrCapabilityMediatypeCount_Object = MibScalar
brCapabilityMediatypeCount = _BrCapabilityMediatypeCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 53, 4, 1),
    _BrCapabilityMediatypeCount_Type()
)
brCapabilityMediatypeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brCapabilityMediatypeCount.setStatus("mandatory")
_BrCapabilityMediatypeTable_Object = MibTable
brCapabilityMediatypeTable = _BrCapabilityMediatypeTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 53, 4, 2)
)
if mibBuilder.loadTexts:
    brCapabilityMediatypeTable.setStatus("mandatory")
_BrCapabilityMediatypeEntry_Object = MibTableRow
brCapabilityMediatypeEntry = _BrCapabilityMediatypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 53, 4, 2, 1)
)
brCapabilityMediatypeEntry.setIndexNames(
    (0, "BROTHER-MIB", "brCapabilityMediatypeIndex"),
)
if mibBuilder.loadTexts:
    brCapabilityMediatypeEntry.setStatus("mandatory")


class _BrCapabilityMediatypeIndex_Type(Integer32):
    """Custom type brCapabilityMediatypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BrCapabilityMediatypeIndex_Type.__name__ = "Integer32"
_BrCapabilityMediatypeIndex_Object = MibTableColumn
brCapabilityMediatypeIndex = _BrCapabilityMediatypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 53, 4, 2, 1, 1),
    _BrCapabilityMediatypeIndex_Type()
)
brCapabilityMediatypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brCapabilityMediatypeIndex.setStatus("mandatory")
_BrCapabilityMediatypeName_Type = DisplayString
_BrCapabilityMediatypeName_Object = MibTableColumn
brCapabilityMediatypeName = _BrCapabilityMediatypeName_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 53, 4, 2, 1, 2),
    _BrCapabilityMediatypeName_Type()
)
brCapabilityMediatypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brCapabilityMediatypeName.setStatus("mandatory")
_Resolution_ObjectIdentity = ObjectIdentity
resolution = _Resolution_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 53, 5)
)
_BrCapabilityResolutionCount_Type = Integer32
_BrCapabilityResolutionCount_Object = MibScalar
brCapabilityResolutionCount = _BrCapabilityResolutionCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 53, 5, 1),
    _BrCapabilityResolutionCount_Type()
)
brCapabilityResolutionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brCapabilityResolutionCount.setStatus("mandatory")
_BrCapabilityResolutionTable_Object = MibTable
brCapabilityResolutionTable = _BrCapabilityResolutionTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 53, 5, 2)
)
if mibBuilder.loadTexts:
    brCapabilityResolutionTable.setStatus("mandatory")
_BrCapabilityResolutionEntry_Object = MibTableRow
brCapabilityResolutionEntry = _BrCapabilityResolutionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 53, 5, 2, 1)
)
brCapabilityResolutionEntry.setIndexNames(
    (0, "BROTHER-MIB", "brCapabilityResolutionIndex"),
)
if mibBuilder.loadTexts:
    brCapabilityResolutionEntry.setStatus("mandatory")


class _BrCapabilityResolutionIndex_Type(Integer32):
    """Custom type brCapabilityResolutionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BrCapabilityResolutionIndex_Type.__name__ = "Integer32"
_BrCapabilityResolutionIndex_Object = MibTableColumn
brCapabilityResolutionIndex = _BrCapabilityResolutionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 53, 5, 2, 1, 1),
    _BrCapabilityResolutionIndex_Type()
)
brCapabilityResolutionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brCapabilityResolutionIndex.setStatus("mandatory")
_BrCapabilityResolution_Type = Integer32
_BrCapabilityResolution_Object = MibTableColumn
brCapabilityResolution = _BrCapabilityResolution_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 53, 5, 2, 1, 2),
    _BrCapabilityResolution_Type()
)
brCapabilityResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brCapabilityResolution.setStatus("mandatory")
_Countinfo_ObjectIdentity = ObjectIdentity
countinfo = _Countinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 54)
)
_Pfkit_ObjectIdentity = ObjectIdentity
pfkit = _Pfkit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 54, 1)
)
_BrPfKitIndexCount_Type = Integer32
_BrPfKitIndexCount_Object = MibScalar
brPfKitIndexCount = _BrPfKitIndexCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 54, 1, 1),
    _BrPfKitIndexCount_Type()
)
brPfKitIndexCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPfKitIndexCount.setStatus("mandatory")
_BrPfKitTable_Object = MibTable
brPfKitTable = _BrPfKitTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 54, 1, 2)
)
if mibBuilder.loadTexts:
    brPfKitTable.setStatus("mandatory")
_BrPfKitEntry_Object = MibTableRow
brPfKitEntry = _BrPfKitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 54, 1, 2, 1)
)
brPfKitEntry.setIndexNames(
    (0, "BROTHER-MIB", "brPfKitIndex"),
)
if mibBuilder.loadTexts:
    brPfKitEntry.setStatus("mandatory")


class _BrPfKitIndex_Type(Integer32):
    """Custom type brPfKitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BrPfKitIndex_Type.__name__ = "Integer32"
_BrPfKitIndex_Object = MibTableColumn
brPfKitIndex = _BrPfKitIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 54, 1, 2, 1, 1),
    _BrPfKitIndex_Type()
)
brPfKitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPfKitIndex.setStatus("mandatory")


class _BrPfKitType_Type(Integer32):
    """Custom type brPfKitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              10,
              20)
        )
    )
    namedValues = NamedValues(
        *(("pfkit1", 1),
          ("pfkit2", 2),
          ("pfkit3", 3),
          ("pfkit4", 4),
          ("pfkitdx", 20),
          ("pfkitmp", 10))
    )


_BrPfKitType_Type.__name__ = "Integer32"
_BrPfKitType_Object = MibTableColumn
brPfKitType = _BrPfKitType_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 54, 1, 2, 1, 2),
    _BrPfKitType_Type()
)
brPfKitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPfKitType.setStatus("mandatory")
_BrPfKitCount_Type = Counter32
_BrPfKitCount_Object = MibTableColumn
brPfKitCount = _BrPfKitCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 54, 1, 2, 1, 3),
    _BrPfKitCount_Type()
)
brPfKitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPfKitCount.setStatus("mandatory")
_Scancount_ObjectIdentity = ObjectIdentity
scancount = _Scancount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 54, 2)
)
_BrScanCountIndexCount_Type = Integer32
_BrScanCountIndexCount_Object = MibScalar
brScanCountIndexCount = _BrScanCountIndexCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 54, 2, 1),
    _BrScanCountIndexCount_Type()
)
brScanCountIndexCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brScanCountIndexCount.setStatus("mandatory")
_BrScanCountTable_Object = MibTable
brScanCountTable = _BrScanCountTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 54, 2, 2)
)
if mibBuilder.loadTexts:
    brScanCountTable.setStatus("mandatory")
_BrScanCountEntry_Object = MibTableRow
brScanCountEntry = _BrScanCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 54, 2, 2, 1)
)
brScanCountEntry.setIndexNames(
    (0, "BROTHER-MIB", "brScanCountIndex"),
)
if mibBuilder.loadTexts:
    brScanCountEntry.setStatus("mandatory")


class _BrScanCountIndex_Type(Integer32):
    """Custom type brScanCountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BrScanCountIndex_Type.__name__ = "Integer32"
_BrScanCountIndex_Object = MibTableColumn
brScanCountIndex = _BrScanCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 54, 2, 2, 1, 1),
    _BrScanCountIndex_Type()
)
brScanCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brScanCountIndex.setStatus("mandatory")


class _BrScanCountType_Type(Integer32):
    """Custom type brScanCountType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adf", 1),
          ("adfdx", 3),
          ("fb", 2))
    )


_BrScanCountType_Type.__name__ = "Integer32"
_BrScanCountType_Object = MibTableColumn
brScanCountType = _BrScanCountType_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 54, 2, 2, 1, 2),
    _BrScanCountType_Type()
)
brScanCountType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brScanCountType.setStatus("mandatory")
_BrScanCountCounter_Type = Counter32
_BrScanCountCounter_Object = MibTableColumn
brScanCountCounter = _BrScanCountCounter_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 54, 2, 2, 1, 3),
    _BrScanCountCounter_Type()
)
brScanCountCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brScanCountCounter.setStatus("mandatory")
_Firmwareupdatekeyword_ObjectIdentity = ObjectIdentity
firmwareupdatekeyword = _Firmwareupdatekeyword_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 55)
)


class _BrFirmwareUpdateKeywordCount_Type(Integer32):
    """Custom type brFirmwareUpdateKeywordCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BrFirmwareUpdateKeywordCount_Type.__name__ = "Integer32"
_BrFirmwareUpdateKeywordCount_Object = MibScalar
brFirmwareUpdateKeywordCount = _BrFirmwareUpdateKeywordCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 55, 1),
    _BrFirmwareUpdateKeywordCount_Type()
)
brFirmwareUpdateKeywordCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFirmwareUpdateKeywordCount.setStatus("mandatory")
_BrFirmwareUpdateKeywordTable_Object = MibTable
brFirmwareUpdateKeywordTable = _BrFirmwareUpdateKeywordTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 55, 2)
)
if mibBuilder.loadTexts:
    brFirmwareUpdateKeywordTable.setStatus("mandatory")
_BrFirmwareUpdateKeywordEntry_Object = MibTableRow
brFirmwareUpdateKeywordEntry = _BrFirmwareUpdateKeywordEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 55, 2, 1)
)
brFirmwareUpdateKeywordEntry.setIndexNames(
    (0, "BROTHER-MIB", "brFirmwareUpdateKeywordIndex"),
)
if mibBuilder.loadTexts:
    brFirmwareUpdateKeywordEntry.setStatus("mandatory")


class _BrFirmwareUpdateKeywordIndex_Type(Integer32):
    """Custom type brFirmwareUpdateKeywordIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_BrFirmwareUpdateKeywordIndex_Type.__name__ = "Integer32"
_BrFirmwareUpdateKeywordIndex_Object = MibTableColumn
brFirmwareUpdateKeywordIndex = _BrFirmwareUpdateKeywordIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 55, 2, 1, 1),
    _BrFirmwareUpdateKeywordIndex_Type()
)
brFirmwareUpdateKeywordIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFirmwareUpdateKeywordIndex.setStatus("mandatory")


class _BrFirmwareUpdateKeyword_Type(OctetString):
    """Custom type brFirmwareUpdateKeyword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BrFirmwareUpdateKeyword_Type.__name__ = "OctetString"
_BrFirmwareUpdateKeyword_Object = MibTableColumn
brFirmwareUpdateKeyword = _BrFirmwareUpdateKeyword_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 5, 55, 2, 1, 2),
    _BrFirmwareUpdateKeyword_Type()
)
brFirmwareUpdateKeyword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFirmwareUpdateKeyword.setStatus("mandatory")
_Printerstatus_ObjectIdentity = ObjectIdentity
printerstatus = _Printerstatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 6)
)


class _BrStatusSleep_Type(Integer32):
    """Custom type brStatusSleep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BrStatusSleep_Type.__name__ = "Integer32"
_BrStatusSleep_Object = MibScalar
brStatusSleep = _BrStatusSleep_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 6, 1),
    _BrStatusSleep_Type()
)
brStatusSleep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brStatusSleep.setStatus("mandatory")
_Secret_ObjectIdentity = ObjectIdentity
secret = _Secret_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 7)
)


class _BrSecretMPRetry_Type(Integer32):
    """Custom type brSecretMPRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrSecretMPRetry_Type.__name__ = "Integer32"
_BrSecretMPRetry_Object = MibScalar
brSecretMPRetry = _BrSecretMPRetry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 7, 1),
    _BrSecretMPRetry_Type()
)
brSecretMPRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brSecretMPRetry.setStatus("mandatory")
_BrSecretReprint_Type = Integer32
_BrSecretReprint_Object = MibScalar
brSecretReprint = _BrSecretReprint_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 7, 2),
    _BrSecretReprint_Type()
)
brSecretReprint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brSecretReprint.setStatus("mandatory")


class _BrFontSetting_Type(Integer32):
    """Custom type brFontSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrFontSetting_Type.__name__ = "Integer32"
_BrFontSetting_Object = MibScalar
brFontSetting = _BrFontSetting_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 7, 3),
    _BrFontSetting_Type()
)
brFontSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFontSetting.setStatus("mandatory")


class _BrFontSwitchOn_Type(Integer32):
    """Custom type brFontSwitchOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_BrFontSwitchOn_Type.__name__ = "Integer32"
_BrFontSwitchOn_Object = MibScalar
brFontSwitchOn = _BrFontSwitchOn_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 7, 4),
    _BrFontSwitchOn_Type()
)
brFontSwitchOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brFontSwitchOn.setStatus("mandatory")


class _BrFontSwitchOff_Type(Integer32):
    """Custom type brFontSwitchOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_BrFontSwitchOff_Type.__name__ = "Integer32"
_BrFontSwitchOff_Object = MibScalar
brFontSwitchOff = _BrFontSwitchOff_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 7, 5),
    _BrFontSwitchOff_Type()
)
brFontSwitchOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brFontSwitchOff.setStatus("mandatory")
_Adminsetting_ObjectIdentity = ObjectIdentity
adminsetting = _Adminsetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 8)
)
_Clockfunction_ObjectIdentity = ObjectIdentity
clockfunction = _Clockfunction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 8, 1)
)


class _BrClockFuncTimeStyle_Type(Integer32):
    """Custom type brClockFuncTimeStyle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BrClockFuncTimeStyle_Type.__name__ = "Integer32"
_BrClockFuncTimeStyle_Object = MibScalar
brClockFuncTimeStyle = _BrClockFuncTimeStyle_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 8, 1, 1),
    _BrClockFuncTimeStyle_Type()
)
brClockFuncTimeStyle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brClockFuncTimeStyle.setStatus("mandatory")


class _BrClockFuncSummerTime_Type(Integer32):
    """Custom type brClockFuncSummerTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BrClockFuncSummerTime_Type.__name__ = "Integer32"
_BrClockFuncSummerTime_Object = MibScalar
brClockFuncSummerTime = _BrClockFuncSummerTime_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 8, 1, 2),
    _BrClockFuncSummerTime_Type()
)
brClockFuncSummerTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brClockFuncSummerTime.setStatus("mandatory")


class _BrClockFuncTimeZone_Type(Integer32):
    """Custom type brClockFuncTimeZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-24, 24),
    )


_BrClockFuncTimeZone_Type.__name__ = "Integer32"
_BrClockFuncTimeZone_Object = MibScalar
brClockFuncTimeZone = _BrClockFuncTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 8, 1, 3),
    _BrClockFuncTimeZone_Type()
)
brClockFuncTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brClockFuncTimeZone.setStatus("mandatory")


class _BrClockFuncZoneSet_Type(Integer32):
    """Custom type brClockFuncZoneSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BrClockFuncZoneSet_Type.__name__ = "Integer32"
_BrClockFuncZoneSet_Object = MibScalar
brClockFuncZoneSet = _BrClockFuncZoneSet_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 3, 9, 4, 2, 1, 5, 8, 1, 4),
    _BrClockFuncZoneSet_Type()
)
brClockFuncZoneSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brClockFuncZoneSet.setStatus("mandatory")
_Interface_ObjectIdentity = ObjectIdentity
interface = _Interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4)
)
_NpCard_ObjectIdentity = ObjectIdentity
npCard = _NpCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3)
)
_NpSys_ObjectIdentity = ObjectIdentity
npSys = _NpSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1)
)
_NpConfig_ObjectIdentity = ObjectIdentity
npConfig = _NpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1, 1)
)


class _BrBasicSettingConfigured_Type(Integer32):
    """Custom type brBasicSettingConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configured", 2),
          ("unconfigured", 1))
    )


_BrBasicSettingConfigured_Type.__name__ = "Integer32"
_BrBasicSettingConfigured_Object = MibScalar
brBasicSettingConfigured = _BrBasicSettingConfigured_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1, 1, 1),
    _BrBasicSettingConfigured_Type()
)
brBasicSettingConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brBasicSettingConfigured.setStatus("mandatory")
_AdminCapa_ObjectIdentity = ObjectIdentity
adminCapa = _AdminCapa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1, 99)
)
_BrAdminCapability_Type = OctetString
_BrAdminCapability_Object = MibScalar
brAdminCapability = _BrAdminCapability_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1, 99, 1),
    _BrAdminCapability_Type()
)
brAdminCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brAdminCapability.setStatus("mandatory")
_UserSetting_ObjectIdentity = ObjectIdentity
userSetting = _UserSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1, 100)
)
_BrUserPasswordVerify_Type = DisplayString
_BrUserPasswordVerify_Object = MibScalar
brUserPasswordVerify = _BrUserPasswordVerify_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1, 100, 1),
    _BrUserPasswordVerify_Type()
)
brUserPasswordVerify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brUserPasswordVerify.setStatus("mandatory")
_BrUserPassword_Type = DisplayString
_BrUserPassword_Object = MibScalar
brUserPassword = _BrUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1, 100, 2),
    _BrUserPassword_Type()
)
brUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brUserPassword.setStatus("mandatory")
_Verify_ObjectIdentity = ObjectIdentity
verify = _Verify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1, 101)
)


class _BrpsVerifyPhysAddress_Type(OctetString):
    """Custom type brpsVerifyPhysAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_BrpsVerifyPhysAddress_Type.__name__ = "OctetString"
_BrpsVerifyPhysAddress_Object = MibScalar
brpsVerifyPhysAddress = _BrpsVerifyPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1, 101, 1),
    _BrpsVerifyPhysAddress_Type()
)
brpsVerifyPhysAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsVerifyPhysAddress.setStatus("mandatory")
_NpTcp_ObjectIdentity = ObjectIdentity
npTcp = _NpTcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 6)
)
_Lpd_ObjectIdentity = ObjectIdentity
lpd = _Lpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 6, 99)
)
_Banner_ObjectIdentity = ObjectIdentity
banner = _Banner_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 6, 99, 1)
)


class _BrLPDBannerPage_Type(Integer32):
    """Custom type brLPDBannerPage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BrLPDBannerPage_Type.__name__ = "Integer32"
_BrLPDBannerPage_Object = MibScalar
brLPDBannerPage = _BrLPDBannerPage_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 6, 99, 1, 1),
    _BrLPDBannerPage_Type()
)
brLPDBannerPage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLPDBannerPage.setStatus("mandatory")
_NpCtl_ObjectIdentity = ObjectIdentity
npCtl = _NpCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 7)
)
_EtherN_ObjectIdentity = ObjectIdentity
etherN = _EtherN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 7, 99)
)
_ENet_ObjectIdentity = ObjectIdentity
eNet = _ENet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 7, 99, 1)
)


class _BrENetModeSupported_Type(Integer32):
    """Custom type brENetModeSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrENetModeSupported_Type.__name__ = "Integer32"
_BrENetModeSupported_Object = MibScalar
brENetModeSupported = _BrENetModeSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 7, 99, 1, 1),
    _BrENetModeSupported_Type()
)
brENetModeSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brENetModeSupported.setStatus("mandatory")


class _BrENetMode_Type(Integer32):
    """Custom type brENetMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrENetMode_Type.__name__ = "Integer32"
_BrENetMode_Object = MibScalar
brENetMode = _BrENetMode_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 7, 99, 1, 2),
    _BrENetMode_Type()
)
brENetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brENetMode.setStatus("mandatory")
_NpPort_ObjectIdentity = ObjectIdentity
npPort = _NpPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 13)
)
_Funa_ObjectIdentity = ObjectIdentity
funa = _Funa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 13, 10)
)


class _BrFindPort_Type(Integer32):
    """Custom type brFindPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrFindPort_Type.__name__ = "Integer32"
_BrFindPort_Object = MibScalar
brFindPort = _BrFindPort_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 13, 10, 1),
    _BrFindPort_Type()
)
brFindPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brFindPort.setStatus("mandatory")


class _BrFindTime_Type(Integer32):
    """Custom type brFindTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrFindTime_Type.__name__ = "Integer32"
_BrFindTime_Object = MibScalar
brFindTime = _BrFindTime_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 13, 10, 2),
    _BrFindTime_Type()
)
brFindTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brFindTime.setStatus("mandatory")
_NpSet_ObjectIdentity = ObjectIdentity
npSet = _NpSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99)
)
_Dns_ObjectIdentity = ObjectIdentity
dns = _Dns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 1)
)


class _BrDNSSupported_Type(Integer32):
    """Custom type brDNSSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrDNSSupported_Type.__name__ = "Integer32"
_BrDNSSupported_Object = MibScalar
brDNSSupported = _BrDNSSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 1, 1),
    _BrDNSSupported_Type()
)
brDNSSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brDNSSupported.setStatus("mandatory")
_BrPrimaryDNSIP_Type = OctetString
_BrPrimaryDNSIP_Object = MibScalar
brPrimaryDNSIP = _BrPrimaryDNSIP_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 1, 2),
    _BrPrimaryDNSIP_Type()
)
brPrimaryDNSIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrimaryDNSIP.setStatus("mandatory")
_BrSecondaryDNSIP_Type = OctetString
_BrSecondaryDNSIP_Object = MibScalar
brSecondaryDNSIP = _BrSecondaryDNSIP_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 1, 3),
    _BrSecondaryDNSIP_Type()
)
brSecondaryDNSIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brSecondaryDNSIP.setStatus("mandatory")


class _BrDNSIPSetup_Type(Integer32):
    """Custom type brDNSIPSetup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("static", 1))
    )


_BrDNSIPSetup_Type.__name__ = "Integer32"
_BrDNSIPSetup_Object = MibScalar
brDNSIPSetup = _BrDNSIPSetup_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 1, 4),
    _BrDNSIPSetup_Type()
)
brDNSIPSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brDNSIPSetup.setStatus("mandatory")
_BrTCPIPConnectTime_Type = Integer32
_BrTCPIPConnectTime_Object = MibScalar
brTCPIPConnectTime = _BrTCPIPConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 1, 5),
    _BrTCPIPConnectTime_Type()
)
brTCPIPConnectTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brTCPIPConnectTime.setStatus("mandatory")


class _BrAdvancedDNSSupported_Type(Integer32):
    """Custom type brAdvancedDNSSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrAdvancedDNSSupported_Type.__name__ = "Integer32"
_BrAdvancedDNSSupported_Object = MibScalar
brAdvancedDNSSupported = _BrAdvancedDNSSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 1, 6),
    _BrAdvancedDNSSupported_Type()
)
brAdvancedDNSSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brAdvancedDNSSupported.setStatus("mandatory")
_BrPrimaryDNSIPAddress_Type = IpAddress
_BrPrimaryDNSIPAddress_Object = MibScalar
brPrimaryDNSIPAddress = _BrPrimaryDNSIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 1, 7),
    _BrPrimaryDNSIPAddress_Type()
)
brPrimaryDNSIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrimaryDNSIPAddress.setStatus("mandatory")
_BrSecondaryDNSIPAddress_Type = IpAddress
_BrSecondaryDNSIPAddress_Object = MibScalar
brSecondaryDNSIPAddress = _BrSecondaryDNSIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 1, 8),
    _BrSecondaryDNSIPAddress_Type()
)
brSecondaryDNSIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brSecondaryDNSIPAddress.setStatus("mandatory")


class _BrPOP3ServerName_Type(OctetString):
    """Custom type brPOP3ServerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BrPOP3ServerName_Type.__name__ = "OctetString"
_BrPOP3ServerName_Object = MibScalar
brPOP3ServerName = _BrPOP3ServerName_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 1, 9),
    _BrPOP3ServerName_Type()
)
brPOP3ServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPOP3ServerName.setStatus("mandatory")


class _BrSMTPServerName_Type(OctetString):
    """Custom type brSMTPServerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BrSMTPServerName_Type.__name__ = "OctetString"
_BrSMTPServerName_Object = MibScalar
brSMTPServerName = _BrSMTPServerName_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 1, 10),
    _BrSMTPServerName_Type()
)
brSMTPServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brSMTPServerName.setStatus("mandatory")
_Pushstatus_ObjectIdentity = ObjectIdentity
pushstatus = _Pushstatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 2)
)


class _BrPushStatusSupported_Type(Integer32):
    """Custom type brPushStatusSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrPushStatusSupported_Type.__name__ = "Integer32"
_BrPushStatusSupported_Object = MibScalar
brPushStatusSupported = _BrPushStatusSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 2, 1),
    _BrPushStatusSupported_Type()
)
brPushStatusSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPushStatusSupported.setStatus("mandatory")
_Priadmin_ObjectIdentity = ObjectIdentity
priadmin = _Priadmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 2, 2)
)
_BrPriMailAddress_Type = OctetString
_BrPriMailAddress_Object = MibScalar
brPriMailAddress = _BrPriMailAddress_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 2, 2, 1),
    _BrPriMailAddress_Type()
)
brPriMailAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPriMailAddress.setStatus("mandatory")


class _BrPriError_Type(Integer32):
    """Custom type brPriError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrPriError_Type.__name__ = "Integer32"
_BrPriError_Object = MibScalar
brPriError = _BrPriError_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 2, 2, 2),
    _BrPriError_Type()
)
brPriError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPriError.setStatus("mandatory")
_Secadmin_ObjectIdentity = ObjectIdentity
secadmin = _Secadmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 2, 3)
)
_BrSecMailAddress_Type = OctetString
_BrSecMailAddress_Object = MibScalar
brSecMailAddress = _BrSecMailAddress_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 2, 3, 1),
    _BrSecMailAddress_Type()
)
brSecMailAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brSecMailAddress.setStatus("mandatory")


class _BrSecError_Type(Integer32):
    """Custom type brSecError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrSecError_Type.__name__ = "Integer32"
_BrSecError_Object = MibScalar
brSecError = _BrSecError_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 2, 3, 2),
    _BrSecError_Type()
)
brSecError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brSecError.setStatus("mandatory")


class _BrNotificationCount_Type(Integer32):
    """Custom type brNotificationCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_BrNotificationCount_Type.__name__ = "Integer32"
_BrNotificationCount_Object = MibScalar
brNotificationCount = _BrNotificationCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 2, 4),
    _BrNotificationCount_Type()
)
brNotificationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brNotificationCount.setStatus("mandatory")
_BrNotificationTable_Object = MibTable
brNotificationTable = _BrNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 2, 5)
)
if mibBuilder.loadTexts:
    brNotificationTable.setStatus("mandatory")
_BrNotificationEntry_Object = MibTableRow
brNotificationEntry = _BrNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 2, 5, 1)
)
brNotificationEntry.setIndexNames(
    (0, "BROTHER-MIB", "brNotificationIndex"),
)
if mibBuilder.loadTexts:
    brNotificationEntry.setStatus("mandatory")


class _BrNotificationIndex_Type(Integer32):
    """Custom type brNotificationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BrNotificationIndex_Type.__name__ = "Integer32"
_BrNotificationIndex_Object = MibTableColumn
brNotificationIndex = _BrNotificationIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 2, 5, 1, 1),
    _BrNotificationIndex_Type()
)
brNotificationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brNotificationIndex.setStatus("mandatory")
_BrNotificationAddress_Type = OctetString
_BrNotificationAddress_Object = MibTableColumn
brNotificationAddress = _BrNotificationAddress_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 2, 5, 1, 2),
    _BrNotificationAddress_Type()
)
brNotificationAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brNotificationAddress.setStatus("mandatory")
_BrNotificationStatusGroup_Type = Integer32
_BrNotificationStatusGroup_Object = MibTableColumn
brNotificationStatusGroup = _BrNotificationStatusGroup_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 2, 5, 1, 3),
    _BrNotificationStatusGroup_Type()
)
brNotificationStatusGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brNotificationStatusGroup.setStatus("mandatory")
_BrNotificationShowURLInfo_Type = Integer32
_BrNotificationShowURLInfo_Object = MibTableColumn
brNotificationShowURLInfo = _BrNotificationShowURLInfo_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 2, 5, 1, 4),
    _BrNotificationShowURLInfo_Type()
)
brNotificationShowURLInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brNotificationShowURLInfo.setStatus("mandatory")
_BrNotificationErrorRule_Type = OctetString
_BrNotificationErrorRule_Object = MibTableColumn
brNotificationErrorRule = _BrNotificationErrorRule_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 2, 5, 1, 5),
    _BrNotificationErrorRule_Type()
)
brNotificationErrorRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brNotificationErrorRule.setStatus("mandatory")


class _BrNotificationRestoration_Type(Integer32):
    """Custom type brNotificationRestoration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_BrNotificationRestoration_Type.__name__ = "Integer32"
_BrNotificationRestoration_Object = MibTableColumn
brNotificationRestoration = _BrNotificationRestoration_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 2, 5, 1, 6),
    _BrNotificationRestoration_Type()
)
brNotificationRestoration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brNotificationRestoration.setStatus("mandatory")
_BrPrintersEmailaddress_Type = OctetString
_BrPrintersEmailaddress_Object = MibScalar
brPrintersEmailaddress = _BrPrintersEmailaddress_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 2, 6),
    _BrPrintersEmailaddress_Type()
)
brPrintersEmailaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brPrintersEmailaddress.setStatus("mandatory")
_BrNotificationVersion_Type = OctetString
_BrNotificationVersion_Object = MibScalar
brNotificationVersion = _BrNotificationVersion_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 2, 7),
    _BrNotificationVersion_Type()
)
brNotificationVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brNotificationVersion.setStatus("mandatory")


class _BrShowIPAddressInfo_Type(Integer32):
    """Custom type brShowIPAddressInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_BrShowIPAddressInfo_Type.__name__ = "Integer32"
_BrShowIPAddressInfo_Object = MibScalar
brShowIPAddressInfo = _BrShowIPAddressInfo_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 2, 8),
    _BrShowIPAddressInfo_Type()
)
brShowIPAddressInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brShowIPAddressInfo.setStatus("mandatory")
_BrNotificationRuleTable_Object = MibTable
brNotificationRuleTable = _BrNotificationRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 2, 50)
)
if mibBuilder.loadTexts:
    brNotificationRuleTable.setStatus("mandatory")
_BrNotificationRuleEntry_Object = MibTableRow
brNotificationRuleEntry = _BrNotificationRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 2, 50, 1)
)
brNotificationRuleEntry.setIndexNames(
    (0, "BROTHER-MIB", "brNotificationIndex"),
    (0, "BROTHER-MIB", "brNotificationRuleIndex"),
)
if mibBuilder.loadTexts:
    brNotificationRuleEntry.setStatus("mandatory")


class _BrNotificationRuleIndex_Type(Integer32):
    """Custom type brNotificationRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BrNotificationRuleIndex_Type.__name__ = "Integer32"
_BrNotificationRuleIndex_Object = MibTableColumn
brNotificationRuleIndex = _BrNotificationRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 2, 50, 1, 1),
    _BrNotificationRuleIndex_Type()
)
brNotificationRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brNotificationRuleIndex.setStatus("mandatory")


class _BrNotificationStatusID_Type(Integer32):
    """Custom type brNotificationStatusID based on Integer32"""
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
        *(("changeDrum", 9),
          ("coverOpen", 1),
          ("inputMediaError", 11),
          ("jam", 2),
          ("machineError", 14),
          ("memoryFull", 10),
          ("notInstalled", 13),
          ("otherErrors", 15),
          ("outputFull", 12),
          ("servicemanConsumableError", 8),
          ("servicemanConsumableWarning", 7),
          ("tonerEmpty", 4),
          ("tonerLow", 3),
          ("userConsumableError", 6),
          ("userConsumableWarning", 5))
    )


_BrNotificationStatusID_Type.__name__ = "Integer32"
_BrNotificationStatusID_Object = MibTableColumn
brNotificationStatusID = _BrNotificationStatusID_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 2, 50, 1, 2),
    _BrNotificationStatusID_Type()
)
brNotificationStatusID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brNotificationStatusID.setStatus("mandatory")


class _BrNotificationMainRule_Type(Integer32):
    """Custom type brNotificationMainRule based on Integer32"""
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
        *(("everytime", 2),
          ("minutes", 4),
          ("off", 1),
          ("times", 3))
    )


_BrNotificationMainRule_Type.__name__ = "Integer32"
_BrNotificationMainRule_Object = MibTableColumn
brNotificationMainRule = _BrNotificationMainRule_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 2, 50, 1, 3),
    _BrNotificationMainRule_Type()
)
brNotificationMainRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brNotificationMainRule.setStatus("mandatory")
_BrNotificationRuleValue_Type = Integer32
_BrNotificationRuleValue_Object = MibTableColumn
brNotificationRuleValue = _BrNotificationRuleValue_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 2, 50, 1, 4),
    _BrNotificationRuleValue_Type()
)
brNotificationRuleValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brNotificationRuleValue.setStatus("mandatory")
_Pjl_ObjectIdentity = ObjectIdentity
pjl = _Pjl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 3)
)
_Pjlinfo_ObjectIdentity = ObjectIdentity
pjlinfo = _Pjlinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 3, 1)
)
_BrPJLInfoOptionsTable_Object = MibTable
brPJLInfoOptionsTable = _BrPJLInfoOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 3, 1, 1)
)
if mibBuilder.loadTexts:
    brPJLInfoOptionsTable.setStatus("mandatory")
_BrPJLInfoOptionsEntry_Object = MibTableRow
brPJLInfoOptionsEntry = _BrPJLInfoOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 3, 1, 1, 1)
)
brPJLInfoOptionsEntry.setIndexNames(
    (0, "BROTHER-MIB", "brPJLInfoOptionsIndex"),
)
if mibBuilder.loadTexts:
    brPJLInfoOptionsEntry.setStatus("mandatory")


class _BrPJLInfoOptionsIndex_Type(Integer32):
    """Custom type brPJLInfoOptionsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BrPJLInfoOptionsIndex_Type.__name__ = "Integer32"
_BrPJLInfoOptionsIndex_Object = MibTableColumn
brPJLInfoOptionsIndex = _BrPJLInfoOptionsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 3, 1, 1, 1, 1),
    _BrPJLInfoOptionsIndex_Type()
)
brPJLInfoOptionsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPJLInfoOptionsIndex.setStatus("mandatory")


class _BrPJLInfoOptions_Type(OctetString):
    """Custom type brPJLInfoOptions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrPJLInfoOptions_Type.__name__ = "OctetString"
_BrPJLInfoOptions_Object = MibTableColumn
brPJLInfoOptions = _BrPJLInfoOptions_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 3, 1, 1, 1, 2),
    _BrPJLInfoOptions_Type()
)
brPJLInfoOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPJLInfoOptions.setStatus("mandatory")
_BrPJLInfoIntrayconfigTable_Object = MibTable
brPJLInfoIntrayconfigTable = _BrPJLInfoIntrayconfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 3, 1, 2)
)
if mibBuilder.loadTexts:
    brPJLInfoIntrayconfigTable.setStatus("mandatory")
_BrPJLInfoIntrayconfigEntry_Object = MibTableRow
brPJLInfoIntrayconfigEntry = _BrPJLInfoIntrayconfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 3, 1, 2, 1)
)
brPJLInfoIntrayconfigEntry.setIndexNames(
    (0, "BROTHER-MIB", "brPJLInfoIntrayconfigIndex"),
)
if mibBuilder.loadTexts:
    brPJLInfoIntrayconfigEntry.setStatus("mandatory")


class _BrPJLInfoIntrayconfigIndex_Type(Integer32):
    """Custom type brPJLInfoIntrayconfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BrPJLInfoIntrayconfigIndex_Type.__name__ = "Integer32"
_BrPJLInfoIntrayconfigIndex_Object = MibTableColumn
brPJLInfoIntrayconfigIndex = _BrPJLInfoIntrayconfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 3, 1, 2, 1, 1),
    _BrPJLInfoIntrayconfigIndex_Type()
)
brPJLInfoIntrayconfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPJLInfoIntrayconfigIndex.setStatus("mandatory")


class _BrPJLInfoIntrayconfig_Type(OctetString):
    """Custom type brPJLInfoIntrayconfig based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrPJLInfoIntrayconfig_Type.__name__ = "OctetString"
_BrPJLInfoIntrayconfig_Object = MibTableColumn
brPJLInfoIntrayconfig = _BrPJLInfoIntrayconfig_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 3, 1, 2, 1, 2),
    _BrPJLInfoIntrayconfig_Type()
)
brPJLInfoIntrayconfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPJLInfoIntrayconfig.setStatus("mandatory")
_BrPJLInfoOuttrayconfigTable_Object = MibTable
brPJLInfoOuttrayconfigTable = _BrPJLInfoOuttrayconfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 3, 1, 3)
)
if mibBuilder.loadTexts:
    brPJLInfoOuttrayconfigTable.setStatus("mandatory")
_BrPJLInfoOuttrayconfigEntry_Object = MibTableRow
brPJLInfoOuttrayconfigEntry = _BrPJLInfoOuttrayconfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 3, 1, 3, 1)
)
brPJLInfoOuttrayconfigEntry.setIndexNames(
    (0, "BROTHER-MIB", "brPJLInfoOuttrayconfigIndex"),
)
if mibBuilder.loadTexts:
    brPJLInfoOuttrayconfigEntry.setStatus("mandatory")


class _BrPJLInfoOuttrayconfigIndex_Type(Integer32):
    """Custom type brPJLInfoOuttrayconfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BrPJLInfoOuttrayconfigIndex_Type.__name__ = "Integer32"
_BrPJLInfoOuttrayconfigIndex_Object = MibTableColumn
brPJLInfoOuttrayconfigIndex = _BrPJLInfoOuttrayconfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 3, 1, 3, 1, 1),
    _BrPJLInfoOuttrayconfigIndex_Type()
)
brPJLInfoOuttrayconfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPJLInfoOuttrayconfigIndex.setStatus("mandatory")


class _BrPJLInfoOuttrayconfig_Type(OctetString):
    """Custom type brPJLInfoOuttrayconfig based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrPJLInfoOuttrayconfig_Type.__name__ = "OctetString"
_BrPJLInfoOuttrayconfig_Object = MibTableColumn
brPJLInfoOuttrayconfig = _BrPJLInfoOuttrayconfig_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 3, 1, 3, 1, 2),
    _BrPJLInfoOuttrayconfig_Type()
)
brPJLInfoOuttrayconfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPJLInfoOuttrayconfig.setStatus("mandatory")
_BrPJLInfoDXconfigTable_Object = MibTable
brPJLInfoDXconfigTable = _BrPJLInfoDXconfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 3, 1, 4)
)
if mibBuilder.loadTexts:
    brPJLInfoDXconfigTable.setStatus("mandatory")
_BrPJLInfoDXconfigEntry_Object = MibTableRow
brPJLInfoDXconfigEntry = _BrPJLInfoDXconfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 3, 1, 4, 1)
)
brPJLInfoDXconfigEntry.setIndexNames(
    (0, "BROTHER-MIB", "brPJLInfoDXconfigIndex"),
)
if mibBuilder.loadTexts:
    brPJLInfoDXconfigEntry.setStatus("mandatory")


class _BrPJLInfoDXconfigIndex_Type(Integer32):
    """Custom type brPJLInfoDXconfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BrPJLInfoDXconfigIndex_Type.__name__ = "Integer32"
_BrPJLInfoDXconfigIndex_Object = MibTableColumn
brPJLInfoDXconfigIndex = _BrPJLInfoDXconfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 3, 1, 4, 1, 1),
    _BrPJLInfoDXconfigIndex_Type()
)
brPJLInfoDXconfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPJLInfoDXconfigIndex.setStatus("mandatory")


class _BrPJLInfoDXconfig_Type(OctetString):
    """Custom type brPJLInfoDXconfig based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrPJLInfoDXconfig_Type.__name__ = "OctetString"
_BrPJLInfoDXconfig_Object = MibTableColumn
brPJLInfoDXconfig = _BrPJLInfoDXconfig_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 3, 1, 4, 1, 2),
    _BrPJLInfoDXconfig_Type()
)
brPJLInfoDXconfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPJLInfoDXconfig.setStatus("mandatory")
_BrPJLInfoStorageconfigTable_Object = MibTable
brPJLInfoStorageconfigTable = _BrPJLInfoStorageconfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 3, 1, 5)
)
if mibBuilder.loadTexts:
    brPJLInfoStorageconfigTable.setStatus("mandatory")
_BrPJLInfoStorageconfigEntry_Object = MibTableRow
brPJLInfoStorageconfigEntry = _BrPJLInfoStorageconfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 3, 1, 5, 1)
)
brPJLInfoStorageconfigEntry.setIndexNames(
    (0, "BROTHER-MIB", "brPJLInfoStorageconfigIndex"),
)
if mibBuilder.loadTexts:
    brPJLInfoStorageconfigEntry.setStatus("mandatory")


class _BrPJLInfoStorageconfigIndex_Type(Integer32):
    """Custom type brPJLInfoStorageconfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BrPJLInfoStorageconfigIndex_Type.__name__ = "Integer32"
_BrPJLInfoStorageconfigIndex_Object = MibTableColumn
brPJLInfoStorageconfigIndex = _BrPJLInfoStorageconfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 3, 1, 5, 1, 1),
    _BrPJLInfoStorageconfigIndex_Type()
)
brPJLInfoStorageconfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPJLInfoStorageconfigIndex.setStatus("mandatory")


class _BrPJLInfoStorageconfig_Type(OctetString):
    """Custom type brPJLInfoStorageconfig based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrPJLInfoStorageconfig_Type.__name__ = "OctetString"
_BrPJLInfoStorageconfig_Object = MibTableColumn
brPJLInfoStorageconfig = _BrPJLInfoStorageconfig_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 3, 1, 5, 1, 2),
    _BrPJLInfoStorageconfig_Type()
)
brPJLInfoStorageconfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPJLInfoStorageconfig.setStatus("mandatory")
_BrPJLInfoFirmwareUpdateconfigTable_Object = MibTable
brPJLInfoFirmwareUpdateconfigTable = _BrPJLInfoFirmwareUpdateconfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 3, 1, 6)
)
if mibBuilder.loadTexts:
    brPJLInfoFirmwareUpdateconfigTable.setStatus("mandatory")
_BrPJLInfoFirmwareUpdateconfigEntry_Object = MibTableRow
brPJLInfoFirmwareUpdateconfigEntry = _BrPJLInfoFirmwareUpdateconfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 3, 1, 6, 1)
)
brPJLInfoFirmwareUpdateconfigEntry.setIndexNames(
    (0, "BROTHER-MIB", "brPJLInfoFirmwareUpdateconfigIndex"),
)
if mibBuilder.loadTexts:
    brPJLInfoFirmwareUpdateconfigEntry.setStatus("mandatory")


class _BrPJLInfoFirmwareUpdateconfigIndex_Type(Integer32):
    """Custom type brPJLInfoFirmwareUpdateconfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BrPJLInfoFirmwareUpdateconfigIndex_Type.__name__ = "Integer32"
_BrPJLInfoFirmwareUpdateconfigIndex_Object = MibTableColumn
brPJLInfoFirmwareUpdateconfigIndex = _BrPJLInfoFirmwareUpdateconfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 3, 1, 6, 1, 1),
    _BrPJLInfoFirmwareUpdateconfigIndex_Type()
)
brPJLInfoFirmwareUpdateconfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPJLInfoFirmwareUpdateconfigIndex.setStatus("mandatory")


class _BrPJLInfoFirmwareUpdateconfig_Type(OctetString):
    """Custom type brPJLInfoFirmwareUpdateconfig based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BrPJLInfoFirmwareUpdateconfig_Type.__name__ = "OctetString"
_BrPJLInfoFirmwareUpdateconfig_Object = MibTableColumn
brPJLInfoFirmwareUpdateconfig = _BrPJLInfoFirmwareUpdateconfig_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 3, 1, 6, 1, 2),
    _BrPJLInfoFirmwareUpdateconfig_Type()
)
brPJLInfoFirmwareUpdateconfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPJLInfoFirmwareUpdateconfig.setStatus("mandatory")
_EMailReports_ObjectIdentity = ObjectIdentity
eMailReports = _EMailReports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 4)
)


class _BrEmailReportsSupported_Type(Integer32):
    """Custom type brEmailReportsSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrEmailReportsSupported_Type.__name__ = "Integer32"
_BrEmailReportsSupported_Object = MibScalar
brEmailReportsSupported = _BrEmailReportsSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 4, 1),
    _BrEmailReportsSupported_Type()
)
brEmailReportsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brEmailReportsSupported.setStatus("mandatory")
_BrEmailReportsCount_Type = Integer32
_BrEmailReportsCount_Object = MibScalar
brEmailReportsCount = _BrEmailReportsCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 4, 2),
    _BrEmailReportsCount_Type()
)
brEmailReportsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brEmailReportsCount.setStatus("mandatory")
_BrEmailReportsTable_Object = MibTable
brEmailReportsTable = _BrEmailReportsTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 4, 11)
)
if mibBuilder.loadTexts:
    brEmailReportsTable.setStatus("mandatory")
_BrEmailReportsEntry_Object = MibTableRow
brEmailReportsEntry = _BrEmailReportsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 4, 11, 1)
)
brEmailReportsEntry.setIndexNames(
    (0, "BROTHER-MIB", "brEmailReportsIndex"),
)
if mibBuilder.loadTexts:
    brEmailReportsEntry.setStatus("mandatory")


class _BrEmailReportsIndex_Type(Integer32):
    """Custom type brEmailReportsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BrEmailReportsIndex_Type.__name__ = "Integer32"
_BrEmailReportsIndex_Object = MibTableColumn
brEmailReportsIndex = _BrEmailReportsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 4, 11, 1, 1),
    _BrEmailReportsIndex_Type()
)
brEmailReportsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brEmailReportsIndex.setStatus("mandatory")


class _BrEmailReportsAddress_Type(OctetString):
    """Custom type brEmailReportsAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_BrEmailReportsAddress_Type.__name__ = "OctetString"
_BrEmailReportsAddress_Object = MibTableColumn
brEmailReportsAddress = _BrEmailReportsAddress_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 4, 11, 1, 2),
    _BrEmailReportsAddress_Type()
)
brEmailReportsAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brEmailReportsAddress.setStatus("mandatory")


class _BrEmailReportsFrequency_Type(Integer32):
    """Custom type brEmailReportsFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("daily", 1),
          ("monthly", 3),
          ("weekly", 2))
    )


_BrEmailReportsFrequency_Type.__name__ = "Integer32"
_BrEmailReportsFrequency_Object = MibTableColumn
brEmailReportsFrequency = _BrEmailReportsFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 4, 11, 1, 3),
    _BrEmailReportsFrequency_Type()
)
brEmailReportsFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brEmailReportsFrequency.setStatus("mandatory")
_BrEmailReportsTime_Type = OctetString
_BrEmailReportsTime_Object = MibTableColumn
brEmailReportsTime = _BrEmailReportsTime_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 4, 11, 1, 4),
    _BrEmailReportsTime_Type()
)
brEmailReportsTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brEmailReportsTime.setStatus("mandatory")


class _BrEmailReportsWeek_Type(Integer32):
    """Custom type brEmailReportsWeek based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("friday", 6),
          ("monday", 2),
          ("saturday", 7),
          ("sunday", 1),
          ("thursday", 5),
          ("tuesday", 3),
          ("wednesday", 4))
    )


_BrEmailReportsWeek_Type.__name__ = "Integer32"
_BrEmailReportsWeek_Object = MibTableColumn
brEmailReportsWeek = _BrEmailReportsWeek_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 4, 11, 1, 5),
    _BrEmailReportsWeek_Type()
)
brEmailReportsWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brEmailReportsWeek.setStatus("mandatory")


class _BrEmailReportsDate_Type(Integer32):
    """Custom type brEmailReportsDate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_BrEmailReportsDate_Type.__name__ = "Integer32"
_BrEmailReportsDate_Object = MibTableColumn
brEmailReportsDate = _BrEmailReportsDate_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 4, 11, 1, 6),
    _BrEmailReportsDate_Type()
)
brEmailReportsDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brEmailReportsDate.setStatus("mandatory")


class _BrEmailReportsSendReportNow_Type(Integer32):
    """Custom type brEmailReportsSendReportNow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_BrEmailReportsSendReportNow_Type.__name__ = "Integer32"
_BrEmailReportsSendReportNow_Object = MibTableColumn
brEmailReportsSendReportNow = _BrEmailReportsSendReportNow_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 4, 11, 1, 7),
    _BrEmailReportsSendReportNow_Type()
)
brEmailReportsSendReportNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brEmailReportsSendReportNow.setStatus("mandatory")


class _BrEmailReportsSendReportatPowerOn_Type(Integer32):
    """Custom type brEmailReportsSendReportatPowerOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_BrEmailReportsSendReportatPowerOn_Type.__name__ = "Integer32"
_BrEmailReportsSendReportatPowerOn_Object = MibTableColumn
brEmailReportsSendReportatPowerOn = _BrEmailReportsSendReportatPowerOn_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 4, 11, 1, 8),
    _BrEmailReportsSendReportatPowerOn_Type()
)
brEmailReportsSendReportatPowerOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brEmailReportsSendReportatPowerOn.setStatus("mandatory")


class _BrEmailReportsNoRTCFrequency_Type(Integer32):
    """Custom type brEmailReportsNoRTCFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_BrEmailReportsNoRTCFrequency_Type.__name__ = "Integer32"
_BrEmailReportsNoRTCFrequency_Object = MibTableColumn
brEmailReportsNoRTCFrequency = _BrEmailReportsNoRTCFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 4, 11, 1, 9),
    _BrEmailReportsNoRTCFrequency_Type()
)
brEmailReportsNoRTCFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brEmailReportsNoRTCFrequency.setStatus("mandatory")


class _BrEmailReportsReportFormat_Type(Integer32):
    """Custom type brEmailReportsReportFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("plaintext", 1),
          ("xml", 2))
    )


_BrEmailReportsReportFormat_Type.__name__ = "Integer32"
_BrEmailReportsReportFormat_Object = MibTableColumn
brEmailReportsReportFormat = _BrEmailReportsReportFormat_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 99, 4, 11, 1, 10),
    _BrEmailReportsReportFormat_Type()
)
brEmailReportsReportFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brEmailReportsReportFormat.setStatus("mandatory")
_Wireless_ObjectIdentity = ObjectIdentity
wireless = _Wireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100)
)
_WlInfo_ObjectIdentity = ObjectIdentity
wlInfo = _WlInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1)
)
_WlCapability_ObjectIdentity = ObjectIdentity
wlCapability = _WlCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 1)
)
_BrpsWLanDot11Supported_Type = Integer32
_BrpsWLanDot11Supported_Object = MibScalar
brpsWLanDot11Supported = _BrpsWLanDot11Supported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 1, 1),
    _BrpsWLanDot11Supported_Type()
)
brpsWLanDot11Supported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanDot11Supported.setStatus("mandatory")
_BrpsWLanAvailableChannel_Type = OctetString
_BrpsWLanAvailableChannel_Object = MibScalar
brpsWLanAvailableChannel = _BrpsWLanAvailableChannel_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 1, 2),
    _BrpsWLanAvailableChannel_Type()
)
brpsWLanAvailableChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanAvailableChannel.setStatus("mandatory")
_BrpsWLanCapabilityEncryptModeCount_Type = Integer32
_BrpsWLanCapabilityEncryptModeCount_Object = MibScalar
brpsWLanCapabilityEncryptModeCount = _BrpsWLanCapabilityEncryptModeCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 1, 3),
    _BrpsWLanCapabilityEncryptModeCount_Type()
)
brpsWLanCapabilityEncryptModeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanCapabilityEncryptModeCount.setStatus("mandatory")
_BrpsWLanCapabilityEncryptModeTable_Object = MibTable
brpsWLanCapabilityEncryptModeTable = _BrpsWLanCapabilityEncryptModeTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 1, 4)
)
if mibBuilder.loadTexts:
    brpsWLanCapabilityEncryptModeTable.setStatus("mandatory")
_BrpsWLanCapabilityEncryptModeEntry_Object = MibTableRow
brpsWLanCapabilityEncryptModeEntry = _BrpsWLanCapabilityEncryptModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 1, 4, 1)
)
brpsWLanCapabilityEncryptModeEntry.setIndexNames(
    (0, "BROTHER-MIB", "brpsWLanCapabilityEncryptModeIndex"),
)
if mibBuilder.loadTexts:
    brpsWLanCapabilityEncryptModeEntry.setStatus("mandatory")


class _BrpsWLanCapabilityEncryptModeIndex_Type(Integer32):
    """Custom type brpsWLanCapabilityEncryptModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BrpsWLanCapabilityEncryptModeIndex_Type.__name__ = "Integer32"
_BrpsWLanCapabilityEncryptModeIndex_Object = MibTableColumn
brpsWLanCapabilityEncryptModeIndex = _BrpsWLanCapabilityEncryptModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 1, 4, 1, 1),
    _BrpsWLanCapabilityEncryptModeIndex_Type()
)
brpsWLanCapabilityEncryptModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanCapabilityEncryptModeIndex.setStatus("mandatory")


class _BrpsWLanCapabilityEncryptModeType_Type(Integer32):
    """Custom type brpsWLanCapabilityEncryptModeType based on Integer32"""
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
        *(("aes", 4),
          ("ckip", 5),
          ("none", 1),
          ("tkip", 3),
          ("wep", 2))
    )


_BrpsWLanCapabilityEncryptModeType_Type.__name__ = "Integer32"
_BrpsWLanCapabilityEncryptModeType_Object = MibTableColumn
brpsWLanCapabilityEncryptModeType = _BrpsWLanCapabilityEncryptModeType_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 1, 4, 1, 2),
    _BrpsWLanCapabilityEncryptModeType_Type()
)
brpsWLanCapabilityEncryptModeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanCapabilityEncryptModeType.setStatus("mandatory")
_BrpsWLanCapabilityEncryptModeDescription_Type = OctetString
_BrpsWLanCapabilityEncryptModeDescription_Object = MibTableColumn
brpsWLanCapabilityEncryptModeDescription = _BrpsWLanCapabilityEncryptModeDescription_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 1, 4, 1, 3),
    _BrpsWLanCapabilityEncryptModeDescription_Type()
)
brpsWLanCapabilityEncryptModeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanCapabilityEncryptModeDescription.setStatus("mandatory")
_BrpsWLanCapabilityEncryptModeSupported_Type = Integer32
_BrpsWLanCapabilityEncryptModeSupported_Object = MibTableColumn
brpsWLanCapabilityEncryptModeSupported = _BrpsWLanCapabilityEncryptModeSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 1, 4, 1, 4),
    _BrpsWLanCapabilityEncryptModeSupported_Type()
)
brpsWLanCapabilityEncryptModeSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanCapabilityEncryptModeSupported.setStatus("mandatory")
_BrpsWLanCapabilityAuthModeCount_Type = Integer32
_BrpsWLanCapabilityAuthModeCount_Object = MibScalar
brpsWLanCapabilityAuthModeCount = _BrpsWLanCapabilityAuthModeCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 1, 5),
    _BrpsWLanCapabilityAuthModeCount_Type()
)
brpsWLanCapabilityAuthModeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanCapabilityAuthModeCount.setStatus("mandatory")
_BrpsWLanCapabilityAuthModeTable_Object = MibTable
brpsWLanCapabilityAuthModeTable = _BrpsWLanCapabilityAuthModeTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 1, 6)
)
if mibBuilder.loadTexts:
    brpsWLanCapabilityAuthModeTable.setStatus("mandatory")
_BrpsWLanCapabilityAuthModeEntry_Object = MibTableRow
brpsWLanCapabilityAuthModeEntry = _BrpsWLanCapabilityAuthModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 1, 6, 1)
)
brpsWLanCapabilityAuthModeEntry.setIndexNames(
    (0, "BROTHER-MIB", "brpsWLanCapabilitAuthModeIndex"),
)
if mibBuilder.loadTexts:
    brpsWLanCapabilityAuthModeEntry.setStatus("mandatory")


class _BrpsWLanCapabilitAuthModeIndex_Type(Integer32):
    """Custom type brpsWLanCapabilitAuthModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BrpsWLanCapabilitAuthModeIndex_Type.__name__ = "Integer32"
_BrpsWLanCapabilitAuthModeIndex_Object = MibTableColumn
brpsWLanCapabilitAuthModeIndex = _BrpsWLanCapabilitAuthModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 1, 6, 1, 1),
    _BrpsWLanCapabilitAuthModeIndex_Type()
)
brpsWLanCapabilitAuthModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanCapabilitAuthModeIndex.setStatus("mandatory")


class _BrpsWLanCapabilityAuthModeType_Type(Integer32):
    """Custom type brpsWLanCapabilityAuthModeType based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("eapfast-gtc", 10),
          ("eapfast-mschapv2", 9),
          ("eapfast-none", 8),
          ("eapfast-tls", 11),
          ("leap", 7),
          ("opensystem", 1),
          ("shardkey", 2),
          ("wpa", 5),
          ("wpa-none", 4),
          ("wpa-psk", 3),
          ("wpa2", 6),
          ("wpa2-psk", 12))
    )


_BrpsWLanCapabilityAuthModeType_Type.__name__ = "Integer32"
_BrpsWLanCapabilityAuthModeType_Object = MibTableColumn
brpsWLanCapabilityAuthModeType = _BrpsWLanCapabilityAuthModeType_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 1, 6, 1, 2),
    _BrpsWLanCapabilityAuthModeType_Type()
)
brpsWLanCapabilityAuthModeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanCapabilityAuthModeType.setStatus("mandatory")
_BrpsWLanCapabilityAuthModeDescription_Type = OctetString
_BrpsWLanCapabilityAuthModeDescription_Object = MibTableColumn
brpsWLanCapabilityAuthModeDescription = _BrpsWLanCapabilityAuthModeDescription_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 1, 6, 1, 3),
    _BrpsWLanCapabilityAuthModeDescription_Type()
)
brpsWLanCapabilityAuthModeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanCapabilityAuthModeDescription.setStatus("mandatory")
_BrpsWLanCapabilityAuthModeSupported_Type = Integer32
_BrpsWLanCapabilityAuthModeSupported_Object = MibTableColumn
brpsWLanCapabilityAuthModeSupported = _BrpsWLanCapabilityAuthModeSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 1, 6, 1, 4),
    _BrpsWLanCapabilityAuthModeSupported_Type()
)
brpsWLanCapabilityAuthModeSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanCapabilityAuthModeSupported.setStatus("mandatory")
_BrpsWLanCapabilityAuthEAPCount_Type = Integer32
_BrpsWLanCapabilityAuthEAPCount_Object = MibScalar
brpsWLanCapabilityAuthEAPCount = _BrpsWLanCapabilityAuthEAPCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 1, 7),
    _BrpsWLanCapabilityAuthEAPCount_Type()
)
brpsWLanCapabilityAuthEAPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanCapabilityAuthEAPCount.setStatus("mandatory")
_BrpsWLanCapabilityAuthEAPTable_Object = MibTable
brpsWLanCapabilityAuthEAPTable = _BrpsWLanCapabilityAuthEAPTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 1, 8)
)
if mibBuilder.loadTexts:
    brpsWLanCapabilityAuthEAPTable.setStatus("mandatory")
_BrpsWLanCapabilityAuthEAPEntry_Object = MibTableRow
brpsWLanCapabilityAuthEAPEntry = _BrpsWLanCapabilityAuthEAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 1, 8, 1)
)
brpsWLanCapabilityAuthEAPEntry.setIndexNames(
    (0, "BROTHER-MIB", "brpsWLanCapabilityAuthEAPIndex"),
)
if mibBuilder.loadTexts:
    brpsWLanCapabilityAuthEAPEntry.setStatus("mandatory")


class _BrpsWLanCapabilityAuthEAPIndex_Type(Integer32):
    """Custom type brpsWLanCapabilityAuthEAPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BrpsWLanCapabilityAuthEAPIndex_Type.__name__ = "Integer32"
_BrpsWLanCapabilityAuthEAPIndex_Object = MibTableColumn
brpsWLanCapabilityAuthEAPIndex = _BrpsWLanCapabilityAuthEAPIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 1, 8, 1, 1),
    _BrpsWLanCapabilityAuthEAPIndex_Type()
)
brpsWLanCapabilityAuthEAPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanCapabilityAuthEAPIndex.setStatus("mandatory")


class _BrpsWLanCapabilityAuthEAPType_Type(Integer32):
    """Custom type brpsWLanCapabilityAuthEAPType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("eap-md5", 1),
          ("eap-tls", 2),
          ("eap-ttls", 3),
          ("eapfast-gtc", 8),
          ("eapfast-mschapv2", 7),
          ("eapfast-none", 6),
          ("eapfast-tls", 9),
          ("leap", 5),
          ("peap", 4))
    )


_BrpsWLanCapabilityAuthEAPType_Type.__name__ = "Integer32"
_BrpsWLanCapabilityAuthEAPType_Object = MibTableColumn
brpsWLanCapabilityAuthEAPType = _BrpsWLanCapabilityAuthEAPType_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 1, 8, 1, 2),
    _BrpsWLanCapabilityAuthEAPType_Type()
)
brpsWLanCapabilityAuthEAPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanCapabilityAuthEAPType.setStatus("mandatory")
_BrpsWLanCapabilityAuthEAPDescription_Type = OctetString
_BrpsWLanCapabilityAuthEAPDescription_Object = MibTableColumn
brpsWLanCapabilityAuthEAPDescription = _BrpsWLanCapabilityAuthEAPDescription_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 1, 8, 1, 3),
    _BrpsWLanCapabilityAuthEAPDescription_Type()
)
brpsWLanCapabilityAuthEAPDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanCapabilityAuthEAPDescription.setStatus("mandatory")
_BrpsWLanCapabilityAuthEAPSupported_Type = Integer32
_BrpsWLanCapabilityAuthEAPSupported_Object = MibTableColumn
brpsWLanCapabilityAuthEAPSupported = _BrpsWLanCapabilityAuthEAPSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 1, 8, 1, 4),
    _BrpsWLanCapabilityAuthEAPSupported_Type()
)
brpsWLanCapabilityAuthEAPSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanCapabilityAuthEAPSupported.setStatus("mandatory")


class _BrpsWLanCapabilityAuthEAPSupportAuthentication_Type(Integer32):
    """Custom type brpsWLanCapabilityAuthEAPSupportAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_BrpsWLanCapabilityAuthEAPSupportAuthentication_Type.__name__ = "Integer32"
_BrpsWLanCapabilityAuthEAPSupportAuthentication_Object = MibTableColumn
brpsWLanCapabilityAuthEAPSupportAuthentication = _BrpsWLanCapabilityAuthEAPSupportAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 1, 8, 1, 5),
    _BrpsWLanCapabilityAuthEAPSupportAuthentication_Type()
)
brpsWLanCapabilityAuthEAPSupportAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanCapabilityAuthEAPSupportAuthentication.setStatus("mandatory")


class _BrpsWLanCapabilityAuthEAPSupportEncryption_Type(Integer32):
    """Custom type brpsWLanCapabilityAuthEAPSupportEncryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_BrpsWLanCapabilityAuthEAPSupportEncryption_Type.__name__ = "Integer32"
_BrpsWLanCapabilityAuthEAPSupportEncryption_Object = MibTableColumn
brpsWLanCapabilityAuthEAPSupportEncryption = _BrpsWLanCapabilityAuthEAPSupportEncryption_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 1, 8, 1, 6),
    _BrpsWLanCapabilityAuthEAPSupportEncryption_Type()
)
brpsWLanCapabilityAuthEAPSupportEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanCapabilityAuthEAPSupportEncryption.setStatus("mandatory")
_WlGeneralInfo_ObjectIdentity = ObjectIdentity
wlGeneralInfo = _WlGeneralInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 2)
)
_BrpsWLanDestination_Type = Integer32
_BrpsWLanDestination_Object = MibScalar
brpsWLanDestination = _BrpsWLanDestination_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 2, 1),
    _BrpsWLanDestination_Type()
)
brpsWLanDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanDestination.setStatus("mandatory")
_BrpsWLanTransmitLevel_Type = Integer32
_BrpsWLanTransmitLevel_Object = MibScalar
brpsWLanTransmitLevel = _BrpsWLanTransmitLevel_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 2, 2),
    _BrpsWLanTransmitLevel_Type()
)
brpsWLanTransmitLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanTransmitLevel.setStatus("mandatory")
_BrpsPit3WLanTestStatus_Type = Integer32
_BrpsPit3WLanTestStatus_Object = MibScalar
brpsPit3WLanTestStatus = _BrpsPit3WLanTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 2, 3),
    _BrpsPit3WLanTestStatus_Type()
)
brpsPit3WLanTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsPit3WLanTestStatus.setStatus("mandatory")
_WlNetSearch_ObjectIdentity = ObjectIdentity
wlNetSearch = _WlNetSearch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 11)
)
_BrpsWLanNetSearchSupported_Type = Integer32
_BrpsWLanNetSearchSupported_Object = MibScalar
brpsWLanNetSearchSupported = _BrpsWLanNetSearchSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 11, 1),
    _BrpsWLanNetSearchSupported_Type()
)
brpsWLanNetSearchSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanNetSearchSupported.setStatus("mandatory")
_BrpsAvailableWLanScan_Type = OctetString
_BrpsAvailableWLanScan_Object = MibScalar
brpsAvailableWLanScan = _BrpsAvailableWLanScan_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 11, 2),
    _BrpsAvailableWLanScan_Type()
)
brpsAvailableWLanScan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsAvailableWLanScan.setStatus("mandatory")
_BrpsAvailableWLanScanWaitTime_Type = Integer32
_BrpsAvailableWLanScanWaitTime_Object = MibScalar
brpsAvailableWLanScanWaitTime = _BrpsAvailableWLanScanWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 11, 3),
    _BrpsAvailableWLanScanWaitTime_Type()
)
brpsAvailableWLanScanWaitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsAvailableWLanScanWaitTime.setStatus("mandatory")
_BrpsAvailableWLanCount_Type = Integer32
_BrpsAvailableWLanCount_Object = MibScalar
brpsAvailableWLanCount = _BrpsAvailableWLanCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 11, 10),
    _BrpsAvailableWLanCount_Type()
)
brpsAvailableWLanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsAvailableWLanCount.setStatus("mandatory")
_BrpsAvailableWLanTable_Object = MibTable
brpsAvailableWLanTable = _BrpsAvailableWLanTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 11, 11)
)
if mibBuilder.loadTexts:
    brpsAvailableWLanTable.setStatus("mandatory")
_BrpsAvailableWLanEntry_Object = MibTableRow
brpsAvailableWLanEntry = _BrpsAvailableWLanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 11, 11, 1)
)
brpsAvailableWLanEntry.setIndexNames(
    (0, "BROTHER-MIB", "brpsAvailableWLanIndex"),
)
if mibBuilder.loadTexts:
    brpsAvailableWLanEntry.setStatus("mandatory")


class _BrpsAvailableWLanIndex_Type(Integer32):
    """Custom type brpsAvailableWLanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BrpsAvailableWLanIndex_Type.__name__ = "Integer32"
_BrpsAvailableWLanIndex_Object = MibTableColumn
brpsAvailableWLanIndex = _BrpsAvailableWLanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 11, 11, 1, 1),
    _BrpsAvailableWLanIndex_Type()
)
brpsAvailableWLanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsAvailableWLanIndex.setStatus("mandatory")


class _BrpsAvailableWLanName_Type(OctetString):
    """Custom type brpsAvailableWLanName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrpsAvailableWLanName_Type.__name__ = "OctetString"
_BrpsAvailableWLanName_Object = MibTableColumn
brpsAvailableWLanName = _BrpsAvailableWLanName_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 11, 11, 1, 2),
    _BrpsAvailableWLanName_Type()
)
brpsAvailableWLanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsAvailableWLanName.setStatus("mandatory")


class _BrpsAvailableWLanMode_Type(Integer32):
    """Custom type brpsAvailableWLanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot11b", 2),
          ("dot11b-gAuto", 1),
          ("dot11g", 3))
    )


_BrpsAvailableWLanMode_Type.__name__ = "Integer32"
_BrpsAvailableWLanMode_Object = MibTableColumn
brpsAvailableWLanMode = _BrpsAvailableWLanMode_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 11, 11, 1, 3),
    _BrpsAvailableWLanMode_Type()
)
brpsAvailableWLanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsAvailableWLanMode.setStatus("mandatory")


class _BrpsAvailableWLanCommMode_Type(Integer32):
    """Custom type brpsAvailableWLanCommMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accesPoint", 1),
          ("adhoc-Wi-Fi", 2))
    )


_BrpsAvailableWLanCommMode_Type.__name__ = "Integer32"
_BrpsAvailableWLanCommMode_Object = MibTableColumn
brpsAvailableWLanCommMode = _BrpsAvailableWLanCommMode_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 11, 11, 1, 4),
    _BrpsAvailableWLanCommMode_Type()
)
brpsAvailableWLanCommMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsAvailableWLanCommMode.setStatus("mandatory")
_BrpsAvailableWLanChannel_Type = Integer32
_BrpsAvailableWLanChannel_Object = MibTableColumn
brpsAvailableWLanChannel = _BrpsAvailableWLanChannel_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 11, 11, 1, 5),
    _BrpsAvailableWLanChannel_Type()
)
brpsAvailableWLanChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsAvailableWLanChannel.setStatus("mandatory")
_BrpsAvailableWLanPowerLevel_Type = Integer32
_BrpsAvailableWLanPowerLevel_Object = MibTableColumn
brpsAvailableWLanPowerLevel = _BrpsAvailableWLanPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 11, 11, 1, 6),
    _BrpsAvailableWLanPowerLevel_Type()
)
brpsAvailableWLanPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsAvailableWLanPowerLevel.setStatus("mandatory")


class _BrpsAvailableWLanAuthMode_Type(Integer32):
    """Custom type brpsAvailableWLanAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("none", 1))
    )


_BrpsAvailableWLanAuthMode_Type.__name__ = "Integer32"
_BrpsAvailableWLanAuthMode_Object = MibTableColumn
brpsAvailableWLanAuthMode = _BrpsAvailableWLanAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 11, 11, 1, 7),
    _BrpsAvailableWLanAuthMode_Type()
)
brpsAvailableWLanAuthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsAvailableWLanAuthMode.setStatus("mandatory")


class _BrpsAvailableWLanEncryptMode_Type(Integer32):
    """Custom type brpsAvailableWLanEncryptMode based on Integer32"""
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
        *(("active", 2),
          ("none", 1),
          ("tkip", 4),
          ("wep", 3))
    )


_BrpsAvailableWLanEncryptMode_Type.__name__ = "Integer32"
_BrpsAvailableWLanEncryptMode_Object = MibTableColumn
brpsAvailableWLanEncryptMode = _BrpsAvailableWLanEncryptMode_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 11, 11, 1, 8),
    _BrpsAvailableWLanEncryptMode_Type()
)
brpsAvailableWLanEncryptMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsAvailableWLanEncryptMode.setStatus("mandatory")
_WlAOSS_ObjectIdentity = ObjectIdentity
wlAOSS = _WlAOSS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 12)
)


class _BrpsWLanAOSSSupported_Type(Integer32):
    """Custom type brpsWLanAOSSSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsWLanAOSSSupported_Type.__name__ = "Integer32"
_BrpsWLanAOSSSupported_Object = MibScalar
brpsWLanAOSSSupported = _BrpsWLanAOSSSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 12, 1),
    _BrpsWLanAOSSSupported_Type()
)
brpsWLanAOSSSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanAOSSSupported.setStatus("mandatory")


class _BrpsWLanAOSSIsRunnning_Type(Integer32):
    """Custom type brpsWLanAOSSIsRunnning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsWLanAOSSIsRunnning_Type.__name__ = "Integer32"
_BrpsWLanAOSSIsRunnning_Object = MibScalar
brpsWLanAOSSIsRunnning = _BrpsWLanAOSSIsRunnning_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 12, 2),
    _BrpsWLanAOSSIsRunnning_Type()
)
brpsWLanAOSSIsRunnning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanAOSSIsRunnning.setStatus("mandatory")
_WlSES_ObjectIdentity = ObjectIdentity
wlSES = _WlSES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 13)
)


class _BrpsWLanSESSupported_Type(Integer32):
    """Custom type brpsWLanSESSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsWLanSESSupported_Type.__name__ = "Integer32"
_BrpsWLanSESSupported_Object = MibScalar
brpsWLanSESSupported = _BrpsWLanSESSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 13, 1),
    _BrpsWLanSESSupported_Type()
)
brpsWLanSESSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanSESSupported.setStatus("mandatory")
_WlWPS_ObjectIdentity = ObjectIdentity
wlWPS = _WlWPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 14)
)


class _BrpsWLanWPSSupported_Type(Integer32):
    """Custom type brpsWLanWPSSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsWLanWPSSupported_Type.__name__ = "Integer32"
_BrpsWLanWPSSupported_Object = MibScalar
brpsWLanWPSSupported = _BrpsWLanWPSSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 14, 1),
    _BrpsWLanWPSSupported_Type()
)
brpsWLanWPSSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanWPSSupported.setStatus("mandatory")


class _BrpsWLanWPSResult_Type(Integer32):
    """Custom type brpsWLanWPSResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1),
    )


_BrpsWLanWPSResult_Type.__name__ = "Integer32"
_BrpsWLanWPSResult_Object = MibScalar
brpsWLanWPSResult = _BrpsWLanWPSResult_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 14, 2),
    _BrpsWLanWPSResult_Type()
)
brpsWLanWPSResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanWPSResult.setStatus("mandatory")
_WlSimpleWizard_ObjectIdentity = ObjectIdentity
wlSimpleWizard = _WlSimpleWizard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 15)
)


class _BrWlanSimpleWizardSupported_Type(Integer32):
    """Custom type brWlanSimpleWizardSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrWlanSimpleWizardSupported_Type.__name__ = "Integer32"
_BrWlanSimpleWizardSupported_Object = MibScalar
brWlanSimpleWizardSupported = _BrWlanSimpleWizardSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 15, 1),
    _BrWlanSimpleWizardSupported_Type()
)
brWlanSimpleWizardSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brWlanSimpleWizardSupported.setStatus("mandatory")


class _BrWlanSimpleWizardPassword_Type(OctetString):
    """Custom type brWlanSimpleWizardPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BrWlanSimpleWizardPassword_Type.__name__ = "OctetString"
_BrWlanSimpleWizardPassword_Object = MibScalar
brWlanSimpleWizardPassword = _BrWlanSimpleWizardPassword_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 1, 15, 2),
    _BrWlanSimpleWizardPassword_Type()
)
brWlanSimpleWizardPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brWlanSimpleWizardPassword.setStatus("mandatory")
_WlSetup_ObjectIdentity = ObjectIdentity
wlSetup = _WlSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11)
)
_WlGeneral_ObjectIdentity = ObjectIdentity
wlGeneral = _WlGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 1)
)


class _BrpsWLanAPSetupMode_Type(Integer32):
    """Custom type brpsWLanAPSetupMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_BrpsWLanAPSetupMode_Type.__name__ = "Integer32"
_BrpsWLanAPSetupMode_Object = MibScalar
brpsWLanAPSetupMode = _BrpsWLanAPSetupMode_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 1, 1),
    _BrpsWLanAPSetupMode_Type()
)
brpsWLanAPSetupMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanAPSetupMode.setStatus("mandatory")


class _BrpsWLanMode_Type(Integer32):
    """Custom type brpsWLanMode based on Integer32"""
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
        *(("dot11b", 2),
          ("dot11b-gAuto", 1),
          ("dot11g", 3),
          ("dot11g-turbo", 4))
    )


_BrpsWLanMode_Type.__name__ = "Integer32"
_BrpsWLanMode_Object = MibScalar
brpsWLanMode = _BrpsWLanMode_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 1, 2),
    _BrpsWLanMode_Type()
)
brpsWLanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsWLanMode.setStatus("mandatory")


class _BrpsWLanName_Type(OctetString):
    """Custom type brpsWLanName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrpsWLanName_Type.__name__ = "OctetString"
_BrpsWLanName_Object = MibScalar
brpsWLanName = _BrpsWLanName_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 1, 3),
    _BrpsWLanName_Type()
)
brpsWLanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsWLanName.setStatus("mandatory")


class _BrpsWLanCommMode_Type(Integer32):
    """Custom type brpsWLanCommMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ad-Hoc", 3),
          ("ad-Hoc-WiFi", 2),
          ("infrastructure", 1))
    )


_BrpsWLanCommMode_Type.__name__ = "Integer32"
_BrpsWLanCommMode_Object = MibScalar
brpsWLanCommMode = _BrpsWLanCommMode_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 1, 4),
    _BrpsWLanCommMode_Type()
)
brpsWLanCommMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsWLanCommMode.setStatus("mandatory")
_BrpsWLanChannel_Type = Integer32
_BrpsWLanChannel_Object = MibScalar
brpsWLanChannel = _BrpsWLanChannel_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 1, 5),
    _BrpsWLanChannel_Type()
)
brpsWLanChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsWLanChannel.setStatus("mandatory")
_WlAdvanced_ObjectIdentity = ObjectIdentity
wlAdvanced = _WlAdvanced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 5)
)


class _BrpsWLanCtsMode_Type(Integer32):
    """Custom type brpsWLanCtsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("always", 2),
          ("auto", 1),
          ("none", 3))
    )


_BrpsWLanCtsMode_Type.__name__ = "Integer32"
_BrpsWLanCtsMode_Object = MibScalar
brpsWLanCtsMode = _BrpsWLanCtsMode_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 5, 1),
    _BrpsWLanCtsMode_Type()
)
brpsWLanCtsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsWLanCtsMode.setStatus("mandatory")


class _BrpsWLanCtsRate_Type(Integer32):
    """Custom type brpsWLanCtsRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_BrpsWLanCtsRate_Type.__name__ = "Integer32"
_BrpsWLanCtsRate_Object = MibScalar
brpsWLanCtsRate = _BrpsWLanCtsRate_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 5, 2),
    _BrpsWLanCtsRate_Type()
)
brpsWLanCtsRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsWLanCtsRate.setStatus("mandatory")


class _BrpsWLanCtsType_Type(Integer32):
    """Custom type brpsWLanCtsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("only", 1),
          ("rts-cts", 2))
    )


_BrpsWLanCtsType_Type.__name__ = "Integer32"
_BrpsWLanCtsType_Object = MibScalar
brpsWLanCtsType = _BrpsWLanCtsType_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 5, 3),
    _BrpsWLanCtsType_Type()
)
brpsWLanCtsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsWLanCtsType.setStatus("mandatory")


class _BrpsWLanRtsCtsThreshold_Type(Integer32):
    """Custom type brpsWLanRtsCtsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2346),
    )


_BrpsWLanRtsCtsThreshold_Type.__name__ = "Integer32"
_BrpsWLanRtsCtsThreshold_Object = MibScalar
brpsWLanRtsCtsThreshold = _BrpsWLanRtsCtsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 5, 4),
    _BrpsWLanRtsCtsThreshold_Type()
)
brpsWLanRtsCtsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsWLanRtsCtsThreshold.setStatus("mandatory")


class _BrpsWLanLengthThreshold_Type(Integer32):
    """Custom type brpsWLanLengthThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2346),
    )


_BrpsWLanLengthThreshold_Type.__name__ = "Integer32"
_BrpsWLanLengthThreshold_Object = MibScalar
brpsWLanLengthThreshold = _BrpsWLanLengthThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 5, 5),
    _BrpsWLanLengthThreshold_Type()
)
brpsWLanLengthThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsWLanLengthThreshold.setStatus("mandatory")


class _BrpsWLanDataRetry_Type(Integer32):
    """Custom type brpsWLanDataRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_BrpsWLanDataRetry_Type.__name__ = "Integer32"
_BrpsWLanDataRetry_Object = MibScalar
brpsWLanDataRetry = _BrpsWLanDataRetry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 5, 6),
    _BrpsWLanDataRetry_Type()
)
brpsWLanDataRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsWLanDataRetry.setStatus("mandatory")


class _BrpsWLanTransmitPowerSetting_Type(Integer32):
    """Custom type brpsWLanTransmitPowerSetting based on Integer32"""
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
        *(("full", 1),
          ("half", 2),
          ("minimum", 5),
          ("off", 6),
          ("one-eighth", 4),
          ("quarter", 3))
    )


_BrpsWLanTransmitPowerSetting_Type.__name__ = "Integer32"
_BrpsWLanTransmitPowerSetting_Object = MibScalar
brpsWLanTransmitPowerSetting = _BrpsWLanTransmitPowerSetting_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 5, 7),
    _BrpsWLanTransmitPowerSetting_Type()
)
brpsWLanTransmitPowerSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsWLanTransmitPowerSetting.setStatus("mandatory")


class _BrpsWLanDeviceType_Type(Integer32):
    """Custom type brpsWLanDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accessPointMode", 2),
          ("stationMode", 1))
    )


_BrpsWLanDeviceType_Type.__name__ = "Integer32"
_BrpsWLanDeviceType_Object = MibScalar
brpsWLanDeviceType = _BrpsWLanDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 5, 8),
    _BrpsWLanDeviceType_Type()
)
brpsWLanDeviceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsWLanDeviceType.setStatus("mandatory")
_WlAssociate_ObjectIdentity = ObjectIdentity
wlAssociate = _WlAssociate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 11)
)


class _BrpsWLanEncryptMode_Type(Integer32):
    """Custom type brpsWLanEncryptMode based on Integer32"""
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
        *(("aes", 4),
          ("none", 1),
          ("tkip", 3),
          ("wep", 2))
    )


_BrpsWLanEncryptMode_Type.__name__ = "Integer32"
_BrpsWLanEncryptMode_Object = MibScalar
brpsWLanEncryptMode = _BrpsWLanEncryptMode_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 11, 1),
    _BrpsWLanEncryptMode_Type()
)
brpsWLanEncryptMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsWLanEncryptMode.setStatus("mandatory")


class _BrpsWLanAuthMode_Type(Integer32):
    """Custom type brpsWLanAuthMode based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("eapfast-gtc", 10),
          ("eapfast-mschapv2", 9),
          ("eapfast-none", 8),
          ("eapfast-tls", 11),
          ("leap", 7),
          ("openSystem", 1),
          ("sharedKey", 2),
          ("wpa", 5),
          ("wpa-none", 4),
          ("wpa-psk", 3),
          ("wpa2", 6),
          ("wpa2-psk", 12))
    )


_BrpsWLanAuthMode_Type.__name__ = "Integer32"
_BrpsWLanAuthMode_Object = MibScalar
brpsWLanAuthMode = _BrpsWLanAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 11, 11),
    _BrpsWLanAuthMode_Type()
)
brpsWLanAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsWLanAuthMode.setStatus("mandatory")


class _BrpsWLanAuthEAP_Type(Integer32):
    """Custom type brpsWLanAuthEAP based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("eapMD5", 1),
          ("eapTLS", 2),
          ("eapTTLS", 3),
          ("eapfast-gtc", 8),
          ("eapfast-mschapv2", 7),
          ("eapfast-none", 6),
          ("eapfast-tls", 9),
          ("leap", 5),
          ("peap", 4))
    )


_BrpsWLanAuthEAP_Type.__name__ = "Integer32"
_BrpsWLanAuthEAP_Object = MibScalar
brpsWLanAuthEAP = _BrpsWLanAuthEAP_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 11, 12),
    _BrpsWLanAuthEAP_Type()
)
brpsWLanAuthEAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsWLanAuthEAP.setStatus("mandatory")


class _BrpsWLanAuthUserID_Type(OctetString):
    """Custom type brpsWLanAuthUserID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrpsWLanAuthUserID_Type.__name__ = "OctetString"
_BrpsWLanAuthUserID_Object = MibScalar
brpsWLanAuthUserID = _BrpsWLanAuthUserID_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 11, 13),
    _BrpsWLanAuthUserID_Type()
)
brpsWLanAuthUserID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsWLanAuthUserID.setStatus("mandatory")


class _BrpsWLanAuthUserPass_Type(OctetString):
    """Custom type brpsWLanAuthUserPass based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrpsWLanAuthUserPass_Type.__name__ = "OctetString"
_BrpsWLanAuthUserPass_Object = MibScalar
brpsWLanAuthUserPass = _BrpsWLanAuthUserPass_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 11, 14),
    _BrpsWLanAuthUserPass_Type()
)
brpsWLanAuthUserPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsWLanAuthUserPass.setStatus("mandatory")


class _BrpsWLanAssociate_Type(Integer32):
    """Custom type brpsWLanAssociate based on Integer32"""
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
        *(("applyonly", 4),
          ("print", 2),
          ("simplewizard", 5),
          ("test", 3),
          ("update", 1))
    )


_BrpsWLanAssociate_Type.__name__ = "Integer32"
_BrpsWLanAssociate_Object = MibScalar
brpsWLanAssociate = _BrpsWLanAssociate_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 11, 21),
    _BrpsWLanAssociate_Type()
)
brpsWLanAssociate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsWLanAssociate.setStatus("mandatory")


class _BrpsWLanAssociateTestResult_Type(Integer32):
    """Custom type brpsWLanAssociateTestResult based on Integer32"""
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
        *(("invalidAuthUserID", 4),
          ("invalidAuthUserPass", 5),
          ("invalidWLanNetKey", 3),
          ("linkOK", 1),
          ("noSuchWLan", 2))
    )


_BrpsWLanAssociateTestResult_Type.__name__ = "Integer32"
_BrpsWLanAssociateTestResult_Object = MibScalar
brpsWLanAssociateTestResult = _BrpsWLanAssociateTestResult_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 11, 22),
    _BrpsWLanAssociateTestResult_Type()
)
brpsWLanAssociateTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanAssociateTestResult.setStatus("mandatory")


class _BrpsWLanAssociateResult_Type(Integer32):
    """Custom type brpsWLanAssociateResult based on Integer32"""
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
        *(("invalidAuthUserID", 4),
          ("invalidAuthUserPass", 5),
          ("invalidWLanNetKey", 3),
          ("linkOK", 1),
          ("noSuchWLan", 2))
    )


_BrpsWLanAssociateResult_Type.__name__ = "Integer32"
_BrpsWLanAssociateResult_Object = MibScalar
brpsWLanAssociateResult = _BrpsWLanAssociateResult_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 11, 23),
    _BrpsWLanAssociateResult_Type()
)
brpsWLanAssociateResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanAssociateResult.setStatus("mandatory")
_BrpsWLanAssociateTestSupported_Type = Integer32
_BrpsWLanAssociateTestSupported_Object = MibScalar
brpsWLanAssociateTestSupported = _BrpsWLanAssociateTestSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 11, 24),
    _BrpsWLanAssociateTestSupported_Type()
)
brpsWLanAssociateTestSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanAssociateTestSupported.setStatus("mandatory")
_WlWEP_ObjectIdentity = ObjectIdentity
wlWEP = _WlWEP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 11, 101)
)
_BrpsWLanWepKeyDefaultIndex_Type = Integer32
_BrpsWLanWepKeyDefaultIndex_Object = MibScalar
brpsWLanWepKeyDefaultIndex = _BrpsWLanWepKeyDefaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 11, 101, 1),
    _BrpsWLanWepKeyDefaultIndex_Type()
)
brpsWLanWepKeyDefaultIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsWLanWepKeyDefaultIndex.setStatus("mandatory")
_BrpsWLanWepKeyTable_Object = MibTable
brpsWLanWepKeyTable = _BrpsWLanWepKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 11, 101, 11)
)
if mibBuilder.loadTexts:
    brpsWLanWepKeyTable.setStatus("mandatory")
_BrpsWLanWepKeyEntry_Object = MibTableRow
brpsWLanWepKeyEntry = _BrpsWLanWepKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 11, 101, 11, 1)
)
brpsWLanWepKeyEntry.setIndexNames(
    (0, "BROTHER-MIB", "brpsWLanWepKeyIndex"),
)
if mibBuilder.loadTexts:
    brpsWLanWepKeyEntry.setStatus("mandatory")


class _BrpsWLanWepKeyIndex_Type(Integer32):
    """Custom type brpsWLanWepKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BrpsWLanWepKeyIndex_Type.__name__ = "Integer32"
_BrpsWLanWepKeyIndex_Object = MibTableColumn
brpsWLanWepKeyIndex = _BrpsWLanWepKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 11, 101, 11, 1, 1),
    _BrpsWLanWepKeyIndex_Type()
)
brpsWLanWepKeyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanWepKeyIndex.setStatus("mandatory")


class _BrpsWLanWepKeySize_Type(Integer32):
    """Custom type brpsWLanWepKeySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("size104", 2),
          ("size40", 1))
    )


_BrpsWLanWepKeySize_Type.__name__ = "Integer32"
_BrpsWLanWepKeySize_Object = MibTableColumn
brpsWLanWepKeySize = _BrpsWLanWepKeySize_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 11, 101, 11, 1, 2),
    _BrpsWLanWepKeySize_Type()
)
brpsWLanWepKeySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsWLanWepKeySize.setStatus("mandatory")


class _BrpsWLanWepKeyType_Type(Integer32):
    """Custom type brpsWLanWepKeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 2),
          ("hex", 1))
    )


_BrpsWLanWepKeyType_Type.__name__ = "Integer32"
_BrpsWLanWepKeyType_Object = MibTableColumn
brpsWLanWepKeyType = _BrpsWLanWepKeyType_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 11, 101, 11, 1, 3),
    _BrpsWLanWepKeyType_Type()
)
brpsWLanWepKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsWLanWepKeyType.setStatus("mandatory")
_BrpsWLanWepKey_Type = OctetString
_BrpsWLanWepKey_Object = MibTableColumn
brpsWLanWepKey = _BrpsWLanWepKey_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 11, 101, 11, 1, 4),
    _BrpsWLanWepKey_Type()
)
brpsWLanWepKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsWLanWepKey.setStatus("mandatory")
_WlWPA_ObjectIdentity = ObjectIdentity
wlWPA = _WlWPA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 11, 102)
)
_BrpsWLanNetworkKey_Type = OctetString
_BrpsWLanNetworkKey_Object = MibScalar
brpsWLanNetworkKey = _BrpsWLanNetworkKey_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 11, 102, 1),
    _BrpsWLanNetworkKey_Type()
)
brpsWLanNetworkKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsWLanNetworkKey.setStatus("mandatory")
_WlTKIP_ObjectIdentity = ObjectIdentity
wlTKIP = _WlTKIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 11, 103)
)
_BrpsWLanTKIPChangeInterval_Type = Integer32
_BrpsWLanTKIPChangeInterval_Object = MibScalar
brpsWLanTKIPChangeInterval = _BrpsWLanTKIPChangeInterval_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 11, 103, 1),
    _BrpsWLanTKIPChangeInterval_Type()
)
brpsWLanTKIPChangeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsWLanTKIPChangeInterval.setStatus("mandatory")
_WlLEAP_ObjectIdentity = ObjectIdentity
wlLEAP = _WlLEAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 11, 104)
)
_BrpsWLanLEAPTimeout_Type = Integer32
_BrpsWLanLEAPTimeout_Object = MibScalar
brpsWLanLEAPTimeout = _BrpsWLanLEAPTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 11, 11, 104, 1),
    _BrpsWLanLEAPTimeout_Type()
)
brpsWLanLEAPTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsWLanLEAPTimeout.setStatus("mandatory")
_WlStatus_ObjectIdentity = ObjectIdentity
wlStatus = _WlStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 21)
)
_WlGeneralStatus_ObjectIdentity = ObjectIdentity
wlGeneralStatus = _WlGeneralStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 21, 1)
)
_BrpsWLanOperatingMode_Type = Integer32
_BrpsWLanOperatingMode_Object = MibScalar
brpsWLanOperatingMode = _BrpsWLanOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 21, 1, 1),
    _BrpsWLanOperatingMode_Type()
)
brpsWLanOperatingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanOperatingMode.setStatus("mandatory")


class _BrpsWLanRSSLevel_Type(Integer32):
    """Custom type brpsWLanRSSLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_BrpsWLanRSSLevel_Type.__name__ = "Integer32"
_BrpsWLanRSSLevel_Object = MibScalar
brpsWLanRSSLevel = _BrpsWLanRSSLevel_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 21, 1, 2),
    _BrpsWLanRSSLevel_Type()
)
brpsWLanRSSLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanRSSLevel.setStatus("mandatory")


class _BrpsWLanCommSpeed_Type(Integer32):
    """Custom type brpsWLanCommSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_BrpsWLanCommSpeed_Type.__name__ = "Integer32"
_BrpsWLanCommSpeed_Object = MibScalar
brpsWLanCommSpeed = _BrpsWLanCommSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 21, 1, 3),
    _BrpsWLanCommSpeed_Type()
)
brpsWLanCommSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanCommSpeed.setStatus("mandatory")
_BrpsWLanOperatingChannel_Type = Integer32
_BrpsWLanOperatingChannel_Object = MibScalar
brpsWLanOperatingChannel = _BrpsWLanOperatingChannel_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 21, 1, 4),
    _BrpsWLanOperatingChannel_Type()
)
brpsWLanOperatingChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanOperatingChannel.setStatus("mandatory")
_BrpsWLanOperatingName_Type = OctetString
_BrpsWLanOperatingName_Object = MibScalar
brpsWLanOperatingName = _BrpsWLanOperatingName_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 21, 1, 5),
    _BrpsWLanOperatingName_Type()
)
brpsWLanOperatingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanOperatingName.setStatus("mandatory")
_BrpsWLanOperatingCommMode_Type = Integer32
_BrpsWLanOperatingCommMode_Object = MibScalar
brpsWLanOperatingCommMode = _BrpsWLanOperatingCommMode_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 21, 1, 6),
    _BrpsWLanOperatingCommMode_Type()
)
brpsWLanOperatingCommMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanOperatingCommMode.setStatus("mandatory")
_BrpsWLanOperatingEncryptMode_Type = Integer32
_BrpsWLanOperatingEncryptMode_Object = MibScalar
brpsWLanOperatingEncryptMode = _BrpsWLanOperatingEncryptMode_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 21, 1, 7),
    _BrpsWLanOperatingEncryptMode_Type()
)
brpsWLanOperatingEncryptMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanOperatingEncryptMode.setStatus("mandatory")
_BrpsWLanOperatingAuthMode_Type = Integer32
_BrpsWLanOperatingAuthMode_Object = MibScalar
brpsWLanOperatingAuthMode = _BrpsWLanOperatingAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 21, 1, 8),
    _BrpsWLanOperatingAuthMode_Type()
)
brpsWLanOperatingAuthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanOperatingAuthMode.setStatus("mandatory")
_BrpsWLanOperatingWepKeyDefaultIndex_Type = Integer32
_BrpsWLanOperatingWepKeyDefaultIndex_Object = MibScalar
brpsWLanOperatingWepKeyDefaultIndex = _BrpsWLanOperatingWepKeyDefaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 100, 21, 1, 9),
    _BrpsWLanOperatingWepKeyDefaultIndex_Type()
)
brpsWLanOperatingWepKeyDefaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsWLanOperatingWepKeyDefaultIndex.setStatus("mandatory")
_BrnetConfig_ObjectIdentity = ObjectIdentity
brnetConfig = _BrnetConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240)
)
_Brconfig_ObjectIdentity = ObjectIdentity
brconfig = _Brconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 1)
)


class _BrpsNodeName_Type(DisplayString):
    """Custom type brpsNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrpsNodeName_Type.__name__ = "DisplayString"
_BrpsNodeName_Object = MibScalar
brpsNodeName = _BrpsNodeName_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 1, 1),
    _BrpsNodeName_Type()
)
brpsNodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsNodeName.setStatus("mandatory")


class _BrpsSerialNumber_Type(DisplayString):
    """Custom type brpsSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrpsSerialNumber_Type.__name__ = "DisplayString"
_BrpsSerialNumber_Object = MibScalar
brpsSerialNumber = _BrpsSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 1, 2),
    _BrpsSerialNumber_Type()
)
brpsSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsSerialNumber.setStatus("mandatory")


class _BrpsHardwareType_Type(Integer32):
    """Custom type brpsHardwareType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_BrpsHardwareType_Type.__name__ = "Integer32"
_BrpsHardwareType_Object = MibScalar
brpsHardwareType = _BrpsHardwareType_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 1, 3),
    _BrpsHardwareType_Type()
)
brpsHardwareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsHardwareType.setStatus("mandatory")


class _BrpsMainRevision_Type(DisplayString):
    """Custom type brpsMainRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_BrpsMainRevision_Type.__name__ = "DisplayString"
_BrpsMainRevision_Object = MibScalar
brpsMainRevision = _BrpsMainRevision_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 1, 4),
    _BrpsMainRevision_Type()
)
brpsMainRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsMainRevision.setStatus("mandatory")


class _BrpsBootRevision_Type(DisplayString):
    """Custom type brpsBootRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_BrpsBootRevision_Type.__name__ = "DisplayString"
_BrpsBootRevision_Object = MibScalar
brpsBootRevision = _BrpsBootRevision_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 1, 5),
    _BrpsBootRevision_Type()
)
brpsBootRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsBootRevision.setStatus("mandatory")
_BrpsPasswordVerify_Type = DisplayString
_BrpsPasswordVerify_Object = MibScalar
brpsPasswordVerify = _BrpsPasswordVerify_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 1, 6),
    _BrpsPasswordVerify_Type()
)
brpsPasswordVerify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsPasswordVerify.setStatus("mandatory")
_BrpsPassword_Type = DisplayString
_BrpsPassword_Object = MibScalar
brpsPassword = _BrpsPassword_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 1, 7),
    _BrpsPassword_Type()
)
brpsPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsPassword.setStatus("mandatory")


class _BrpsMIBVersion_Type(DisplayString):
    """Custom type brpsMIBVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_BrpsMIBVersion_Type.__name__ = "DisplayString"
_BrpsMIBVersion_Object = MibScalar
brpsMIBVersion = _BrpsMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 1, 8),
    _BrpsMIBVersion_Type()
)
brpsMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsMIBVersion.setStatus("mandatory")


class _BrpsOEMString_Type(DisplayString):
    """Custom type brpsOEMString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_BrpsOEMString_Type.__name__ = "DisplayString"
_BrpsOEMString_Object = MibScalar
brpsOEMString = _BrpsOEMString_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 1, 9),
    _BrpsOEMString_Type()
)
brpsOEMString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsOEMString.setStatus("mandatory")


class _BrpsMIBMajor_Type(Integer32):
    """Custom type brpsMIBMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_BrpsMIBMajor_Type.__name__ = "Integer32"
_BrpsMIBMajor_Object = MibScalar
brpsMIBMajor = _BrpsMIBMajor_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 1, 10),
    _BrpsMIBMajor_Type()
)
brpsMIBMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsMIBMajor.setStatus("mandatory")


class _BrpsMIBMinor_Type(Integer32):
    """Custom type brpsMIBMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_BrpsMIBMinor_Type.__name__ = "Integer32"
_BrpsMIBMinor_Object = MibScalar
brpsMIBMinor = _BrpsMIBMinor_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 1, 11),
    _BrpsMIBMinor_Type()
)
brpsMIBMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsMIBMinor.setStatus("mandatory")


class _BrpsServerDescription_Type(DisplayString):
    """Custom type brpsServerDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrpsServerDescription_Type.__name__ = "DisplayString"
_BrpsServerDescription_Object = MibScalar
brpsServerDescription = _BrpsServerDescription_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 1, 12),
    _BrpsServerDescription_Type()
)
brpsServerDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsServerDescription.setStatus("mandatory")


class _BrpsEnetMode_Type(Integer32):
    """Custom type brpsEnetMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_BrpsEnetMode_Type.__name__ = "Integer32"
_BrpsEnetMode_Object = MibScalar
brpsEnetMode = _BrpsEnetMode_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 1, 13),
    _BrpsEnetMode_Type()
)
brpsEnetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsEnetMode.setStatus("mandatory")


class _BrpsFlashROMSize_Type(Integer32):
    """Custom type brpsFlashROMSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrpsFlashROMSize_Type.__name__ = "Integer32"
_BrpsFlashROMSize_Object = MibScalar
brpsFlashROMSize = _BrpsFlashROMSize_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 1, 14),
    _BrpsFlashROMSize_Type()
)
brpsFlashROMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsFlashROMSize.setStatus("mandatory")


class _BrpsSNMPGetCommunity_Type(DisplayString):
    """Custom type brpsSNMPGetCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrpsSNMPGetCommunity_Type.__name__ = "DisplayString"
_BrpsSNMPGetCommunity_Object = MibScalar
brpsSNMPGetCommunity = _BrpsSNMPGetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 1, 15),
    _BrpsSNMPGetCommunity_Type()
)
brpsSNMPGetCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsSNMPGetCommunity.setStatus("mandatory")


class _BrpsSNMPJetAdmin_Type(Integer32):
    """Custom type brpsSNMPJetAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsSNMPJetAdmin_Type.__name__ = "Integer32"
_BrpsSNMPJetAdmin_Object = MibScalar
brpsSNMPJetAdmin = _BrpsSNMPJetAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 1, 16),
    _BrpsSNMPJetAdmin_Type()
)
brpsSNMPJetAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsSNMPJetAdmin.setStatus("mandatory")


class _BrpsSNMPSetCommunity1_Type(DisplayString):
    """Custom type brpsSNMPSetCommunity1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrpsSNMPSetCommunity1_Type.__name__ = "DisplayString"
_BrpsSNMPSetCommunity1_Object = MibScalar
brpsSNMPSetCommunity1 = _BrpsSNMPSetCommunity1_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 1, 17),
    _BrpsSNMPSetCommunity1_Type()
)
brpsSNMPSetCommunity1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsSNMPSetCommunity1.setStatus("mandatory")


class _BrpsSNMPSetCommunity2_Type(DisplayString):
    """Custom type brpsSNMPSetCommunity2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrpsSNMPSetCommunity2_Type.__name__ = "DisplayString"
_BrpsSNMPSetCommunity2_Object = MibScalar
brpsSNMPSetCommunity2 = _BrpsSNMPSetCommunity2_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 1, 18),
    _BrpsSNMPSetCommunity2_Type()
)
brpsSNMPSetCommunity2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsSNMPSetCommunity2.setStatus("mandatory")


class _BrSupportedInfo_Type(OctetString):
    """Custom type brSupportedInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BrSupportedInfo_Type.__name__ = "OctetString"
_BrSupportedInfo_Object = MibScalar
brSupportedInfo = _BrSupportedInfo_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 1, 200),
    _BrSupportedInfo_Type()
)
brSupportedInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brSupportedInfo.setStatus("mandatory")
_Brcontrol_ObjectIdentity = ObjectIdentity
brcontrol = _Brcontrol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 2)
)


class _BrpsTestPage_Type(Integer32):
    """Custom type brpsTestPage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_BrpsTestPage_Type.__name__ = "Integer32"
_BrpsTestPage_Object = MibScalar
brpsTestPage = _BrpsTestPage_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 2, 1),
    _BrpsTestPage_Type()
)
brpsTestPage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsTestPage.setStatus("mandatory")


class _BrpsSetDefault_Type(Integer32):
    """Custom type brpsSetDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_BrpsSetDefault_Type.__name__ = "Integer32"
_BrpsSetDefault_Object = MibScalar
brpsSetDefault = _BrpsSetDefault_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 2, 2),
    _BrpsSetDefault_Type()
)
brpsSetDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsSetDefault.setStatus("mandatory")


class _BrpsReset_Type(Integer32):
    """Custom type brpsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_BrpsReset_Type.__name__ = "Integer32"
_BrpsReset_Object = MibScalar
brpsReset = _BrpsReset_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 2, 3),
    _BrpsReset_Type()
)
brpsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsReset.setStatus("mandatory")


class _BrpsProtectModeEnable_Type(Integer32):
    """Custom type brpsProtectModeEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsProtectModeEnable_Type.__name__ = "Integer32"
_BrpsProtectModeEnable_Object = MibScalar
brpsProtectModeEnable = _BrpsProtectModeEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 2, 4),
    _BrpsProtectModeEnable_Type()
)
brpsProtectModeEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsProtectModeEnable.setStatus("mandatory")


class _BrpsProtectPassword_Type(DisplayString):
    """Custom type brpsProtectPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrpsProtectPassword_Type.__name__ = "DisplayString"
_BrpsProtectPassword_Object = MibScalar
brpsProtectPassword = _BrpsProtectPassword_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 2, 5),
    _BrpsProtectPassword_Type()
)
brpsProtectPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsProtectPassword.setStatus("mandatory")
_Brport_ObjectIdentity = ObjectIdentity
brport = _Brport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 3)
)


class _BrpsPortCount_Type(Integer32):
    """Custom type brpsPortCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_BrpsPortCount_Type.__name__ = "Integer32"
_BrpsPortCount_Object = MibScalar
brpsPortCount = _BrpsPortCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 3, 1),
    _BrpsPortCount_Type()
)
brpsPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsPortCount.setStatus("mandatory")
_BrpsPortInfoTable_Object = MibTable
brpsPortInfoTable = _BrpsPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 3, 2)
)
if mibBuilder.loadTexts:
    brpsPortInfoTable.setStatus("mandatory")
_BrpsPortInfoEntry_Object = MibTableRow
brpsPortInfoEntry = _BrpsPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 3, 2, 1)
)
brpsPortInfoEntry.setIndexNames(
    (0, "BROTHER-MIB", "brpsPortIndex"),
)
if mibBuilder.loadTexts:
    brpsPortInfoEntry.setStatus("mandatory")


class _BrpsPortIndex_Type(Integer32):
    """Custom type brpsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BrpsPortIndex_Type.__name__ = "Integer32"
_BrpsPortIndex_Object = MibTableColumn
brpsPortIndex = _BrpsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 3, 2, 1, 1),
    _BrpsPortIndex_Type()
)
brpsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsPortIndex.setStatus("mandatory")


class _BrpsPortName_Type(DisplayString):
    """Custom type brpsPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BrpsPortName_Type.__name__ = "DisplayString"
_BrpsPortName_Object = MibTableColumn
brpsPortName = _BrpsPortName_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 3, 2, 1, 2),
    _BrpsPortName_Type()
)
brpsPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsPortName.setStatus("mandatory")


class _BrpsPortType_Type(Integer32):
    """Custom type brpsPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("parallel", 1),
          ("serial", 2))
    )


_BrpsPortType_Type.__name__ = "Integer32"
_BrpsPortType_Object = MibTableColumn
brpsPortType = _BrpsPortType_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 3, 2, 1, 3),
    _BrpsPortType_Type()
)
brpsPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsPortType.setStatus("mandatory")


class _BrpsPortStatus_Type(Integer32):
    """Custom type brpsPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_BrpsPortStatus_Type.__name__ = "Integer32"
_BrpsPortStatus_Object = MibTableColumn
brpsPortStatus = _BrpsPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 3, 2, 1, 4),
    _BrpsPortStatus_Type()
)
brpsPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsPortStatus.setStatus("mandatory")


class _BrpsPortStatusString_Type(DisplayString):
    """Custom type brpsPortStatusString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BrpsPortStatusString_Type.__name__ = "DisplayString"
_BrpsPortStatusString_Object = MibTableColumn
brpsPortStatusString = _BrpsPortStatusString_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 3, 2, 1, 5),
    _BrpsPortStatusString_Type()
)
brpsPortStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsPortStatusString.setStatus("mandatory")


class _BrpsPortProtocol_Type(Integer32):
    """Custom type brpsPortProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_BrpsPortProtocol_Type.__name__ = "Integer32"
_BrpsPortProtocol_Object = MibTableColumn
brpsPortProtocol = _BrpsPortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 3, 2, 1, 6),
    _BrpsPortProtocol_Type()
)
brpsPortProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsPortProtocol.setStatus("mandatory")
_BrpsPortQueueSize_Type = Integer32
_BrpsPortQueueSize_Object = MibTableColumn
brpsPortQueueSize = _BrpsPortQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 3, 2, 1, 7),
    _BrpsPortQueueSize_Type()
)
brpsPortQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsPortQueueSize.setStatus("mandatory")


class _BrpsPortDescriptionString_Type(DisplayString):
    """Custom type brpsPortDescriptionString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_BrpsPortDescriptionString_Type.__name__ = "DisplayString"
_BrpsPortDescriptionString_Object = MibTableColumn
brpsPortDescriptionString = _BrpsPortDescriptionString_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 3, 2, 1, 8),
    _BrpsPortDescriptionString_Type()
)
brpsPortDescriptionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsPortDescriptionString.setStatus("mandatory")


class _BrpsPortInfoString_Type(DisplayString):
    """Custom type brpsPortInfoString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_BrpsPortInfoString_Type.__name__ = "DisplayString"
_BrpsPortInfoString_Object = MibTableColumn
brpsPortInfoString = _BrpsPortInfoString_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 3, 2, 1, 9),
    _BrpsPortInfoString_Type()
)
brpsPortInfoString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsPortInfoString.setStatus("mandatory")


class _BrpsPortHTTPExtensions_Type(Integer32):
    """Custom type brpsPortHTTPExtensions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsPortHTTPExtensions_Type.__name__ = "Integer32"
_BrpsPortHTTPExtensions_Object = MibTableColumn
brpsPortHTTPExtensions = _BrpsPortHTTPExtensions_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 3, 2, 1, 10),
    _BrpsPortHTTPExtensions_Type()
)
brpsPortHTTPExtensions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsPortHTTPExtensions.setStatus("mandatory")


class _BrpsPortSNMPExtensions_Type(Integer32):
    """Custom type brpsPortSNMPExtensions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsPortSNMPExtensions_Type.__name__ = "Integer32"
_BrpsPortSNMPExtensions_Object = MibTableColumn
brpsPortSNMPExtensions = _BrpsPortSNMPExtensions_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 3, 2, 1, 11),
    _BrpsPortSNMPExtensions_Type()
)
brpsPortSNMPExtensions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsPortSNMPExtensions.setStatus("mandatory")


class _BrpsPortAttribute_Type(DisplayString):
    """Custom type brpsPortAttribute based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BrpsPortAttribute_Type.__name__ = "DisplayString"
_BrpsPortAttribute_Object = MibTableColumn
brpsPortAttribute = _BrpsPortAttribute_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 3, 2, 1, 12),
    _BrpsPortAttribute_Type()
)
brpsPortAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsPortAttribute.setStatus("mandatory")


class _BrpsPortBinaryMode_Type(Integer32):
    """Custom type brpsPortBinaryMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_BrpsPortBinaryMode_Type.__name__ = "Integer32"
_BrpsPortBinaryMode_Object = MibTableColumn
brpsPortBinaryMode = _BrpsPortBinaryMode_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 3, 2, 1, 13),
    _BrpsPortBinaryMode_Type()
)
brpsPortBinaryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsPortBinaryMode.setStatus("mandatory")


class _BrpsPortInhibitDatagramSupport_Type(Integer32):
    """Custom type brpsPortInhibitDatagramSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsPortInhibitDatagramSupport_Type.__name__ = "Integer32"
_BrpsPortInhibitDatagramSupport_Object = MibTableColumn
brpsPortInhibitDatagramSupport = _BrpsPortInhibitDatagramSupport_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 3, 2, 1, 14),
    _BrpsPortInhibitDatagramSupport_Type()
)
brpsPortInhibitDatagramSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsPortInhibitDatagramSupport.setStatus("mandatory")
_Brservice_ObjectIdentity = ObjectIdentity
brservice = _Brservice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 4)
)


class _BrpsServiceCount_Type(Integer32):
    """Custom type brpsServiceCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_BrpsServiceCount_Type.__name__ = "Integer32"
_BrpsServiceCount_Object = MibScalar
brpsServiceCount = _BrpsServiceCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 4, 1),
    _BrpsServiceCount_Type()
)
brpsServiceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsServiceCount.setStatus("mandatory")
_BrpsServiceInfoTable_Object = MibTable
brpsServiceInfoTable = _BrpsServiceInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 4, 2)
)
if mibBuilder.loadTexts:
    brpsServiceInfoTable.setStatus("mandatory")
_BrpsServiceInfoEntry_Object = MibTableRow
brpsServiceInfoEntry = _BrpsServiceInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 4, 2, 1)
)
brpsServiceInfoEntry.setIndexNames(
    (0, "BROTHER-MIB", "brpsServiceIndex"),
)
if mibBuilder.loadTexts:
    brpsServiceInfoEntry.setStatus("mandatory")


class _BrpsServiceIndex_Type(Integer32):
    """Custom type brpsServiceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_BrpsServiceIndex_Type.__name__ = "Integer32"
_BrpsServiceIndex_Object = MibTableColumn
brpsServiceIndex = _BrpsServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 4, 2, 1, 1),
    _BrpsServiceIndex_Type()
)
brpsServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsServiceIndex.setStatus("mandatory")


class _BrpsServiceName_Type(DisplayString):
    """Custom type brpsServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BrpsServiceName_Type.__name__ = "DisplayString"
_BrpsServiceName_Object = MibTableColumn
brpsServiceName = _BrpsServiceName_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 4, 2, 1, 2),
    _BrpsServiceName_Type()
)
brpsServiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsServiceName.setStatus("mandatory")


class _BrpsServicePort_Type(Integer32):
    """Custom type brpsServicePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_BrpsServicePort_Type.__name__ = "Integer32"
_BrpsServicePort_Object = MibTableColumn
brpsServicePort = _BrpsServicePort_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 4, 2, 1, 3),
    _BrpsServicePort_Type()
)
brpsServicePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsServicePort.setStatus("mandatory")


class _BrpsServiceFilter_Type(Integer32):
    """Custom type brpsServiceFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrpsServiceFilter_Type.__name__ = "Integer32"
_BrpsServiceFilter_Object = MibTableColumn
brpsServiceFilter = _BrpsServiceFilter_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 4, 2, 1, 4),
    _BrpsServiceFilter_Type()
)
brpsServiceFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsServiceFilter.setStatus("mandatory")


class _BrpsServiceBOT_Type(Integer32):
    """Custom type brpsServiceBOT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrpsServiceBOT_Type.__name__ = "Integer32"
_BrpsServiceBOT_Object = MibTableColumn
brpsServiceBOT = _BrpsServiceBOT_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 4, 2, 1, 5),
    _BrpsServiceBOT_Type()
)
brpsServiceBOT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsServiceBOT.setStatus("mandatory")


class _BrpsServiceEOT_Type(Integer32):
    """Custom type brpsServiceEOT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrpsServiceEOT_Type.__name__ = "Integer32"
_BrpsServiceEOT_Object = MibTableColumn
brpsServiceEOT = _BrpsServiceEOT_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 4, 2, 1, 6),
    _BrpsServiceEOT_Type()
)
brpsServiceEOT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsServiceEOT.setStatus("mandatory")


class _BrpsServiceMatch_Type(Integer32):
    """Custom type brpsServiceMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrpsServiceMatch_Type.__name__ = "Integer32"
_BrpsServiceMatch_Object = MibTableColumn
brpsServiceMatch = _BrpsServiceMatch_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 4, 2, 1, 7),
    _BrpsServiceMatch_Type()
)
brpsServiceMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsServiceMatch.setStatus("mandatory")


class _BrpsServiceReplace_Type(Integer32):
    """Custom type brpsServiceReplace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrpsServiceReplace_Type.__name__ = "Integer32"
_BrpsServiceReplace_Object = MibTableColumn
brpsServiceReplace = _BrpsServiceReplace_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 4, 2, 1, 8),
    _BrpsServiceReplace_Type()
)
brpsServiceReplace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsServiceReplace.setStatus("mandatory")


class _BrpsServiceTCPPort_Type(Integer32):
    """Custom type brpsServiceTCPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrpsServiceTCPPort_Type.__name__ = "Integer32"
_BrpsServiceTCPPort_Object = MibTableColumn
brpsServiceTCPPort = _BrpsServiceTCPPort_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 4, 2, 1, 9),
    _BrpsServiceTCPPort_Type()
)
brpsServiceTCPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsServiceTCPPort.setStatus("mandatory")


class _BrpsServiceNDSTree_Type(DisplayString):
    """Custom type brpsServiceNDSTree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_BrpsServiceNDSTree_Type.__name__ = "DisplayString"
_BrpsServiceNDSTree_Object = MibTableColumn
brpsServiceNDSTree = _BrpsServiceNDSTree_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 4, 2, 1, 10),
    _BrpsServiceNDSTree_Type()
)
brpsServiceNDSTree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsServiceNDSTree.setStatus("mandatory")


class _BrpsServiceNDSContext_Type(OctetString):
    """Custom type brpsServiceNDSContext based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BrpsServiceNDSContext_Type.__name__ = "OctetString"
_BrpsServiceNDSContext_Object = MibTableColumn
brpsServiceNDSContext = _BrpsServiceNDSContext_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 4, 2, 1, 11),
    _BrpsServiceNDSContext_Type()
)
brpsServiceNDSContext.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsServiceNDSContext.setStatus("mandatory")


class _BrpsServiceVines_Type(DisplayString):
    """Custom type brpsServiceVines based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_BrpsServiceVines_Type.__name__ = "DisplayString"
_BrpsServiceVines_Object = MibTableColumn
brpsServiceVines = _BrpsServiceVines_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 4, 2, 1, 12),
    _BrpsServiceVines_Type()
)
brpsServiceVines.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsServiceVines.setStatus("mandatory")


class _BrpsServiceObsolete_Type(Integer32):
    """Custom type brpsServiceObsolete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_BrpsServiceObsolete_Type.__name__ = "Integer32"
_BrpsServiceObsolete_Object = MibTableColumn
brpsServiceObsolete = _BrpsServiceObsolete_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 4, 2, 1, 13),
    _BrpsServiceObsolete_Type()
)
brpsServiceObsolete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsServiceObsolete.setStatus("mandatory")


class _BrpsServiceNetwareServerCount_Type(Integer32):
    """Custom type brpsServiceNetwareServerCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_BrpsServiceNetwareServerCount_Type.__name__ = "Integer32"
_BrpsServiceNetwareServerCount_Object = MibTableColumn
brpsServiceNetwareServerCount = _BrpsServiceNetwareServerCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 4, 2, 1, 14),
    _BrpsServiceNetwareServerCount_Type()
)
brpsServiceNetwareServerCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsServiceNetwareServerCount.setStatus("mandatory")


class _BrpsServiceReceiveOnly_Type(Integer32):
    """Custom type brpsServiceReceiveOnly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsServiceReceiveOnly_Type.__name__ = "Integer32"
_BrpsServiceReceiveOnly_Object = MibTableColumn
brpsServiceReceiveOnly = _BrpsServiceReceiveOnly_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 4, 2, 1, 15),
    _BrpsServiceReceiveOnly_Type()
)
brpsServiceReceiveOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsServiceReceiveOnly.setStatus("mandatory")


class _BrpsServiceTCPQueued_Type(Integer32):
    """Custom type brpsServiceTCPQueued based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsServiceTCPQueued_Type.__name__ = "Integer32"
_BrpsServiceTCPQueued_Object = MibTableColumn
brpsServiceTCPQueued = _BrpsServiceTCPQueued_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 4, 2, 1, 16),
    _BrpsServiceTCPQueued_Type()
)
brpsServiceTCPQueued.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsServiceTCPQueued.setStatus("mandatory")


class _BrpsServiceProtocolLAT_Type(Integer32):
    """Custom type brpsServiceProtocolLAT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsServiceProtocolLAT_Type.__name__ = "Integer32"
_BrpsServiceProtocolLAT_Object = MibTableColumn
brpsServiceProtocolLAT = _BrpsServiceProtocolLAT_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 4, 2, 1, 17),
    _BrpsServiceProtocolLAT_Type()
)
brpsServiceProtocolLAT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsServiceProtocolLAT.setStatus("mandatory")


class _BrpsServiceProtocolTCPIP_Type(Integer32):
    """Custom type brpsServiceProtocolTCPIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsServiceProtocolTCPIP_Type.__name__ = "Integer32"
_BrpsServiceProtocolTCPIP_Object = MibTableColumn
brpsServiceProtocolTCPIP = _BrpsServiceProtocolTCPIP_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 4, 2, 1, 18),
    _BrpsServiceProtocolTCPIP_Type()
)
brpsServiceProtocolTCPIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsServiceProtocolTCPIP.setStatus("mandatory")


class _BrpsServiceProtocolNetware_Type(Integer32):
    """Custom type brpsServiceProtocolNetware based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsServiceProtocolNetware_Type.__name__ = "Integer32"
_BrpsServiceProtocolNetware_Object = MibTableColumn
brpsServiceProtocolNetware = _BrpsServiceProtocolNetware_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 4, 2, 1, 19),
    _BrpsServiceProtocolNetware_Type()
)
brpsServiceProtocolNetware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsServiceProtocolNetware.setStatus("mandatory")


class _BrpsServiceProtocolAppleTalk_Type(Integer32):
    """Custom type brpsServiceProtocolAppleTalk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsServiceProtocolAppleTalk_Type.__name__ = "Integer32"
_BrpsServiceProtocolAppleTalk_Object = MibTableColumn
brpsServiceProtocolAppleTalk = _BrpsServiceProtocolAppleTalk_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 4, 2, 1, 20),
    _BrpsServiceProtocolAppleTalk_Type()
)
brpsServiceProtocolAppleTalk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsServiceProtocolAppleTalk.setStatus("mandatory")


class _BrpsServiceProtocolBanyan_Type(Integer32):
    """Custom type brpsServiceProtocolBanyan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsServiceProtocolBanyan_Type.__name__ = "Integer32"
_BrpsServiceProtocolBanyan_Object = MibTableColumn
brpsServiceProtocolBanyan = _BrpsServiceProtocolBanyan_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 4, 2, 1, 21),
    _BrpsServiceProtocolBanyan_Type()
)
brpsServiceProtocolBanyan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsServiceProtocolBanyan.setStatus("mandatory")


class _BrpsServiceProtocolDLC_Type(Integer32):
    """Custom type brpsServiceProtocolDLC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsServiceProtocolDLC_Type.__name__ = "Integer32"
_BrpsServiceProtocolDLC_Object = MibTableColumn
brpsServiceProtocolDLC = _BrpsServiceProtocolDLC_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 4, 2, 1, 22),
    _BrpsServiceProtocolDLC_Type()
)
brpsServiceProtocolDLC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsServiceProtocolDLC.setStatus("mandatory")


class _BrpsServiceProtocolNetBEUI_Type(Integer32):
    """Custom type brpsServiceProtocolNetBEUI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsServiceProtocolNetBEUI_Type.__name__ = "Integer32"
_BrpsServiceProtocolNetBEUI_Object = MibTableColumn
brpsServiceProtocolNetBEUI = _BrpsServiceProtocolNetBEUI_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 4, 2, 1, 23),
    _BrpsServiceProtocolNetBEUI_Type()
)
brpsServiceProtocolNetBEUI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsServiceProtocolNetBEUI.setStatus("mandatory")


class _BrpsServiceNetwareServerMode_Type(Integer32):
    """Custom type brpsServiceNetwareServerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsServiceNetwareServerMode_Type.__name__ = "Integer32"
_BrpsServiceNetwareServerMode_Object = MibTableColumn
brpsServiceNetwareServerMode = _BrpsServiceNetwareServerMode_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 4, 2, 1, 24),
    _BrpsServiceNetwareServerMode_Type()
)
brpsServiceNetwareServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsServiceNetwareServerMode.setStatus("mandatory")


class _BrpsServiceNetwareRemotePrinterNum_Type(Integer32):
    """Custom type brpsServiceNetwareRemotePrinterNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrpsServiceNetwareRemotePrinterNum_Type.__name__ = "Integer32"
_BrpsServiceNetwareRemotePrinterNum_Object = MibTableColumn
brpsServiceNetwareRemotePrinterNum = _BrpsServiceNetwareRemotePrinterNum_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 4, 2, 1, 25),
    _BrpsServiceNetwareRemotePrinterNum_Type()
)
brpsServiceNetwareRemotePrinterNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsServiceNetwareRemotePrinterNum.setStatus("mandatory")


class _BrpsServiceProtocolIPP_Type(Integer32):
    """Custom type brpsServiceProtocolIPP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsServiceProtocolIPP_Type.__name__ = "Integer32"
_BrpsServiceProtocolIPP_Object = MibTableColumn
brpsServiceProtocolIPP = _BrpsServiceProtocolIPP_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 4, 2, 1, 26),
    _BrpsServiceProtocolIPP_Type()
)
brpsServiceProtocolIPP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsServiceProtocolIPP.setStatus("mandatory")


class _BrpsServiceAppleTalkType_Type(DisplayString):
    """Custom type brpsServiceAppleTalkType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BrpsServiceAppleTalkType_Type.__name__ = "DisplayString"
_BrpsServiceAppleTalkType_Object = MibTableColumn
brpsServiceAppleTalkType = _BrpsServiceAppleTalkType_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 4, 2, 1, 27),
    _BrpsServiceAppleTalkType_Type()
)
brpsServiceAppleTalkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsServiceAppleTalkType.setStatus("mandatory")


class _BrpsServiceStringLimit_Type(Integer32):
    """Custom type brpsServiceStringLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_BrpsServiceStringLimit_Type.__name__ = "Integer32"
_BrpsServiceStringLimit_Object = MibScalar
brpsServiceStringLimit = _BrpsServiceStringLimit_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 4, 3),
    _BrpsServiceStringLimit_Type()
)
brpsServiceStringLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsServiceStringLimit.setStatus("mandatory")
_BrpsServiceStringInfoTable_Object = MibTable
brpsServiceStringInfoTable = _BrpsServiceStringInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 4, 4)
)
if mibBuilder.loadTexts:
    brpsServiceStringInfoTable.setStatus("mandatory")
_BrpsServiceStringInfoEntry_Object = MibTableRow
brpsServiceStringInfoEntry = _BrpsServiceStringInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 4, 4, 1)
)
brpsServiceStringInfoEntry.setIndexNames(
    (0, "BROTHER-MIB", "brpsServiceStringIndex"),
)
if mibBuilder.loadTexts:
    brpsServiceStringInfoEntry.setStatus("mandatory")


class _BrpsServiceStringIndex_Type(Integer32):
    """Custom type brpsServiceStringIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BrpsServiceStringIndex_Type.__name__ = "Integer32"
_BrpsServiceStringIndex_Object = MibTableColumn
brpsServiceStringIndex = _BrpsServiceStringIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 4, 4, 1, 1),
    _BrpsServiceStringIndex_Type()
)
brpsServiceStringIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsServiceStringIndex.setStatus("mandatory")


class _BrpsServiceString_Type(DisplayString):
    """Custom type brpsServiceString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BrpsServiceString_Type.__name__ = "DisplayString"
_BrpsServiceString_Object = MibTableColumn
brpsServiceString = _BrpsServiceString_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 4, 4, 1, 2),
    _BrpsServiceString_Type()
)
brpsServiceString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsServiceString.setStatus("mandatory")
_BrpsServiceStringCount_Type = Integer32
_BrpsServiceStringCount_Object = MibScalar
brpsServiceStringCount = _BrpsServiceStringCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 4, 5),
    _BrpsServiceStringCount_Type()
)
brpsServiceStringCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsServiceStringCount.setStatus("mandatory")
_BrpsServiceFilterCount_Type = Integer32
_BrpsServiceFilterCount_Object = MibScalar
brpsServiceFilterCount = _BrpsServiceFilterCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 4, 6),
    _BrpsServiceFilterCount_Type()
)
brpsServiceFilterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsServiceFilterCount.setStatus("mandatory")
_Brprotocol_ObjectIdentity = ObjectIdentity
brprotocol = _Brprotocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5)
)
_Brlat_ObjectIdentity = ObjectIdentity
brlat = _Brlat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 1)
)


class _BrpsLATSupported_Type(Integer32):
    """Custom type brpsLATSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsLATSupported_Type.__name__ = "Integer32"
_BrpsLATSupported_Object = MibScalar
brpsLATSupported = _BrpsLATSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 1, 1),
    _BrpsLATSupported_Type()
)
brpsLATSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsLATSupported.setStatus("mandatory")


class _BrpsLATEnable_Type(Integer32):
    """Custom type brpsLATEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsLATEnable_Type.__name__ = "Integer32"
_BrpsLATEnable_Object = MibScalar
brpsLATEnable = _BrpsLATEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 1, 2),
    _BrpsLATEnable_Type()
)
brpsLATEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsLATEnable.setStatus("mandatory")


class _BrpsLATCircuitTimer_Type(Integer32):
    """Custom type brpsLATCircuitTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 499),
    )


_BrpsLATCircuitTimer_Type.__name__ = "Integer32"
_BrpsLATCircuitTimer_Object = MibScalar
brpsLATCircuitTimer = _BrpsLATCircuitTimer_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 1, 3),
    _BrpsLATCircuitTimer_Type()
)
brpsLATCircuitTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsLATCircuitTimer.setStatus("mandatory")


class _BrpsLATKeepAliveTimer_Type(Integer32):
    """Custom type brpsLATKeepAliveTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_BrpsLATKeepAliveTimer_Type.__name__ = "Integer32"
_BrpsLATKeepAliveTimer_Object = MibScalar
brpsLATKeepAliveTimer = _BrpsLATKeepAliveTimer_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 1, 4),
    _BrpsLATKeepAliveTimer_Type()
)
brpsLATKeepAliveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsLATKeepAliveTimer.setStatus("mandatory")


class _BrpsLATReceiveBufferMax_Type(Integer32):
    """Custom type brpsLATReceiveBufferMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_BrpsLATReceiveBufferMax_Type.__name__ = "Integer32"
_BrpsLATReceiveBufferMax_Object = MibScalar
brpsLATReceiveBufferMax = _BrpsLATReceiveBufferMax_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 1, 5),
    _BrpsLATReceiveBufferMax_Type()
)
brpsLATReceiveBufferMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsLATReceiveBufferMax.setStatus("mandatory")


class _BrpsLATTransmitBufferMax_Type(Integer32):
    """Custom type brpsLATTransmitBufferMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_BrpsLATTransmitBufferMax_Type.__name__ = "Integer32"
_BrpsLATTransmitBufferMax_Object = MibScalar
brpsLATTransmitBufferMax = _BrpsLATTransmitBufferMax_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 1, 6),
    _BrpsLATTransmitBufferMax_Type()
)
brpsLATTransmitBufferMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsLATTransmitBufferMax.setStatus("mandatory")


class _BrpsLATTimeout_Type(Integer32):
    """Custom type brpsLATTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 499),
    )


_BrpsLATTimeout_Type.__name__ = "Integer32"
_BrpsLATTimeout_Object = MibScalar
brpsLATTimeout = _BrpsLATTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 1, 7),
    _BrpsLATTimeout_Type()
)
brpsLATTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsLATTimeout.setStatus("mandatory")


class _BrpsLATGroup_Type(DisplayString):
    """Custom type brpsLATGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 7),
    )


_BrpsLATGroup_Type.__name__ = "DisplayString"
_BrpsLATGroup_Object = MibScalar
brpsLATGroup = _BrpsLATGroup_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 1, 8),
    _BrpsLATGroup_Type()
)
brpsLATGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsLATGroup.setStatus("mandatory")
_Brtcpip_ObjectIdentity = ObjectIdentity
brtcpip = _Brtcpip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 2)
)


class _BrpsTCPIPSupported_Type(Integer32):
    """Custom type brpsTCPIPSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsTCPIPSupported_Type.__name__ = "Integer32"
_BrpsTCPIPSupported_Object = MibScalar
brpsTCPIPSupported = _BrpsTCPIPSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 2, 1),
    _BrpsTCPIPSupported_Type()
)
brpsTCPIPSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsTCPIPSupported.setStatus("mandatory")


class _BrpsTCPIPEnable_Type(Integer32):
    """Custom type brpsTCPIPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsTCPIPEnable_Type.__name__ = "Integer32"
_BrpsTCPIPEnable_Object = MibScalar
brpsTCPIPEnable = _BrpsTCPIPEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 2, 2),
    _BrpsTCPIPEnable_Type()
)
brpsTCPIPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsTCPIPEnable.setStatus("mandatory")
_BrpsTCPIPAddress_Type = IpAddress
_BrpsTCPIPAddress_Object = MibScalar
brpsTCPIPAddress = _BrpsTCPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 2, 3),
    _BrpsTCPIPAddress_Type()
)
brpsTCPIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsTCPIPAddress.setStatus("mandatory")
_BrpsTCPIPSubnetMask_Type = IpAddress
_BrpsTCPIPSubnetMask_Object = MibScalar
brpsTCPIPSubnetMask = _BrpsTCPIPSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 2, 4),
    _BrpsTCPIPSubnetMask_Type()
)
brpsTCPIPSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsTCPIPSubnetMask.setStatus("mandatory")
_BrpsTCPIPGateway_Type = IpAddress
_BrpsTCPIPGateway_Object = MibScalar
brpsTCPIPGateway = _BrpsTCPIPGateway_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 2, 5),
    _BrpsTCPIPGateway_Type()
)
brpsTCPIPGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsTCPIPGateway.setStatus("mandatory")


class _BrpsTCPIPMethod_Type(Integer32):
    """Custom type brpsTCPIPMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BrpsTCPIPMethod_Type.__name__ = "Integer32"
_BrpsTCPIPMethod_Object = MibScalar
brpsTCPIPMethod = _BrpsTCPIPMethod_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 2, 6),
    _BrpsTCPIPMethod_Type()
)
brpsTCPIPMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsTCPIPMethod.setStatus("mandatory")


class _BrpsTCPIPTimeout_Type(Integer32):
    """Custom type brpsTCPIPTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_BrpsTCPIPTimeout_Type.__name__ = "Integer32"
_BrpsTCPIPTimeout_Object = MibScalar
brpsTCPIPTimeout = _BrpsTCPIPTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 2, 7),
    _BrpsTCPIPTimeout_Type()
)
brpsTCPIPTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsTCPIPTimeout.setStatus("mandatory")


class _BrpsTCPIPBootTries_Type(Integer32):
    """Custom type brpsTCPIPBootTries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_BrpsTCPIPBootTries_Type.__name__ = "Integer32"
_BrpsTCPIPBootTries_Object = MibScalar
brpsTCPIPBootTries = _BrpsTCPIPBootTries_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 2, 8),
    _BrpsTCPIPBootTries_Type()
)
brpsTCPIPBootTries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsTCPIPBootTries.setStatus("mandatory")


class _BrpsTCPIPMaxWindow_Type(Integer32):
    """Custom type brpsTCPIPMaxWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1500, 65535),
    )


_BrpsTCPIPMaxWindow_Type.__name__ = "Integer32"
_BrpsTCPIPMaxWindow_Object = MibScalar
brpsTCPIPMaxWindow = _BrpsTCPIPMaxWindow_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 2, 9),
    _BrpsTCPIPMaxWindow_Type()
)
brpsTCPIPMaxWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsTCPIPMaxWindow.setStatus("mandatory")


class _BrpsTCPIPRARPNoSubnet_Type(Integer32):
    """Custom type brpsTCPIPRARPNoSubnet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsTCPIPRARPNoSubnet_Type.__name__ = "Integer32"
_BrpsTCPIPRARPNoSubnet_Object = MibScalar
brpsTCPIPRARPNoSubnet = _BrpsTCPIPRARPNoSubnet_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 2, 10),
    _BrpsTCPIPRARPNoSubnet_Type()
)
brpsTCPIPRARPNoSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsTCPIPRARPNoSubnet.setStatus("mandatory")


class _BrpsTCPIPRARPNoGateway_Type(Integer32):
    """Custom type brpsTCPIPRARPNoGateway based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsTCPIPRARPNoGateway_Type.__name__ = "Integer32"
_BrpsTCPIPRARPNoGateway_Object = MibScalar
brpsTCPIPRARPNoGateway = _BrpsTCPIPRARPNoGateway_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 2, 11),
    _BrpsTCPIPRARPNoGateway_Type()
)
brpsTCPIPRARPNoGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsTCPIPRARPNoGateway.setStatus("mandatory")


class _BrpsTCPIPUpdate_Type(OctetString):
    """Custom type brpsTCPIPUpdate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_BrpsTCPIPUpdate_Type.__name__ = "OctetString"
_BrpsTCPIPUpdate_Object = MibScalar
brpsTCPIPUpdate = _BrpsTCPIPUpdate_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 2, 12),
    _BrpsTCPIPUpdate_Type()
)
brpsTCPIPUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsTCPIPUpdate.setStatus("mandatory")


class _BrpsTCPIPBanner_Type(Integer32):
    """Custom type brpsTCPIPBanner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsTCPIPBanner_Type.__name__ = "Integer32"
_BrpsTCPIPBanner_Object = MibScalar
brpsTCPIPBanner = _BrpsTCPIPBanner_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 2, 13),
    _BrpsTCPIPBanner_Type()
)
brpsTCPIPBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsTCPIPBanner.setStatus("mandatory")


class _BrpsTCPIPFastTimeoutEnable_Type(Integer32):
    """Custom type brpsTCPIPFastTimeoutEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsTCPIPFastTimeoutEnable_Type.__name__ = "Integer32"
_BrpsTCPIPFastTimeoutEnable_Object = MibScalar
brpsTCPIPFastTimeoutEnable = _BrpsTCPIPFastTimeoutEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 2, 14),
    _BrpsTCPIPFastTimeoutEnable_Type()
)
brpsTCPIPFastTimeoutEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsTCPIPFastTimeoutEnable.setStatus("mandatory")


class _BrpsTCPIPLPRRetryEnable_Type(Integer32):
    """Custom type brpsTCPIPLPRRetryEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsTCPIPLPRRetryEnable_Type.__name__ = "Integer32"
_BrpsTCPIPLPRRetryEnable_Object = MibScalar
brpsTCPIPLPRRetryEnable = _BrpsTCPIPLPRRetryEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 2, 15),
    _BrpsTCPIPLPRRetryEnable_Type()
)
brpsTCPIPLPRRetryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsTCPIPLPRRetryEnable.setStatus("mandatory")


class _BrpsTCPIPUseMethod_Type(Integer32):
    """Custom type brpsTCPIPUseMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BrpsTCPIPUseMethod_Type.__name__ = "Integer32"
_BrpsTCPIPUseMethod_Object = MibScalar
brpsTCPIPUseMethod = _BrpsTCPIPUseMethod_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 2, 16),
    _BrpsTCPIPUseMethod_Type()
)
brpsTCPIPUseMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsTCPIPUseMethod.setStatus("mandatory")
_BrpsTCPIPMethodServer_Type = IpAddress
_BrpsTCPIPMethodServer_Object = MibScalar
brpsTCPIPMethodServer = _BrpsTCPIPMethodServer_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 2, 17),
    _BrpsTCPIPMethodServer_Type()
)
brpsTCPIPMethodServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsTCPIPMethodServer.setStatus("mandatory")
_BrpsTCPIPAccessTable_Object = MibTable
brpsTCPIPAccessTable = _BrpsTCPIPAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 2, 18)
)
if mibBuilder.loadTexts:
    brpsTCPIPAccessTable.setStatus("mandatory")
_BrpsTCPIPAccessEntry_Object = MibTableRow
brpsTCPIPAccessEntry = _BrpsTCPIPAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 2, 18, 1)
)
brpsTCPIPAccessEntry.setIndexNames(
    (0, "BROTHER-MIB", "brpsTCPIPAccessIndex"),
)
if mibBuilder.loadTexts:
    brpsTCPIPAccessEntry.setStatus("mandatory")


class _BrpsTCPIPAccessIndex_Type(Integer32):
    """Custom type brpsTCPIPAccessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BrpsTCPIPAccessIndex_Type.__name__ = "Integer32"
_BrpsTCPIPAccessIndex_Object = MibTableColumn
brpsTCPIPAccessIndex = _BrpsTCPIPAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 2, 18, 1, 1),
    _BrpsTCPIPAccessIndex_Type()
)
brpsTCPIPAccessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsTCPIPAccessIndex.setStatus("mandatory")
_BrpsTCPIPAccessNodeAddress_Type = IpAddress
_BrpsTCPIPAccessNodeAddress_Object = MibTableColumn
brpsTCPIPAccessNodeAddress = _BrpsTCPIPAccessNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 2, 18, 1, 2),
    _BrpsTCPIPAccessNodeAddress_Type()
)
brpsTCPIPAccessNodeAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsTCPIPAccessNodeAddress.setStatus("mandatory")
_BrpsTCPIPAccessSubnetMask_Type = IpAddress
_BrpsTCPIPAccessSubnetMask_Object = MibTableColumn
brpsTCPIPAccessSubnetMask = _BrpsTCPIPAccessSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 2, 18, 1, 3),
    _BrpsTCPIPAccessSubnetMask_Type()
)
brpsTCPIPAccessSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsTCPIPAccessSubnetMask.setStatus("mandatory")


class _BrpsAdvancedTCPIPAccessSupported_Type(Integer32):
    """Custom type brpsAdvancedTCPIPAccessSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsAdvancedTCPIPAccessSupported_Type.__name__ = "Integer32"
_BrpsAdvancedTCPIPAccessSupported_Object = MibScalar
brpsAdvancedTCPIPAccessSupported = _BrpsAdvancedTCPIPAccessSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 2, 19),
    _BrpsAdvancedTCPIPAccessSupported_Type()
)
brpsAdvancedTCPIPAccessSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsAdvancedTCPIPAccessSupported.setStatus("mandatory")


class _BrpsAdvancedTCPIPAccessEnable_Type(Integer32):
    """Custom type brpsAdvancedTCPIPAccessEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsAdvancedTCPIPAccessEnable_Type.__name__ = "Integer32"
_BrpsAdvancedTCPIPAccessEnable_Object = MibScalar
brpsAdvancedTCPIPAccessEnable = _BrpsAdvancedTCPIPAccessEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 2, 20),
    _BrpsAdvancedTCPIPAccessEnable_Type()
)
brpsAdvancedTCPIPAccessEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsAdvancedTCPIPAccessEnable.setStatus("mandatory")
_BrpsAdvancedTCPIPAccessAdministratorIPAddress_Type = IpAddress
_BrpsAdvancedTCPIPAccessAdministratorIPAddress_Object = MibScalar
brpsAdvancedTCPIPAccessAdministratorIPAddress = _BrpsAdvancedTCPIPAccessAdministratorIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 2, 21),
    _BrpsAdvancedTCPIPAccessAdministratorIPAddress_Type()
)
brpsAdvancedTCPIPAccessAdministratorIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsAdvancedTCPIPAccessAdministratorIPAddress.setStatus("mandatory")


class _BrpsAdvancedTCPIPAccessSetting_Type(Integer32):
    """Custom type brpsAdvancedTCPIPAccessSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsAdvancedTCPIPAccessSetting_Type.__name__ = "Integer32"
_BrpsAdvancedTCPIPAccessSetting_Object = MibScalar
brpsAdvancedTCPIPAccessSetting = _BrpsAdvancedTCPIPAccessSetting_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 2, 22),
    _BrpsAdvancedTCPIPAccessSetting_Type()
)
brpsAdvancedTCPIPAccessSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsAdvancedTCPIPAccessSetting.setStatus("mandatory")
_Brnetware_ObjectIdentity = ObjectIdentity
brnetware = _Brnetware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 3)
)


class _BrpsNetwareSupported_Type(Integer32):
    """Custom type brpsNetwareSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BrpsNetwareSupported_Type.__name__ = "Integer32"
_BrpsNetwareSupported_Object = MibScalar
brpsNetwareSupported = _BrpsNetwareSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 3, 1),
    _BrpsNetwareSupported_Type()
)
brpsNetwareSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsNetwareSupported.setStatus("mandatory")


class _BrpsNetwareEnable_Type(Integer32):
    """Custom type brpsNetwareEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsNetwareEnable_Type.__name__ = "Integer32"
_BrpsNetwareEnable_Object = MibScalar
brpsNetwareEnable = _BrpsNetwareEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 3, 2),
    _BrpsNetwareEnable_Type()
)
brpsNetwareEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsNetwareEnable.setStatus("mandatory")


class _BrpsNetwareFrameType_Type(Integer32):
    """Custom type brpsNetwareFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_BrpsNetwareFrameType_Type.__name__ = "Integer32"
_BrpsNetwareFrameType_Object = MibScalar
brpsNetwareFrameType = _BrpsNetwareFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 3, 3),
    _BrpsNetwareFrameType_Type()
)
brpsNetwareFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsNetwareFrameType.setStatus("mandatory")


class _BrpsNetwarePollFreq_Type(Integer32):
    """Custom type brpsNetwarePollFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 60),
    )


_BrpsNetwarePollFreq_Type.__name__ = "Integer32"
_BrpsNetwarePollFreq_Object = MibScalar
brpsNetwarePollFreq = _BrpsNetwarePollFreq_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 3, 4),
    _BrpsNetwarePollFreq_Type()
)
brpsNetwarePollFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsNetwarePollFreq.setStatus("mandatory")


class _BrpsNetwareAdvFreq_Type(Integer32):
    """Custom type brpsNetwareAdvFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 210),
    )


_BrpsNetwareAdvFreq_Type.__name__ = "Integer32"
_BrpsNetwareAdvFreq_Object = MibScalar
brpsNetwareAdvFreq = _BrpsNetwareAdvFreq_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 3, 5),
    _BrpsNetwareAdvFreq_Type()
)
brpsNetwareAdvFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsNetwareAdvFreq.setStatus("mandatory")


class _BrpsNetwarePassword_Type(DisplayString):
    """Custom type brpsNetwarePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrpsNetwarePassword_Type.__name__ = "DisplayString"
_BrpsNetwarePassword_Object = MibScalar
brpsNetwarePassword = _BrpsNetwarePassword_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 3, 6),
    _BrpsNetwarePassword_Type()
)
brpsNetwarePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsNetwarePassword.setStatus("mandatory")


class _BrpsNetwareRestart_Type(Integer32):
    """Custom type brpsNetwareRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsNetwareRestart_Type.__name__ = "Integer32"
_BrpsNetwareRestart_Object = MibScalar
brpsNetwareRestart = _BrpsNetwareRestart_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 3, 7),
    _BrpsNetwareRestart_Type()
)
brpsNetwareRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsNetwareRestart.setStatus("mandatory")
_BrpsNetwareServerTable_Object = MibTable
brpsNetwareServerTable = _BrpsNetwareServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 3, 8)
)
if mibBuilder.loadTexts:
    brpsNetwareServerTable.setStatus("mandatory")
_BrpsNetwareServerEntry_Object = MibTableRow
brpsNetwareServerEntry = _BrpsNetwareServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 3, 8, 1)
)
brpsNetwareServerEntry.setIndexNames(
    (0, "BROTHER-MIB", "brpsServiceIndex"),
    (0, "BROTHER-MIB", "brpsNetwareServerIndex"),
)
if mibBuilder.loadTexts:
    brpsNetwareServerEntry.setStatus("mandatory")


class _BrpsNetwareServerIndex_Type(Integer32):
    """Custom type brpsNetwareServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BrpsNetwareServerIndex_Type.__name__ = "Integer32"
_BrpsNetwareServerIndex_Object = MibTableColumn
brpsNetwareServerIndex = _BrpsNetwareServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 3, 8, 1, 1),
    _BrpsNetwareServerIndex_Type()
)
brpsNetwareServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsNetwareServerIndex.setStatus("mandatory")


class _BrpsNetwareServerName_Type(DisplayString):
    """Custom type brpsNetwareServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_BrpsNetwareServerName_Type.__name__ = "DisplayString"
_BrpsNetwareServerName_Object = MibTableColumn
brpsNetwareServerName = _BrpsNetwareServerName_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 3, 8, 1, 2),
    _BrpsNetwareServerName_Type()
)
brpsNetwareServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsNetwareServerName.setStatus("mandatory")


class _BrpsNetwarePasswordSet_Type(Integer32):
    """Custom type brpsNetwarePasswordSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsNetwarePasswordSet_Type.__name__ = "Integer32"
_BrpsNetwarePasswordSet_Object = MibScalar
brpsNetwarePasswordSet = _BrpsNetwarePasswordSet_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 3, 9),
    _BrpsNetwarePasswordSet_Type()
)
brpsNetwarePasswordSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsNetwarePasswordSet.setStatus("mandatory")


class _BrpsNDSSupported_Type(Integer32):
    """Custom type brpsNDSSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsNDSSupported_Type.__name__ = "Integer32"
_BrpsNDSSupported_Object = MibScalar
brpsNDSSupported = _BrpsNDSSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 3, 10),
    _BrpsNDSSupported_Type()
)
brpsNDSSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsNDSSupported.setStatus("mandatory")


class _BrpsNetwareEtherIINetInfo_Type(DisplayString):
    """Custom type brpsNetwareEtherIINetInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BrpsNetwareEtherIINetInfo_Type.__name__ = "DisplayString"
_BrpsNetwareEtherIINetInfo_Object = MibScalar
brpsNetwareEtherIINetInfo = _BrpsNetwareEtherIINetInfo_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 3, 11),
    _BrpsNetwareEtherIINetInfo_Type()
)
brpsNetwareEtherIINetInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsNetwareEtherIINetInfo.setStatus("mandatory")


class _BrpsNetwareEtherIICount_Type(Integer32):
    """Custom type brpsNetwareEtherIICount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrpsNetwareEtherIICount_Type.__name__ = "Integer32"
_BrpsNetwareEtherIICount_Object = MibScalar
brpsNetwareEtherIICount = _BrpsNetwareEtherIICount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 3, 12),
    _BrpsNetwareEtherIICount_Type()
)
brpsNetwareEtherIICount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsNetwareEtherIICount.setStatus("mandatory")


class _BrpsNetware8022NetInfo_Type(DisplayString):
    """Custom type brpsNetware8022NetInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BrpsNetware8022NetInfo_Type.__name__ = "DisplayString"
_BrpsNetware8022NetInfo_Object = MibScalar
brpsNetware8022NetInfo = _BrpsNetware8022NetInfo_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 3, 13),
    _BrpsNetware8022NetInfo_Type()
)
brpsNetware8022NetInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsNetware8022NetInfo.setStatus("mandatory")


class _BrpsNetware8022Count_Type(Integer32):
    """Custom type brpsNetware8022Count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrpsNetware8022Count_Type.__name__ = "Integer32"
_BrpsNetware8022Count_Object = MibScalar
brpsNetware8022Count = _BrpsNetware8022Count_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 3, 14),
    _BrpsNetware8022Count_Type()
)
brpsNetware8022Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsNetware8022Count.setStatus("mandatory")


class _BrpsNetware8023NetInfo_Type(DisplayString):
    """Custom type brpsNetware8023NetInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BrpsNetware8023NetInfo_Type.__name__ = "DisplayString"
_BrpsNetware8023NetInfo_Object = MibScalar
brpsNetware8023NetInfo = _BrpsNetware8023NetInfo_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 3, 15),
    _BrpsNetware8023NetInfo_Type()
)
brpsNetware8023NetInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsNetware8023NetInfo.setStatus("mandatory")


class _BrpsNetware8023Count_Type(Integer32):
    """Custom type brpsNetware8023Count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrpsNetware8023Count_Type.__name__ = "Integer32"
_BrpsNetware8023Count_Object = MibScalar
brpsNetware8023Count = _BrpsNetware8023Count_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 3, 16),
    _BrpsNetware8023Count_Type()
)
brpsNetware8023Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsNetware8023Count.setStatus("mandatory")


class _BrpsNetwareSNAPNetInfo_Type(DisplayString):
    """Custom type brpsNetwareSNAPNetInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BrpsNetwareSNAPNetInfo_Type.__name__ = "DisplayString"
_BrpsNetwareSNAPNetInfo_Object = MibScalar
brpsNetwareSNAPNetInfo = _BrpsNetwareSNAPNetInfo_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 3, 17),
    _BrpsNetwareSNAPNetInfo_Type()
)
brpsNetwareSNAPNetInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsNetwareSNAPNetInfo.setStatus("mandatory")


class _BrpsNetwareSNAPCount_Type(Integer32):
    """Custom type brpsNetwareSNAPCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrpsNetwareSNAPCount_Type.__name__ = "Integer32"
_BrpsNetwareSNAPCount_Object = MibScalar
brpsNetwareSNAPCount = _BrpsNetwareSNAPCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 3, 18),
    _BrpsNetwareSNAPCount_Type()
)
brpsNetwareSNAPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsNetwareSNAPCount.setStatus("mandatory")


class _BrpsNetwareServicingServerName_Type(DisplayString):
    """Custom type brpsNetwareServicingServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_BrpsNetwareServicingServerName_Type.__name__ = "DisplayString"
_BrpsNetwareServicingServerName_Object = MibScalar
brpsNetwareServicingServerName = _BrpsNetwareServicingServerName_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 3, 19),
    _BrpsNetwareServicingServerName_Type()
)
brpsNetwareServicingServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsNetwareServicingServerName.setStatus("mandatory")


class _BrpsNetwareServicingQueueName_Type(DisplayString):
    """Custom type brpsNetwareServicingQueueName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_BrpsNetwareServicingQueueName_Type.__name__ = "DisplayString"
_BrpsNetwareServicingQueueName_Object = MibScalar
brpsNetwareServicingQueueName = _BrpsNetwareServicingQueueName_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 3, 20),
    _BrpsNetwareServicingQueueName_Type()
)
brpsNetwareServicingQueueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsNetwareServicingQueueName.setStatus("mandatory")


class _BrpsNetwareServicingServerCount_Type(Integer32):
    """Custom type brpsNetwareServicingServerCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrpsNetwareServicingServerCount_Type.__name__ = "Integer32"
_BrpsNetwareServicingServerCount_Object = MibScalar
brpsNetwareServicingServerCount = _BrpsNetwareServicingServerCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 3, 21),
    _BrpsNetwareServicingServerCount_Type()
)
brpsNetwareServicingServerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsNetwareServicingServerCount.setStatus("mandatory")


class _BrpsNetwareServicingQueueCount_Type(Integer32):
    """Custom type brpsNetwareServicingQueueCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrpsNetwareServicingQueueCount_Type.__name__ = "Integer32"
_BrpsNetwareServicingQueueCount_Object = MibScalar
brpsNetwareServicingQueueCount = _BrpsNetwareServicingQueueCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 3, 22),
    _BrpsNetwareServicingQueueCount_Type()
)
brpsNetwareServicingQueueCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsNetwareServicingQueueCount.setStatus("mandatory")


class _BrpsNetwarePrintJob_Type(Integer32):
    """Custom type brpsNetwarePrintJob based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrpsNetwarePrintJob_Type.__name__ = "Integer32"
_BrpsNetwarePrintJob_Object = MibScalar
brpsNetwarePrintJob = _BrpsNetwarePrintJob_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 3, 23),
    _BrpsNetwarePrintJob_Type()
)
brpsNetwarePrintJob.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsNetwarePrintJob.setStatus("mandatory")
_Brappletalk_ObjectIdentity = ObjectIdentity
brappletalk = _Brappletalk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 4)
)


class _BrpsAppleTalkSupported_Type(Integer32):
    """Custom type brpsAppleTalkSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsAppleTalkSupported_Type.__name__ = "Integer32"
_BrpsAppleTalkSupported_Object = MibScalar
brpsAppleTalkSupported = _BrpsAppleTalkSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 4, 1),
    _BrpsAppleTalkSupported_Type()
)
brpsAppleTalkSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsAppleTalkSupported.setStatus("mandatory")


class _BrpsAppleTalkEnable_Type(Integer32):
    """Custom type brpsAppleTalkEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsAppleTalkEnable_Type.__name__ = "Integer32"
_BrpsAppleTalkEnable_Object = MibScalar
brpsAppleTalkEnable = _BrpsAppleTalkEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 4, 2),
    _BrpsAppleTalkEnable_Type()
)
brpsAppleTalkEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsAppleTalkEnable.setStatus("mandatory")
_BrpsAppleTalkZone_Type = DisplayString
_BrpsAppleTalkZone_Object = MibScalar
brpsAppleTalkZone = _BrpsAppleTalkZone_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 4, 3),
    _BrpsAppleTalkZone_Type()
)
brpsAppleTalkZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsAppleTalkZone.setStatus("mandatory")


class _BrpsAppleTalkPrintJob_Type(Integer32):
    """Custom type brpsAppleTalkPrintJob based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrpsAppleTalkPrintJob_Type.__name__ = "Integer32"
_BrpsAppleTalkPrintJob_Object = MibScalar
brpsAppleTalkPrintJob = _BrpsAppleTalkPrintJob_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 4, 4),
    _BrpsAppleTalkPrintJob_Type()
)
brpsAppleTalkPrintJob.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsAppleTalkPrintJob.setStatus("mandatory")


class _BrpsAppleTalkReadByte_Type(Integer32):
    """Custom type brpsAppleTalkReadByte based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrpsAppleTalkReadByte_Type.__name__ = "Integer32"
_BrpsAppleTalkReadByte_Object = MibScalar
brpsAppleTalkReadByte = _BrpsAppleTalkReadByte_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 4, 5),
    _BrpsAppleTalkReadByte_Type()
)
brpsAppleTalkReadByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsAppleTalkReadByte.setStatus("mandatory")


class _BrpsAppleTalkWriteByte_Type(Integer32):
    """Custom type brpsAppleTalkWriteByte based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrpsAppleTalkWriteByte_Type.__name__ = "Integer32"
_BrpsAppleTalkWriteByte_Object = MibScalar
brpsAppleTalkWriteByte = _BrpsAppleTalkWriteByte_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 4, 6),
    _BrpsAppleTalkWriteByte_Type()
)
brpsAppleTalkWriteByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsAppleTalkWriteByte.setStatus("mandatory")


class _BrpsAppleTalkReadError_Type(Integer32):
    """Custom type brpsAppleTalkReadError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrpsAppleTalkReadError_Type.__name__ = "Integer32"
_BrpsAppleTalkReadError_Object = MibScalar
brpsAppleTalkReadError = _BrpsAppleTalkReadError_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 4, 7),
    _BrpsAppleTalkReadError_Type()
)
brpsAppleTalkReadError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsAppleTalkReadError.setStatus("mandatory")


class _BrpsAppleTalkWriteError_Type(Integer32):
    """Custom type brpsAppleTalkWriteError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrpsAppleTalkWriteError_Type.__name__ = "Integer32"
_BrpsAppleTalkWriteError_Object = MibScalar
brpsAppleTalkWriteError = _BrpsAppleTalkWriteError_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 4, 8),
    _BrpsAppleTalkWriteError_Type()
)
brpsAppleTalkWriteError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsAppleTalkWriteError.setStatus("mandatory")
_Brbanyan_ObjectIdentity = ObjectIdentity
brbanyan = _Brbanyan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 5)
)


class _BrpsBanyanSupported_Type(Integer32):
    """Custom type brpsBanyanSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsBanyanSupported_Type.__name__ = "Integer32"
_BrpsBanyanSupported_Object = MibScalar
brpsBanyanSupported = _BrpsBanyanSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 5, 1),
    _BrpsBanyanSupported_Type()
)
brpsBanyanSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsBanyanSupported.setStatus("mandatory")


class _BrpsBanyanEnable_Type(Integer32):
    """Custom type brpsBanyanEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsBanyanEnable_Type.__name__ = "Integer32"
_BrpsBanyanEnable_Object = MibScalar
brpsBanyanEnable = _BrpsBanyanEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 5, 2),
    _BrpsBanyanEnable_Type()
)
brpsBanyanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsBanyanEnable.setStatus("mandatory")


class _BrpsBanyanLoginName_Type(DisplayString):
    """Custom type brpsBanyanLoginName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrpsBanyanLoginName_Type.__name__ = "DisplayString"
_BrpsBanyanLoginName_Object = MibScalar
brpsBanyanLoginName = _BrpsBanyanLoginName_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 5, 3),
    _BrpsBanyanLoginName_Type()
)
brpsBanyanLoginName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsBanyanLoginName.setStatus("mandatory")


class _BrpsBanyanPassword_Type(DisplayString):
    """Custom type brpsBanyanPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BrpsBanyanPassword_Type.__name__ = "DisplayString"
_BrpsBanyanPassword_Object = MibScalar
brpsBanyanPassword = _BrpsBanyanPassword_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 5, 4),
    _BrpsBanyanPassword_Type()
)
brpsBanyanPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsBanyanPassword.setStatus("mandatory")


class _BrpsBanyanHopCount_Type(Integer32):
    """Custom type brpsBanyanHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_BrpsBanyanHopCount_Type.__name__ = "Integer32"
_BrpsBanyanHopCount_Object = MibScalar
brpsBanyanHopCount = _BrpsBanyanHopCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 5, 5),
    _BrpsBanyanHopCount_Type()
)
brpsBanyanHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsBanyanHopCount.setStatus("mandatory")


class _BrpsBanyanTimeout_Type(Integer32):
    """Custom type brpsBanyanTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_BrpsBanyanTimeout_Type.__name__ = "Integer32"
_BrpsBanyanTimeout_Object = MibScalar
brpsBanyanTimeout = _BrpsBanyanTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 5, 6),
    _BrpsBanyanTimeout_Type()
)
brpsBanyanTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsBanyanTimeout.setStatus("mandatory")


class _BrpsBanyanPasswordSet_Type(Integer32):
    """Custom type brpsBanyanPasswordSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsBanyanPasswordSet_Type.__name__ = "Integer32"
_BrpsBanyanPasswordSet_Object = MibScalar
brpsBanyanPasswordSet = _BrpsBanyanPasswordSet_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 5, 7),
    _BrpsBanyanPasswordSet_Type()
)
brpsBanyanPasswordSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsBanyanPasswordSet.setStatus("mandatory")


class _BrpsBanyanIPNetworkID1_Type(OctetString):
    """Custom type brpsBanyanIPNetworkID1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_BrpsBanyanIPNetworkID1_Type.__name__ = "OctetString"
_BrpsBanyanIPNetworkID1_Object = MibScalar
brpsBanyanIPNetworkID1 = _BrpsBanyanIPNetworkID1_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 5, 8),
    _BrpsBanyanIPNetworkID1_Type()
)
brpsBanyanIPNetworkID1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsBanyanIPNetworkID1.setStatus("mandatory")


class _BrpsBanyanIPNetworkID2_Type(OctetString):
    """Custom type brpsBanyanIPNetworkID2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_BrpsBanyanIPNetworkID2_Type.__name__ = "OctetString"
_BrpsBanyanIPNetworkID2_Object = MibScalar
brpsBanyanIPNetworkID2 = _BrpsBanyanIPNetworkID2_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 5, 9),
    _BrpsBanyanIPNetworkID2_Type()
)
brpsBanyanIPNetworkID2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsBanyanIPNetworkID2.setStatus("mandatory")


class _BrpsBanyanRouter1_Type(OctetString):
    """Custom type brpsBanyanRouter1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_BrpsBanyanRouter1_Type.__name__ = "OctetString"
_BrpsBanyanRouter1_Object = MibScalar
brpsBanyanRouter1 = _BrpsBanyanRouter1_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 5, 10),
    _BrpsBanyanRouter1_Type()
)
brpsBanyanRouter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsBanyanRouter1.setStatus("mandatory")


class _BrpsBanyanRouter2_Type(OctetString):
    """Custom type brpsBanyanRouter2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_BrpsBanyanRouter2_Type.__name__ = "OctetString"
_BrpsBanyanRouter2_Object = MibScalar
brpsBanyanRouter2 = _BrpsBanyanRouter2_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 5, 11),
    _BrpsBanyanRouter2_Type()
)
brpsBanyanRouter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsBanyanRouter2.setStatus("mandatory")


class _BrpsBanyanIPPacket_Type(Integer32):
    """Custom type brpsBanyanIPPacket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrpsBanyanIPPacket_Type.__name__ = "Integer32"
_BrpsBanyanIPPacket_Object = MibScalar
brpsBanyanIPPacket = _BrpsBanyanIPPacket_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 5, 12),
    _BrpsBanyanIPPacket_Type()
)
brpsBanyanIPPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsBanyanIPPacket.setStatus("mandatory")


class _BrpsBanyanErrorCS_Type(Integer32):
    """Custom type brpsBanyanErrorCS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrpsBanyanErrorCS_Type.__name__ = "Integer32"
_BrpsBanyanErrorCS_Object = MibScalar
brpsBanyanErrorCS = _BrpsBanyanErrorCS_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 5, 13),
    _BrpsBanyanErrorCS_Type()
)
brpsBanyanErrorCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsBanyanErrorCS.setStatus("mandatory")


class _BrpsBanyanErrorPT_Type(Integer32):
    """Custom type brpsBanyanErrorPT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrpsBanyanErrorPT_Type.__name__ = "Integer32"
_BrpsBanyanErrorPT_Object = MibScalar
brpsBanyanErrorPT = _BrpsBanyanErrorPT_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 5, 14),
    _BrpsBanyanErrorPT_Type()
)
brpsBanyanErrorPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsBanyanErrorPT.setStatus("mandatory")


class _BrpsBanyanErrorLE_Type(Integer32):
    """Custom type brpsBanyanErrorLE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrpsBanyanErrorLE_Type.__name__ = "Integer32"
_BrpsBanyanErrorLE_Object = MibScalar
brpsBanyanErrorLE = _BrpsBanyanErrorLE_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 5, 15),
    _BrpsBanyanErrorLE_Type()
)
brpsBanyanErrorLE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsBanyanErrorLE.setStatus("mandatory")


class _BrpsBanyanPrintServerStatus_Type(DisplayString):
    """Custom type brpsBanyanPrintServerStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BrpsBanyanPrintServerStatus_Type.__name__ = "DisplayString"
_BrpsBanyanPrintServerStatus_Object = MibScalar
brpsBanyanPrintServerStatus = _BrpsBanyanPrintServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 5, 16),
    _BrpsBanyanPrintServerStatus_Type()
)
brpsBanyanPrintServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsBanyanPrintServerStatus.setStatus("mandatory")


class _BrpsBanyanServerAddress1_Type(OctetString):
    """Custom type brpsBanyanServerAddress1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_BrpsBanyanServerAddress1_Type.__name__ = "OctetString"
_BrpsBanyanServerAddress1_Object = MibScalar
brpsBanyanServerAddress1 = _BrpsBanyanServerAddress1_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 5, 17),
    _BrpsBanyanServerAddress1_Type()
)
brpsBanyanServerAddress1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsBanyanServerAddress1.setStatus("mandatory")


class _BrpsBanyanServerAddress2_Type(OctetString):
    """Custom type brpsBanyanServerAddress2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_BrpsBanyanServerAddress2_Type.__name__ = "OctetString"
_BrpsBanyanServerAddress2_Object = MibScalar
brpsBanyanServerAddress2 = _BrpsBanyanServerAddress2_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 5, 18),
    _BrpsBanyanServerAddress2_Type()
)
brpsBanyanServerAddress2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsBanyanServerAddress2.setStatus("mandatory")


class _BrpsBanyanIPCConnectionInformation_Type(DisplayString):
    """Custom type brpsBanyanIPCConnectionInformation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BrpsBanyanIPCConnectionInformation_Type.__name__ = "DisplayString"
_BrpsBanyanIPCConnectionInformation_Object = MibScalar
brpsBanyanIPCConnectionInformation = _BrpsBanyanIPCConnectionInformation_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 5, 19),
    _BrpsBanyanIPCConnectionInformation_Type()
)
brpsBanyanIPCConnectionInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsBanyanIPCConnectionInformation.setStatus("mandatory")


class _BrpsBanyanIPCSequenceError_Type(Integer32):
    """Custom type brpsBanyanIPCSequenceError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrpsBanyanIPCSequenceError_Type.__name__ = "Integer32"
_BrpsBanyanIPCSequenceError_Object = MibScalar
brpsBanyanIPCSequenceError = _BrpsBanyanIPCSequenceError_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 5, 20),
    _BrpsBanyanIPCSequenceError_Type()
)
brpsBanyanIPCSequenceError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsBanyanIPCSequenceError.setStatus("mandatory")


class _BrpsBanyanIPCListen_Type(DisplayString):
    """Custom type brpsBanyanIPCListen based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BrpsBanyanIPCListen_Type.__name__ = "DisplayString"
_BrpsBanyanIPCListen_Object = MibScalar
brpsBanyanIPCListen = _BrpsBanyanIPCListen_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 5, 21),
    _BrpsBanyanIPCListen_Type()
)
brpsBanyanIPCListen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsBanyanIPCListen.setStatus("mandatory")


class _BrpsBanyanSPPConnectionInformation_Type(DisplayString):
    """Custom type brpsBanyanSPPConnectionInformation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BrpsBanyanSPPConnectionInformation_Type.__name__ = "DisplayString"
_BrpsBanyanSPPConnectionInformation_Object = MibScalar
brpsBanyanSPPConnectionInformation = _BrpsBanyanSPPConnectionInformation_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 5, 22),
    _BrpsBanyanSPPConnectionInformation_Type()
)
brpsBanyanSPPConnectionInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsBanyanSPPConnectionInformation.setStatus("mandatory")


class _BrpsBanyanSPPSequenceError_Type(Integer32):
    """Custom type brpsBanyanSPPSequenceError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrpsBanyanSPPSequenceError_Type.__name__ = "Integer32"
_BrpsBanyanSPPSequenceError_Object = MibScalar
brpsBanyanSPPSequenceError = _BrpsBanyanSPPSequenceError_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 5, 23),
    _BrpsBanyanSPPSequenceError_Type()
)
brpsBanyanSPPSequenceError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsBanyanSPPSequenceError.setStatus("mandatory")


class _BrpsBanyanSPPListen_Type(DisplayString):
    """Custom type brpsBanyanSPPListen based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BrpsBanyanSPPListen_Type.__name__ = "DisplayString"
_BrpsBanyanSPPListen_Object = MibScalar
brpsBanyanSPPListen = _BrpsBanyanSPPListen_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 5, 24),
    _BrpsBanyanSPPListen_Type()
)
brpsBanyanSPPListen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsBanyanSPPListen.setStatus("mandatory")
_Bremail_ObjectIdentity = ObjectIdentity
bremail = _Bremail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6)
)


class _BrpsEmailSupported_Type(Integer32):
    """Custom type brpsEmailSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsEmailSupported_Type.__name__ = "Integer32"
_BrpsEmailSupported_Object = MibScalar
brpsEmailSupported = _BrpsEmailSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 1),
    _BrpsEmailSupported_Type()
)
brpsEmailSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsEmailSupported.setStatus("mandatory")


class _BrpsEmailEnable_Type(Integer32):
    """Custom type brpsEmailEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsEmailEnable_Type.__name__ = "Integer32"
_BrpsEmailEnable_Object = MibScalar
brpsEmailEnable = _BrpsEmailEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 2),
    _BrpsEmailEnable_Type()
)
brpsEmailEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsEmailEnable.setStatus("mandatory")
_BrpsPOP3Address_Type = IpAddress
_BrpsPOP3Address_Object = MibScalar
brpsPOP3Address = _BrpsPOP3Address_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 3),
    _BrpsPOP3Address_Type()
)
brpsPOP3Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsPOP3Address.setStatus("mandatory")
_BrpsSMTPAddress_Type = IpAddress
_BrpsSMTPAddress_Object = MibScalar
brpsSMTPAddress = _BrpsSMTPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 4),
    _BrpsSMTPAddress_Type()
)
brpsSMTPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsSMTPAddress.setStatus("mandatory")
_BrpsPOP3Name_Type = DisplayString
_BrpsPOP3Name_Object = MibScalar
brpsPOP3Name = _BrpsPOP3Name_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 5),
    _BrpsPOP3Name_Type()
)
brpsPOP3Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsPOP3Name.setStatus("mandatory")
_BrpsPOP3Password_Type = DisplayString
_BrpsPOP3Password_Object = MibScalar
brpsPOP3Password = _BrpsPOP3Password_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 6),
    _BrpsPOP3Password_Type()
)
brpsPOP3Password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsPOP3Password.setStatus("mandatory")


class _BrpsPOP3PollFreq_Type(Integer32):
    """Custom type brpsPOP3PollFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 32767),
    )


_BrpsPOP3PollFreq_Type.__name__ = "Integer32"
_BrpsPOP3PollFreq_Object = MibScalar
brpsPOP3PollFreq = _BrpsPOP3PollFreq_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 7),
    _BrpsPOP3PollFreq_Type()
)
brpsPOP3PollFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsPOP3PollFreq.setStatus("mandatory")


class _BrpsPOP3Timeout_Type(Integer32):
    """Custom type brpsPOP3Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 32767),
    )


_BrpsPOP3Timeout_Type.__name__ = "Integer32"
_BrpsPOP3Timeout_Object = MibScalar
brpsPOP3Timeout = _BrpsPOP3Timeout_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 8),
    _BrpsPOP3Timeout_Type()
)
brpsPOP3Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsPOP3Timeout.setStatus("mandatory")


class _BrpsPOP3PasswordSet_Type(Integer32):
    """Custom type brpsPOP3PasswordSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsPOP3PasswordSet_Type.__name__ = "Integer32"
_BrpsPOP3PasswordSet_Object = MibScalar
brpsPOP3PasswordSet = _BrpsPOP3PasswordSet_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 9),
    _BrpsPOP3PasswordSet_Type()
)
brpsPOP3PasswordSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsPOP3PasswordSet.setStatus("mandatory")


class _BrpsPOP3TotalMessage_Type(Integer32):
    """Custom type brpsPOP3TotalMessage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrpsPOP3TotalMessage_Type.__name__ = "Integer32"
_BrpsPOP3TotalMessage_Object = MibScalar
brpsPOP3TotalMessage = _BrpsPOP3TotalMessage_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 10),
    _BrpsPOP3TotalMessage_Type()
)
brpsPOP3TotalMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsPOP3TotalMessage.setStatus("mandatory")


class _BrpsPOP3TotalConnect_Type(Integer32):
    """Custom type brpsPOP3TotalConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrpsPOP3TotalConnect_Type.__name__ = "Integer32"
_BrpsPOP3TotalConnect_Object = MibScalar
brpsPOP3TotalConnect = _BrpsPOP3TotalConnect_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 11),
    _BrpsPOP3TotalConnect_Type()
)
brpsPOP3TotalConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsPOP3TotalConnect.setStatus("mandatory")


class _BrpsPOP3TotalConnectFailure_Type(Integer32):
    """Custom type brpsPOP3TotalConnectFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrpsPOP3TotalConnectFailure_Type.__name__ = "Integer32"
_BrpsPOP3TotalConnectFailure_Object = MibScalar
brpsPOP3TotalConnectFailure = _BrpsPOP3TotalConnectFailure_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 12),
    _BrpsPOP3TotalConnectFailure_Type()
)
brpsPOP3TotalConnectFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsPOP3TotalConnectFailure.setStatus("mandatory")


class _BrpsPOP3TotalConnectionLost_Type(Integer32):
    """Custom type brpsPOP3TotalConnectionLost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrpsPOP3TotalConnectionLost_Type.__name__ = "Integer32"
_BrpsPOP3TotalConnectionLost_Object = MibScalar
brpsPOP3TotalConnectionLost = _BrpsPOP3TotalConnectionLost_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 13),
    _BrpsPOP3TotalConnectionLost_Type()
)
brpsPOP3TotalConnectionLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsPOP3TotalConnectionLost.setStatus("mandatory")


class _BrpsPOP3TotalUserFailure_Type(Integer32):
    """Custom type brpsPOP3TotalUserFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrpsPOP3TotalUserFailure_Type.__name__ = "Integer32"
_BrpsPOP3TotalUserFailure_Object = MibScalar
brpsPOP3TotalUserFailure = _BrpsPOP3TotalUserFailure_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 14),
    _BrpsPOP3TotalUserFailure_Type()
)
brpsPOP3TotalUserFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsPOP3TotalUserFailure.setStatus("mandatory")


class _BrpsPOP3TotalPasswordFailure_Type(Integer32):
    """Custom type brpsPOP3TotalPasswordFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrpsPOP3TotalPasswordFailure_Type.__name__ = "Integer32"
_BrpsPOP3TotalPasswordFailure_Object = MibScalar
brpsPOP3TotalPasswordFailure = _BrpsPOP3TotalPasswordFailure_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 15),
    _BrpsPOP3TotalPasswordFailure_Type()
)
brpsPOP3TotalPasswordFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsPOP3TotalPasswordFailure.setStatus("mandatory")


class _BrpsPOP3TotalIOError_Type(Integer32):
    """Custom type brpsPOP3TotalIOError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrpsPOP3TotalIOError_Type.__name__ = "Integer32"
_BrpsPOP3TotalIOError_Object = MibScalar
brpsPOP3TotalIOError = _BrpsPOP3TotalIOError_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 16),
    _BrpsPOP3TotalIOError_Type()
)
brpsPOP3TotalIOError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsPOP3TotalIOError.setStatus("mandatory")


class _BrpsSMTPTotalMessage_Type(Integer32):
    """Custom type brpsSMTPTotalMessage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrpsSMTPTotalMessage_Type.__name__ = "Integer32"
_BrpsSMTPTotalMessage_Object = MibScalar
brpsSMTPTotalMessage = _BrpsSMTPTotalMessage_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 17),
    _BrpsSMTPTotalMessage_Type()
)
brpsSMTPTotalMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsSMTPTotalMessage.setStatus("mandatory")


class _BrpsSMTPTotalConnect_Type(Integer32):
    """Custom type brpsSMTPTotalConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrpsSMTPTotalConnect_Type.__name__ = "Integer32"
_BrpsSMTPTotalConnect_Object = MibScalar
brpsSMTPTotalConnect = _BrpsSMTPTotalConnect_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 18),
    _BrpsSMTPTotalConnect_Type()
)
brpsSMTPTotalConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsSMTPTotalConnect.setStatus("mandatory")


class _BrpsSMTPTotalConnectFailure_Type(Integer32):
    """Custom type brpsSMTPTotalConnectFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrpsSMTPTotalConnectFailure_Type.__name__ = "Integer32"
_BrpsSMTPTotalConnectFailure_Object = MibScalar
brpsSMTPTotalConnectFailure = _BrpsSMTPTotalConnectFailure_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 19),
    _BrpsSMTPTotalConnectFailure_Type()
)
brpsSMTPTotalConnectFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsSMTPTotalConnectFailure.setStatus("mandatory")


class _BrpsSMTPTotalRecvFromFailure_Type(Integer32):
    """Custom type brpsSMTPTotalRecvFromFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrpsSMTPTotalRecvFromFailure_Type.__name__ = "Integer32"
_BrpsSMTPTotalRecvFromFailure_Object = MibScalar
brpsSMTPTotalRecvFromFailure = _BrpsSMTPTotalRecvFromFailure_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 20),
    _BrpsSMTPTotalRecvFromFailure_Type()
)
brpsSMTPTotalRecvFromFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsSMTPTotalRecvFromFailure.setStatus("mandatory")


class _BrpsSMTPTotalSendToFailure_Type(Integer32):
    """Custom type brpsSMTPTotalSendToFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrpsSMTPTotalSendToFailure_Type.__name__ = "Integer32"
_BrpsSMTPTotalSendToFailure_Object = MibScalar
brpsSMTPTotalSendToFailure = _BrpsSMTPTotalSendToFailure_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 21),
    _BrpsSMTPTotalSendToFailure_Type()
)
brpsSMTPTotalSendToFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsSMTPTotalSendToFailure.setStatus("mandatory")


class _BrpsPOP3Supported_Type(Integer32):
    """Custom type brpsPOP3Supported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsPOP3Supported_Type.__name__ = "Integer32"
_BrpsPOP3Supported_Object = MibScalar
brpsPOP3Supported = _BrpsPOP3Supported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 101),
    _BrpsPOP3Supported_Type()
)
brpsPOP3Supported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsPOP3Supported.setStatus("mandatory")


class _BrpsSMTPServerAuthMethod_Type(Integer32):
    """Custom type brpsSMTPServerAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BrpsSMTPServerAuthMethod_Type.__name__ = "Integer32"
_BrpsSMTPServerAuthMethod_Object = MibScalar
brpsSMTPServerAuthMethod = _BrpsSMTPServerAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 102),
    _BrpsSMTPServerAuthMethod_Type()
)
brpsSMTPServerAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsSMTPServerAuthMethod.setStatus("mandatory")


class _BrpsSMTPAUTHUsername_Type(OctetString):
    """Custom type brpsSMTPAUTHUsername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_BrpsSMTPAUTHUsername_Type.__name__ = "OctetString"
_BrpsSMTPAUTHUsername_Object = MibScalar
brpsSMTPAUTHUsername = _BrpsSMTPAUTHUsername_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 103),
    _BrpsSMTPAUTHUsername_Type()
)
brpsSMTPAUTHUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsSMTPAUTHUsername.setStatus("mandatory")


class _BrpsSMTPAUTHPassword_Type(OctetString):
    """Custom type brpsSMTPAUTHPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrpsSMTPAUTHPassword_Type.__name__ = "OctetString"
_BrpsSMTPAUTHPassword_Object = MibScalar
brpsSMTPAUTHPassword = _BrpsSMTPAUTHPassword_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 104),
    _BrpsSMTPAUTHPassword_Type()
)
brpsSMTPAUTHPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsSMTPAUTHPassword.setStatus("mandatory")


class _BrpsSMTPAUTHPasswordSet_Type(Integer32):
    """Custom type brpsSMTPAUTHPasswordSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsSMTPAUTHPasswordSet_Type.__name__ = "Integer32"
_BrpsSMTPAUTHPasswordSet_Object = MibScalar
brpsSMTPAUTHPasswordSet = _BrpsSMTPAUTHPasswordSet_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 105),
    _BrpsSMTPAUTHPasswordSet_Type()
)
brpsSMTPAUTHPasswordSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsSMTPAUTHPasswordSet.setStatus("mandatory")


class _BrpsSmtpAUTHTimeout_Type(Integer32):
    """Custom type brpsSmtpAUTHTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 32767),
    )


_BrpsSmtpAUTHTimeout_Type.__name__ = "Integer32"
_BrpsSmtpAUTHTimeout_Object = MibScalar
brpsSmtpAUTHTimeout = _BrpsSmtpAUTHTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 106),
    _BrpsSmtpAUTHTimeout_Type()
)
brpsSmtpAUTHTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsSmtpAUTHTimeout.setStatus("mandatory")


class _BrpsPOPbeforeSMTPWait_Type(Integer32):
    """Custom type brpsPOPbeforeSMTPWait based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_BrpsPOPbeforeSMTPWait_Type.__name__ = "Integer32"
_BrpsPOPbeforeSMTPWait_Object = MibScalar
brpsPOPbeforeSMTPWait = _BrpsPOPbeforeSMTPWait_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 107),
    _BrpsPOPbeforeSMTPWait_Type()
)
brpsPOPbeforeSMTPWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsPOPbeforeSMTPWait.setStatus("mandatory")


class _BrpsAPOPEnable_Type(Integer32):
    """Custom type brpsAPOPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsAPOPEnable_Type.__name__ = "Integer32"
_BrpsAPOPEnable_Object = MibScalar
brpsAPOPEnable = _BrpsAPOPEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 108),
    _BrpsAPOPEnable_Type()
)
brpsAPOPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsAPOPEnable.setStatus("mandatory")


class _BrpsSMTPEnhancedAuthSupported_Type(Integer32):
    """Custom type brpsSMTPEnhancedAuthSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BrpsSMTPEnhancedAuthSupported_Type.__name__ = "Integer32"
_BrpsSMTPEnhancedAuthSupported_Object = MibScalar
brpsSMTPEnhancedAuthSupported = _BrpsSMTPEnhancedAuthSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 150),
    _BrpsSMTPEnhancedAuthSupported_Type()
)
brpsSMTPEnhancedAuthSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsSMTPEnhancedAuthSupported.setStatus("mandatory")


class _BrpsAPOPSupported_Type(Integer32):
    """Custom type brpsAPOPSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsAPOPSupported_Type.__name__ = "Integer32"
_BrpsAPOPSupported_Object = MibScalar
brpsAPOPSupported = _BrpsAPOPSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 151),
    _BrpsAPOPSupported_Type()
)
brpsAPOPSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsAPOPSupported.setStatus("mandatory")


class _BrpsEmailSendTestSupported_Type(Integer32):
    """Custom type brpsEmailSendTestSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsEmailSendTestSupported_Type.__name__ = "Integer32"
_BrpsEmailSendTestSupported_Object = MibScalar
brpsEmailSendTestSupported = _BrpsEmailSendTestSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 152),
    _BrpsEmailSendTestSupported_Type()
)
brpsEmailSendTestSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsEmailSendTestSupported.setStatus("mandatory")


class _BrpsEmailRecvTestSupported_Type(Integer32):
    """Custom type brpsEmailRecvTestSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsEmailRecvTestSupported_Type.__name__ = "Integer32"
_BrpsEmailRecvTestSupported_Object = MibScalar
brpsEmailRecvTestSupported = _BrpsEmailRecvTestSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 153),
    _BrpsEmailRecvTestSupported_Type()
)
brpsEmailRecvTestSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsEmailRecvTestSupported.setStatus("mandatory")


class _BrpsChangeSMTPPortSupported_Type(Integer32):
    """Custom type brpsChangeSMTPPortSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsChangeSMTPPortSupported_Type.__name__ = "Integer32"
_BrpsChangeSMTPPortSupported_Object = MibScalar
brpsChangeSMTPPortSupported = _BrpsChangeSMTPPortSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 154),
    _BrpsChangeSMTPPortSupported_Type()
)
brpsChangeSMTPPortSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsChangeSMTPPortSupported.setStatus("mandatory")


class _BrpsSMTPPortNumber_Type(Integer32):
    """Custom type brpsSMTPPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BrpsSMTPPortNumber_Type.__name__ = "Integer32"
_BrpsSMTPPortNumber_Object = MibScalar
brpsSMTPPortNumber = _BrpsSMTPPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 155),
    _BrpsSMTPPortNumber_Type()
)
brpsSMTPPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsSMTPPortNumber.setStatus("mandatory")


class _BrpsChangePOP3PortSupported_Type(Integer32):
    """Custom type brpsChangePOP3PortSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsChangePOP3PortSupported_Type.__name__ = "Integer32"
_BrpsChangePOP3PortSupported_Object = MibScalar
brpsChangePOP3PortSupported = _BrpsChangePOP3PortSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 156),
    _BrpsChangePOP3PortSupported_Type()
)
brpsChangePOP3PortSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsChangePOP3PortSupported.setStatus("mandatory")


class _BrpsPOP3PortNumber_Type(Integer32):
    """Custom type brpsPOP3PortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BrpsPOP3PortNumber_Type.__name__ = "Integer32"
_BrpsPOP3PortNumber_Object = MibScalar
brpsPOP3PortNumber = _BrpsPOP3PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 157),
    _BrpsPOP3PortNumber_Type()
)
brpsPOP3PortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsPOP3PortNumber.setStatus("mandatory")


class _BrpsTmpSMTPServerName_Type(OctetString):
    """Custom type brpsTmpSMTPServerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BrpsTmpSMTPServerName_Type.__name__ = "OctetString"
_BrpsTmpSMTPServerName_Object = MibScalar
brpsTmpSMTPServerName = _BrpsTmpSMTPServerName_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 170),
    _BrpsTmpSMTPServerName_Type()
)
brpsTmpSMTPServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsTmpSMTPServerName.setStatus("mandatory")


class _BrpsTmpSMTPServerAuthMethod_Type(Integer32):
    """Custom type brpsTmpSMTPServerAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BrpsTmpSMTPServerAuthMethod_Type.__name__ = "Integer32"
_BrpsTmpSMTPServerAuthMethod_Object = MibScalar
brpsTmpSMTPServerAuthMethod = _BrpsTmpSMTPServerAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 171),
    _BrpsTmpSMTPServerAuthMethod_Type()
)
brpsTmpSMTPServerAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsTmpSMTPServerAuthMethod.setStatus("mandatory")


class _BrpsTmpSMTPAUTHUsername_Type(OctetString):
    """Custom type brpsTmpSMTPAUTHUsername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_BrpsTmpSMTPAUTHUsername_Type.__name__ = "OctetString"
_BrpsTmpSMTPAUTHUsername_Object = MibScalar
brpsTmpSMTPAUTHUsername = _BrpsTmpSMTPAUTHUsername_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 172),
    _BrpsTmpSMTPAUTHUsername_Type()
)
brpsTmpSMTPAUTHUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsTmpSMTPAUTHUsername.setStatus("mandatory")


class _BrpsTmpSMTPAUTHPassword_Type(OctetString):
    """Custom type brpsTmpSMTPAUTHPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrpsTmpSMTPAUTHPassword_Type.__name__ = "OctetString"
_BrpsTmpSMTPAUTHPassword_Object = MibScalar
brpsTmpSMTPAUTHPassword = _BrpsTmpSMTPAUTHPassword_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 173),
    _BrpsTmpSMTPAUTHPassword_Type()
)
brpsTmpSMTPAUTHPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsTmpSMTPAUTHPassword.setStatus("mandatory")


class _BrpsTmpPOP3ServerName_Type(OctetString):
    """Custom type brpsTmpPOP3ServerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BrpsTmpPOP3ServerName_Type.__name__ = "OctetString"
_BrpsTmpPOP3ServerName_Object = MibScalar
brpsTmpPOP3ServerName = _BrpsTmpPOP3ServerName_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 174),
    _BrpsTmpPOP3ServerName_Type()
)
brpsTmpPOP3ServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsTmpPOP3ServerName.setStatus("mandatory")
_BrpsTmpPOP3Name_Type = DisplayString
_BrpsTmpPOP3Name_Object = MibScalar
brpsTmpPOP3Name = _BrpsTmpPOP3Name_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 175),
    _BrpsTmpPOP3Name_Type()
)
brpsTmpPOP3Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsTmpPOP3Name.setStatus("mandatory")
_BrpsTmpPOP3Password_Type = DisplayString
_BrpsTmpPOP3Password_Object = MibScalar
brpsTmpPOP3Password = _BrpsTmpPOP3Password_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 176),
    _BrpsTmpPOP3Password_Type()
)
brpsTmpPOP3Password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsTmpPOP3Password.setStatus("mandatory")
_BrpsTmpPrintersEmailaddress_Type = OctetString
_BrpsTmpPrintersEmailaddress_Object = MibScalar
brpsTmpPrintersEmailaddress = _BrpsTmpPrintersEmailaddress_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 177),
    _BrpsTmpPrintersEmailaddress_Type()
)
brpsTmpPrintersEmailaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsTmpPrintersEmailaddress.setStatus("mandatory")


class _BrpsTmpAPOPEnable_Type(Integer32):
    """Custom type brpsTmpAPOPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsTmpAPOPEnable_Type.__name__ = "Integer32"
_BrpsTmpAPOPEnable_Object = MibScalar
brpsTmpAPOPEnable = _BrpsTmpAPOPEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 178),
    _BrpsTmpAPOPEnable_Type()
)
brpsTmpAPOPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsTmpAPOPEnable.setStatus("mandatory")


class _BrpsTmpSMTPAUTHPasswordModified_Type(Integer32):
    """Custom type brpsTmpSMTPAUTHPasswordModified based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsTmpSMTPAUTHPasswordModified_Type.__name__ = "Integer32"
_BrpsTmpSMTPAUTHPasswordModified_Object = MibScalar
brpsTmpSMTPAUTHPasswordModified = _BrpsTmpSMTPAUTHPasswordModified_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 179),
    _BrpsTmpSMTPAUTHPasswordModified_Type()
)
brpsTmpSMTPAUTHPasswordModified.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsTmpSMTPAUTHPasswordModified.setStatus("mandatory")


class _BrpsTmpPOP3PasswordModified_Type(Integer32):
    """Custom type brpsTmpPOP3PasswordModified based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsTmpPOP3PasswordModified_Type.__name__ = "Integer32"
_BrpsTmpPOP3PasswordModified_Object = MibScalar
brpsTmpPOP3PasswordModified = _BrpsTmpPOP3PasswordModified_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 180),
    _BrpsTmpPOP3PasswordModified_Type()
)
brpsTmpPOP3PasswordModified.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsTmpPOP3PasswordModified.setStatus("mandatory")


class _BrpsTmpSMTPPortNumber_Type(Integer32):
    """Custom type brpsTmpSMTPPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BrpsTmpSMTPPortNumber_Type.__name__ = "Integer32"
_BrpsTmpSMTPPortNumber_Object = MibScalar
brpsTmpSMTPPortNumber = _BrpsTmpSMTPPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 181),
    _BrpsTmpSMTPPortNumber_Type()
)
brpsTmpSMTPPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsTmpSMTPPortNumber.setStatus("mandatory")


class _BrpsTmpPOP3PortNumber_Type(Integer32):
    """Custom type brpsTmpPOP3PortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BrpsTmpPOP3PortNumber_Type.__name__ = "Integer32"
_BrpsTmpPOP3PortNumber_Object = MibScalar
brpsTmpPOP3PortNumber = _BrpsTmpPOP3PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 182),
    _BrpsTmpPOP3PortNumber_Type()
)
brpsTmpPOP3PortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsTmpPOP3PortNumber.setStatus("mandatory")


class _BrpsEmailSendTestMail_Type(Integer32):
    """Custom type brpsEmailSendTestMail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsEmailSendTestMail_Type.__name__ = "Integer32"
_BrpsEmailSendTestMail_Object = MibScalar
brpsEmailSendTestMail = _BrpsEmailSendTestMail_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 200),
    _BrpsEmailSendTestMail_Type()
)
brpsEmailSendTestMail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsEmailSendTestMail.setStatus("mandatory")


class _BrpsEmailTestDestinationAddress_Type(DisplayString):
    """Custom type brpsEmailTestDestinationAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_BrpsEmailTestDestinationAddress_Type.__name__ = "DisplayString"
_BrpsEmailTestDestinationAddress_Object = MibScalar
brpsEmailTestDestinationAddress = _BrpsEmailTestDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 201),
    _BrpsEmailTestDestinationAddress_Type()
)
brpsEmailTestDestinationAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsEmailTestDestinationAddress.setStatus("mandatory")


class _BrpsEmailSendTestCall_Type(Integer32):
    """Custom type brpsEmailSendTestCall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BrpsEmailSendTestCall_Type.__name__ = "Integer32"
_BrpsEmailSendTestCall_Object = MibScalar
brpsEmailSendTestCall = _BrpsEmailSendTestCall_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 210),
    _BrpsEmailSendTestCall_Type()
)
brpsEmailSendTestCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsEmailSendTestCall.setStatus("mandatory")


class _BrpsEmailRecvTestCall_Type(Integer32):
    """Custom type brpsEmailRecvTestCall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BrpsEmailRecvTestCall_Type.__name__ = "Integer32"
_BrpsEmailRecvTestCall_Object = MibScalar
brpsEmailRecvTestCall = _BrpsEmailRecvTestCall_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 211),
    _BrpsEmailRecvTestCall_Type()
)
brpsEmailRecvTestCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsEmailRecvTestCall.setStatus("mandatory")


class _BrpsEmailSendRecvTestCall_Type(Integer32):
    """Custom type brpsEmailSendRecvTestCall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BrpsEmailSendRecvTestCall_Type.__name__ = "Integer32"
_BrpsEmailSendRecvTestCall_Object = MibScalar
brpsEmailSendRecvTestCall = _BrpsEmailSendRecvTestCall_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 212),
    _BrpsEmailSendRecvTestCall_Type()
)
brpsEmailSendRecvTestCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsEmailSendRecvTestCall.setStatus("mandatory")


class _BrpsEmailTestResult_Type(Integer32):
    """Custom type brpsEmailTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrpsEmailTestResult_Type.__name__ = "Integer32"
_BrpsEmailTestResult_Object = MibScalar
brpsEmailTestResult = _BrpsEmailTestResult_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 220),
    _BrpsEmailTestResult_Type()
)
brpsEmailTestResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsEmailTestResult.setStatus("mandatory")


class _BrpsPOP3TotalAPOPFailure_Type(Integer32):
    """Custom type brpsPOP3TotalAPOPFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrpsPOP3TotalAPOPFailure_Type.__name__ = "Integer32"
_BrpsPOP3TotalAPOPFailure_Object = MibScalar
brpsPOP3TotalAPOPFailure = _BrpsPOP3TotalAPOPFailure_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 6, 221),
    _BrpsPOP3TotalAPOPFailure_Type()
)
brpsPOP3TotalAPOPFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsPOP3TotalAPOPFailure.setStatus("mandatory")
_Brdlc_ObjectIdentity = ObjectIdentity
brdlc = _Brdlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 7)
)


class _BrpsDLCSupported_Type(Integer32):
    """Custom type brpsDLCSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsDLCSupported_Type.__name__ = "Integer32"
_BrpsDLCSupported_Object = MibScalar
brpsDLCSupported = _BrpsDLCSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 7, 1),
    _BrpsDLCSupported_Type()
)
brpsDLCSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsDLCSupported.setStatus("mandatory")


class _BrpsDLCEnable_Type(Integer32):
    """Custom type brpsDLCEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsDLCEnable_Type.__name__ = "Integer32"
_BrpsDLCEnable_Object = MibScalar
brpsDLCEnable = _BrpsDLCEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 7, 2),
    _BrpsDLCEnable_Type()
)
brpsDLCEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsDLCEnable.setStatus("mandatory")


class _BrpsDLCPrintStatus_Type(DisplayString):
    """Custom type brpsDLCPrintStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrpsDLCPrintStatus_Type.__name__ = "DisplayString"
_BrpsDLCPrintStatus_Object = MibScalar
brpsDLCPrintStatus = _BrpsDLCPrintStatus_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 7, 3),
    _BrpsDLCPrintStatus_Type()
)
brpsDLCPrintStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsDLCPrintStatus.setStatus("mandatory")


class _BrpsDLCLLCState_Type(Integer32):
    """Custom type brpsDLCLLCState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrpsDLCLLCState_Type.__name__ = "Integer32"
_BrpsDLCLLCState_Object = MibScalar
brpsDLCLLCState = _BrpsDLCLLCState_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 7, 4),
    _BrpsDLCLLCState_Type()
)
brpsDLCLLCState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsDLCLLCState.setStatus("mandatory")


class _BrpsDLCLLCConnectHost_Type(DisplayString):
    """Custom type brpsDLCLLCConnectHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrpsDLCLLCConnectHost_Type.__name__ = "DisplayString"
_BrpsDLCLLCConnectHost_Object = MibScalar
brpsDLCLLCConnectHost = _BrpsDLCLLCConnectHost_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 7, 5),
    _BrpsDLCLLCConnectHost_Type()
)
brpsDLCLLCConnectHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsDLCLLCConnectHost.setStatus("mandatory")


class _BrpsDLCLLCLastIFrame_Type(Integer32):
    """Custom type brpsDLCLLCLastIFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrpsDLCLLCLastIFrame_Type.__name__ = "Integer32"
_BrpsDLCLLCLastIFrame_Object = MibScalar
brpsDLCLLCLastIFrame = _BrpsDLCLLCLastIFrame_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 7, 6),
    _BrpsDLCLLCLastIFrame_Type()
)
brpsDLCLLCLastIFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsDLCLLCLastIFrame.setStatus("mandatory")


class _BrpsDLCLLCRecvPacket_Type(Integer32):
    """Custom type brpsDLCLLCRecvPacket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrpsDLCLLCRecvPacket_Type.__name__ = "Integer32"
_BrpsDLCLLCRecvPacket_Object = MibScalar
brpsDLCLLCRecvPacket = _BrpsDLCLLCRecvPacket_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 7, 7),
    _BrpsDLCLLCRecvPacket_Type()
)
brpsDLCLLCRecvPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsDLCLLCRecvPacket.setStatus("mandatory")


class _BrpsDLCLLCPortStatus_Type(DisplayString):
    """Custom type brpsDLCLLCPortStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrpsDLCLLCPortStatus_Type.__name__ = "DisplayString"
_BrpsDLCLLCPortStatus_Object = MibScalar
brpsDLCLLCPortStatus = _BrpsDLCLLCPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 7, 8),
    _BrpsDLCLLCPortStatus_Type()
)
brpsDLCLLCPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsDLCLLCPortStatus.setStatus("mandatory")
_Brnetbeui_ObjectIdentity = ObjectIdentity
brnetbeui = _Brnetbeui_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 8)
)


class _BrpsNetBEUISupported_Type(Integer32):
    """Custom type brpsNetBEUISupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsNetBEUISupported_Type.__name__ = "Integer32"
_BrpsNetBEUISupported_Object = MibScalar
brpsNetBEUISupported = _BrpsNetBEUISupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 8, 1),
    _BrpsNetBEUISupported_Type()
)
brpsNetBEUISupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsNetBEUISupported.setStatus("mandatory")


class _BrpsNetBEUIEnable_Type(Integer32):
    """Custom type brpsNetBEUIEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsNetBEUIEnable_Type.__name__ = "Integer32"
_BrpsNetBEUIEnable_Object = MibScalar
brpsNetBEUIEnable = _BrpsNetBEUIEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 8, 2),
    _BrpsNetBEUIEnable_Type()
)
brpsNetBEUIEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsNetBEUIEnable.setStatus("mandatory")


class _BrpsNetBEUIDomain_Type(DisplayString):
    """Custom type brpsNetBEUIDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_BrpsNetBEUIDomain_Type.__name__ = "DisplayString"
_BrpsNetBEUIDomain_Object = MibScalar
brpsNetBEUIDomain = _BrpsNetBEUIDomain_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 8, 3),
    _BrpsNetBEUIDomain_Type()
)
brpsNetBEUIDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsNetBEUIDomain.setStatus("mandatory")


class _BrpsNetBIOSIPSupported_Type(Integer32):
    """Custom type brpsNetBIOSIPSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsNetBIOSIPSupported_Type.__name__ = "Integer32"
_BrpsNetBIOSIPSupported_Object = MibScalar
brpsNetBIOSIPSupported = _BrpsNetBIOSIPSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 8, 4),
    _BrpsNetBIOSIPSupported_Type()
)
brpsNetBIOSIPSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsNetBIOSIPSupported.setStatus("mandatory")


class _BrpsNetBIOSIPEnable_Type(Integer32):
    """Custom type brpsNetBIOSIPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsNetBIOSIPEnable_Type.__name__ = "Integer32"
_BrpsNetBIOSIPEnable_Object = MibScalar
brpsNetBIOSIPEnable = _BrpsNetBIOSIPEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 8, 5),
    _BrpsNetBIOSIPEnable_Type()
)
brpsNetBIOSIPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsNetBIOSIPEnable.setStatus("mandatory")


class _BrpsNetBIOSIPMethod_Type(Integer32):
    """Custom type brpsNetBIOSIPMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsNetBIOSIPMethod_Type.__name__ = "Integer32"
_BrpsNetBIOSIPMethod_Object = MibScalar
brpsNetBIOSIPMethod = _BrpsNetBIOSIPMethod_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 8, 6),
    _BrpsNetBIOSIPMethod_Type()
)
brpsNetBIOSIPMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsNetBIOSIPMethod.setStatus("mandatory")
_BrpsNetBIOSPrimaryWINSAddr_Type = IpAddress
_BrpsNetBIOSPrimaryWINSAddr_Object = MibScalar
brpsNetBIOSPrimaryWINSAddr = _BrpsNetBIOSPrimaryWINSAddr_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 8, 7),
    _BrpsNetBIOSPrimaryWINSAddr_Type()
)
brpsNetBIOSPrimaryWINSAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsNetBIOSPrimaryWINSAddr.setStatus("mandatory")
_BrpsNetBIOSSecondaryWINSAddr_Type = IpAddress
_BrpsNetBIOSSecondaryWINSAddr_Object = MibScalar
brpsNetBIOSSecondaryWINSAddr = _BrpsNetBIOSSecondaryWINSAddr_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 8, 8),
    _BrpsNetBIOSSecondaryWINSAddr_Type()
)
brpsNetBIOSSecondaryWINSAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsNetBIOSSecondaryWINSAddr.setStatus("mandatory")


class _BrpsNetBIOSPrintingSupported_Type(Integer32):
    """Custom type brpsNetBIOSPrintingSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsNetBIOSPrintingSupported_Type.__name__ = "Integer32"
_BrpsNetBIOSPrintingSupported_Object = MibScalar
brpsNetBIOSPrintingSupported = _BrpsNetBIOSPrintingSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 8, 101),
    _BrpsNetBIOSPrintingSupported_Type()
)
brpsNetBIOSPrintingSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsNetBIOSPrintingSupported.setStatus("mandatory")
_Bripp_ObjectIdentity = ObjectIdentity
bripp = _Bripp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 9)
)


class _BrpsIPPSupported_Type(Integer32):
    """Custom type brpsIPPSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsIPPSupported_Type.__name__ = "Integer32"
_BrpsIPPSupported_Object = MibScalar
brpsIPPSupported = _BrpsIPPSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 9, 1),
    _BrpsIPPSupported_Type()
)
brpsIPPSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsIPPSupported.setStatus("mandatory")


class _BrpsIPPEnable_Type(Integer32):
    """Custom type brpsIPPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsIPPEnable_Type.__name__ = "Integer32"
_BrpsIPPEnable_Object = MibScalar
brpsIPPEnable = _BrpsIPPEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 9, 2),
    _BrpsIPPEnable_Type()
)
brpsIPPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsIPPEnable.setStatus("mandatory")


class _BrIPPRegularPortEnable_Type(Integer32):
    """Custom type brIPPRegularPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrIPPRegularPortEnable_Type.__name__ = "Integer32"
_BrIPPRegularPortEnable_Object = MibScalar
brIPPRegularPortEnable = _BrIPPRegularPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 9, 3),
    _BrIPPRegularPortEnable_Type()
)
brIPPRegularPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brIPPRegularPortEnable.setStatus("mandatory")


class _BrIPPSSLPortEnable_Type(Integer32):
    """Custom type brIPPSSLPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrIPPSSLPortEnable_Type.__name__ = "Integer32"
_BrIPPSSLPortEnable_Object = MibScalar
brIPPSSLPortEnable = _BrIPPSSLPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 9, 4),
    _BrIPPSSLPortEnable_Type()
)
brIPPSSLPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brIPPSSLPortEnable.setStatus("mandatory")


class _BrIPPOriginalPortEnable_Type(Integer32):
    """Custom type brIPPOriginalPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrIPPOriginalPortEnable_Type.__name__ = "Integer32"
_BrIPPOriginalPortEnable_Object = MibScalar
brIPPOriginalPortEnable = _BrIPPOriginalPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 9, 5),
    _BrIPPOriginalPortEnable_Type()
)
brIPPOriginalPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brIPPOriginalPortEnable.setStatus("mandatory")
_Brntsend_ObjectIdentity = ObjectIdentity
brntsend = _Brntsend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 10)
)


class _BrpsNtSendSupported_Type(Integer32):
    """Custom type brpsNtSendSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsNtSendSupported_Type.__name__ = "Integer32"
_BrpsNtSendSupported_Object = MibScalar
brpsNtSendSupported = _BrpsNtSendSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 10, 1),
    _BrpsNtSendSupported_Type()
)
brpsNtSendSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsNtSendSupported.setStatus("mandatory")


class _BrpsNtSendEnable_Type(Integer32):
    """Custom type brpsNtSendEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsNtSendEnable_Type.__name__ = "Integer32"
_BrpsNtSendEnable_Object = MibScalar
brpsNtSendEnable = _BrpsNtSendEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 5, 10, 2),
    _BrpsNtSendEnable_Type()
)
brpsNtSendEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsNtSendEnable.setStatus("mandatory")
_Brfirmware_ObjectIdentity = ObjectIdentity
brfirmware = _Brfirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 6)
)
_BrpsFirmwareIPAddress_Type = IpAddress
_BrpsFirmwareIPAddress_Object = MibScalar
brpsFirmwareIPAddress = _BrpsFirmwareIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 6, 1),
    _BrpsFirmwareIPAddress_Type()
)
brpsFirmwareIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsFirmwareIPAddress.setStatus("mandatory")
_BrpsFirmwareHost_Type = DisplayString
_BrpsFirmwareHost_Object = MibScalar
brpsFirmwareHost = _BrpsFirmwareHost_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 6, 2),
    _BrpsFirmwareHost_Type()
)
brpsFirmwareHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsFirmwareHost.setStatus("mandatory")
_BrpsFirmwareFile_Type = DisplayString
_BrpsFirmwareFile_Object = MibScalar
brpsFirmwareFile = _BrpsFirmwareFile_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 6, 3),
    _BrpsFirmwareFile_Type()
)
brpsFirmwareFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsFirmwareFile.setStatus("mandatory")


class _BrpsFirmwareReload_Type(Integer32):
    """Custom type brpsFirmwareReload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsFirmwareReload_Type.__name__ = "Integer32"
_BrpsFirmwareReload_Object = MibScalar
brpsFirmwareReload = _BrpsFirmwareReload_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 6, 4),
    _BrpsFirmwareReload_Type()
)
brpsFirmwareReload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsFirmwareReload.setStatus("mandatory")
_BrpsFirmwareDescription_Type = DisplayString
_BrpsFirmwareDescription_Object = MibScalar
brpsFirmwareDescription = _BrpsFirmwareDescription_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 6, 5),
    _BrpsFirmwareDescription_Type()
)
brpsFirmwareDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsFirmwareDescription.setStatus("mandatory")


class _BrpsFirmwareXModem_Type(Integer32):
    """Custom type brpsFirmwareXModem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsFirmwareXModem_Type.__name__ = "Integer32"
_BrpsFirmwareXModem_Object = MibScalar
brpsFirmwareXModem = _BrpsFirmwareXModem_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 6, 6),
    _BrpsFirmwareXModem_Type()
)
brpsFirmwareXModem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsFirmwareXModem.setStatus("mandatory")


class _BrpsFirmwareAdvancedAddressSupported_Type(Integer32):
    """Custom type brpsFirmwareAdvancedAddressSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrpsFirmwareAdvancedAddressSupported_Type.__name__ = "Integer32"
_BrpsFirmwareAdvancedAddressSupported_Object = MibScalar
brpsFirmwareAdvancedAddressSupported = _BrpsFirmwareAdvancedAddressSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 6, 7),
    _BrpsFirmwareAdvancedAddressSupported_Type()
)
brpsFirmwareAdvancedAddressSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsFirmwareAdvancedAddressSupported.setStatus("mandatory")


class _BrpsFirmwareAdvancedAddress_Type(DisplayString):
    """Custom type brpsFirmwareAdvancedAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BrpsFirmwareAdvancedAddress_Type.__name__ = "DisplayString"
_BrpsFirmwareAdvancedAddress_Object = MibScalar
brpsFirmwareAdvancedAddress = _BrpsFirmwareAdvancedAddress_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 1240, 6, 8),
    _BrpsFirmwareAdvancedAddress_Type()
)
brpsFirmwareAdvancedAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brpsFirmwareAdvancedAddress.setStatus("mandatory")
_BrnetConfigOpt_ObjectIdentity = ObjectIdentity
brnetConfigOpt = _BrnetConfigOpt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435)
)
_Broriginalprotocol_ObjectIdentity = ObjectIdentity
broriginalprotocol = _Broriginalprotocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5)
)
_Broriginaltcpip_ObjectIdentity = ObjectIdentity
broriginaltcpip = _Broriginaltcpip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 2)
)


class _BrLPDType_Type(Integer32):
    """Custom type brLPDType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_BrLPDType_Type.__name__ = "Integer32"
_BrLPDType_Object = MibScalar
brLPDType = _BrLPDType_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 2, 1),
    _BrLPDType_Type()
)
brLPDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLPDType.setStatus("mandatory")
_Broriginalftp_ObjectIdentity = ObjectIdentity
broriginalftp = _Broriginalftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 10)
)


class _BrFTPSupported_Type(Integer32):
    """Custom type brFTPSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrFTPSupported_Type.__name__ = "Integer32"
_BrFTPSupported_Object = MibScalar
brFTPSupported = _BrFTPSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 10, 1),
    _BrFTPSupported_Type()
)
brFTPSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brFTPSupported.setStatus("mandatory")


class _BrFTPEnable_Type(Integer32):
    """Custom type brFTPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrFTPEnable_Type.__name__ = "Integer32"
_BrFTPEnable_Object = MibScalar
brFTPEnable = _BrFTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 10, 2),
    _BrFTPEnable_Type()
)
brFTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brFTPEnable.setStatus("mandatory")
_Broriginalupnp_ObjectIdentity = ObjectIdentity
broriginalupnp = _Broriginalupnp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 11)
)


class _BrUPnPSupported_Type(Integer32):
    """Custom type brUPnPSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrUPnPSupported_Type.__name__ = "Integer32"
_BrUPnPSupported_Object = MibScalar
brUPnPSupported = _BrUPnPSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 11, 1),
    _BrUPnPSupported_Type()
)
brUPnPSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brUPnPSupported.setStatus("mandatory")


class _BrUPnPEnable_Type(Integer32):
    """Custom type brUPnPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrUPnPEnable_Type.__name__ = "Integer32"
_BrUPnPEnable_Object = MibScalar
brUPnPEnable = _BrUPnPEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 11, 2),
    _BrUPnPEnable_Type()
)
brUPnPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brUPnPEnable.setStatus("mandatory")
_Broriginalapipa_ObjectIdentity = ObjectIdentity
broriginalapipa = _Broriginalapipa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 12)
)


class _BrAPIPASupported_Type(Integer32):
    """Custom type brAPIPASupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrAPIPASupported_Type.__name__ = "Integer32"
_BrAPIPASupported_Object = MibScalar
brAPIPASupported = _BrAPIPASupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 12, 1),
    _BrAPIPASupported_Type()
)
brAPIPASupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brAPIPASupported.setStatus("mandatory")


class _BrAPIPAEnable_Type(Integer32):
    """Custom type brAPIPAEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrAPIPAEnable_Type.__name__ = "Integer32"
_BrAPIPAEnable_Object = MibScalar
brAPIPAEnable = _BrAPIPAEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 12, 2),
    _BrAPIPAEnable_Type()
)
brAPIPAEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brAPIPAEnable.setStatus("mandatory")
_Broriginalmdns_ObjectIdentity = ObjectIdentity
broriginalmdns = _Broriginalmdns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 13)
)


class _BrmDNSSupported_Type(Integer32):
    """Custom type brmDNSSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrmDNSSupported_Type.__name__ = "Integer32"
_BrmDNSSupported_Object = MibScalar
brmDNSSupported = _BrmDNSSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 13, 1),
    _BrmDNSSupported_Type()
)
brmDNSSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brmDNSSupported.setStatus("mandatory")


class _BrmDNSEnable_Type(Integer32):
    """Custom type brmDNSEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrmDNSEnable_Type.__name__ = "Integer32"
_BrmDNSEnable_Object = MibScalar
brmDNSEnable = _BrmDNSEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 13, 2),
    _BrmDNSEnable_Type()
)
brmDNSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brmDNSEnable.setStatus("mandatory")


class _BrmDNSPrinterName_Type(DisplayString):
    """Custom type brmDNSPrinterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BrmDNSPrinterName_Type.__name__ = "DisplayString"
_BrmDNSPrinterName_Object = MibScalar
brmDNSPrinterName = _BrmDNSPrinterName_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 13, 3),
    _BrmDNSPrinterName_Type()
)
brmDNSPrinterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brmDNSPrinterName.setStatus("mandatory")
_BroriginalLAA_ObjectIdentity = ObjectIdentity
broriginalLAA = _BroriginalLAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 14)
)


class _BrLAASupported_Type(Integer32):
    """Custom type brLAASupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrLAASupported_Type.__name__ = "Integer32"
_BrLAASupported_Object = MibScalar
brLAASupported = _BrLAASupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 14, 1),
    _BrLAASupported_Type()
)
brLAASupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLAASupported.setStatus("mandatory")


class _BrLAAMacAddress_Type(OctetString):
    """Custom type brLAAMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_BrLAAMacAddress_Type.__name__ = "OctetString"
_BrLAAMacAddress_Object = MibScalar
brLAAMacAddress = _BrLAAMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 14, 2),
    _BrLAAMacAddress_Type()
)
brLAAMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLAAMacAddress.setStatus("mandatory")
_BroriginalIPv6_ObjectIdentity = ObjectIdentity
broriginalIPv6 = _BroriginalIPv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 15)
)


class _BrIPv6Supported_Type(Integer32):
    """Custom type brIPv6Supported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrIPv6Supported_Type.__name__ = "Integer32"
_BrIPv6Supported_Object = MibScalar
brIPv6Supported = _BrIPv6Supported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 15, 1),
    _BrIPv6Supported_Type()
)
brIPv6Supported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brIPv6Supported.setStatus("mandatory")


class _BrIPv6Enable_Type(Integer32):
    """Custom type brIPv6Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrIPv6Enable_Type.__name__ = "Integer32"
_BrIPv6Enable_Object = MibScalar
brIPv6Enable = _BrIPv6Enable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 15, 2),
    _BrIPv6Enable_Type()
)
brIPv6Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brIPv6Enable.setStatus("mandatory")


class _BrIPv6Priority_Type(Integer32):
    """Custom type brIPv6Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrIPv6Priority_Type.__name__ = "Integer32"
_BrIPv6Priority_Object = MibScalar
brIPv6Priority = _BrIPv6Priority_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 15, 3),
    _BrIPv6Priority_Type()
)
brIPv6Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brIPv6Priority.setStatus("mandatory")
_Broriginaltelnet_ObjectIdentity = ObjectIdentity
broriginaltelnet = _Broriginaltelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 16)
)


class _BrtelnetSupported_Type(Integer32):
    """Custom type brtelnetSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrtelnetSupported_Type.__name__ = "Integer32"
_BrtelnetSupported_Object = MibScalar
brtelnetSupported = _BrtelnetSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 16, 1),
    _BrtelnetSupported_Type()
)
brtelnetSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brtelnetSupported.setStatus("mandatory")


class _BrtelnetEnable_Type(Integer32):
    """Custom type brtelnetEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrtelnetEnable_Type.__name__ = "Integer32"
_BrtelnetEnable_Object = MibScalar
brtelnetEnable = _BrtelnetEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 16, 2),
    _BrtelnetEnable_Type()
)
brtelnetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brtelnetEnable.setStatus("mandatory")
_BroriginalEWS_ObjectIdentity = ObjectIdentity
broriginalEWS = _BroriginalEWS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 17)
)


class _BrEWSSupported_Type(Integer32):
    """Custom type brEWSSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrEWSSupported_Type.__name__ = "Integer32"
_BrEWSSupported_Object = MibScalar
brEWSSupported = _BrEWSSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 17, 1),
    _BrEWSSupported_Type()
)
brEWSSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brEWSSupported.setStatus("mandatory")


class _BrEWSEnable_Type(Integer32):
    """Custom type brEWSEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrEWSEnable_Type.__name__ = "Integer32"
_BrEWSEnable_Object = MibScalar
brEWSEnable = _BrEWSEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 17, 2),
    _BrEWSEnable_Type()
)
brEWSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brEWSEnable.setStatus("mandatory")


class _BrEWSRegularPortEnable_Type(Integer32):
    """Custom type brEWSRegularPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrEWSRegularPortEnable_Type.__name__ = "Integer32"
_BrEWSRegularPortEnable_Object = MibScalar
brEWSRegularPortEnable = _BrEWSRegularPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 17, 3),
    _BrEWSRegularPortEnable_Type()
)
brEWSRegularPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brEWSRegularPortEnable.setStatus("mandatory")


class _BrEWSSSLPortEnable_Type(Integer32):
    """Custom type brEWSSSLPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrEWSSSLPortEnable_Type.__name__ = "Integer32"
_BrEWSSSLPortEnable_Object = MibScalar
brEWSSSLPortEnable = _BrEWSSSLPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 17, 4),
    _BrEWSSSLPortEnable_Type()
)
brEWSSSLPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brEWSSSLPortEnable.setStatus("mandatory")
_BroriginalSNMP_ObjectIdentity = ObjectIdentity
broriginalSNMP = _BroriginalSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 18)
)


class _BrSNMPSupported_Type(Integer32):
    """Custom type brSNMPSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrSNMPSupported_Type.__name__ = "Integer32"
_BrSNMPSupported_Object = MibScalar
brSNMPSupported = _BrSNMPSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 18, 1),
    _BrSNMPSupported_Type()
)
brSNMPSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brSNMPSupported.setStatus("mandatory")


class _BrSNMPEnable_Type(Integer32):
    """Custom type brSNMPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrSNMPEnable_Type.__name__ = "Integer32"
_BrSNMPEnable_Object = MibScalar
brSNMPEnable = _BrSNMPEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 18, 2),
    _BrSNMPEnable_Type()
)
brSNMPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brSNMPEnable.setStatus("mandatory")


class _BrSNMPV3Supported_Type(Integer32):
    """Custom type brSNMPV3Supported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrSNMPV3Supported_Type.__name__ = "Integer32"
_BrSNMPV3Supported_Object = MibScalar
brSNMPV3Supported = _BrSNMPV3Supported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 18, 10),
    _BrSNMPV3Supported_Type()
)
brSNMPV3Supported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brSNMPV3Supported.setStatus("mandatory")


class _BrSNMPCommMode_Type(Integer32):
    """Custom type brSNMPCommMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_BrSNMPCommMode_Type.__name__ = "Integer32"
_BrSNMPCommMode_Object = MibScalar
brSNMPCommMode = _BrSNMPCommMode_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 18, 11),
    _BrSNMPCommMode_Type()
)
brSNMPCommMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brSNMPCommMode.setStatus("mandatory")


class _BrSNMPV3UserName_Type(DisplayString):
    """Custom type brSNMPV3UserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BrSNMPV3UserName_Type.__name__ = "DisplayString"
_BrSNMPV3UserName_Object = MibScalar
brSNMPV3UserName = _BrSNMPV3UserName_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 18, 12),
    _BrSNMPV3UserName_Type()
)
brSNMPV3UserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brSNMPV3UserName.setStatus("mandatory")


class _BrSNMPV3KeyType_Type(Integer32):
    """Custom type brSNMPV3KeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_BrSNMPV3KeyType_Type.__name__ = "Integer32"
_BrSNMPV3KeyType_Object = MibScalar
brSNMPV3KeyType = _BrSNMPV3KeyType_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 18, 13),
    _BrSNMPV3KeyType_Type()
)
brSNMPV3KeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brSNMPV3KeyType.setStatus("mandatory")


class _BrSNMPV3AuthKey_Type(OctetString):
    """Custom type brSNMPV3AuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BrSNMPV3AuthKey_Type.__name__ = "OctetString"
_BrSNMPV3AuthKey_Object = MibScalar
brSNMPV3AuthKey = _BrSNMPV3AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 18, 14),
    _BrSNMPV3AuthKey_Type()
)
brSNMPV3AuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brSNMPV3AuthKey.setStatus("mandatory")


class _BrSNMPV3AuthPassword_Type(DisplayString):
    """Custom type brSNMPV3AuthPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_BrSNMPV3AuthPassword_Type.__name__ = "DisplayString"
_BrSNMPV3AuthPassword_Object = MibScalar
brSNMPV3AuthPassword = _BrSNMPV3AuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 18, 15),
    _BrSNMPV3AuthPassword_Type()
)
brSNMPV3AuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brSNMPV3AuthPassword.setStatus("mandatory")


class _BrSNMPV3PrivKey_Type(OctetString):
    """Custom type brSNMPV3PrivKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BrSNMPV3PrivKey_Type.__name__ = "OctetString"
_BrSNMPV3PrivKey_Object = MibScalar
brSNMPV3PrivKey = _BrSNMPV3PrivKey_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 18, 16),
    _BrSNMPV3PrivKey_Type()
)
brSNMPV3PrivKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brSNMPV3PrivKey.setStatus("mandatory")


class _BrSNMPV3PrivPassword_Type(DisplayString):
    """Custom type brSNMPV3PrivPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_BrSNMPV3PrivPassword_Type.__name__ = "DisplayString"
_BrSNMPV3PrivPassword_Object = MibScalar
brSNMPV3PrivPassword = _BrSNMPV3PrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 18, 17),
    _BrSNMPV3PrivPassword_Type()
)
brSNMPV3PrivPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brSNMPV3PrivPassword.setStatus("mandatory")


class _BrSNMPV3ContextName_Type(DisplayString):
    """Custom type brSNMPV3ContextName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrSNMPV3ContextName_Type.__name__ = "DisplayString"
_BrSNMPV3ContextName_Object = MibScalar
brSNMPV3ContextName = _BrSNMPV3ContextName_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 18, 18),
    _BrSNMPV3ContextName_Type()
)
brSNMPV3ContextName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brSNMPV3ContextName.setStatus("mandatory")
_Broriginalldap_ObjectIdentity = ObjectIdentity
broriginalldap = _Broriginalldap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 19)
)


class _BrLdapSupported_Type(Integer32):
    """Custom type brLdapSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrLdapSupported_Type.__name__ = "Integer32"
_BrLdapSupported_Object = MibScalar
brLdapSupported = _BrLdapSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 19, 1),
    _BrLdapSupported_Type()
)
brLdapSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLdapSupported.setStatus("mandatory")


class _BrLdapEnable_Type(Integer32):
    """Custom type brLdapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrLdapEnable_Type.__name__ = "Integer32"
_BrLdapEnable_Object = MibScalar
brLdapEnable = _BrLdapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 19, 2),
    _BrLdapEnable_Type()
)
brLdapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLdapEnable.setStatus("mandatory")


class _BrLdapTimeout_Type(Integer32):
    """Custom type brLdapTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_BrLdapTimeout_Type.__name__ = "Integer32"
_BrLdapTimeout_Object = MibScalar
brLdapTimeout = _BrLdapTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 19, 3),
    _BrLdapTimeout_Type()
)
brLdapTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLdapTimeout.setStatus("mandatory")


class _BrLdapTimeoutSupported_Type(Integer32):
    """Custom type brLdapTimeoutSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrLdapTimeoutSupported_Type.__name__ = "Integer32"
_BrLdapTimeoutSupported_Object = MibScalar
brLdapTimeoutSupported = _BrLdapTimeoutSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 19, 4),
    _BrLdapTimeoutSupported_Type()
)
brLdapTimeoutSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLdapTimeoutSupported.setStatus("mandatory")
_BrLdapServerCount_Type = Integer32
_BrLdapServerCount_Object = MibScalar
brLdapServerCount = _BrLdapServerCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 19, 11),
    _BrLdapServerCount_Type()
)
brLdapServerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLdapServerCount.setStatus("mandatory")
_BrLdapServerInfoTable_Object = MibTable
brLdapServerInfoTable = _BrLdapServerInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 19, 12)
)
if mibBuilder.loadTexts:
    brLdapServerInfoTable.setStatus("mandatory")
_BrLdapServerInfoEntry_Object = MibTableRow
brLdapServerInfoEntry = _BrLdapServerInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 19, 12, 1)
)
brLdapServerInfoEntry.setIndexNames(
    (0, "BROTHER-MIB", "brLdapServerInfoIndex"),
)
if mibBuilder.loadTexts:
    brLdapServerInfoEntry.setStatus("mandatory")


class _BrLdapServerInfoIndex_Type(Integer32):
    """Custom type brLdapServerInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrLdapServerInfoIndex_Type.__name__ = "Integer32"
_BrLdapServerInfoIndex_Object = MibTableColumn
brLdapServerInfoIndex = _BrLdapServerInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 19, 12, 1, 1),
    _BrLdapServerInfoIndex_Type()
)
brLdapServerInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLdapServerInfoIndex.setStatus("mandatory")


class _BrLdapServerName_Type(DisplayString):
    """Custom type brLdapServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BrLdapServerName_Type.__name__ = "DisplayString"
_BrLdapServerName_Object = MibTableColumn
brLdapServerName = _BrLdapServerName_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 19, 12, 1, 2),
    _BrLdapServerName_Type()
)
brLdapServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLdapServerName.setStatus("mandatory")


class _BrLdapServerPort_Type(Integer32):
    """Custom type brLdapServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrLdapServerPort_Type.__name__ = "Integer32"
_BrLdapServerPort_Object = MibTableColumn
brLdapServerPort = _BrLdapServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 19, 12, 1, 3),
    _BrLdapServerPort_Type()
)
brLdapServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLdapServerPort.setStatus("mandatory")


class _BrLdapServerAuth_Type(Integer32):
    """Custom type brLdapServerAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("anonymous", 1),
          ("kerberos", 3),
          ("simple", 2))
    )


_BrLdapServerAuth_Type.__name__ = "Integer32"
_BrLdapServerAuth_Object = MibTableColumn
brLdapServerAuth = _BrLdapServerAuth_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 19, 12, 1, 4),
    _BrLdapServerAuth_Type()
)
brLdapServerAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLdapServerAuth.setStatus("mandatory")


class _BrLdapServerUserDN_Type(OctetString):
    """Custom type brLdapServerUserDN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BrLdapServerUserDN_Type.__name__ = "OctetString"
_BrLdapServerUserDN_Object = MibTableColumn
brLdapServerUserDN = _BrLdapServerUserDN_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 19, 12, 1, 5),
    _BrLdapServerUserDN_Type()
)
brLdapServerUserDN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLdapServerUserDN.setStatus("mandatory")


class _BrLdapServerPassword_Type(OctetString):
    """Custom type brLdapServerPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrLdapServerPassword_Type.__name__ = "OctetString"
_BrLdapServerPassword_Object = MibTableColumn
brLdapServerPassword = _BrLdapServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 19, 12, 1, 6),
    _BrLdapServerPassword_Type()
)
brLdapServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLdapServerPassword.setStatus("mandatory")


class _BrLdapServerPasswordSet_Type(Integer32):
    """Custom type brLdapServerPasswordSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrLdapServerPasswordSet_Type.__name__ = "Integer32"
_BrLdapServerPasswordSet_Object = MibTableColumn
brLdapServerPasswordSet = _BrLdapServerPasswordSet_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 19, 12, 1, 7),
    _BrLdapServerPasswordSet_Type()
)
brLdapServerPasswordSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLdapServerPasswordSet.setStatus("mandatory")


class _BrLdapServerBaseDN_Type(OctetString):
    """Custom type brLdapServerBaseDN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BrLdapServerBaseDN_Type.__name__ = "OctetString"
_BrLdapServerBaseDN_Object = MibTableColumn
brLdapServerBaseDN = _BrLdapServerBaseDN_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 19, 12, 1, 8),
    _BrLdapServerBaseDN_Type()
)
brLdapServerBaseDN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLdapServerBaseDN.setStatus("mandatory")


class _BrLdapServerAttrEMail_Type(DisplayString):
    """Custom type brLdapServerAttrEMail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BrLdapServerAttrEMail_Type.__name__ = "DisplayString"
_BrLdapServerAttrEMail_Object = MibTableColumn
brLdapServerAttrEMail = _BrLdapServerAttrEMail_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 19, 12, 1, 10),
    _BrLdapServerAttrEMail_Type()
)
brLdapServerAttrEMail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLdapServerAttrEMail.setStatus("mandatory")


class _BrLdapServerAttrFAXNumber_Type(DisplayString):
    """Custom type brLdapServerAttrFAXNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BrLdapServerAttrFAXNumber_Type.__name__ = "DisplayString"
_BrLdapServerAttrFAXNumber_Object = MibTableColumn
brLdapServerAttrFAXNumber = _BrLdapServerAttrFAXNumber_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 19, 12, 1, 11),
    _BrLdapServerAttrFAXNumber_Type()
)
brLdapServerAttrFAXNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLdapServerAttrFAXNumber.setStatus("mandatory")


class _BrLdapServerAttrDetail1_Type(DisplayString):
    """Custom type brLdapServerAttrDetail1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BrLdapServerAttrDetail1_Type.__name__ = "DisplayString"
_BrLdapServerAttrDetail1_Object = MibTableColumn
brLdapServerAttrDetail1 = _BrLdapServerAttrDetail1_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 19, 12, 1, 12),
    _BrLdapServerAttrDetail1_Type()
)
brLdapServerAttrDetail1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLdapServerAttrDetail1.setStatus("mandatory")


class _BrLdapServerAttrDetail2_Type(DisplayString):
    """Custom type brLdapServerAttrDetail2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BrLdapServerAttrDetail2_Type.__name__ = "DisplayString"
_BrLdapServerAttrDetail2_Object = MibTableColumn
brLdapServerAttrDetail2 = _BrLdapServerAttrDetail2_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 19, 12, 1, 13),
    _BrLdapServerAttrDetail2_Type()
)
brLdapServerAttrDetail2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLdapServerAttrDetail2.setStatus("mandatory")


class _BrLdapServerAttrDetail3_Type(DisplayString):
    """Custom type brLdapServerAttrDetail3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BrLdapServerAttrDetail3_Type.__name__ = "DisplayString"
_BrLdapServerAttrDetail3_Object = MibTableColumn
brLdapServerAttrDetail3 = _BrLdapServerAttrDetail3_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 19, 12, 1, 14),
    _BrLdapServerAttrDetail3_Type()
)
brLdapServerAttrDetail3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLdapServerAttrDetail3.setStatus("mandatory")


class _BrLdapServerAttrDetail4_Type(DisplayString):
    """Custom type brLdapServerAttrDetail4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BrLdapServerAttrDetail4_Type.__name__ = "DisplayString"
_BrLdapServerAttrDetail4_Object = MibTableColumn
brLdapServerAttrDetail4 = _BrLdapServerAttrDetail4_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 19, 12, 1, 15),
    _BrLdapServerAttrDetail4_Type()
)
brLdapServerAttrDetail4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLdapServerAttrDetail4.setStatus("mandatory")


class _BrLdapServerAttrDetailEnable1_Type(Integer32):
    """Custom type brLdapServerAttrDetailEnable1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrLdapServerAttrDetailEnable1_Type.__name__ = "Integer32"
_BrLdapServerAttrDetailEnable1_Object = MibTableColumn
brLdapServerAttrDetailEnable1 = _BrLdapServerAttrDetailEnable1_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 19, 12, 1, 16),
    _BrLdapServerAttrDetailEnable1_Type()
)
brLdapServerAttrDetailEnable1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLdapServerAttrDetailEnable1.setStatus("mandatory")


class _BrLdapServerAttrDetailEnable2_Type(Integer32):
    """Custom type brLdapServerAttrDetailEnable2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrLdapServerAttrDetailEnable2_Type.__name__ = "Integer32"
_BrLdapServerAttrDetailEnable2_Object = MibTableColumn
brLdapServerAttrDetailEnable2 = _BrLdapServerAttrDetailEnable2_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 19, 12, 1, 17),
    _BrLdapServerAttrDetailEnable2_Type()
)
brLdapServerAttrDetailEnable2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLdapServerAttrDetailEnable2.setStatus("mandatory")


class _BrLdapServerAttrDetailEnable3_Type(Integer32):
    """Custom type brLdapServerAttrDetailEnable3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrLdapServerAttrDetailEnable3_Type.__name__ = "Integer32"
_BrLdapServerAttrDetailEnable3_Object = MibTableColumn
brLdapServerAttrDetailEnable3 = _BrLdapServerAttrDetailEnable3_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 19, 12, 1, 18),
    _BrLdapServerAttrDetailEnable3_Type()
)
brLdapServerAttrDetailEnable3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLdapServerAttrDetailEnable3.setStatus("mandatory")


class _BrLdapServerAttrDetailEnable4_Type(Integer32):
    """Custom type brLdapServerAttrDetailEnable4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrLdapServerAttrDetailEnable4_Type.__name__ = "Integer32"
_BrLdapServerAttrDetailEnable4_Object = MibTableColumn
brLdapServerAttrDetailEnable4 = _BrLdapServerAttrDetailEnable4_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 19, 12, 1, 19),
    _BrLdapServerAttrDetailEnable4_Type()
)
brLdapServerAttrDetailEnable4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLdapServerAttrDetailEnable4.setStatus("mandatory")


class _BrLdapKerberosServerName_Type(DisplayString):
    """Custom type brLdapKerberosServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BrLdapKerberosServerName_Type.__name__ = "DisplayString"
_BrLdapKerberosServerName_Object = MibTableColumn
brLdapKerberosServerName = _BrLdapKerberosServerName_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 19, 12, 1, 20),
    _BrLdapKerberosServerName_Type()
)
brLdapKerberosServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLdapKerberosServerName.setStatus("mandatory")


class _BrLdapKerberosServerPort_Type(Integer32):
    """Custom type brLdapKerberosServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrLdapKerberosServerPort_Type.__name__ = "Integer32"
_BrLdapKerberosServerPort_Object = MibTableColumn
brLdapKerberosServerPort = _BrLdapKerberosServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 19, 12, 1, 21),
    _BrLdapKerberosServerPort_Type()
)
brLdapKerberosServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLdapKerberosServerPort.setStatus("mandatory")
_BrLdapServerAttrNameCount_Type = Integer32
_BrLdapServerAttrNameCount_Object = MibScalar
brLdapServerAttrNameCount = _BrLdapServerAttrNameCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 19, 21),
    _BrLdapServerAttrNameCount_Type()
)
brLdapServerAttrNameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLdapServerAttrNameCount.setStatus("mandatory")
_BrLdapServerAttrNameTable_Object = MibTable
brLdapServerAttrNameTable = _BrLdapServerAttrNameTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 19, 22)
)
if mibBuilder.loadTexts:
    brLdapServerAttrNameTable.setStatus("mandatory")
_BrLdapServerAttrNameEntry_Object = MibTableRow
brLdapServerAttrNameEntry = _BrLdapServerAttrNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 19, 22, 1)
)
brLdapServerAttrNameEntry.setIndexNames(
    (0, "BROTHER-MIB", "brLdapServerInfoIndex"),
    (0, "BROTHER-MIB", "brLdapServerAttrNameIndex"),
)
if mibBuilder.loadTexts:
    brLdapServerAttrNameEntry.setStatus("mandatory")


class _BrLdapServerAttrNameIndex_Type(Integer32):
    """Custom type brLdapServerAttrNameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_BrLdapServerAttrNameIndex_Type.__name__ = "Integer32"
_BrLdapServerAttrNameIndex_Object = MibTableColumn
brLdapServerAttrNameIndex = _BrLdapServerAttrNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 19, 22, 1, 1),
    _BrLdapServerAttrNameIndex_Type()
)
brLdapServerAttrNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLdapServerAttrNameIndex.setStatus("mandatory")


class _BrLdapServerAttrName_Type(DisplayString):
    """Custom type brLdapServerAttrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BrLdapServerAttrName_Type.__name__ = "DisplayString"
_BrLdapServerAttrName_Object = MibTableColumn
brLdapServerAttrName = _BrLdapServerAttrName_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 19, 22, 1, 2),
    _BrLdapServerAttrName_Type()
)
brLdapServerAttrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLdapServerAttrName.setStatus("mandatory")


class _BrLdapSetDefault_Type(Integer32):
    """Custom type brLdapSetDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_BrLdapSetDefault_Type.__name__ = "Integer32"
_BrLdapSetDefault_Object = MibScalar
brLdapSetDefault = _BrLdapSetDefault_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 19, 99),
    _BrLdapSetDefault_Type()
)
brLdapSetDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLdapSetDefault.setStatus("mandatory")
_BroriginalTFTP_ObjectIdentity = ObjectIdentity
broriginalTFTP = _BroriginalTFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 20)
)


class _BrTFTPSupported_Type(Integer32):
    """Custom type brTFTPSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrTFTPSupported_Type.__name__ = "Integer32"
_BrTFTPSupported_Object = MibScalar
brTFTPSupported = _BrTFTPSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 20, 1),
    _BrTFTPSupported_Type()
)
brTFTPSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brTFTPSupported.setStatus("mandatory")


class _BrTFTPEnable_Type(Integer32):
    """Custom type brTFTPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrTFTPEnable_Type.__name__ = "Integer32"
_BrTFTPEnable_Object = MibScalar
brTFTPEnable = _BrTFTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 20, 2),
    _BrTFTPEnable_Type()
)
brTFTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brTFTPEnable.setStatus("mandatory")
_BroriginalHTTPS_ObjectIdentity = ObjectIdentity
broriginalHTTPS = _BroriginalHTTPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 21)
)


class _BrHTTPSSupported_Type(Integer32):
    """Custom type brHTTPSSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrHTTPSSupported_Type.__name__ = "Integer32"
_BrHTTPSSupported_Object = MibScalar
brHTTPSSupported = _BrHTTPSSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 21, 1),
    _BrHTTPSSupported_Type()
)
brHTTPSSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brHTTPSSupported.setStatus("mandatory")


class _BrHTTPSEnable_Type(Integer32):
    """Custom type brHTTPSEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrHTTPSEnable_Type.__name__ = "Integer32"
_BrHTTPSEnable_Object = MibScalar
brHTTPSEnable = _BrHTTPSEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 21, 2),
    _BrHTTPSEnable_Type()
)
brHTTPSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brHTTPSEnable.setStatus("mandatory")
_BroriginalLPD_ObjectIdentity = ObjectIdentity
broriginalLPD = _BroriginalLPD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 22)
)


class _BrLPDSupported_Type(Integer32):
    """Custom type brLPDSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrLPDSupported_Type.__name__ = "Integer32"
_BrLPDSupported_Object = MibScalar
brLPDSupported = _BrLPDSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 22, 1),
    _BrLPDSupported_Type()
)
brLPDSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLPDSupported.setStatus("mandatory")


class _BrLPDEnable_Type(Integer32):
    """Custom type brLPDEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrLPDEnable_Type.__name__ = "Integer32"
_BrLPDEnable_Object = MibScalar
brLPDEnable = _BrLPDEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 22, 2),
    _BrLPDEnable_Type()
)
brLPDEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLPDEnable.setStatus("mandatory")
_BroriginalRawPort_ObjectIdentity = ObjectIdentity
broriginalRawPort = _BroriginalRawPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 23)
)


class _BrRawPortSupported_Type(Integer32):
    """Custom type brRawPortSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrRawPortSupported_Type.__name__ = "Integer32"
_BrRawPortSupported_Object = MibScalar
brRawPortSupported = _BrRawPortSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 23, 1),
    _BrRawPortSupported_Type()
)
brRawPortSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brRawPortSupported.setStatus("mandatory")


class _BrRawPortEnable_Type(Integer32):
    """Custom type brRawPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrRawPortEnable_Type.__name__ = "Integer32"
_BrRawPortEnable_Object = MibScalar
brRawPortEnable = _BrRawPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 23, 2),
    _BrRawPortEnable_Type()
)
brRawPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brRawPortEnable.setStatus("mandatory")
_BroriginalLLTD_ObjectIdentity = ObjectIdentity
broriginalLLTD = _BroriginalLLTD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 24)
)


class _BrLLTDSupported_Type(Integer32):
    """Custom type brLLTDSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrLLTDSupported_Type.__name__ = "Integer32"
_BrLLTDSupported_Object = MibScalar
brLLTDSupported = _BrLLTDSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 24, 1),
    _BrLLTDSupported_Type()
)
brLLTDSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brLLTDSupported.setStatus("mandatory")


class _BrLLTDEnable_Type(Integer32):
    """Custom type brLLTDEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrLLTDEnable_Type.__name__ = "Integer32"
_BrLLTDEnable_Object = MibScalar
brLLTDEnable = _BrLLTDEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 24, 2),
    _BrLLTDEnable_Type()
)
brLLTDEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLLTDEnable.setStatus("mandatory")
_BroriginalWebServices_ObjectIdentity = ObjectIdentity
broriginalWebServices = _BroriginalWebServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 25)
)


class _BrWebServicesSupported_Type(Integer32):
    """Custom type brWebServicesSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrWebServicesSupported_Type.__name__ = "Integer32"
_BrWebServicesSupported_Object = MibScalar
brWebServicesSupported = _BrWebServicesSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 25, 1),
    _BrWebServicesSupported_Type()
)
brWebServicesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brWebServicesSupported.setStatus("mandatory")


class _BrWebServicesEnable_Type(Integer32):
    """Custom type brWebServicesEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrWebServicesEnable_Type.__name__ = "Integer32"
_BrWebServicesEnable_Object = MibScalar
brWebServicesEnable = _BrWebServicesEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 25, 2),
    _BrWebServicesEnable_Type()
)
brWebServicesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brWebServicesEnable.setStatus("mandatory")


class _BrWebServicesRegularPortEnable_Type(Integer32):
    """Custom type brWebServicesRegularPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrWebServicesRegularPortEnable_Type.__name__ = "Integer32"
_BrWebServicesRegularPortEnable_Object = MibScalar
brWebServicesRegularPortEnable = _BrWebServicesRegularPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 25, 3),
    _BrWebServicesRegularPortEnable_Type()
)
brWebServicesRegularPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brWebServicesRegularPortEnable.setStatus("mandatory")


class _BrWebServicesSSLPortEnable_Type(Integer32):
    """Custom type brWebServicesSSLPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrWebServicesSSLPortEnable_Type.__name__ = "Integer32"
_BrWebServicesSSLPortEnable_Object = MibScalar
brWebServicesSSLPortEnable = _BrWebServicesSSLPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 25, 4),
    _BrWebServicesSSLPortEnable_Type()
)
brWebServicesSSLPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brWebServicesSSLPortEnable.setStatus("mandatory")
_BroriginalLLMNR_ObjectIdentity = ObjectIdentity
broriginalLLMNR = _BroriginalLLMNR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 26)
)


class _BrLLMNREnable_Type(Integer32):
    """Custom type brLLMNREnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrLLMNREnable_Type.__name__ = "Integer32"
_BrLLMNREnable_Object = MibScalar
brLLMNREnable = _BrLLMNREnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 26, 1),
    _BrLLMNREnable_Type()
)
brLLMNREnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLLMNREnable.setStatus("mandatory")
_BroriginalKerberos_ObjectIdentity = ObjectIdentity
broriginalKerberos = _BroriginalKerberos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 27)
)


class _BrKerberosSupported_Type(Integer32):
    """Custom type brKerberosSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrKerberosSupported_Type.__name__ = "Integer32"
_BrKerberosSupported_Object = MibScalar
brKerberosSupported = _BrKerberosSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 27, 1),
    _BrKerberosSupported_Type()
)
brKerberosSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brKerberosSupported.setStatus("mandatory")
_BroriginalCIFS_ObjectIdentity = ObjectIdentity
broriginalCIFS = _BroriginalCIFS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 28)
)


class _BrCIFSSupported_Type(Integer32):
    """Custom type brCIFSSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrCIFSSupported_Type.__name__ = "Integer32"
_BrCIFSSupported_Object = MibScalar
brCIFSSupported = _BrCIFSSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 28, 1),
    _BrCIFSSupported_Type()
)
brCIFSSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brCIFSSupported.setStatus("mandatory")


class _BrCIFSEnable_Type(Integer32):
    """Custom type brCIFSEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrCIFSEnable_Type.__name__ = "Integer32"
_BrCIFSEnable_Object = MibScalar
brCIFSEnable = _BrCIFSEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 28, 2),
    _BrCIFSEnable_Type()
)
brCIFSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brCIFSEnable.setStatus("mandatory")
_BroriginalSNTP_ObjectIdentity = ObjectIdentity
broriginalSNTP = _BroriginalSNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 29)
)


class _BrSNTPCSupported_Type(Integer32):
    """Custom type brSNTPCSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrSNTPCSupported_Type.__name__ = "Integer32"
_BrSNTPCSupported_Object = MibScalar
brSNTPCSupported = _BrSNTPCSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 29, 1),
    _BrSNTPCSupported_Type()
)
brSNTPCSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brSNTPCSupported.setStatus("mandatory")


class _BrSNTPCEnable_Type(Integer32):
    """Custom type brSNTPCEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrSNTPCEnable_Type.__name__ = "Integer32"
_BrSNTPCEnable_Object = MibScalar
brSNTPCEnable = _BrSNTPCEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 29, 2),
    _BrSNTPCEnable_Type()
)
brSNTPCEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brSNTPCEnable.setStatus("mandatory")


class _BrSNTPCServerMethod_Type(Integer32):
    """Custom type brSNTPCServerMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_BrSNTPCServerMethod_Type.__name__ = "Integer32"
_BrSNTPCServerMethod_Object = MibScalar
brSNTPCServerMethod = _BrSNTPCServerMethod_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 29, 3),
    _BrSNTPCServerMethod_Type()
)
brSNTPCServerMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brSNTPCServerMethod.setStatus("mandatory")


class _BrSNTPCSyncMethod_Type(Integer32):
    """Custom type brSNTPCSyncMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_BrSNTPCSyncMethod_Type.__name__ = "Integer32"
_BrSNTPCSyncMethod_Object = MibScalar
brSNTPCSyncMethod = _BrSNTPCSyncMethod_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 29, 4),
    _BrSNTPCSyncMethod_Type()
)
brSNTPCSyncMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brSNTPCSyncMethod.setStatus("mandatory")


class _BrSNTPCIntervalMin_Type(Integer32):
    """Custom type brSNTPCIntervalMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 168),
    )


_BrSNTPCIntervalMin_Type.__name__ = "Integer32"
_BrSNTPCIntervalMin_Object = MibScalar
brSNTPCIntervalMin = _BrSNTPCIntervalMin_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 29, 5),
    _BrSNTPCIntervalMin_Type()
)
brSNTPCIntervalMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brSNTPCIntervalMin.setStatus("mandatory")


class _BrSNTPCInterval_Type(Integer32):
    """Custom type brSNTPCInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 168),
    )


_BrSNTPCInterval_Type.__name__ = "Integer32"
_BrSNTPCInterval_Object = MibScalar
brSNTPCInterval = _BrSNTPCInterval_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 29, 6),
    _BrSNTPCInterval_Type()
)
brSNTPCInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brSNTPCInterval.setStatus("mandatory")


class _BrSNTPCSyncResult_Type(Integer32):
    """Custom type brSNTPCSyncResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BrSNTPCSyncResult_Type.__name__ = "Integer32"
_BrSNTPCSyncResult_Object = MibScalar
brSNTPCSyncResult = _BrSNTPCSyncResult_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 29, 7),
    _BrSNTPCSyncResult_Type()
)
brSNTPCSyncResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brSNTPCSyncResult.setStatus("mandatory")


class _BrSNTPCPrimaryServerName_Type(DisplayString):
    """Custom type brSNTPCPrimaryServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BrSNTPCPrimaryServerName_Type.__name__ = "DisplayString"
_BrSNTPCPrimaryServerName_Object = MibScalar
brSNTPCPrimaryServerName = _BrSNTPCPrimaryServerName_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 29, 8),
    _BrSNTPCPrimaryServerName_Type()
)
brSNTPCPrimaryServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brSNTPCPrimaryServerName.setStatus("mandatory")


class _BrSNTPCPrimaryServerPort_Type(Integer32):
    """Custom type brSNTPCPrimaryServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BrSNTPCPrimaryServerPort_Type.__name__ = "Integer32"
_BrSNTPCPrimaryServerPort_Object = MibScalar
brSNTPCPrimaryServerPort = _BrSNTPCPrimaryServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 29, 9),
    _BrSNTPCPrimaryServerPort_Type()
)
brSNTPCPrimaryServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brSNTPCPrimaryServerPort.setStatus("mandatory")


class _BrSNTPCSecondaryServerName_Type(DisplayString):
    """Custom type brSNTPCSecondaryServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BrSNTPCSecondaryServerName_Type.__name__ = "DisplayString"
_BrSNTPCSecondaryServerName_Object = MibScalar
brSNTPCSecondaryServerName = _BrSNTPCSecondaryServerName_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 29, 10),
    _BrSNTPCSecondaryServerName_Type()
)
brSNTPCSecondaryServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brSNTPCSecondaryServerName.setStatus("mandatory")


class _BrSNTPCSecondaryServerPort_Type(Integer32):
    """Custom type brSNTPCSecondaryServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BrSNTPCSecondaryServerPort_Type.__name__ = "Integer32"
_BrSNTPCSecondaryServerPort_Object = MibScalar
brSNTPCSecondaryServerPort = _BrSNTPCSecondaryServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 29, 11),
    _BrSNTPCSecondaryServerPort_Type()
)
brSNTPCSecondaryServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brSNTPCSecondaryServerPort.setStatus("mandatory")
_BroriginalSecurity_ObjectIdentity = ObjectIdentity
broriginalSecurity = _BroriginalSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 100)
)
_BrSecurityGeneralStatus_ObjectIdentity = ObjectIdentity
brSecurityGeneralStatus = _BrSecurityGeneralStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 100, 1)
)


class _BrDeviceNegotiationEncryptVer_Type(Integer32):
    """Custom type brDeviceNegotiationEncryptVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrDeviceNegotiationEncryptVer_Type.__name__ = "Integer32"
_BrDeviceNegotiationEncryptVer_Object = MibScalar
brDeviceNegotiationEncryptVer = _BrDeviceNegotiationEncryptVer_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 100, 1, 1),
    _BrDeviceNegotiationEncryptVer_Type()
)
brDeviceNegotiationEncryptVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brDeviceNegotiationEncryptVer.setStatus("mandatory")
_BrpsServerCertificateNum_Type = Integer32
_BrpsServerCertificateNum_Object = MibScalar
brpsServerCertificateNum = _BrpsServerCertificateNum_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 100, 1, 2),
    _BrpsServerCertificateNum_Type()
)
brpsServerCertificateNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brpsServerCertificateNum.setStatus("mandatory")
_BrSecurityGeneralSetup_ObjectIdentity = ObjectIdentity
brSecurityGeneralSetup = _BrSecurityGeneralSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 100, 2)
)
_BrSecurityDeviceNegotiation_ObjectIdentity = ObjectIdentity
brSecurityDeviceNegotiation = _BrSecurityDeviceNegotiation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 100, 10)
)


class _BrDeviceNegotiationGetChallenge_Type(OctetString):
    """Custom type brDeviceNegotiationGetChallenge based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_BrDeviceNegotiationGetChallenge_Type.__name__ = "OctetString"
_BrDeviceNegotiationGetChallenge_Object = MibScalar
brDeviceNegotiationGetChallenge = _BrDeviceNegotiationGetChallenge_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 100, 10, 1),
    _BrDeviceNegotiationGetChallenge_Type()
)
brDeviceNegotiationGetChallenge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brDeviceNegotiationGetChallenge.setStatus("mandatory")


class _BrDeviceNegotiationConfirmPassword_Type(OctetString):
    """Custom type brDeviceNegotiationConfirmPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(60, 60),
    )


_BrDeviceNegotiationConfirmPassword_Type.__name__ = "OctetString"
_BrDeviceNegotiationConfirmPassword_Object = MibScalar
brDeviceNegotiationConfirmPassword = _BrDeviceNegotiationConfirmPassword_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 100, 10, 2),
    _BrDeviceNegotiationConfirmPassword_Type()
)
brDeviceNegotiationConfirmPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brDeviceNegotiationConfirmPassword.setStatus("mandatory")


class _BrDeviceNegotiationChangePassword_Type(OctetString):
    """Custom type brDeviceNegotiationChangePassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(48, 48),
    )


_BrDeviceNegotiationChangePassword_Type.__name__ = "OctetString"
_BrDeviceNegotiationChangePassword_Object = MibScalar
brDeviceNegotiationChangePassword = _BrDeviceNegotiationChangePassword_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 5, 100, 10, 3),
    _BrDeviceNegotiationChangePassword_Type()
)
brDeviceNegotiationChangePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brDeviceNegotiationChangePassword.setStatus("mandatory")
_Broriginalinternetsetting_ObjectIdentity = ObjectIdentity
broriginalinternetsetting = _Broriginalinternetsetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 10)
)
_Broriginalproxy_ObjectIdentity = ObjectIdentity
broriginalproxy = _Broriginalproxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 10, 1)
)


class _BrProxySupported_Type(Integer32):
    """Custom type brProxySupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrProxySupported_Type.__name__ = "Integer32"
_BrProxySupported_Object = MibScalar
brProxySupported = _BrProxySupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 10, 1, 1),
    _BrProxySupported_Type()
)
brProxySupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brProxySupported.setStatus("mandatory")


class _BrProxyEnable_Type(Integer32):
    """Custom type brProxyEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrProxyEnable_Type.__name__ = "Integer32"
_BrProxyEnable_Object = MibScalar
brProxyEnable = _BrProxyEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 10, 1, 2),
    _BrProxyEnable_Type()
)
brProxyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brProxyEnable.setStatus("mandatory")


class _BrProxyBypassServer_Type(Integer32):
    """Custom type brProxyBypassServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_BrProxyBypassServer_Type.__name__ = "Integer32"
_BrProxyBypassServer_Object = MibScalar
brProxyBypassServer = _BrProxyBypassServer_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 10, 1, 3),
    _BrProxyBypassServer_Type()
)
brProxyBypassServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brProxyBypassServer.setStatus("mandatory")
_BrProxyServerCount_Type = Integer32
_BrProxyServerCount_Object = MibScalar
brProxyServerCount = _BrProxyServerCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 10, 1, 11),
    _BrProxyServerCount_Type()
)
brProxyServerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brProxyServerCount.setStatus("mandatory")
_BrProxyServerInfoTable_Object = MibTable
brProxyServerInfoTable = _BrProxyServerInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 10, 1, 12)
)
if mibBuilder.loadTexts:
    brProxyServerInfoTable.setStatus("mandatory")
_BrProxyServerInfoEntry_Object = MibTableRow
brProxyServerInfoEntry = _BrProxyServerInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 10, 1, 12, 1)
)
brProxyServerInfoEntry.setIndexNames(
    (0, "BROTHER-MIB", "brProxyServerInfoIndex"),
)
if mibBuilder.loadTexts:
    brProxyServerInfoEntry.setStatus("mandatory")


class _BrProxyServerInfoIndex_Type(Integer32):
    """Custom type brProxyServerInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BrProxyServerInfoIndex_Type.__name__ = "Integer32"
_BrProxyServerInfoIndex_Object = MibTableColumn
brProxyServerInfoIndex = _BrProxyServerInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 10, 1, 12, 1, 1),
    _BrProxyServerInfoIndex_Type()
)
brProxyServerInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brProxyServerInfoIndex.setStatus("mandatory")


class _BrProxyServerType_Type(Integer32):
    """Custom type brProxyServerType based on Integer32"""
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
        *(("ftp", 3),
          ("gopher", 4),
          ("http", 1),
          ("secure", 2),
          ("socks", 5))
    )


_BrProxyServerType_Type.__name__ = "Integer32"
_BrProxyServerType_Object = MibTableColumn
brProxyServerType = _BrProxyServerType_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 10, 1, 12, 1, 2),
    _BrProxyServerType_Type()
)
brProxyServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brProxyServerType.setStatus("mandatory")


class _BrProxyServerName_Type(OctetString):
    """Custom type brProxyServerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_BrProxyServerName_Type.__name__ = "OctetString"
_BrProxyServerName_Object = MibTableColumn
brProxyServerName = _BrProxyServerName_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 10, 1, 12, 1, 3),
    _BrProxyServerName_Type()
)
brProxyServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brProxyServerName.setStatus("mandatory")


class _BrProxyServerPort_Type(Integer32):
    """Custom type brProxyServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrProxyServerPort_Type.__name__ = "Integer32"
_BrProxyServerPort_Object = MibTableColumn
brProxyServerPort = _BrProxyServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 10, 1, 12, 1, 4),
    _BrProxyServerPort_Type()
)
brProxyServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brProxyServerPort.setStatus("mandatory")
_BroriginalOtherSetting_ObjectIdentity = ObjectIdentity
broriginalOtherSetting = _BroriginalOtherSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 20)
)
_BroriginalJobTermination_ObjectIdentity = ObjectIdentity
broriginalJobTermination = _BroriginalJobTermination_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 20, 1)
)


class _BrJobTerminationSupported_Type(Integer32):
    """Custom type brJobTerminationSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrJobTerminationSupported_Type.__name__ = "Integer32"
_BrJobTerminationSupported_Object = MibScalar
brJobTerminationSupported = _BrJobTerminationSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 20, 1, 1),
    _BrJobTerminationSupported_Type()
)
brJobTerminationSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brJobTerminationSupported.setStatus("mandatory")


class _BrJobTerminationEnable_Type(Integer32):
    """Custom type brJobTerminationEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrJobTerminationEnable_Type.__name__ = "Integer32"
_BrJobTerminationEnable_Object = MibScalar
brJobTerminationEnable = _BrJobTerminationEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 20, 1, 2),
    _BrJobTerminationEnable_Type()
)
brJobTerminationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brJobTerminationEnable.setStatus("mandatory")
_BroriginalSNMPTrap_ObjectIdentity = ObjectIdentity
broriginalSNMPTrap = _BroriginalSNMPTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 20, 2)
)
_BrSNMPTrapTable_Object = MibTable
brSNMPTrapTable = _BrSNMPTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 20, 2, 1)
)
if mibBuilder.loadTexts:
    brSNMPTrapTable.setStatus("mandatory")
_BrSNMPTrapEntry_Object = MibTableRow
brSNMPTrapEntry = _BrSNMPTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 20, 2, 1, 1)
)
brSNMPTrapEntry.setIndexNames(
    (0, "BROTHER-MIB", "brSNMPTrapIndex"),
)
if mibBuilder.loadTexts:
    brSNMPTrapEntry.setStatus("mandatory")


class _BrSNMPTrapIndex_Type(Integer32):
    """Custom type brSNMPTrapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BrSNMPTrapIndex_Type.__name__ = "Integer32"
_BrSNMPTrapIndex_Object = MibTableColumn
brSNMPTrapIndex = _BrSNMPTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 20, 2, 1, 1, 1),
    _BrSNMPTrapIndex_Type()
)
brSNMPTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brSNMPTrapIndex.setStatus("mandatory")
_BrTCPIPServerAddress_Type = IpAddress
_BrTCPIPServerAddress_Object = MibTableColumn
brTCPIPServerAddress = _BrTCPIPServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 20, 2, 1, 1, 2),
    _BrTCPIPServerAddress_Type()
)
brTCPIPServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brTCPIPServerAddress.setStatus("mandatory")
_BroriginalLegacy_ObjectIdentity = ObjectIdentity
broriginalLegacy = _BroriginalLegacy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 20, 3)
)
_BrLegacyCompatible_Type = Integer32
_BrLegacyCompatible_Object = MibScalar
brLegacyCompatible = _BrLegacyCompatible_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 3, 2435, 20, 3, 1),
    _BrLegacyCompatible_Type()
)
brLegacyCompatible.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLegacyCompatible.setStatus("mandatory")
_NpMultiCards_ObjectIdentity = ObjectIdentity
npMultiCards = _NpMultiCards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4)
)
_NpMultiIFSet_ObjectIdentity = ObjectIdentity
npMultiIFSet = _NpMultiIFSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 99)
)
_BrMultiIFdns_ObjectIdentity = ObjectIdentity
brMultiIFdns = _BrMultiIFdns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 99, 1)
)
_BrMultiIFDNSTable_Object = MibTable
brMultiIFDNSTable = _BrMultiIFDNSTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 99, 1, 1)
)
if mibBuilder.loadTexts:
    brMultiIFDNSTable.setStatus("mandatory")
_BrMultiIFDNSEntry_Object = MibTableRow
brMultiIFDNSEntry = _BrMultiIFDNSEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 99, 1, 1, 1)
)
brMultiIFDNSEntry.setIndexNames(
    (0, "BROTHER-MIB", "brMultiIFConfigureIndex"),
)
if mibBuilder.loadTexts:
    brMultiIFDNSEntry.setStatus("mandatory")


class _BrMultiIFTCPIPDNSIPSetup_Type(Integer32):
    """Custom type brMultiIFTCPIPDNSIPSetup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("static", 1))
    )


_BrMultiIFTCPIPDNSIPSetup_Type.__name__ = "Integer32"
_BrMultiIFTCPIPDNSIPSetup_Object = MibTableColumn
brMultiIFTCPIPDNSIPSetup = _BrMultiIFTCPIPDNSIPSetup_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 99, 1, 1, 1, 1),
    _BrMultiIFTCPIPDNSIPSetup_Type()
)
brMultiIFTCPIPDNSIPSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFTCPIPDNSIPSetup.setStatus("mandatory")
_BrMultiIFPrimaryDNSIPAddress_Type = IpAddress
_BrMultiIFPrimaryDNSIPAddress_Object = MibTableColumn
brMultiIFPrimaryDNSIPAddress = _BrMultiIFPrimaryDNSIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 99, 1, 1, 1, 2),
    _BrMultiIFPrimaryDNSIPAddress_Type()
)
brMultiIFPrimaryDNSIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFPrimaryDNSIPAddress.setStatus("mandatory")
_BrMultiIFSecondaryDNSIPAddress_Type = IpAddress
_BrMultiIFSecondaryDNSIPAddress_Object = MibTableColumn
brMultiIFSecondaryDNSIPAddress = _BrMultiIFSecondaryDNSIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 99, 1, 1, 1, 3),
    _BrMultiIFSecondaryDNSIPAddress_Type()
)
brMultiIFSecondaryDNSIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFSecondaryDNSIPAddress.setStatus("mandatory")
_BrMultiIFTCPIPConnectTime_Type = Integer32
_BrMultiIFTCPIPConnectTime_Object = MibTableColumn
brMultiIFTCPIPConnectTime = _BrMultiIFTCPIPConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 99, 1, 1, 1, 4),
    _BrMultiIFTCPIPConnectTime_Type()
)
brMultiIFTCPIPConnectTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFTCPIPConnectTime.setStatus("mandatory")
_BrnetMultiIFConfig_ObjectIdentity = ObjectIdentity
brnetMultiIFConfig = _BrnetMultiIFConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240)
)
_BrMultiIFconfig_ObjectIdentity = ObjectIdentity
brMultiIFconfig = _BrMultiIFconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 1)
)


class _BrMultiIFSupported_Type(Integer32):
    """Custom type brMultiIFSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrMultiIFSupported_Type.__name__ = "Integer32"
_BrMultiIFSupported_Object = MibScalar
brMultiIFSupported = _BrMultiIFSupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 1, 1),
    _BrMultiIFSupported_Type()
)
brMultiIFSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMultiIFSupported.setStatus("mandatory")


class _BrMultiIFActiveIF_Type(Integer32):
    """Custom type brMultiIFActiveIF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("lan", 1),
          ("wirelesslan", 2))
    )


_BrMultiIFActiveIF_Type.__name__ = "Integer32"
_BrMultiIFActiveIF_Object = MibScalar
brMultiIFActiveIF = _BrMultiIFActiveIF_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 1, 2),
    _BrMultiIFActiveIF_Type()
)
brMultiIFActiveIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMultiIFActiveIF.setStatus("mandatory")


class _BrMultiIFAllSetDefault_Type(Integer32):
    """Custom type brMultiIFAllSetDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_BrMultiIFAllSetDefault_Type.__name__ = "Integer32"
_BrMultiIFAllSetDefault_Object = MibScalar
brMultiIFAllSetDefault = _BrMultiIFAllSetDefault_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 1, 3),
    _BrMultiIFAllSetDefault_Type()
)
brMultiIFAllSetDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFAllSetDefault.setStatus("mandatory")
_BrMultiIFCount_Type = Integer32
_BrMultiIFCount_Object = MibScalar
brMultiIFCount = _BrMultiIFCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 1, 4),
    _BrMultiIFCount_Type()
)
brMultiIFCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMultiIFCount.setStatus("mandatory")
_BrMultiIFConfigureTable_Object = MibTable
brMultiIFConfigureTable = _BrMultiIFConfigureTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 1, 5)
)
if mibBuilder.loadTexts:
    brMultiIFConfigureTable.setStatus("mandatory")
_BrMultiIFConfigureEntry_Object = MibTableRow
brMultiIFConfigureEntry = _BrMultiIFConfigureEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 1, 5, 1)
)
brMultiIFConfigureEntry.setIndexNames(
    (0, "BROTHER-MIB", "brMultiIFConfigureIndex"),
)
if mibBuilder.loadTexts:
    brMultiIFConfigureEntry.setStatus("mandatory")


class _BrMultiIFConfigureIndex_Type(Integer32):
    """Custom type brMultiIFConfigureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BrMultiIFConfigureIndex_Type.__name__ = "Integer32"
_BrMultiIFConfigureIndex_Object = MibTableColumn
brMultiIFConfigureIndex = _BrMultiIFConfigureIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 1, 5, 1, 1),
    _BrMultiIFConfigureIndex_Type()
)
brMultiIFConfigureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMultiIFConfigureIndex.setStatus("mandatory")


class _BrMultiIFType_Type(Integer32):
    """Custom type brMultiIFType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lan", 1),
          ("wirelesslan", 2))
    )


_BrMultiIFType_Type.__name__ = "Integer32"
_BrMultiIFType_Object = MibTableColumn
brMultiIFType = _BrMultiIFType_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 1, 5, 1, 2),
    _BrMultiIFType_Type()
)
brMultiIFType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMultiIFType.setStatus("mandatory")


class _BrMultiIFDescription_Type(DisplayString):
    """Custom type brMultiIFDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BrMultiIFDescription_Type.__name__ = "DisplayString"
_BrMultiIFDescription_Object = MibTableColumn
brMultiIFDescription = _BrMultiIFDescription_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 1, 5, 1, 3),
    _BrMultiIFDescription_Type()
)
brMultiIFDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMultiIFDescription.setStatus("mandatory")
_BrMultiIFNodeName_Type = OctetString
_BrMultiIFNodeName_Object = MibTableColumn
brMultiIFNodeName = _BrMultiIFNodeName_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 1, 5, 1, 4),
    _BrMultiIFNodeName_Type()
)
brMultiIFNodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFNodeName.setStatus("mandatory")


class _BrMultiIFInterfaceEnable_Type(Integer32):
    """Custom type brMultiIFInterfaceEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrMultiIFInterfaceEnable_Type.__name__ = "Integer32"
_BrMultiIFInterfaceEnable_Object = MibTableColumn
brMultiIFInterfaceEnable = _BrMultiIFInterfaceEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 1, 5, 1, 5),
    _BrMultiIFInterfaceEnable_Type()
)
brMultiIFInterfaceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFInterfaceEnable.setStatus("mandatory")


class _BrMultiIFEnetMode_Type(Integer32):
    """Custom type brMultiIFEnetMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_BrMultiIFEnetMode_Type.__name__ = "Integer32"
_BrMultiIFEnetMode_Object = MibTableColumn
brMultiIFEnetMode = _BrMultiIFEnetMode_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 1, 5, 1, 6),
    _BrMultiIFEnetMode_Type()
)
brMultiIFEnetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFEnetMode.setStatus("mandatory")


class _BrMultiIFHardwareType_Type(Integer32):
    """Custom type brMultiIFHardwareType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_BrMultiIFHardwareType_Type.__name__ = "Integer32"
_BrMultiIFHardwareType_Object = MibTableColumn
brMultiIFHardwareType = _BrMultiIFHardwareType_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 1, 5, 1, 7),
    _BrMultiIFHardwareType_Type()
)
brMultiIFHardwareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMultiIFHardwareType.setStatus("mandatory")
_BrMultiIFNodeType_Type = OctetString
_BrMultiIFNodeType_Object = MibTableColumn
brMultiIFNodeType = _BrMultiIFNodeType_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 1, 5, 1, 8),
    _BrMultiIFNodeType_Type()
)
brMultiIFNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMultiIFNodeType.setStatus("mandatory")


class _BrMultiIFInterfaceEnableImmediate_Type(Integer32):
    """Custom type brMultiIFInterfaceEnableImmediate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrMultiIFInterfaceEnableImmediate_Type.__name__ = "Integer32"
_BrMultiIFInterfaceEnableImmediate_Object = MibTableColumn
brMultiIFInterfaceEnableImmediate = _BrMultiIFInterfaceEnableImmediate_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 1, 5, 1, 9),
    _BrMultiIFInterfaceEnableImmediate_Type()
)
brMultiIFInterfaceEnableImmediate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFInterfaceEnableImmediate.setStatus("mandatory")
_BrMultiIFPrimaryInterface_Type = Integer32
_BrMultiIFPrimaryInterface_Object = MibScalar
brMultiIFPrimaryInterface = _BrMultiIFPrimaryInterface_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 1, 6),
    _BrMultiIFPrimaryInterface_Type()
)
brMultiIFPrimaryInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFPrimaryInterface.setStatus("mandatory")
_BrMultiIFInterfaceInformation_Type = Integer32
_BrMultiIFInterfaceInformation_Object = MibScalar
brMultiIFInterfaceInformation = _BrMultiIFInterfaceInformation_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 1, 7),
    _BrMultiIFInterfaceInformation_Type()
)
brMultiIFInterfaceInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMultiIFInterfaceInformation.setStatus("mandatory")
_BrMultiIFcontrol_ObjectIdentity = ObjectIdentity
brMultiIFcontrol = _BrMultiIFcontrol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 2)
)
_BrMultiIFControlTable_Object = MibTable
brMultiIFControlTable = _BrMultiIFControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 2, 1)
)
if mibBuilder.loadTexts:
    brMultiIFControlTable.setStatus("mandatory")
_BrMultiIFControlEntry_Object = MibTableRow
brMultiIFControlEntry = _BrMultiIFControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 2, 1, 1)
)
brMultiIFControlEntry.setIndexNames(
    (0, "BROTHER-MIB", "brMultiIFConfigureIndex"),
)
if mibBuilder.loadTexts:
    brMultiIFControlEntry.setStatus("mandatory")


class _BrMultiIFSetDefault_Type(Integer32):
    """Custom type brMultiIFSetDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_BrMultiIFSetDefault_Type.__name__ = "Integer32"
_BrMultiIFSetDefault_Object = MibTableColumn
brMultiIFSetDefault = _BrMultiIFSetDefault_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 2, 1, 1, 1),
    _BrMultiIFSetDefault_Type()
)
brMultiIFSetDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFSetDefault.setStatus("mandatory")
_BrMultiIFservice_ObjectIdentity = ObjectIdentity
brMultiIFservice = _BrMultiIFservice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4)
)
_BrMultiIFServiceTable_Object = MibTable
brMultiIFServiceTable = _BrMultiIFServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 1)
)
if mibBuilder.loadTexts:
    brMultiIFServiceTable.setStatus("mandatory")
_BrMultiIFServiceEntry_Object = MibTableRow
brMultiIFServiceEntry = _BrMultiIFServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 1, 1)
)
brMultiIFServiceEntry.setIndexNames(
    (0, "BROTHER-MIB", "brMultiIFConfigureIndex"),
)
if mibBuilder.loadTexts:
    brMultiIFServiceEntry.setStatus("mandatory")


class _BrMultiIFServiceCount_Type(Integer32):
    """Custom type brMultiIFServiceCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_BrMultiIFServiceCount_Type.__name__ = "Integer32"
_BrMultiIFServiceCount_Object = MibTableColumn
brMultiIFServiceCount = _BrMultiIFServiceCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 1, 1, 1),
    _BrMultiIFServiceCount_Type()
)
brMultiIFServiceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMultiIFServiceCount.setStatus("mandatory")


class _BrMultiIFServiceStringLimit_Type(Integer32):
    """Custom type brMultiIFServiceStringLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_BrMultiIFServiceStringLimit_Type.__name__ = "Integer32"
_BrMultiIFServiceStringLimit_Object = MibTableColumn
brMultiIFServiceStringLimit = _BrMultiIFServiceStringLimit_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 1, 1, 2),
    _BrMultiIFServiceStringLimit_Type()
)
brMultiIFServiceStringLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMultiIFServiceStringLimit.setStatus("mandatory")
_BrMultiIFServiceStringCount_Type = Integer32
_BrMultiIFServiceStringCount_Object = MibTableColumn
brMultiIFServiceStringCount = _BrMultiIFServiceStringCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 1, 1, 3),
    _BrMultiIFServiceStringCount_Type()
)
brMultiIFServiceStringCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMultiIFServiceStringCount.setStatus("mandatory")
_BrMultiIFServiceFilterCount_Type = Integer32
_BrMultiIFServiceFilterCount_Object = MibTableColumn
brMultiIFServiceFilterCount = _BrMultiIFServiceFilterCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 1, 1, 4),
    _BrMultiIFServiceFilterCount_Type()
)
brMultiIFServiceFilterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMultiIFServiceFilterCount.setStatus("mandatory")
_BrMultiIFServiceInfoTable_Object = MibTable
brMultiIFServiceInfoTable = _BrMultiIFServiceInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 2)
)
if mibBuilder.loadTexts:
    brMultiIFServiceInfoTable.setStatus("mandatory")
_BrMultiIFServiceInfoEntry_Object = MibTableRow
brMultiIFServiceInfoEntry = _BrMultiIFServiceInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 2, 1)
)
brMultiIFServiceInfoEntry.setIndexNames(
    (0, "BROTHER-MIB", "brMultiIFConfigureIndex"),
    (0, "BROTHER-MIB", "brMultiIFServiceIndex"),
)
if mibBuilder.loadTexts:
    brMultiIFServiceInfoEntry.setStatus("mandatory")


class _BrMultiIFServiceIndex_Type(Integer32):
    """Custom type brMultiIFServiceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_BrMultiIFServiceIndex_Type.__name__ = "Integer32"
_BrMultiIFServiceIndex_Object = MibTableColumn
brMultiIFServiceIndex = _BrMultiIFServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 2, 1, 1),
    _BrMultiIFServiceIndex_Type()
)
brMultiIFServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMultiIFServiceIndex.setStatus("mandatory")


class _BrMultiIFServiceName_Type(DisplayString):
    """Custom type brMultiIFServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BrMultiIFServiceName_Type.__name__ = "DisplayString"
_BrMultiIFServiceName_Object = MibTableColumn
brMultiIFServiceName = _BrMultiIFServiceName_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 2, 1, 2),
    _BrMultiIFServiceName_Type()
)
brMultiIFServiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFServiceName.setStatus("mandatory")


class _BrMultiIFServicePort_Type(Integer32):
    """Custom type brMultiIFServicePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_BrMultiIFServicePort_Type.__name__ = "Integer32"
_BrMultiIFServicePort_Object = MibTableColumn
brMultiIFServicePort = _BrMultiIFServicePort_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 2, 1, 3),
    _BrMultiIFServicePort_Type()
)
brMultiIFServicePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFServicePort.setStatus("mandatory")


class _BrMultiIFServiceFilter_Type(Integer32):
    """Custom type brMultiIFServiceFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrMultiIFServiceFilter_Type.__name__ = "Integer32"
_BrMultiIFServiceFilter_Object = MibTableColumn
brMultiIFServiceFilter = _BrMultiIFServiceFilter_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 2, 1, 4),
    _BrMultiIFServiceFilter_Type()
)
brMultiIFServiceFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFServiceFilter.setStatus("mandatory")


class _BrMultiIFServiceBOT_Type(Integer32):
    """Custom type brMultiIFServiceBOT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrMultiIFServiceBOT_Type.__name__ = "Integer32"
_BrMultiIFServiceBOT_Object = MibTableColumn
brMultiIFServiceBOT = _BrMultiIFServiceBOT_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 2, 1, 5),
    _BrMultiIFServiceBOT_Type()
)
brMultiIFServiceBOT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFServiceBOT.setStatus("mandatory")


class _BrMultiIFServiceEOT_Type(Integer32):
    """Custom type brMultiIFServiceEOT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrMultiIFServiceEOT_Type.__name__ = "Integer32"
_BrMultiIFServiceEOT_Object = MibTableColumn
brMultiIFServiceEOT = _BrMultiIFServiceEOT_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 2, 1, 6),
    _BrMultiIFServiceEOT_Type()
)
brMultiIFServiceEOT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFServiceEOT.setStatus("mandatory")


class _BrMultiIFServiceMatch_Type(Integer32):
    """Custom type brMultiIFServiceMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrMultiIFServiceMatch_Type.__name__ = "Integer32"
_BrMultiIFServiceMatch_Object = MibTableColumn
brMultiIFServiceMatch = _BrMultiIFServiceMatch_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 2, 1, 7),
    _BrMultiIFServiceMatch_Type()
)
brMultiIFServiceMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFServiceMatch.setStatus("mandatory")


class _BrMultiIFServiceReplace_Type(Integer32):
    """Custom type brMultiIFServiceReplace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrMultiIFServiceReplace_Type.__name__ = "Integer32"
_BrMultiIFServiceReplace_Object = MibTableColumn
brMultiIFServiceReplace = _BrMultiIFServiceReplace_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 2, 1, 8),
    _BrMultiIFServiceReplace_Type()
)
brMultiIFServiceReplace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFServiceReplace.setStatus("mandatory")


class _BrMultiIFServiceTCPPort_Type(Integer32):
    """Custom type brMultiIFServiceTCPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrMultiIFServiceTCPPort_Type.__name__ = "Integer32"
_BrMultiIFServiceTCPPort_Object = MibTableColumn
brMultiIFServiceTCPPort = _BrMultiIFServiceTCPPort_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 2, 1, 9),
    _BrMultiIFServiceTCPPort_Type()
)
brMultiIFServiceTCPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFServiceTCPPort.setStatus("mandatory")


class _BrMultiIFServiceNDSTree_Type(DisplayString):
    """Custom type brMultiIFServiceNDSTree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_BrMultiIFServiceNDSTree_Type.__name__ = "DisplayString"
_BrMultiIFServiceNDSTree_Object = MibTableColumn
brMultiIFServiceNDSTree = _BrMultiIFServiceNDSTree_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 2, 1, 10),
    _BrMultiIFServiceNDSTree_Type()
)
brMultiIFServiceNDSTree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFServiceNDSTree.setStatus("mandatory")


class _BrMultiIFServiceNDSContext_Type(OctetString):
    """Custom type brMultiIFServiceNDSContext based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BrMultiIFServiceNDSContext_Type.__name__ = "OctetString"
_BrMultiIFServiceNDSContext_Object = MibTableColumn
brMultiIFServiceNDSContext = _BrMultiIFServiceNDSContext_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 2, 1, 11),
    _BrMultiIFServiceNDSContext_Type()
)
brMultiIFServiceNDSContext.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFServiceNDSContext.setStatus("mandatory")


class _BrMultiIFServiceVines_Type(DisplayString):
    """Custom type brMultiIFServiceVines based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_BrMultiIFServiceVines_Type.__name__ = "DisplayString"
_BrMultiIFServiceVines_Object = MibTableColumn
brMultiIFServiceVines = _BrMultiIFServiceVines_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 2, 1, 12),
    _BrMultiIFServiceVines_Type()
)
brMultiIFServiceVines.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFServiceVines.setStatus("mandatory")


class _BrMultiIFServiceObsolete_Type(Integer32):
    """Custom type brMultiIFServiceObsolete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_BrMultiIFServiceObsolete_Type.__name__ = "Integer32"
_BrMultiIFServiceObsolete_Object = MibTableColumn
brMultiIFServiceObsolete = _BrMultiIFServiceObsolete_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 2, 1, 13),
    _BrMultiIFServiceObsolete_Type()
)
brMultiIFServiceObsolete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFServiceObsolete.setStatus("mandatory")


class _BrMultiIFServiceNetwareServerCount_Type(Integer32):
    """Custom type brMultiIFServiceNetwareServerCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_BrMultiIFServiceNetwareServerCount_Type.__name__ = "Integer32"
_BrMultiIFServiceNetwareServerCount_Object = MibTableColumn
brMultiIFServiceNetwareServerCount = _BrMultiIFServiceNetwareServerCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 2, 1, 14),
    _BrMultiIFServiceNetwareServerCount_Type()
)
brMultiIFServiceNetwareServerCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFServiceNetwareServerCount.setStatus("mandatory")


class _BrMultiIFServiceReceiveOnly_Type(Integer32):
    """Custom type brMultiIFServiceReceiveOnly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrMultiIFServiceReceiveOnly_Type.__name__ = "Integer32"
_BrMultiIFServiceReceiveOnly_Object = MibTableColumn
brMultiIFServiceReceiveOnly = _BrMultiIFServiceReceiveOnly_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 2, 1, 15),
    _BrMultiIFServiceReceiveOnly_Type()
)
brMultiIFServiceReceiveOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFServiceReceiveOnly.setStatus("mandatory")


class _BrMultiIFServiceTCPQueued_Type(Integer32):
    """Custom type brMultiIFServiceTCPQueued based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrMultiIFServiceTCPQueued_Type.__name__ = "Integer32"
_BrMultiIFServiceTCPQueued_Object = MibTableColumn
brMultiIFServiceTCPQueued = _BrMultiIFServiceTCPQueued_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 2, 1, 16),
    _BrMultiIFServiceTCPQueued_Type()
)
brMultiIFServiceTCPQueued.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFServiceTCPQueued.setStatus("mandatory")


class _BrMultiIFServiceProtocolLAT_Type(Integer32):
    """Custom type brMultiIFServiceProtocolLAT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrMultiIFServiceProtocolLAT_Type.__name__ = "Integer32"
_BrMultiIFServiceProtocolLAT_Object = MibTableColumn
brMultiIFServiceProtocolLAT = _BrMultiIFServiceProtocolLAT_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 2, 1, 17),
    _BrMultiIFServiceProtocolLAT_Type()
)
brMultiIFServiceProtocolLAT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFServiceProtocolLAT.setStatus("mandatory")


class _BrMultiIFServiceProtocolTCPIP_Type(Integer32):
    """Custom type brMultiIFServiceProtocolTCPIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrMultiIFServiceProtocolTCPIP_Type.__name__ = "Integer32"
_BrMultiIFServiceProtocolTCPIP_Object = MibTableColumn
brMultiIFServiceProtocolTCPIP = _BrMultiIFServiceProtocolTCPIP_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 2, 1, 18),
    _BrMultiIFServiceProtocolTCPIP_Type()
)
brMultiIFServiceProtocolTCPIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFServiceProtocolTCPIP.setStatus("mandatory")


class _BrMultiIFServiceProtocolNetware_Type(Integer32):
    """Custom type brMultiIFServiceProtocolNetware based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrMultiIFServiceProtocolNetware_Type.__name__ = "Integer32"
_BrMultiIFServiceProtocolNetware_Object = MibTableColumn
brMultiIFServiceProtocolNetware = _BrMultiIFServiceProtocolNetware_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 2, 1, 19),
    _BrMultiIFServiceProtocolNetware_Type()
)
brMultiIFServiceProtocolNetware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFServiceProtocolNetware.setStatus("mandatory")


class _BrMultiIFServiceProtocolAppleTalk_Type(Integer32):
    """Custom type brMultiIFServiceProtocolAppleTalk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrMultiIFServiceProtocolAppleTalk_Type.__name__ = "Integer32"
_BrMultiIFServiceProtocolAppleTalk_Object = MibTableColumn
brMultiIFServiceProtocolAppleTalk = _BrMultiIFServiceProtocolAppleTalk_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 2, 1, 20),
    _BrMultiIFServiceProtocolAppleTalk_Type()
)
brMultiIFServiceProtocolAppleTalk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFServiceProtocolAppleTalk.setStatus("mandatory")


class _BrMultiIFServiceProtocolBanyan_Type(Integer32):
    """Custom type brMultiIFServiceProtocolBanyan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrMultiIFServiceProtocolBanyan_Type.__name__ = "Integer32"
_BrMultiIFServiceProtocolBanyan_Object = MibTableColumn
brMultiIFServiceProtocolBanyan = _BrMultiIFServiceProtocolBanyan_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 2, 1, 21),
    _BrMultiIFServiceProtocolBanyan_Type()
)
brMultiIFServiceProtocolBanyan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFServiceProtocolBanyan.setStatus("mandatory")


class _BrMultiIFServiceProtocolDLC_Type(Integer32):
    """Custom type brMultiIFServiceProtocolDLC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrMultiIFServiceProtocolDLC_Type.__name__ = "Integer32"
_BrMultiIFServiceProtocolDLC_Object = MibTableColumn
brMultiIFServiceProtocolDLC = _BrMultiIFServiceProtocolDLC_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 2, 1, 22),
    _BrMultiIFServiceProtocolDLC_Type()
)
brMultiIFServiceProtocolDLC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFServiceProtocolDLC.setStatus("mandatory")


class _BrMultiIFServiceProtocolNetBEUI_Type(Integer32):
    """Custom type brMultiIFServiceProtocolNetBEUI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrMultiIFServiceProtocolNetBEUI_Type.__name__ = "Integer32"
_BrMultiIFServiceProtocolNetBEUI_Object = MibTableColumn
brMultiIFServiceProtocolNetBEUI = _BrMultiIFServiceProtocolNetBEUI_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 2, 1, 23),
    _BrMultiIFServiceProtocolNetBEUI_Type()
)
brMultiIFServiceProtocolNetBEUI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFServiceProtocolNetBEUI.setStatus("mandatory")


class _BrMultiIFServiceNetwareServerMode_Type(Integer32):
    """Custom type brMultiIFServiceNetwareServerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrMultiIFServiceNetwareServerMode_Type.__name__ = "Integer32"
_BrMultiIFServiceNetwareServerMode_Object = MibTableColumn
brMultiIFServiceNetwareServerMode = _BrMultiIFServiceNetwareServerMode_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 2, 1, 24),
    _BrMultiIFServiceNetwareServerMode_Type()
)
brMultiIFServiceNetwareServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFServiceNetwareServerMode.setStatus("mandatory")


class _BrMultiIFServiceNetwareRemotePrinterNum_Type(Integer32):
    """Custom type brMultiIFServiceNetwareRemotePrinterNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrMultiIFServiceNetwareRemotePrinterNum_Type.__name__ = "Integer32"
_BrMultiIFServiceNetwareRemotePrinterNum_Object = MibTableColumn
brMultiIFServiceNetwareRemotePrinterNum = _BrMultiIFServiceNetwareRemotePrinterNum_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 2, 1, 25),
    _BrMultiIFServiceNetwareRemotePrinterNum_Type()
)
brMultiIFServiceNetwareRemotePrinterNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFServiceNetwareRemotePrinterNum.setStatus("mandatory")


class _BrMultiIFServiceProtocolIPP_Type(Integer32):
    """Custom type brMultiIFServiceProtocolIPP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrMultiIFServiceProtocolIPP_Type.__name__ = "Integer32"
_BrMultiIFServiceProtocolIPP_Object = MibTableColumn
brMultiIFServiceProtocolIPP = _BrMultiIFServiceProtocolIPP_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 2, 1, 26),
    _BrMultiIFServiceProtocolIPP_Type()
)
brMultiIFServiceProtocolIPP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFServiceProtocolIPP.setStatus("mandatory")


class _BrMultiIFServiceAppleTalkType_Type(DisplayString):
    """Custom type brMultiIFServiceAppleTalkType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BrMultiIFServiceAppleTalkType_Type.__name__ = "DisplayString"
_BrMultiIFServiceAppleTalkType_Object = MibTableColumn
brMultiIFServiceAppleTalkType = _BrMultiIFServiceAppleTalkType_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 2, 1, 27),
    _BrMultiIFServiceAppleTalkType_Type()
)
brMultiIFServiceAppleTalkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFServiceAppleTalkType.setStatus("mandatory")
_BrMultiIFServiceStringInfoTable_Object = MibTable
brMultiIFServiceStringInfoTable = _BrMultiIFServiceStringInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 3)
)
if mibBuilder.loadTexts:
    brMultiIFServiceStringInfoTable.setStatus("mandatory")
_BrMultiIFServiceStringInfoEntry_Object = MibTableRow
brMultiIFServiceStringInfoEntry = _BrMultiIFServiceStringInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 3, 1)
)
brMultiIFServiceStringInfoEntry.setIndexNames(
    (0, "BROTHER-MIB", "brMultiIFConfigureIndex"),
    (0, "BROTHER-MIB", "brMultiIFServiceStringIndex"),
)
if mibBuilder.loadTexts:
    brMultiIFServiceStringInfoEntry.setStatus("mandatory")


class _BrMultiIFServiceStringIndex_Type(Integer32):
    """Custom type brMultiIFServiceStringIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BrMultiIFServiceStringIndex_Type.__name__ = "Integer32"
_BrMultiIFServiceStringIndex_Object = MibTableColumn
brMultiIFServiceStringIndex = _BrMultiIFServiceStringIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 3, 1, 1),
    _BrMultiIFServiceStringIndex_Type()
)
brMultiIFServiceStringIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMultiIFServiceStringIndex.setStatus("mandatory")


class _BrMultiIFServiceString_Type(DisplayString):
    """Custom type brMultiIFServiceString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BrMultiIFServiceString_Type.__name__ = "DisplayString"
_BrMultiIFServiceString_Object = MibTableColumn
brMultiIFServiceString = _BrMultiIFServiceString_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 4, 3, 1, 2),
    _BrMultiIFServiceString_Type()
)
brMultiIFServiceString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFServiceString.setStatus("mandatory")
_BrMultiIFprotocol_ObjectIdentity = ObjectIdentity
brMultiIFprotocol = _BrMultiIFprotocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5)
)
_BrMultiIFtcpip_ObjectIdentity = ObjectIdentity
brMultiIFtcpip = _BrMultiIFtcpip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 2)
)
_BrMultiIFTCPIPTable_Object = MibTable
brMultiIFTCPIPTable = _BrMultiIFTCPIPTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 2, 1)
)
if mibBuilder.loadTexts:
    brMultiIFTCPIPTable.setStatus("mandatory")
_BrMultiIFTCPIPEntry_Object = MibTableRow
brMultiIFTCPIPEntry = _BrMultiIFTCPIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 2, 1, 1)
)
brMultiIFTCPIPEntry.setIndexNames(
    (0, "BROTHER-MIB", "brMultiIFConfigureIndex"),
)
if mibBuilder.loadTexts:
    brMultiIFTCPIPEntry.setStatus("mandatory")
_BrMultiIFTCPIPAddress_Type = IpAddress
_BrMultiIFTCPIPAddress_Object = MibTableColumn
brMultiIFTCPIPAddress = _BrMultiIFTCPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 2, 1, 1, 1),
    _BrMultiIFTCPIPAddress_Type()
)
brMultiIFTCPIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFTCPIPAddress.setStatus("mandatory")
_BrMultiIFTCPIPSubnetMask_Type = IpAddress
_BrMultiIFTCPIPSubnetMask_Object = MibTableColumn
brMultiIFTCPIPSubnetMask = _BrMultiIFTCPIPSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 2, 1, 1, 2),
    _BrMultiIFTCPIPSubnetMask_Type()
)
brMultiIFTCPIPSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFTCPIPSubnetMask.setStatus("mandatory")
_BrMultiIFTCPIPGateway_Type = IpAddress
_BrMultiIFTCPIPGateway_Object = MibTableColumn
brMultiIFTCPIPGateway = _BrMultiIFTCPIPGateway_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 2, 1, 1, 3),
    _BrMultiIFTCPIPGateway_Type()
)
brMultiIFTCPIPGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFTCPIPGateway.setStatus("mandatory")


class _BrMultiIFTCPIPMethod_Type(Integer32):
    """Custom type brMultiIFTCPIPMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BrMultiIFTCPIPMethod_Type.__name__ = "Integer32"
_BrMultiIFTCPIPMethod_Object = MibTableColumn
brMultiIFTCPIPMethod = _BrMultiIFTCPIPMethod_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 2, 1, 1, 4),
    _BrMultiIFTCPIPMethod_Type()
)
brMultiIFTCPIPMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFTCPIPMethod.setStatus("mandatory")


class _BrMultiIFTCPIPUpdate_Type(OctetString):
    """Custom type brMultiIFTCPIPUpdate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_BrMultiIFTCPIPUpdate_Type.__name__ = "OctetString"
_BrMultiIFTCPIPUpdate_Object = MibTableColumn
brMultiIFTCPIPUpdate = _BrMultiIFTCPIPUpdate_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 2, 1, 1, 5),
    _BrMultiIFTCPIPUpdate_Type()
)
brMultiIFTCPIPUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFTCPIPUpdate.setStatus("mandatory")


class _BrMultiIFTCPIPTimeout_Type(Integer32):
    """Custom type brMultiIFTCPIPTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_BrMultiIFTCPIPTimeout_Type.__name__ = "Integer32"
_BrMultiIFTCPIPTimeout_Object = MibTableColumn
brMultiIFTCPIPTimeout = _BrMultiIFTCPIPTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 2, 1, 1, 6),
    _BrMultiIFTCPIPTimeout_Type()
)
brMultiIFTCPIPTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFTCPIPTimeout.setStatus("mandatory")


class _BrMultiIFTCPIPBootTries_Type(Integer32):
    """Custom type brMultiIFTCPIPBootTries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_BrMultiIFTCPIPBootTries_Type.__name__ = "Integer32"
_BrMultiIFTCPIPBootTries_Object = MibTableColumn
brMultiIFTCPIPBootTries = _BrMultiIFTCPIPBootTries_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 2, 1, 1, 7),
    _BrMultiIFTCPIPBootTries_Type()
)
brMultiIFTCPIPBootTries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFTCPIPBootTries.setStatus("mandatory")


class _BrMultiIFTCPIPRARPNoSubnet_Type(Integer32):
    """Custom type brMultiIFTCPIPRARPNoSubnet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrMultiIFTCPIPRARPNoSubnet_Type.__name__ = "Integer32"
_BrMultiIFTCPIPRARPNoSubnet_Object = MibTableColumn
brMultiIFTCPIPRARPNoSubnet = _BrMultiIFTCPIPRARPNoSubnet_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 2, 1, 1, 8),
    _BrMultiIFTCPIPRARPNoSubnet_Type()
)
brMultiIFTCPIPRARPNoSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFTCPIPRARPNoSubnet.setStatus("mandatory")


class _BrMultiIFTCPIPRARPNoGateway_Type(Integer32):
    """Custom type brMultiIFTCPIPRARPNoGateway based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrMultiIFTCPIPRARPNoGateway_Type.__name__ = "Integer32"
_BrMultiIFTCPIPRARPNoGateway_Object = MibTableColumn
brMultiIFTCPIPRARPNoGateway = _BrMultiIFTCPIPRARPNoGateway_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 2, 1, 1, 9),
    _BrMultiIFTCPIPRARPNoGateway_Type()
)
brMultiIFTCPIPRARPNoGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFTCPIPRARPNoGateway.setStatus("mandatory")


class _BrMultiIFTCPIPUseMethod_Type(Integer32):
    """Custom type brMultiIFTCPIPUseMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BrMultiIFTCPIPUseMethod_Type.__name__ = "Integer32"
_BrMultiIFTCPIPUseMethod_Object = MibTableColumn
brMultiIFTCPIPUseMethod = _BrMultiIFTCPIPUseMethod_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 2, 1, 1, 10),
    _BrMultiIFTCPIPUseMethod_Type()
)
brMultiIFTCPIPUseMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFTCPIPUseMethod.setStatus("mandatory")
_BrMultiIFTCPIPMethodServer_Type = IpAddress
_BrMultiIFTCPIPMethodServer_Object = MibTableColumn
brMultiIFTCPIPMethodServer = _BrMultiIFTCPIPMethodServer_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 2, 1, 1, 11),
    _BrMultiIFTCPIPMethodServer_Type()
)
brMultiIFTCPIPMethodServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFTCPIPMethodServer.setStatus("mandatory")
_BrMultiIFnetbeui_ObjectIdentity = ObjectIdentity
brMultiIFnetbeui = _BrMultiIFnetbeui_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 8)
)
_BrMultiIFNetBIOSTable_Object = MibTable
brMultiIFNetBIOSTable = _BrMultiIFNetBIOSTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 8, 1)
)
if mibBuilder.loadTexts:
    brMultiIFNetBIOSTable.setStatus("mandatory")
_BrMultiIFNetBIOSEntry_Object = MibTableRow
brMultiIFNetBIOSEntry = _BrMultiIFNetBIOSEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 8, 1, 1)
)
brMultiIFNetBIOSEntry.setIndexNames(
    (0, "BROTHER-MIB", "brMultiIFConfigureIndex"),
)
if mibBuilder.loadTexts:
    brMultiIFNetBIOSEntry.setStatus("mandatory")


class _BrMultiIFNetBIOSIPMethod_Type(Integer32):
    """Custom type brMultiIFNetBIOSIPMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrMultiIFNetBIOSIPMethod_Type.__name__ = "Integer32"
_BrMultiIFNetBIOSIPMethod_Object = MibTableColumn
brMultiIFNetBIOSIPMethod = _BrMultiIFNetBIOSIPMethod_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 8, 1, 1, 1),
    _BrMultiIFNetBIOSIPMethod_Type()
)
brMultiIFNetBIOSIPMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFNetBIOSIPMethod.setStatus("mandatory")
_BrMultiIFTCPIPNetBIOSPrimaryWINSAddr_Type = IpAddress
_BrMultiIFTCPIPNetBIOSPrimaryWINSAddr_Object = MibTableColumn
brMultiIFTCPIPNetBIOSPrimaryWINSAddr = _BrMultiIFTCPIPNetBIOSPrimaryWINSAddr_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 8, 1, 1, 2),
    _BrMultiIFTCPIPNetBIOSPrimaryWINSAddr_Type()
)
brMultiIFTCPIPNetBIOSPrimaryWINSAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFTCPIPNetBIOSPrimaryWINSAddr.setStatus("mandatory")
_BrMultiIFTCPIPNetBIOSSecondaryWINSAddr_Type = IpAddress
_BrMultiIFTCPIPNetBIOSSecondaryWINSAddr_Object = MibTableColumn
brMultiIFTCPIPNetBIOSSecondaryWINSAddr = _BrMultiIFTCPIPNetBIOSSecondaryWINSAddr_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 8, 1, 1, 3),
    _BrMultiIFTCPIPNetBIOSSecondaryWINSAddr_Type()
)
brMultiIFTCPIPNetBIOSSecondaryWINSAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFTCPIPNetBIOSSecondaryWINSAddr.setStatus("mandatory")


class _BrMultiIFNetBEUIDomain_Type(DisplayString):
    """Custom type brMultiIFNetBEUIDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_BrMultiIFNetBEUIDomain_Type.__name__ = "DisplayString"
_BrMultiIFNetBEUIDomain_Object = MibTableColumn
brMultiIFNetBEUIDomain = _BrMultiIFNetBEUIDomain_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 8, 1, 1, 4),
    _BrMultiIFNetBEUIDomain_Type()
)
brMultiIFNetBEUIDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFNetBEUIDomain.setStatus("mandatory")
_BrMultiIForiginalapipa_ObjectIdentity = ObjectIdentity
brMultiIForiginalapipa = _BrMultiIForiginalapipa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 12)
)
_BrMultiIFAPIPATable_Object = MibTable
brMultiIFAPIPATable = _BrMultiIFAPIPATable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 12, 1)
)
if mibBuilder.loadTexts:
    brMultiIFAPIPATable.setStatus("mandatory")
_BrMultiIFAPIPAEntry_Object = MibTableRow
brMultiIFAPIPAEntry = _BrMultiIFAPIPAEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 12, 1, 1)
)
brMultiIFAPIPAEntry.setIndexNames(
    (0, "BROTHER-MIB", "brMultiIFConfigureIndex"),
)
if mibBuilder.loadTexts:
    brMultiIFAPIPAEntry.setStatus("mandatory")


class _BrMultiIFAPIPASupported_Type(Integer32):
    """Custom type brMultiIFAPIPASupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrMultiIFAPIPASupported_Type.__name__ = "Integer32"
_BrMultiIFAPIPASupported_Object = MibTableColumn
brMultiIFAPIPASupported = _BrMultiIFAPIPASupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 12, 1, 1, 1),
    _BrMultiIFAPIPASupported_Type()
)
brMultiIFAPIPASupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMultiIFAPIPASupported.setStatus("mandatory")


class _BrMultiIFAPIPAEnable_Type(Integer32):
    """Custom type brMultiIFAPIPAEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrMultiIFAPIPAEnable_Type.__name__ = "Integer32"
_BrMultiIFAPIPAEnable_Object = MibTableColumn
brMultiIFAPIPAEnable = _BrMultiIFAPIPAEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 12, 1, 1, 2),
    _BrMultiIFAPIPAEnable_Type()
)
brMultiIFAPIPAEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFAPIPAEnable.setStatus("mandatory")
_BrMultiIForiginalLAA_ObjectIdentity = ObjectIdentity
brMultiIForiginalLAA = _BrMultiIForiginalLAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 14)
)
_BrMultiIFLAATable_Object = MibTable
brMultiIFLAATable = _BrMultiIFLAATable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 14, 1)
)
if mibBuilder.loadTexts:
    brMultiIFLAATable.setStatus("mandatory")
_BrMultiIFLAAEntry_Object = MibTableRow
brMultiIFLAAEntry = _BrMultiIFLAAEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 14, 1, 1)
)
brMultiIFLAAEntry.setIndexNames(
    (0, "BROTHER-MIB", "brMultiIFConfigureIndex"),
)
if mibBuilder.loadTexts:
    brMultiIFLAAEntry.setStatus("mandatory")


class _BrMultiIFLAASupported_Type(Integer32):
    """Custom type brMultiIFLAASupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BrMultiIFLAASupported_Type.__name__ = "Integer32"
_BrMultiIFLAASupported_Object = MibTableColumn
brMultiIFLAASupported = _BrMultiIFLAASupported_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 14, 1, 1, 1),
    _BrMultiIFLAASupported_Type()
)
brMultiIFLAASupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMultiIFLAASupported.setStatus("mandatory")


class _BrMultiIFLAAMacAddress_Type(OctetString):
    """Custom type brMultiIFLAAMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_BrMultiIFLAAMacAddress_Type.__name__ = "OctetString"
_BrMultiIFLAAMacAddress_Object = MibTableColumn
brMultiIFLAAMacAddress = _BrMultiIFLAAMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 14, 1, 1, 2),
    _BrMultiIFLAAMacAddress_Type()
)
brMultiIFLAAMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFLAAMacAddress.setStatus("mandatory")
_BrMultiIForiginalIPv6_ObjectIdentity = ObjectIdentity
brMultiIForiginalIPv6 = _BrMultiIForiginalIPv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 15)
)
_BrMultiIFIPv6AddressCountTable_Object = MibTable
brMultiIFIPv6AddressCountTable = _BrMultiIFIPv6AddressCountTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 15, 1)
)
if mibBuilder.loadTexts:
    brMultiIFIPv6AddressCountTable.setStatus("mandatory")
_BrMultiIFIPv6AddressCountEntry_Object = MibTableRow
brMultiIFIPv6AddressCountEntry = _BrMultiIFIPv6AddressCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 15, 1, 1)
)
brMultiIFIPv6AddressCountEntry.setIndexNames(
    (0, "BROTHER-MIB", "brMultiIFConfigureIndex"),
)
if mibBuilder.loadTexts:
    brMultiIFIPv6AddressCountEntry.setStatus("mandatory")
_BrMultiIFIPv6AddressCount_Type = Integer32
_BrMultiIFIPv6AddressCount_Object = MibTableColumn
brMultiIFIPv6AddressCount = _BrMultiIFIPv6AddressCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 15, 1, 1, 1),
    _BrMultiIFIPv6AddressCount_Type()
)
brMultiIFIPv6AddressCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMultiIFIPv6AddressCount.setStatus("mandatory")
_BrMultiIFIPv6AddressTable_Object = MibTable
brMultiIFIPv6AddressTable = _BrMultiIFIPv6AddressTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 15, 2)
)
if mibBuilder.loadTexts:
    brMultiIFIPv6AddressTable.setStatus("mandatory")
_BrMultiIFIPv6AddressEntry_Object = MibTableRow
brMultiIFIPv6AddressEntry = _BrMultiIFIPv6AddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 15, 2, 1)
)
brMultiIFIPv6AddressEntry.setIndexNames(
    (0, "BROTHER-MIB", "brMultiIFConfigureIndex"),
    (0, "BROTHER-MIB", "brMultiIFIPv6AddressIndex"),
)
if mibBuilder.loadTexts:
    brMultiIFIPv6AddressEntry.setStatus("mandatory")


class _BrMultiIFIPv6AddressIndex_Type(Integer32):
    """Custom type brMultiIFIPv6AddressIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BrMultiIFIPv6AddressIndex_Type.__name__ = "Integer32"
_BrMultiIFIPv6AddressIndex_Object = MibTableColumn
brMultiIFIPv6AddressIndex = _BrMultiIFIPv6AddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 15, 2, 1, 1),
    _BrMultiIFIPv6AddressIndex_Type()
)
brMultiIFIPv6AddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMultiIFIPv6AddressIndex.setStatus("mandatory")
_BrMultiIFIPv6Address_Type = Ipv6Address
_BrMultiIFIPv6Address_Object = MibTableColumn
brMultiIFIPv6Address = _BrMultiIFIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 15, 2, 1, 2),
    _BrMultiIFIPv6Address_Type()
)
brMultiIFIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMultiIFIPv6Address.setStatus("mandatory")


class _BrMultiIFIPv6UseMethod_Type(Integer32):
    """Custom type brMultiIFIPv6UseMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BrMultiIFIPv6UseMethod_Type.__name__ = "Integer32"
_BrMultiIFIPv6UseMethod_Object = MibTableColumn
brMultiIFIPv6UseMethod = _BrMultiIFIPv6UseMethod_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 15, 2, 1, 3),
    _BrMultiIFIPv6UseMethod_Type()
)
brMultiIFIPv6UseMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMultiIFIPv6UseMethod.setStatus("mandatory")


class _BrMultiIFIPv6MethodServer_Type(DisplayString):
    """Custom type brMultiIFIPv6MethodServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BrMultiIFIPv6MethodServer_Type.__name__ = "DisplayString"
_BrMultiIFIPv6MethodServer_Object = MibTableColumn
brMultiIFIPv6MethodServer = _BrMultiIFIPv6MethodServer_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 15, 2, 1, 4),
    _BrMultiIFIPv6MethodServer_Type()
)
brMultiIFIPv6MethodServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMultiIFIPv6MethodServer.setStatus("mandatory")
_BrMultiIFIPv6StaticAddressCountTable_Object = MibTable
brMultiIFIPv6StaticAddressCountTable = _BrMultiIFIPv6StaticAddressCountTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 15, 3)
)
if mibBuilder.loadTexts:
    brMultiIFIPv6StaticAddressCountTable.setStatus("mandatory")
_BrMultiIFIPv6StaticAddressCountEntry_Object = MibTableRow
brMultiIFIPv6StaticAddressCountEntry = _BrMultiIFIPv6StaticAddressCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 15, 3, 1)
)
brMultiIFIPv6StaticAddressCountEntry.setIndexNames(
    (0, "BROTHER-MIB", "brMultiIFConfigureIndex"),
)
if mibBuilder.loadTexts:
    brMultiIFIPv6StaticAddressCountEntry.setStatus("mandatory")
_BrMultiIFIPv6StaticAddressCount_Type = Integer32
_BrMultiIFIPv6StaticAddressCount_Object = MibTableColumn
brMultiIFIPv6StaticAddressCount = _BrMultiIFIPv6StaticAddressCount_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 15, 3, 1, 1),
    _BrMultiIFIPv6StaticAddressCount_Type()
)
brMultiIFIPv6StaticAddressCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMultiIFIPv6StaticAddressCount.setStatus("mandatory")
_BrMultiIFIPv6StaticAddressTable_Object = MibTable
brMultiIFIPv6StaticAddressTable = _BrMultiIFIPv6StaticAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 15, 4)
)
if mibBuilder.loadTexts:
    brMultiIFIPv6StaticAddressTable.setStatus("mandatory")
_BrMultiIFIPv6StaticAddressEntry_Object = MibTableRow
brMultiIFIPv6StaticAddressEntry = _BrMultiIFIPv6StaticAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 15, 4, 1)
)
brMultiIFIPv6StaticAddressEntry.setIndexNames(
    (0, "BROTHER-MIB", "brMultiIFConfigureIndex"),
    (0, "BROTHER-MIB", "brMultiIFIPv6StaticAddressIndex"),
)
if mibBuilder.loadTexts:
    brMultiIFIPv6StaticAddressEntry.setStatus("mandatory")


class _BrMultiIFIPv6StaticAddressIndex_Type(Integer32):
    """Custom type brMultiIFIPv6StaticAddressIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BrMultiIFIPv6StaticAddressIndex_Type.__name__ = "Integer32"
_BrMultiIFIPv6StaticAddressIndex_Object = MibTableColumn
brMultiIFIPv6StaticAddressIndex = _BrMultiIFIPv6StaticAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 15, 4, 1, 1),
    _BrMultiIFIPv6StaticAddressIndex_Type()
)
brMultiIFIPv6StaticAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMultiIFIPv6StaticAddressIndex.setStatus("mandatory")
_BrMultiIFIPv6StaticAddressEnable_Type = Integer32
_BrMultiIFIPv6StaticAddressEnable_Object = MibTableColumn
brMultiIFIPv6StaticAddressEnable = _BrMultiIFIPv6StaticAddressEnable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 15, 4, 1, 2),
    _BrMultiIFIPv6StaticAddressEnable_Type()
)
brMultiIFIPv6StaticAddressEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFIPv6StaticAddressEnable.setStatus("mandatory")
_BrMultiIFIPv6StaticAddress_Type = Ipv6Address
_BrMultiIFIPv6StaticAddress_Object = MibTableColumn
brMultiIFIPv6StaticAddress = _BrMultiIFIPv6StaticAddress_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 15, 4, 1, 3),
    _BrMultiIFIPv6StaticAddress_Type()
)
brMultiIFIPv6StaticAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFIPv6StaticAddress.setStatus("mandatory")
_BrMultiIFIPv6StaticAddressPrefixLength_Type = Integer32
_BrMultiIFIPv6StaticAddressPrefixLength_Object = MibTableColumn
brMultiIFIPv6StaticAddressPrefixLength = _BrMultiIFIPv6StaticAddressPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 15, 4, 1, 4),
    _BrMultiIFIPv6StaticAddressPrefixLength_Type()
)
brMultiIFIPv6StaticAddressPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFIPv6StaticAddressPrefixLength.setStatus("mandatory")
_BrMultiIFDNSIPv6AddressTable_Object = MibTable
brMultiIFDNSIPv6AddressTable = _BrMultiIFDNSIPv6AddressTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 15, 5)
)
if mibBuilder.loadTexts:
    brMultiIFDNSIPv6AddressTable.setStatus("mandatory")
_BrMultiIFDNSIPv6AddressEntry_Object = MibTableRow
brMultiIFDNSIPv6AddressEntry = _BrMultiIFDNSIPv6AddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 15, 5, 1)
)
brMultiIFDNSIPv6AddressEntry.setIndexNames(
    (0, "BROTHER-MIB", "brMultiIFConfigureIndex"),
)
if mibBuilder.loadTexts:
    brMultiIFDNSIPv6AddressEntry.setStatus("mandatory")
_BrMultiIFPrimaryDNSIPv6Address_Type = Ipv6Address
_BrMultiIFPrimaryDNSIPv6Address_Object = MibTableColumn
brMultiIFPrimaryDNSIPv6Address = _BrMultiIFPrimaryDNSIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 15, 5, 1, 1),
    _BrMultiIFPrimaryDNSIPv6Address_Type()
)
brMultiIFPrimaryDNSIPv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFPrimaryDNSIPv6Address.setStatus("mandatory")
_BrMultiIFSecondaryDNSIPv6Address_Type = Ipv6Address
_BrMultiIFSecondaryDNSIPv6Address_Object = MibTableColumn
brMultiIFSecondaryDNSIPv6Address = _BrMultiIFSecondaryDNSIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 15, 5, 1, 2),
    _BrMultiIFSecondaryDNSIPv6Address_Type()
)
brMultiIFSecondaryDNSIPv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFSecondaryDNSIPv6Address.setStatus("mandatory")
_BrMultiIForiginalWebServices_ObjectIdentity = ObjectIdentity
brMultiIForiginalWebServices = _BrMultiIForiginalWebServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 16)
)
_BrMultiIFWebServicesTable_Object = MibTable
brMultiIFWebServicesTable = _BrMultiIFWebServicesTable_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 16, 1)
)
if mibBuilder.loadTexts:
    brMultiIFWebServicesTable.setStatus("mandatory")
_BrMultiIFWebServicesEntry_Object = MibTableRow
brMultiIFWebServicesEntry = _BrMultiIFWebServicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 16, 1, 1)
)
brMultiIFWebServicesEntry.setIndexNames(
    (0, "BROTHER-MIB", "brMultiIFConfigureIndex"),
)
if mibBuilder.loadTexts:
    brMultiIFWebServicesEntry.setStatus("mandatory")


class _BrMultiIFWebServicesName_Type(DisplayString):
    """Custom type brMultiIFWebServicesName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BrMultiIFWebServicesName_Type.__name__ = "DisplayString"
_BrMultiIFWebServicesName_Object = MibTableColumn
brMultiIFWebServicesName = _BrMultiIFWebServicesName_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 16, 1, 1, 1),
    _BrMultiIFWebServicesName_Type()
)
brMultiIFWebServicesName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFWebServicesName.setStatus("mandatory")


class _BrMultiIFWebServicesInstanceID_Type(Integer32):
    """Custom type brMultiIFWebServicesInstanceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BrMultiIFWebServicesInstanceID_Type.__name__ = "Integer32"
_BrMultiIFWebServicesInstanceID_Object = MibTableColumn
brMultiIFWebServicesInstanceID = _BrMultiIFWebServicesInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 16, 1, 1, 2),
    _BrMultiIFWebServicesInstanceID_Type()
)
brMultiIFWebServicesInstanceID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFWebServicesInstanceID.setStatus("mandatory")


class _BrMultiIFWebServicesMetadataVersion_Type(Integer32):
    """Custom type brMultiIFWebServicesMetadataVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BrMultiIFWebServicesMetadataVersion_Type.__name__ = "Integer32"
_BrMultiIFWebServicesMetadataVersion_Object = MibTableColumn
brMultiIFWebServicesMetadataVersion = _BrMultiIFWebServicesMetadataVersion_Object(
    (1, 3, 6, 1, 4, 1, 2435, 2, 4, 4, 1240, 5, 16, 1, 1, 3),
    _BrMultiIFWebServicesMetadataVersion_Type()
)
brMultiIFWebServicesMetadataVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brMultiIFWebServicesMetadataVersion.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BROTHER-MIB",
    **{"brother": brother,
       "nm": nm,
       "system": system,
       "net-peripheral": net_peripheral,
       "net-printer": net_printer,
       "generalDeviceStatus": generalDeviceStatus,
       "status": status,
       "brJamPlace": brJamPlace,
       "tonerlow": tonerlow,
       "brToner1Low": brToner1Low,
       "brToner2Low": brToner2Low,
       "brToner3Low": brToner3Low,
       "brToner4Low": brToner4Low,
       "brieee1284id": brieee1284id,
       "brttt1": brttt1,
       "net-MFP": net_MFP,
       "fax-setup": fax_setup,
       "autodial": autodial,
       "onetouchDial": onetouchDial,
       "brOneTouchDialCount": brOneTouchDialCount,
       "brOneTouchDialTable": brOneTouchDialTable,
       "brOneTouchDialEntry": brOneTouchDialEntry,
       "brOneTouchDialIndex": brOneTouchDialIndex,
       "brOneTouchDialData": brOneTouchDialData,
       "speedDial": speedDial,
       "brSpeedDialCount": brSpeedDialCount,
       "brSpeedDialTable": brSpeedDialTable,
       "brSpeedDialEntry": brSpeedDialEntry,
       "brSpeedDialIndex": brSpeedDialIndex,
       "brSpeedDialData": brSpeedDialData,
       "brDialDataAllClear": brDialDataAllClear,
       "fax-general": fax_general,
       "brFaxReceiveMode": brFaxReceiveMode,
       "brRingDelayCount": brRingDelayCount,
       "brOwnFaxNumber": brOwnFaxNumber,
       "scanner-setup": scanner_setup,
       "scanToInfo": scanToInfo,
       "brRegisterKeyInfo": brRegisterKeyInfo,
       "brUnRegisterKeyInfo": brUnRegisterKeyInfo,
       "brNetSKeyReceiverAddress": brNetSKeyReceiverAddress,
       "mfpCapability": mfpCapability,
       "mcGeneral": mcGeneral,
       "mcgRemoteSetup": mcgRemoteSetup,
       "brNetRemoteSetUpSupported": brNetRemoteSetUpSupported,
       "brNetRemoteSetUpEnable": brNetRemoteSetUpEnable,
       "brNetRemoteSetUpFileFormat": brNetRemoteSetUpFileFormat,
       "mcFax": mcFax,
       "mcfGeneral": mcfGeneral,
       "brFaxSupported": brFaxSupported,
       "brIFaxSupported": brIFaxSupported,
       "mcfNetFaxShare": mcfNetFaxShare,
       "brNetFaxShareSupported": brNetFaxShareSupported,
       "brNetFaxShareEnable": brNetFaxShareEnable,
       "mcfNetPcFaxRx": mcfNetPcFaxRx,
       "brNetPcFaxRxSupported": brNetPcFaxRxSupported,
       "brNetPcFaxRxEnable": brNetPcFaxRxEnable,
       "brNetRegisterPcFaxInfo": brNetRegisterPcFaxInfo,
       "mcfFaxInfomation": mcfFaxInfomation,
       "brPhoneNumberLastFax": brPhoneNumberLastFax,
       "brPagesSentLastFax": brPagesSentLastFax,
       "brTimestampLastFax": brTimestampLastFax,
       "brFaxHeaderInfo": brFaxHeaderInfo,
       "mcScanner": mcScanner,
       "mcsNetScanner": mcsNetScanner,
       "brNetScannerSupported": brNetScannerSupported,
       "brNetScannerEnable": brNetScannerEnable,
       "mcsNetSKy": mcsNetSKy,
       "brNetSKeySupported": brNetSKeySupported,
       "brNetSKeyEnable": brNetSKeyEnable,
       "mfpgeneral-setup": mfpgeneral_setup,
       "brServiceMode": brServiceMode,
       "brLockMode": brLockMode,
       "brActivityReportSetting": brActivityReportSetting,
       "netPML": netPML,
       "netPMLmgmt": netPMLmgmt,
       "device": device,
       "destination-subsystem1": destination_subsystem1,
       "sleep": sleep,
       "brpowerstime": brpowerstime,
       "autoc": autoc,
       "brautocont": brautocont,
       "simm": simm,
       "specification": specification,
       "simmkind0": simmkind0,
       "brsimmtype0": brsimmtype0,
       "brsimmsize0": brsimmsize0,
       "simmkind1": simmkind1,
       "brsimmtype1": brsimmtype1,
       "brsimmsize1": brsimmsize1,
       "simmkind2": simmkind2,
       "brsimmtype2": brsimmtype2,
       "brsimmsize2": brsimmsize2,
       "simmkind3": simmkind3,
       "brsimmtype3": brsimmtype3,
       "brsimmsize3": brsimmsize3,
       "bio1-explanation": bio1_explanation,
       "determined": determined,
       "brTBD1": brTBD1,
       "destination-subsystem2": destination_subsystem2,
       "printerjob": printerjob,
       "jobend": jobend,
       "brtimeout": brtimeout,
       "brTBD2": brTBD2,
       "destination-subsystem3": destination_subsystem3,
       "prt-setup": prt_setup,
       "prt-condition": prt_condition,
       "brpersonality": brpersonality,
       "brorientation": brorientation,
       "brcopies": brcopies,
       "brTBD3": brTBD3,
       "brresolution": brresolution,
       "brpageprotect": brpageprotect,
       "brlines": brlines,
       "brpaper": brpaper,
       "brpapertype": brpapertype,
       "brpapertype2": brpapertype2,
       "brpapertypeMP": brpapertypeMP,
       "destination-subsystem4": destination_subsystem4,
       "print-engine": print_engine,
       "prt-density": prt_density,
       "brdensity": brdensity,
       "status-prt-eng": status_prt_eng,
       "tray": tray,
       "manual": manual,
       "brmanualfeed": brmanualfeed,
       "traysize": traysize,
       "mp": mp,
       "brmpsize": brmpsize,
       "cassette": cassette,
       "brtray1size": brtray1size,
       "cassette2": cassette2,
       "brtray2size": brtray2size,
       "cassette3": cassette3,
       "brtray3size": brtray3size,
       "cassette4": cassette4,
       "brtray4size": brtray4size,
       "economy": economy,
       "brret": brret,
       "breconomode": breconomode,
       "brorg": brorg,
       "printersetup": printersetup,
       "general": general,
       "brPrtGeneralEmulationTimeout": brPrtGeneralEmulationTimeout,
       "brPrtGeneralFeeder": brPrtGeneralFeeder,
       "brPrtGeneralPowerSave": brPrtGeneralPowerSave,
       "brPrtGeneralBuzzer": brPrtGeneralBuzzer,
       "brPrtGeneralColor": brPrtGeneralColor,
       "brPrtGeneralDuplex": brPrtGeneralDuplex,
       "brPrtGeneralBinding": brPrtGeneralBinding,
       "advanced": advanced,
       "brPrtAdvancedPriority": brPrtAdvancedPriority,
       "brPrtAdvancedUseMPTrayFirst": brPrtAdvancedUseMPTrayFirst,
       "brPrtAdvancedMPTrayFeed": brPrtAdvancedMPTrayFeed,
       "brPrtAdvancedXOffset": brPrtAdvancedXOffset,
       "brPrtAdvancedYOffset": brPrtAdvancedYOffset,
       "brPrtAdvancedImageCompression": brPrtAdvancedImageCompression,
       "autoff": autoff,
       "brPrtAdvancedAutoFormFeed": brPrtAdvancedAutoFormFeed,
       "brPrtAdvancedAutoTimeout": brPrtAdvancedAutoTimeout,
       "brPrtAdvancedFFSuppress": brPrtAdvancedFFSuppress,
       "brPrtAdvancedTonerLowPrint": brPrtAdvancedTonerLowPrint,
       "brPrtAdvancedPrintDensity": brPrtAdvancedPrintDensity,
       "brPrtAdvancedInputBuffer": brPrtAdvancedInputBuffer,
       "brPrtAdvancedLanguage": brPrtAdvancedLanguage,
       "brSecurePrintRAMSizeMax": brSecurePrintRAMSizeMax,
       "brSecurePrintRAMSize": brSecurePrintRAMSize,
       "brPrtAdvancedJamRecovery": brPrtAdvancedJamRecovery,
       "brPrtAdvancedSleepIndication": brPrtAdvancedSleepIndication,
       "brPrtAdvancedDestination": brPrtAdvancedDestination,
       "brPrtAdvancedLowerLCD": brPrtAdvancedLowerLCD,
       "brPrtAdvancedAutoOnline": brPrtAdvancedAutoOnline,
       "brPrtAdvancedButtonRepeat": brPrtAdvancedButtonRepeat,
       "brPrtAdvancedMessageScroll": brPrtAdvancedMessageScroll,
       "buzzer": buzzer,
       "brPrtAdvancedErrorBuzzer": brPrtAdvancedErrorBuzzer,
       "brPrtAdvancedPanelBuzzer": brPrtAdvancedPanelBuzzer,
       "brPrtAdvancedBuzzerVolume": brPrtAdvancedBuzzerVolume,
       "brPrtAdvancedLCDDensity": brPrtAdvancedLCDDensity,
       "smallPaperSize": smallPaperSize,
       "brSmallPaperSizeMP": brSmallPaperSizeMP,
       "brSmallPaperSize1": brSmallPaperSize1,
       "brSmallPaperSize2": brSmallPaperSize2,
       "brSmallPaperSize3": brSmallPaperSize3,
       "brSmallPaperSize4": brSmallPaperSize4,
       "trayPriority": trayPriority,
       "brPrtAdvancedTrayPriority": brPrtAdvancedTrayPriority,
       "brTrayPriorityCount": brTrayPriorityCount,
       "brTrayPriorityTable": brTrayPriorityTable,
       "brTrayPriorityEntry": brTrayPriorityEntry,
       "brTrayPriorityIndex": brTrayPriorityIndex,
       "brTrayPriorityMember": brTrayPriorityMember,
       "carbonCopy": carbonCopy,
       "brCarbonCopyMode": brCarbonCopyMode,
       "brCarbonCopies": brCarbonCopies,
       "brCarbonCopyTable": brCarbonCopyTable,
       "brCarbonCopyEntry": brCarbonCopyEntry,
       "brCarbonCopyIndex": brCarbonCopyIndex,
       "brCarbonCopyTray": brCarbonCopyTray,
       "brCarbonCopyMacro": brCarbonCopyMacro,
       "brCarbonCopyMacroID": brCarbonCopyMacroID,
       "mediaFix": mediaFix,
       "brMediaFixTray1": brMediaFixTray1,
       "brMediaFixTray2": brMediaFixTray2,
       "brMediaFixTray3": brMediaFixTray3,
       "brMediaFixTray4": brMediaFixTray4,
       "brMediaFixMP": brMediaFixMP,
       "directprint": directprint,
       "brDirectPrintPaperSize": brDirectPrintPaperSize,
       "brDirectPrintMediaType": brDirectPrintMediaType,
       "brDirectPrintMultipulPage": brDirectPrintMultipulPage,
       "brDirectPrintOrientation": brDirectPrintOrientation,
       "brDirectPrintCollate": brDirectPrintCollate,
       "brDirectPrintOutputColor": brDirectPrintOutputColor,
       "brDirectPrintPrintQuality": brDirectPrintPrintQuality,
       "brDirectPrintPdfOption": brDirectPrintPdfOption,
       "brDirectPrintSetting": brDirectPrintSetting,
       "brDirectPrintPdfThumbnailType": brDirectPrintPdfThumbnailType,
       "pictbridge": pictbridge,
       "brPictBridgePaperSize": brPictBridgePaperSize,
       "brPictBridgeOrientation": brPictBridgeOrientation,
       "brPictBridgeDateTime": brPictBridgeDateTime,
       "brPictBridgeFileName": brPictBridgeFileName,
       "brPictBridgePrintQuality": brPictBridgePrintQuality,
       "brPictBridgePrintSetting": brPictBridgePrintSetting,
       "colorcorrection": colorcorrection,
       "brColorCalibration": brColorCalibration,
       "brColorCalibrationReset": brColorCalibrationReset,
       "brAutoRegistRegistrate": brAutoRegistRegistrate,
       "brAutoRegistSetInterval": brAutoRegistSetInterval,
       "brRegistrationPrintChart": brRegistrationPrintChart,
       "brRegistrationXMagentaLeft": brRegistrationXMagentaLeft,
       "brRegistrationXMagentaRight": brRegistrationXMagentaRight,
       "brRegistrationXCyanLeft": brRegistrationXCyanLeft,
       "brRegistrationXCyanRight": brRegistrationXCyanRight,
       "brRegistrationXYellowLeft": brRegistrationXYellowLeft,
       "brRegistrationXYellowRight": brRegistrationXYellowRight,
       "brRegistrationYMagenta": brRegistrationYMagenta,
       "brRegistrationYCyan": brRegistrationYCyan,
       "brRegistrationYYellow": brRegistrationYYellow,
       "funclock": funclock,
       "brFuncLockSettingInit": brFuncLockSettingInit,
       "brFuncLockAdminPassword": brFuncLockAdminPassword,
       "brFuncLock": brFuncLock,
       "brFuncLockPublicFuncCount": brFuncLockPublicFuncCount,
       "brFuncLockPublicTable": brFuncLockPublicTable,
       "brFuncLockPublicEntry": brFuncLockPublicEntry,
       "brFuncLockPublicFuncIndex": brFuncLockPublicFuncIndex,
       "brFuncLockPublicFuncMember": brFuncLockPublicFuncMember,
       "brFuncLockPublicFuncSupported": brFuncLockPublicFuncSupported,
       "brFuncLockPublicFuncEnable": brFuncLockPublicFuncEnable,
       "brFuncLockUserCount": brFuncLockUserCount,
       "brFuncLockUserTable": brFuncLockUserTable,
       "brFuncLockUserEntry": brFuncLockUserEntry,
       "brFuncLockUserIndex": brFuncLockUserIndex,
       "brFuncLockUserName": brFuncLockUserName,
       "brFuncLockUserPassword": brFuncLockUserPassword,
       "brFuncLockUserFuncCount": brFuncLockUserFuncCount,
       "brFuncLockUserFuncTable": brFuncLockUserFuncTable,
       "brFuncLockUserFuncEntry": brFuncLockUserFuncEntry,
       "brFuncLockUserFuncIndex": brFuncLockUserFuncIndex,
       "brFuncLockUserFuncMember": brFuncLockUserFuncMember,
       "brFuncLockUserFuncSupported": brFuncLockUserFuncSupported,
       "brFuncLockUserFuncEnable": brFuncLockUserFuncEnable,
       "brFuncLockSetting": brFuncLockSetting,
       "brFuncLockUserPrintPageCounterReset": brFuncLockUserPrintPageCounterReset,
       "brFuncLockPublicPrintLimitEnable": brFuncLockPublicPrintLimitEnable,
       "brFuncLockPublicPrintPageMax": brFuncLockPublicPrintPageMax,
       "brFuncLockPublicPrintPageCountMono": brFuncLockPublicPrintPageCountMono,
       "brFuncLockPublicPrintPageCountColor": brFuncLockPublicPrintPageCountColor,
       "brFuncLockUserPrintPageTable": brFuncLockUserPrintPageTable,
       "brFuncLockUserPrintPageEntry": brFuncLockUserPrintPageEntry,
       "brFuncLockUserPrintPageIndex": brFuncLockUserPrintPageIndex,
       "brFuncLockUserPrintPageLimitEnable": brFuncLockUserPrintPageLimitEnable,
       "brFuncLockUserPrintPageCountMono": brFuncLockUserPrintPageCountMono,
       "brFuncLockUserPrintPageCountColor": brFuncLockUserPrintPageCountColor,
       "brFuncLockUserPrintPageMax": brFuncLockUserPrintPageMax,
       "brFuncLockUserPrintPageCountMonoLast": brFuncLockUserPrintPageCountMonoLast,
       "brFuncLockUserPrintPageCountColorLast": brFuncLockUserPrintPageCountColorLast,
       "brFuncLockPcLoginNameAuthEnable": brFuncLockPcLoginNameAuthEnable,
       "brFuncLockPcLoginNameAuthCount": brFuncLockPcLoginNameAuthCount,
       "brFuncLockPcLoginNameTable": brFuncLockPcLoginNameTable,
       "brFuncLockPcLoginNameEntry": brFuncLockPcLoginNameEntry,
       "brFuncLockPcLoginNameAuthIndex": brFuncLockPcLoginNameAuthIndex,
       "brFuncLockPcLoginName": brFuncLockPcLoginName,
       "brFuncLockPcLoginNameAuthID": brFuncLockPcLoginNameAuthID,
       "brFuncLockPublicPrintPageCountMonoLast": brFuncLockPublicPrintPageCountMonoLast,
       "brFuncLockPublicPrintPageCountColorLast": brFuncLockPublicPrintPageCountColorLast,
       "autocountreset": autocountreset,
       "brFuncLockAutoCountResetFrequency": brFuncLockAutoCountResetFrequency,
       "brFuncLockAutoCountResetTime": brFuncLockAutoCountResetTime,
       "brFuncLockAutoCountResetWeek": brFuncLockAutoCountResetWeek,
       "brFuncLockAutoCountResetDate": brFuncLockAutoCountResetDate,
       "mail": mail,
       "brPrtMailbox": brPrtMailbox,
       "brPrtMailboxProtectTable": brPrtMailboxProtectTable,
       "brPrtMailboxProtectEntry": brPrtMailboxProtectEntry,
       "brPrtMailboxProtectIndex": brPrtMailboxProtectIndex,
       "brPrtMailboxProtect": brPrtMailboxProtect,
       "brPrtAvoidMailboxFullTable": brPrtAvoidMailboxFullTable,
       "brPrtAvoidMailboxFullEntry": brPrtAvoidMailboxFullEntry,
       "brPrtAvoidMailboxFullIndex": brPrtAvoidMailboxFullIndex,
       "brPrtAvoidMailboxFull": brPrtAvoidMailboxFull,
       "brPrtMailboxOutbin": brPrtMailboxOutbin,
       "brPrtMailboxProtectGroup": brPrtMailboxProtectGroup,
       "brPrtAvoidMailboxFullGroup": brPrtAvoidMailboxFullGroup,
       "finisher": finisher,
       "brPrtFinisher": brPrtFinisher,
       "catch-tray": catch_tray,
       "brPrtCatchTray": brPrtCatchTray,
       "pagesetup": pagesetup,
       "pcl": pcl,
       "margin-p": margin_p,
       "brPagePCLLeftMargin": brPagePCLLeftMargin,
       "brPagePCLRightMargin": brPagePCLRightMargin,
       "brPagePCLTopMargin": brPagePCLTopMargin,
       "brPagePCLBottomMargin": brPagePCLBottomMargin,
       "brPagePCLLines": brPagePCLLines,
       "auto-p": auto_p,
       "brPagePCLAutoLF": brPagePCLAutoLF,
       "brPagePCLAutoCR": brPagePCLAutoCR,
       "brPagePCLAutoWrap": brPagePCLAutoWrap,
       "brPagePCLAutoSkip": brPagePCLAutoSkip,
       "ps": ps,
       "brPagePSPrintPSError": brPagePSPrintPSError,
       "brPagePSKeepPCLFonts": brPagePSKeepPCLFonts,
       "brPagePSCAPTsetting": brPagePSCAPTsetting,
       "gl": gl,
       "pen1": pen1,
       "brPageGLPen1Size": brPageGLPen1Size,
       "brPageGLPen1GrayLevel": brPageGLPen1GrayLevel,
       "pen2": pen2,
       "brPageGLPen2Size": brPageGLPen2Size,
       "brPageGLPen2GrayLevel": brPageGLPen2GrayLevel,
       "pen3": pen3,
       "brPageGLPen3Size": brPageGLPen3Size,
       "brPageGLPen3GrayLevel": brPageGLPen3GrayLevel,
       "pen4": pen4,
       "brPageGLPen4Size": brPageGLPen4Size,
       "brPageGLPen4GrayLevel": brPageGLPen4GrayLevel,
       "pen5": pen5,
       "brPageGLPen5Size": brPageGLPen5Size,
       "brPageGLPen5GrayLevel": brPageGLPen5GrayLevel,
       "pen6": pen6,
       "brPageGLPen6Size": brPageGLPen6Size,
       "brPageGLPen6GrayLevel": brPageGLPen6GrayLevel,
       "epson": epson,
       "margin-e": margin_e,
       "brPageEPSONLeftMargin": brPageEPSONLeftMargin,
       "brPageEPSONRightMargin": brPageEPSONRightMargin,
       "brPageEPSONTopMargin": brPageEPSONTopMargin,
       "brPageEPSONBottomMargin": brPageEPSONBottomMargin,
       "brPageEPSONLines": brPageEPSONLines,
       "auto-e": auto_e,
       "brPageEPSONAutoLF": brPageEPSONAutoLF,
       "brPageEPSONAutoMask": brPageEPSONAutoMask,
       "ibm": ibm,
       "margin-i": margin_i,
       "brPageIBMLeftMargin": brPageIBMLeftMargin,
       "brPageIBMRightMargin": brPageIBMRightMargin,
       "brPageIBMTopMargin": brPageIBMTopMargin,
       "brPageIBMBottomMargin": brPageIBMBottomMargin,
       "brPageIBMLines": brPageIBMLines,
       "auto-i": auto_i,
       "brPageIBMAutoLF": brPageIBMAutoLF,
       "brPageIBMAutoCR": brPageIBMAutoCR,
       "brPageIBMAutoMask": brPageIBMAutoMask,
       "fontsetup": fontsetup,
       "brFontName": brFontName,
       "brFontPointSize": brFontPointSize,
       "brFontPitch": brFontPitch,
       "brFontSymbolSet": brFontSymbolSet,
       "controlpanel": controlpanel,
       "reset": reset,
       "brPanelResetUser": brPanelResetUser,
       "brPanelResetFactory": brPanelResetFactory,
       "test": test,
       "brPanelTestConfiguration": brPanelTestConfiguration,
       "brPanelTestFontList": brPanelTestFontList,
       "brPanelTestTestPage": brPanelTestTestPage,
       "brPanelTestDemoPage": brPanelTestDemoPage,
       "panellock": panellock,
       "brPanelLockPasswd": brPanelLockPasswd,
       "brPanelLock": brPanelLock,
       "brPanelLockOn": brPanelLockOn,
       "brPanelLockOff": brPanelLockOff,
       "key": key,
       "brPanelKeyOnline": brPanelKeyOnline,
       "brPanelKeyFormFeed": brPanelKeyFormFeed,
       "brPanelKeyContinue": brPanelKeyContinue,
       "brPanelKeyMode": brPanelKeyMode,
       "brPanelKeyGo": brPanelKeyGo,
       "brPanelKeyJobCancel": brPanelKeyJobCancel,
       "brPanelKeyReprint": brPanelKeyReprint,
       "brPanelKeySecure": brPanelKeySecure,
       "panelinfo": panelinfo,
       "brLCDMode1": brLCDMode1,
       "brLCDString1": brLCDString1,
       "brLCDMode2": brLCDMode2,
       "brLCDString2": brLCDString2,
       "brLCDString16fix": brLCDString16fix,
       "brBackLightColor": brBackLightColor,
       "brLCDMode3": brLCDMode3,
       "brLCDString3": brLCDString3,
       "brLCDMode4": brLCDMode4,
       "brLCDString4": brLCDString4,
       "brLCDMode5": brLCDMode5,
       "brLCDString5": brLCDString5,
       "brLCDContrast": brLCDContrast,
       "printerinfomation": printerinfomation,
       "brInfoSerialNumber": brInfoSerialNumber,
       "brInfoType": brInfoType,
       "version": version,
       "brInfoUpperMIBVer": brInfoUpperMIBVer,
       "brInfoLowerMIBVer": brInfoLowerMIBVer,
       "brInfoStatus": brInfoStatus,
       "brInfoNetVerUpStatus": brInfoNetVerUpStatus,
       "brInfoPrinterUStatus": brInfoPrinterUStatus,
       "brInfoPConSupported": brInfoPConSupported,
       "brInfoMaintenance": brInfoMaintenance,
       "brInfoModelNumber": brInfoModelNumber,
       "brInfoCounter": brInfoCounter,
       "brInfoNextCare": brInfoNextCare,
       "brInfoHDDSlot1": brInfoHDDSlot1,
       "brInfoHDDSlot2": brInfoHDDSlot2,
       "brInfoHDDInternal": brInfoHDDInternal,
       "brInfoHDDSize": brInfoHDDSize,
       "brInfoSolutionsCenterURL": brInfoSolutionsCenterURL,
       "brInfoDeviceRomVersion": brInfoDeviceRomVersion,
       "brInfoCoverage": brInfoCoverage,
       "brInfoEstimatedPagesRemaining": brInfoEstimatedPagesRemaining,
       "brInfoReplaceCount": brInfoReplaceCount,
       "brInfoJamCount": brInfoJamCount,
       "brInfoJamCountClear": brInfoJamCountClear,
       "brInfoReplaceTime": brInfoReplaceTime,
       "brInfoDeviceSubRomVersion": brInfoDeviceSubRomVersion,
       "brInfoAlertVersion": brInfoAlertVersion,
       "brInfoBlackPrint": brInfoBlackPrint,
       "errorHistory": errorHistory,
       "brErrorHistoryCount": brErrorHistoryCount,
       "brErrorHistoryTable": brErrorHistoryTable,
       "brErrorHistoryEntry": brErrorHistoryEntry,
       "brErrorHistoryIndex": brErrorHistoryIndex,
       "brErrorHistoryDescription": brErrorHistoryDescription,
       "brErrorHistoryAllClear": brErrorHistoryAllClear,
       "brCommunicationErrorHistoryCount": brCommunicationErrorHistoryCount,
       "brCommunicationErrorHistoryTable": brCommunicationErrorHistoryTable,
       "brCommunicationErrorHistoryEntry": brCommunicationErrorHistoryEntry,
       "brCommunicationErrorHistoryIndex": brCommunicationErrorHistoryIndex,
       "brCommunicationErrorHistoryDescription": brCommunicationErrorHistoryDescription,
       "printPages": printPages,
       "brPrintPagesTable": brPrintPagesTable,
       "brPrintPagesEntry": brPrintPagesEntry,
       "brPrintPagesIndex": brPrintPagesIndex,
       "brPrintPagesPaperSize": brPrintPagesPaperSize,
       "brPrintPages": brPrintPages,
       "brPrintPagesMediaPlaceTable": brPrintPagesMediaPlaceTable,
       "brPrintPagesMediaPlaceEntry": brPrintPagesMediaPlaceEntry,
       "brPrintPagesMediaPlaceIndex": brPrintPagesMediaPlaceIndex,
       "brPrintPagesMediaPlaceType": brPrintPagesMediaPlaceType,
       "brPrintPagesMediaPlaceCounter": brPrintPagesMediaPlaceCounter,
       "brPrintPagesFuncTable": brPrintPagesFuncTable,
       "brPrintPagesFuncEntry": brPrintPagesFuncEntry,
       "brPrintPagesFuncIndex": brPrintPagesFuncIndex,
       "brPrintPagesFuncType": brPrintPagesFuncType,
       "brPrintPagesFuncCounter": brPrintPagesFuncCounter,
       "brPrintPagesPaperTypeTable": brPrintPagesPaperTypeTable,
       "brPrintPagesPaperTypeEntry": brPrintPagesPaperTypeEntry,
       "brPrintPagesPaperTypeIndex": brPrintPagesPaperTypeIndex,
       "brPrintPagesPaperTypeType": brPrintPagesPaperTypeType,
       "brPrintPagesPaperTypeCounter": brPrintPagesPaperTypeCounter,
       "capability": capability,
       "copies": copies,
       "brCapabilityCopiesMax": brCapabilityCopiesMax,
       "brCapabilityCopiesMin": brCapabilityCopiesMin,
       "orientation": orientation,
       "brCapabilityOrientationCount": brCapabilityOrientationCount,
       "brCapabilityOrientationTable": brCapabilityOrientationTable,
       "brCapabilityOrientationEntry": brCapabilityOrientationEntry,
       "brCapabilityOrientationIndex": brCapabilityOrientationIndex,
       "brCapabilityOrientationName": brCapabilityOrientationName,
       "paper": paper,
       "brCapabilityPaperCount": brCapabilityPaperCount,
       "brCapabilityPaperTable": brCapabilityPaperTable,
       "brCapabilityPaperEntry": brCapabilityPaperEntry,
       "brCapabilityPaperIndex": brCapabilityPaperIndex,
       "brCapabilityPaperName": brCapabilityPaperName,
       "mediatype": mediatype,
       "brCapabilityMediatypeCount": brCapabilityMediatypeCount,
       "brCapabilityMediatypeTable": brCapabilityMediatypeTable,
       "brCapabilityMediatypeEntry": brCapabilityMediatypeEntry,
       "brCapabilityMediatypeIndex": brCapabilityMediatypeIndex,
       "brCapabilityMediatypeName": brCapabilityMediatypeName,
       "resolution": resolution,
       "brCapabilityResolutionCount": brCapabilityResolutionCount,
       "brCapabilityResolutionTable": brCapabilityResolutionTable,
       "brCapabilityResolutionEntry": brCapabilityResolutionEntry,
       "brCapabilityResolutionIndex": brCapabilityResolutionIndex,
       "brCapabilityResolution": brCapabilityResolution,
       "countinfo": countinfo,
       "pfkit": pfkit,
       "brPfKitIndexCount": brPfKitIndexCount,
       "brPfKitTable": brPfKitTable,
       "brPfKitEntry": brPfKitEntry,
       "brPfKitIndex": brPfKitIndex,
       "brPfKitType": brPfKitType,
       "brPfKitCount": brPfKitCount,
       "scancount": scancount,
       "brScanCountIndexCount": brScanCountIndexCount,
       "brScanCountTable": brScanCountTable,
       "brScanCountEntry": brScanCountEntry,
       "brScanCountIndex": brScanCountIndex,
       "brScanCountType": brScanCountType,
       "brScanCountCounter": brScanCountCounter,
       "firmwareupdatekeyword": firmwareupdatekeyword,
       "brFirmwareUpdateKeywordCount": brFirmwareUpdateKeywordCount,
       "brFirmwareUpdateKeywordTable": brFirmwareUpdateKeywordTable,
       "brFirmwareUpdateKeywordEntry": brFirmwareUpdateKeywordEntry,
       "brFirmwareUpdateKeywordIndex": brFirmwareUpdateKeywordIndex,
       "brFirmwareUpdateKeyword": brFirmwareUpdateKeyword,
       "printerstatus": printerstatus,
       "brStatusSleep": brStatusSleep,
       "secret": secret,
       "brSecretMPRetry": brSecretMPRetry,
       "brSecretReprint": brSecretReprint,
       "brFontSetting": brFontSetting,
       "brFontSwitchOn": brFontSwitchOn,
       "brFontSwitchOff": brFontSwitchOff,
       "adminsetting": adminsetting,
       "clockfunction": clockfunction,
       "brClockFuncTimeStyle": brClockFuncTimeStyle,
       "brClockFuncSummerTime": brClockFuncSummerTime,
       "brClockFuncTimeZone": brClockFuncTimeZone,
       "brClockFuncZoneSet": brClockFuncZoneSet,
       "interface": interface,
       "npCard": npCard,
       "npSys": npSys,
       "npConfig": npConfig,
       "brBasicSettingConfigured": brBasicSettingConfigured,
       "adminCapa": adminCapa,
       "brAdminCapability": brAdminCapability,
       "userSetting": userSetting,
       "brUserPasswordVerify": brUserPasswordVerify,
       "brUserPassword": brUserPassword,
       "verify": verify,
       "brpsVerifyPhysAddress": brpsVerifyPhysAddress,
       "npTcp": npTcp,
       "lpd": lpd,
       "banner": banner,
       "brLPDBannerPage": brLPDBannerPage,
       "npCtl": npCtl,
       "etherN": etherN,
       "eNet": eNet,
       "brENetModeSupported": brENetModeSupported,
       "brENetMode": brENetMode,
       "npPort": npPort,
       "funa": funa,
       "brFindPort": brFindPort,
       "brFindTime": brFindTime,
       "npSet": npSet,
       "dns": dns,
       "brDNSSupported": brDNSSupported,
       "brPrimaryDNSIP": brPrimaryDNSIP,
       "brSecondaryDNSIP": brSecondaryDNSIP,
       "brDNSIPSetup": brDNSIPSetup,
       "brTCPIPConnectTime": brTCPIPConnectTime,
       "brAdvancedDNSSupported": brAdvancedDNSSupported,
       "brPrimaryDNSIPAddress": brPrimaryDNSIPAddress,
       "brSecondaryDNSIPAddress": brSecondaryDNSIPAddress,
       "brPOP3ServerName": brPOP3ServerName,
       "brSMTPServerName": brSMTPServerName,
       "pushstatus": pushstatus,
       "brPushStatusSupported": brPushStatusSupported,
       "priadmin": priadmin,
       "brPriMailAddress": brPriMailAddress,
       "brPriError": brPriError,
       "secadmin": secadmin,
       "brSecMailAddress": brSecMailAddress,
       "brSecError": brSecError,
       "brNotificationCount": brNotificationCount,
       "brNotificationTable": brNotificationTable,
       "brNotificationEntry": brNotificationEntry,
       "brNotificationIndex": brNotificationIndex,
       "brNotificationAddress": brNotificationAddress,
       "brNotificationStatusGroup": brNotificationStatusGroup,
       "brNotificationShowURLInfo": brNotificationShowURLInfo,
       "brNotificationErrorRule": brNotificationErrorRule,
       "brNotificationRestoration": brNotificationRestoration,
       "brPrintersEmailaddress": brPrintersEmailaddress,
       "brNotificationVersion": brNotificationVersion,
       "brShowIPAddressInfo": brShowIPAddressInfo,
       "brNotificationRuleTable": brNotificationRuleTable,
       "brNotificationRuleEntry": brNotificationRuleEntry,
       "brNotificationRuleIndex": brNotificationRuleIndex,
       "brNotificationStatusID": brNotificationStatusID,
       "brNotificationMainRule": brNotificationMainRule,
       "brNotificationRuleValue": brNotificationRuleValue,
       "pjl": pjl,
       "pjlinfo": pjlinfo,
       "brPJLInfoOptionsTable": brPJLInfoOptionsTable,
       "brPJLInfoOptionsEntry": brPJLInfoOptionsEntry,
       "brPJLInfoOptionsIndex": brPJLInfoOptionsIndex,
       "brPJLInfoOptions": brPJLInfoOptions,
       "brPJLInfoIntrayconfigTable": brPJLInfoIntrayconfigTable,
       "brPJLInfoIntrayconfigEntry": brPJLInfoIntrayconfigEntry,
       "brPJLInfoIntrayconfigIndex": brPJLInfoIntrayconfigIndex,
       "brPJLInfoIntrayconfig": brPJLInfoIntrayconfig,
       "brPJLInfoOuttrayconfigTable": brPJLInfoOuttrayconfigTable,
       "brPJLInfoOuttrayconfigEntry": brPJLInfoOuttrayconfigEntry,
       "brPJLInfoOuttrayconfigIndex": brPJLInfoOuttrayconfigIndex,
       "brPJLInfoOuttrayconfig": brPJLInfoOuttrayconfig,
       "brPJLInfoDXconfigTable": brPJLInfoDXconfigTable,
       "brPJLInfoDXconfigEntry": brPJLInfoDXconfigEntry,
       "brPJLInfoDXconfigIndex": brPJLInfoDXconfigIndex,
       "brPJLInfoDXconfig": brPJLInfoDXconfig,
       "brPJLInfoStorageconfigTable": brPJLInfoStorageconfigTable,
       "brPJLInfoStorageconfigEntry": brPJLInfoStorageconfigEntry,
       "brPJLInfoStorageconfigIndex": brPJLInfoStorageconfigIndex,
       "brPJLInfoStorageconfig": brPJLInfoStorageconfig,
       "brPJLInfoFirmwareUpdateconfigTable": brPJLInfoFirmwareUpdateconfigTable,
       "brPJLInfoFirmwareUpdateconfigEntry": brPJLInfoFirmwareUpdateconfigEntry,
       "brPJLInfoFirmwareUpdateconfigIndex": brPJLInfoFirmwareUpdateconfigIndex,
       "brPJLInfoFirmwareUpdateconfig": brPJLInfoFirmwareUpdateconfig,
       "eMailReports": eMailReports,
       "brEmailReportsSupported": brEmailReportsSupported,
       "brEmailReportsCount": brEmailReportsCount,
       "brEmailReportsTable": brEmailReportsTable,
       "brEmailReportsEntry": brEmailReportsEntry,
       "brEmailReportsIndex": brEmailReportsIndex,
       "brEmailReportsAddress": brEmailReportsAddress,
       "brEmailReportsFrequency": brEmailReportsFrequency,
       "brEmailReportsTime": brEmailReportsTime,
       "brEmailReportsWeek": brEmailReportsWeek,
       "brEmailReportsDate": brEmailReportsDate,
       "brEmailReportsSendReportNow": brEmailReportsSendReportNow,
       "brEmailReportsSendReportatPowerOn": brEmailReportsSendReportatPowerOn,
       "brEmailReportsNoRTCFrequency": brEmailReportsNoRTCFrequency,
       "brEmailReportsReportFormat": brEmailReportsReportFormat,
       "wireless": wireless,
       "wlInfo": wlInfo,
       "wlCapability": wlCapability,
       "brpsWLanDot11Supported": brpsWLanDot11Supported,
       "brpsWLanAvailableChannel": brpsWLanAvailableChannel,
       "brpsWLanCapabilityEncryptModeCount": brpsWLanCapabilityEncryptModeCount,
       "brpsWLanCapabilityEncryptModeTable": brpsWLanCapabilityEncryptModeTable,
       "brpsWLanCapabilityEncryptModeEntry": brpsWLanCapabilityEncryptModeEntry,
       "brpsWLanCapabilityEncryptModeIndex": brpsWLanCapabilityEncryptModeIndex,
       "brpsWLanCapabilityEncryptModeType": brpsWLanCapabilityEncryptModeType,
       "brpsWLanCapabilityEncryptModeDescription": brpsWLanCapabilityEncryptModeDescription,
       "brpsWLanCapabilityEncryptModeSupported": brpsWLanCapabilityEncryptModeSupported,
       "brpsWLanCapabilityAuthModeCount": brpsWLanCapabilityAuthModeCount,
       "brpsWLanCapabilityAuthModeTable": brpsWLanCapabilityAuthModeTable,
       "brpsWLanCapabilityAuthModeEntry": brpsWLanCapabilityAuthModeEntry,
       "brpsWLanCapabilitAuthModeIndex": brpsWLanCapabilitAuthModeIndex,
       "brpsWLanCapabilityAuthModeType": brpsWLanCapabilityAuthModeType,
       "brpsWLanCapabilityAuthModeDescription": brpsWLanCapabilityAuthModeDescription,
       "brpsWLanCapabilityAuthModeSupported": brpsWLanCapabilityAuthModeSupported,
       "brpsWLanCapabilityAuthEAPCount": brpsWLanCapabilityAuthEAPCount,
       "brpsWLanCapabilityAuthEAPTable": brpsWLanCapabilityAuthEAPTable,
       "brpsWLanCapabilityAuthEAPEntry": brpsWLanCapabilityAuthEAPEntry,
       "brpsWLanCapabilityAuthEAPIndex": brpsWLanCapabilityAuthEAPIndex,
       "brpsWLanCapabilityAuthEAPType": brpsWLanCapabilityAuthEAPType,
       "brpsWLanCapabilityAuthEAPDescription": brpsWLanCapabilityAuthEAPDescription,
       "brpsWLanCapabilityAuthEAPSupported": brpsWLanCapabilityAuthEAPSupported,
       "brpsWLanCapabilityAuthEAPSupportAuthentication": brpsWLanCapabilityAuthEAPSupportAuthentication,
       "brpsWLanCapabilityAuthEAPSupportEncryption": brpsWLanCapabilityAuthEAPSupportEncryption,
       "wlGeneralInfo": wlGeneralInfo,
       "brpsWLanDestination": brpsWLanDestination,
       "brpsWLanTransmitLevel": brpsWLanTransmitLevel,
       "brpsPit3WLanTestStatus": brpsPit3WLanTestStatus,
       "wlNetSearch": wlNetSearch,
       "brpsWLanNetSearchSupported": brpsWLanNetSearchSupported,
       "brpsAvailableWLanScan": brpsAvailableWLanScan,
       "brpsAvailableWLanScanWaitTime": brpsAvailableWLanScanWaitTime,
       "brpsAvailableWLanCount": brpsAvailableWLanCount,
       "brpsAvailableWLanTable": brpsAvailableWLanTable,
       "brpsAvailableWLanEntry": brpsAvailableWLanEntry,
       "brpsAvailableWLanIndex": brpsAvailableWLanIndex,
       "brpsAvailableWLanName": brpsAvailableWLanName,
       "brpsAvailableWLanMode": brpsAvailableWLanMode,
       "brpsAvailableWLanCommMode": brpsAvailableWLanCommMode,
       "brpsAvailableWLanChannel": brpsAvailableWLanChannel,
       "brpsAvailableWLanPowerLevel": brpsAvailableWLanPowerLevel,
       "brpsAvailableWLanAuthMode": brpsAvailableWLanAuthMode,
       "brpsAvailableWLanEncryptMode": brpsAvailableWLanEncryptMode,
       "wlAOSS": wlAOSS,
       "brpsWLanAOSSSupported": brpsWLanAOSSSupported,
       "brpsWLanAOSSIsRunnning": brpsWLanAOSSIsRunnning,
       "wlSES": wlSES,
       "brpsWLanSESSupported": brpsWLanSESSupported,
       "wlWPS": wlWPS,
       "brpsWLanWPSSupported": brpsWLanWPSSupported,
       "brpsWLanWPSResult": brpsWLanWPSResult,
       "wlSimpleWizard": wlSimpleWizard,
       "brWlanSimpleWizardSupported": brWlanSimpleWizardSupported,
       "brWlanSimpleWizardPassword": brWlanSimpleWizardPassword,
       "wlSetup": wlSetup,
       "wlGeneral": wlGeneral,
       "brpsWLanAPSetupMode": brpsWLanAPSetupMode,
       "brpsWLanMode": brpsWLanMode,
       "brpsWLanName": brpsWLanName,
       "brpsWLanCommMode": brpsWLanCommMode,
       "brpsWLanChannel": brpsWLanChannel,
       "wlAdvanced": wlAdvanced,
       "brpsWLanCtsMode": brpsWLanCtsMode,
       "brpsWLanCtsRate": brpsWLanCtsRate,
       "brpsWLanCtsType": brpsWLanCtsType,
       "brpsWLanRtsCtsThreshold": brpsWLanRtsCtsThreshold,
       "brpsWLanLengthThreshold": brpsWLanLengthThreshold,
       "brpsWLanDataRetry": brpsWLanDataRetry,
       "brpsWLanTransmitPowerSetting": brpsWLanTransmitPowerSetting,
       "brpsWLanDeviceType": brpsWLanDeviceType,
       "wlAssociate": wlAssociate,
       "brpsWLanEncryptMode": brpsWLanEncryptMode,
       "brpsWLanAuthMode": brpsWLanAuthMode,
       "brpsWLanAuthEAP": brpsWLanAuthEAP,
       "brpsWLanAuthUserID": brpsWLanAuthUserID,
       "brpsWLanAuthUserPass": brpsWLanAuthUserPass,
       "brpsWLanAssociate": brpsWLanAssociate,
       "brpsWLanAssociateTestResult": brpsWLanAssociateTestResult,
       "brpsWLanAssociateResult": brpsWLanAssociateResult,
       "brpsWLanAssociateTestSupported": brpsWLanAssociateTestSupported,
       "wlWEP": wlWEP,
       "brpsWLanWepKeyDefaultIndex": brpsWLanWepKeyDefaultIndex,
       "brpsWLanWepKeyTable": brpsWLanWepKeyTable,
       "brpsWLanWepKeyEntry": brpsWLanWepKeyEntry,
       "brpsWLanWepKeyIndex": brpsWLanWepKeyIndex,
       "brpsWLanWepKeySize": brpsWLanWepKeySize,
       "brpsWLanWepKeyType": brpsWLanWepKeyType,
       "brpsWLanWepKey": brpsWLanWepKey,
       "wlWPA": wlWPA,
       "brpsWLanNetworkKey": brpsWLanNetworkKey,
       "wlTKIP": wlTKIP,
       "brpsWLanTKIPChangeInterval": brpsWLanTKIPChangeInterval,
       "wlLEAP": wlLEAP,
       "brpsWLanLEAPTimeout": brpsWLanLEAPTimeout,
       "wlStatus": wlStatus,
       "wlGeneralStatus": wlGeneralStatus,
       "brpsWLanOperatingMode": brpsWLanOperatingMode,
       "brpsWLanRSSLevel": brpsWLanRSSLevel,
       "brpsWLanCommSpeed": brpsWLanCommSpeed,
       "brpsWLanOperatingChannel": brpsWLanOperatingChannel,
       "brpsWLanOperatingName": brpsWLanOperatingName,
       "brpsWLanOperatingCommMode": brpsWLanOperatingCommMode,
       "brpsWLanOperatingEncryptMode": brpsWLanOperatingEncryptMode,
       "brpsWLanOperatingAuthMode": brpsWLanOperatingAuthMode,
       "brpsWLanOperatingWepKeyDefaultIndex": brpsWLanOperatingWepKeyDefaultIndex,
       "brnetConfig": brnetConfig,
       "brconfig": brconfig,
       "brpsNodeName": brpsNodeName,
       "brpsSerialNumber": brpsSerialNumber,
       "brpsHardwareType": brpsHardwareType,
       "brpsMainRevision": brpsMainRevision,
       "brpsBootRevision": brpsBootRevision,
       "brpsPasswordVerify": brpsPasswordVerify,
       "brpsPassword": brpsPassword,
       "brpsMIBVersion": brpsMIBVersion,
       "brpsOEMString": brpsOEMString,
       "brpsMIBMajor": brpsMIBMajor,
       "brpsMIBMinor": brpsMIBMinor,
       "brpsServerDescription": brpsServerDescription,
       "brpsEnetMode": brpsEnetMode,
       "brpsFlashROMSize": brpsFlashROMSize,
       "brpsSNMPGetCommunity": brpsSNMPGetCommunity,
       "brpsSNMPJetAdmin": brpsSNMPJetAdmin,
       "brpsSNMPSetCommunity1": brpsSNMPSetCommunity1,
       "brpsSNMPSetCommunity2": brpsSNMPSetCommunity2,
       "brSupportedInfo": brSupportedInfo,
       "brcontrol": brcontrol,
       "brpsTestPage": brpsTestPage,
       "brpsSetDefault": brpsSetDefault,
       "brpsReset": brpsReset,
       "brpsProtectModeEnable": brpsProtectModeEnable,
       "brpsProtectPassword": brpsProtectPassword,
       "brport": brport,
       "brpsPortCount": brpsPortCount,
       "brpsPortInfoTable": brpsPortInfoTable,
       "brpsPortInfoEntry": brpsPortInfoEntry,
       "brpsPortIndex": brpsPortIndex,
       "brpsPortName": brpsPortName,
       "brpsPortType": brpsPortType,
       "brpsPortStatus": brpsPortStatus,
       "brpsPortStatusString": brpsPortStatusString,
       "brpsPortProtocol": brpsPortProtocol,
       "brpsPortQueueSize": brpsPortQueueSize,
       "brpsPortDescriptionString": brpsPortDescriptionString,
       "brpsPortInfoString": brpsPortInfoString,
       "brpsPortHTTPExtensions": brpsPortHTTPExtensions,
       "brpsPortSNMPExtensions": brpsPortSNMPExtensions,
       "brpsPortAttribute": brpsPortAttribute,
       "brpsPortBinaryMode": brpsPortBinaryMode,
       "brpsPortInhibitDatagramSupport": brpsPortInhibitDatagramSupport,
       "brservice": brservice,
       "brpsServiceCount": brpsServiceCount,
       "brpsServiceInfoTable": brpsServiceInfoTable,
       "brpsServiceInfoEntry": brpsServiceInfoEntry,
       "brpsServiceIndex": brpsServiceIndex,
       "brpsServiceName": brpsServiceName,
       "brpsServicePort": brpsServicePort,
       "brpsServiceFilter": brpsServiceFilter,
       "brpsServiceBOT": brpsServiceBOT,
       "brpsServiceEOT": brpsServiceEOT,
       "brpsServiceMatch": brpsServiceMatch,
       "brpsServiceReplace": brpsServiceReplace,
       "brpsServiceTCPPort": brpsServiceTCPPort,
       "brpsServiceNDSTree": brpsServiceNDSTree,
       "brpsServiceNDSContext": brpsServiceNDSContext,
       "brpsServiceVines": brpsServiceVines,
       "brpsServiceObsolete": brpsServiceObsolete,
       "brpsServiceNetwareServerCount": brpsServiceNetwareServerCount,
       "brpsServiceReceiveOnly": brpsServiceReceiveOnly,
       "brpsServiceTCPQueued": brpsServiceTCPQueued,
       "brpsServiceProtocolLAT": brpsServiceProtocolLAT,
       "brpsServiceProtocolTCPIP": brpsServiceProtocolTCPIP,
       "brpsServiceProtocolNetware": brpsServiceProtocolNetware,
       "brpsServiceProtocolAppleTalk": brpsServiceProtocolAppleTalk,
       "brpsServiceProtocolBanyan": brpsServiceProtocolBanyan,
       "brpsServiceProtocolDLC": brpsServiceProtocolDLC,
       "brpsServiceProtocolNetBEUI": brpsServiceProtocolNetBEUI,
       "brpsServiceNetwareServerMode": brpsServiceNetwareServerMode,
       "brpsServiceNetwareRemotePrinterNum": brpsServiceNetwareRemotePrinterNum,
       "brpsServiceProtocolIPP": brpsServiceProtocolIPP,
       "brpsServiceAppleTalkType": brpsServiceAppleTalkType,
       "brpsServiceStringLimit": brpsServiceStringLimit,
       "brpsServiceStringInfoTable": brpsServiceStringInfoTable,
       "brpsServiceStringInfoEntry": brpsServiceStringInfoEntry,
       "brpsServiceStringIndex": brpsServiceStringIndex,
       "brpsServiceString": brpsServiceString,
       "brpsServiceStringCount": brpsServiceStringCount,
       "brpsServiceFilterCount": brpsServiceFilterCount,
       "brprotocol": brprotocol,
       "brlat": brlat,
       "brpsLATSupported": brpsLATSupported,
       "brpsLATEnable": brpsLATEnable,
       "brpsLATCircuitTimer": brpsLATCircuitTimer,
       "brpsLATKeepAliveTimer": brpsLATKeepAliveTimer,
       "brpsLATReceiveBufferMax": brpsLATReceiveBufferMax,
       "brpsLATTransmitBufferMax": brpsLATTransmitBufferMax,
       "brpsLATTimeout": brpsLATTimeout,
       "brpsLATGroup": brpsLATGroup,
       "brtcpip": brtcpip,
       "brpsTCPIPSupported": brpsTCPIPSupported,
       "brpsTCPIPEnable": brpsTCPIPEnable,
       "brpsTCPIPAddress": brpsTCPIPAddress,
       "brpsTCPIPSubnetMask": brpsTCPIPSubnetMask,
       "brpsTCPIPGateway": brpsTCPIPGateway,
       "brpsTCPIPMethod": brpsTCPIPMethod,
       "brpsTCPIPTimeout": brpsTCPIPTimeout,
       "brpsTCPIPBootTries": brpsTCPIPBootTries,
       "brpsTCPIPMaxWindow": brpsTCPIPMaxWindow,
       "brpsTCPIPRARPNoSubnet": brpsTCPIPRARPNoSubnet,
       "brpsTCPIPRARPNoGateway": brpsTCPIPRARPNoGateway,
       "brpsTCPIPUpdate": brpsTCPIPUpdate,
       "brpsTCPIPBanner": brpsTCPIPBanner,
       "brpsTCPIPFastTimeoutEnable": brpsTCPIPFastTimeoutEnable,
       "brpsTCPIPLPRRetryEnable": brpsTCPIPLPRRetryEnable,
       "brpsTCPIPUseMethod": brpsTCPIPUseMethod,
       "brpsTCPIPMethodServer": brpsTCPIPMethodServer,
       "brpsTCPIPAccessTable": brpsTCPIPAccessTable,
       "brpsTCPIPAccessEntry": brpsTCPIPAccessEntry,
       "brpsTCPIPAccessIndex": brpsTCPIPAccessIndex,
       "brpsTCPIPAccessNodeAddress": brpsTCPIPAccessNodeAddress,
       "brpsTCPIPAccessSubnetMask": brpsTCPIPAccessSubnetMask,
       "brpsAdvancedTCPIPAccessSupported": brpsAdvancedTCPIPAccessSupported,
       "brpsAdvancedTCPIPAccessEnable": brpsAdvancedTCPIPAccessEnable,
       "brpsAdvancedTCPIPAccessAdministratorIPAddress": brpsAdvancedTCPIPAccessAdministratorIPAddress,
       "brpsAdvancedTCPIPAccessSetting": brpsAdvancedTCPIPAccessSetting,
       "brnetware": brnetware,
       "brpsNetwareSupported": brpsNetwareSupported,
       "brpsNetwareEnable": brpsNetwareEnable,
       "brpsNetwareFrameType": brpsNetwareFrameType,
       "brpsNetwarePollFreq": brpsNetwarePollFreq,
       "brpsNetwareAdvFreq": brpsNetwareAdvFreq,
       "brpsNetwarePassword": brpsNetwarePassword,
       "brpsNetwareRestart": brpsNetwareRestart,
       "brpsNetwareServerTable": brpsNetwareServerTable,
       "brpsNetwareServerEntry": brpsNetwareServerEntry,
       "brpsNetwareServerIndex": brpsNetwareServerIndex,
       "brpsNetwareServerName": brpsNetwareServerName,
       "brpsNetwarePasswordSet": brpsNetwarePasswordSet,
       "brpsNDSSupported": brpsNDSSupported,
       "brpsNetwareEtherIINetInfo": brpsNetwareEtherIINetInfo,
       "brpsNetwareEtherIICount": brpsNetwareEtherIICount,
       "brpsNetware8022NetInfo": brpsNetware8022NetInfo,
       "brpsNetware8022Count": brpsNetware8022Count,
       "brpsNetware8023NetInfo": brpsNetware8023NetInfo,
       "brpsNetware8023Count": brpsNetware8023Count,
       "brpsNetwareSNAPNetInfo": brpsNetwareSNAPNetInfo,
       "brpsNetwareSNAPCount": brpsNetwareSNAPCount,
       "brpsNetwareServicingServerName": brpsNetwareServicingServerName,
       "brpsNetwareServicingQueueName": brpsNetwareServicingQueueName,
       "brpsNetwareServicingServerCount": brpsNetwareServicingServerCount,
       "brpsNetwareServicingQueueCount": brpsNetwareServicingQueueCount,
       "brpsNetwarePrintJob": brpsNetwarePrintJob,
       "brappletalk": brappletalk,
       "brpsAppleTalkSupported": brpsAppleTalkSupported,
       "brpsAppleTalkEnable": brpsAppleTalkEnable,
       "brpsAppleTalkZone": brpsAppleTalkZone,
       "brpsAppleTalkPrintJob": brpsAppleTalkPrintJob,
       "brpsAppleTalkReadByte": brpsAppleTalkReadByte,
       "brpsAppleTalkWriteByte": brpsAppleTalkWriteByte,
       "brpsAppleTalkReadError": brpsAppleTalkReadError,
       "brpsAppleTalkWriteError": brpsAppleTalkWriteError,
       "brbanyan": brbanyan,
       "brpsBanyanSupported": brpsBanyanSupported,
       "brpsBanyanEnable": brpsBanyanEnable,
       "brpsBanyanLoginName": brpsBanyanLoginName,
       "brpsBanyanPassword": brpsBanyanPassword,
       "brpsBanyanHopCount": brpsBanyanHopCount,
       "brpsBanyanTimeout": brpsBanyanTimeout,
       "brpsBanyanPasswordSet": brpsBanyanPasswordSet,
       "brpsBanyanIPNetworkID1": brpsBanyanIPNetworkID1,
       "brpsBanyanIPNetworkID2": brpsBanyanIPNetworkID2,
       "brpsBanyanRouter1": brpsBanyanRouter1,
       "brpsBanyanRouter2": brpsBanyanRouter2,
       "brpsBanyanIPPacket": brpsBanyanIPPacket,
       "brpsBanyanErrorCS": brpsBanyanErrorCS,
       "brpsBanyanErrorPT": brpsBanyanErrorPT,
       "brpsBanyanErrorLE": brpsBanyanErrorLE,
       "brpsBanyanPrintServerStatus": brpsBanyanPrintServerStatus,
       "brpsBanyanServerAddress1": brpsBanyanServerAddress1,
       "brpsBanyanServerAddress2": brpsBanyanServerAddress2,
       "brpsBanyanIPCConnectionInformation": brpsBanyanIPCConnectionInformation,
       "brpsBanyanIPCSequenceError": brpsBanyanIPCSequenceError,
       "brpsBanyanIPCListen": brpsBanyanIPCListen,
       "brpsBanyanSPPConnectionInformation": brpsBanyanSPPConnectionInformation,
       "brpsBanyanSPPSequenceError": brpsBanyanSPPSequenceError,
       "brpsBanyanSPPListen": brpsBanyanSPPListen,
       "bremail": bremail,
       "brpsEmailSupported": brpsEmailSupported,
       "brpsEmailEnable": brpsEmailEnable,
       "brpsPOP3Address": brpsPOP3Address,
       "brpsSMTPAddress": brpsSMTPAddress,
       "brpsPOP3Name": brpsPOP3Name,
       "brpsPOP3Password": brpsPOP3Password,
       "brpsPOP3PollFreq": brpsPOP3PollFreq,
       "brpsPOP3Timeout": brpsPOP3Timeout,
       "brpsPOP3PasswordSet": brpsPOP3PasswordSet,
       "brpsPOP3TotalMessage": brpsPOP3TotalMessage,
       "brpsPOP3TotalConnect": brpsPOP3TotalConnect,
       "brpsPOP3TotalConnectFailure": brpsPOP3TotalConnectFailure,
       "brpsPOP3TotalConnectionLost": brpsPOP3TotalConnectionLost,
       "brpsPOP3TotalUserFailure": brpsPOP3TotalUserFailure,
       "brpsPOP3TotalPasswordFailure": brpsPOP3TotalPasswordFailure,
       "brpsPOP3TotalIOError": brpsPOP3TotalIOError,
       "brpsSMTPTotalMessage": brpsSMTPTotalMessage,
       "brpsSMTPTotalConnect": brpsSMTPTotalConnect,
       "brpsSMTPTotalConnectFailure": brpsSMTPTotalConnectFailure,
       "brpsSMTPTotalRecvFromFailure": brpsSMTPTotalRecvFromFailure,
       "brpsSMTPTotalSendToFailure": brpsSMTPTotalSendToFailure,
       "brpsPOP3Supported": brpsPOP3Supported,
       "brpsSMTPServerAuthMethod": brpsSMTPServerAuthMethod,
       "brpsSMTPAUTHUsername": brpsSMTPAUTHUsername,
       "brpsSMTPAUTHPassword": brpsSMTPAUTHPassword,
       "brpsSMTPAUTHPasswordSet": brpsSMTPAUTHPasswordSet,
       "brpsSmtpAUTHTimeout": brpsSmtpAUTHTimeout,
       "brpsPOPbeforeSMTPWait": brpsPOPbeforeSMTPWait,
       "brpsAPOPEnable": brpsAPOPEnable,
       "brpsSMTPEnhancedAuthSupported": brpsSMTPEnhancedAuthSupported,
       "brpsAPOPSupported": brpsAPOPSupported,
       "brpsEmailSendTestSupported": brpsEmailSendTestSupported,
       "brpsEmailRecvTestSupported": brpsEmailRecvTestSupported,
       "brpsChangeSMTPPortSupported": brpsChangeSMTPPortSupported,
       "brpsSMTPPortNumber": brpsSMTPPortNumber,
       "brpsChangePOP3PortSupported": brpsChangePOP3PortSupported,
       "brpsPOP3PortNumber": brpsPOP3PortNumber,
       "brpsTmpSMTPServerName": brpsTmpSMTPServerName,
       "brpsTmpSMTPServerAuthMethod": brpsTmpSMTPServerAuthMethod,
       "brpsTmpSMTPAUTHUsername": brpsTmpSMTPAUTHUsername,
       "brpsTmpSMTPAUTHPassword": brpsTmpSMTPAUTHPassword,
       "brpsTmpPOP3ServerName": brpsTmpPOP3ServerName,
       "brpsTmpPOP3Name": brpsTmpPOP3Name,
       "brpsTmpPOP3Password": brpsTmpPOP3Password,
       "brpsTmpPrintersEmailaddress": brpsTmpPrintersEmailaddress,
       "brpsTmpAPOPEnable": brpsTmpAPOPEnable,
       "brpsTmpSMTPAUTHPasswordModified": brpsTmpSMTPAUTHPasswordModified,
       "brpsTmpPOP3PasswordModified": brpsTmpPOP3PasswordModified,
       "brpsTmpSMTPPortNumber": brpsTmpSMTPPortNumber,
       "brpsTmpPOP3PortNumber": brpsTmpPOP3PortNumber,
       "brpsEmailSendTestMail": brpsEmailSendTestMail,
       "brpsEmailTestDestinationAddress": brpsEmailTestDestinationAddress,
       "brpsEmailSendTestCall": brpsEmailSendTestCall,
       "brpsEmailRecvTestCall": brpsEmailRecvTestCall,
       "brpsEmailSendRecvTestCall": brpsEmailSendRecvTestCall,
       "brpsEmailTestResult": brpsEmailTestResult,
       "brpsPOP3TotalAPOPFailure": brpsPOP3TotalAPOPFailure,
       "brdlc": brdlc,
       "brpsDLCSupported": brpsDLCSupported,
       "brpsDLCEnable": brpsDLCEnable,
       "brpsDLCPrintStatus": brpsDLCPrintStatus,
       "brpsDLCLLCState": brpsDLCLLCState,
       "brpsDLCLLCConnectHost": brpsDLCLLCConnectHost,
       "brpsDLCLLCLastIFrame": brpsDLCLLCLastIFrame,
       "brpsDLCLLCRecvPacket": brpsDLCLLCRecvPacket,
       "brpsDLCLLCPortStatus": brpsDLCLLCPortStatus,
       "brnetbeui": brnetbeui,
       "brpsNetBEUISupported": brpsNetBEUISupported,
       "brpsNetBEUIEnable": brpsNetBEUIEnable,
       "brpsNetBEUIDomain": brpsNetBEUIDomain,
       "brpsNetBIOSIPSupported": brpsNetBIOSIPSupported,
       "brpsNetBIOSIPEnable": brpsNetBIOSIPEnable,
       "brpsNetBIOSIPMethod": brpsNetBIOSIPMethod,
       "brpsNetBIOSPrimaryWINSAddr": brpsNetBIOSPrimaryWINSAddr,
       "brpsNetBIOSSecondaryWINSAddr": brpsNetBIOSSecondaryWINSAddr,
       "brpsNetBIOSPrintingSupported": brpsNetBIOSPrintingSupported,
       "bripp": bripp,
       "brpsIPPSupported": brpsIPPSupported,
       "brpsIPPEnable": brpsIPPEnable,
       "brIPPRegularPortEnable": brIPPRegularPortEnable,
       "brIPPSSLPortEnable": brIPPSSLPortEnable,
       "brIPPOriginalPortEnable": brIPPOriginalPortEnable,
       "brntsend": brntsend,
       "brpsNtSendSupported": brpsNtSendSupported,
       "brpsNtSendEnable": brpsNtSendEnable,
       "brfirmware": brfirmware,
       "brpsFirmwareIPAddress": brpsFirmwareIPAddress,
       "brpsFirmwareHost": brpsFirmwareHost,
       "brpsFirmwareFile": brpsFirmwareFile,
       "brpsFirmwareReload": brpsFirmwareReload,
       "brpsFirmwareDescription": brpsFirmwareDescription,
       "brpsFirmwareXModem": brpsFirmwareXModem,
       "brpsFirmwareAdvancedAddressSupported": brpsFirmwareAdvancedAddressSupported,
       "brpsFirmwareAdvancedAddress": brpsFirmwareAdvancedAddress,
       "brnetConfigOpt": brnetConfigOpt,
       "broriginalprotocol": broriginalprotocol,
       "broriginaltcpip": broriginaltcpip,
       "brLPDType": brLPDType,
       "broriginalftp": broriginalftp,
       "brFTPSupported": brFTPSupported,
       "brFTPEnable": brFTPEnable,
       "broriginalupnp": broriginalupnp,
       "brUPnPSupported": brUPnPSupported,
       "brUPnPEnable": brUPnPEnable,
       "broriginalapipa": broriginalapipa,
       "brAPIPASupported": brAPIPASupported,
       "brAPIPAEnable": brAPIPAEnable,
       "broriginalmdns": broriginalmdns,
       "brmDNSSupported": brmDNSSupported,
       "brmDNSEnable": brmDNSEnable,
       "brmDNSPrinterName": brmDNSPrinterName,
       "broriginalLAA": broriginalLAA,
       "brLAASupported": brLAASupported,
       "brLAAMacAddress": brLAAMacAddress,
       "broriginalIPv6": broriginalIPv6,
       "brIPv6Supported": brIPv6Supported,
       "brIPv6Enable": brIPv6Enable,
       "brIPv6Priority": brIPv6Priority,
       "broriginaltelnet": broriginaltelnet,
       "brtelnetSupported": brtelnetSupported,
       "brtelnetEnable": brtelnetEnable,
       "broriginalEWS": broriginalEWS,
       "brEWSSupported": brEWSSupported,
       "brEWSEnable": brEWSEnable,
       "brEWSRegularPortEnable": brEWSRegularPortEnable,
       "brEWSSSLPortEnable": brEWSSSLPortEnable,
       "broriginalSNMP": broriginalSNMP,
       "brSNMPSupported": brSNMPSupported,
       "brSNMPEnable": brSNMPEnable,
       "brSNMPV3Supported": brSNMPV3Supported,
       "brSNMPCommMode": brSNMPCommMode,
       "brSNMPV3UserName": brSNMPV3UserName,
       "brSNMPV3KeyType": brSNMPV3KeyType,
       "brSNMPV3AuthKey": brSNMPV3AuthKey,
       "brSNMPV3AuthPassword": brSNMPV3AuthPassword,
       "brSNMPV3PrivKey": brSNMPV3PrivKey,
       "brSNMPV3PrivPassword": brSNMPV3PrivPassword,
       "brSNMPV3ContextName": brSNMPV3ContextName,
       "broriginalldap": broriginalldap,
       "brLdapSupported": brLdapSupported,
       "brLdapEnable": brLdapEnable,
       "brLdapTimeout": brLdapTimeout,
       "brLdapTimeoutSupported": brLdapTimeoutSupported,
       "brLdapServerCount": brLdapServerCount,
       "brLdapServerInfoTable": brLdapServerInfoTable,
       "brLdapServerInfoEntry": brLdapServerInfoEntry,
       "brLdapServerInfoIndex": brLdapServerInfoIndex,
       "brLdapServerName": brLdapServerName,
       "brLdapServerPort": brLdapServerPort,
       "brLdapServerAuth": brLdapServerAuth,
       "brLdapServerUserDN": brLdapServerUserDN,
       "brLdapServerPassword": brLdapServerPassword,
       "brLdapServerPasswordSet": brLdapServerPasswordSet,
       "brLdapServerBaseDN": brLdapServerBaseDN,
       "brLdapServerAttrEMail": brLdapServerAttrEMail,
       "brLdapServerAttrFAXNumber": brLdapServerAttrFAXNumber,
       "brLdapServerAttrDetail1": brLdapServerAttrDetail1,
       "brLdapServerAttrDetail2": brLdapServerAttrDetail2,
       "brLdapServerAttrDetail3": brLdapServerAttrDetail3,
       "brLdapServerAttrDetail4": brLdapServerAttrDetail4,
       "brLdapServerAttrDetailEnable1": brLdapServerAttrDetailEnable1,
       "brLdapServerAttrDetailEnable2": brLdapServerAttrDetailEnable2,
       "brLdapServerAttrDetailEnable3": brLdapServerAttrDetailEnable3,
       "brLdapServerAttrDetailEnable4": brLdapServerAttrDetailEnable4,
       "brLdapKerberosServerName": brLdapKerberosServerName,
       "brLdapKerberosServerPort": brLdapKerberosServerPort,
       "brLdapServerAttrNameCount": brLdapServerAttrNameCount,
       "brLdapServerAttrNameTable": brLdapServerAttrNameTable,
       "brLdapServerAttrNameEntry": brLdapServerAttrNameEntry,
       "brLdapServerAttrNameIndex": brLdapServerAttrNameIndex,
       "brLdapServerAttrName": brLdapServerAttrName,
       "brLdapSetDefault": brLdapSetDefault,
       "broriginalTFTP": broriginalTFTP,
       "brTFTPSupported": brTFTPSupported,
       "brTFTPEnable": brTFTPEnable,
       "broriginalHTTPS": broriginalHTTPS,
       "brHTTPSSupported": brHTTPSSupported,
       "brHTTPSEnable": brHTTPSEnable,
       "broriginalLPD": broriginalLPD,
       "brLPDSupported": brLPDSupported,
       "brLPDEnable": brLPDEnable,
       "broriginalRawPort": broriginalRawPort,
       "brRawPortSupported": brRawPortSupported,
       "brRawPortEnable": brRawPortEnable,
       "broriginalLLTD": broriginalLLTD,
       "brLLTDSupported": brLLTDSupported,
       "brLLTDEnable": brLLTDEnable,
       "broriginalWebServices": broriginalWebServices,
       "brWebServicesSupported": brWebServicesSupported,
       "brWebServicesEnable": brWebServicesEnable,
       "brWebServicesRegularPortEnable": brWebServicesRegularPortEnable,
       "brWebServicesSSLPortEnable": brWebServicesSSLPortEnable,
       "broriginalLLMNR": broriginalLLMNR,
       "brLLMNREnable": brLLMNREnable,
       "broriginalKerberos": broriginalKerberos,
       "brKerberosSupported": brKerberosSupported,
       "broriginalCIFS": broriginalCIFS,
       "brCIFSSupported": brCIFSSupported,
       "brCIFSEnable": brCIFSEnable,
       "broriginalSNTP": broriginalSNTP,
       "brSNTPCSupported": brSNTPCSupported,
       "brSNTPCEnable": brSNTPCEnable,
       "brSNTPCServerMethod": brSNTPCServerMethod,
       "brSNTPCSyncMethod": brSNTPCSyncMethod,
       "brSNTPCIntervalMin": brSNTPCIntervalMin,
       "brSNTPCInterval": brSNTPCInterval,
       "brSNTPCSyncResult": brSNTPCSyncResult,
       "brSNTPCPrimaryServerName": brSNTPCPrimaryServerName,
       "brSNTPCPrimaryServerPort": brSNTPCPrimaryServerPort,
       "brSNTPCSecondaryServerName": brSNTPCSecondaryServerName,
       "brSNTPCSecondaryServerPort": brSNTPCSecondaryServerPort,
       "broriginalSecurity": broriginalSecurity,
       "brSecurityGeneralStatus": brSecurityGeneralStatus,
       "brDeviceNegotiationEncryptVer": brDeviceNegotiationEncryptVer,
       "brpsServerCertificateNum": brpsServerCertificateNum,
       "brSecurityGeneralSetup": brSecurityGeneralSetup,
       "brSecurityDeviceNegotiation": brSecurityDeviceNegotiation,
       "brDeviceNegotiationGetChallenge": brDeviceNegotiationGetChallenge,
       "brDeviceNegotiationConfirmPassword": brDeviceNegotiationConfirmPassword,
       "brDeviceNegotiationChangePassword": brDeviceNegotiationChangePassword,
       "broriginalinternetsetting": broriginalinternetsetting,
       "broriginalproxy": broriginalproxy,
       "brProxySupported": brProxySupported,
       "brProxyEnable": brProxyEnable,
       "brProxyBypassServer": brProxyBypassServer,
       "brProxyServerCount": brProxyServerCount,
       "brProxyServerInfoTable": brProxyServerInfoTable,
       "brProxyServerInfoEntry": brProxyServerInfoEntry,
       "brProxyServerInfoIndex": brProxyServerInfoIndex,
       "brProxyServerType": brProxyServerType,
       "brProxyServerName": brProxyServerName,
       "brProxyServerPort": brProxyServerPort,
       "broriginalOtherSetting": broriginalOtherSetting,
       "broriginalJobTermination": broriginalJobTermination,
       "brJobTerminationSupported": brJobTerminationSupported,
       "brJobTerminationEnable": brJobTerminationEnable,
       "broriginalSNMPTrap": broriginalSNMPTrap,
       "brSNMPTrapTable": brSNMPTrapTable,
       "brSNMPTrapEntry": brSNMPTrapEntry,
       "brSNMPTrapIndex": brSNMPTrapIndex,
       "brTCPIPServerAddress": brTCPIPServerAddress,
       "broriginalLegacy": broriginalLegacy,
       "brLegacyCompatible": brLegacyCompatible,
       "npMultiCards": npMultiCards,
       "npMultiIFSet": npMultiIFSet,
       "brMultiIFdns": brMultiIFdns,
       "brMultiIFDNSTable": brMultiIFDNSTable,
       "brMultiIFDNSEntry": brMultiIFDNSEntry,
       "brMultiIFTCPIPDNSIPSetup": brMultiIFTCPIPDNSIPSetup,
       "brMultiIFPrimaryDNSIPAddress": brMultiIFPrimaryDNSIPAddress,
       "brMultiIFSecondaryDNSIPAddress": brMultiIFSecondaryDNSIPAddress,
       "brMultiIFTCPIPConnectTime": brMultiIFTCPIPConnectTime,
       "brnetMultiIFConfig": brnetMultiIFConfig,
       "brMultiIFconfig": brMultiIFconfig,
       "brMultiIFSupported": brMultiIFSupported,
       "brMultiIFActiveIF": brMultiIFActiveIF,
       "brMultiIFAllSetDefault": brMultiIFAllSetDefault,
       "brMultiIFCount": brMultiIFCount,
       "brMultiIFConfigureTable": brMultiIFConfigureTable,
       "brMultiIFConfigureEntry": brMultiIFConfigureEntry,
       "brMultiIFConfigureIndex": brMultiIFConfigureIndex,
       "brMultiIFType": brMultiIFType,
       "brMultiIFDescription": brMultiIFDescription,
       "brMultiIFNodeName": brMultiIFNodeName,
       "brMultiIFInterfaceEnable": brMultiIFInterfaceEnable,
       "brMultiIFEnetMode": brMultiIFEnetMode,
       "brMultiIFHardwareType": brMultiIFHardwareType,
       "brMultiIFNodeType": brMultiIFNodeType,
       "brMultiIFInterfaceEnableImmediate": brMultiIFInterfaceEnableImmediate,
       "brMultiIFPrimaryInterface": brMultiIFPrimaryInterface,
       "brMultiIFInterfaceInformation": brMultiIFInterfaceInformation,
       "brMultiIFcontrol": brMultiIFcontrol,
       "brMultiIFControlTable": brMultiIFControlTable,
       "brMultiIFControlEntry": brMultiIFControlEntry,
       "brMultiIFSetDefault": brMultiIFSetDefault,
       "brMultiIFservice": brMultiIFservice,
       "brMultiIFServiceTable": brMultiIFServiceTable,
       "brMultiIFServiceEntry": brMultiIFServiceEntry,
       "brMultiIFServiceCount": brMultiIFServiceCount,
       "brMultiIFServiceStringLimit": brMultiIFServiceStringLimit,
       "brMultiIFServiceStringCount": brMultiIFServiceStringCount,
       "brMultiIFServiceFilterCount": brMultiIFServiceFilterCount,
       "brMultiIFServiceInfoTable": brMultiIFServiceInfoTable,
       "brMultiIFServiceInfoEntry": brMultiIFServiceInfoEntry,
       "brMultiIFServiceIndex": brMultiIFServiceIndex,
       "brMultiIFServiceName": brMultiIFServiceName,
       "brMultiIFServicePort": brMultiIFServicePort,
       "brMultiIFServiceFilter": brMultiIFServiceFilter,
       "brMultiIFServiceBOT": brMultiIFServiceBOT,
       "brMultiIFServiceEOT": brMultiIFServiceEOT,
       "brMultiIFServiceMatch": brMultiIFServiceMatch,
       "brMultiIFServiceReplace": brMultiIFServiceReplace,
       "brMultiIFServiceTCPPort": brMultiIFServiceTCPPort,
       "brMultiIFServiceNDSTree": brMultiIFServiceNDSTree,
       "brMultiIFServiceNDSContext": brMultiIFServiceNDSContext,
       "brMultiIFServiceVines": brMultiIFServiceVines,
       "brMultiIFServiceObsolete": brMultiIFServiceObsolete,
       "brMultiIFServiceNetwareServerCount": brMultiIFServiceNetwareServerCount,
       "brMultiIFServiceReceiveOnly": brMultiIFServiceReceiveOnly,
       "brMultiIFServiceTCPQueued": brMultiIFServiceTCPQueued,
       "brMultiIFServiceProtocolLAT": brMultiIFServiceProtocolLAT,
       "brMultiIFServiceProtocolTCPIP": brMultiIFServiceProtocolTCPIP,
       "brMultiIFServiceProtocolNetware": brMultiIFServiceProtocolNetware,
       "brMultiIFServiceProtocolAppleTalk": brMultiIFServiceProtocolAppleTalk,
       "brMultiIFServiceProtocolBanyan": brMultiIFServiceProtocolBanyan,
       "brMultiIFServiceProtocolDLC": brMultiIFServiceProtocolDLC,
       "brMultiIFServiceProtocolNetBEUI": brMultiIFServiceProtocolNetBEUI,
       "brMultiIFServiceNetwareServerMode": brMultiIFServiceNetwareServerMode,
       "brMultiIFServiceNetwareRemotePrinterNum": brMultiIFServiceNetwareRemotePrinterNum,
       "brMultiIFServiceProtocolIPP": brMultiIFServiceProtocolIPP,
       "brMultiIFServiceAppleTalkType": brMultiIFServiceAppleTalkType,
       "brMultiIFServiceStringInfoTable": brMultiIFServiceStringInfoTable,
       "brMultiIFServiceStringInfoEntry": brMultiIFServiceStringInfoEntry,
       "brMultiIFServiceStringIndex": brMultiIFServiceStringIndex,
       "brMultiIFServiceString": brMultiIFServiceString,
       "brMultiIFprotocol": brMultiIFprotocol,
       "brMultiIFtcpip": brMultiIFtcpip,
       "brMultiIFTCPIPTable": brMultiIFTCPIPTable,
       "brMultiIFTCPIPEntry": brMultiIFTCPIPEntry,
       "brMultiIFTCPIPAddress": brMultiIFTCPIPAddress,
       "brMultiIFTCPIPSubnetMask": brMultiIFTCPIPSubnetMask,
       "brMultiIFTCPIPGateway": brMultiIFTCPIPGateway,
       "brMultiIFTCPIPMethod": brMultiIFTCPIPMethod,
       "brMultiIFTCPIPUpdate": brMultiIFTCPIPUpdate,
       "brMultiIFTCPIPTimeout": brMultiIFTCPIPTimeout,
       "brMultiIFTCPIPBootTries": brMultiIFTCPIPBootTries,
       "brMultiIFTCPIPRARPNoSubnet": brMultiIFTCPIPRARPNoSubnet,
       "brMultiIFTCPIPRARPNoGateway": brMultiIFTCPIPRARPNoGateway,
       "brMultiIFTCPIPUseMethod": brMultiIFTCPIPUseMethod,
       "brMultiIFTCPIPMethodServer": brMultiIFTCPIPMethodServer,
       "brMultiIFnetbeui": brMultiIFnetbeui,
       "brMultiIFNetBIOSTable": brMultiIFNetBIOSTable,
       "brMultiIFNetBIOSEntry": brMultiIFNetBIOSEntry,
       "brMultiIFNetBIOSIPMethod": brMultiIFNetBIOSIPMethod,
       "brMultiIFTCPIPNetBIOSPrimaryWINSAddr": brMultiIFTCPIPNetBIOSPrimaryWINSAddr,
       "brMultiIFTCPIPNetBIOSSecondaryWINSAddr": brMultiIFTCPIPNetBIOSSecondaryWINSAddr,
       "brMultiIFNetBEUIDomain": brMultiIFNetBEUIDomain,
       "brMultiIForiginalapipa": brMultiIForiginalapipa,
       "brMultiIFAPIPATable": brMultiIFAPIPATable,
       "brMultiIFAPIPAEntry": brMultiIFAPIPAEntry,
       "brMultiIFAPIPASupported": brMultiIFAPIPASupported,
       "brMultiIFAPIPAEnable": brMultiIFAPIPAEnable,
       "brMultiIForiginalLAA": brMultiIForiginalLAA,
       "brMultiIFLAATable": brMultiIFLAATable,
       "brMultiIFLAAEntry": brMultiIFLAAEntry,
       "brMultiIFLAASupported": brMultiIFLAASupported,
       "brMultiIFLAAMacAddress": brMultiIFLAAMacAddress,
       "brMultiIForiginalIPv6": brMultiIForiginalIPv6,
       "brMultiIFIPv6AddressCountTable": brMultiIFIPv6AddressCountTable,
       "brMultiIFIPv6AddressCountEntry": brMultiIFIPv6AddressCountEntry,
       "brMultiIFIPv6AddressCount": brMultiIFIPv6AddressCount,
       "brMultiIFIPv6AddressTable": brMultiIFIPv6AddressTable,
       "brMultiIFIPv6AddressEntry": brMultiIFIPv6AddressEntry,
       "brMultiIFIPv6AddressIndex": brMultiIFIPv6AddressIndex,
       "brMultiIFIPv6Address": brMultiIFIPv6Address,
       "brMultiIFIPv6UseMethod": brMultiIFIPv6UseMethod,
       "brMultiIFIPv6MethodServer": brMultiIFIPv6MethodServer,
       "brMultiIFIPv6StaticAddressCountTable": brMultiIFIPv6StaticAddressCountTable,
       "brMultiIFIPv6StaticAddressCountEntry": brMultiIFIPv6StaticAddressCountEntry,
       "brMultiIFIPv6StaticAddressCount": brMultiIFIPv6StaticAddressCount,
       "brMultiIFIPv6StaticAddressTable": brMultiIFIPv6StaticAddressTable,
       "brMultiIFIPv6StaticAddressEntry": brMultiIFIPv6StaticAddressEntry,
       "brMultiIFIPv6StaticAddressIndex": brMultiIFIPv6StaticAddressIndex,
       "brMultiIFIPv6StaticAddressEnable": brMultiIFIPv6StaticAddressEnable,
       "brMultiIFIPv6StaticAddress": brMultiIFIPv6StaticAddress,
       "brMultiIFIPv6StaticAddressPrefixLength": brMultiIFIPv6StaticAddressPrefixLength,
       "brMultiIFDNSIPv6AddressTable": brMultiIFDNSIPv6AddressTable,
       "brMultiIFDNSIPv6AddressEntry": brMultiIFDNSIPv6AddressEntry,
       "brMultiIFPrimaryDNSIPv6Address": brMultiIFPrimaryDNSIPv6Address,
       "brMultiIFSecondaryDNSIPv6Address": brMultiIFSecondaryDNSIPv6Address,
       "brMultiIForiginalWebServices": brMultiIForiginalWebServices,
       "brMultiIFWebServicesTable": brMultiIFWebServicesTable,
       "brMultiIFWebServicesEntry": brMultiIFWebServicesEntry,
       "brMultiIFWebServicesName": brMultiIFWebServicesName,
       "brMultiIFWebServicesInstanceID": brMultiIFWebServicesInstanceID,
       "brMultiIFWebServicesMetadataVersion": brMultiIFWebServicesMetadataVersion}
)
