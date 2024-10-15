# SNMP MIB module (LOGEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LOGEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:19:19 2024
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

(logExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "logExt")

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

apLogExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 20, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _ApLogFileName_Type(DisplayString):
    """Custom type apLogFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApLogFileName_Type.__name__ = "DisplayString"
_ApLogFileName_Object = MibScalar
apLogFileName = _ApLogFileName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 20, 2),
    _ApLogFileName_Type()
)
apLogFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLogFileName.setStatus("current")


class _ApLogBufferSize_Type(Integer32):
    """Custom type apLogBufferSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64000),
    )


_ApLogBufferSize_Type.__name__ = "Integer32"
_ApLogBufferSize_Object = MibScalar
apLogBufferSize = _ApLogBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 20, 3),
    _ApLogBufferSize_Type()
)
apLogBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLogBufferSize.setStatus("current")
_ApLogHostTable_Object = MibTable
apLogHostTable = _ApLogHostTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 20, 4)
)
if mibBuilder.loadTexts:
    apLogHostTable.setStatus("current")
_ApLogHostEntry_Object = MibTableRow
apLogHostEntry = _ApLogHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 20, 4, 1)
)
apLogHostEntry.setIndexNames(
    (0, "LOGEXT-MIB", "apLogHostIpAddress"),
)
if mibBuilder.loadTexts:
    apLogHostEntry.setStatus("current")
_ApLogHostIpAddress_Type = IpAddress
_ApLogHostIpAddress_Object = MibTableColumn
apLogHostIpAddress = _ApLogHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 20, 4, 1, 1),
    _ApLogHostIpAddress_Type()
)
apLogHostIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apLogHostIpAddress.setStatus("current")


class _ApLogHostFacility_Type(Integer32):
    """Custom type apLogHostFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ApLogHostFacility_Type.__name__ = "Integer32"
_ApLogHostFacility_Object = MibTableColumn
apLogHostFacility = _ApLogHostFacility_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 20, 4, 1, 2),
    _ApLogHostFacility_Type()
)
apLogHostFacility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apLogHostFacility.setStatus("current")
_ApLogHostStatus_Type = RowStatus
_ApLogHostStatus_Object = MibTableColumn
apLogHostStatus = _ApLogHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 20, 4, 1, 3),
    _ApLogHostStatus_Type()
)
apLogHostStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apLogHostStatus.setStatus("current")


class _ApLogCmds_Type(Integer32):
    """Custom type apLogCmds based on Integer32"""
    defaultValue = 0

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


_ApLogCmds_Type.__name__ = "Integer32"
_ApLogCmds_Object = MibScalar
apLogCmds = _ApLogCmds_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 20, 5),
    _ApLogCmds_Type()
)
apLogCmds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLogCmds.setStatus("current")
_ApLogSubSystemTable_Object = MibTable
apLogSubSystemTable = _ApLogSubSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 20, 7)
)
if mibBuilder.loadTexts:
    apLogSubSystemTable.setStatus("current")
_ApLogSubSystemEntry_Object = MibTableRow
apLogSubSystemEntry = _ApLogSubSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 20, 7, 1)
)
apLogSubSystemEntry.setIndexNames(
    (0, "LOGEXT-MIB", "apLogSubSystemName"),
)
if mibBuilder.loadTexts:
    apLogSubSystemEntry.setStatus("current")


class _ApLogSubSystemName_Type(DisplayString):
    """Custom type apLogSubSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ApLogSubSystemName_Type.__name__ = "DisplayString"
_ApLogSubSystemName_Object = MibTableColumn
apLogSubSystemName = _ApLogSubSystemName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 20, 7, 1, 1),
    _ApLogSubSystemName_Type()
)
apLogSubSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLogSubSystemName.setStatus("current")


class _ApLogSubSystemLevel_Type(Integer32):
    """Custom type apLogSubSystemLevel based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("error", 3),
          ("fatal", 0),
          ("info", 6),
          ("notice", 5),
          ("off", 8),
          ("warning", 4))
    )


_ApLogSubSystemLevel_Type.__name__ = "Integer32"
_ApLogSubSystemLevel_Object = MibTableColumn
apLogSubSystemLevel = _ApLogSubSystemLevel_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 20, 7, 1, 2),
    _ApLogSubSystemLevel_Type()
)
apLogSubSystemLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLogSubSystemLevel.setStatus("current")
_ApLogSendMailTable_Object = MibTable
apLogSendMailTable = _ApLogSendMailTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 20, 8)
)
if mibBuilder.loadTexts:
    apLogSendMailTable.setStatus("current")
_ApLogSendMailEntry_Object = MibTableRow
apLogSendMailEntry = _ApLogSendMailEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 20, 8, 1)
)
apLogSendMailEntry.setIndexNames(
    (0, "LOGEXT-MIB", "apLogRecipientName"),
)
if mibBuilder.loadTexts:
    apLogSendMailEntry.setStatus("current")
_ApLogRecipientAddress_Type = IpAddress
_ApLogRecipientAddress_Object = MibTableColumn
apLogRecipientAddress = _ApLogRecipientAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 20, 8, 1, 1),
    _ApLogRecipientAddress_Type()
)
apLogRecipientAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apLogRecipientAddress.setStatus("current")


class _ApLogRecipientName_Type(DisplayString):
    """Custom type apLogRecipientName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_ApLogRecipientName_Type.__name__ = "DisplayString"
_ApLogRecipientName_Object = MibTableColumn
apLogRecipientName = _ApLogRecipientName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 20, 8, 1, 2),
    _ApLogRecipientName_Type()
)
apLogRecipientName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apLogRecipientName.setStatus("current")


class _ApLogSendMailLevel_Type(Integer32):
    """Custom type apLogSendMailLevel based on Integer32"""
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
        *(("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("fatal", 0),
          ("info", 6),
          ("notice", 5),
          ("warning", 4))
    )


_ApLogSendMailLevel_Type.__name__ = "Integer32"
_ApLogSendMailLevel_Object = MibTableColumn
apLogSendMailLevel = _ApLogSendMailLevel_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 20, 8, 1, 3),
    _ApLogSendMailLevel_Type()
)
apLogSendMailLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apLogSendMailLevel.setStatus("current")
_ApLogSendMailStatus_Type = RowStatus
_ApLogSendMailStatus_Object = MibTableColumn
apLogSendMailStatus = _ApLogSendMailStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 20, 8, 1, 4),
    _ApLogSendMailStatus_Type()
)
apLogSendMailStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apLogSendMailStatus.setStatus("current")


class _ApLogSendMailDomain_Type(DisplayString):
    """Custom type apLogSendMailDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApLogSendMailDomain_Type.__name__ = "DisplayString"
_ApLogSendMailDomain_Object = MibTableColumn
apLogSendMailDomain = _ApLogSendMailDomain_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 20, 8, 1, 5),
    _ApLogSendMailDomain_Type()
)
apLogSendMailDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apLogSendMailDomain.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LOGEXT-MIB",
    **{"apLogExtMib": apLogExtMib,
       "apLogFileName": apLogFileName,
       "apLogBufferSize": apLogBufferSize,
       "apLogHostTable": apLogHostTable,
       "apLogHostEntry": apLogHostEntry,
       "apLogHostIpAddress": apLogHostIpAddress,
       "apLogHostFacility": apLogHostFacility,
       "apLogHostStatus": apLogHostStatus,
       "apLogCmds": apLogCmds,
       "apLogSubSystemTable": apLogSubSystemTable,
       "apLogSubSystemEntry": apLogSubSystemEntry,
       "apLogSubSystemName": apLogSubSystemName,
       "apLogSubSystemLevel": apLogSubSystemLevel,
       "apLogSendMailTable": apLogSendMailTable,
       "apLogSendMailEntry": apLogSendMailEntry,
       "apLogRecipientAddress": apLogRecipientAddress,
       "apLogRecipientName": apLogRecipientName,
       "apLogSendMailLevel": apLogSendMailLevel,
       "apLogSendMailStatus": apLogSendMailStatus,
       "apLogSendMailDomain": apLogSendMailDomain}
)
