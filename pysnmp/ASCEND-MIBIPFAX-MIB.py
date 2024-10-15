# SNMP MIB module (ASCEND-MIBIPFAX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBIPFAX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:44 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibipFaxProfile_ObjectIdentity = ObjectIdentity
mibipFaxProfile = _MibipFaxProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 84)
)
_MibipFaxProfileTable_Object = MibTable
mibipFaxProfileTable = _MibipFaxProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 84, 1)
)
if mibBuilder.loadTexts:
    mibipFaxProfileTable.setStatus("mandatory")
_MibipFaxProfileEntry_Object = MibTableRow
mibipFaxProfileEntry = _MibipFaxProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 84, 1, 1)
)
mibipFaxProfileEntry.setIndexNames(
    (0, "ASCEND-MIBIPFAX-MIB", "ipFaxProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibipFaxProfileEntry.setStatus("mandatory")
_IpFaxProfile_Index_o_Type = Integer32
_IpFaxProfile_Index_o_Object = MibScalar
ipFaxProfile_Index_o = _IpFaxProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 84, 1, 1, 1),
    _IpFaxProfile_Index_o_Type()
)
ipFaxProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFaxProfile_Index_o.setStatus("mandatory")


class _IpFaxProfile_IpFaxEnabled_Type(Integer32):
    """Custom type ipFaxProfile_IpFaxEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IpFaxProfile_IpFaxEnabled_Type.__name__ = "Integer32"
_IpFaxProfile_IpFaxEnabled_Object = MibScalar
ipFaxProfile_IpFaxEnabled = _IpFaxProfile_IpFaxEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 84, 1, 1, 2),
    _IpFaxProfile_IpFaxEnabled_Type()
)
ipFaxProfile_IpFaxEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFaxProfile_IpFaxEnabled.setStatus("mandatory")
_IpFaxProfile_OutgoingFaxPort_Type = Integer32
_IpFaxProfile_OutgoingFaxPort_Object = MibScalar
ipFaxProfile_OutgoingFaxPort = _IpFaxProfile_OutgoingFaxPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 84, 1, 1, 3),
    _IpFaxProfile_OutgoingFaxPort_Type()
)
ipFaxProfile_OutgoingFaxPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFaxProfile_OutgoingFaxPort.setStatus("mandatory")
_IpFaxProfile_ServerLogin_Type = DisplayString
_IpFaxProfile_ServerLogin_Object = MibScalar
ipFaxProfile_ServerLogin = _IpFaxProfile_ServerLogin_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 84, 1, 1, 4),
    _IpFaxProfile_ServerLogin_Type()
)
ipFaxProfile_ServerLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFaxProfile_ServerLogin.setStatus("mandatory")


class _IpFaxProfile_DialerType_Type(Integer32):
    """Custom type ipFaxProfile_DialerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atlas", 2),
          ("mitel", 1))
    )


_IpFaxProfile_DialerType_Type.__name__ = "Integer32"
_IpFaxProfile_DialerType_Object = MibScalar
ipFaxProfile_DialerType = _IpFaxProfile_DialerType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 84, 1, 1, 5),
    _IpFaxProfile_DialerType_Type()
)
ipFaxProfile_DialerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFaxProfile_DialerType.setStatus("mandatory")
_IpFaxProfile_ServerPassword_Type = DisplayString
_IpFaxProfile_ServerPassword_Object = MibScalar
ipFaxProfile_ServerPassword = _IpFaxProfile_ServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 84, 1, 1, 6),
    _IpFaxProfile_ServerPassword_Type()
)
ipFaxProfile_ServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFaxProfile_ServerPassword.setStatus("mandatory")
_IpFaxProfile_IncomingFaxPort_Type = Integer32
_IpFaxProfile_IncomingFaxPort_Object = MibScalar
ipFaxProfile_IncomingFaxPort = _IpFaxProfile_IncomingFaxPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 84, 1, 1, 7),
    _IpFaxProfile_IncomingFaxPort_Type()
)
ipFaxProfile_IncomingFaxPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFaxProfile_IncomingFaxPort.setStatus("mandatory")


class _IpFaxProfile_AllCallsAreFax_Type(Integer32):
    """Custom type ipFaxProfile_AllCallsAreFax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IpFaxProfile_AllCallsAreFax_Type.__name__ = "Integer32"
_IpFaxProfile_AllCallsAreFax_Object = MibScalar
ipFaxProfile_AllCallsAreFax = _IpFaxProfile_AllCallsAreFax_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 84, 1, 1, 8),
    _IpFaxProfile_AllCallsAreFax_Type()
)
ipFaxProfile_AllCallsAreFax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFaxProfile_AllCallsAreFax.setStatus("mandatory")


class _IpFaxProfile_FaxIncomingCallType_Type(Integer32):
    """Custom type ipFaxProfile_FaxIncomingCallType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("did", 2),
          ("redialer", 1))
    )


_IpFaxProfile_FaxIncomingCallType_Type.__name__ = "Integer32"
_IpFaxProfile_FaxIncomingCallType_Object = MibScalar
ipFaxProfile_FaxIncomingCallType = _IpFaxProfile_FaxIncomingCallType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 84, 1, 1, 9),
    _IpFaxProfile_FaxIncomingCallType_Type()
)
ipFaxProfile_FaxIncomingCallType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFaxProfile_FaxIncomingCallType.setStatus("mandatory")


class _IpFaxProfile_Action_o_Type(Integer32):
    """Custom type ipFaxProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_IpFaxProfile_Action_o_Type.__name__ = "Integer32"
_IpFaxProfile_Action_o_Object = MibScalar
ipFaxProfile_Action_o = _IpFaxProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 84, 1, 1, 10),
    _IpFaxProfile_Action_o_Type()
)
ipFaxProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFaxProfile_Action_o.setStatus("mandatory")
_MibipFaxProfile_FaxServersTable_Object = MibTable
mibipFaxProfile_FaxServersTable = _MibipFaxProfile_FaxServersTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 84, 2)
)
if mibBuilder.loadTexts:
    mibipFaxProfile_FaxServersTable.setStatus("mandatory")
_MibipFaxProfile_FaxServersEntry_Object = MibTableRow
mibipFaxProfile_FaxServersEntry = _MibipFaxProfile_FaxServersEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 84, 2, 1)
)
mibipFaxProfile_FaxServersEntry.setIndexNames(
    (0, "ASCEND-MIBIPFAX-MIB", "ipFaxProfile-FaxServers-Index-o"),
    (0, "ASCEND-MIBIPFAX-MIB", "ipFaxProfile-FaxServers-Index1-o"),
)
if mibBuilder.loadTexts:
    mibipFaxProfile_FaxServersEntry.setStatus("mandatory")
_IpFaxProfile_FaxServers_Index_o_Type = Integer32
_IpFaxProfile_FaxServers_Index_o_Object = MibScalar
ipFaxProfile_FaxServers_Index_o = _IpFaxProfile_FaxServers_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 84, 2, 1, 1),
    _IpFaxProfile_FaxServers_Index_o_Type()
)
ipFaxProfile_FaxServers_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFaxProfile_FaxServers_Index_o.setStatus("mandatory")
_IpFaxProfile_FaxServers_Index1_o_Type = Integer32
_IpFaxProfile_FaxServers_Index1_o_Object = MibScalar
ipFaxProfile_FaxServers_Index1_o = _IpFaxProfile_FaxServers_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 84, 2, 1, 2),
    _IpFaxProfile_FaxServers_Index1_o_Type()
)
ipFaxProfile_FaxServers_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFaxProfile_FaxServers_Index1_o.setStatus("mandatory")
_IpFaxProfile_FaxServers_Type = IpAddress
_IpFaxProfile_FaxServers_Object = MibScalar
ipFaxProfile_FaxServers = _IpFaxProfile_FaxServers_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 84, 2, 1, 3),
    _IpFaxProfile_FaxServers_Type()
)
ipFaxProfile_FaxServers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFaxProfile_FaxServers.setStatus("mandatory")
_MibipFaxProfile_FaxDidTable_Object = MibTable
mibipFaxProfile_FaxDidTable = _MibipFaxProfile_FaxDidTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 84, 3)
)
if mibBuilder.loadTexts:
    mibipFaxProfile_FaxDidTable.setStatus("mandatory")
_MibipFaxProfile_FaxDidEntry_Object = MibTableRow
mibipFaxProfile_FaxDidEntry = _MibipFaxProfile_FaxDidEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 84, 3, 1)
)
mibipFaxProfile_FaxDidEntry.setIndexNames(
    (0, "ASCEND-MIBIPFAX-MIB", "ipFaxProfile-FaxDid-Index-o"),
    (0, "ASCEND-MIBIPFAX-MIB", "ipFaxProfile-FaxDid-Index1-o"),
)
if mibBuilder.loadTexts:
    mibipFaxProfile_FaxDidEntry.setStatus("mandatory")
_IpFaxProfile_FaxDid_Index_o_Type = Integer32
_IpFaxProfile_FaxDid_Index_o_Object = MibScalar
ipFaxProfile_FaxDid_Index_o = _IpFaxProfile_FaxDid_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 84, 3, 1, 1),
    _IpFaxProfile_FaxDid_Index_o_Type()
)
ipFaxProfile_FaxDid_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFaxProfile_FaxDid_Index_o.setStatus("mandatory")
_IpFaxProfile_FaxDid_Index1_o_Type = Integer32
_IpFaxProfile_FaxDid_Index1_o_Object = MibScalar
ipFaxProfile_FaxDid_Index1_o = _IpFaxProfile_FaxDid_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 84, 3, 1, 2),
    _IpFaxProfile_FaxDid_Index1_o_Type()
)
ipFaxProfile_FaxDid_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFaxProfile_FaxDid_Index1_o.setStatus("mandatory")
_IpFaxProfile_FaxDid_Type = DisplayString
_IpFaxProfile_FaxDid_Object = MibScalar
ipFaxProfile_FaxDid = _IpFaxProfile_FaxDid_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 84, 3, 1, 3),
    _IpFaxProfile_FaxDid_Type()
)
ipFaxProfile_FaxDid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFaxProfile_FaxDid.setStatus("mandatory")
_MibipFaxProfile_FaxDnisTable_Object = MibTable
mibipFaxProfile_FaxDnisTable = _MibipFaxProfile_FaxDnisTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 84, 4)
)
if mibBuilder.loadTexts:
    mibipFaxProfile_FaxDnisTable.setStatus("mandatory")
_MibipFaxProfile_FaxDnisEntry_Object = MibTableRow
mibipFaxProfile_FaxDnisEntry = _MibipFaxProfile_FaxDnisEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 84, 4, 1)
)
mibipFaxProfile_FaxDnisEntry.setIndexNames(
    (0, "ASCEND-MIBIPFAX-MIB", "ipFaxProfile-FaxDnis-Index-o"),
    (0, "ASCEND-MIBIPFAX-MIB", "ipFaxProfile-FaxDnis-Index1-o"),
)
if mibBuilder.loadTexts:
    mibipFaxProfile_FaxDnisEntry.setStatus("mandatory")
_IpFaxProfile_FaxDnis_Index_o_Type = Integer32
_IpFaxProfile_FaxDnis_Index_o_Object = MibScalar
ipFaxProfile_FaxDnis_Index_o = _IpFaxProfile_FaxDnis_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 84, 4, 1, 1),
    _IpFaxProfile_FaxDnis_Index_o_Type()
)
ipFaxProfile_FaxDnis_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFaxProfile_FaxDnis_Index_o.setStatus("mandatory")
_IpFaxProfile_FaxDnis_Index1_o_Type = Integer32
_IpFaxProfile_FaxDnis_Index1_o_Object = MibScalar
ipFaxProfile_FaxDnis_Index1_o = _IpFaxProfile_FaxDnis_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 84, 4, 1, 2),
    _IpFaxProfile_FaxDnis_Index1_o_Type()
)
ipFaxProfile_FaxDnis_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFaxProfile_FaxDnis_Index1_o.setStatus("mandatory")
_IpFaxProfile_FaxDnis_Type = DisplayString
_IpFaxProfile_FaxDnis_Object = MibScalar
ipFaxProfile_FaxDnis = _IpFaxProfile_FaxDnis_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 84, 4, 1, 3),
    _IpFaxProfile_FaxDnis_Type()
)
ipFaxProfile_FaxDnis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFaxProfile_FaxDnis.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBIPFAX-MIB",
    **{"DisplayString": DisplayString,
       "mibipFaxProfile": mibipFaxProfile,
       "mibipFaxProfileTable": mibipFaxProfileTable,
       "mibipFaxProfileEntry": mibipFaxProfileEntry,
       "ipFaxProfile-Index-o": ipFaxProfile_Index_o,
       "ipFaxProfile-IpFaxEnabled": ipFaxProfile_IpFaxEnabled,
       "ipFaxProfile-OutgoingFaxPort": ipFaxProfile_OutgoingFaxPort,
       "ipFaxProfile-ServerLogin": ipFaxProfile_ServerLogin,
       "ipFaxProfile-DialerType": ipFaxProfile_DialerType,
       "ipFaxProfile-ServerPassword": ipFaxProfile_ServerPassword,
       "ipFaxProfile-IncomingFaxPort": ipFaxProfile_IncomingFaxPort,
       "ipFaxProfile-AllCallsAreFax": ipFaxProfile_AllCallsAreFax,
       "ipFaxProfile-FaxIncomingCallType": ipFaxProfile_FaxIncomingCallType,
       "ipFaxProfile-Action-o": ipFaxProfile_Action_o,
       "mibipFaxProfile-FaxServersTable": mibipFaxProfile_FaxServersTable,
       "mibipFaxProfile-FaxServersEntry": mibipFaxProfile_FaxServersEntry,
       "ipFaxProfile-FaxServers-Index-o": ipFaxProfile_FaxServers_Index_o,
       "ipFaxProfile-FaxServers-Index1-o": ipFaxProfile_FaxServers_Index1_o,
       "ipFaxProfile-FaxServers": ipFaxProfile_FaxServers,
       "mibipFaxProfile-FaxDidTable": mibipFaxProfile_FaxDidTable,
       "mibipFaxProfile-FaxDidEntry": mibipFaxProfile_FaxDidEntry,
       "ipFaxProfile-FaxDid-Index-o": ipFaxProfile_FaxDid_Index_o,
       "ipFaxProfile-FaxDid-Index1-o": ipFaxProfile_FaxDid_Index1_o,
       "ipFaxProfile-FaxDid": ipFaxProfile_FaxDid,
       "mibipFaxProfile-FaxDnisTable": mibipFaxProfile_FaxDnisTable,
       "mibipFaxProfile-FaxDnisEntry": mibipFaxProfile_FaxDnisEntry,
       "ipFaxProfile-FaxDnis-Index-o": ipFaxProfile_FaxDnis_Index_o,
       "ipFaxProfile-FaxDnis-Index1-o": ipFaxProfile_FaxDnis_Index1_o,
       "ipFaxProfile-FaxDnis": ipFaxProfile_FaxDnis}
)
