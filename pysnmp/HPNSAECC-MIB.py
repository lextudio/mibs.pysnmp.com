# SNMP MIB module (HPNSAECC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPNSAECC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:19 2024
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
 NotificationType,
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
    "NotificationType",
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

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_Hpnsa_ObjectIdentity = ObjectIdentity
hpnsa = _Hpnsa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23)
)
_HpnsaECC_ObjectIdentity = ObjectIdentity
hpnsaECC = _HpnsaECC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 6)
)
_HpnsaEccMibRev_ObjectIdentity = ObjectIdentity
hpnsaEccMibRev = _HpnsaEccMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 6, 1)
)


class _HpnsaEccMibRevMajor_Type(Integer32):
    """Custom type hpnsaEccMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnsaEccMibRevMajor_Type.__name__ = "Integer32"
_HpnsaEccMibRevMajor_Object = MibScalar
hpnsaEccMibRevMajor = _HpnsaEccMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 6, 1, 1),
    _HpnsaEccMibRevMajor_Type()
)
hpnsaEccMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEccMibRevMajor.setStatus("mandatory")


class _HpnsaEccMibRevMinor_Type(Integer32):
    """Custom type hpnsaEccMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaEccMibRevMinor_Type.__name__ = "Integer32"
_HpnsaEccMibRevMinor_Object = MibScalar
hpnsaEccMibRevMinor = _HpnsaEccMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 6, 1, 2),
    _HpnsaEccMibRevMinor_Type()
)
hpnsaEccMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEccMibRevMinor.setStatus("mandatory")
_HpnsaEccAgent_ObjectIdentity = ObjectIdentity
hpnsaEccAgent = _HpnsaEccAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 6, 2)
)
_HpnsaEccAgentTable_Object = MibTable
hpnsaEccAgentTable = _HpnsaEccAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 6, 2, 1)
)
if mibBuilder.loadTexts:
    hpnsaEccAgentTable.setStatus("mandatory")
_HpnsaEccAgentEntry_Object = MibTableRow
hpnsaEccAgentEntry = _HpnsaEccAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 6, 2, 1, 1)
)
hpnsaEccAgentEntry.setIndexNames(
    (0, "HPNSAECC-MIB", "hpnsaEccAgentIndex"),
)
if mibBuilder.loadTexts:
    hpnsaEccAgentEntry.setStatus("mandatory")


class _HpnsaEccAgentIndex_Type(Integer32):
    """Custom type hpnsaEccAgentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaEccAgentIndex_Type.__name__ = "Integer32"
_HpnsaEccAgentIndex_Object = MibTableColumn
hpnsaEccAgentIndex = _HpnsaEccAgentIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 6, 2, 1, 1, 1),
    _HpnsaEccAgentIndex_Type()
)
hpnsaEccAgentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEccAgentIndex.setStatus("mandatory")


class _HpnsaEccAgentName_Type(DisplayString):
    """Custom type hpnsaEccAgentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaEccAgentName_Type.__name__ = "DisplayString"
_HpnsaEccAgentName_Object = MibTableColumn
hpnsaEccAgentName = _HpnsaEccAgentName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 6, 2, 1, 1, 2),
    _HpnsaEccAgentName_Type()
)
hpnsaEccAgentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEccAgentName.setStatus("mandatory")


class _HpnsaEccAgentVersion_Type(DisplayString):
    """Custom type hpnsaEccAgentVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_HpnsaEccAgentVersion_Type.__name__ = "DisplayString"
_HpnsaEccAgentVersion_Object = MibTableColumn
hpnsaEccAgentVersion = _HpnsaEccAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 6, 2, 1, 1, 3),
    _HpnsaEccAgentVersion_Type()
)
hpnsaEccAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEccAgentVersion.setStatus("mandatory")


class _HpnsaEccAgentDate_Type(OctetString):
    """Custom type hpnsaEccAgentDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_HpnsaEccAgentDate_Type.__name__ = "OctetString"
_HpnsaEccAgentDate_Object = MibTableColumn
hpnsaEccAgentDate = _HpnsaEccAgentDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 6, 2, 1, 1, 4),
    _HpnsaEccAgentDate_Type()
)
hpnsaEccAgentDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEccAgentDate.setStatus("mandatory")
_HpnsaEccLog_ObjectIdentity = ObjectIdentity
hpnsaEccLog = _HpnsaEccLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 6, 3)
)


class _HpnsaEccStatus_Type(Integer32):
    """Custom type hpnsaEccStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("notSupported", 1))
    )


_HpnsaEccStatus_Type.__name__ = "Integer32"
_HpnsaEccStatus_Object = MibScalar
hpnsaEccStatus = _HpnsaEccStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 6, 3, 1),
    _HpnsaEccStatus_Type()
)
hpnsaEccStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEccStatus.setStatus("mandatory")
_HpnsaEccEraseLog_Type = Integer32
_HpnsaEccEraseLog_Object = MibScalar
hpnsaEccEraseLog = _HpnsaEccEraseLog_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 6, 3, 2),
    _HpnsaEccEraseLog_Type()
)
hpnsaEccEraseLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaEccEraseLog.setStatus("mandatory")
_HpnsaEccTotalErrCorrected_Type = Integer32
_HpnsaEccTotalErrCorrected_Object = MibScalar
hpnsaEccTotalErrCorrected = _HpnsaEccTotalErrCorrected_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 6, 3, 3),
    _HpnsaEccTotalErrCorrected_Type()
)
hpnsaEccTotalErrCorrected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEccTotalErrCorrected.setStatus("mandatory")


class _HpnsaEccTrapEnable_Type(Integer32):
    """Custom type hpnsaEccTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("trapOff", 0),
          ("trapOn", 1))
    )


_HpnsaEccTrapEnable_Type.__name__ = "Integer32"
_HpnsaEccTrapEnable_Object = MibScalar
hpnsaEccTrapEnable = _HpnsaEccTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 6, 3, 4),
    _HpnsaEccTrapEnable_Type()
)
hpnsaEccTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaEccTrapEnable.setStatus("mandatory")


class _HpnsaEccTrapDelay_Type(Integer32):
    """Custom type hpnsaEccTrapDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 5000),
    )


_HpnsaEccTrapDelay_Type.__name__ = "Integer32"
_HpnsaEccTrapDelay_Object = MibScalar
hpnsaEccTrapDelay = _HpnsaEccTrapDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 6, 3, 5),
    _HpnsaEccTrapDelay_Type()
)
hpnsaEccTrapDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaEccTrapDelay.setStatus("mandatory")


class _HpnsaEccPollTime_Type(Integer32):
    """Custom type hpnsaEccPollTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 2592000),
    )


_HpnsaEccPollTime_Type.__name__ = "Integer32"
_HpnsaEccPollTime_Object = MibScalar
hpnsaEccPollTime = _HpnsaEccPollTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 6, 3, 6),
    _HpnsaEccPollTime_Type()
)
hpnsaEccPollTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaEccPollTime.setStatus("mandatory")
_HpnsaEccMemErrTable_Object = MibTable
hpnsaEccMemErrTable = _HpnsaEccMemErrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 6, 3, 7)
)
if mibBuilder.loadTexts:
    hpnsaEccMemErrTable.setStatus("mandatory")
_HpnsaEccMemErrEntry_Object = MibTableRow
hpnsaEccMemErrEntry = _HpnsaEccMemErrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 6, 3, 7, 1)
)
hpnsaEccMemErrEntry.setIndexNames(
    (0, "HPNSAECC-MIB", "hpnsaEccMemErrIndex"),
)
if mibBuilder.loadTexts:
    hpnsaEccMemErrEntry.setStatus("mandatory")
_HpnsaEccMemErrIndex_Type = Integer32
_HpnsaEccMemErrIndex_Object = MibTableColumn
hpnsaEccMemErrIndex = _HpnsaEccMemErrIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 6, 3, 7, 1, 1),
    _HpnsaEccMemErrIndex_Type()
)
hpnsaEccMemErrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEccMemErrIndex.setStatus("mandatory")
_HpnsaEccMemErrTime_Type = DisplayString
_HpnsaEccMemErrTime_Object = MibTableColumn
hpnsaEccMemErrTime = _HpnsaEccMemErrTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 6, 3, 7, 1, 2),
    _HpnsaEccMemErrTime_Type()
)
hpnsaEccMemErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEccMemErrTime.setStatus("mandatory")
_HpnsaEccMemErrDesc_Type = DisplayString
_HpnsaEccMemErrDesc_Object = MibTableColumn
hpnsaEccMemErrDesc = _HpnsaEccMemErrDesc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 6, 3, 7, 1, 3),
    _HpnsaEccMemErrDesc_Type()
)
hpnsaEccMemErrDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEccMemErrDesc.setStatus("mandatory")

# Managed Objects groups


# Notification objects

hpnsaEccErrorCorrected = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 6, 0, 4353)
)
if mibBuilder.loadTexts:
    hpnsaEccErrorCorrected.setStatus(
        ""
    )

hpnsaEccSBEOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 6, 0, 4354)
)
if mibBuilder.loadTexts:
    hpnsaEccSBEOverflow.setStatus(
        ""
    )

hpnsaEccMemoryResize = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 6, 0, 4355)
)
if mibBuilder.loadTexts:
    hpnsaEccMemoryResize.setStatus(
        ""
    )

hpnsaEccMultiBitError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 6, 0, 4357)
)
if mibBuilder.loadTexts:
    hpnsaEccMultiBitError.setStatus(
        ""
    )

hpnsaEccMultiBitErrorOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 6, 0, 4358)
)
if mibBuilder.loadTexts:
    hpnsaEccMultiBitErrorOverflow.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPNSAECC-MIB",
    **{"hp": hp,
       "nm": nm,
       "hpnsa": hpnsa,
       "hpnsaECC": hpnsaECC,
       "hpnsaEccErrorCorrected": hpnsaEccErrorCorrected,
       "hpnsaEccSBEOverflow": hpnsaEccSBEOverflow,
       "hpnsaEccMemoryResize": hpnsaEccMemoryResize,
       "hpnsaEccMultiBitError": hpnsaEccMultiBitError,
       "hpnsaEccMultiBitErrorOverflow": hpnsaEccMultiBitErrorOverflow,
       "hpnsaEccMibRev": hpnsaEccMibRev,
       "hpnsaEccMibRevMajor": hpnsaEccMibRevMajor,
       "hpnsaEccMibRevMinor": hpnsaEccMibRevMinor,
       "hpnsaEccAgent": hpnsaEccAgent,
       "hpnsaEccAgentTable": hpnsaEccAgentTable,
       "hpnsaEccAgentEntry": hpnsaEccAgentEntry,
       "hpnsaEccAgentIndex": hpnsaEccAgentIndex,
       "hpnsaEccAgentName": hpnsaEccAgentName,
       "hpnsaEccAgentVersion": hpnsaEccAgentVersion,
       "hpnsaEccAgentDate": hpnsaEccAgentDate,
       "hpnsaEccLog": hpnsaEccLog,
       "hpnsaEccStatus": hpnsaEccStatus,
       "hpnsaEccEraseLog": hpnsaEccEraseLog,
       "hpnsaEccTotalErrCorrected": hpnsaEccTotalErrCorrected,
       "hpnsaEccTrapEnable": hpnsaEccTrapEnable,
       "hpnsaEccTrapDelay": hpnsaEccTrapDelay,
       "hpnsaEccPollTime": hpnsaEccPollTime,
       "hpnsaEccMemErrTable": hpnsaEccMemErrTable,
       "hpnsaEccMemErrEntry": hpnsaEccMemErrEntry,
       "hpnsaEccMemErrIndex": hpnsaEccMemErrIndex,
       "hpnsaEccMemErrTime": hpnsaEccMemErrTime,
       "hpnsaEccMemErrDesc": hpnsaEccMemErrDesc}
)
