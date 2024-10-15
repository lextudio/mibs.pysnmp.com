# SNMP MIB module (OASWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OASWITCH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:36 2024
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



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Oaccess_ObjectIdentity = ObjectIdentity
oaccess = _Oaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926)
)
_OaManagement_ObjectIdentity = ObjectIdentity
oaManagement = _OaManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1)
)
_OaSwitch_ObjectIdentity = ObjectIdentity
oaSwitch = _OaSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 5)
)
_OaSwitchMac_ObjectIdentity = ObjectIdentity
oaSwitchMac = _OaSwitchMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 5, 1)
)
_OaSwitchMacInfo_ObjectIdentity = ObjectIdentity
oaSwitchMacInfo = _OaSwitchMacInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 5, 1, 1)
)
_OaSwitchMacInfoNumber_Type = Integer32
_OaSwitchMacInfoNumber_Object = MibScalar
oaSwitchMacInfoNumber = _OaSwitchMacInfoNumber_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 5, 1, 1, 1),
    _OaSwitchMacInfoNumber_Type()
)
oaSwitchMacInfoNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSwitchMacInfoNumber.setStatus("mandatory")
_OaSwitchMacInfoMaxNumbr_Type = Integer32
_OaSwitchMacInfoMaxNumbr_Object = MibScalar
oaSwitchMacInfoMaxNumbr = _OaSwitchMacInfoMaxNumbr_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 5, 1, 1, 2),
    _OaSwitchMacInfoMaxNumbr_Type()
)
oaSwitchMacInfoMaxNumbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSwitchMacInfoMaxNumbr.setStatus("mandatory")


class _OaSwitchMacInfoClear_Type(Integer32):
    """Custom type oaSwitchMacInfoClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("none", 1))
    )


_OaSwitchMacInfoClear_Type.__name__ = "Integer32"
_OaSwitchMacInfoClear_Object = MibScalar
oaSwitchMacInfoClear = _OaSwitchMacInfoClear_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 5, 1, 1, 5),
    _OaSwitchMacInfoClear_Type()
)
oaSwitchMacInfoClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSwitchMacInfoClear.setStatus("mandatory")
_OaSwMacTable_Object = MibTable
oaSwMacTable = _OaSwMacTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    oaSwMacTable.setStatus("mandatory")
_OaSwMacEntry_Object = MibTableRow
oaSwMacEntry = _OaSwMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 5, 1, 2, 1)
)
oaSwMacEntry.setIndexNames(
    (0, "OASWITCH-MIB", "oaSwMacAddr"),
    (0, "OASWITCH-MIB", "oaSwMacVid"),
)
if mibBuilder.loadTexts:
    oaSwMacEntry.setStatus("mandatory")
_OaSwMacAddr_Type = MacAddress
_OaSwMacAddr_Object = MibTableColumn
oaSwMacAddr = _OaSwMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 5, 1, 2, 1, 1),
    _OaSwMacAddr_Type()
)
oaSwMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSwMacAddr.setStatus("mandatory")
_OaSwMacVid_Type = Integer32
_OaSwMacVid_Object = MibTableColumn
oaSwMacVid = _OaSwMacVid_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 5, 1, 2, 1, 2),
    _OaSwMacVid_Type()
)
oaSwMacVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSwMacVid.setStatus("mandatory")
_OaSwMacVidx_Type = Integer32
_OaSwMacVidx_Object = MibTableColumn
oaSwMacVidx = _OaSwMacVidx_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 5, 1, 2, 1, 6),
    _OaSwMacVidx_Type()
)
oaSwMacVidx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSwMacVidx.setStatus("mandatory")
_OaSwMacGetViewIndex_Type = Integer32
_OaSwMacGetViewIndex_Object = MibTableColumn
oaSwMacGetViewIndex = _OaSwMacGetViewIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 5, 1, 2, 1, 8),
    _OaSwMacGetViewIndex_Type()
)
oaSwMacGetViewIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSwMacGetViewIndex.setStatus("mandatory")


class _OaSwMacPort_Type(Integer32):
    """Custom type oaSwMacPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OaSwMacPort_Type.__name__ = "Integer32"
_OaSwMacPort_Object = MibTableColumn
oaSwMacPort = _OaSwMacPort_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 5, 1, 2, 1, 9),
    _OaSwMacPort_Type()
)
oaSwMacPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSwMacPort.setStatus("mandatory")


class _OaSwMacMode_Type(Integer32):
    """Custom type oaSwMacMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("other", 1),
          ("static", 3))
    )


_OaSwMacMode_Type.__name__ = "Integer32"
_OaSwMacMode_Object = MibTableColumn
oaSwMacMode = _OaSwMacMode_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 5, 1, 2, 1, 20),
    _OaSwMacMode_Type()
)
oaSwMacMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSwMacMode.setStatus("mandatory")


class _OaSwMacTagged_Type(Integer32):
    """Custom type oaSwMacTagged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_OaSwMacTagged_Type.__name__ = "Integer32"
_OaSwMacTagged_Object = MibTableColumn
oaSwMacTagged = _OaSwMacTagged_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 5, 1, 2, 1, 21),
    _OaSwMacTagged_Type()
)
oaSwMacTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSwMacTagged.setStatus("mandatory")
_OaSwMacPriority_Type = Integer32
_OaSwMacPriority_Object = MibTableColumn
oaSwMacPriority = _OaSwMacPriority_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 5, 1, 2, 1, 22),
    _OaSwMacPriority_Type()
)
oaSwMacPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSwMacPriority.setStatus("mandatory")
_OaSwMacFlags_Type = Integer32
_OaSwMacFlags_Object = MibTableColumn
oaSwMacFlags = _OaSwMacFlags_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 5, 1, 2, 1, 23),
    _OaSwMacFlags_Type()
)
oaSwMacFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSwMacFlags.setStatus("mandatory")


class _OaSwMacStatus_Type(Integer32):
    """Custom type oaSwMacStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_OaSwMacStatus_Type.__name__ = "Integer32"
_OaSwMacStatus_Object = MibTableColumn
oaSwMacStatus = _OaSwMacStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 5, 1, 2, 1, 30),
    _OaSwMacStatus_Type()
)
oaSwMacStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSwMacStatus.setStatus("mandatory")
_OaSysFrmGen_ObjectIdentity = ObjectIdentity
oaSysFrmGen = _OaSysFrmGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 5, 3)
)


class _OaSysFrmGenSession_Type(Integer32):
    """Custom type oaSysFrmGenSession based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idleFG", 1),
          ("runFG", 2))
    )


_OaSysFrmGenSession_Type.__name__ = "Integer32"
_OaSysFrmGenSession_Object = MibScalar
oaSysFrmGenSession = _OaSysFrmGenSession_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 5, 3, 1),
    _OaSysFrmGenSession_Type()
)
oaSysFrmGenSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSysFrmGenSession.setStatus("mandatory")


class _OaSysFrmGenDa_Type(MacAddress):
    """Custom type oaSysFrmGenDa based on MacAddress"""
    defaultHexValue = "000000000000"


_OaSysFrmGenDa_Object = MibScalar
oaSysFrmGenDa = _OaSysFrmGenDa_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 5, 3, 2),
    _OaSysFrmGenDa_Type()
)
oaSysFrmGenDa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSysFrmGenDa.setStatus("mandatory")


class _OaSysFrmGenSa_Type(MacAddress):
    """Custom type oaSysFrmGenSa based on MacAddress"""
    defaultHexValue = "000000000000"


_OaSysFrmGenSa_Object = MibScalar
oaSysFrmGenSa = _OaSysFrmGenSa_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 5, 3, 3),
    _OaSysFrmGenSa_Type()
)
oaSysFrmGenSa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSysFrmGenSa.setStatus("mandatory")
_OaSysFrmGenPktFill_Type = Integer32
_OaSysFrmGenPktFill_Object = MibScalar
oaSysFrmGenPktFill = _OaSysFrmGenPktFill_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 5, 3, 4),
    _OaSysFrmGenPktFill_Type()
)
oaSysFrmGenPktFill.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSysFrmGenPktFill.setStatus("mandatory")
_OaSysFrmGenPktRate_Type = Integer32
_OaSysFrmGenPktRate_Object = MibScalar
oaSysFrmGenPktRate = _OaSysFrmGenPktRate_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 5, 3, 5),
    _OaSysFrmGenPktRate_Type()
)
oaSysFrmGenPktRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSysFrmGenPktRate.setStatus("mandatory")
_OaSysFrmGenDestMap_Type = OctetString
_OaSysFrmGenDestMap_Object = MibScalar
oaSysFrmGenDestMap = _OaSysFrmGenDestMap_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 5, 3, 6),
    _OaSysFrmGenDestMap_Type()
)
oaSysFrmGenDestMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSysFrmGenDestMap.setStatus("mandatory")
_OaSysFrmGenPktNum_Type = Counter32
_OaSysFrmGenPktNum_Object = MibScalar
oaSysFrmGenPktNum = _OaSysFrmGenPktNum_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 5, 3, 7),
    _OaSysFrmGenPktNum_Type()
)
oaSysFrmGenPktNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSysFrmGenPktNum.setStatus("mandatory")
_OaSysFrmGenPktLen_Type = Integer32
_OaSysFrmGenPktLen_Object = MibScalar
oaSysFrmGenPktLen = _OaSysFrmGenPktLen_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 5, 3, 8),
    _OaSysFrmGenPktLen_Type()
)
oaSysFrmGenPktLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSysFrmGenPktLen.setStatus("mandatory")
_OaSysFrmGenXmtPktNum_Type = Counter32
_OaSysFrmGenXmtPktNum_Object = MibScalar
oaSysFrmGenXmtPktNum = _OaSysFrmGenXmtPktNum_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 5, 3, 9),
    _OaSysFrmGenXmtPktNum_Type()
)
oaSysFrmGenXmtPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSysFrmGenXmtPktNum.setStatus("mandatory")


class _OaSysFrmGenPriority_Type(Integer32):
    """Custom type oaSysFrmGenPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_OaSysFrmGenPriority_Type.__name__ = "Integer32"
_OaSysFrmGenPriority_Object = MibScalar
oaSysFrmGenPriority = _OaSysFrmGenPriority_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 5, 3, 10),
    _OaSysFrmGenPriority_Type()
)
oaSysFrmGenPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSysFrmGenPriority.setStatus("mandatory")


class _OaSysFrmGenVlanId_Type(Integer32):
    """Custom type oaSysFrmGenVlanId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_OaSysFrmGenVlanId_Type.__name__ = "Integer32"
_OaSysFrmGenVlanId_Object = MibScalar
oaSysFrmGenVlanId = _OaSysFrmGenVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 5, 3, 11),
    _OaSysFrmGenVlanId_Type()
)
oaSysFrmGenVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaSysFrmGenVlanId.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OASWITCH-MIB",
    **{"MacAddress": MacAddress,
       "oaccess": oaccess,
       "oaManagement": oaManagement,
       "oaSwitch": oaSwitch,
       "oaSwitchMac": oaSwitchMac,
       "oaSwitchMacInfo": oaSwitchMacInfo,
       "oaSwitchMacInfoNumber": oaSwitchMacInfoNumber,
       "oaSwitchMacInfoMaxNumbr": oaSwitchMacInfoMaxNumbr,
       "oaSwitchMacInfoClear": oaSwitchMacInfoClear,
       "oaSwMacTable": oaSwMacTable,
       "oaSwMacEntry": oaSwMacEntry,
       "oaSwMacAddr": oaSwMacAddr,
       "oaSwMacVid": oaSwMacVid,
       "oaSwMacVidx": oaSwMacVidx,
       "oaSwMacGetViewIndex": oaSwMacGetViewIndex,
       "oaSwMacPort": oaSwMacPort,
       "oaSwMacMode": oaSwMacMode,
       "oaSwMacTagged": oaSwMacTagged,
       "oaSwMacPriority": oaSwMacPriority,
       "oaSwMacFlags": oaSwMacFlags,
       "oaSwMacStatus": oaSwMacStatus,
       "oaSysFrmGen": oaSysFrmGen,
       "oaSysFrmGenSession": oaSysFrmGenSession,
       "oaSysFrmGenDa": oaSysFrmGenDa,
       "oaSysFrmGenSa": oaSysFrmGenSa,
       "oaSysFrmGenPktFill": oaSysFrmGenPktFill,
       "oaSysFrmGenPktRate": oaSysFrmGenPktRate,
       "oaSysFrmGenDestMap": oaSysFrmGenDestMap,
       "oaSysFrmGenPktNum": oaSysFrmGenPktNum,
       "oaSysFrmGenPktLen": oaSysFrmGenPktLen,
       "oaSysFrmGenXmtPktNum": oaSysFrmGenXmtPktNum,
       "oaSysFrmGenPriority": oaSysFrmGenPriority,
       "oaSysFrmGenVlanId": oaSysFrmGenVlanId}
)
