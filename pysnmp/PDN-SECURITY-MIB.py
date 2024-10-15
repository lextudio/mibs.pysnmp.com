# SNMP MIB module (PDN-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-SECURITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:05 2024
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

(pdn_security,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-security")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _DevSecurityMgrValidation_Type(Integer32):
    """Custom type devSecurityMgrValidation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_DevSecurityMgrValidation_Type.__name__ = "Integer32"
_DevSecurityMgrValidation_Object = MibScalar
devSecurityMgrValidation = _DevSecurityMgrValidation_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 8, 1),
    _DevSecurityMgrValidation_Type()
)
devSecurityMgrValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devSecurityMgrValidation.setStatus("mandatory")
_DevSecurityMgrMaxNumber_Type = Integer32
_DevSecurityMgrMaxNumber_Object = MibScalar
devSecurityMgrMaxNumber = _DevSecurityMgrMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 8, 2),
    _DevSecurityMgrMaxNumber_Type()
)
devSecurityMgrMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devSecurityMgrMaxNumber.setStatus("mandatory")
_DevSecurityMgrCurrentNumber_Type = Integer32
_DevSecurityMgrCurrentNumber_Object = MibScalar
devSecurityMgrCurrentNumber = _DevSecurityMgrCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 8, 3),
    _DevSecurityMgrCurrentNumber_Type()
)
devSecurityMgrCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devSecurityMgrCurrentNumber.setStatus("mandatory")
_DevSecurityMgrTable_Object = MibTable
devSecurityMgrTable = _DevSecurityMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 8, 4)
)
if mibBuilder.loadTexts:
    devSecurityMgrTable.setStatus("mandatory")
_DevSecurityMgrEntry_Object = MibTableRow
devSecurityMgrEntry = _DevSecurityMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 8, 4, 1)
)
devSecurityMgrEntry.setIndexNames(
    (0, "PDN-SECURITY-MIB", "devSecurityMgrIpAddress"),
)
if mibBuilder.loadTexts:
    devSecurityMgrEntry.setStatus("mandatory")
_DevSecurityMgrIpAddress_Type = IpAddress
_DevSecurityMgrIpAddress_Object = MibTableColumn
devSecurityMgrIpAddress = _DevSecurityMgrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 8, 4, 1, 1),
    _DevSecurityMgrIpAddress_Type()
)
devSecurityMgrIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devSecurityMgrIpAddress.setStatus("mandatory")


class _DevSecurityMgrAccess_Type(Integer32):
    """Custom type devSecurityMgrAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("read", 1),
          ("readWrite", 2))
    )


_DevSecurityMgrAccess_Type.__name__ = "Integer32"
_DevSecurityMgrAccess_Object = MibTableColumn
devSecurityMgrAccess = _DevSecurityMgrAccess_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 8, 4, 1, 2),
    _DevSecurityMgrAccess_Type()
)
devSecurityMgrAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devSecurityMgrAccess.setStatus("mandatory")
_NewSecurityMgrTable_Object = MibTable
newSecurityMgrTable = _NewSecurityMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 8, 5)
)
if mibBuilder.loadTexts:
    newSecurityMgrTable.setStatus("mandatory")
_NewSecurityMgrEntry_Object = MibTableRow
newSecurityMgrEntry = _NewSecurityMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 8, 5, 1)
)
newSecurityMgrEntry.setIndexNames(
    (0, "PDN-SECURITY-MIB", "newSecurityMgrIpAddress"),
)
if mibBuilder.loadTexts:
    newSecurityMgrEntry.setStatus("mandatory")
_NewSecurityMgrIpAddress_Type = IpAddress
_NewSecurityMgrIpAddress_Object = MibTableColumn
newSecurityMgrIpAddress = _NewSecurityMgrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 8, 5, 1, 1),
    _NewSecurityMgrIpAddress_Type()
)
newSecurityMgrIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newSecurityMgrIpAddress.setStatus("mandatory")


class _NewSecurityMgrAccess_Type(Integer32):
    """Custom type newSecurityMgrAccess based on Integer32"""
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
        *(("noAccess", 3),
          ("read", 1),
          ("readWrite", 2),
          ("telnetNoAccess", 4),
          ("telnetRead", 5),
          ("telnetReadWrite", 6))
    )


_NewSecurityMgrAccess_Type.__name__ = "Integer32"
_NewSecurityMgrAccess_Object = MibTableColumn
newSecurityMgrAccess = _NewSecurityMgrAccess_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 8, 5, 1, 2),
    _NewSecurityMgrAccess_Type()
)
newSecurityMgrAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newSecurityMgrAccess.setStatus("mandatory")
_NewSecurityMgrSubnetMask_Type = IpAddress
_NewSecurityMgrSubnetMask_Object = MibTableColumn
newSecurityMgrSubnetMask = _NewSecurityMgrSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 8, 5, 1, 3),
    _NewSecurityMgrSubnetMask_Type()
)
newSecurityMgrSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newSecurityMgrSubnetMask.setStatus("mandatory")


class _DevSecurityTelnetSourceValidation_Type(Integer32):
    """Custom type devSecurityTelnetSourceValidation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_DevSecurityTelnetSourceValidation_Type.__name__ = "Integer32"
_DevSecurityTelnetSourceValidation_Object = MibScalar
devSecurityTelnetSourceValidation = _DevSecurityTelnetSourceValidation_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 8, 6),
    _DevSecurityTelnetSourceValidation_Type()
)
devSecurityTelnetSourceValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devSecurityTelnetSourceValidation.setStatus("mandatory")


class _DevSecurityFtpSourceValidation_Type(Integer32):
    """Custom type devSecurityFtpSourceValidation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_DevSecurityFtpSourceValidation_Type.__name__ = "Integer32"
_DevSecurityFtpSourceValidation_Object = MibScalar
devSecurityFtpSourceValidation = _DevSecurityFtpSourceValidation_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 8, 7),
    _DevSecurityFtpSourceValidation_Type()
)
devSecurityFtpSourceValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devSecurityFtpSourceValidation.setStatus("mandatory")
_SecurityMgrTable_Object = MibTable
securityMgrTable = _SecurityMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 8, 8)
)
if mibBuilder.loadTexts:
    securityMgrTable.setStatus("mandatory")
_SecurityMgrEntry_Object = MibTableRow
securityMgrEntry = _SecurityMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 8, 8, 1)
)
securityMgrEntry.setIndexNames(
    (0, "PDN-SECURITY-MIB", "securityMgrIpAddress"),
    (0, "PDN-SECURITY-MIB", "securityMgrSubnetMask"),
)
if mibBuilder.loadTexts:
    securityMgrEntry.setStatus("mandatory")
_SecurityMgrIpAddress_Type = IpAddress
_SecurityMgrIpAddress_Object = MibTableColumn
securityMgrIpAddress = _SecurityMgrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 8, 8, 1, 1),
    _SecurityMgrIpAddress_Type()
)
securityMgrIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityMgrIpAddress.setStatus("mandatory")
_SecurityMgrSubnetMask_Type = IpAddress
_SecurityMgrSubnetMask_Object = MibTableColumn
securityMgrSubnetMask = _SecurityMgrSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 8, 8, 1, 2),
    _SecurityMgrSubnetMask_Type()
)
securityMgrSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityMgrSubnetMask.setStatus("mandatory")


class _SecurityMgrSnmpAccess_Type(Integer32):
    """Custom type securityMgrSnmpAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAccess", 3),
          ("readOnly", 1),
          ("readWrite", 2))
    )


_SecurityMgrSnmpAccess_Type.__name__ = "Integer32"
_SecurityMgrSnmpAccess_Object = MibTableColumn
securityMgrSnmpAccess = _SecurityMgrSnmpAccess_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 8, 8, 1, 3),
    _SecurityMgrSnmpAccess_Type()
)
securityMgrSnmpAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityMgrSnmpAccess.setStatus("mandatory")


class _SecurityMgrTelnetAccess_Type(Integer32):
    """Custom type securityMgrTelnetAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_SecurityMgrTelnetAccess_Type.__name__ = "Integer32"
_SecurityMgrTelnetAccess_Object = MibTableColumn
securityMgrTelnetAccess = _SecurityMgrTelnetAccess_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 8, 8, 1, 4),
    _SecurityMgrTelnetAccess_Type()
)
securityMgrTelnetAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityMgrTelnetAccess.setStatus("mandatory")


class _SecurityMgrFtpAccess_Type(Integer32):
    """Custom type securityMgrFtpAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_SecurityMgrFtpAccess_Type.__name__ = "Integer32"
_SecurityMgrFtpAccess_Object = MibTableColumn
securityMgrFtpAccess = _SecurityMgrFtpAccess_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 8, 8, 1, 5),
    _SecurityMgrFtpAccess_Type()
)
securityMgrFtpAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityMgrFtpAccess.setStatus("mandatory")
_SecurityMgrRowStatus_Type = RowStatus
_SecurityMgrRowStatus_Object = MibTableColumn
securityMgrRowStatus = _SecurityMgrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 8, 8, 1, 6),
    _SecurityMgrRowStatus_Type()
)
securityMgrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityMgrRowStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-SECURITY-MIB",
    **{"devSecurityMgrValidation": devSecurityMgrValidation,
       "devSecurityMgrMaxNumber": devSecurityMgrMaxNumber,
       "devSecurityMgrCurrentNumber": devSecurityMgrCurrentNumber,
       "devSecurityMgrTable": devSecurityMgrTable,
       "devSecurityMgrEntry": devSecurityMgrEntry,
       "devSecurityMgrIpAddress": devSecurityMgrIpAddress,
       "devSecurityMgrAccess": devSecurityMgrAccess,
       "newSecurityMgrTable": newSecurityMgrTable,
       "newSecurityMgrEntry": newSecurityMgrEntry,
       "newSecurityMgrIpAddress": newSecurityMgrIpAddress,
       "newSecurityMgrAccess": newSecurityMgrAccess,
       "newSecurityMgrSubnetMask": newSecurityMgrSubnetMask,
       "devSecurityTelnetSourceValidation": devSecurityTelnetSourceValidation,
       "devSecurityFtpSourceValidation": devSecurityFtpSourceValidation,
       "securityMgrTable": securityMgrTable,
       "securityMgrEntry": securityMgrEntry,
       "securityMgrIpAddress": securityMgrIpAddress,
       "securityMgrSubnetMask": securityMgrSubnetMask,
       "securityMgrSnmpAccess": securityMgrSnmpAccess,
       "securityMgrTelnetAccess": securityMgrTelnetAccess,
       "securityMgrFtpAccess": securityMgrFtpAccess,
       "securityMgrRowStatus": securityMgrRowStatus}
)
