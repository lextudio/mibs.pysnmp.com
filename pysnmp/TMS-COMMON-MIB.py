# SNMP MIB module (TMS-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TMS-COMMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:05:25 2024
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

(PortList,
 dot1qStaticMulticastEntry) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "dot1qStaticMulticastEntry")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(tmsGeneric,) = mibBuilder.importSymbols(
    "WRS-MASTER-MIB",
    "tmsGeneric")


# MODULE-IDENTITY

tmsCommonMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1)
)
tmsCommonMib.setRevisions(
        ("2000-11-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TmsCommonNotify_ObjectIdentity = ObjectIdentity
tmsCommonNotify = _TmsCommonNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 0)
)
_TmsCommonVer_ObjectIdentity = ObjectIdentity
tmsCommonVer = _TmsCommonVer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 1)
)
_TmsCommonVerMIBMajor_Type = Integer32
_TmsCommonVerMIBMajor_Object = MibScalar
tmsCommonVerMIBMajor = _TmsCommonVerMIBMajor_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 1, 1),
    _TmsCommonVerMIBMajor_Type()
)
tmsCommonVerMIBMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsCommonVerMIBMajor.setStatus("current")
_TmsCommonVerMIBMinor_Type = Integer32
_TmsCommonVerMIBMinor_Object = MibScalar
tmsCommonVerMIBMinor = _TmsCommonVerMIBMinor_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 1, 2),
    _TmsCommonVerMIBMinor_Type()
)
tmsCommonVerMIBMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsCommonVerMIBMinor.setStatus("current")
_TmsCommonVerBootSWMajor_Type = Integer32
_TmsCommonVerBootSWMajor_Object = MibScalar
tmsCommonVerBootSWMajor = _TmsCommonVerBootSWMajor_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 1, 3),
    _TmsCommonVerBootSWMajor_Type()
)
tmsCommonVerBootSWMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsCommonVerBootSWMajor.setStatus("current")
_TmsCommonVerBootSWMinor_Type = Integer32
_TmsCommonVerBootSWMinor_Object = MibScalar
tmsCommonVerBootSWMinor = _TmsCommonVerBootSWMinor_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 1, 4),
    _TmsCommonVerBootSWMinor_Type()
)
tmsCommonVerBootSWMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsCommonVerBootSWMinor.setStatus("current")
_TmsCommonVerAppSWMajor_Type = Integer32
_TmsCommonVerAppSWMajor_Object = MibScalar
tmsCommonVerAppSWMajor = _TmsCommonVerAppSWMajor_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 1, 5),
    _TmsCommonVerAppSWMajor_Type()
)
tmsCommonVerAppSWMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsCommonVerAppSWMajor.setStatus("current")
_TmsCommonVerAppSWMinor_Type = Integer32
_TmsCommonVerAppSWMinor_Object = MibScalar
tmsCommonVerAppSWMinor = _TmsCommonVerAppSWMinor_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 1, 6),
    _TmsCommonVerAppSWMinor_Type()
)
tmsCommonVerAppSWMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsCommonVerAppSWMinor.setStatus("current")
_TmsCommonIP_ObjectIdentity = ObjectIdentity
tmsCommonIP = _TmsCommonIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 2)
)
_TmsCommonIPMACAddr_Type = MacAddress
_TmsCommonIPMACAddr_Object = MibScalar
tmsCommonIPMACAddr = _TmsCommonIPMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 2, 1),
    _TmsCommonIPMACAddr_Type()
)
tmsCommonIPMACAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmsCommonIPMACAddr.setStatus("current")
_TmsCommonIPIpAddress_Type = IpAddress
_TmsCommonIPIpAddress_Object = MibScalar
tmsCommonIPIpAddress = _TmsCommonIPIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 2, 2),
    _TmsCommonIPIpAddress_Type()
)
tmsCommonIPIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmsCommonIPIpAddress.setStatus("current")
_TmsCommonIPGateAddress_Type = IpAddress
_TmsCommonIPGateAddress_Object = MibScalar
tmsCommonIPGateAddress = _TmsCommonIPGateAddress_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 2, 3),
    _TmsCommonIPGateAddress_Type()
)
tmsCommonIPGateAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmsCommonIPGateAddress.setStatus("current")
_TmsCommonIPNetMask_Type = IpAddress
_TmsCommonIPNetMask_Object = MibScalar
tmsCommonIPNetMask = _TmsCommonIPNetMask_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 2, 4),
    _TmsCommonIPNetMask_Type()
)
tmsCommonIPNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmsCommonIPNetMask.setStatus("current")


class _TmsCommonIPStatus_Type(Integer32):
    """Custom type tmsCommonIPStatus based on Integer32"""
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
        *(("apply", 4),
          ("modified", 2),
          ("notModified", 1),
          ("restore", 3))
    )


_TmsCommonIPStatus_Type.__name__ = "Integer32"
_TmsCommonIPStatus_Object = MibScalar
tmsCommonIPStatus = _TmsCommonIPStatus_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 2, 5),
    _TmsCommonIPStatus_Type()
)
tmsCommonIPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmsCommonIPStatus.setStatus("current")
_TmsCommonLoad_ObjectIdentity = ObjectIdentity
tmsCommonLoad = _TmsCommonLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 5)
)
_TmsCommonLoadTftpAddress_Type = IpAddress
_TmsCommonLoadTftpAddress_Object = MibScalar
tmsCommonLoadTftpAddress = _TmsCommonLoadTftpAddress_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 5, 1),
    _TmsCommonLoadTftpAddress_Type()
)
tmsCommonLoadTftpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmsCommonLoadTftpAddress.setStatus("current")


class _TmsCommonLoadTftpFileName_Type(DisplayString):
    """Custom type tmsCommonLoadTftpFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmsCommonLoadTftpFileName_Type.__name__ = "DisplayString"
_TmsCommonLoadTftpFileName_Object = MibScalar
tmsCommonLoadTftpFileName = _TmsCommonLoadTftpFileName_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 5, 2),
    _TmsCommonLoadTftpFileName_Type()
)
tmsCommonLoadTftpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmsCommonLoadTftpFileName.setStatus("current")


class _TmsCommonLoadType_Type(Integer32):
    """Custom type tmsCommonLoadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("application", 1),
          ("boot", 2),
          ("configuration", 3))
    )


_TmsCommonLoadType_Type.__name__ = "Integer32"
_TmsCommonLoadType_Object = MibScalar
tmsCommonLoadType = _TmsCommonLoadType_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 5, 3),
    _TmsCommonLoadType_Type()
)
tmsCommonLoadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmsCommonLoadType.setStatus("current")


class _TmsCommonLoadExecute_Type(Integer32):
    """Custom type tmsCommonLoadExecute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("download", 2),
          ("noop", 1),
          ("upload", 3))
    )


_TmsCommonLoadExecute_Type.__name__ = "Integer32"
_TmsCommonLoadExecute_Object = MibScalar
tmsCommonLoadExecute = _TmsCommonLoadExecute_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 5, 4),
    _TmsCommonLoadExecute_Type()
)
tmsCommonLoadExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmsCommonLoadExecute.setStatus("current")


class _TmsCommonLoadExecuteStatus_Type(Integer32):
    """Custom type tmsCommonLoadExecuteStatus based on Integer32"""
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
        *(("errorConnection", 4),
          ("errorFault", 6),
          ("errorFilename", 5),
          ("inProgress", 2),
          ("notStarted", 1),
          ("success", 3))
    )


_TmsCommonLoadExecuteStatus_Type.__name__ = "Integer32"
_TmsCommonLoadExecuteStatus_Object = MibScalar
tmsCommonLoadExecuteStatus = _TmsCommonLoadExecuteStatus_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 5, 5),
    _TmsCommonLoadExecuteStatus_Type()
)
tmsCommonLoadExecuteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsCommonLoadExecuteStatus.setStatus("current")
_TmsCommonMisc_ObjectIdentity = ObjectIdentity
tmsCommonMisc = _TmsCommonMisc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 6)
)


class _TmsCommonMiscSaveToNvm_Type(Integer32):
    """Custom type tmsCommonMiscSaveToNvm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("save", 2),
          ("saveInProgress", 3))
    )


_TmsCommonMiscSaveToNvm_Type.__name__ = "Integer32"
_TmsCommonMiscSaveToNvm_Object = MibScalar
tmsCommonMiscSaveToNvm = _TmsCommonMiscSaveToNvm_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 6, 1),
    _TmsCommonMiscSaveToNvm_Type()
)
tmsCommonMiscSaveToNvm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmsCommonMiscSaveToNvm.setStatus("current")


class _TmsCommonMiscSnmpSecurityOnOff_Type(Integer32):
    """Custom type tmsCommonMiscSnmpSecurityOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_TmsCommonMiscSnmpSecurityOnOff_Type.__name__ = "Integer32"
_TmsCommonMiscSnmpSecurityOnOff_Object = MibScalar
tmsCommonMiscSnmpSecurityOnOff = _TmsCommonMiscSnmpSecurityOnOff_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 6, 2),
    _TmsCommonMiscSnmpSecurityOnOff_Type()
)
tmsCommonMiscSnmpSecurityOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmsCommonMiscSnmpSecurityOnOff.setStatus("obsolete")


class _TmsCommonMiscSpanOnOff_Type(Integer32):
    """Custom type tmsCommonMiscSpanOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_TmsCommonMiscSpanOnOff_Type.__name__ = "Integer32"
_TmsCommonMiscSpanOnOff_Object = MibScalar
tmsCommonMiscSpanOnOff = _TmsCommonMiscSpanOnOff_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 6, 3),
    _TmsCommonMiscSpanOnOff_Type()
)
tmsCommonMiscSpanOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmsCommonMiscSpanOnOff.setStatus("current")


class _TmsCommonMiscBOOTPOnOff_Type(Integer32):
    """Custom type tmsCommonMiscBOOTPOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_TmsCommonMiscBOOTPOnOff_Type.__name__ = "Integer32"
_TmsCommonMiscBOOTPOnOff_Object = MibScalar
tmsCommonMiscBOOTPOnOff = _TmsCommonMiscBOOTPOnOff_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 6, 4),
    _TmsCommonMiscBOOTPOnOff_Type()
)
tmsCommonMiscBOOTPOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmsCommonMiscBOOTPOnOff.setStatus("current")


class _TmsCommonMiscDHCPOnOff_Type(Integer32):
    """Custom type tmsCommonMiscDHCPOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_TmsCommonMiscDHCPOnOff_Type.__name__ = "Integer32"
_TmsCommonMiscDHCPOnOff_Object = MibScalar
tmsCommonMiscDHCPOnOff = _TmsCommonMiscDHCPOnOff_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 6, 5),
    _TmsCommonMiscDHCPOnOff_Type()
)
tmsCommonMiscDHCPOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmsCommonMiscDHCPOnOff.setStatus("current")


class _TmsCommonMiscBaud_Type(Integer32):
    """Custom type tmsCommonMiscBaud based on Integer32"""
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
        *(("baud19200", 3),
          ("baud2400", 1),
          ("baud38400", 4),
          ("baud9600", 2))
    )


_TmsCommonMiscBaud_Type.__name__ = "Integer32"
_TmsCommonMiscBaud_Object = MibScalar
tmsCommonMiscBaud = _TmsCommonMiscBaud_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 6, 6),
    _TmsCommonMiscBaud_Type()
)
tmsCommonMiscBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmsCommonMiscBaud.setStatus("current")


class _TmsCommonMiscPassword_Type(DisplayString):
    """Custom type tmsCommonMiscPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_TmsCommonMiscPassword_Type.__name__ = "DisplayString"
_TmsCommonMiscPassword_Object = MibScalar
tmsCommonMiscPassword = _TmsCommonMiscPassword_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 6, 7),
    _TmsCommonMiscPassword_Type()
)
tmsCommonMiscPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmsCommonMiscPassword.setStatus("current")


class _TmsCommonMiscProductName_Type(DisplayString):
    """Custom type tmsCommonMiscProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmsCommonMiscProductName_Type.__name__ = "DisplayString"
_TmsCommonMiscProductName_Object = MibScalar
tmsCommonMiscProductName = _TmsCommonMiscProductName_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 6, 8),
    _TmsCommonMiscProductName_Type()
)
tmsCommonMiscProductName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmsCommonMiscProductName.setStatus("current")


class _TmsCommonMiscReset_Type(Integer32):
    """Custom type tmsCommonMiscReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("reset", 2),
          ("resetToDefaults", 3))
    )


_TmsCommonMiscReset_Type.__name__ = "Integer32"
_TmsCommonMiscReset_Object = MibScalar
tmsCommonMiscReset = _TmsCommonMiscReset_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 6, 9),
    _TmsCommonMiscReset_Type()
)
tmsCommonMiscReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmsCommonMiscReset.setStatus("current")


class _TmsCommonMiscTrapTest_Type(Integer32):
    """Custom type tmsCommonMiscTrapTest based on Integer32"""
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
        *(("authentication", 5),
          ("coldstart", 2),
          ("linkdown", 3),
          ("linkup", 4),
          ("noop", 1),
          ("tmsTestTrap", 6))
    )


_TmsCommonMiscTrapTest_Type.__name__ = "Integer32"
_TmsCommonMiscTrapTest_Object = MibScalar
tmsCommonMiscTrapTest = _TmsCommonMiscTrapTest_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 6, 10),
    _TmsCommonMiscTrapTest_Type()
)
tmsCommonMiscTrapTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmsCommonMiscTrapTest.setStatus("current")
_TmsCommonCommToView_ObjectIdentity = ObjectIdentity
tmsCommonCommToView = _TmsCommonCommToView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 7)
)
_TmsCommonCommunityToViewTable_Object = MibTable
tmsCommonCommunityToViewTable = _TmsCommonCommunityToViewTable_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 7, 1)
)
if mibBuilder.loadTexts:
    tmsCommonCommunityToViewTable.setStatus("current")
_TmsCommonCommunityToViewEntry_Object = MibTableRow
tmsCommonCommunityToViewEntry = _TmsCommonCommunityToViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 7, 1, 1)
)
tmsCommonCommunityToViewEntry.setIndexNames(
    (0, "TMS-COMMON-MIB", "tmsCommonComm2ViewIndex"),
)
if mibBuilder.loadTexts:
    tmsCommonCommunityToViewEntry.setStatus("current")


class _TmsCommonComm2ViewIndex_Type(Integer32):
    """Custom type tmsCommonComm2ViewIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TmsCommonComm2ViewIndex_Type.__name__ = "Integer32"
_TmsCommonComm2ViewIndex_Object = MibTableColumn
tmsCommonComm2ViewIndex = _TmsCommonComm2ViewIndex_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 7, 1, 1, 1),
    _TmsCommonComm2ViewIndex_Type()
)
tmsCommonComm2ViewIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmsCommonComm2ViewIndex.setStatus("current")


class _TmsCommonComm2ViewCommName_Type(DisplayString):
    """Custom type tmsCommonComm2ViewCommName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_TmsCommonComm2ViewCommName_Type.__name__ = "DisplayString"
_TmsCommonComm2ViewCommName_Object = MibTableColumn
tmsCommonComm2ViewCommName = _TmsCommonComm2ViewCommName_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 7, 1, 1, 2),
    _TmsCommonComm2ViewCommName_Type()
)
tmsCommonComm2ViewCommName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmsCommonComm2ViewCommName.setStatus("current")


class _TmsCommonComm2ViewViewName_Type(SnmpAdminString):
    """Custom type tmsCommonComm2ViewViewName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmsCommonComm2ViewViewName_Type.__name__ = "SnmpAdminString"
_TmsCommonComm2ViewViewName_Object = MibTableColumn
tmsCommonComm2ViewViewName = _TmsCommonComm2ViewViewName_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 7, 1, 1, 3),
    _TmsCommonComm2ViewViewName_Type()
)
tmsCommonComm2ViewViewName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmsCommonComm2ViewViewName.setStatus("current")


class _TmsCommonComm2ViewPermission_Type(Integer32):
    """Custom type tmsCommonComm2ViewPermission based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2))
    )


_TmsCommonComm2ViewPermission_Type.__name__ = "Integer32"
_TmsCommonComm2ViewPermission_Object = MibTableColumn
tmsCommonComm2ViewPermission = _TmsCommonComm2ViewPermission_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 7, 1, 1, 4),
    _TmsCommonComm2ViewPermission_Type()
)
tmsCommonComm2ViewPermission.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmsCommonComm2ViewPermission.setStatus("current")
_TmsCommonComm2ViewRowStatus_Type = RowStatus
_TmsCommonComm2ViewRowStatus_Object = MibTableColumn
tmsCommonComm2ViewRowStatus = _TmsCommonComm2ViewRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 7, 1, 1, 5),
    _TmsCommonComm2ViewRowStatus_Type()
)
tmsCommonComm2ViewRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmsCommonComm2ViewRowStatus.setStatus("current")
_TmsCommonIgmpSnoop_ObjectIdentity = ObjectIdentity
tmsCommonIgmpSnoop = _TmsCommonIgmpSnoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 8)
)
_TmsCommonIgmpSnoopEnabled_Type = TruthValue
_TmsCommonIgmpSnoopEnabled_Object = MibScalar
tmsCommonIgmpSnoopEnabled = _TmsCommonIgmpSnoopEnabled_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 8, 1),
    _TmsCommonIgmpSnoopEnabled_Type()
)
tmsCommonIgmpSnoopEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmsCommonIgmpSnoopEnabled.setStatus("current")
_TmsCommonIgmpSnoopAlerts_Type = TruthValue
_TmsCommonIgmpSnoopAlerts_Object = MibScalar
tmsCommonIgmpSnoopAlerts = _TmsCommonIgmpSnoopAlerts_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 8, 2),
    _TmsCommonIgmpSnoopAlerts_Type()
)
tmsCommonIgmpSnoopAlerts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmsCommonIgmpSnoopAlerts.setStatus("current")


class _TmsCommonIgmpSnoopAging_Type(Integer32):
    """Custom type tmsCommonIgmpSnoopAging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_TmsCommonIgmpSnoopAging_Type.__name__ = "Integer32"
_TmsCommonIgmpSnoopAging_Object = MibScalar
tmsCommonIgmpSnoopAging = _TmsCommonIgmpSnoopAging_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 8, 3),
    _TmsCommonIgmpSnoopAging_Type()
)
tmsCommonIgmpSnoopAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmsCommonIgmpSnoopAging.setStatus("current")
_TmsCommonIgmpSnoopTable_Object = MibTable
tmsCommonIgmpSnoopTable = _TmsCommonIgmpSnoopTable_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 8, 4)
)
if mibBuilder.loadTexts:
    tmsCommonIgmpSnoopTable.setStatus("current")
_TmsCommonIgmpSnoopEntry_Object = MibTableRow
tmsCommonIgmpSnoopEntry = _TmsCommonIgmpSnoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 8, 4, 1)
)
if mibBuilder.loadTexts:
    tmsCommonIgmpSnoopEntry.setStatus("current")
_TmsCommonIgmpSnoopEgressPorts_Type = PortList
_TmsCommonIgmpSnoopEgressPorts_Object = MibTableColumn
tmsCommonIgmpSnoopEgressPorts = _TmsCommonIgmpSnoopEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 8, 4, 1, 1),
    _TmsCommonIgmpSnoopEgressPorts_Type()
)
tmsCommonIgmpSnoopEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsCommonIgmpSnoopEgressPorts.setStatus("current")
_TmsCommonConformance_ObjectIdentity = ObjectIdentity
tmsCommonConformance = _TmsCommonConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 9)
)
_TmsCommonGroups_ObjectIdentity = ObjectIdentity
tmsCommonGroups = _TmsCommonGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 9, 1)
)
_TmsCommonCompliances_ObjectIdentity = ObjectIdentity
tmsCommonCompliances = _TmsCommonCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 9, 2)
)
dot1qStaticMulticastEntry.registerAugmentions(
    ("TMS-COMMON-MIB",
     "tmsCommonIgmpSnoopEntry")
)
tmsCommonIgmpSnoopEntry.setIndexNames(*dot1qStaticMulticastEntry.getIndexNames())

# Managed Objects groups

tmsCommonVerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 9, 1, 1)
)
tmsCommonVerGroup.setObjects(
      *(("TMS-COMMON-MIB", "tmsCommonVerMIBMajor"),
        ("TMS-COMMON-MIB", "tmsCommonVerMIBMinor"),
        ("TMS-COMMON-MIB", "tmsCommonVerBootSWMajor"),
        ("TMS-COMMON-MIB", "tmsCommonVerBootSWMinor"),
        ("TMS-COMMON-MIB", "tmsCommonVerAppSWMajor"),
        ("TMS-COMMON-MIB", "tmsCommonVerAppSWMinor"))
)
if mibBuilder.loadTexts:
    tmsCommonVerGroup.setStatus("current")

tmsCommonIPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 9, 1, 2)
)
tmsCommonIPGroup.setObjects(
      *(("TMS-COMMON-MIB", "tmsCommonIPMACAddr"),
        ("TMS-COMMON-MIB", "tmsCommonIPIpAddress"),
        ("TMS-COMMON-MIB", "tmsCommonIPGateAddress"),
        ("TMS-COMMON-MIB", "tmsCommonIPNetMask"),
        ("TMS-COMMON-MIB", "tmsCommonIPStatus"))
)
if mibBuilder.loadTexts:
    tmsCommonIPGroup.setStatus("current")

tmsCommonLoadGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 9, 1, 3)
)
tmsCommonLoadGroup.setObjects(
      *(("TMS-COMMON-MIB", "tmsCommonLoadTftpAddress"),
        ("TMS-COMMON-MIB", "tmsCommonLoadTftpFileName"),
        ("TMS-COMMON-MIB", "tmsCommonLoadType"),
        ("TMS-COMMON-MIB", "tmsCommonLoadExecute"),
        ("TMS-COMMON-MIB", "tmsCommonLoadExecuteStatus"))
)
if mibBuilder.loadTexts:
    tmsCommonLoadGroup.setStatus("current")

tmsCommonMiscGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 9, 1, 4)
)
tmsCommonMiscGroup.setObjects(
      *(("TMS-COMMON-MIB", "tmsCommonMiscSaveToNvm"),
        ("TMS-COMMON-MIB", "tmsCommonMiscSpanOnOff"),
        ("TMS-COMMON-MIB", "tmsCommonMiscBOOTPOnOff"),
        ("TMS-COMMON-MIB", "tmsCommonMiscDHCPOnOff"),
        ("TMS-COMMON-MIB", "tmsCommonMiscBaud"),
        ("TMS-COMMON-MIB", "tmsCommonMiscPassword"),
        ("TMS-COMMON-MIB", "tmsCommonMiscProductName"),
        ("TMS-COMMON-MIB", "tmsCommonMiscReset"),
        ("TMS-COMMON-MIB", "tmsCommonMiscTrapTest"))
)
if mibBuilder.loadTexts:
    tmsCommonMiscGroup.setStatus("current")

tmsCommonCommToViewGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 9, 1, 5)
)
tmsCommonCommToViewGroup.setObjects(
      *(("TMS-COMMON-MIB", "tmsCommonComm2ViewCommName"),
        ("TMS-COMMON-MIB", "tmsCommonComm2ViewViewName"),
        ("TMS-COMMON-MIB", "tmsCommonComm2ViewPermission"),
        ("TMS-COMMON-MIB", "tmsCommonComm2ViewRowStatus"))
)
if mibBuilder.loadTexts:
    tmsCommonCommToViewGroup.setStatus("current")

tmsCommonIgmpSnoopGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 9, 1, 6)
)
tmsCommonIgmpSnoopGroup.setObjects(
      *(("TMS-COMMON-MIB", "tmsCommonIgmpSnoopEnabled"),
        ("TMS-COMMON-MIB", "tmsCommonIgmpSnoopAlerts"),
        ("TMS-COMMON-MIB", "tmsCommonIgmpSnoopAging"),
        ("TMS-COMMON-MIB", "tmsCommonIgmpSnoopEgressPorts"))
)
if mibBuilder.loadTexts:
    tmsCommonIgmpSnoopGroup.setStatus("current")


# Notification objects

tmsCommonSnmpV2TestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 0, 1)
)
tmsCommonSnmpV2TestTrap.setObjects(
    ("TMS-COMMON-MIB", "tmsCommonMiscProductName")
)
if mibBuilder.loadTexts:
    tmsCommonSnmpV2TestTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

tmsCommonCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 9, 2, 1)
)
if mibBuilder.loadTexts:
    tmsCommonCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TMS-COMMON-MIB",
    **{"tmsCommonMib": tmsCommonMib,
       "tmsCommonNotify": tmsCommonNotify,
       "tmsCommonSnmpV2TestTrap": tmsCommonSnmpV2TestTrap,
       "tmsCommonVer": tmsCommonVer,
       "tmsCommonVerMIBMajor": tmsCommonVerMIBMajor,
       "tmsCommonVerMIBMinor": tmsCommonVerMIBMinor,
       "tmsCommonVerBootSWMajor": tmsCommonVerBootSWMajor,
       "tmsCommonVerBootSWMinor": tmsCommonVerBootSWMinor,
       "tmsCommonVerAppSWMajor": tmsCommonVerAppSWMajor,
       "tmsCommonVerAppSWMinor": tmsCommonVerAppSWMinor,
       "tmsCommonIP": tmsCommonIP,
       "tmsCommonIPMACAddr": tmsCommonIPMACAddr,
       "tmsCommonIPIpAddress": tmsCommonIPIpAddress,
       "tmsCommonIPGateAddress": tmsCommonIPGateAddress,
       "tmsCommonIPNetMask": tmsCommonIPNetMask,
       "tmsCommonIPStatus": tmsCommonIPStatus,
       "tmsCommonLoad": tmsCommonLoad,
       "tmsCommonLoadTftpAddress": tmsCommonLoadTftpAddress,
       "tmsCommonLoadTftpFileName": tmsCommonLoadTftpFileName,
       "tmsCommonLoadType": tmsCommonLoadType,
       "tmsCommonLoadExecute": tmsCommonLoadExecute,
       "tmsCommonLoadExecuteStatus": tmsCommonLoadExecuteStatus,
       "tmsCommonMisc": tmsCommonMisc,
       "tmsCommonMiscSaveToNvm": tmsCommonMiscSaveToNvm,
       "tmsCommonMiscSnmpSecurityOnOff": tmsCommonMiscSnmpSecurityOnOff,
       "tmsCommonMiscSpanOnOff": tmsCommonMiscSpanOnOff,
       "tmsCommonMiscBOOTPOnOff": tmsCommonMiscBOOTPOnOff,
       "tmsCommonMiscDHCPOnOff": tmsCommonMiscDHCPOnOff,
       "tmsCommonMiscBaud": tmsCommonMiscBaud,
       "tmsCommonMiscPassword": tmsCommonMiscPassword,
       "tmsCommonMiscProductName": tmsCommonMiscProductName,
       "tmsCommonMiscReset": tmsCommonMiscReset,
       "tmsCommonMiscTrapTest": tmsCommonMiscTrapTest,
       "tmsCommonCommToView": tmsCommonCommToView,
       "tmsCommonCommunityToViewTable": tmsCommonCommunityToViewTable,
       "tmsCommonCommunityToViewEntry": tmsCommonCommunityToViewEntry,
       "tmsCommonComm2ViewIndex": tmsCommonComm2ViewIndex,
       "tmsCommonComm2ViewCommName": tmsCommonComm2ViewCommName,
       "tmsCommonComm2ViewViewName": tmsCommonComm2ViewViewName,
       "tmsCommonComm2ViewPermission": tmsCommonComm2ViewPermission,
       "tmsCommonComm2ViewRowStatus": tmsCommonComm2ViewRowStatus,
       "tmsCommonIgmpSnoop": tmsCommonIgmpSnoop,
       "tmsCommonIgmpSnoopEnabled": tmsCommonIgmpSnoopEnabled,
       "tmsCommonIgmpSnoopAlerts": tmsCommonIgmpSnoopAlerts,
       "tmsCommonIgmpSnoopAging": tmsCommonIgmpSnoopAging,
       "tmsCommonIgmpSnoopTable": tmsCommonIgmpSnoopTable,
       "tmsCommonIgmpSnoopEntry": tmsCommonIgmpSnoopEntry,
       "tmsCommonIgmpSnoopEgressPorts": tmsCommonIgmpSnoopEgressPorts,
       "tmsCommonConformance": tmsCommonConformance,
       "tmsCommonGroups": tmsCommonGroups,
       "tmsCommonVerGroup": tmsCommonVerGroup,
       "tmsCommonIPGroup": tmsCommonIPGroup,
       "tmsCommonLoadGroup": tmsCommonLoadGroup,
       "tmsCommonMiscGroup": tmsCommonMiscGroup,
       "tmsCommonCommToViewGroup": tmsCommonCommToViewGroup,
       "tmsCommonIgmpSnoopGroup": tmsCommonIgmpSnoopGroup,
       "tmsCommonCompliances": tmsCommonCompliances,
       "tmsCommonCompliance": tmsCommonCompliance}
)
