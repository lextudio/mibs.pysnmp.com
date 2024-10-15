# SNMP MIB module (NSMAIL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NSMAIL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:34 2024
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
 TextualConvention,
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeInterval")


# MODULE-IDENTITY

nsmail = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1450, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Netscape_ObjectIdentity = ObjectIdentity
netscape = _Netscape_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1450)
)
_NsmailEntityInfo_ObjectIdentity = ObjectIdentity
nsmailEntityInfo = _NsmailEntityInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1450, 5, 1)
)


class _NsmailEntityDescr_Type(DisplayString):
    """Custom type nsmailEntityDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsmailEntityDescr_Type.__name__ = "DisplayString"
_NsmailEntityDescr_Object = MibScalar
nsmailEntityDescr = _NsmailEntityDescr_Object(
    (1, 3, 6, 1, 4, 1, 1450, 5, 1, 1),
    _NsmailEntityDescr_Type()
)
nsmailEntityDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsmailEntityDescr.setStatus("mandatory")


class _NsmailEntityVers_Type(DisplayString):
    """Custom type nsmailEntityVers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsmailEntityVers_Type.__name__ = "DisplayString"
_NsmailEntityVers_Object = MibScalar
nsmailEntityVers = _NsmailEntityVers_Object(
    (1, 3, 6, 1, 4, 1, 1450, 5, 1, 2),
    _NsmailEntityVers_Type()
)
nsmailEntityVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsmailEntityVers.setStatus("mandatory")


class _NsmailEntityOrg_Type(DisplayString):
    """Custom type nsmailEntityOrg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsmailEntityOrg_Type.__name__ = "DisplayString"
_NsmailEntityOrg_Object = MibScalar
nsmailEntityOrg = _NsmailEntityOrg_Object(
    (1, 3, 6, 1, 4, 1, 1450, 5, 1, 3),
    _NsmailEntityOrg_Type()
)
nsmailEntityOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsmailEntityOrg.setStatus("mandatory")


class _NsmailEntityLocation_Type(DisplayString):
    """Custom type nsmailEntityLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsmailEntityLocation_Type.__name__ = "DisplayString"
_NsmailEntityLocation_Object = MibScalar
nsmailEntityLocation = _NsmailEntityLocation_Object(
    (1, 3, 6, 1, 4, 1, 1450, 5, 1, 4),
    _NsmailEntityLocation_Type()
)
nsmailEntityLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsmailEntityLocation.setStatus("mandatory")


class _NsmailEntityContact_Type(DisplayString):
    """Custom type nsmailEntityContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsmailEntityContact_Type.__name__ = "DisplayString"
_NsmailEntityContact_Object = MibScalar
nsmailEntityContact = _NsmailEntityContact_Object(
    (1, 3, 6, 1, 4, 1, 1450, 5, 1, 5),
    _NsmailEntityContact_Type()
)
nsmailEntityContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsmailEntityContact.setStatus("mandatory")


class _NsmailEntityName_Type(DisplayString):
    """Custom type nsmailEntityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsmailEntityName_Type.__name__ = "DisplayString"
_NsmailEntityName_Object = MibScalar
nsmailEntityName = _NsmailEntityName_Object(
    (1, 3, 6, 1, 4, 1, 1450, 5, 1, 6),
    _NsmailEntityName_Type()
)
nsmailEntityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsmailEntityName.setStatus("mandatory")
_MtaTable_Object = MibTable
mtaTable = _MtaTable_Object(
    (1, 3, 6, 1, 4, 1, 1450, 5, 2)
)
if mibBuilder.loadTexts:
    mtaTable.setStatus("mandatory")
_MtaEntry_Object = MibTableRow
mtaEntry = _MtaEntry_Object(
    (1, 3, 6, 1, 4, 1, 1450, 5, 2, 1)
)
mtaEntry.setIndexNames(
    (0, "NSMAIL-MIB", "mtaId"),
)
if mibBuilder.loadTexts:
    mtaEntry.setStatus("mandatory")
_MtaReceivedMessages_Type = Counter32
_MtaReceivedMessages_Object = MibTableColumn
mtaReceivedMessages = _MtaReceivedMessages_Object(
    (1, 3, 6, 1, 4, 1, 1450, 5, 2, 1, 1),
    _MtaReceivedMessages_Type()
)
mtaReceivedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaReceivedMessages.setStatus("mandatory")
_MtaStoredMessages_Type = Gauge32
_MtaStoredMessages_Object = MibTableColumn
mtaStoredMessages = _MtaStoredMessages_Object(
    (1, 3, 6, 1, 4, 1, 1450, 5, 2, 1, 2),
    _MtaStoredMessages_Type()
)
mtaStoredMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaStoredMessages.setStatus("mandatory")
_MtaTransmittedMessages_Type = Counter32
_MtaTransmittedMessages_Object = MibTableColumn
mtaTransmittedMessages = _MtaTransmittedMessages_Object(
    (1, 3, 6, 1, 4, 1, 1450, 5, 2, 1, 3),
    _MtaTransmittedMessages_Type()
)
mtaTransmittedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaTransmittedMessages.setStatus("mandatory")
_MtaReceivedVolume_Type = Counter32
_MtaReceivedVolume_Object = MibTableColumn
mtaReceivedVolume = _MtaReceivedVolume_Object(
    (1, 3, 6, 1, 4, 1, 1450, 5, 2, 1, 4),
    _MtaReceivedVolume_Type()
)
mtaReceivedVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaReceivedVolume.setStatus("mandatory")
_MtaStoredVolume_Type = Gauge32
_MtaStoredVolume_Object = MibTableColumn
mtaStoredVolume = _MtaStoredVolume_Object(
    (1, 3, 6, 1, 4, 1, 1450, 5, 2, 1, 5),
    _MtaStoredVolume_Type()
)
mtaStoredVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaStoredVolume.setStatus("mandatory")
_MtaTransmittedVolume_Type = Counter32
_MtaTransmittedVolume_Object = MibTableColumn
mtaTransmittedVolume = _MtaTransmittedVolume_Object(
    (1, 3, 6, 1, 4, 1, 1450, 5, 2, 1, 6),
    _MtaTransmittedVolume_Type()
)
mtaTransmittedVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaTransmittedVolume.setStatus("mandatory")
_MtaReceivedRecipients_Type = Counter32
_MtaReceivedRecipients_Object = MibTableColumn
mtaReceivedRecipients = _MtaReceivedRecipients_Object(
    (1, 3, 6, 1, 4, 1, 1450, 5, 2, 1, 7),
    _MtaReceivedRecipients_Type()
)
mtaReceivedRecipients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaReceivedRecipients.setStatus("mandatory")
_MtaStoredRecipients_Type = Gauge32
_MtaStoredRecipients_Object = MibTableColumn
mtaStoredRecipients = _MtaStoredRecipients_Object(
    (1, 3, 6, 1, 4, 1, 1450, 5, 2, 1, 8),
    _MtaStoredRecipients_Type()
)
mtaStoredRecipients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaStoredRecipients.setStatus("mandatory")
_MtaTransmittedRecipients_Type = Counter32
_MtaTransmittedRecipients_Object = MibTableColumn
mtaTransmittedRecipients = _MtaTransmittedRecipients_Object(
    (1, 3, 6, 1, 4, 1, 1450, 5, 2, 1, 9),
    _MtaTransmittedRecipients_Type()
)
mtaTransmittedRecipients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaTransmittedRecipients.setStatus("mandatory")
_MtaId_Type = Integer32
_MtaId_Object = MibTableColumn
mtaId = _MtaId_Object(
    (1, 3, 6, 1, 4, 1, 1450, 5, 2, 1, 10),
    _MtaId_Type()
)
mtaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaId.setStatus("mandatory")

# Managed Objects groups


# Notification objects

nsMailServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1450, 0, 5001)
)
nsMailServerDown.setObjects(
      *(("NSMAIL-MIB", "nsmailEntityDescr"),
        ("NSMAIL-MIB", "nsmailEntityVers"),
        ("NSMAIL-MIB", "nsmailEntityLocation"),
        ("NSMAIL-MIB", "nsmailEntityContact"))
)
if mibBuilder.loadTexts:
    nsMailServerDown.setStatus(
        ""
    )

nsMailServerStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1450, 0, 5002)
)
nsMailServerStart.setObjects(
      *(("NSMAIL-MIB", "nsmailEntityDescr"),
        ("NSMAIL-MIB", "nsmailEntityVers"),
        ("NSMAIL-MIB", "nsmailEntityLocation"))
)
if mibBuilder.loadTexts:
    nsMailServerStart.setStatus(
        ""
    )

nsMailServerNoResponse = NotificationType(
    (1, 3, 6, 1, 4, 1, 1450, 0, 5003)
)
nsMailServerNoResponse.setObjects(
      *(("NSMAIL-MIB", "nsmailEntityDescr"),
        ("NSMAIL-MIB", "nsmailEntityVers"),
        ("NSMAIL-MIB", "nsmailEntityLocation"),
        ("NSMAIL-MIB", "nsmailEntityContact"))
)
if mibBuilder.loadTexts:
    nsMailServerNoResponse.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSMAIL-MIB",
    **{"netscape": netscape,
       "nsMailServerDown": nsMailServerDown,
       "nsMailServerStart": nsMailServerStart,
       "nsMailServerNoResponse": nsMailServerNoResponse,
       "nsmail": nsmail,
       "nsmailEntityInfo": nsmailEntityInfo,
       "nsmailEntityDescr": nsmailEntityDescr,
       "nsmailEntityVers": nsmailEntityVers,
       "nsmailEntityOrg": nsmailEntityOrg,
       "nsmailEntityLocation": nsmailEntityLocation,
       "nsmailEntityContact": nsmailEntityContact,
       "nsmailEntityName": nsmailEntityName,
       "mtaTable": mtaTable,
       "mtaEntry": mtaEntry,
       "mtaReceivedMessages": mtaReceivedMessages,
       "mtaStoredMessages": mtaStoredMessages,
       "mtaTransmittedMessages": mtaTransmittedMessages,
       "mtaReceivedVolume": mtaReceivedVolume,
       "mtaStoredVolume": mtaStoredVolume,
       "mtaTransmittedVolume": mtaTransmittedVolume,
       "mtaReceivedRecipients": mtaReceivedRecipients,
       "mtaStoredRecipients": mtaStoredRecipients,
       "mtaTransmittedRecipients": mtaTransmittedRecipients,
       "mtaId": mtaId}
)
